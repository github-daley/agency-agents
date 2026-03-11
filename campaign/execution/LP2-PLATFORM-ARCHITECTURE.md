# Learning Path 2: PLATFORM ARCHITECTURE
## @telcoinTAO Education Series — 10 Posts
### Created: March 11, 2026

---

## Post 1 of 10 — The Telcoin Platform Overview

**Post text:**

The Telcoin Platform is not a single product. It is an integrated system of three distinct layers – each with its own function, participants, and economic role.

Telcoin Network: the Layer 1 blockchain validated by GSMA mobile network operators.
TELx: the decentralized exchange and liquidity layer.
TAN: the application layer where end users interact with mobile financial services.

Together, these layers form a vertically integrated platform designed to deliver blockchain-powered financial services through existing mobile infrastructure – from validator to end user.

Each layer has its own proof mechanism and miner group, creating a governance model where no single layer controls the system.

What questions do you have about how the three layers of the Telcoin Platform work together?

**Rationale:** Establishes the macro architecture immediately. Readers need to understand that Telcoin Association is not building a single app or a single chain – it is building a coordinated platform. This frames every subsequent post in the series.

---

## Post 2 of 10 — Telcoin Network Explained

**Post text:**

Telcoin Network is an EVM-compatible Layer 1 public blockchain purpose-built for mobile financial services.

Key technical facts:

- Consensus: Proof of Stake using the Narwhal and Bullshark protocol – a DAG-based consensus mechanism designed for high throughput and low latency
- Validators: Exclusively GSMA full-member mobile network operators
- Native gas token: TEL
- Chain ID: 2017

Unlike general-purpose blockchains, Telcoin Network restricts validator participation to licensed, accountable telecommunications companies. Each validator MNO also serves as a distribution channel – connecting the network directly to mobile subscribers.

The Adiri public testnet is currently active, with production hardening and security assessments underway. Mainnet launch is milestone-based, not calendar-based.

Full roadmap details: roadmap.telcoin.network

What aspects of the GSMA-exclusive validator model would you like to understand in more detail?

**Rationale:** Introduces the network layer with verifiable technical specifics. Emphasizes the GSMA validator differentiator without hype. Links to the roadmap for readers who want to track progress themselves.

---

## Post 3 of 10 — TELx Explained

**Post text:**

TELx is the decentralized finance layer of the Telcoin Platform – an automated market maker (AMM) exchange where liquidity providers earn fees, TEL rewards, and governance rights.

Current deployment:

- Networks: Polygon PoS and Base
- Protocols: Balancer V2 (6 active markets) and Uniswap V4
- Staking rewards: 3.2 billion TEL distributed weekly to liquidity miners, every Wednesday at 00:00 UTC
- Analytics: telx.network/pools

TELx serves two critical functions within the platform. First, it provides the on-chain liquidity that makes cross-border value transfer possible. Second, it creates an economic participation layer – anyone can provide liquidity and earn rewards, without intermediaries.

Liquidity miners on TELx are one of the four miner groups in Telcoin Association governance, with equal authority alongside validators, developers, and stakers.

What do you find most relevant about how TELx connects DeFi liquidity to real-world remittance corridors?

**Rationale:** Positions TELx as infrastructure rather than a yield farm. Grounds the description in verifiable on-chain data (pool counts, reward schedules, network deployments). Connects liquidity provision to the broader remittance mission.

---

## Post 4 of 10 — TAN Explained

**Post text:**

TAN – the Telcoin Application Network – is the application layer of the Telcoin Platform. It is where end users interact with mobile financial services built on top of Telcoin Network and TELx.

The primary TAN application today is the Telcoin Wallet, available on iOS and Android. Through the wallet, users can:

- Hold Digital Cash stablecoins (eUSD, eGBP, eJPY, eSGD, eZAR)
- Swap tokens
- Send remittances to 23+ mobile money platforms across 16 countries

TAN is also where builders are developing new applications – from the Telcoin Name Service (.tel human-readable addresses) to charitable giving tools and micro-applications designed for mass adoption.

TAN participants – called stakers – form one of the four miner groups in the governance model, earning rewards through referrals and adoption activity.

What aspects of the TAN application layer are you most interested in exploring further?

**Rationale:** Introduces TAN as the user-facing layer. Grounds it in the existing Telcoin Wallet product and its live corridor data. Mentions the builder ecosystem to signal that TAN is an open platform, not a closed product.

---

## Post 5 of 10 — How the Layers Connect

**Post text:**

The three layers of the Telcoin Platform – Telcoin Network, TELx, and TAN – are designed to function as an integrated system. Here is how value flows through them.

A user in the United States opens the Telcoin Wallet (TAN layer) and initiates a remittance to a family member in the Philippines.

The transaction routes through TELx (liquidity layer), where AMM pools convert the user's Digital Cash stablecoin into the destination currency at market rates with minimal slippage.

The settlement is recorded and validated on Telcoin Network (infrastructure layer) by GSMA mobile network operator nodes.

The recipient receives funds on their local mobile money platform – in this example, Coins in the Philippines.

Each layer contributes something distinct: TAN provides the user interface and distribution. TELx provides the liquidity and price discovery. Telcoin Network provides the settlement and security.

No single layer functions in isolation. Together, they replace the correspondent banking chain that currently makes remittances slow and expensive.

How does this integrated layer model compare to other blockchain approaches you have seen in the payments space?

**Rationale:** The most important post in the series – it shows how the three layers work together through a concrete, real-world transaction example using a live corridor (US to Philippines via Coins). Avoids abstract descriptions by walking through a user journey.

---

## Post 6 of 10 — TEL Token Utility

**Post text:**

TEL is the native token of the Telcoin Platform. It serves four distinct functions across the three platform layers.

1. Gas: TEL is the native gas token on Telcoin Network (Chain ID 2017). Every transaction on the network requires TEL to execute.

2. Staking: Validators must stake TEL to participate in block production. TAN stakers deposit TEL through the Telcoin Wallet to earn rewards and governance rights.

3. Liquidity: TEL is a base pair in TELx AMM pools. Liquidity providers deposit TEL alongside other assets to facilitate decentralized exchange.

4. Governance: All four miner groups – validators, liquidity miners, developers, and stakers – participate in platform governance. TEL staking and liquidity provision are prerequisites for governance participation in their respective groups.

TEL has a hard cap of 100 billion tokens, with approximately 96 billion currently in circulation.

Contract addresses are published on telcoin.org.

Which of these four TEL utility functions do you consider most significant for long-term platform sustainability?

**Rationale:** Clearly delineates the four utility pillars without speculation about value. Uses the verified hard cap and circulating supply. Directs readers to official sources for contract addresses rather than listing them in a tweet.

---

## Post 7 of 10 — TEL Issuance and Harvesting

**Post text:**

TEL issuance follows a structured distribution model governed by Telcoin Association.

The maximum supply is fixed at 100 billion TEL. New issuance from the treasury is allocated through governance proposals – such as the Year 3 allocation of 900 million TEL approved for platform development, miner incentives, and mainnet launch support.

TEL is distributed to miners across all four groups:

- Validators earn network transaction fees
- Liquidity miners earn exchange fees and TEL rewards from TELx pools
- Stakers earn referral fees and adoption-based TEL issuance
- Developers earn through approved governance allocations

Weekly distribution of 3.2 billion TEL occurs every Wednesday at 00:00 UTC, allocated based on each miner's contribution to the platform.

This model – sometimes called "harvesting" – ties token distribution directly to productive activity rather than passive holding. Each TEL distributed corresponds to a measurable contribution: a block validated, liquidity provided, a user referred, or code deployed.

How does tying token distribution to measurable platform contributions shape your understanding of TEL's economic model?

**Rationale:** Explains issuance with verified numbers (100B cap, 900M Y3 allocation, 3.2B weekly distribution). Frames the "harvesting" concept without jargon. Connects distribution to all four miner groups with specific examples of what each contributes.

---

## Post 8 of 10 — Proof of Stake on Telcoin Network

**Post text:**

Telcoin Network uses Proof of Stake consensus with a critical distinction: only GSMA full-member mobile network operators can serve as validators.

The consensus protocol – Narwhal and Bullshark – is a DAG-based mechanism designed for high throughput and Byzantine fault tolerance. Validators propose and certify transaction batches, reaching consensus without the energy costs of Proof of Work.

To become a validator, an MNO must:

- Hold full GSMA Operator Member status
- Meet criteria set by Telcoin Association
- Stake TEL tokens

Each MNO validator runs infrastructure in its own data centers – the same secured facilities that house existing telecom packet-switching equipment. These are not cloud instances. They are fiber-optic-interconnected bare-metal servers capable of streaming tens of gigabits per second.

This design creates a direct economic incentive: MNO validators earn network fees, which motivates them to promote Telcoin services to their subscriber bases – turning validators into distribution partners.

What do you see as the most important implication of restricting validator status to licensed mobile network operators?

**Rationale:** Deep dive into the Proof of Stake mechanism with verified technical details from the Platform and Treasury Council recap. Highlights the MNO data center infrastructure point, which is a compelling and underreported differentiator. Explains the economic alignment without overstating it.

---

## Post 9 of 10 — Proof of Liquidity on TELx

**Post text:**

TELx operates on a Proof of Liquidity model. Participants earn rewards by providing real economic value – liquidity – to the platform's decentralized exchange infrastructure.

How it works:

1. A liquidity provider deposits token pairs into TELx AMM pools (currently on Balancer V2 and Uniswap V4)
2. Their LP position generates exchange fees from every swap that routes through their pool
3. In addition to fees, liquidity miners receive weekly TEL rewards – 3.2 billion TEL distributed every Wednesday at 00:00 UTC
4. Active liquidity miners gain governance rights within the TELx Council, one of the platform's specialized governance bodies

The TELx Council recently approved a trial integration with Merkl – a protocol for dynamic, flexible incentive distribution. This trial, running on the Base V4 TEL/ETH pool beginning approximately April 2026, will test whether targeted incentive structures can improve capital efficiency across pools.

The strategic direction is clear: shift from fixed equal allocation across pools toward formula-based distribution that can scale as new markets – particularly eXYZ stablecoin corridors – come online.

What aspects of the Proof of Liquidity model and its governance structure would you like to explore further?

**Rationale:** Explains Proof of Liquidity with a step-by-step walkthrough. Incorporates the Merkl trial as a timely, verified development that shows the system is actively evolving. Connects liquidity provision to the broader stablecoin corridor strategy without speculating on outcomes.

---

## Post 10 of 10 — Proof of Alignment on TAN

**Post text:**

The TAN layer introduces a third proof mechanism: Proof of Alignment. This model rewards participants – called stakers – for activities that directly grow the platform's user base and real-world utility.

TAN stakers deposit TEL through the Telcoin Wallet and earn rewards through two channels:

- Referral fees: Earned in real time when referred users complete transactions
- TEL issuance: Distributed weekly based on adoption-related activity

This creates a fundamentally different incentive structure from speculative token models. TAN stakers are not rewarded for holding tokens passively. They are rewarded for bringing new users onto the platform and facilitating real financial transactions – particularly cross-border remittances to the 16 countries and 23+ mobile money platforms currently supported.

Stakers form one of four equal miner groups in Telcoin Association governance, alongside validators, liquidity miners, and developers. Their governance weight reflects the principle that user acquisition and retention are as valuable to the platform as infrastructure, liquidity, and code.

Proof of Alignment is the mechanism that connects the Telcoin Platform's technical architecture to its stated mission: financial inclusion for mobile users globally.

How do you evaluate the effectiveness of tying governance rights and economic rewards to measurable adoption activity?

**Rationale:** Closes the learning path by connecting the most user-facing proof mechanism back to the mission. Emphasizes that Proof of Alignment rewards real activity (referrals, transactions) rather than passive holding. Ties the four miner groups together as a complete governance picture, giving readers a sense of the full system after all 10 posts.

---

## Series Summary

| # | Topic | Key Concept |
|---|---|---|
| 1 | Platform Overview | Three layers, integrated system |
| 2 | Telcoin Network | L1, PoS, GSMA validators, Narwhal/Bullshark |
| 3 | TELx | AMM liquidity, Balancer V2 + Uniswap V4, weekly rewards |
| 4 | TAN | Application layer, Telcoin Wallet, builder ecosystem |
| 5 | Layer Integration | Value flow, user journey, correspondent banking replacement |
| 6 | TEL Utility | Gas, staking, liquidity, governance |
| 7 | TEL Issuance | Treasury, harvesting, activity-based distribution |
| 8 | Proof of Stake | MNO validators, bare-metal data centers, economic alignment |
| 9 | Proof of Liquidity | LP rewards, Merkl trial, formula-based distribution |
| 10 | Proof of Alignment | Staker mechanics, referrals, adoption incentives |

All facts sourced from: campaign/research/TELCOIN-RESEARCH.md (last updated March 11, 2026)
