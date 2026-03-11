"""
scanner_shorts.py — TarsierAlpha v2
=====================================
New file — place in root of Replit project.

Add to scanner.py:
    1. Import: from scanner_shorts import run_shorts_scan
    2. Call after Phase 5 in run_scan():

        # Phase 6: Shorts scan (admin-gated beta)
        from scanner_shorts import run_shorts_scan
        shorts_found = run_shorts_scan(app, scan_run)
        scan_run.shorts_found = shorts_found

Usage from run_scan() in scanner.py:
    After phase 5 (paper trade check), add Phase 6 as shown above.
"""

import time
import logging
import traceback
from datetime import datetime, date
from typing import List, Optional

logger = logging.getLogger(__name__)

# Minimum score to generate a short candidate (beta gate)
SHORT_MIN_SCORE = 80

# Negative headline keywords (used for catalyst_short detection)
NEGATIVE_KEYWORDS = [
    'downgrade', 'miss', 'decline', 'lawsuit', 'investigation',
    'cut', 'layoff', 'warning', 'recall', 'fraud', 'sec', 'class action',
    'revenue miss', 'earnings miss', 'guidance cut', 'guidance lowered',
]


def run_shorts_scan(app, scan_run) -> int:
    """
    Scan for short setups.

    Runs as Phase 6 after the main long-only scan. Admin-gated.

    Args:
        app:      Flask app (for context)
        scan_run: ScanRun model instance from the current scan

    Returns:
        int: number of short candidates found
    """
    from models import db, Stock, Candidate, TechnicalIndicator, User

    # Gate: only run if at least one admin has shorts enabled
    # (In practice, once you flip the admin switch, it runs for all scored tickers)
    with app.app_context():
        admin_with_shorts = db.session.query(User).filter(
            User.is_admin == True,
            User.shorts_enabled == True,
        ).first()

        if not admin_with_shorts:
            logger.info("Phase 6 (Shorts): Skipped — no admin has enabled shorts yet")
            return 0

        logger.info("Phase 6: Starting shorts scan")
        start = time.time()

        # Get the ticker universe — same as main scan but we only need
        # stocks that already have fresh TechnicalIndicator data from Phase 1
        tickers = _get_shortable_tickers(scan_run.id)
        logger.info(f"Phase 6: Evaluating {len(tickers)} tickers for short setups")

        shorts_found = 0
        for ticker, tech_data in tickers:
            try:
                result = _evaluate_short_candidate(ticker, tech_data, scan_run.id)
                if result:
                    shorts_found += 1
            except Exception as e:
                logger.error(f"Phase 6 error for {ticker}: {e}")
                try:
                    db.session.rollback()
                except Exception:
                    pass

        db.session.commit()
        elapsed = time.time() - start
        logger.info(f"Phase 6 complete: {shorts_found} short candidates found ({elapsed:.1f}s)")
        return shorts_found


def _get_shortable_tickers(scan_run_id: int) -> List[tuple]:
    """
    Pull tickers that Phase 1 already scanned (have fresh TechnicalIndicator data).
    Returns list of (ticker, tech_data_dict) tuples.
    """
    from models import db, Stock, TechnicalIndicator, ScanResult

    today = date.today()
    results = (
        db.session.query(Stock, TechnicalIndicator)
        .join(TechnicalIndicator, TechnicalIndicator.stock_id == Stock.id)
        .filter(TechnicalIndicator.date == today)
        .filter(Stock.is_active == True)
        .all()
    )

    tickers = []
    for stock, ti in results:
        tech_data = {
            'close': ti.close_price,
            'volume': ti.volume,
            'avg_volume_30d': ti.avg_volume_30d,
            'rsi_14': ti.rsi_14,
            'macd_line': ti.macd_line,
            'macd_signal': ti.macd_signal,
            'macd_histogram': ti.macd_histogram,
            'macd_crossover': ti.macd_crossover,
            'bb_upper': ti.bb_upper,
            'bb_middle': ti.bb_middle,
            'bb_lower': ti.bb_lower,
            'bb_width': ti.bb_width,
            'bb_width_percentile': ti.bb_width_percentile,
            'high_52w': ti.high_52w,
            'low_52w': ti.low_52w,
            'pct_from_52w_high': ti.pct_from_52w_high,
            'pct_from_52w_low': ti.pct_from_52w_low,
        }
        tickers.append((stock.ticker, tech_data))

    return tickers


def _evaluate_short_candidate(ticker: str, tech_data: dict, scan_run_id: int) -> bool:
    """
    Score a ticker for short potential and save a Candidate if it qualifies.

    Returns True if a short candidate was saved.
    """
    from models import db, Stock, Candidate, ScanRun
    from scoring_additions import score_short, build_risk_note
    from options_selector_additions import select_put_options_for_candidate
    import json

    # Enrich tech_data with catalyst flag from recent headlines
    tech_data = _enrich_with_catalyst_flag(ticker, tech_data)

    setup_type, score, breakdown = score_short(tech_data)
    if score == 0 or setup_type is None:
        return False

    stock = db.session.query(Stock).filter_by(ticker=ticker).first()
    if not stock:
        return False

    entry_price = tech_data.get('close', 0)
    if entry_price <= 0:
        return False

    # Short target: expect -5% to -15% depending on setup
    target_pct = {
        'gap_fill_short':  0.92,   # -8%
        'overbought_short': 0.90,  # -10%
        'catalyst_short':  0.88,   # -12%
    }.get(setup_type, 0.92)
    target_price = entry_price * target_pct
    stop_loss = entry_price * 1.08   # +8% stop loss on a short

    # Check if this ticker already has a short candidate for this scan run
    existing = db.session.query(Candidate).filter_by(
        stock_id=stock.id,
        scan_run_id=scan_run_id,
        strategy_type=setup_type,
        side='short',
    ).first()

    if existing:
        # Update score only if it improved
        if score > (existing.total_score or 0):
            existing.total_score = score
            existing.strategy_score = score
            existing.score_breakdown = json.dumps({
                'setup_type': setup_type,
                'short_score': score,
                'breakdown': breakdown,
            })
            existing.updated_at = datetime.utcnow()
        return True

    # Build score breakdown
    score_breakdown = json.dumps({
        'strategy_type': setup_type,
        'short_score': score,
        'gap_fill_score': 0,
        'oversold_bounce_score': 0,
        'catalyst_score': 0,
        'fundamental_score': 0,
        'strategy_details': breakdown,
        'fundamental_details': {},
        'total_score': score,
        'side': 'short',
    })

    candidate = Candidate(
        stock_id=stock.id,
        scan_run_id=scan_run_id,
        strategy_type=setup_type,
        total_score=score,
        strategy_score=score,
        fundamental_score=0,
        gap_fill_score=0,
        oversold_score=0,
        catalyst_score=0,
        score_breakdown=score_breakdown,
        entry_price=round(entry_price, 2),
        target_price=round(target_price, 2),
        stop_loss=round(stop_loss, 2),
        risk_reward_ratio=round((entry_price - target_price) / (stop_loss - entry_price), 2),
        option_type='put',
        side='short',
        status='new',
        outcome_status='pending',
        discovery_price=round(entry_price, 2),
        discovery_date=datetime.utcnow(),
        original_entry_low=round(entry_price * 0.99, 2),
        original_entry_high=round(entry_price * 1.01, 2),
        original_strike=round(entry_price, 0),
        original_target1=round(target_price, 2),
        original_target2=round(entry_price * 0.85, 2),
        entry_window_status='active',
        confirmation_status='confirmed',
        confirmation_score=score,
        confirmed_date=datetime.utcnow(),
    )
    db.session.add(candidate)
    db.session.flush()

    # Select PUT options
    try:
        saved = select_put_options_for_candidate(candidate, stock, short_score=score)
        db.session.commit()

        if saved > 0:
            # Calculate leverage and risk note from the put
            from models import OptionCandidate
            rec_put = db.session.query(OptionCandidate).filter_by(
                candidate_id=candidate.id, is_recommended=True
            ).first()

            if rec_put:
                mid = rec_put.mid_price
                if mid > 0:
                    leverage = round(entry_price / mid, 1)
                    candidate.leverage = leverage
                    risk_note = build_risk_note(
                        setup_type, entry_price,
                        rec_put.strike_price, mid
                    )
                    candidate.risk_note = risk_note[:200]

            db.session.commit()
            logger.info(f"SHORT candidate saved: {ticker} | {setup_type} | score={score}")
            return True
        else:
            logger.warning(f"SHORT candidate {ticker}: no PUT found, still saving candidate")
            db.session.commit()
            return True

    except Exception as e:
        logger.error(f"Short candidate PUT selection failed for {ticker}: {e}")
        logger.error(traceback.format_exc())
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
        return False


def _enrich_with_catalyst_flag(ticker: str, tech_data: dict) -> dict:
    """
    Check recent news headlines for negative sentiment.
    Sets tech_data['negative_catalyst'] = True if found.
    """
    tech_data = dict(tech_data)  # don't mutate original
    try:
        from models import db, CatalystEvent, Stock
        stock = db.session.query(Stock).filter_by(ticker=ticker).first()
        if not stock:
            return tech_data

        from datetime import timedelta
        cutoff = datetime.utcnow() - timedelta(days=3)
        recent_events = db.session.query(CatalystEvent).filter(
            CatalystEvent.stock_id == stock.id,
            CatalystEvent.created_at >= cutoff,
        ).all()

        for event in recent_events:
            desc = (event.event_description or '').lower()
            if any(kw in desc for kw in NEGATIVE_KEYWORDS):
                tech_data['negative_catalyst'] = True
                logger.info(f"{ticker}: Negative catalyst detected: {desc[:60]}")
                break

    except Exception as e:
        logger.warning(f"Catalyst flag check failed for {ticker}: {e}")

    return tech_data


def create_short_paper_trade(candidate, rec_option) -> Optional[object]:
    """
    Create a paper PaperTrade for a short candidate.
    Mirror of create_paper_trade_for_candidate() in paper_trade_checker.py
    but sets option_type='PUT', side='short'.

    Call from run_scan() Phase 3b after checking `candidate.side == 'short'`.
    The existing paper_trade_checker.create_paper_trade_for_candidate() does NOT
    need to be modified — just add this check in scanner.py:

        if cand.side == 'short':
            pt = create_short_paper_trade(cand, rec_option)
        else:
            pt = create_paper_trade_for_candidate(cand, rec_option)
    """
    from models import db, PaperTrade, PaperTradeLog, PaperPortfolio
    from datetime import timedelta

    ticker = candidate.stock.ticker
    entry_price = rec_option.mid_price if rec_option.mid_price > 0 else rec_option.ask or 0
    if not entry_price or entry_price <= 0:
        logger.warning(f"Short paper trade skipped for {ticker}: no valid entry price")
        return None

    # Check for duplicate active short paper trade
    existing = db.session.query(PaperTrade).filter(
        PaperTrade.candidate_id == candidate.id,
        PaperTrade.status.in_(['active', 'partial_exit', 'pending_fill']),
    ).first()
    if existing:
        logger.info(f"Short paper trade already exists for {ticker} (#{existing.id})")
        return existing

    target_stock_price = candidate.target_price or (candidate.entry_price * 0.92)
    stop_stock_price = candidate.stop_loss or (candidate.entry_price * 1.08)

    # For a put: target premium ≈ 2× entry (stock drops to target)
    target_option_price = entry_price * 2.0
    stop_option_price = entry_price * 0.50

    # T1/T2: staged exits
    t1_stock = candidate.entry_price * 0.96
    t2_stock = candidate.entry_price * 0.92
    t1_option = entry_price * 1.5
    t2_option = entry_price * 2.0

    try:
        pt = PaperTrade(
            candidate_id=candidate.id,
            ticker=ticker,
            strategy=candidate.strategy_type,
            option_type='PUT',
            strike=rec_option.strike_price,
            expiration=rec_option.expiration_date,
            entry_price=round(entry_price, 4),
            entry_date=datetime.utcnow(),
            entry_stock_price=candidate.entry_price,
            target_price=round(target_option_price, 4),
            stop_loss_price=round(stop_option_price, 4),
            target_1=round(t1_option, 4),
            target_2=round(t2_option, 4),
            target_3=round(t2_option * 1.3, 4),
            status='pending_fill',
            contracts_total=3,
            contracts_remaining=3,
            cost_basis=round(entry_price * 100 * 3, 2),
            side='short',
        )
        db.session.add(pt)
        db.session.flush()

        log_entry = PaperTradeLog(
            paper_trade_id=pt.id,
            event_type='short_created',
            stock_price=candidate.entry_price,
            option_price=entry_price,
            notes=(
                f"Short paper trade: {candidate.strategy_type} | "
                f"Score {candidate.total_score:.0f} | "
                f"PUT ${rec_option.strike_price:.0f} exp {rec_option.expiration_date}"
            ),
            event_date=datetime.utcnow(),
        )
        db.session.add(log_entry)
        db.session.commit()

        logger.info(
            f"SHORT paper trade created: {ticker} PUT ${rec_option.strike_price:.0f} "
            f"exp {rec_option.expiration_date}, entry ${entry_price:.4f}"
        )
        return pt

    except Exception as e:
        logger.error(f"Short paper trade creation failed for {ticker}: {e}")
        db.session.rollback()
        return None
