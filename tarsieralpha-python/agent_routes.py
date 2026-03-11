"""
agent_routes.py — TarsierAlpha v2 Agentic API
===============================================
New file — place in root of Replit project.

Register the blueprint in app.py:

    from agent_routes import agent_bp
    app.register_blueprint(agent_bp)

Auth: X-Agent-Key header validated against AGENT_API_KEYS env var (comma-separated).

Endpoints:
    GET  /api/agent/scans          — paginated scan candidates
    GET  /api/agent/pnl            — paper trade performance by side
    POST /api/agent/paper-trade    — simulate a paper trade entry
"""

import os
import logging
from datetime import datetime, timedelta, date
from functools import wraps

from flask import Blueprint, request, jsonify

logger = logging.getLogger(__name__)

agent_bp = Blueprint('agent', __name__)


# ─────────────────────────────────────────────────────────────────────────────
# Auth middleware
# ─────────────────────────────────────────────────────────────────────────────

def _valid_agent_keys() -> set:
    """Read comma-separated AGENT_API_KEYS from environment."""
    raw = os.environ.get('AGENT_API_KEYS', '')
    return {k.strip() for k in raw.split(',') if k.strip()}


def require_agent_key(f):
    """Decorator: validate X-Agent-Key header."""
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get('X-Agent-Key', '').strip()
        if not key:
            return jsonify({'error': 'X-Agent-Key header required'}), 401
        valid_keys = _valid_agent_keys()
        if not valid_keys:
            return jsonify({'error': 'Agent API not configured (AGENT_API_KEYS not set)'}), 503
        if key not in valid_keys:
            return jsonify({'error': 'Invalid agent key'}), 403
        return f(*args, **kwargs)
    return decorated


# ─────────────────────────────────────────────────────────────────────────────
# GET /api/agent/scans
# ─────────────────────────────────────────────────────────────────────────────

@agent_bp.route('/api/agent/scans', methods=['GET'])
@require_agent_key
def agent_scans():
    """
    Return active scan candidates optimized for AI agent consumption.

    Query params:
        type      — 'long' | 'short' | 'all'  (default: 'all')
        minScore  — minimum total_score        (default: 62, min: 50)
        limit     — max results                (default: 10, max: 25)
        strategy  — filter by strategy_type   (optional)

    Response: JSON array of candidate objects with Greeks.
    """
    from models import db, Candidate, Stock, OptionCandidate, ScanRun, TechnicalIndicator

    scan_type = request.args.get('type', 'all').lower()
    min_score = max(50, request.args.get('minScore', 62, type=int))
    limit = min(25, max(1, request.args.get('limit', 10, type=int)))
    strategy_filter = request.args.get('strategy', '').lower()

    query = (
        db.session.query(Candidate)
        .join(Stock)
        .filter(Candidate.status != 'archived')
        .filter(Candidate.total_score >= min_score)
    )

    if scan_type == 'long':
        query = query.filter(
            db.or_(Candidate.side == 'long', Candidate.side == None)
        )
    elif scan_type == 'short':
        query = query.filter(Candidate.side == 'short')

    if strategy_filter:
        query = query.filter(Candidate.strategy_type.ilike(f'%{strategy_filter}%'))

    candidates = query.order_by(Candidate.total_score.desc()).limit(limit).all()

    results = []
    for c in candidates:
        stock = c.stock
        ticker = stock.ticker if stock else '???'

        # Fetch recommended option
        rec_opt = db.session.query(OptionCandidate).filter_by(
            candidate_id=c.id, is_recommended=True
        ).first()

        # Latest technical snapshot
        ti = db.session.query(TechnicalIndicator).filter_by(
            stock_id=c.stock_id
        ).order_by(TechnicalIndicator.date.desc()).first()

        chain = None
        if rec_opt:
            chain = {
                'strike': rec_opt.strike_price,
                'expiration': rec_opt.expiration_date,
                'dte': rec_opt.days_to_expiry,
                'optionType': rec_opt.option_type,
                'delta': rec_opt.delta,
                'bid': rec_opt.bid,
                'ask': rec_opt.ask,
                'mid': rec_opt.mid_price,
                'iv': rec_opt.implied_volatility,
                'openInterest': rec_opt.open_interest,
                'volume': rec_opt.volume,
                'targetReturn': rec_opt.target_return,
                'holdType': rec_opt.hold_type,
            }

        side = c.side or 'long'

        result = {
            'ticker': ticker,
            'company': stock.company_name if stock else '',
            'setupType': c.strategy_type,
            'side': side,
            'score': c.total_score,
            'price': c.entry_price,
            'discoveryPrice': c.discovery_price,
            'entryZone': {
                'low': c.original_entry_low,
                'high': c.original_entry_high,
            } if c.original_entry_low else None,
            'target1': c.original_target1,
            'target2': c.original_target2,
            'stopLoss': c.stop_loss,
            'riskReward': c.risk_reward_ratio,
            'confirmationStatus': c.confirmation_status,
            'chain': chain,
            'technicals': {
                'rsi': ti.rsi_14 if ti else None,
                'macdCrossover': ti.macd_crossover if ti else None,
                'bbUpper': ti.bb_upper if ti else None,
                'bbLower': ti.bb_lower if ti else None,
                'pctFrom52wHigh': ti.pct_from_52w_high if ti else None,
                'volume': ti.volume if ti else None,
                'avgVolume30d': ti.avg_volume_30d if ti else None,
            } if ti else None,
            'badges': _parse_badges(c),
            'scannedAt': c.updated_at.isoformat() if c.updated_at else c.created_at.isoformat(),
        }

        # Short-specific fields
        if side == 'short':
            result['leverage'] = c.leverage
            result['riskNote'] = c.risk_note

        results.append(result)

    return jsonify({
        'candidates': results,
        'count': len(results),
        'filters': {
            'type': scan_type,
            'minScore': min_score,
            'limit': limit,
        },
        'generatedAt': datetime.utcnow().isoformat(),
    })


# ─────────────────────────────────────────────────────────────────────────────
# GET /api/agent/pnl
# ─────────────────────────────────────────────────────────────────────────────

@agent_bp.route('/api/agent/pnl', methods=['GET'])
@require_agent_key
def agent_pnl():
    """
    Return paper trade P&L stats split by side (long / short).

    Query params:
        period  — 'week' | 'month' | 'all'  (default: 'month')

    Response includes: winRate, netPnlPct, totalPnlUsd, count per side.
    """
    from models import db, PaperTrade, PaperPortfolio

    period = request.args.get('period', 'month').lower()

    cutoff = None
    if period == 'week':
        cutoff = datetime.utcnow() - timedelta(days=7)
    elif period == 'month':
        cutoff = datetime.utcnow() - timedelta(days=30)

    closed_statuses = ['closed', 'stopped_out', 'expired']
    query = db.session.query(PaperTrade).filter(
        PaperTrade.status.in_(closed_statuses)
    )
    if cutoff:
        query = query.filter(PaperTrade.created_at >= cutoff)

    trades = query.all()

    def _side_stats(side_trades):
        if not side_trades:
            return {'count': 0, 'wins': 0, 'losses': 0, 'winRate': 0,
                    'netPnlPct': 0, 'totalPnlUsd': 0, 'avgReturn': 0}

        wins = [t for t in side_trades if (t.total_return_pct or 0) > 0]
        losses = [t for t in side_trades if (t.total_return_pct or 0) <= 0]
        count = len(side_trades)
        total_pnl_usd = sum(
            (t.current_value or 0) - ((t.entry_price or 0) * 100 * (t.contracts_total or 1))
            for t in side_trades
        )
        avg_entry_cost = sum(
            (t.entry_price or 0) * 100 * (t.contracts_total or 1)
            for t in side_trades
        )
        net_pnl_pct = (total_pnl_usd / avg_entry_cost * 100) if avg_entry_cost > 0 else 0
        avg_return = sum(t.total_return_pct or 0 for t in side_trades) / count

        return {
            'count': count,
            'wins': len(wins),
            'losses': len(losses),
            'winRate': round(len(wins) / count * 100, 1),
            'netPnlPct': round(net_pnl_pct, 2),
            'totalPnlUsd': round(total_pnl_usd, 2),
            'avgReturn': round(avg_return, 2),
        }

    long_trades = [t for t in trades if (t.side or 'long') == 'long']
    short_trades = [t for t in trades if t.side == 'short']

    portfolio = db.session.query(PaperPortfolio).first()
    portfolio_stats = None
    if portfolio:
        portfolio_stats = {
            'startingCapital': float(portfolio.starting_capital or 5000),
            'realizedPnl': float(portfolio.realized_pnl or 0),
        }

    return jsonify({
        'period': period,
        'longs': _side_stats(long_trades),
        'shorts': _side_stats(short_trades),
        'overall': _side_stats(trades),
        'portfolio': portfolio_stats,
        'generatedAt': datetime.utcnow().isoformat(),
    })


# ─────────────────────────────────────────────────────────────────────────────
# POST /api/agent/paper-trade
# ─────────────────────────────────────────────────────────────────────────────

@agent_bp.route('/api/agent/paper-trade', methods=['POST'])
@require_agent_key
def agent_paper_trade():
    """
    Simulate a paper trade entry.

    Body (JSON):
        ticker      — required, e.g. "AAPL"
        strike      — required, e.g. 195.0
        side        — required, 'long' | 'short'
        qty         — number of contracts (default: 1)
        expiry      — 'YYYY-MM-DD' (default: next Friday)
        setupType   — optional, e.g. 'gap_fill_short'

    Returns: tradeId, ticker, strike, optionType, entryPrice, timestamp

    Note: Paper trade simulated — no real broker execution.
    """
    from models import db, PaperTrade, PaperTradeLog, Candidate, Stock, ScanRun

    data = request.get_json(silent=True) or {}

    ticker = (data.get('ticker') or '').upper().strip()
    strike = data.get('strike')
    side = (data.get('side') or '').lower()
    qty = max(1, int(data.get('qty', 1)))
    expiry = data.get('expiry')
    setup_type = data.get('setupType', 'agent_entry')

    # Validate required fields
    if not ticker:
        return jsonify({'error': 'ticker is required'}), 400
    if not strike:
        return jsonify({'error': 'strike is required'}), 400
    if side not in ('long', 'short'):
        return jsonify({'error': "side must be 'long' or 'short'"}), 400

    try:
        strike = float(strike)
    except (TypeError, ValueError):
        return jsonify({'error': 'strike must be a number'}), 400

    # Default expiry: next Friday
    if not expiry:
        today = date.today()
        days_until_friday = (4 - today.weekday()) % 7
        if days_until_friday == 0:
            days_until_friday = 7
        expiry = (today + timedelta(days=days_until_friday)).strftime('%Y-%m-%d')

    option_type = 'PUT' if side == 'short' else 'CALL'

    # Fetch current stock price for entry simulation
    entry_stock_price = 0.0
    entry_option_price = 0.0
    try:
        from api_client import DataManager
        dm = DataManager()
        prices = dm.get_batch_prices([ticker])
        entry_stock_price = prices.get(ticker, 0) or 0.0
        # Estimate option price (simplified: ~3% of stock price for ATM)
        entry_option_price = round(entry_stock_price * 0.03, 2) if entry_stock_price > 0 else 1.0
    except Exception as e:
        logger.warning(f"Agent paper trade: price fetch failed for {ticker}: {e}")
        entry_option_price = 1.0

    # Find or create a stock record
    stock = db.session.query(Stock).filter_by(ticker=ticker).first()
    if not stock:
        return jsonify({'error': f"Ticker {ticker} not found in database"}), 404

    # Find or create a synthetic candidate for the agent trade
    agent_scan = db.session.query(ScanRun).filter_by(scan_type='agent').first()
    if not agent_scan:
        agent_scan = ScanRun(
            scan_date=date.today(),
            scan_type='agent',
            status='completed',
            stocks_scanned=0,
            candidates_found=0,
            started_at=datetime.utcnow(),
            completed_at=datetime.utcnow(),
        )
        db.session.add(agent_scan)
        db.session.flush()

    candidate = Candidate(
        stock_id=stock.id,
        scan_run_id=agent_scan.id,
        strategy_type=setup_type,
        total_score=70,
        strategy_score=70,
        fundamental_score=0,
        entry_price=entry_stock_price,
        option_type=option_type.lower(),
        side=side,
        status='new',
        outcome_status='pending',
    )
    db.session.add(candidate)
    db.session.flush()

    pt = PaperTrade(
        candidate_id=candidate.id,
        ticker=ticker,
        strategy=setup_type,
        option_type=option_type,
        strike=strike,
        expiration=expiry,
        entry_price=entry_option_price,
        entry_date=datetime.utcnow(),
        entry_stock_price=entry_stock_price,
        status='pending_fill',
        contracts_total=qty,
        contracts_remaining=qty,
        cost_basis=round(entry_option_price * 100 * qty, 2),
        side=side,
    )
    db.session.add(pt)
    db.session.flush()

    log_entry = PaperTradeLog(
        paper_trade_id=pt.id,
        event_type='agent_paper_trade',
        stock_price=entry_stock_price,
        option_price=entry_option_price,
        notes=f"Agent-initiated paper trade. Setup: {setup_type}. Side: {side}.",
        event_date=datetime.utcnow(),
    )
    db.session.add(log_entry)
    db.session.commit()

    return jsonify({
        'tradeId': pt.id,
        'ticker': ticker,
        'strike': strike,
        'optionType': option_type,
        'side': side,
        'contracts': qty,
        'entryPrice': entry_option_price,
        'entryStockPrice': entry_stock_price,
        'expiry': expiry,
        'setupType': setup_type,
        'timestamp': pt.entry_date.isoformat(),
        'disclaimer': 'Paper trade simulated — no real broker execution',
    }), 201


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _parse_badges(candidate) -> list:
    """Parse candidate.badges JSON or return empty list."""
    import json
    if not candidate.badges:
        return []
    try:
        return json.loads(candidate.badges)
    except (TypeError, ValueError):
        return []
