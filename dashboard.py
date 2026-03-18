"""
dashboard.py — Terminal-style Polymarket LP Bot dashboard.

Run alongside the bot:
    pip install streamlit
    streamlit run dashboard.py

Auto-refreshes every 3 seconds.
"""

import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import streamlit as st

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Polymarket LP Bot",
    page_icon="▶",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Terminal CSS ──────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');

  html, body, [class*="css"] {
    font-family: 'JetBrains Mono', 'Courier New', monospace !important;
    background-color: #0d0d0d !important;
    color: #c8c8c8 !important;
  }
  .stApp { background-color: #0d0d0d; }

  /* Header bar */
  .term-header {
    background: #111;
    border: 1px solid #2a2a2a;
    border-bottom: 2px solid #00ff88;
    padding: 10px 16px;
    font-size: 13px;
    color: #00ff88;
    letter-spacing: 0.05em;
    margin-bottom: 12px;
  }

  /* Section boxes */
  .term-box {
    background: #111;
    border: 1px solid #2a2a2a;
    padding: 12px 14px;
    margin-bottom: 10px;
    font-size: 12px;
  }
  .term-box-title {
    color: #00aaff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.12em;
    border-bottom: 1px solid #2a2a2a;
    padding-bottom: 5px;
    margin-bottom: 8px;
  }

  /* Stat tiles */
  .stat-grid { display: flex; gap: 8px; margin-bottom: 10px; }
  .stat-tile {
    flex: 1;
    background: #151515;
    border: 1px solid #2a2a2a;
    padding: 10px 14px;
    text-align: center;
  }
  .stat-label { color: #555; font-size: 10px; letter-spacing: 0.1em; }
  .stat-value { color: #e0e0e0; font-size: 18px; font-weight: 700; margin-top: 2px; }
  .stat-value.green  { color: #00ff88; }
  .stat-value.red    { color: #ff4444; }
  .stat-value.yellow { color: #ffcc00; }
  .stat-value.blue   { color: #00aaff; }

  /* Tables */
  .term-table { width: 100%; border-collapse: collapse; font-size: 11.5px; }
  .term-table th {
    color: #555;
    font-size: 10px;
    letter-spacing: 0.1em;
    text-align: left;
    padding: 3px 8px;
    border-bottom: 1px solid #222;
  }
  .term-table td { padding: 4px 8px; border-bottom: 1px solid #1a1a1a; }
  .term-table tr:hover td { background: #161616; }

  .buy    { color: #00aaff; }
  .sell   { color: #ffcc00; }
  .win    { color: #00ff88; }
  .loss   { color: #ff4444; }
  .settle { color: #aa88ff; }
  .dim    { color: #555; }
  .up     { color: #00cc66; }
  .down   { color: #ff6655; }

  /* Time left colors */
  .time-ok     { color: #00ff88; }
  .time-warn   { color: #ffcc00; }
  .time-urgent { color: #ff4444; }

  /* Hide streamlit chrome */
  #MainMenu { visibility: hidden; }
  footer    { visibility: hidden; }
  header    { visibility: hidden; }
  .block-container { padding-top: 0.5rem; padding-bottom: 0; max-width: 100%; }
</style>
""", unsafe_allow_html=True)

LOG_FILE    = "bot_trades.csv"
REFRESH_SEC = 3


# ── Data loader ───────────────────────────────────────────────
@st.cache_data(ttl=REFRESH_SEC)
def load_trades(path: str) -> pd.DataFrame:
    if not Path(path).exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(path, parse_dates=["timestamp"])
        df = df[df["success"] == True].copy()
        for col in ("market_end_ts", "pnl_usdc"):
            if col not in df.columns:
                df[col] = 0.0
        df["market_end_ts"] = pd.to_numeric(df["market_end_ts"], errors="coerce").fillna(0)
        df["pnl_usdc"]      = pd.to_numeric(df["pnl_usdc"],      errors="coerce").fillna(0)
        return df.sort_values("timestamp").reset_index(drop=True)
    except Exception:
        return pd.DataFrame()


def fmt_time_left(end_ts: float) -> str:
    """Format seconds remaining as mm:ss or EXPIRED."""
    if not end_ts:
        return "—"
    secs = int(end_ts - time.time())
    if secs <= 0:
        return "EXPIRED"
    m, s = divmod(secs, 60)
    return f"{m}m {s:02d}s"


def time_left_class(end_ts: float) -> str:
    if not end_ts:
        return "dim"
    secs = end_ts - time.time()
    if secs <= 0:
        return "dim"
    if secs < 60:
        return "time-urgent"
    if secs < 120:
        return "time-warn"
    return "time-ok"


def short_question(q: str) -> str:
    if not q:
        return "—"
    # Strip "Up or Down -" prefix pattern and trim
    for prefix in ("Up or Down - ", "up or down - "):
        if prefix in q:
            q = q.split(prefix, 1)[-1]
    return q[:48]


def outcome_html(outcome: str) -> str:
    cls = "up" if outcome == "Up" else "down"
    return f'<span class="{cls}">{outcome}</span>'


def side_html(side: str) -> str:
    mapping = {"BUY": "buy", "SELL": "sell", "SETTLE": "settle"}
    cls = mapping.get(side, "dim")
    return f'<span class="{cls}">{side}</span>'


def pnl_html(pnl: float) -> str:
    if pnl > 0:
        return f'<span class="win">+${pnl:.2f}</span>'
    elif pnl < 0:
        return f'<span class="loss">-${abs(pnl):.2f}</span>'
    return f'<span class="dim">$0.00</span>'


# ── Load data ─────────────────────────────────────────────────
df = load_trades(LOG_FILE)
now_ts = time.time()
now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

if df.empty:
    st.markdown(f"""
    <div class="term-header">▶ POLYMARKET LP BOT &nbsp;|&nbsp; {now_str}</div>
    <div class="term-box">
      <div class="dim">No trades yet. Start the bot: <b>python run_bot.py</b></div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(REFRESH_SEC)
    st.rerun()

# ── Derived sets ──────────────────────────────────────────────
buys    = df[df["side"] == "BUY"]
settles = df[df["side"] == "SETTLE"]
wins    = settles[settles["fill_price"] >= 0.99]
losses  = settles[settles["fill_price"] < 0.01]

# Open positions: BUY records with no SETTLE for same market_id+outcome
settled_keys = set(zip(settles["market_id"], settles["outcome"]))
open_mask = buys.apply(
    lambda r: (r["market_id"], r["outcome"]) not in settled_keys, axis=1
)
open_buys = buys[open_mask].copy()

total_invested = buys["size_usdc"].sum()
total_won_usdc = wins["size_usdc"].sum()
total_pnl      = settles["pnl_usdc"].sum()
open_exposure  = open_buys["size_usdc"].sum()

# ── Header bar ────────────────────────────────────────────────
mode_str = df["mode"].iloc[-1].upper() if "mode" in df.columns and not df.empty else "PAPER"
pnl_color = "green" if total_pnl >= 0 else "red"
pnl_sign  = "+" if total_pnl >= 0 else ""

st.markdown(f"""
<div class="term-header">
  ▶ POLYMARKET LP BOT &nbsp;|&nbsp; {mode_str} &nbsp;|&nbsp; {now_str}
</div>
<div class="stat-grid">
  <div class="stat-tile">
    <div class="stat-label">TOTAL TRADES</div>
    <div class="stat-value blue">{len(buys):,}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">OPEN</div>
    <div class="stat-value yellow">{len(open_buys):,}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">WON</div>
    <div class="stat-value green">{len(wins):,}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">LOST</div>
    <div class="stat-value red">{len(losses):,}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">WIN RATE</div>
    <div class="stat-value {'green' if len(wins) >= len(losses) else 'red'}">
      {(len(wins) / (len(wins)+len(losses))*100) if (len(wins)+len(losses)) > 0 else 0:.1f}%
    </div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">REALISED P&amp;L</div>
    <div class="stat-value {pnl_color}">{pnl_sign}${total_pnl:.2f}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">OPEN EXPOSURE</div>
    <div class="stat-value yellow">${open_exposure:.2f}</div>
  </div>
  <div class="stat-tile">
    <div class="stat-label">TOTAL INVESTED</div>
    <div class="stat-value">${total_invested:.2f}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Open Positions ────────────────────────────────────────────
if not open_buys.empty:
    rows_html = ""
    # Aggregate by market+outcome for display
    grp = open_buys.groupby(["market_id", "question", "outcome", "market_end_ts"]).agg(
        cost=("size_usdc", "sum"),
        tokens=("tokens", "sum"),
        avg_price=("fill_price", "mean"),
    ).reset_index()

    for _, r in grp.sort_values("market_end_ts").iterrows():
        tl    = fmt_time_left(r["market_end_ts"])
        tl_cls = time_left_class(r["market_end_ts"])
        q_str  = short_question(str(r.get("question", "")))
        rows_html += f"""
        <tr>
          <td>{q_str}</td>
          <td>{outcome_html(r['outcome'])}</td>
          <td>{r['avg_price']:.4f}</td>
          <td>${r['cost']:.2f}</td>
          <td>{r['tokens']:.4f}</td>
          <td><span class="{tl_cls}">{tl}</span></td>
        </tr>"""

    st.markdown(f"""
    <div class="term-box">
      <div class="term-box-title">── OPEN POSITIONS ({len(grp)})</div>
      <table class="term-table">
        <tr>
          <th>MARKET</th><th>SIDE</th><th>AVG ENTRY</th>
          <th>COST</th><th>TOKENS</th><th>TIME LEFT</th>
        </tr>
        {rows_html}
      </table>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="term-box">
      <div class="term-box-title">── OPEN POSITIONS (0)</div>
      <span class="dim">No open positions.</span>
    </div>
    """, unsafe_allow_html=True)

# ── Two-column: Won | Lost ────────────────────────────────────
col_won, col_lost = st.columns(2)

with col_won:
    if not wins.empty:
        rows_html = ""
        for _, r in wins.tail(30).sort_values("timestamp", ascending=False).iterrows():
            ts = r["timestamp"].strftime("%H:%M:%S") if hasattr(r["timestamp"], "strftime") else str(r["timestamp"])[:19]
            q  = short_question(str(r.get("question", "")))
            rows_html += f"""
            <tr>
              <td class="dim">{ts}</td>
              <td>{outcome_html(r['outcome'])}</td>
              <td class="dim">{r['price']:.4f}</td>
              <td class="win">${r['size_usdc']:.2f}</td>
              <td>{pnl_html(r['pnl_usdc'])}</td>
            </tr>"""
        st.markdown(f"""
        <div class="term-box">
          <div class="term-box-title">── WON ({len(wins):,}) &nbsp; total=${wins['size_usdc'].sum():.2f}</div>
          <table class="term-table">
            <tr><th>TIME</th><th>SIDE</th><th>ENTRY</th><th>PAYOUT</th><th>P&L</th></tr>
            {rows_html}
          </table>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="term-box">
          <div class="term-box-title">── WON (0)</div>
          <span class="dim">No wins yet.</span>
        </div>
        """, unsafe_allow_html=True)

with col_lost:
    if not losses.empty:
        rows_html = ""
        for _, r in losses.tail(30).sort_values("timestamp", ascending=False).iterrows():
            ts = r["timestamp"].strftime("%H:%M:%S") if hasattr(r["timestamp"], "strftime") else str(r["timestamp"])[:19]
            q  = short_question(str(r.get("question", "")))
            rows_html += f"""
            <tr>
              <td class="dim">{ts}</td>
              <td>{outcome_html(r['outcome'])}</td>
              <td class="dim">{r['price']:.4f}</td>
              <td class="loss">$0.00</td>
              <td>{pnl_html(r['pnl_usdc'])}</td>
            </tr>"""
        st.markdown(f"""
        <div class="term-box">
          <div class="term-box-title">── LOST ({len(losses):,}) &nbsp; total=${losses['pnl_usdc'].abs().sum():.2f} lost</div>
          <table class="term-table">
            <tr><th>TIME</th><th>SIDE</th><th>ENTRY</th><th>PAYOUT</th><th>P&L</th></tr>
            {rows_html}
          </table>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="term-box">
          <div class="term-box-title">── LOST (0)</div>
          <span class="dim">No losses yet.</span>
        </div>
        """, unsafe_allow_html=True)

# ── Trade Log ─────────────────────────────────────────────────
recent = df.tail(80).sort_values("timestamp", ascending=False)
rows_html = ""
for _, r in recent.iterrows():
    ts    = r["timestamp"].strftime("%H:%M:%S") if hasattr(r["timestamp"], "strftime") else str(r["timestamp"])[:19]
    q     = short_question(str(r.get("question", "")))
    price = f"{r['fill_price']:.4f}"
    size  = f"${r['size_usdc']:.2f}"
    pnl   = pnl_html(r["pnl_usdc"]) if r["side"] == "SETTLE" else '<span class="dim">—</span>'
    rows_html += f"""
    <tr>
      <td class="dim">{ts}</td>
      <td>{side_html(r['side'])}</td>
      <td>{outcome_html(r['outcome'])}</td>
      <td class="dim">{price}</td>
      <td>{size}</td>
      <td>{pnl}</td>
      <td class="dim" style="font-size:10px">{q}</td>
    </tr>"""

st.markdown(f"""
<div class="term-box">
  <div class="term-box-title">── TRADE LOG (last {len(recent)} of {len(df)})</div>
  <table class="term-table">
    <tr>
      <th>TIME</th><th>TYPE</th><th>SIDE</th>
      <th>PRICE</th><th>SIZE</th><th>P&L</th><th>MARKET</th>
    </tr>
    {rows_html}
  </table>
</div>
<div class="dim" style="font-size:10px; text-align:right; padding: 4px 0;">
  auto-refresh every {REFRESH_SEC}s &nbsp;|&nbsp; {now_str}
</div>
""", unsafe_allow_html=True)

# ── Export ───────────────────────────────────────────────────
st.markdown("""
<div class="term-box">
  <div class="term-box-title">── EXPORT TRADES FOR COMPARISON</div>
</div>
""", unsafe_allow_html=True)

# Build a comparison-friendly export that mirrors the original trade CSV format
if not buys.empty:
    export = buys[["timestamp", "question", "outcome", "fill_price", "size_usdc", "tokens", "market_end_ts"]].copy()
    export.columns = ["timestamp", "market", "outcome", "entry_price", "size_usdc", "tokens", "market_end_ts"]

    # Attach settlement info
    settle_lookup = settles.set_index(["market_id", "outcome"])[["fill_price", "pnl_usdc", "timestamp"]].copy()
    settle_lookup.columns = ["payout_price", "pnl_usdc", "settled_at"]

    buy_keys = list(zip(buys["market_id"], buys["outcome"]))
    export["payout_price"] = [
        settle_lookup.loc[(mid, out), "payout_price"]
        if (mid, out) in settle_lookup.index else None
        for mid, out in zip(buys["market_id"], buys["outcome"])
    ]
    export["pnl_usdc"] = [
        settle_lookup.loc[(mid, out), "pnl_usdc"]
        if (mid, out) in settle_lookup.index else None
        for mid, out in zip(buys["market_id"], buys["outcome"])
    ]
    export["settled_at"] = [
        settle_lookup.loc[(mid, out), "settled_at"]
        if (mid, out) in settle_lookup.index else None
        for mid, out in zip(buys["market_id"], buys["outcome"])
    ]
    export["result"] = export["payout_price"].apply(
        lambda p: "WIN" if p is not None and p >= 0.99
        else ("LOSS" if p is not None and p < 0.01 else "OPEN")
    )
    export["market_end_ts"] = export["market_end_ts"].apply(
        lambda ts: datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S UTC")
        if ts and ts > 0 else ""
    )

    export_csv = export.to_csv(index=False)
    fname = f"bot_trades_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    st.download_button(
        label="⬇  Download trade export CSV",
        data=export_csv,
        file_name=fname,
        mime="text/csv",
        help="Download a CSV comparing bot trades to the original account format",
    )

    # Preview the first 10 rows
    st.markdown(f"""
    <div style="font-size:11px; color:#555; margin-top:6px; margin-bottom:4px;">
      Preview — {len(export)} trades &nbsp;|&nbsp; {len(export[export['result']=='WIN'])} wins &nbsp;
      {len(export[export['result']=='LOSS'])} losses &nbsp;
      {len(export[export['result']=='OPEN'])} open
    </div>
    """, unsafe_allow_html=True)
    st.dataframe(
        export.head(10),
        use_container_width=True,
        hide_index=True,
    )
else:
    st.markdown('<div style="color:#555; font-size:12px; padding:4px 0;">No trades to export yet.</div>',
                unsafe_allow_html=True)

# ── Auto-refresh ──────────────────────────────────────────────
time.sleep(REFRESH_SEC)
st.rerun()
