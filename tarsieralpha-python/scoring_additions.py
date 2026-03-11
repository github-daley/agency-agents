"""
scoring_additions.py — TarsierAlpha v2
======================================
Paste these functions into scoring.py (alongside the existing score_gap_fill,
score_oversold_bounce, score_catalyst, score_fundamentals functions).

No existing functions need to be modified — these are pure additions.
"""

import json
import logging

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# SHORT SCORING  (beta threshold: 80)
# ─────────────────────────────────────────────────────────────────────────────

def score_short(tech_data: dict, fundamentals: dict = None, market_cap: float = None) -> tuple:
    """
    Score a short setup candidate.

    Returns:
        (setup_type: str | None, score: int, breakdown: dict)

    setup_type is one of:
        'gap_fill_short'    — gapped up ≥ 2%, showing reversal signals
        'overbought_short'  — RSI > 75, near upper Bollinger, vol fading
        'catalyst_short'    — negative catalyst + overbought technicals

    Score must reach SHORT_MIN_SCORE (80) or (None, 0, {}) is returned.
    Lower threshold (70) is used when called from hedge.py for basket generation.
    """
    SHORT_MIN_SCORE = 80

    score = 0
    setup_type = None
    breakdown = {}

    rsi = tech_data.get('rsi_14')
    close = tech_data.get('close', 0)
    bb_upper = tech_data.get('bb_upper')
    bb_lower = tech_data.get('bb_lower')
    volume = tech_data.get('volume', 0)
    avg_vol = tech_data.get('avg_volume_30d', 1) or 1
    pct_from_52w_high = tech_data.get('pct_from_52w_high')  # negative = below high
    macd_histogram = tech_data.get('macd_histogram')
    macd_crossover = tech_data.get('macd_crossover', False)

    vol_ratio = volume / avg_vol if avg_vol > 0 else 1.0
    vol_fading = vol_ratio < 0.8  # price rising but volume declining = fade signal

    # ── Gap Fill Short: gapped UP ≥ 2% then showed reversal ──────────────────
    # Uses pct_from_52w_high as a proxy: if stock is near its 52w high (< 5% below),
    # it likely gapped up recently and is overextended.
    near_52w_high = pct_from_52w_high is not None and abs(pct_from_52w_high) <= 5.0

    if near_52w_high:
        s = 35
        bd = {'near_52w_high': {'value': pct_from_52w_high, 'points': 10, 'max': 10}}

        # RSI momentum fading
        if rsi and rsi > 65:
            pts = 10
            s += pts
            bd['rsi_extended'] = {'value': rsi, 'points': pts, 'max': 10}

        # Volume fading on price extension
        if vol_fading:
            pts = 10
            s += pts
            bd['vol_fade'] = {'value': round(vol_ratio, 2), 'points': pts, 'max': 10}

        # At or above upper Bollinger Band
        if bb_upper and close >= bb_upper * 0.99:
            pts = 15
            s += pts
            bd['bb_upper_touch'] = {'value': round(close / bb_upper, 3), 'points': pts, 'max': 15}

        # MACD losing momentum (negative histogram or bearish cross)
        if macd_histogram is not None and macd_histogram < 0:
            pts = 10
            s += pts
            bd['macd_bearish'] = {'value': round(macd_histogram, 3), 'points': pts, 'max': 10}

        if s > score:
            score = s
            setup_type = 'gap_fill_short'
            breakdown = bd

    # ── Overbought Short: RSI > 75, upper BB, vol fade ───────────────────────
    if rsi and rsi > 75:
        s = 45 + int(rsi - 75)   # base 45 + bonus for extreme RSI
        bd = {'rsi_overbought': {'value': rsi, 'points': 45 + int(rsi - 75), 'max': 60}}

        if bb_upper and close >= bb_upper:
            pts = 15
            s += pts
            bd['at_bb_upper'] = {'value': round(close, 2), 'points': pts, 'max': 15}

        if vol_fading:
            pts = 10
            s += pts
            bd['vol_fade'] = {'value': round(vol_ratio, 2), 'points': pts, 'max': 10}

        if macd_histogram is not None and macd_histogram < 0:
            pts = 10
            s += pts
            bd['macd_bearish'] = {'value': round(macd_histogram, 3), 'points': pts, 'max': 10}

        if s > score:
            score = s
            setup_type = 'overbought_short'
            breakdown = bd

    # ── Catalyst Short: negative news + overbought tech ──────────────────────
    # (Negative sentiment is evaluated in scanner_shorts.py and passed as
    #  tech_data['negative_catalyst'] = True when applicable.)
    has_negative_catalyst = tech_data.get('negative_catalyst', False)
    if has_negative_catalyst and rsi and rsi > 60:
        s = 40
        bd = {'negative_catalyst': {'value': True, 'points': 20, 'max': 20}}

        if rsi > 65:
            pts = min(int(rsi - 60), 20)
            s += pts
            bd['rsi_extended'] = {'value': rsi, 'points': pts, 'max': 20}

        if near_52w_high:
            pts = 15
            s += pts
            bd['near_52w_high'] = {'value': pct_from_52w_high, 'points': pts, 'max': 15}

        if vol_fading:
            pts = 10
            s += pts
            bd['vol_fade'] = {'value': round(vol_ratio, 2), 'points': pts, 'max': 10}

        if s > score:
            score = s
            setup_type = 'catalyst_short'
            breakdown = bd

    score = min(score, 100)

    if score >= SHORT_MIN_SCORE:
        return setup_type, score, breakdown
    return None, 0, {}


def score_short_for_hedge(tech_data: dict, fundamentals: dict = None) -> tuple:
    """
    Lower-threshold version of score_short() used by hedge basket generation.
    Returns same tuple but with min_score=70 instead of 80.
    """
    setup_type, score, breakdown = score_short(tech_data, fundamentals)
    # If raw scoring returned nothing (below 80), re-check at 70 threshold
    if score == 0:
        # Re-run the scoring logic with 70 threshold
        rsi = tech_data.get('rsi_14')
        close = tech_data.get('close', 0)
        bb_upper = tech_data.get('bb_upper')
        volume = tech_data.get('volume', 0)
        avg_vol = tech_data.get('avg_volume_30d', 1) or 1
        pct_from_52w_high = tech_data.get('pct_from_52w_high')
        macd_histogram = tech_data.get('macd_histogram')

        vol_ratio = volume / avg_vol if avg_vol > 0 else 1.0
        vol_fading = vol_ratio < 0.8
        near_52w_high = pct_from_52w_high is not None and abs(pct_from_52w_high) <= 5.0

        s = 0
        st = None
        bd = {}

        if near_52w_high:
            s = 35
            st = 'gap_fill_short'
            bd = {}
            if rsi and rsi > 65:
                s += 10
            if vol_fading:
                s += 10
            if bb_upper and close >= bb_upper * 0.99:
                s += 15
            if macd_histogram is not None and macd_histogram < 0:
                s += 10

        if rsi and rsi > 70 and (45 + int(rsi - 70)) > s:
            s = 45 + int(rsi - 70)
            st = 'overbought_short'
            bd = {'rsi_overbought': {'value': rsi, 'points': s, 'max': 70}}
            if bb_upper and close >= bb_upper:
                s += 10
            if vol_fading:
                s += 5

        s = min(s, 100)
        if s >= 70:
            return st, s, bd

    return setup_type, score, breakdown


def build_risk_note(setup_type: str, entry_price: float, strike: float,
                    premium: float) -> str:
    """
    Generate human-readable risk note for a short candidate.
    Example: "Stock +10% → est. -280% on put"
    """
    if premium <= 0 or entry_price <= 0:
        return "High risk — verify premium before entry"

    # Estimate loss if stock moves against short position by 10%
    adverse_price = entry_price * 1.10
    put_loss = max(0, adverse_price - strike) if strike else premium
    loss_multiple = round((put_loss / premium - 1) * 100, 0) if premium > 0 else 0

    notes = {
        'gap_fill_short': f"Gap reversal play. Stock +10% → est. {loss_multiple:+.0f}% on put",
        'overbought_short': f"Overbought fade. Stock +10% → est. {loss_multiple:+.0f}% on put",
        'catalyst_short': f"Negative catalyst play. Stock +10% → est. {loss_multiple:+.0f}% on put",
    }
    return notes.get(setup_type, f"Short setup. Adverse move: est. {loss_multiple:+.0f}%")
