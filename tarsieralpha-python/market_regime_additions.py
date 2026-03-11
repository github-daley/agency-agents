"""
market_regime_additions.py — TarsierAlpha v2
=============================================
Modify market_regime.py to add `allow_shorts` and `allow_hedge` flags.

ONLY 3 changes needed in market_regime.py:

1. In the `if vix >= VIX_EXTREME:` block, add:
       allow_shorts = True   # shorts thrive in crisis
       allow_hedge = True

2. In the `elif vix >= VIX_HIGH:` block, add:
       allow_shorts = True   # risk-off = good short environment
       allow_hedge = True

3. In the `elif vix >= VIX_ELEVATED ...` block, add:
       allow_shorts = True
       allow_hedge = True

4. In the `else:` (bull) block, add:
       allow_shorts = False  # longs-only in bull market (risk/reward unfavorable)
       allow_hedge = False

5. Add both flags to the `result` dict.

──────────────────────────────────────────────────
FULL MODIFIED REGIME LOGIC (paste over existing block)
──────────────────────────────────────────────────
"""

# ─── PASTE THIS over the existing if/elif/else regime block in market_regime.py ─────

_MODIFIED_BLOCK = '''
        if vix >= VIX_EXTREME:
            regime = 'crisis'
            allow_gap_fill = False
            allow_oversold = False
            allow_catalyst = False
            allow_shorts = True       # shorts are ideal in crisis
            allow_hedge = True
            pause_all = True
            reason = f"VIX at {vix:.1f} — crisis level. Long entries paused. Shorts/hedge active."
        elif vix >= VIX_HIGH:
            regime = 'risk_off'
            allow_gap_fill = False
            allow_oversold = True
            allow_catalyst = False
            allow_shorts = True       # risk-off = favorable short environment
            allow_hedge = True
            pause_all = False
            reason = f"VIX at {vix:.1f}. Risk-off. Shorts/hedge active; gap fills paused."
        elif vix >= VIX_ELEVATED and not spy_above_sma20:
            regime = 'caution'
            allow_gap_fill = True
            allow_oversold = True
            allow_catalyst = False
            allow_shorts = True       # caution = short setups starting to form
            allow_hedge = True
            pause_all = False
            reason = f"VIX at {vix:.1f}, SPY below 20SMA ({spy_sma20:.2f}). Caution — catalysts paused."
        else:
            regime = 'bull'
            allow_gap_fill = True
            allow_oversold = True
            allow_catalyst = True
            allow_shorts = False      # longs-only in clean bull market
            allow_hedge = False       # hedges less cost-effective when VIX < 20
            pause_all = False
            reason = f"VIX at {vix:.1f}, SPY above 20SMA. Normal conditions — longs only."
'''

# ─── UPDATE the `result` dict to include allow_shorts and allow_hedge ─────────────
# Find:
#         result = {
#             'regime': regime,
#             ...
#             'pause_all': pause_all,
#             'reason': reason
#         }
#
# Replace with:
_MODIFIED_RESULT = '''
        result = {
            'regime': regime,
            'vix': round(vix, 2),
            'spy_price': round(spy_price, 2),
            'spy_sma20': round(spy_sma20, 2),
            'spy_above_sma20': spy_above_sma20,
            'spy_trend': spy_trend,
            'allow_gap_fill': allow_gap_fill,
            'allow_oversold': allow_oversold,
            'allow_catalyst': allow_catalyst,
            'allow_shorts': allow_shorts,
            'allow_hedge': allow_hedge,
            'pause_all': pause_all,
            'reason': reason
        }
'''

# ─── Also update _default_caution_regime() ────────────────────────────────────────
_MODIFIED_DEFAULT_REGIME = '''
def _default_caution_regime(reason):
    regime_result = {
        'regime': 'caution',
        'vix': None,
        'spy_price': None,
        'spy_sma20': None,
        'spy_above_sma20': False,
        'spy_trend': 'neutral',
        'allow_gap_fill': True,
        'allow_oversold': True,
        'allow_catalyst': False,
        'allow_shorts': True,    # allow shorts in uncertainty
        'allow_hedge': True,
        'pause_all': False,
        'reason': reason
    }
    _regime_cache['result'] = regime_result
    _regime_cache['ts'] = _time.time() - (CACHE_TTL - 300)
    return regime_result
'''

# ─────────────────────────────────────────────────────────────────────────────
# SCANNER HOOK — in scanner.py Phase 6 (shorts), gate on regime:
# ─────────────────────────────────────────────────────────────────────────────
#
#     regime = get_market_regime()
#     if not regime.get('allow_shorts', False):
#         logger.info(f"Phase 6 (Shorts): Skipped — regime={regime['regime']} (shorts not allowed)")
#         return 0
#
# Add this check inside run_shorts_scan() in scanner_shorts.py
# BEFORE the ticker loop.
# ─────────────────────────────────────────────────────────────────────────────
