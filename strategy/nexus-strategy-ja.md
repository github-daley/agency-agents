# 🌐 NEXUS — Network of EXperts, Unified in Strategy

## The Agency のマルチエージェントオーケストレーションに関する完全運用プレイブック

> **NEXUS** は The Agency に属する独立した AI スペシャリスト群を同期化されたインテリジェンスネットワークに変えます。これは単なるプロンプト集ではなく、プロジェクトやプロダクト、組織に対して The Agency を掛け算的に強化するための **導入ドクトリン** です。

---

## 目次

1. [戦略的基盤](#1-strategic-foundation)
2. [NEXUS の運用モデル](#2-the-nexus-operating-model)
3. [Phase 0 — インテリジェンス & ディスカバリー](#3-phase-0--intelligence--discovery)
4. [Phase 1 — 戦略 & アーキテクチャ](#4-phase-1--strategy--architecture)
5. [Phase 2 — 基盤 & スキャフォルディング](#5-phase-2--foundation--scaffolding)
6. [Phase 3 — 構築 & 反復](#6-phase-3--build--iterate)
7. [Phase 4 — 品質 & ハードニング](#7-phase-4--quality--hardening)
8. [Phase 5 — ローンチ & 成長](#8-phase-5--launch--growth)
9. [Phase 6 — 運用 & 進化](#9-phase-6--operate--evolve)
10. [エージェント調整マトリクス](#10-agent-coordination-matrix)
11. [引き渡しプロトコル](#11-handoff-protocols)
12. [品質ゲート](#12-quality-gates)
13. [リスク管理](#13-risk-management)
14. [成功指標](#14-success-metrics)
15. [クイックスタート起動ガイド](#15-quick-start-activation-guide)

---

## 1. 戦略的基盤

### 1.1 NEXUS が解決する問題

個々のエージェントは強力ですが、調整がないと以下のような問題が発生します：
- 矛盾するアーキテクチャ上の決定
- 部門間での作業の重複
- 引き渡し境界での品質のギャップ
- 共有コンテキストや組織的記憶が存在しない

**NEXUS はこれらの失敗モードを排除します**。具体的には以下を定義します：
- **Who**（誰が）各フェーズで起動されるか
- **What**（何を）誰に対して生産するか
- **When**（いつ）引き渡すのか
- **How**（どのように）品質が検証されるか
- **Why**（なぜ）各エージェントがパイプラインに存在するのか（無駄な参加者は許容しない）

### 1.2 コア原則

| Principle | 説明 |
|-----------|------|
| **Pipeline Integrity** | 品質ゲートを通過しない限りフェーズは進まない |
| **Context Continuity** | すべての引き渡しは完全なコンテキストを運ぶ — エージェントはコールドスタートしない |
| **Parallel Execution** | 独立したワークストリームは同時に実行され、タイムラインを短縮する |
| **Evidence Over Claims** | すべての品質評価は証拠を必要とし、主張だけでは不十分 |
| **Fail Fast, Fix Fast** | タスクごとのリトライは最大 3 回、以後はエスカレーション |
| **Single Source of Truth** | 正式な仕様書、タスクリスト、アーキテクチャが唯一の情報源 |

### 1.3 部門別エージェント名簿

| Division | Agents | 主な NEXUS 上の役割 |
|----------|--------|---------------------|
| **Engineering** | Frontend Developer, Backend Architect, Mobile App Builder, AI Engineer, DevOps Automator, Rapid Prototyper, Senior Developer | 技術システムの構築・デプロイ・保守 |
| **Design** | UI Designer, UX Researcher, UX Architect, Brand Guardian, Visual Storyteller, Whimsy Injector, Image Prompt Engineer | ビジュアルアイデンティティ、UX、ブランド整合性の定義 |
| **Marketing** | Growth Hacker, Content Creator, Twitter Engager, TikTok Strategist, Instagram Curator, Reddit Community Builder, App Store Optimizer, Social Media Strategist | 獲得、エンゲージメント、マーケットプレゼンスの推進 |
| **Product** | Sprint Prioritizer, Trend Researcher, Feedback Synthesizer | 何をいつなぜ作るかを定義 |
| **Project Management** | Studio Producer, Project Shepherd, Studio Operations, Experiment Tracker, Senior Project Manager | タイムライン、リソース、横断調整の運営 |
| **Testing** | Evidence Collector, Reality Checker, Test Results Analyzer, Performance Benchmarker, API Tester, Tool Evaluator, Workflow Optimizer | 証拠に基づく品質検証 |
| **Support** | Support Responder, Analytics Reporter, Finance Tracker, Infrastructure Maintainer, Legal Compliance Checker, Executive Summary Generator | 運用保守、コンプライアンス、BI |
| **Spatial Computing** | XR Interface Architect, macOS Spatial/Metal Engineer, XR Immersive Developer, XR Cockpit Interaction Specialist, visionOS Spatial Engineer, Terminal Integration Specialist | イマーシブ／空間コンピューティング体験の構築 |
| **Specialized** | Agents Orchestrator, Data Analytics Reporter, LSP/Index Engineer, Sales Data Extraction Agent, Data Consolidation Agent, Report Distribution Agent | 横断的な調整、深い分析、コードインテリジェンス |

---

## 2. NEXUS の運用モデル

### 2.1 七段階のパイプライン

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        NEXUS PIPELINE                                   │
│                                                                         │
│  Phase 0        Phase 1         Phase 2          Phase 3                │
│  DISCOVER  ───▶ STRATEGIZE ───▶ SCAFFOLD   ───▶  BUILD                 │
│  Intelligence   Architecture    Foundation       Dev ↔ QA Loop          │
│                                                                         │
│  Phase 4        Phase 5         Phase 6                                 │
│  HARDEN   ───▶  LAUNCH    ───▶  OPERATE                                │
│  Quality Gate   Go-to-Market    Sustained Ops                           │
│                                                                         │
│  ◆ Quality Gate between every phase                                     │
│  ◆ Parallel tracks within phases                                        │
│  ◆ Feedback loops at every boundary                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.2 コマンド構造

```
                    ┌──────────────────────┐
                    │  Agents Orchestrator  │  ◄── Pipeline Controller
                    │  (Specialized)        │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
     ┌────────▼──────┐ ┌──────▼───────┐ ┌──────▼──────────┐
     │ Studio        │ │ Project      │ │ Senior Project   │
     │ Producer      │ │ Shepherd     │ │ Manager          │
     │ (Portfolio)   │ │ (Execution)  │ │ (Task Scoping)   │
     └───────────────┘ └──────────────┘ └─────────────────┘
              │                │                │
              ▼                ▼                ▼
     ┌─────────────────────────────────────────────────┐
     │           Division Leads (per phase)             │
     │  Engineering │ Design │ Marketing │ Product │ QA │
     └─────────────────────────────────────────────────┘
```

### 2.3 起動モード

NEXUS は三つのデプロイ設定をサポートします：

| Mode | Agents Active | Use Case | Timeline |
|------|---------------|----------|----------|
| **NEXUS-Full** | All | エンタープライズ製品ローンチ、ライフサイクル全体 | 12–24 週間 |
| **NEXUS-Sprint** | 15–25 | 機能開発、MVP 構築 | 2–6 週間 |
| **NEXUS-Micro** | 5–10 | バグ修正、コンテンツキャンペーン、単一の成果物 | 1–5 日 |

---

## 3. Phase 0 — インテリジェンス & ディスカバリー

> **目的**: リソースを投入する前に状況を理解する。問題が検証されるまでは構築を始めない。

### 3.1 稼働エージェント

| Agent | フェーズでの役割 | 主なアウトプット |
|-------|----------------|-------------------|
| **Trend Researcher** | マーケットインテリジェンスリード | TAM/SAM/SOM を含む市場分析レポート |
| **Feedback Synthesizer** | ユーザーニーズ分析 | ペインポイントを含む統合フィードバックレポート |
| **UX Researcher** | ユーザー行動分析 | ペルソナとジャーニーマップを含む調査結果 |
| **Analytics Reporter** | データレンドスケープ評価 | 利用可能なシグナルを含むデータ監査レポート |
| **Legal Compliance Checker** | 規制スキャン | コンプライアンス要件マトリックス |
| **Tool Evaluator** | 技術ランドスケープ | Tech Stack Assessment |

### 3.2 並列ワークストリーム

```
WORKSTREAM A: Market Intelligence          WORKSTREAM B: User Intelligence
├── Trend Researcher                       ├── Feedback Synthesizer
│   ├── Competitive landscape              │   ├── Multi-channel feedback collection
│   ├── Market sizing (TAM/SAM/SOM)        │   ├── Sentiment analysis
│   └── Trend lifecycle mapping            │   └── Pain point prioritization
│                                          │
├── Analytics Reporter                     ├── UX Researcher
│   ├── Existing data audit                │   ├── User interviews/surveys
│   ├── Signal identification              │   ├── Persona development
│   └── Baseline metrics                   │   └── Journey mapping
│                                          │
└── Legal Compliance Checker               └── Tool Evaluator
    ├── Regulatory requirements                ├── Technology assessment
    ├── Data handling constraints               ├── Build vs. buy analysis
    └── Jurisdiction mapping                   └── Integration feasibility
```

### 3.3 Phase 0 品質ゲート

**Gate Keeper**: Executive Summary Generator

| 判定基準 | 閾値 | 必要な証拠 |
|-----------|------|-----------|
| 市場機会が検証されている | TAM > 最小可用閾値 | Trend Researcher レポート（出典付き） |
| ユーザーニーズが確認されている | ≥3 の検証済ペインポイント | Feedback Synthesizer + UX Researcher のデータ |
| 規制上の道筋が明確 | ブロッキングな問題なし | Legal Compliance Checker マトリックス |
| データ基盤が評価済み | 主要指標が特定されている | Analytics Reporter の監査 |
| 技術的実現性が確認済み | スタックが検証済み | Tool Evaluator の評価 |

**出力**: Executive Summary（≤500 語、SCQA 形式）→ 判定: GO / NO-GO / PIVOT

---

## 4. Phase 1 — 戦略 & アーキテクチャ

> **目的**: 何を、どのように構造化し、成功をどう測るかを定義する — コードを書く前に。

### 4.1 稼働エージェント

| Agent | フェーズでの役割 | 主なアウトプット |
|-------|----------------|-------------------|
| **Studio Producer** | 戦略的ポートフォリオ整合 | Strategic Portfolio Plan |
| **Senior Project Manager** | 仕様→タスク変換 | Comprehensive Task List |
| **Sprint Prioritizer** | 機能の優先順位付け | RICE スコア付きの優先バックログ |
| **UX Architect** | 技術アーキテクチャ + UX 基盤 | Architecture Spec + CSS Design System |
| **Brand Guardian** | ブランドアイデンティティ | Brand Foundation Document |
| **Backend Architect** | システムアーキテクチャ | System Architecture Specification |
| **AI Engineer** | AI/ML のアーキテクチャ（該当時） | ML System Design |
| **Finance Tracker** | 予算とリソース計画 | Financial Plan with ROI projections |

### 4.2 実行シーケンス

```
STEP 1: Strategic Framing (Parallel)
├── Studio Producer → Strategic Portfolio Plan (vision, objectives, ROI targets)
├── Brand Guardian → Brand Foundation (purpose, values, visual identity system)
└── Finance Tracker → Budget Framework (resource allocation, cost projections)

STEP 2: Technical Architecture (Parallel, after Step 1)
├── UX Architect → CSS Design System + Layout Framework + UX Structure
├── Backend Architect → System Architecture (services, databases, APIs)
├── AI Engineer → ML Architecture (models, pipelines, inference strategy)
└── Senior Project Manager → Task List (spec → tasks, exact requirements)

STEP 3: Prioritization (Sequential, after Step 2)
└── Sprint Prioritizer → RICE-scored backlog with sprint assignments
    ├── Input: Task List + Architecture Spec + Budget Framework
    ├── Output: Prioritized sprint plan with dependency map
    └── Validation: Studio Producer confirms strategic alignment
```

### 4.3 Phase 1 品質ゲート

**Gate Keeper**: Studio Producer + Reality Checker（デュアルサインオフ）

| 判定基準 | 閾値 | 必要な証拠 |
|-----------|------|-----------|
| アーキテクチャが要件を網羅している | 100% の仕様カバレッジ | Senior PM のタスクリストとのクロス参照 |
| ブランドシステムが完成している | ロゴ、色、タイポ、ボイス定義 | Brand Guardian の成果物 |
| 技術的実現性が検証されている | すべてのコンポーネントに実装経路がある | Backend Architect + UX Architect の仕様 |
| 予算が承認されている | 組織の制約内 | Finance Tracker の計画 |
| スプリント計画が現実的である | Velocity ベースの見積り | Sprint Prioritizer のバックログ |

**出力**: 承認済みアーキテクチャパッケージ → Phase 2 を起動

---

## 5. Phase 2 — 基盤 & スキャフォルディング

> **目的**: 以降の作業が依存する技術的・運用的基盤を構築する。骨格を整えてから肉付けする。

### 5.1 稼働エージェント

| Agent | 役割 | 主なアウトプット |
|-------|------|------------------|
| **DevOps Automator** | CI/CD パイプライン + インフラ | Deployment Pipeline + IaC Templates |
| **Frontend Developer** | プロジェクトスキャフォールディング + コンポーネントライブラリ | App Skeleton + Design System Implementation |
| **Backend Architect** | DB + API の基盤 | Schema + API Scaffold + Auth System |
| **UX Architect** | CSS システム実装 | Design Tokens + Layout Framework |
| **Infrastructure Maintainer** | クラウドインフラセットアップ | Monitoring + Logging + Alerting |
| **Studio Operations** | プロセス設定 | Collaboration tools + workflows |

### 5.2 並列ワークストリーム

```
WORKSTREAM A: Infrastructure              WORKSTREAM B: Application Foundation
├── DevOps Automator                      ├── Frontend Developer
│   ├── CI/CD pipeline (GitHub Actions)   │   ├── Project scaffolding
│   ├── Container orchestration           │   ├── Component library setup
│   └── Environment provisioning          │   └── Design system integration
│                                         │
├── Infrastructure Maintainer             ├── Backend Architect
│   ├── Cloud resource provisioning       │   ├── Database schema deployment
│   ├── Monitoring (Prometheus/Grafana)   │   ├── API scaffold + auth
│   └── Security hardening                │   └── Service communication layer
│                                         │
└── Studio Operations                     └── UX Architect
    ├── Git workflow + branch strategy        ├── CSS design tokens
    ├── Communication channels                ├── Responsive layout system
    └── Documentation templates               └── Theme system (light/dark/system)
```

### 5.3 Phase 2 品質ゲート

**Gate Keeper**: DevOps Automator + Evidence Collector

| 判定基準 | 閾値 | 必要な証拠 |
|-----------|------|-----------|
| CI/CD パイプラインが稼働している | ビルド + テスト + デプロイが成功すること | パイプライン実行ログ |
| DB スキーマがデプロイ済み | すべてのテーブル/インデックスが作成されている | マイグレーション成功 + スキーマダンプ |
| API スキャフォールドが応答する | ヘルスチェックエンドポイントが生きている | curl の応答証拠 |
| フロントエンドがレンダリングされる | スケルトンアプリがブラウザで動作すること | Evidence Collector のスクリーンショット |
| モニタリングが稼働している | メトリクスが表示されること | Grafana 等のスクリーンショット |
| デザインシステムが実装されている | トークン + コンポーネントが利用可能であること | Component ライブラリのデモ |

**出力**: 動作するスケルトンアプリと DevOps パイプライン → Phase 3 を起動

---

## 6. Phase 3 — 構築 & 反復

> **目的**: Dev↔QA の継続ループで機能を実装する。各タスクは次に進む前に検証される。ここが本格的な作業現場です。

### 6.1 Dev↔QA ループ

これは NEXUS の中心です。Agents Orchestrator は **タスク単位の品質ループ**を管理します。

```
┌─────────────────────────────────────────────────────────┐
│                   DEV ↔ QA LOOP                          │
│                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────┐   │
│  │ Developer │───▶│ Evidence │───▶│ Decision Logic    │   │
│  │ Agent     │    │ Collector│    │                   │   │
│  │           │    │ (QA)     │    │ PASS → Next Task  │   │
│  │ Implements│    │          │    │ FAIL → Retry (≤3) │   │
│  │ Task N    │    │ Tests    │    │ BLOCKED → Escalate│   │
│  │           │◀───│ Task N   │◀───│                   │   │
│  └──────────┘    └──────────┘    └──────────────────┘   │
│       ▲                                    │             │
│       │            QA Feedback             │             │
│       └────────────────────────────────────┘             │
│                                                          │
│  Orchestrator tracks: attempt count, QA feedback,        │
│  task status, cumulative quality metrics                 │
└─────────────────────────────────────────────────────────┘
```

### 6.2 タスクタイプ別エージェント割り当て

| タスクタイプ | 主担当開発者 | QA エージェント | 専門サポート |
|-------------|--------------|----------------|-------------|
| Frontend UI | Frontend Developer | Evidence Collector | UI Designer, Whimsy Injector |
| Backend API | Backend Architect | API Tester | Performance Benchmarker |
| Database | Backend Architect | API Tester | Analytics Reporter |
| Mobile | Mobile App Builder | Evidence Collector | UX Researcher |
| AI/ML Feature | AI Engineer | Test Results Analyzer | Data Analytics Reporter |
| Infrastructure | DevOps Automator | Performance Benchmarker | Infrastructure Maintainer |
| Premium Polish | Senior Developer | Evidence Collector | Visual Storyteller |
| Rapid Prototype | Rapid Prototyper | Evidence Collector | Experiment Tracker |
| Spatial/XR | XR Immersive Developer | Evidence Collector | XR Interface Architect |
| visionOS | visionOS Spatial Engineer | Evidence Collector | macOS Spatial/Metal Engineer |
| Cockpit UI | XR Cockpit Interaction Specialist | Evidence Collector | XR Interface Architect |
| CLI/Terminal | Terminal Integration Specialist | API Tester | LSP/Index Engineer |
| Code Intelligence | LSP/Index Engineer | Test Results Analyzer | Senior Developer |

### 6.3 並列ビルドトラック

複雑なプロジェクトでは、複数のトラックが同時に進行します。

```
TRACK A: Core Product                    TRACK B: Growth & Marketing
├── Frontend Developer                   ├── Growth Hacker
│   └── UI implementation                │   └── Viral loops + referral system
├── Backend Architect                    ├── Content Creator
│   └── API + business logic             │   └── Launch content + editorial calendar
├── AI Engineer                          ├── Social Media Strategist
│   └── ML features + pipelines          │   └── Cross-platform campaign
│                                        ├── App Store Optimizer (if mobile)
│                                        │   └── ASO strategy + metadata
│                                        │
TRACK C: Quality & Operations            TRACK D: Brand & Experience
├── Evidence Collector                   ├── UI Designer
│   └── Continuous QA screenshots        │   └── Component refinement
├── API Tester                           ├── Brand Guardian
│   └── Endpoint validation              │   └── Brand consistency audit
├── Performance Benchmarker              ├── Visual Storyteller
│   └── Load testing + optimization      │   └── Visual narrative assets
├── Workflow Optimizer                   └── Whimsy Injector
│   └── Process improvement                  └── Delight moments + micro-interactions
└── Experiment Tracker
    └── A/B test management
```

### 6.4 Phase 3 品質ゲート

**Gate Keeper**: Agents Orchestrator

| 判定基準 | 閾値 | 必要な証拠 |
|-----------|------|-----------|
| すべてのタスクが QA を通過 | 100% のタスク完了 | Evidence Collector のタスクごとのスクリーンショット |
| API エンドポイントが検証済み | すべてのエンドポイントがテスト済み | API Tester のレポート |
| 性能ベースラインが満たされている | P95 < 200ms, LCP < 2.5s | Performance Benchmarker のレポート |
| ブランド整合性が確認されている | 95% 以上の遵守 | Brand Guardian の監査 |
| 致命的なバグがない | P0/P1 の未解決が 0 | Test Results Analyzer のサマリ |

**出力**: 機能完了のアプリケーション → Phase 4 を起動

---

## 7. Phase 4 — 品質 & ハードニング

> **目的**: 最終的な品質の試練。Reality Checker の既定値は「NEEDS WORK」であり、圧倒的な証拠がなければ READY は出ません。

### 7.1 稼働エージェント

| Agent | 役割 | 主なアウトプット |
|-------|------|------------------|
| **Reality Checker** | 最終統合テスト（デフォルト: NEEDS WORK） | Reality-Based Integration Report |
| **Evidence Collector** | 包括的な視覚証拠 | Screenshot Evidence Package |
| **Performance Benchmarker** | ロードテスト + 最適化 | Performance Certification |
| **API Tester** | フル API 回帰スイート | API Test Report |
| **Test Results Analyzer** | 品質指標の集約 | Quality Metrics Dashboard |
| **Legal Compliance Checker** | 最終コンプライアンス監査 | Compliance Certification |
| **Infrastructure Maintainer** | 本番準備チェック | Infrastructure Readiness Report |
| **Workflow Optimizer** | プロセス効率レビュー | Optimization Recommendations |

### 7.2 ハードニング シーケンス

```
STEP 1: Evidence Collection (Parallel)
├── Evidence Collector → Full screenshot suite (desktop, tablet, mobile)
├── API Tester → Complete endpoint regression
├── Performance Benchmarker → Load test at 10x expected traffic
└── Legal Compliance Checker → Final regulatory audit

STEP 2: Analysis (Parallel, after Step 1)
├── Test Results Analyzer → Aggregate all test data into quality dashboard
├── Workflow Optimizer → Identify remaining process inefficiencies
└── Infrastructure Maintainer → Production environment validation

STEP 3: Final Judgment (Sequential, after Step 2)
└── Reality Checker → Integration Report
    ├── Cross-validates ALL previous QA findings
    ├── Tests complete user journeys with screenshot evidence
    ├── Verifies specification compliance point-by-point
    ├── Default verdict: NEEDS WORK
    └── READY only with overwhelming evidence across all criteria
```

### 7.3 Phase 4 品質ゲート（最終ゲート）

**Gate Keeper**: Reality Checker（単独の権限）

| 判定基準 | 閾値 | 必要な証拠 |
|-----------|------|-----------|
| ユーザージャーニーが完了している | すべての重要経路が動作すること | エンドツーエンドのスクリーンショット |
| デバイス間の一貫性 | Desktop + Tablet + Mobile | レスポンシブのスクリーンショット |
| 性能が認証されている | P95 < 200ms, uptime > 99.9% | ロードテスト結果 |
| セキュリティが検証されている | 致命的脆弱性 0 | セキュリティスキャン報告 |
| コンプライアンスが認証されている | 規制要件が満たされている | Legal Compliance Checker の報告 |
| 仕様準拠 | 100% の仕様要件 | 項目ごとの検証 |

**判定オプション**:
- **READY** — ローンチへ進む（初回で READY が出るのは稀）
- **NEEDS WORK** — 具体的な修正項目を持って Phase 3 に戻す（通常）
- **NOT READY** — 大きなアーキテクチャ問題があるため Phase 1/2 に戻す

**期待値**: 初回実装は通常 2–3 回のリビジョンが必要。B/B+ 相当は正常。

---

## 8. Phase 5 — ローンチ & 成長

> **目的**: すべてのチャネルを同時に調整して Go-to-Market を実行し、最大のインパクトを狙う。

### 8.1 稼働エージェント

| Agent | 役割 | 主なアウトプット |
|-------|------|------------------|
| **Growth Hacker** | ローンチ戦略のリード | Growth Playbook with viral loops |
| **Content Creator** | ローンチ用コンテンツ | ブログ、動画、ソーシャルコンテンツ |
| **Social Media Strategist** | クロスプラットフォームキャンペーン | Campaign Calendar + Content |
| **Twitter Engager** | Twitter/X ローンチ | Thread strategy + engagement plan |
| **TikTok Strategist** | TikTok のバイラルコンテンツ | Short-form video strategy |
| **Instagram Curator** | 視覚的ローンチキャンペーン | Visual content + stories |
| **Reddit Community Builder** | コミュニティローンチ | Community engagement plan |
| **App Store Optimizer** | ストア最適化（モバイル時） | ASO Package |
| **Executive Summary Generator** | ステークホルダー連絡 | Launch Executive Summary |
| **Project Shepherd** | ローンチ調整 | Launch Checklist + Timeline |
| **DevOps Automator** | デプロイ実行 | Zero-downtime deployment |
| **Infrastructure Maintainer** | ローンチ監視 | Real-time dashboards |

### 8.2 ローンチシーケンス

```
T-7 DAYS: Pre-Launch
├── Content Creator → Launch content queued and scheduled
├── Social Media Strategist → Campaign assets finalized
├── Growth Hacker → Viral mechanics tested and armed
├── App Store Optimizer → Store listing optimized
├── DevOps Automator → Blue-green deployment prepared
└── Infrastructure Maintainer → Auto-scaling configured for 10x

T-0: Launch Day
├── DevOps Automator → Execute deployment
├── Infrastructure Maintainer → Monitor all systems
├── Twitter Engager → Launch thread + real-time engagement
├── Reddit Community Builder → Authentic community posts
├── Instagram Curator → Visual launch content
├── TikTok Strategist → Launch videos published
├── Support Responder → Customer support active
└── Analytics Reporter → Real-time metrics dashboard

T+1 TO T+7: Post-Launch
├── Growth Hacker → Analyze acquisition data, optimize funnels
├── Feedback Synthesizer → Collect and analyze early user feedback
├── Analytics Reporter → Daily metrics reports
├── Content Creator → Response content based on reception
├── Experiment Tracker → Launch A/B tests
└── Executive Summary Generator → Daily stakeholder briefings
```

### 8.3 Phase 5 品質ゲート

**Gate Keeper**: Studio Producer + Analytics Reporter

| 判定基準 | 閾値 | 必要な証拠 |
|-----------|------|-----------|
| デプロイが成功している | ゼロダウンタイム、すべてのヘルスチェック合格 | DevOps のデプロイログ |
| システムが安定している | 最初の 48 時間に P0/P1 発生なし | インフラ監視 |
| ユーザー獲得が始まっている | チャネルがトラフィックを生んでいる | Analytics ダッシュボード |
| フィードバックループが稼働している | ユーザーフィードバックが収集されている | Feedback Synthesizer の報告 |
| ステークホルダーへの報告が行われている | Executive summary が提出されている | Executive Summary Generator の出力 |

**出力**: 安定したローンチ済みプロダクトとアクティブな成長チャネル → Phase 6 を起動

---

## 9. Phase 6 — 運用 & 進化

> **目的**: 継続的な運用と継続的改善。プロダクトが稼働状態になったら成長させ続ける。

### 9.1 稼働エージェント（継続）

| Agent | 周期 | 責務 |
|-------|------|------|
| **Infrastructure Maintainer** | 継続 | システムの信頼性、稼働率、性能 |
| **Support Responder** | 継続 | カスタマーサポートと問題対応 |
| **Analytics Reporter** | 週次 | KPI トラッキング、ダッシュボード、インサイト |
| **Feedback Synthesizer** | 隔週 | ユーザーフィードバックの分析と統合 |
| **Finance Tracker** | 月次 | 財務パフォーマンス、予算追跡 |
| **Legal Compliance Checker** | 月次 | 規制監視と準拠 |
| **Trend Researcher** | 月次 | 市場インテリジェンスと競合分析 |
| **Executive Summary Generator** | 月次 | C-suite 向け報告 |
| **Sprint Prioritizer** | 各スプリント | バックログの整備とスプリント計画 |
| **Experiment Tracker** | 各実験 | A/B テスト管理と分析 |
| **Growth Hacker** | 継続 | 獲得最適化と成長実験 |
| **Workflow Optimizer** | 四半期毎 | プロセス改善と効率化 |

### 9.2 継続的改善サイクル

```
┌──────────────────────────────────────────────────────────┐
│              CONTINUOUS IMPROVEMENT LOOP                   │
│                                                           │
│  MEASURE          ANALYZE           PLAN          ACT     │
│  ┌─────────┐     ┌──────────┐     ┌─────────┐   ┌─────┐ │
│  │Analytics │────▶│Feedback  │────▶│Sprint   │──▶│Build│ │
│  │Reporter  │     │Synthesizer│    │Prioritizer│  │Loop │ │
│  └─────────┘     └──────────┘     └─────────┘   └─────┘ │
│       ▲                                            │      │
│       │              Experiment                    │      │
│       │              Tracker                       │      │
│       └────────────────────────────────────────────┘      │
│                                                           │
│  Monthly: Executive Summary Generator → C-suite report    │
│  Monthly: Finance Tracker → Financial performance         │
│  Monthly: Legal Compliance Checker → Regulatory update    │
│  Monthly: Trend Researcher → Market intelligence          │
│  Quarterly: Workflow Optimizer → Process improvements     │
└──────────────────────────────────────────────────────────┘
```

---

## 10. エージェント調整マトリクス

### 10.1 部門横断の依存マップ

このマトリクスは、どのエージェントが他のエージェントに消費される成果物を生成するかを示します。行のエージェントが生成 → 列のエージェントが消費。

```
PRODUCER →          │ ENG │ DES │ MKT │ PRD │ PM  │ TST │ SUP │ SPC │ SPZ
─────────────────────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼────
Engineering         │  ●  │     │     │     │     │  ●  │  ●  │  ●  │
Design              │  ●  │  ●  │  ●  │     │     │  ●  │     │  ●  │
Marketing           │     │     │  ●  │  ●  │     │     │  ●  │     │
Product             │  ●  │  ●  │  ●  │  ●  │  ●  │     │     │     │  ●
Project Management  │  ●  │  ●  │  ●  │  ●  │  ●  │  ●  │  ●  │  ●  │  ●
Testing             │  ●  │  ●  │     │  ●  │  ●  │  ●  │     │  ●  │
Support             │  ●  │     │  ●  │  ●  │  ●  │     │  ●  │     │  ●
Spatial Computing   │  ●  │  ●  │     │     │     │  ●  │     │  ●  │
Specialized         │  ●  │     │     │  ●  │  ●  │  ●  │  ●  │     │  ●

● = Active dependency (producer creates artifacts consumed by this division)
```

### 10.2 重要な引き渡しペア

頻度が高い、NEXUS における主要な引き渡し関係：

| From | To | Artifact | Frequency |
|------|----|----------|-----------|
| Senior Project Manager | All Developers | Task List | Per sprint |
| UX Architect | Frontend Developer | CSS Design System + Layout Spec | Per project |
| Backend Architect | Frontend Developer | API Specification | Per feature |
| Frontend Developer | Evidence Collector | Implemented Feature | Per task |
| Evidence Collector | Agents Orchestrator | QA Verdict (PASS/FAIL) | Per task |
| Agents Orchestrator | Developer (any) | QA Feedback + Retry Instructions | Per failure |
| Brand Guardian | All Design + Marketing | Brand Guidelines | Per project |
| Analytics Reporter | Sprint Prioritizer | Performance Data | Per sprint |
| Feedback Synthesizer | Sprint Prioritizer | User Insights | Per sprint |
| Trend Researcher | Studio Producer | Market Intelligence | Monthly |
| Reality Checker | Agents Orchestrator | Integration Verdict | Per phase |
| Executive Summary Generator | Studio Producer | Executive Brief | Per milestone |

---

## 11. 引き渡しプロトコル

### 11.1 標準引き渡しテンプレート

すべてのエージェント間引き渡しは次を含むこと：

```markdown
## NEXUS Handoff Document

### Metadata
- **From**: [Agent Name] ([Division])
- **To**: [Agent Name] ([Division])
- **Phase**: [Current NEXUS Phase]
- **Task Reference**: [Task ID from Sprint Prioritizer backlog]
- **Priority**: [Critical / High / Medium / Low]
- **Timestamp**: [ISO 8601]

### Context
- **Project**: [Project name and brief description]
- **Current State**: [What has been completed so far]
- **Relevant Files**: [List of files/artifacts to review]
- **Dependencies**: [What this work depends on]

### Deliverable Request
- **What is needed**: [Specific, measurable deliverable]
- **Acceptance criteria**: [How success will be measured]
- **Constraints**: [Technical, timeline, or resource constraints]
- **Reference materials**: [Links to specs, designs, previous work]

### Quality Expectations
- **Must pass**: [Specific quality criteria]
- **Evidence required**: [What proof of completion looks like]
- **Handoff to next**: [Who receives the output and what they need]
```

### 11.2 QA フィードバックループプロトコル

タスクが QA を通らなかった場合、フィードバックは実行可能であること：

```markdown
## QA Failure Feedback

### Task: [Task ID and description]
### Attempt: [1/2/3] of 3 maximum
### Verdict: FAIL

### Specific Issues Found
1. **[Issue Category]**: [Exact description with screenshot reference]
   - Expected: [What should happen]
   - Actual: [What actually happens]
   - Evidence: [Screenshot filename or test output]

2. **[Issue Category]**: [Exact description]
   - Expected: [...]
   - Actual: [...]
   - Evidence: [...]

### Fix Instructions
- [Specific, actionable fix instruction 1]
- [Specific, actionable fix instruction 2]

### Files to Modify
- [file path 1]: [what needs to change]
- [file path 2]: [what needs to change]

### Retry Expectations
- Fix the above issues and re-submit for QA
- Do NOT introduce new features — fix only
- Attempt [N+1] of 3 maximum
```

### 11.3 エスカレーションプロトコル

タスクが 3 回のリトライを超えた場合：

```markdown
## Escalation Report

### Task: [Task ID]
### Attempts Exhausted: 3/3
### Escalation Level: [To Agents Orchestrator / To Studio Producer]

### Failure History
- Attempt 1: [Summary of issues and fixes attempted]
- Attempt 2: [Summary of issues and fixes attempted]
- Attempt 3: [Summary of issues and fixes attempted]

### Root Cause Analysis
- [Why the task keeps failing]
- [What systemic issue is preventing resolution]

### Recommended Resolution
- [ ] Reassign to different developer agent
- [ ] Decompose task into smaller sub-tasks
- [ ] Revise architecture/approach
- [ ] Accept current state with known limitations
- [ ] Defer to future sprint

### Impact Assessment
- **Blocking**: [What other tasks are blocked by this]
- **Timeline Impact**: [How this affects the overall schedule]
- **Quality Impact**: [What quality compromises exist]
```

---

## 12. 品質ゲート

### 12.1 ゲート概要

| フェーズ | ゲート名 | ゲートキーパー | 合格基準 |
|---------|---------|----------------|---------|
| 0 → 1 | Discovery Gate | Executive Summary Generator | 市場検証、ユーザーニーズ確認、規制経路が明確 |
| 1 → 2 | Architecture Gate | Studio Producer + Reality Checker | アーキテクチャ完了、ブランド定義、予算承認、現実的なスプリント計画 |
| 2 → 3 | Foundation Gate | DevOps Automator + Evidence Collector | CI/CD 稼働、スケルトンアプリ稼働、監視稼働 |
| 3 → 4 | Feature Gate | Agents Orchestrator | すべてのタスクが QA を通過、致命的バグなし、性能基準満たす |
| 4 → 5 | Production Gate | Reality Checker（単独） | ユーザージャーニー完了、デバイス間一貫性、セキュリティ検証、仕様準拠 |
| 5 → 6 | Launch Gate | Studio Producer + Analytics Reporter | デプロイ成功、システム安定、成長チャネルが稼働 |

### 12.2 ゲート失敗時の処理

```
IF gate FAILS:
  ├── Gate Keeper produces specific failure report
  ├── Agents Orchestrator routes failures to responsible agents
  ├── Failed items enter Dev↔QA loop (Phase 3 mechanics)
  ├── Maximum 3 gate re-attempts before escalation to Studio Producer
  └── Studio Producer decides: fix, descope, or accept with risk
```

---

## 13. リスク管理

### 13.1 リスクカテゴリとオーナー

| リスクカテゴリ | プライマリオーナー | 対策エージェント | エスカレーションパス |
|---------------|-------------------|------------------|----------------------|
| Technical Debt | Backend Architect | Workflow Optimizer | Senior Developer |
| Security Vulnerability | Legal Compliance Checker | Infrastructure Maintainer | DevOps Automator |
| Performance Degradation | Performance Benchmarker | Infrastructure Maintainer | Backend Architect |
| Brand Inconsistency | Brand Guardian | UI Designer | Studio Producer |
| Scope Creep | Senior Project Manager | Sprint Prioritizer | Project Shepherd |
| Budget Overrun | Finance Tracker | Studio Operations | Studio Producer |
| Regulatory Non-Compliance | Legal Compliance Checker | Support Responder | Studio Producer |
| Market Shift | Trend Researcher | Growth Hacker | Studio Producer |
| Team Bottleneck | Project Shepherd | Studio Operations | Studio Producer |
| Quality Regression | Reality Checker | Evidence Collector | Agents Orchestrator |

### 13.2 リスク対応マトリクス

| Severity | Response Time | Decision Authority | Action |
|----------|---------------|--------------------|--------|
| **Critical** (P0) | Immediate | Studio Producer | All-hands, stop other work |
| **High** (P1) | < 4 hours | Project Shepherd | Dedicated agent assignment |
| **Medium** (P2) | < 24 hours | Agents Orchestrator | Next sprint priority |
| **Low** (P3) | < 1 week | Sprint Prioritizer | Backlog item |

---

## 14. 成功指標

### 14.1 パイプライン指標

| 指標 | 目標 | 測定エージェント |
|------|------|------------------|
| Phase completion rate | 95% on first attempt | Agents Orchestrator |
| Task first-pass QA rate | 70%+ | Evidence Collector |
| Average retries per task | < 1.5 | Agents Orchestrator |
| Pipeline cycle time | Within sprint estimate ±15% | Project Shepherd |
| Quality gate pass rate | 80%+ on first attempt | Reality Checker |

### 14.2 プロダクト指標

| 指標 | 目標 | 測定エージェント |
|------|------|------------------|
| API response time (P95) | < 200ms | Performance Benchmarker |
| Page load time (LCP) | < 2.5s | Performance Benchmarker |
| System uptime | > 99.9% | Infrastructure Maintainer |
| Lighthouse score | > 90 (Performance + Accessibility) | Frontend Developer |
| Security vulnerabilities | Zero critical | Legal Compliance Checker |
| Spec compliance | 100% | Reality Checker |

### 14.3 ビジネス指標

| 指標 | 目標 | 測定エージェント |
|------|------|------------------|
| User acquisition (MoM) | 20%+ growth | Growth Hacker |
| Activation rate | 60%+ in first week | Analytics Reporter |
| Retention (Day 7 / Day 30) | 40% / 20% | Analytics Reporter |
| LTV:CAC ratio | > 3:1 | Finance Tracker |
| NPS score | > 50 | Feedback Synthesizer |
| Portfolio ROI | > 25% | Studio Producer |

### 14.4 運用指標

| 指標 | 目標 | 測定エージェント |
|------|------|------------------|
| Deployment frequency | Multiple per day | DevOps Automator |
| Mean time to recovery | < 30 minutes | Infrastructure Maintainer |
| Compliance adherence | 98%+ | Legal Compliance Checker |
| Stakeholder satisfaction | 4.5/5 | Executive Summary Generator |
| Process efficiency gain | 20%+ per quarter | Workflow Optimizer |

---

## 15. クイックスタート起動ガイド

### 15.1 NEXUS-Full 起動（エンタープライズ）

```bash
# Step 1: Initialize NEXUS pipeline
"Activate Agents Orchestrator in NEXUS-Full mode for [PROJECT NAME].
 Project specification: [path to spec file].
 Execute complete 7-phase pipeline with all quality gates."

# The Orchestrator will:
# 1. Read the project specification
# 2. Activate Phase 0 agents for discovery
# 3. Progress through all phases with quality gates
# 4. Manage Dev↔QA loops automatically
# 5. Report status at each phase boundary
```

### 15.2 NEXUS-Sprint 起動（機能/MVP）

```bash
# Step 1: Initialize sprint pipeline
"Activate Agents Orchestrator in NEXUS-Sprint mode for [FEATURE/MVP NAME].
 Requirements: [brief description or path to spec].
 Skip Phase 0 (market already validated).
 Begin at Phase 1 with architecture and sprint planning."

# Recommended agent subset (15-25):
# PM: Senior Project Manager, Sprint Prioritizer, Project Shepherd
# Design: UX Architect, UI Designer, Brand Guardian
# Engineering: Frontend Developer, Backend Architect, DevOps Automator
# + AI Engineer or Mobile App Builder (if applicable)
# Testing: Evidence Collector, Reality Checker, API Tester, Performance Benchmarker
# Support: Analytics Reporter, Infrastructure Maintainer
# Specialized: Agents Orchestrator
```

### 15.3 NEXUS-Micro 起動（ターゲットタスク）

```bash
# Step 1: Direct agent activation
"Activate [SPECIFIC AGENT] for [TASK DESCRIPTION].
 Context: [relevant background].
 Deliverable: [specific output expected].
 Quality check: Evidence Collector to verify upon completion."

# Common NEXUS-Micro configurations:
#
# Bug Fix:
#   Backend Architect → API Tester → Evidence Collector
#
# Content Campaign:
#   Content Creator → Social Media Strategist → Twitter Engager
#   + Instagram Curator + Reddit Community Builder
#
# Performance Issue:
#   Performance Benchmarker → Infrastructure Maintainer → DevOps Automator
#
# Compliance Audit:
#   Legal Compliance Checker → Executive Summary Generator
#
# Market Research:
#   Trend Researcher → Analytics Reporter → Executive Summary Generator
#
# UX Improvement:
#   UX Researcher → UX Architect → Frontend Developer → Evidence Collector
```

### 15.4 エージェント起動プロンプトテンプレート

#### Orchestrator（パイプライン開始用）

``` (truncated)
``` 

---

## 付録 A: 部門クイックリファレンス

(各 Division のクイックリファレンスは原文に従います — エージェント名は英語のまま記載されています)

<div align="center">

**🌐 NEXUS: 9 部門。7 フェーズ。1 つの統一戦略。🌐**

*発見から継続的運用まで — すべてのエージェントは自分の役割、タイミング、引き渡し方法を知っています。*

</div>
