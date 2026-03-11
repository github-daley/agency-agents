"""
options_selector_additions.py — TarsierAlpha v2
================================================
Add these functions to options_selector.py.

Also make these two edits to EXISTING functions:

1. In save_option_candidate(), change the hardcoded option_type='call' to
   accept a parameter. See the modified version below.

2. In get_options_chain_yfinance(), the 'puts' key is already populated
   (chain.puts) — no change needed there.
"""

import logging
import traceback
import json
from datetime import datetime

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# REPLACEMENT for save_option_candidate()
# (only change: option_type is now a parameter instead of hardcoded 'call')
# ─────────────────────────────────────────────────────────────────────────────

def save_option_candidate(candidate, stock, option_data, is_recommended=False,
                          reason='', option_type='call'):
    """
    REPLACE the existing save_option_candidate() with this version.
    The only change is `option_type` is now a parameter (default 'call').
    """
    from models import db, OptionCandidate
    try:
        strike_val = float(option_data['strike'])
        dte_val = int(option_data['dte'])
        exp_date = option_data['expiration']
        bid_val = float(option_data.get('bid', 0) or 0)
        ask_val = float(option_data.get('ask', 0) or 0)
        delta_val = float(option_data.get('delta', 0) or 0)
        spread_val = float(option_data.get('spread_pct', 0) or 0)
        oi_val = int(option_data.get('open_interest', 0) or 0)
        vol_val = int(option_data.get('volume', 0) or 0)
        iv_val = float(option_data.get('iv', 0) or 0)
        target_ret = float(option_data.get('target_return', 0) or 0)

        oc = OptionCandidate(
            candidate_id=candidate.id,
            stock_id=stock.id,
            option_type=option_type,          # ← was hardcoded 'call'
            strike_price=strike_val,
            expiration_date=exp_date,
            days_to_expiry=dte_val,
            delta=delta_val,
            bid=bid_val,
            ask=ask_val,
            spread_pct=spread_val,
            open_interest=oi_val,
            volume=vol_val,
            implied_volatility=iv_val,
            data_source=option_data.get('data_source', 'yfinance'),
            is_recommended=is_recommended,
            recommendation_reason=reason,
            target_return=target_ret,
            hold_type=_classify_hold_type(dte_val)
        )
        db.session.add(oc)
        logger.info(
            f"  {stock.ticker}: Added OptionCandidate — {option_type.upper()} "
            f"strike=${strike_val:.0f}, {dte_val} DTE, recommended={is_recommended}"
        )
    except Exception as e:
        logger.error(f"  {stock.ticker}: FAILED to create OptionCandidate: {e}")
        logger.error(traceback.format_exc())
        raise


# ─────────────────────────────────────────────────────────────────────────────
# PUT chain fetching
# ─────────────────────────────────────────────────────────────────────────────

def _get_scanner_put_chain(ticker: str):
    """
    Same as _get_scanner_chain() but returns put data keyed under 'options'
    for use by find_best_put().

    Returns: (put_chain_data, source_name)
    put_chain_data is a list of:
        {'expiration': str, 'dte': int, 'puts': DataFrame or list}
    """
    import os
    tradier_key = os.environ.get('TRADIER_API_KEY')
    if tradier_key:
        try:
            from providers.tradier_provider import TradierOptionsProvider
            provider = TradierOptionsProvider()
            chain_data = provider.get_options_chain_for_scanner(ticker)
            if chain_data:
                has_puts = any(len(c.get('puts', [])) > 0 for c in chain_data)
                if has_puts:
                    return chain_data, 'tradier'
        except Exception as e:
            logger.error(f"  {ticker}: Tradier PUT chain failed: {e}")

    # Fallback: yfinance already populates 'puts' in the chain dict
    try:
        chain_data = get_options_chain_yfinance(ticker)
        return chain_data, 'yfinance'
    except Exception as e:
        logger.error(f"  {ticker}: yfinance PUT chain failed: {e}")
        return None, 'yfinance'


def find_best_put(chain_data, entry_price: float, target_price: float,
                  dte_min: int = 21, dte_max: int = 90,
                  delta_min: float = -0.55, delta_max: float = -0.20,
                  max_spread_pct: float = 20, min_oi: int = 50,
                  min_volume: int = 5, strategy: str = 'short',
                  data_source: str = 'yfinance'):
    """
    Mirror of find_best_option() but for PUT contracts.

    Delta convention: puts have negative deltas.
    delta_min = -0.55 (deeper ITM), delta_max = -0.20 (lighter OTM)

    target_price for shorts = expected price DROP target (below entry).
    """
    import math
    from statistics import NormalDist

    candidates = []
    reject_counts = {'dte': 0, 'bid_ask_zero': 0,
                     'spread': 0, 'liquidity': 0, 'delta': 0, 'neg_return': 0}
    total_options = 0

    for chain in chain_data:
        dte = chain['dte']
        if dte < dte_min or dte > dte_max:
            continue

        puts = chain.get('puts')
        if puts is None:
            continue

        # Handle both DataFrame and list formats
        try:
            rows = puts.iterrows() if hasattr(puts, 'iterrows') else enumerate(puts)
        except Exception:
            continue

        for _, row in rows:
            total_options += 1

            if hasattr(row, 'get'):
                strike = row.get('strike', 0)
                bid = row.get('bid', 0) or 0
                ask = row.get('ask', 0) or 0
                oi = row.get('openInterest', 0) or 0
                vol = row.get('volume', 0) or 0
                iv = row.get('impliedVolatility', 0) or 0
                real_delta = row.get('delta', 0) or 0
            else:
                # dict-style row
                strike = row.get('strike', 0)
                bid = row.get('bid', 0) or 0
                ask = row.get('ask', 0) or 0
                oi = row.get('openInterest', 0) or 0
                vol = row.get('volume', 0) or 0
                iv = row.get('impliedVolatility', 0) or 0
                real_delta = row.get('delta', 0) or 0

            if bid <= 0 or ask <= 0:
                reject_counts['bid_ask_zero'] += 1
                continue

            mid_price = (bid + ask) / 2
            spread_pct = ((ask - bid) / ask * 100) if ask > 0 else 100
            if spread_pct > max_spread_pct:
                reject_counts['spread'] += 1
                continue

            if oi < min_oi or vol < min_volume:
                reject_counts['liquidity'] += 1
                continue

            # Delta for puts is negative; normalize to negative convention
            if data_source == 'tradier' and real_delta != 0:
                est_delta = real_delta if real_delta < 0 else -real_delta
            else:
                # Estimate put delta from call delta parity: put_delta ≈ call_delta - 1
                moneyness = strike / entry_price if entry_price > 0 else 1
                try:
                    t = dte / 365.0
                    if iv <= 0:
                        iv = 0.30
                    d1 = (math.log(1.0 / moneyness) + (0.5 * iv ** 2) * t) / (iv * math.sqrt(t))
                    call_delta = NormalDist().cdf(d1)
                    est_delta = call_delta - 1.0    # put delta = call_delta - 1
                except Exception:
                    est_delta = -0.35 if moneyness >= 1.0 else -0.60

            if not (delta_min <= est_delta <= delta_max):
                reject_counts['delta'] += 1
                continue

            # Expected return: stock drops to target_price
            theo_return = 0
            if target_price and target_price > 0 and ask > 0:
                half_dte = max(dte / 2.0, 1)
                time_decay_factor = (half_dte / dte) if dte > 0 else 0.5

                bear_stock = target_price                          # full drop
                bear_intrinsic = max(0, strike - bear_stock)      # put intrinsic value
                bear_time_val = ask * time_decay_factor * 0.5
                bear_option = bear_intrinsic + bear_time_val
                bear_return = ((bear_option - ask) / ask) * 100

                mid_stock = entry_price - (entry_price - target_price) * 0.5
                mid_intrinsic = max(0, strike - mid_stock)
                mid_time_val = ask * time_decay_factor * 0.6
                mid_option = mid_intrinsic + mid_time_val
                mid_return = ((mid_option - ask) / ask) * 100

                sideways_option = ask * time_decay_factor * 0.4
                if entry_price < strike:
                    sideways_option += max(0, strike - entry_price) * 0.3
                sideways_return = ((sideways_option - ask) / ask) * 100

                theo_return = (bear_return * 0.4) + (mid_return * 0.4) + (sideways_return * 0.2)
                if theo_return > 300:
                    theo_return = 300.0

            if target_price and target_price > 0 and theo_return <= 0:
                reject_counts['neg_return'] += 1
                continue

            # Scoring (same weighting as find_best_option)
            score = 0
            if theo_return > 0:
                score += min(theo_return / 200, 1.0) * 25
            mid_delta = (delta_min + delta_max) / 2
            score += (1 - abs(est_delta - mid_delta) / 0.3) * 20
            score += max(0, (max_spread_pct - spread_pct) / max_spread_pct) * 15
            score += min(oi / 500, 1) * 12
            score += min(vol / 200, 1) * 8
            mid_dte = (dte_min + dte_max) / 2
            dte_score = 1 - abs(dte - mid_dte) / (mid_dte if mid_dte > 0 else 1)
            score += max(0, dte_score) * 20

            # OI bonus for shorts (prefer liquid puts)
            if oi > 500:
                score += 8
            if iv > 0.5:
                score += 5     # elevated IV = better premium

            candidates.append({
                'strike': strike,
                'expiration': chain['expiration'],
                'dte': dte,
                'bid': bid,
                'ask': ask,
                'mid': round(mid_price, 2),
                'spread_pct': round(spread_pct, 1),
                'open_interest': int(oi),
                'volume': int(vol),
                'iv': round(iv, 4),
                'delta': round(est_delta, 3),
                'score': round(score, 1),
                'target_return': round(theo_return, 1),
                'data_source': data_source,
                'option_type': 'put',
            })

    if not candidates:
        return None

    candidates.sort(key=lambda x: x['score'], reverse=True)
    return candidates[0]


def select_put_options_for_candidate(candidate, stock, short_score: int = 0,
                                     hedge_mode: bool = False):
    """
    Select the best PUT contract for a short candidate.

    Mirrors select_options_for_candidate() but for puts.
    Saves one recommended OptionCandidate with option_type='put'.

    Args:
        candidate: Candidate model instance (side='short')
        stock: Stock model instance
        short_score: The score from score_short() (used to gate min quality)
        hedge_mode: True when called from hedge basket generation

    Returns:
        int: 1 if a put was saved, 0 otherwise
    """
    from models import db, OptionCandidate
    ticker = stock.ticker
    entry_price = candidate.entry_price or 0
    target_price = candidate.target_price or 0

    if entry_price <= 0:
        logger.warning(f"{ticker}: No entry price for short candidate, skipping put selection")
        return 0

    # For shorts, target is below entry (stock expected to fall)
    # If no target set, default to -8% from entry
    if not target_price or target_price >= entry_price:
        target_price = entry_price * 0.92
        logger.info(f"{ticker}: Short target defaulting to -8% (${target_price:.2f})")

    logger.info(
        f"{ticker}: Selecting PUT — entry=${entry_price:.2f}, target=${target_price:.2f}, "
        f"score={short_score}"
    )

    try:
        chain_data, data_source = _get_scanner_put_chain(ticker)
        if not chain_data:
            logger.warning(f"{ticker}: No options chain for put selection")
            return 0

        strategy = candidate.strategy_type or 'gap_fill_short'

        # DTE ranges by strategy type
        if strategy == 'gap_fill_short':
            best = find_best_put(chain_data, entry_price, target_price,
                                 dte_min=21, dte_max=90,
                                 delta_min=-0.55, delta_max=-0.20,
                                 max_spread_pct=20, min_oi=50, min_volume=5,
                                 strategy=strategy, data_source=data_source)
        elif strategy == 'overbought_short':
            best = find_best_put(chain_data, entry_price, target_price,
                                 dte_min=14, dte_max=60,
                                 delta_min=-0.55, delta_max=-0.25,
                                 max_spread_pct=20, min_oi=50, min_volume=5,
                                 strategy=strategy, data_source=data_source)
        elif strategy == 'catalyst_short':
            best = find_best_put(chain_data, entry_price, target_price,
                                 dte_min=30, dte_max=120,
                                 delta_min=-0.50, delta_max=-0.20,
                                 max_spread_pct=25, min_oi=30, min_volume=1,
                                 strategy=strategy, data_source=data_source)
        else:
            # Generic short fallback
            best = find_best_put(chain_data, entry_price, target_price,
                                 dte_min=21, dte_max=90,
                                 data_source=data_source)

        if not best:
            # Relaxed fallback
            best = find_best_put(chain_data, entry_price, target_price,
                                 dte_min=14, dte_max=180,
                                 delta_min=-0.60, delta_max=-0.15,
                                 max_spread_pct=35, min_oi=20, min_volume=1,
                                 strategy='short_relaxed', data_source=data_source)

        if not best:
            logger.warning(f"{ticker}: No put contract found")
            db.session.query(OptionCandidate).filter_by(candidate_id=candidate.id).delete()
            _update_candidate_option_fields_short(candidate, None)
            db.session.flush()
            return 0

        # Clear stale put candidates
        db.session.query(OptionCandidate).filter_by(candidate_id=candidate.id).delete()

        # Build risk badges
        badges = ['margin_alert']
        if best['dte'] < 30:
            badges.append('theta_burn')
        leverage = entry_price / best['mid'] if best.get('mid', 0) > 0 else None

        reason = (
            f"Short PUT: {best['dte']} DTE, strike ${best['strike']:.0f}, "
            f"delta {best['delta']:.2f}, target return {best.get('target_return', 0):.0f}%"
        )

        save_option_candidate(
            candidate, stock, best,
            is_recommended=True,
            reason=reason,
            option_type='put'
        )
        _update_candidate_option_fields_short(candidate, best, badges, leverage)
        db.session.flush()

        logger.info(f"{ticker}: PUT saved — {reason}")
        return 1

    except Exception as e:
        logger.error(f"{ticker}: PUT selection crashed: {e}")
        logger.error(traceback.format_exc())
        return 0


def _update_candidate_option_fields_short(candidate, best_option, badges=None, leverage=None):
    """Update Candidate fields for a short entry (mirrors update_candidate_option_fields)."""
    if best_option:
        candidate.suggested_strike = best_option['strike']
        candidate.suggested_expiry = best_option['expiration']
        candidate.days_to_expiry = best_option['dte']
        candidate.option_type = 'put'
        if badges:
            import json
            candidate.badges = json.dumps(badges)
        if leverage:
            candidate.leverage = round(leverage, 1)
    else:
        candidate.suggested_strike = None
        candidate.suggested_expiry = None
        candidate.days_to_expiry = None
        candidate.option_type = 'put'
