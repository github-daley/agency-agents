"""
hedge.py — TarsierAlpha v2 Portfolio Hedge Mode
================================================
New file — place in root of Replit project alongside scanner.py, scoring.py etc.

Generates a PUT basket to hedge a business's exposure to a specific industry.
All trades are paper-only — no real broker execution.

Usage (from app.py routes):
    from hedge import generate_hedge_basket, enter_paper_hedge_basket
"""

import logging
import uuid
from datetime import datetime, timedelta
from typing import Optional

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# Industry → correlated public tickers
# ─────────────────────────────────────────────────────────────────────────────
INDUSTRY_MAP = {
    'trucking':      ['XPO', 'JBHT', 'ODFL', 'WERN', 'SAIA'],
    'retail':        ['WMT', 'TGT', 'COST', 'AMZN', 'EBAY'],
    'oil':           ['CVX', 'XOM', 'OXY', 'HAL', 'SLB'],
    'tech':          ['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'META'],
    'airlines':      ['DAL', 'UAL', 'AAL', 'LUV', 'JBLU'],
    'housing':       ['DHI', 'LEN', 'PHM', 'TOL', 'KBH'],
    'banking':       ['JPM', 'BAC', 'WFC', 'C', 'GS'],
    'healthcare':    ['UNH', 'CVS', 'HCA', 'HUM', 'CI'],
    'manufacturing': ['CAT', 'DE', 'EMR', 'HON', 'GE'],
    'consumer':      ['MCD', 'SBUX', 'NKE', 'YUM', 'CMG'],
}

# Hedge ratio by risk tolerance (fraction of exposure)
HEDGE_RATIOS = {
    'low':  0.10,  # 10% hedged
    'med':  0.20,  # 20% hedged (default)
    'high': 0.35,  # 35% hedged
}


def generate_hedge_basket(
    industry: str,
    exposure_usd: float,
    risk_tolerance: str = 'med',
    max_candidates: int = 5,
) -> dict:
    """
    Generate a PUT basket to hedge a business's exposure to an industry.

    Args:
        industry:        Key from INDUSTRY_MAP (e.g. 'trucking')
        exposure_usd:    Dollar value of business exposure (e.g. annual diesel cost)
        risk_tolerance:  'low' | 'med' | 'high'
        max_candidates:  Max basket size (default 5)

    Returns:
        dict with keys:
            industry, exposure_usd, hedge_target, risk_tolerance,
            basket (list of position dicts), total_cost, coverage_ratio,
            expected_gain_5pct_drop, disclaimer
    """
    if industry not in INDUSTRY_MAP:
        available = list(INDUSTRY_MAP.keys())
        raise ValueError(f"Unknown industry '{industry}'. Available: {available}")

    if risk_tolerance not in HEDGE_RATIOS:
        risk_tolerance = 'med'

    hedge_target = exposure_usd * HEDGE_RATIOS[risk_tolerance]
    tickers = INDUSTRY_MAP[industry]

    logger.info(
        f"Hedge basket: industry={industry}, exposure=${exposure_usd:,.0f}, "
        f"target=${hedge_target:,.0f}, tolerance={risk_tolerance}"
    )

    # Score each correlated ticker as a short candidate
    scored = []
    for ticker in tickers:
        try:
            result = _score_ticker_for_hedge(ticker)
            if result:
                scored.append(result)
        except Exception as e:
            logger.warning(f"Hedge scoring failed for {ticker}: {e}")

    # Sort by score, take top N
    scored.sort(key=lambda x: x['score'], reverse=True)
    basket_tickers = scored[:max_candidates]

    if not basket_tickers:
        # Fall back: include all tickers with placeholder scores if scoring failed
        logger.warning(f"No scored candidates for {industry} hedge; using unscored tickers")
        basket_tickers = [{'ticker': t, 'score': 60, 'setup_type': 'hedge_default',
                           'price': 0, 'put': None} for t in tickers[:max_candidates]]

    # Size each position
    n = len(basket_tickers)
    per_position_usd = hedge_target / n if n > 0 else 0

    basket = []
    total_cost = 0.0
    expected_gain = 0.0

    for item in basket_tickers:
        ticker = item['ticker']
        put = item.get('put')
        price = item.get('price', 0)
        score = item.get('score', 60)
        setup_type = item.get('setup_type', 'hedge')

        if put and put.get('mid', 0) > 0:
            premium = put['mid']
            contracts = max(1, int((per_position_usd / 100) / premium))
            position_cost = round(contracts * premium * 100, 2)
            strike = put['strike']
            delta = abs(put.get('delta', 0.35))
            dte = put.get('dte', 45)
            expiry = put.get('expiration', '')
            iv = put.get('iv', 0)

            # Estimated gain if correlated stock drops 5%
            # Gain ≈ delta × 5% drop × stock_price × contracts × 100
            gain_per_contract = delta * (price * 0.05) * 100
            pos_gain = round(gain_per_contract * contracts, 2)

            hedge_hint = _delta_hedge_hint(delta)
            badges = ['hedge_position']
            if dte < 30:
                badges.append('theta_burn')
        else:
            # No live options data — estimate
            premium = price * 0.03 if price > 0 else 2.0
            contracts = max(1, int((per_position_usd / 100) / premium))
            position_cost = round(contracts * premium * 100, 2)
            strike = round(price * 0.95, 0) if price > 0 else 0
            delta = 0.35
            dte = 45
            expiry = (datetime.utcnow() + timedelta(days=45)).strftime('%Y-%m-%d')
            iv = 0
            pos_gain = round(delta * (price * 0.05) * 100 * contracts, 2)
            hedge_hint = "~35Δ estimated"
            badges = ['hedge_position', 'estimate_only']

        basket.append({
            'ticker': ticker,
            'setup_type': setup_type,
            'score': score,
            'stock_price': price,
            'strike': strike,
            'expiry': expiry,
            'dte': dte,
            'premium': premium,
            'contracts': contracts,
            'position_cost': position_cost,
            'delta': round(delta, 3),
            'iv': round(iv, 4),
            'gain_at_5pct_drop': pos_gain,
            'hedge_hint': hedge_hint,
            'badges': badges,
        })

        total_cost += position_cost
        expected_gain += pos_gain

    coverage_ratio = (expected_gain / hedge_target * 100) if hedge_target > 0 else 0

    return {
        'industry': industry,
        'exposure_usd': exposure_usd,
        'hedge_target': round(hedge_target, 2),
        'risk_tolerance': risk_tolerance,
        'basket': basket,
        'basket_size': len(basket),
        'total_cost': round(total_cost, 2),
        'expected_gain_5pct_drop': round(expected_gain, 2),
        'coverage_ratio': round(coverage_ratio, 1),
        'disclaimer': (
            "Paper hedge only — no real trades placed. "
            "PUT options carry significant risk including total loss of premium. "
            "This is not financial advice."
        ),
    }


def enter_paper_hedge_basket(basket_data: dict, app) -> dict:
    """
    Create paper PaperTrade records for each position in a hedge basket.
    Links all positions via a shared hedge_group_id.

    Args:
        basket_data: dict returned by generate_hedge_basket()
        app:         Flask app (for app_context)

    Returns:
        dict with trade_ids, group_id, total_cost, status
    """
    from models import db, Stock, Candidate, ScanRun, PaperTrade, PaperTradeLog, PaperPortfolio
    from datetime import date

    group_id = f"hedge_{uuid.uuid4().hex[:10]}"
    trade_ids = []
    errors = []

    with app.app_context():
        # Find or create a paper hedge scan run
        hedge_scan = db.session.query(ScanRun).filter_by(
            scan_type='hedge',
            status='completed'
        ).order_by(ScanRun.created_at.desc()).first()

        if not hedge_scan:
            hedge_scan = ScanRun(
                scan_date=date.today(),
                scan_type='hedge',
                status='completed',
                stocks_scanned=0,
                candidates_found=0,
                started_at=datetime.utcnow(),
                completed_at=datetime.utcnow(),
            )
            db.session.add(hedge_scan)
            db.session.flush()

        for pos in basket_data.get('basket', []):
            try:
                ticker = pos['ticker']
                stock = db.session.query(Stock).filter_by(ticker=ticker).first()
                if not stock:
                    logger.warning(f"Hedge: Stock {ticker} not in DB, skipping")
                    errors.append(f"{ticker}: not in database")
                    continue

                # Create or find a short candidate for this stock
                candidate = db.session.query(Candidate).filter_by(
                    stock_id=stock.id,
                    scan_run_id=hedge_scan.id,
                    strategy_type='hedge',
                ).first()

                if not candidate:
                    candidate = Candidate(
                        stock_id=stock.id,
                        scan_run_id=hedge_scan.id,
                        strategy_type='hedge',
                        total_score=pos.get('score', 60),
                        strategy_score=pos.get('score', 60),
                        fundamental_score=0,
                        entry_price=pos.get('stock_price', 0),
                        target_price=round(pos.get('stock_price', 0) * 0.92, 2),
                        stop_loss=round(pos.get('stock_price', 0) * 1.08, 2),
                        option_type='put',
                        side='short',
                        status='new',
                        outcome_status='pending',
                    )
                    db.session.add(candidate)
                    db.session.flush()

                expiry_str = pos.get('expiry', '')
                entry_price = pos.get('premium', 0)
                strike = pos.get('strike', 0)
                contracts = pos.get('contracts', 1)

                pt = PaperTrade(
                    candidate_id=candidate.id,
                    ticker=ticker,
                    strategy='hedge',
                    option_type='PUT',
                    strike=strike,
                    expiration=expiry_str,
                    entry_price=entry_price,
                    entry_date=datetime.utcnow(),
                    entry_stock_price=pos.get('stock_price', 0),
                    target_price=round(pos.get('stock_price', 0) * 0.92, 2),
                    stop_loss_price=round(pos.get('stock_price', 0) * 1.08, 2),
                    target_1=round(strike * 0.95, 2),
                    target_2=round(strike * 0.90, 2),
                    status='pending_fill',
                    contracts_total=contracts,
                    contracts_remaining=contracts,
                    cost_basis=round(entry_price * 100 * contracts, 2),
                    side='short',
                    hedge_group_id=group_id,
                )
                db.session.add(pt)
                db.session.flush()

                log_entry = PaperTradeLog(
                    paper_trade_id=pt.id,
                    event_type='hedge_entered',
                    stock_price=pos.get('stock_price', 0),
                    option_price=entry_price,
                    notes=(
                        f"Hedge basket {group_id}. Industry: {basket_data.get('industry')}. "
                        f"Exposure: ${basket_data.get('exposure_usd', 0):,.0f}. "
                        f"Contracts: {contracts}"
                    ),
                    event_date=datetime.utcnow(),
                )
                db.session.add(log_entry)
                trade_ids.append(pt.id)

            except Exception as e:
                logger.error(f"Hedge basket entry failed for {pos.get('ticker')}: {e}")
                errors.append(f"{pos.get('ticker')}: {str(e)}")
                db.session.rollback()
                continue

        db.session.commit()

    return {
        'group_id': group_id,
        'trade_ids': trade_ids,
        'trades_created': len(trade_ids),
        'total_cost': basket_data.get('total_cost', 0),
        'errors': errors,
        'disclaimer': basket_data.get('disclaimer', ''),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Internal helpers
# ─────────────────────────────────────────────────────────────────────────────

def _score_ticker_for_hedge(ticker: str) -> Optional[dict]:
    """
    Fetch price/tech data for a ticker and run score_short_for_hedge().
    Returns dict or None if scoring fails or below threshold.
    """
    try:
        from api_client import DataManager
        from technical import analyze_stock
        from scoring_additions import score_short_for_hedge
        from options_selector_additions import find_best_put

        dm = DataManager()
        df = dm.get_price_history(ticker, period='3mo')
        if df is None or len(df) < 20:
            return None

        tech_data = analyze_stock(df)
        if not tech_data:
            return None

        setup_type, score, breakdown = score_short_for_hedge(tech_data)
        if score < 70:
            return None

        price = tech_data.get('close', 0)
        target_price = price * 0.92

        # Try to fetch a PUT for sizing estimate
        try:
            from options_selector_additions import _get_scanner_put_chain
            chain_data, source = _get_scanner_put_chain(ticker)
            put = None
            if chain_data:
                put = find_best_put(chain_data, price, target_price,
                                    dte_min=21, dte_max=90,
                                    delta_min=-0.55, delta_max=-0.20,
                                    max_spread_pct=30, min_oi=20, min_volume=1,
                                    strategy='hedge', data_source=source)
        except Exception:
            put = None

        return {
            'ticker': ticker,
            'setup_type': setup_type,
            'score': score,
            'price': price,
            'put': put,
        }

    except Exception as e:
        logger.warning(f"_score_ticker_for_hedge({ticker}) failed: {e}")
        return None


def _delta_hedge_hint(delta: float) -> str:
    """Human-readable delta hedge interpretation."""
    abs_delta = abs(delta)
    if abs_delta >= 0.50:
        return f"Δ{delta:.2f} — strong correlation, deeper hedge"
    elif abs_delta >= 0.35:
        return f"Δ{delta:.2f} — moderate hedge, balanced premium/protection"
    else:
        return f"Δ{delta:.2f} — lighter hedge, lower cost"


def get_available_industries() -> list:
    """Returns list of supported industries for the hedge form dropdown."""
    return [
        {'key': 'trucking',      'label': 'Trucking / Logistics'},
        {'key': 'retail',        'label': 'Retail / E-Commerce'},
        {'key': 'oil',           'label': 'Oil & Gas'},
        {'key': 'tech',          'label': 'Technology'},
        {'key': 'airlines',      'label': 'Airlines / Travel'},
        {'key': 'housing',       'label': 'Housing / Construction'},
        {'key': 'banking',       'label': 'Banking / Finance'},
        {'key': 'healthcare',    'label': 'Healthcare'},
        {'key': 'manufacturing', 'label': 'Manufacturing'},
        {'key': 'consumer',      'label': 'Consumer / Food & Beverage'},
    ]
