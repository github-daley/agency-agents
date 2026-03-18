# Agency Workflow SOPs
## Telcoin Association Marketing Agency

Standard operating procedures for running this agency through Claude Code. These replace the OpenClaw onboarding flow — no Telegram bot needed. The repo IS the agency.

---

## How This System Works

```
CLAUDE.md               ← Agency brain (auto-loaded every session)
    ↓
campaign/research/      ← Memory (source of truth for all client facts)
    ↓
campaign/AGENTS.md      ← Skills (who does what)
    ↓
campaign/execution/     ← Output (deliverables ready to publish)
    ↓
git push                ← Persistence (everything tracked, nothing lost)
```

Claude Code reads `CLAUDE.md` automatically. Every session starts with full agency context. No re-briefing required.

---

## Routine Triggers & What to Do

### New Council Call Recap Received
1. Paste recap into Claude chat
2. Claude updates `campaign/research/TELCOIN-RESEARCH.md` with new intel
3. Claude commits + pushes the update
4. Claude flags what campaign content the new info unlocks
5. Decide what to produce → run the relevant agent

### New Announcement / Press Release / Product Launch
1. Share the announcement with Claude
2. Claude verifies facts against `TELCOIN-RESEARCH.md` and updates if needed
3. Produce: tweet thread, forum post, community announcement (run agents in parallel)
4. Review outputs, approve, Claude pushes to branch

### Weekly Content Cadence
1. Start session: Claude reads current research + campaign state
2. Run `Social Media Strategist` agent for weekly calendar
3. Run `Content Creator` agents (parallel) for individual pieces
4. Review, edit, approve
5. Claude commits approved content to `campaign/execution/`

### Competitor / Market Intelligence Update
1. Run `Trend Researcher` agent: "What's happening with [Stellar/Ripple/Celo] this week?"
2. Capture findings in research file under Section 6 (Competitive Landscape)
3. Use intel to update messaging angles in upcoming content

### Community Question / FUD Response
1. Paste the question/comment to Claude
2. Run `Support Responder` agent for draft reply
3. Review, adjust tone, approve
4. No commit needed unless it becomes a template

---

## Starting a New Campaign from Scratch

1. **Brief Claude** — paste the objective, audience, key message, timeline
2. **Claude reads** `campaign/research/TELCOIN-RESEARCH.md` for relevant facts
3. **Run `Plan` agent** — produces a full campaign structure (audiences, deliverables, sequence)
4. **Approve the plan** — or iterate
5. **Run content agents in parallel** — one per deliverable type
6. **Review all outputs** — edit in Claude chat
7. **Claude commits** approved deliverables to `campaign/execution/[campaign-name]/`
8. **Push** → tracked, versioned, recoverable

---

## File Naming Conventions

```
campaign/execution/
  [topic]-tweet-thread-[date].md
  [topic]-forum-post-[date].md
  [topic]-press-release-[date].md
  [topic]-email-[audience]-[date].md

campaign/research/
  TELCOIN-RESEARCH.md    ← Always this single file (append, never replace)

campaign/briefs/
  [campaign-name]-brief-[date].md
```

---

## Git Workflow

You don't need to manage git manually. Claude handles it. But for reference:

- **Branch**: `claude/campaign-iLgt5` (always)
- **After any meaningful work**: Claude auto-commits and pushes
- **To review history**: `git log --oneline` shows all commits with messages
- **To see what's changed**: `git diff HEAD~1` shows last commit's changes
- **To roll back a bad commit**: tell Claude "revert the last commit" — it will handle it

---

## What Goes in `campaign/execution/` vs `campaign/research/`

| Content | Goes In |
|---|---|
| Tweet threads, posts, captions ready to publish | `execution/` |
| Forum posts, announcements, press releases | `execution/` |
| Client facts, product details, roadmap status | `research/TELCOIN-RESEARCH.md` |
| Council call intel, partnership info | `research/TELCOIN-RESEARCH.md` |
| Campaign briefs and strategy docs | `campaign/briefs/` |
| Editorial calendars | `execution/calendars/` |

---

## How to Talk to Claude for Best Results

**For content tasks**: Be specific about audience, platform, tone, and length. Always mention "use facts from TELCOIN-RESEARCH.md."

**For research updates**: Just paste the source material (recap, article, screenshot description). Claude will parse and update the file.

**For strategy**: Describe the goal and the constraint. Claude will structure the approach.

**For parallel work**: List multiple tasks in one message — "do X and Y at the same time." Claude will launch agents simultaneously.

**Tip**: The more specific the brief, the better the output. "Write a tweet about the bank charter" is weak. "Write a tweet for @telcoinTAO celebrating the first anniversary of the Nebraska digital asset bank charter, audience: crypto-native holders, tone: milestone + momentum, no hype, link to eUSD as the first output of the bank" is what gets you publish-ready copy.

---

## When to Update CLAUDE.md

Update `CLAUDE.md` when:
- A new client is added to the roster
- The working branch changes
- Campaign status changes significantly
- Tone/voice guidelines evolve
- New standing instructions need to persist across sessions

Just tell Claude: "Update CLAUDE.md to reflect [change]." It will edit and push.

---

## What This System Replaces

| OpenClaw Feature | This System's Equivalent |
|---|---|
| SOUL.md (agent personality) | `CLAUDE.md` Agency OS section |
| USER.md (your info + preferences) | `CLAUDE.md` Client + Workflow sections |
| MEMORY.md (long-term memory) | `campaign/research/TELCOIN-RESEARCH.md` |
| Skills system | Claude Code specialized agents (`AGENTS.md`) |
| QMD skill (chat log persistence) | Git commits — every action is tracked and recoverable |
| Brave Search | Claude Code's WebSearch + WebFetch tools |
| Telegram bot interface | Claude.ai chat or Claude Code CLI |
| Groq voice transcription | Paste voice note transcripts directly into chat |
| Always-on machine | Sessions resume with full context via `CLAUDE.md` |

The key difference: OpenClaw is one always-on bot. This is a full agency with specialized experts on call. You get a content strategist, a researcher, a brand guardian, a technical writer — all reading from the same verified source of truth.
