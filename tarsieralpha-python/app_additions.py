"""
app_additions.py — TarsierAlpha v2
====================================
These snippets belong in app.py.

──────────────────────────────────────────────────
1. IMPORTS  — add near the top of app.py
──────────────────────────────────────────────────

    from agent_routes import agent_bp
    from hedge import generate_hedge_basket, enter_paper_hedge_basket, get_available_industries

──────────────────────────────────────────────────
2. BLUEPRINT REGISTRATION — after existing blueprints
──────────────────────────────────────────────────

    app.register_blueprint(agent_bp)

──────────────────────────────────────────────────
3. MIGRATION ENTRIES — inside _init_database() migrations list
──────────────────────────────────────────────────
Add these strings to the `migrations` list in _init_database():

    "ALTER TABLE users ADD COLUMN IF NOT EXISTS shorts_enabled BOOLEAN DEFAULT FALSE",
    "ALTER TABLE candidates ADD COLUMN IF NOT EXISTS side VARCHAR(5) DEFAULT 'long'",
    "ALTER TABLE candidates ADD COLUMN IF NOT EXISTS badges TEXT",
    "ALTER TABLE candidates ADD COLUMN IF NOT EXISTS leverage FLOAT",
    "ALTER TABLE candidates ADD COLUMN IF NOT EXISTS risk_note VARCHAR(200)",
    "ALTER TABLE paper_trades ADD COLUMN IF NOT EXISTS side VARCHAR(5) DEFAULT 'long'",
    "ALTER TABLE paper_trades ADD COLUMN IF NOT EXISTS hedge_group_id VARCHAR(50)",
    "ALTER TABLE scan_runs ADD COLUMN IF NOT EXISTS shorts_found INTEGER DEFAULT 0",
    "CREATE INDEX IF NOT EXISTS idx_cand_side ON candidates(side)",
    "CREATE INDEX IF NOT EXISTS idx_pt_side ON paper_trades(side)",
    "CREATE INDEX IF NOT EXISTS idx_pt_hedge_group ON paper_trades(hedge_group_id)",

──────────────────────────────────────────────────
4. NEW ROUTES — paste into app.py (anywhere after existing routes)
──────────────────────────────────────────────────
"""

# ─────────────────────────────────────────────────────────────────────────────
# Copy everything below this line into app.py
# ─────────────────────────────────────────────────────────────────────────────

# Paste these imports at the top of app.py (with existing imports):
# from hedge import generate_hedge_basket, enter_paper_hedge_basket, get_available_industries


# ── Admin: Enable/disable shorts for a user ──────────────────────────────────

def _route_admin_shorts_toggle():
    """
    POST /admin/shorts/toggle
    Toggle shorts_enabled for a user (admin only).
    Body JSON: {"user_id": "...", "enabled": true}
    """
    from flask import request, jsonify
    from flask_login import current_user
    from models import db, User

    if not current_user.is_admin:
        return jsonify({'error': 'Admin only'}), 403

    data = request.get_json(silent=True) or {}
    user_id = data.get('user_id')
    enabled = bool(data.get('enabled', False))

    if not user_id:
        # Toggle for ALL users (admin broadcast)
        users = db.session.query(User).all()
        for u in users:
            u.shorts_enabled = enabled
        db.session.commit()
        return jsonify({'success': True, 'message': f"Shorts {'enabled' for all' if enabled else 'disabled for all'}"})

    user = db.session.get(User, user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.shorts_enabled = enabled
    db.session.commit()
    return jsonify({
        'success': True,
        'user_id': user_id,
        'shorts_enabled': enabled,
    })


# ── Hedge Mode: Suggest basket ────────────────────────────────────────────────

def _route_hedge_suggest():
    """
    POST /api/hedge/suggest
    Body JSON:
        {
          "industry": "trucking",
          "exposureUsd": 500000,
          "riskTolerance": "med"    (optional, default "med")
        }
    Returns: hedge basket JSON from generate_hedge_basket()
    """
    from flask import request, jsonify
    from hedge import generate_hedge_basket

    data = request.get_json(silent=True) or {}
    industry = data.get('industry', '').lower().strip()
    exposure_usd = data.get('exposureUsd', 0)
    risk_tolerance = data.get('riskTolerance', 'med').lower()

    if not industry:
        return jsonify({'error': 'industry is required'}), 400
    try:
        exposure_usd = float(exposure_usd)
    except (TypeError, ValueError):
        return jsonify({'error': 'exposureUsd must be a number'}), 400

    if exposure_usd <= 0:
        return jsonify({'error': 'exposureUsd must be greater than 0'}), 400

    try:
        basket = generate_hedge_basket(industry, exposure_usd, risk_tolerance)
        return jsonify(basket)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"Hedge suggest error: {e}")
        return jsonify({'error': 'Failed to generate basket'}), 500


# ── Hedge Mode: Enter paper basket ───────────────────────────────────────────

def _route_hedge_enter():
    """
    POST /api/hedge/enter
    Requires auth (require_onboarded).
    Body JSON: same as /api/hedge/suggest — re-generates and enters the basket.
    Returns: trade IDs, group_id, total_cost.
    """
    from flask import request, jsonify, current_app
    from flask_login import current_user
    from hedge import generate_hedge_basket, enter_paper_hedge_basket

    data = request.get_json(silent=True) or {}
    industry = data.get('industry', '').lower().strip()
    exposure_usd = float(data.get('exposureUsd', 0))
    risk_tolerance = data.get('riskTolerance', 'med').lower()

    try:
        basket = generate_hedge_basket(industry, exposure_usd, risk_tolerance)
        result = enter_paper_hedge_basket(basket, current_app._get_current_object())
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"Hedge enter error: {e}")
        return jsonify({'error': 'Failed to enter hedge basket'}), 500


# ── Hedge Mode: UI page ───────────────────────────────────────────────────────

def _route_hedge_page():
    """
    GET /hedge
    Render the hedge mode UI (admin-gated initially).
    """
    from flask import render_template
    from flask_login import current_user
    from hedge import get_available_industries

    if not current_user.is_admin:
        from flask import flash, redirect, url_for
        flash('Hedge Mode is in admin preview.', 'info')
        return redirect(url_for('dashboard'))

    industries = get_available_industries()
    return render_template('hedge.html', industries=industries)


# ── Shorts page (for dashboard integration) ──────────────────────────────────

def _route_shorts_candidates():
    """
    GET /shorts
    Admin-gated shorts candidate listing.
    Returns JSON for AJAX loading by the Shorts tab on the dashboard.
    """
    from flask import request, jsonify
    from flask_login import current_user
    from models import db, Candidate, Stock, OptionCandidate
    from sqlalchemy.orm import joinedload

    if not current_user.is_admin and not current_user.shorts_enabled:
        return jsonify({'error': 'Shorts not enabled for your account'}), 403

    min_score = request.args.get('minScore', 80, type=int)
    page = request.args.get('page', 1, type=int)
    per_page = 20

    query = (
        db.session.query(Candidate)
        .options(joinedload(Candidate.stock))
        .filter(Candidate.side == 'short')
        .filter(Candidate.status != 'archived')
        .filter(Candidate.total_score >= min_score)
        .order_by(Candidate.total_score.desc())
    )

    total = query.count()
    candidates = query.offset((page - 1) * per_page).limit(per_page).all()

    results = []
    for c in candidates:
        stock = c.stock
        rec_opt = db.session.query(OptionCandidate).filter_by(
            candidate_id=c.id, is_recommended=True
        ).first()

        import json
        try:
            badges = json.loads(c.badges) if c.badges else []
        except (TypeError, ValueError):
            badges = []

        results.append({
            'id': c.id,
            'ticker': stock.ticker if stock else '',
            'company': stock.company_name if stock else '',
            'setupType': c.strategy_type,
            'score': c.total_score,
            'entryPrice': c.entry_price,
            'targetPrice': c.target_price,
            'stopLoss': c.stop_loss,
            'leverage': c.leverage,
            'riskNote': c.risk_note,
            'badges': badges,
            'option': {
                'strike': rec_opt.strike_price,
                'expiry': rec_opt.expiration_date,
                'dte': rec_opt.days_to_expiry,
                'delta': rec_opt.delta,
                'mid': rec_opt.mid_price,
                'iv': rec_opt.implied_volatility,
            } if rec_opt else None,
            'createdAt': c.created_at.isoformat() if c.created_at else None,
        })

    return jsonify({
        'candidates': results,
        'total': total,
        'page': page,
        'totalPages': max(1, (total + per_page - 1) // per_page),
    })


# ─────────────────────────────────────────────────────────────────────────────
# REGISTER ROUTES
# Paste this block into app.py after all other route definitions,
# BEFORE the __main__ block.
# ─────────────────────────────────────────────────────────────────────────────
#
#  app.add_url_rule('/admin/shorts/toggle',
#                   'admin_shorts_toggle',
#                   _route_admin_shorts_toggle,
#                   methods=['POST'])
#
#  app.add_url_rule('/api/hedge/suggest',
#                   'hedge_suggest',
#                   _route_hedge_suggest,
#                   methods=['POST'])
#
#  app.add_url_rule('/api/hedge/enter',
#                   'hedge_enter',
#                   _route_hedge_enter,
#                   methods=['POST'])
#
#  @app.route('/hedge')
#  @require_onboarded
#  def hedge_page():
#      return _route_hedge_page()
#
#  @app.route('/api/shorts/candidates')
#  @require_onboarded
#  def shorts_candidates():
#      return _route_shorts_candidates()
#
# ─────────────────────────────────────────────────────────────────────────────
# SCANNER HOOK — add to scanner.py run_scan() after Phase 5
# ─────────────────────────────────────────────────────────────────────────────
#
#     logger.info("Phase 6: Shorts scan")
#     try:
#         from scanner_shorts import run_shorts_scan
#         shorts_found = run_shorts_scan(app, scan_run)
#         scan_run.shorts_found = shorts_found
#         db.session.commit()
#         logger.info(f"Phase 6 complete: {shorts_found} short candidates")
#     except Exception as e:
#         logger.error(f"Phase 6 error (shorts): {e}")
#
# ─────────────────────────────────────────────────────────────────────────────
# PAPER TRADE HOOK — modify Phase 3b in scanner.py
# In the loop where paper trades are created, replace:
#     pt = create_paper_trade_for_candidate(cand, rec_option)
# with:
#     if getattr(cand, 'side', 'long') == 'short':
#         from scanner_shorts import create_short_paper_trade
#         pt = create_short_paper_trade(cand, rec_option)
#     else:
#         pt = create_paper_trade_for_candidate(cand, rec_option)
# ─────────────────────────────────────────────────────────────────────────────
