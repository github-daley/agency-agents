# TarsierAlpha v2 — Integration Guide
## Shorts Scanner + Portfolio Hedge + Agentic API

This directory contains all new/modified files for the v2 feature set.
Follow these steps **in order** to apply them to your Replit project.

---

## File Map

| File | Action | Destination |
|------|--------|-------------|
| `scoring_additions.py` | Paste functions into | `scoring.py` |
| `options_selector_additions.py` | Paste functions into | `options_selector.py` |
| `scanner_shorts.py` | **New file** | root of project |
| `hedge.py` | **New file** | root of project |
| `agent_routes.py` | **New file** | root of project |
| `app_additions.py` | Follow inline instructions | `app.py` |
| `market_regime_additions.py` | Follow inline instructions | `market_regime.py` |
| `migrations.sql` | See Step 2 below | `app.py` (_init_database) |
| `templates/hedge.html` | **New file** | `templates/hedge.html` |
| `templates/partials/shorts_beta_banner.html` | **New file** | `templates/partials/` |
| `templates/partials/shorts_tab.html` | **New file** | `templates/partials/` |

---

## Step 1 — New/Drop-in Files

Copy these directly to your Replit root:
```
scanner_shorts.py
hedge.py
agent_routes.py
templates/hedge.html
templates/partials/shorts_beta_banner.html
templates/partials/shorts_tab.html
```

---

## Step 2 — Database Migrations

Open `app.py` and find the `migrations = [...]` list inside `_init_database()`.
Append these strings to the list:

```python
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
```

The migrations run automatically on next app boot via `_init_database()`.

---

## Step 3 — Model Columns

Open `models.py`. Add these columns to the relevant classes:

### User (after `accepted_disclaimer`)
```python
shorts_enabled = db.Column(db.Boolean, default=False)
```

### Candidate (after `entry_window_status`)
```python
side = db.Column(db.String(5), default='long')
badges = db.Column(db.Text)
leverage = db.Column(db.Float)
risk_note = db.Column(db.String(200))
```

### PaperTrade (after `exit_reason`)
```python
side = db.Column(db.String(5), default='long')
hedge_group_id = db.Column(db.String(50))
```

### ScanRun (after `catalyst_found`)
```python
shorts_found = db.Column(db.Integer, default=0)
```

> The `ALTER TABLE` migrations in Step 2 handle the DB side.
> These model additions keep SQLAlchemy in sync.

---

## Step 4 — scoring.py

Open `scoring.py` and paste all functions from `scoring_additions.py` at the bottom:
- `score_short()`
- `score_short_for_hedge()`
- `build_risk_note()`

---

## Step 5 — options_selector.py

Open `options_selector.py` and:

1. **Replace** the existing `save_option_candidate()` with the version from
   `options_selector_additions.py` (adds `option_type` parameter).

2. **Paste** all new functions at the bottom:
   - `_get_scanner_put_chain()`
   - `find_best_put()`
   - `select_put_options_for_candidate()`
   - `_update_candidate_option_fields_short()`

---

## Step 6 — app.py

### 6a. Imports (near the top, with existing imports)
```python
from agent_routes import agent_bp
from hedge import generate_hedge_basket, enter_paper_hedge_basket, get_available_industries
```

### 6b. Register the agent blueprint (after existing blueprint registrations)
```python
app.register_blueprint(agent_bp)
```

### 6c. Add routes (paste at the end of app.py, before `if __name__ == '__main__':`)

Copy the route registration block from the bottom of `app_additions.py`:

```python
app.add_url_rule('/admin/shorts/toggle',
                 'admin_shorts_toggle',
                 _route_admin_shorts_toggle,
                 methods=['POST'])

app.add_url_rule('/api/hedge/suggest',
                 'hedge_suggest',
                 _route_hedge_suggest,
                 methods=['POST'])

app.add_url_rule('/api/hedge/enter',
                 'hedge_enter',
                 _route_hedge_enter,
                 methods=['POST'])

@app.route('/hedge')
@require_onboarded
def hedge_page():
    return _route_hedge_page()

@app.route('/api/shorts/candidates')
@require_onboarded
def shorts_candidates():
    return _route_shorts_candidates()
```

Also paste the four route functions (`_route_admin_shorts_toggle`, `_route_hedge_suggest`,
`_route_hedge_enter`, `_route_shorts_candidates`) from `app_additions.py`.

### 6d. Pass `shorts_enabled` to the dashboard template

In the existing `dashboard()` route, add `shorts_enabled=current_user.shorts_enabled`
to the `render_template('dashboard.html', ...)` call.

---

## Step 7 — market_regime.py

Follow the instructions in `market_regime_additions.py`:

1. Add `allow_shorts` and `allow_hedge` variables to each regime branch.
2. Add them to the `result` dict.
3. Update `_default_caution_regime()` to include the new keys.

Quick reference (from the file):
- `crisis` regime: `allow_shorts = True, allow_hedge = True`
- `risk_off` regime: `allow_shorts = True, allow_hedge = True`
- `caution` regime: `allow_shorts = True, allow_hedge = True`
- `bull` regime: `allow_shorts = False, allow_hedge = False`

---

## Step 8 — scanner.py (add Phase 6)

In `run_scan()`, after the **Phase 5** block (paper trade check), add:

```python
logger.info("Phase 6: Shorts scan")
try:
    from scanner_shorts import run_shorts_scan
    from market_regime import get_market_regime
    regime = get_market_regime()
    if regime.get('allow_shorts', False):
        shorts_found = run_shorts_scan(app, scan_run)
        scan_run.shorts_found = shorts_found
        db.session.commit()
        logger.info(f"Phase 6 complete: {shorts_found} short candidates")
    else:
        logger.info(f"Phase 6 skipped: regime={regime['regime']} (allow_shorts=False)")
except Exception as e:
    logger.error(f"Phase 6 error (shorts): {e}")
```

### Phase 3b modification

In the Phase 3b paper trade loop, change:
```python
pt = create_paper_trade_for_candidate(cand, rec_option)
```
to:
```python
if getattr(cand, 'side', 'long') == 'short':
    from scanner_shorts import create_short_paper_trade
    pt = create_short_paper_trade(cand, rec_option)
else:
    pt = create_paper_trade_for_candidate(cand, rec_option)
```

---

## Step 9 — dashboard.html (add Shorts tab)

Follow the inline comments in `templates/partials/shorts_tab.html`.

1. Wrap the existing longs content in a Bootstrap tab pane `#longs-pane`
2. Add the nav tabs (Longs / Shorts / Hedge) above the filter form
3. Add `{% include 'partials/shorts_tab.html' %}` in the `#shorts-pane`
4. Add a Hedge pane with a link to `/hedge`

---

## Step 10 — Environment Variables

Add to Replit Secrets:

| Key | Value | Notes |
|-----|-------|-------|
| `AGENT_API_KEYS` | `your-key-1,your-key-2` | Comma-separated API keys for `/api/agent/*` endpoints |

---

## Step 11 — Enable Shorts (Admin Gate)

After deploying:
1. Go to `/admin`
2. Find your admin user
3. Call `POST /admin/shorts/toggle` with `{"user_id": "<your-id>", "enabled": true}`
   OR use the Enable button on the Shorts tab in the dashboard.

---

## Verification Checklist

- [ ] App boots without errors after changes
- [ ] Existing longs scan still works (run a manual scan)
- [ ] `GET /api/agent/scans?type=long` returns candidates with `X-Agent-Key` header
- [ ] `POST /api/hedge/suggest` with `{"industry":"trucking","exposureUsd":100000}` returns a basket
- [ ] `/hedge` page renders for admin users
- [ ] Shorts tab appears on dashboard for admin users
- [ ] After enabling shorts and running a scan: short candidates appear under Shorts tab
- [ ] `GET /api/agent/scans?type=short` returns short candidates when available
- [ ] Paper trade P&L at `GET /api/agent/pnl` shows `longs` and `shorts` split

---

## Architecture Summary

```
New files:
  scanner_shorts.py   ─ Phase 6 shorts pipeline
  hedge.py            ─ industry → PUT basket generator
  agent_routes.py     ─ /api/agent/* Blueprint

Modified files:
  scoring.py          ─ + score_short(), score_short_for_hedge(), build_risk_note()
  options_selector.py ─ + find_best_put(), select_put_options_for_candidate()
                          modified save_option_candidate() (option_type param)
  app.py              ─ + 5 routes, 2 blueprints, migrations
  market_regime.py    ─ + allow_shorts, allow_hedge flags
  scanner.py          ─ + Phase 6 hook, Phase 3b short paper trade fork
  models.py           ─ + side, badges, leverage, risk_note, hedge_group_id columns

New templates:
  templates/hedge.html
  templates/partials/shorts_beta_banner.html
  templates/partials/shorts_tab.html
```
