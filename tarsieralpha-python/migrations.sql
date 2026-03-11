-- TarsierAlpha v2: Shorts + Portfolio Hedge + Agentic API
-- Run via _init_database() in app.py  (ALTER TABLE ... ADD COLUMN IF NOT EXISTS pattern)
-- ─────────────────────────────────────────────────────────────────────────────
-- These SQL statements belong inside the `migrations` list in app.py's
-- _init_database() function. Add them after the existing entries.
-- ─────────────────────────────────────────────────────────────────────────────

-- 1. User: shorts opt-in flag (admin gates this; users flip it when enabled)
ALTER TABLE users ADD COLUMN IF NOT EXISTS shorts_enabled BOOLEAN DEFAULT FALSE;

-- 2. Candidate: trade direction + short-specific metadata
ALTER TABLE candidates ADD COLUMN IF NOT EXISTS side VARCHAR(5) DEFAULT 'long';
ALTER TABLE candidates ADD COLUMN IF NOT EXISTS badges TEXT;          -- JSON array: ["theta_burn","margin_alert"]
ALTER TABLE candidates ADD COLUMN IF NOT EXISTS leverage FLOAT;       -- stock_price / put_premium
ALTER TABLE candidates ADD COLUMN IF NOT EXISTS risk_note VARCHAR(200); -- "Stock +10% → est. -300% on put"

-- 3. PaperTrade: track direction + hedge basket grouping
ALTER TABLE paper_trades ADD COLUMN IF NOT EXISTS side VARCHAR(5) DEFAULT 'long';
ALTER TABLE paper_trades ADD COLUMN IF NOT EXISTS hedge_group_id VARCHAR(50); -- links basket members

-- 4. ScanRun: short candidate counter
ALTER TABLE scan_runs ADD COLUMN IF NOT EXISTS shorts_found INTEGER DEFAULT 0;

-- ─────────────────────────────────────────────────────────────────────────────
-- Indexes for new columns
-- ─────────────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_cand_side ON candidates(side);
CREATE INDEX IF NOT EXISTS idx_pt_side ON paper_trades(side);
CREATE INDEX IF NOT EXISTS idx_pt_hedge_group ON paper_trades(hedge_group_id);
