# ⚡ NEXUS クイックスタートガイド

> **5分でゼロからオーケストレーションされたマルチエージェントパイプラインを稼働させます。**

---

## NEXUS とは何か？

**NEXUS**（Network of EXperts, Unified in Strategy）は The Agency の AI スペシャリスト群を調整されたパイプラインに変えます。エージェントを一つずつ起動してうまく連携することを期待するのではなく、誰がいつ何をし、どのように品質が各段階で検証されるかを明確に定義します。

## モードを選ぶ

| 私は… | 使う | エージェント数 | 期間 |
|-------|-----|----------------|------|
| 完全な製品をゼロから作る | **NEXUS-Full** | All | 12–24 週間 |
| 機能や MVP を作る | **NEXUS-Sprint** | 15–25 | 2–6 週間 |
| 特定のタスク（バグ修正、キャンペーン、監査）を行う | **NEXUS-Micro** | 5–10 | 1–5 日 |

---

## 🚀 NEXUS-Full: 完全プロジェクトを開始する

**以下のプロンプトをコピーしてフルパイプラインを起動してください：**

```
Activate Agents Orchestrator in NEXUS-Full mode.

Project: [YOUR PROJECT NAME]
Specification: [DESCRIBE YOUR PROJECT OR LINK TO SPEC]

Execute the complete NEXUS pipeline:
- Phase 0: Discovery (Trend Researcher, Feedback Synthesizer, UX Researcher, Analytics Reporter, Legal Compliance Checker, Tool Evaluator)
- Phase 1: Strategy (Studio Producer, Senior Project Manager, Sprint Prioritizer, UX Architect, Brand Guardian, Backend Architect, Finance Tracker)
- Phase 2: Foundation (DevOps Automator, Frontend Developer, Backend Architect, UX Architect, Infrastructure Maintainer)
- Phase 3: Build (Dev↔QA loops — all engineering + Evidence Collector)
- Phase 4: Harden (Reality Checker, Performance Benchmarker, API Tester, Legal Compliance Checker)
- Phase 5: Launch (Growth Hacker, Content Creator, all marketing agents, DevOps Automator)
- Phase 6: Operate (Analytics Reporter, Infrastructure Maintainer, Support Responder, ongoing)

Quality gates between every phase. Evidence required for all assessments.
Maximum 3 retries per task before escalation.
```

---

## 🏃 NEXUS-Sprint: 機能や MVP を構築する

**以下のプロンプトをコピーしてください：**

```
Activate Agents Orchestrator in NEXUS-Sprint mode.

Feature/MVP: [DESCRIBE WHAT YOU'RE BUILDING]
Timeline: [TARGET WEEKS]
Skip Phase 0 (market already validated).

Sprint team:
- PM: Senior Project Manager, Sprint Prioritizer
- Design: UX Architect, Brand Guardian
- Engineering: Frontend Developer, Backend Architect, DevOps Automator
- QA: Evidence Collector, Reality Checker, API Tester
- Support: Analytics Reporter

Begin at Phase 1 with architecture and sprint planning.
Run Dev↔QA loops for all implementation tasks.
Reality Checker approval required before launch.
```

---

## 🎯 NEXUS-Micro: 特定タスクを実行する

**シナリオを選び、プロンプトをコピーしてください：**

### バグ修正
```
Activate Backend Architect to investigate and fix [BUG DESCRIPTION].
After fix, activate API Tester to verify the fix.
Then activate Evidence Collector to confirm no visual regressions.
```

### マーケティングキャンペーン実行
```
Activate Social Media Strategist as campaign lead for [CAMPAIGN DESCRIPTION].
Team: Content Creator, Twitter Engager, Instagram Curator, Reddit Community Builder.
Brand Guardian reviews all content before publishing.
Analytics Reporter tracks performance daily.
Growth Hacker optimizes channels weekly.
```

### コンプライアンス監査実施
```
Activate Legal Compliance Checker for comprehensive compliance audit.
Scope: [GDPR / CCPA / HIPAA / ALL]
After audit, activate Executive Summary Generator to create stakeholder report.
```

### パフォーマンス問題の調査
```
Activate Performance Benchmarker to diagnose performance issues.
Scope: [API response times / Page load / Database queries / All]
After diagnosis, activate Infrastructure Maintainer for optimization.
DevOps Automator deploys any infrastructure changes.
```

### マーケットリサーチ
```
Activate Trend Researcher for market intelligence on [DOMAIN].
Deliverables: Competitive landscape, market sizing, trend forecast.
After research, activate Executive Summary Generator for executive brief.
```

### UX 改善
```
Activate UX Researcher to identify usability issues in [FEATURE/PRODUCT].
After research, activate UX Architect to design improvements.
Frontend Developer implements changes.
Evidence Collector verifies improvements.
```

---

## 📁 戦略ドキュメント

| ドキュメント | 目的 | 場所 |
|-------------|------|------|
| **Master Strategy** | 完全な NEXUS ドクトリン | `strategy/nexus-strategy.md` |
| **Phase 0 Playbook** | 発見とインテリジェンス | `strategy/playbooks/phase-0-discovery.md` |
| **Phase 1 Playbook** | 戦略とアーキテクチャ | `strategy/playbooks/phase-1-strategy.md` |
| **Phase 2 Playbook** | 基盤とスキャフォルディング | `strategy/playbooks/phase-2-foundation.md` |
| **Phase 3 Playbook** | 構築と反復 | `strategy/playbooks/phase-3-build.md` |
| **Phase 4 Playbook** | 品質とハードニング | `strategy/playbooks/phase-4-hardening.md` |
| **Phase 5 Playbook** | ローンチと成長 | `strategy/playbooks/phase-5-launch.md` |
| **Phase 6 Playbook** | 運用と進化 | `strategy/playbooks/phase-6-operate.md` |
| **Activation Prompts** | すぐに使えるエージェントプロンプト | `strategy/coordination/agent-activation-prompts.md` |
| **Handoff Templates** | 標準化された引き渡しフォーマット | `strategy/coordination/handoff-templates.md` |
| **Startup MVP Runbook** | 4–6 週の MVP 構築 | `strategy/runbooks/scenario-startup-mvp.md` |
| **Enterprise Feature Runbook** | エンタープライズ機能開発 | `strategy/runbooks/scenario-enterprise-feature.md` |
| **Marketing Campaign Runbook** | マルチチャネルキャンペーン | `strategy/runbooks/scenario-marketing-campaign.md` |
| **Incident Response Runbook** | 本番インシデント対応 | `strategy/runbooks/scenario-incident-response.md` |

---

## 🔑 30秒で分かるキーポイント

1. **品質ゲート** — 証拠に基づく承認がないと次フェーズへ進めない
2. **Dev↔QA ループ** — 各タスクは作成後に必ずテストされる。PASS で進行、FAIL はリトライ（最大3回）
3. **引き渡し** — エージェント間の構造化されたコンテキスト転送（コールドスタートを避ける）
4. **Reality Checker** — 最終的な品質判断者。デフォルトは「NEEDS WORK」
5. **Agents Orchestrator** — パイプライン全体を制御するコントローラ
6. **証拠を重視** — 主張ではなくスクリーンショット、テスト結果、データを要求する

---

## 🎭 エージェント一覧（概観）

```
ENGINEERING         │ DESIGN              │ MARKETING
Frontend Developer  │ UI Designer         │ Growth Hacker
Backend Architect   │ UX Researcher       │ Content Creator
Mobile App Builder  │ UX Architect        │ Twitter Engager
AI Engineer         │ Brand Guardian      │ TikTok Strategist
DevOps Automator    │ Visual Storyteller  │ Instagram Curator
Rapid Prototyper    │ Whimsy Injector     │ Reddit Community Builder
Senior Developer    │ Image Prompt Eng.   │ App Store Optimizer
                    │                     │ Social Media Strategist
────────────────────┼─────────────────────┼──────────────────────
PRODUCT             │ PROJECT MGMT        │ TESTING
Sprint Prioritizer  │ Studio Producer     │ Evidence Collector
Trend Researcher    │ Project Shepherd    │ Reality Checker
Feedback Synthesizer│ Studio Operations   │ Test Results Analyzer
                    │ Experiment Tracker  │ Performance Benchmarker
                    │ Senior Project Mgr  │ API Tester
                    │                     │ Tool Evaluator
                    │                     │ Workflow Optimizer
────────────────────┼─────────────────────┼──────────────────────
SUPPORT             │ SPATIAL             │ SPECIALIZED
Support Responder   │ XR Interface Arch.  │ Agents Orchestrator
Analytics Reporter  │ macOS Spatial/Metal │ Data Analytics Reporter
Finance Tracker     │ XR Immersive Dev    │ LSP/Index Engineer
Infra Maintainer    │ XR Cockpit Spec.    │ Sales Data Extraction
Legal Compliance    │ visionOS Spatial    │ Data Consolidation
Exec Summary Gen.   │ Terminal Integration│ Report Distribution
```

---

<div align="center">

**モードを選び、プレイブックに従い、パイプラインを信頼してください。**

`strategy/nexus-strategy.md` — 完全なドクトリン

</div>
