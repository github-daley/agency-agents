# Twitter Thread: Merkl Trial Explainer
**Account**: @telcoinTAO
**Date drafted**: March 12, 2026
**Status**: DRAFT — pending publish-ready checklist sign-off
**Format**: 7-tweet thread
**Target audience**: DeFi-aware TEL holders, TELx liquidity miners, governance participants

---

## PUBLISH-READY CHECKLIST

Review the following before posting. Items marked [VERIFY] require council confirmation.

- [VERIFY] **363,000 TEL/month figure** — derived from the research file (~2.175M TEL over 6 months). Confirm the council-approved monthly figure is exactly 363,000 TEL and not a rounded approximation before going live.
- [VERIFY] **"~4 weeks from snapshot to live"** — research file notes "~4 weeks from snapshot → live ~April 2026." Confirm this timeline has not shifted given that the snapshot closed March 10.
- [VERIFY] **"6/6 unanimous"** — confirm voter count was exactly 6 eligible votes and all 6 were cast in favor (not 6 out of a larger eligible set with others abstaining).
- [VERIFY] **$6,000 integration cost** — sourced from research file (per-position model). Confirm this is a public-facing figure the council is comfortable disclosing.
- [CONFIRM] **Mid-May 2026 analysis date** — confirm this is still the target review window; flag if the TELx Council meeting on March 18 changes this.
- [CONFIRM] **"No double rewards"** — confirm the parallel test setup means LPs in the TEL/ETH pool on Base V4 receive rewards from one system only (Merkl OR current hook), not both simultaneously.
- [NOTE] The 10M TEL TX operational wallet figure is in the research file. The thread does not mention this wallet balance directly — confirm whether it is appropriate to reference it publicly if asked in replies.

---

## THREAD

---

**Tweet 1 of 7**

TELx governance just recorded its first unanimous council vote.

On March 10, the TELx Council passed a snapshot proposal 6/6 — approving a live trial of Merkl for liquidity incentive distribution.

Here is what was voted on, how it works, and what it means for LPs.

---

**Tweet 2 of 7**

First: what is Merkl?

Merkl is an incentive distribution system built by Angle Labs. TELx did not build it — it is external infrastructure that TELx is evaluating for adoption.

It distributes LP rewards dynamically, targeting active liquidity positions rather than applying a fixed allocation across all pools equally.

---

**Tweet 3 of 7**

Why is TELx looking at this?

The current hook-based system works. But it has limits as TELx scales.

Merkl enables:
- Per-position gating (rewards go to active ticks, not idle capital)
- Bounded price range support
- Per-pool configuration without rewriting hooks
- Flexible structure for adding new pools quickly

The goal is more precise incentive targeting — especially as eXYZ stablecoin pools and new corridors come online.

---

**Tweet 4 of 7**

The trial specifics:

- Pool: TEL/ETH on Base V4 (Uniswap V4)
- Rewards: ~363,000 TEL per month
- Duration: 6 months
- Analysis checkpoint: mid-May 2026
- Go-live: approximately April 2026 (~4 weeks from snapshot close)

Funding comes from the TX operational wallet — the trial does not reduce existing pool incentives.

---

**Tweet 5 of 7**

Critically: this is a parallel test.

Merkl runs alongside the current hook system on the TEL/ETH pool — not replacing it.

There are no double rewards. The purpose is a controlled comparison: does Merkl distribute incentives more efficiently than the current setup?

Real data from a live pool. Six months. Then governance reviews the results.

---

**Tweet 6 of 7**

What this means for LPs right now:

If you are providing liquidity in the TEL/ETH pool on Base V4, you are part of the first governance-approved experiment in TELx's incentive infrastructure.

This is not a product launch. It is a structured trial with a defined review date — exactly how a governance-driven protocol should test new systems before committing to them.

---

**Tweet 7 of 7**

The bigger picture:

TELx has six active pools across Polygon and Base. As eXYZ stablecoins and new remittance corridors scale, the incentive system needs to scale with them.

The vote was unanimous. The trial has defined parameters. The analysis has a date.

This is TELx governance working as designed — data first, then decisions.

Forum thread with full detail: forum.telcoin.org

---

## PRODUCTION NOTES

**Companion content flagged for follow-up:**
This thread has strong potential for a companion post on forum.telcoin.org. A forum post would allow fuller treatment of: the per-position vs. per-wallet model tradeoff, the $6,000 integration cost context, the strategic rationale for formula-based pool allocation as eXYZ scales, and a plain-language FAQ for LPs. Recommended to draft and publish on the forum before or simultaneously with this thread so the final tweet's forum link is live at posting time.

**Suggested thread visual (optional):**
A simple diagram showing the parallel test structure — Merkl vs. hook system running simultaneously on the TEL/ETH Base V4 pool — would improve comprehension for tweet 5. Flag for design team if visual assets are being prepared for this drop.

**Reply preparedness:**
Community questions likely to follow (per intel-x-2026-03-12.md Gap 5): "What does this mean for my LP rewards?" and "When exactly does this go live?" Have reply copy ready. Do not speculate on yield improvement — the trial exists precisely because that data does not exist yet.

**Timing recommendation:**
Do not post until the publish-ready checklist above is cleared. If the TELx Council on March 18 updates any figures, revise before publishing. Ideal window: 1–2 weeks before the April go-live date to build anticipation without leaving too much time for questions the team cannot yet answer.
