# Agent Dispatch Guide
## Telcoin Association Marketing Agency

Quick reference for which specialized agent to invoke and how. Think of these as your agency's skill roster — each one is a specialist. Launch them via the Agent tool in Claude Code. Run multiple in parallel when tasks are independent.

---

## Content Production

### Social Media Copy (tweets, threads, captions)
**Agent**: `Content Creator`
**When**: Writing posts for @telcoinTAO, Instagram, LinkedIn, Telegram announcements
**Example prompt**:
> "Write a 7-tweet thread announcing the Merkl trial approval. Audience: crypto-native TEL holders. Tone: confident, factual, no hype. Facts from TELCOIN-RESEARCH.md: [paste relevant section]. End with a CTA to forum.telcoin.org."

**Agent**: `Social Media Strategist`
**When**: Building editorial calendars, cross-platform campaign planning, engagement strategy
**Example prompt**:
> "Build a 2-week Twitter/X content calendar for the lead-up to the Merkl trial going live in April. Mix: education, governance updates, builder spotlights, community engagement. Pull facts from campaign/research/TELCOIN-RESEARCH.md."

---

## Strategy & Planning

### Campaign Architecture
**Agent**: `Plan`
**When**: Designing a full campaign from brief to execution, mapping out deliverables, sequencing
**Example prompt**:
> "Plan the mainnet announcement campaign. Inputs: TELCOIN-RESEARCH.md. Audience tiers: MNO partners, crypto investors, telecom press, general crypto Twitter. Deliverables: press release, tweet thread, forum post, email to stakeholders. Map out sequence and dependencies."

### Brand & Messaging Consistency
**Agent**: `Brand Guardian`
**When**: Reviewing copy for voice consistency, checking messaging against brand rules, auditing published content
**Example prompt**:
> "Review these three draft tweets for brand consistency against the tone rules in CLAUDE.md. Flag any hype language, unverified claims, or off-brand phrasing."

---

## Research & Intelligence

### Market & Competitor Research
**Agent**: `Trend Researcher`
**When**: Competitive analysis, market positioning, trend identification, news monitoring
**Example prompt**:
> "Research how Stellar and Ripple are positioning their remittance products in Q1 2026. Look for recent press releases, blog posts, and social posts. I want to find gaps Telcoin can own in messaging."

### Codebase & Technical Exploration
**Agent**: `Explore`
**When**: Digging through GitHub repos, finding technical facts for content, verifying contract addresses or architecture
**Example prompt**:
> "Search github.com/Telcoin-Association for any documentation on how the GSMA validator onboarding process works. I need accurate technical language for a blog post."

---

## Written Content

### Long-form (blog, editorial, forum posts)
**Agent**: `Content Creator`
**When**: Medium-length to long-form pieces for Telcoin Magazine, forum.telcoin.org, external publications

### Developer-facing content
**Agent**: `Technical Writer`
**When**: Developer guides, onboarding docs, GitHub README updates, API reference content
**Example prompt**:
> "Write a developer onboarding guide for building on Telcoin Network. The network is EVM-compatible, builders can start on Base and redeploy at mainnet. Link to github.com/Telcoin-Association. Tone: clear, welcoming, technically precise."

### SEO / Web Copy
**Agent**: `SEO Specialist`
**When**: Website copy, landing pages, articles targeting search traffic
**Example prompt**:
> "Write SEO-optimized web copy for a landing page targeting 'bank-issued stablecoin' and 'regulated crypto remittance' keywords. Facts from TELCOIN-RESEARCH.md eUSD section."

---

## Community & Engagement

### Community Replies & Support
**Agent**: `Support Responder`
**When**: Drafting responses to community questions, handling FUD, reply templates for common questions on Reddit/X/Telegram

### Developer Advocacy Content
**Agent**: `Developer Advocate`
**When**: Content targeting builder community, hackathon materials, developer ecosystem messaging

---

## Analytics & Reporting

### Campaign Performance
**Agent**: `Analytics Reporter`
**When**: Interpreting social metrics, building performance reports, presenting data from council updates

---

## Visual Direction

### Image Prompts for AI-generated visuals
**Agent**: `Image Prompt Engineer`
**When**: Generating prompts for Midjourney/DALL-E/Flux for social graphics, campaign visuals, thumbnails
**Example prompt**:
> "Write 3 image generation prompts for a Twitter header image representing 'telecom-grade blockchain infrastructure'. Style: sleek, dark blue/purple, futuristic but credible. No cartoons. Professional."

---

## Parallelization Patterns

Run these combinations simultaneously (single message, multiple Agent tool calls):

**Launch week content blitz:**
- Agent 1 (`Content Creator`): Tweet thread
- Agent 2 (`Content Creator`): Forum announcement post
- Agent 3 (`Technical Writer`): Developer-facing blog post

**Research + strategy sprint:**
- Agent 1 (`Trend Researcher`): Competitive landscape snapshot
- Agent 2 (`Explore`): Technical fact-finding in GitHub repos
- Agent 3 (`Plan`): Campaign architecture draft

**Content calendar + copy production:**
- Agent 1 (`Social Media Strategist`): 2-week calendar
- Agent 2 (`Content Creator`): First week's posts
- Agent 3 (`Brand Guardian`): Review existing published content

---

## Rules for All Agents

When briefing any agent for client work, always include:
1. "Read `campaign/research/TELCOIN-RESEARCH.md` for verified facts"
2. The specific audience for this piece
3. Tone reference from CLAUDE.md
4. Any hard constraints (no speculative mainnet dates, no hype language)
5. Where output gets published and when
