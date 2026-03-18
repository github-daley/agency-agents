"""
bot.py — Main async bot loop.

Orchestrates: scan → signal → risk check → execute → log → settle → dashboard
"""

import asyncio
import json
import logging
import time
from typing import Optional, Union

import httpx

from .config import Config
from .market_scanner import Market, fetch_markets, GAMMA_API
from .monitor import Monitor
from .paper_trader import FillResult, PaperTrader
from .risk import RiskState
from .sizer import OrderIntent, build_order_intents, total_intent_usdc

logger = logging.getLogger(__name__)

_SETTLE_TIMEOUT = httpx.Timeout(10.0)


class PolymarketLPBot:
    """
    LP Seeding Bot that replicates the reverse-engineered strategy:
      1. Scan all active markets passing the liquidity filter
      2. For each market, generate two-sided BUY intents (Up + Down)
         using the price-proportional sizing rule
      3. Check risk gates before each order
      4. Execute orders (paper or live)
      5. Settle resolved positions (check Gamma API for outcomes)
      6. Log fills and print dashboard
    """

    def __init__(
        self,
        cfg: Config,
        executor: Union[PaperTrader, "LiveExecutor"],  # noqa: F821
        risk: RiskState,
        monitor: Monitor,
    ) -> None:
        self.cfg      = cfg
        self.executor = executor
        self.risk     = risk
        self.monitor  = monitor
        self._running = False

    async def run_once(self) -> tuple[int, int, int, dict]:
        """
        Execute one full scan-and-trade cycle.
        Returns (markets_scanned, intents_generated, fills_executed, market_prices).
        """
        # 1 — Fetch qualifying markets
        try:
            markets = await fetch_markets(self.cfg)
        except Exception as exc:
            logger.error("Market scan failed: %s", exc)
            return 0, 0, 0, {}

        intents_generated = 0
        fills_executed    = 0
        market_prices: dict[str, dict[str, float]] = {}

        for market in markets:
            if self.risk.halted:
                logger.warning("Bot halted — skipping remaining markets")
                break

            market_prices[market.id] = {
                "Up":   market.up_price,
                "Down": market.down_price,
            }

            intents = build_order_intents(
                market=market,
                cfg=self.cfg,
                exposure_up_usdc=self.risk.exposure_for(market.id, "Up"),
                exposure_down_usdc=self.risk.exposure_for(market.id, "Down"),
            )

            if not intents:
                continue

            intents_generated += len(intents)
            fills = await self._execute_intents(intents)
            fills_executed += len([f for f in fills if f.success])
            self.monitor.log_fills(fills)

            await asyncio.sleep(0.1)

        return len(markets), intents_generated, fills_executed, market_prices

    async def _execute_intents(self, intents: list[OrderIntent]) -> list[FillResult]:
        fills = []
        for intent in intents:
            if self.risk.halted:
                break
            fill = await self.executor.execute_buy(intent)
            fills.append(fill)
        return fills

    async def _settle_closed_positions(self) -> int:
        """
        Check all open positions where the market end_time has passed.
        Query the Gamma API to determine the winning outcome and settle.
        Returns number of positions settled.
        """
        now = time.time()
        settled_count = 0
        to_remove: list[str] = []

        for market_id, end_time in list(self.risk.market_end_times.items()):
            # Only check markets that have closed (with a 10s grace period)
            if end_time > now - 10:
                continue
            if market_id not in self.risk.positions:
                to_remove.append(market_id)
                continue

            winner = await self._fetch_market_outcome(market_id)
            if winner is None:
                # Not yet resolved — try again next cycle
                continue

            question = self.risk.market_questions.get(market_id, "")
            for outcome, rec in list(self.risk.positions[market_id].items()):
                if rec.tokens_held <= 0:
                    continue

                won = (
                    (outcome == "Up"   and winner in ("Yes", "Up",   "YES", "UP"))   or
                    (outcome == "Down" and winner in ("No",  "Down", "NO",  "DOWN"))
                )
                payout_price = 1.0 if won else 0.0

                fill = await self.executor.settle_position(
                    market_id=market_id,
                    question=question,
                    outcome=outcome,
                    tokens=rec.tokens_held,
                    payout_price=payout_price,
                )
                fill.market_end_ts = end_time
                self.monitor.log_fill(fill)
                settled_count += 1

            to_remove.append(market_id)

        for mid in to_remove:
            self.risk.market_end_times.pop(mid, None)

        return settled_count

    async def _fetch_market_outcome(self, market_id: str) -> Optional[str]:
        """
        Query Gamma API to check if a market has resolved.
        Returns the winner string (e.g. "Yes", "No") or None if not yet resolved.
        """
        try:
            async with httpx.AsyncClient(timeout=_SETTLE_TIMEOUT) as client:
                resp = await client.get(
                    f"{GAMMA_API}/markets",
                    params={"id": market_id},
                )
                if resp.status_code != 200:
                    return None
                data = resp.json()
                raw = data[0] if isinstance(data, list) and data else data
                if not isinstance(raw, dict):
                    return None

                # Market is settled if active=false or resolved=true
                is_resolved = raw.get("resolved", False) or not raw.get("active", True)
                if not is_resolved:
                    return None

                # Try winner field first
                winner = raw.get("winner") or raw.get("outcome")
                if winner:
                    return str(winner)

                # Fall back to outcome prices: winner has price ≈ 1.0
                outcome_prices = raw.get("outcomePrices", [])
                if isinstance(outcome_prices, str):
                    outcome_prices = json.loads(outcome_prices)
                outcomes = raw.get("outcomes", ["Yes", "No"])
                if isinstance(outcomes, str):
                    outcomes = json.loads(outcomes)
                for i, p in enumerate(outcome_prices):
                    if float(p) >= 0.99 and i < len(outcomes):
                        return str(outcomes[i])

        except Exception as exc:
            logger.debug("Outcome fetch failed for %s: %s", market_id, exc)
        return None

    async def run(self) -> None:
        """Main loop: scan → trade → settle → sleep → repeat."""
        self._running = True
        logger.info("Bot started in %s mode", self.cfg.mode.upper())

        while self._running:
            if self.risk.halted:
                logger.critical("Bot halted. Stopping loop.")
                break

            markets_scanned, intents_gen, fills_exec, prices = await self.run_once()

            # Settle any positions whose markets have now closed
            settled = await self._settle_closed_positions()
            if settled:
                logger.info("Settled %d position(s) this cycle", settled)

            self.monitor.print_dashboard(
                markets_scanned=markets_scanned,
                intents_generated=intents_gen,
                fills_this_cycle=fills_exec,
                market_prices=prices,
            )

            await asyncio.sleep(self.cfg.scan_interval_sec)

    def stop(self) -> None:
        self._running = False
