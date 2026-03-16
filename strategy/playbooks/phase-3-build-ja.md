# 🔨 フェーズ3 プレイブック — 構築と反復

> **期間**: 2–12週間（規模により変動） | **エージェント数**: 15–30+ | **ゲートキーパー**: Agents Orchestrator

---

## 目的

継続的な Dev↔QA ループを通してすべての機能を実装します。各タスクは次に進む前に検証されます。ここが作業の大半が行われ、NEXUS のオーケストレーションが最も価値を発揮する領域です。

## 事前条件

- [ ] Phase 2 品質ゲート合格（基盤が検証済み）
- [ ] Sprint Prioritizer バックログが RICE スコア付きで利用可能
- [ ] CI/CD パイプラインが稼働している
- [ ] デザインシステムとコンポーネントライブラリが準備済み
- [ ] 認証を備えた API スキャフォールドが用意されている

## Dev↔QA ループ — コアメカニズム

Agents Orchestrator は各タスクを以下のサイクルで管理します。

```
FOR EACH task IN sprint_backlog (ordered by RICE score):

  1. ASSIGN task to appropriate Developer Agent (see assignment matrix)
  2. Developer IMPLEMENTS task
  3. Evidence Collector TESTS task
     - Visual screenshots (desktop, tablet, mobile)
     - Functional verification against acceptance criteria
     - Brand consistency check
  4. IF verdict == PASS:
       Mark task complete
       Move to next task
     ELIF verdict == FAIL AND attempts < 3:
       Send QA feedback to Developer
       Developer FIXES specific issues
       Return to step 3
     ELIF attempts >= 3:
       ESCALATE to Agents Orchestrator
       Orchestrator decides: reassign, decompose, defer, or accept
   5. UPDATE pipeline status report
```

## エージェント割り当てマトリクス

### プライマリ開発者割り当て

| タスクカテゴリ | プライマリエージェント | バックアップ | QA エージェント |
|--------------|----------------------|-------------|-----------------|
| **React/Vue/Angular UI** | Frontend Developer | Rapid Prototyper | Evidence Collector |
| **REST/GraphQL API** | Backend Architect | Senior Developer | API Tester |
| **Database operations** | Backend Architect | — | API Tester |
| **Mobile (iOS/Android)** | Mobile App Builder | — | Evidence Collector |
| **ML model/pipeline** | AI Engineer | — | Test Results Analyzer |
| **CI/CD/Infrastructure** | DevOps Automator | Infrastructure Maintainer | Performance Benchmarker |
| **Premium/complex feature** | Senior Developer | Backend Architect | Evidence Collector |
| **Quick prototype/POC** | Rapid Prototyper | Frontend Developer | Evidence Collector |
| **WebXR/immersive** | XR Immersive Developer | — | Evidence Collector |
| **visionOS** | visionOS Spatial Engineer | macOS Spatial/Metal Engineer | Evidence Collector |
| **Cockpit controls** | XR Cockpit Interaction Specialist | XR Interface Architect | Evidence Collector |
| **CLI/terminal tools** | Terminal Integration Specialist | — | API Tester |
| **Code intelligence** | LSP/Index Engineer | — | Test Results Analyzer |
| **Performance optimization** | Performance Benchmarker | Infrastructure Maintainer | Performance Benchmarker |

### 専門サポート（必要時に起動）

| Specialist | When to Activate | Trigger |
|-----------|-----------------|---------|
| UI Designer | コンポーネントの視覚的改善が必要な場合 | Developer がデザインガイダンスを要求したとき |
| Whimsy Injector | 機能に楽しさ/個性を加えたい場合 | UX レビューで機会が確認されたとき |
| Visual Storyteller | ビジュアルナラティブが必要な場合 | コンテンツに視覚資産が必要なとき |
| Brand Guardian | ブランド整合性に懸念がある場合 | QA がブランド逸脱を検出したとき |
| XR Interface Architect | 空間的なインタラクション設計が必要な場合 | XR 機能が UX 指針を必要とするとき |
| Data Analytics Reporter | 深いデータ分析が必要な場合 | 機能が分析統合を必要とするとき |

## 並列ビルドトラック

NEXUS-Full のデプロイでは、四つのトラックが同時に走ります。

### Track A: Core Product Development

```
Managed by: Agents Orchestrator (Dev↔QA loop)
Agents: Frontend Developer, Backend Architect, AI Engineer,
        Mobile App Builder, Senior Developer
QA: Evidence Collector, API Tester, Test Results Analyzer

Sprint cadence: 2-week sprints
Daily: Task implementation + QA validation
End of sprint: Sprint review + retrospective
```

### Track B: Growth & Marketing Preparation

```
Managed by: Project Shepherd
Agents: Growth Hacker, Content Creator, Social Media Strategist,
        App Store Optimizer

Sprint cadence: Aligned with Track A milestones
Activities:
- Growth Hacker → Design viral loops and referral mechanics
- Content Creator → Build launch content pipeline
- Social Media Strategist → Plan cross-platform campaign
- App Store Optimizer → Prepare store listing (if mobile)
```

### Track C: Quality & Operations

```
Managed by: Agents Orchestrator
Agents: Evidence Collector, API Tester, Performance Benchmarker,
        Workflow Optimizer, Experiment Tracker

Continuous activities:
- Evidence Collector → Screenshot QA for every task
- API Tester → Endpoint validation for every API task
- Performance Benchmarker → Periodic load testing
- Workflow Optimizer → Process improvement identification
- Experiment Tracker → A/B test setup for validated features
```

### Track D: Brand & Experience Polish

```
Managed by: Brand Guardian
Agents: UI Designer, Brand Guardian, Visual Storyteller,
        Whimsy Injector

Triggered activities:
- UI Designer → Component refinement when QA identifies visual issues
- Brand Guardian → Periodic brand consistency audit
- Visual Storyteller → Visual narrative assets as features complete
- Whimsy Injector → Micro-interactions and delight moments
```

## スプリント実行テンプレート

### スプリント計画（Day 1）

```
Sprint Prioritizer activates:
1. Review backlog with updated RICE scores
2. Select tasks for sprint based on team velocity
3. Assign tasks to developer agents
4. Identify dependencies and ordering
5. Set sprint goal and success criteria

Output: Sprint Plan with task assignments
```

### 日次実行（Day 2 〜 Day N-1）

```
Agents Orchestrator manages:
1. Current task status check
2. Dev↔QA loop execution
3. Blocker identification and resolution
4. Progress tracking and reporting

Status report format:
- Tasks completed today: [list]
- Tasks in QA: [list]
- Tasks in development: [list]
- Blocked tasks: [list with reason]
- QA pass rate: [X/Y]
```

### スプリントレビュー（Day N）

```
Project Shepherd facilitates:
1. Demo completed features
2. Review QA evidence for each task
3. Collect stakeholder feedback
4. Update backlog based on learnings

Participants: All active agents + stakeholders
Output: Sprint Review Summary
```

### スプリント回顧

```
Workflow Optimizer facilitates:
1. What went well?
2. What could improve?
3. What will we change next sprint?
4. Process efficiency metrics

Output: Retrospective Action Items
```

## オーケストレーター判定ロジック

### タスク失敗時の処理

```
WHEN task fails QA:
  IF attempt == 1:
    → Send specific QA feedback to developer
    → Developer fixes ONLY the identified issues
    → Re-submit for QA
    
  IF attempt == 2:
    → Send accumulated QA feedback
    → Consider: Is the developer agent the right fit?
    → Developer fixes with additional context
    → Re-submit for QA
    
  IF attempt == 3:
    → ESCALATE
    → Options:
      a) Reassign to different developer agent
      b) Decompose task into smaller sub-tasks
      c) Revise approach/architecture
      d) Accept with known limitations (document)
      e) Defer to future sprint
    → Document decision and rationale
```

### 並列タスク管理

```
WHEN multiple tasks have no dependencies:
  → Assign to different developer agents simultaneously
  → Each runs independent Dev↔QA loop
  → Orchestrator tracks all loops concurrently
  → Merge completed tasks in dependency order

WHEN task has dependencies:
  → Wait for dependency to pass QA
  → Then assign dependent task
  → Include dependency context in handoff
```

## 品質ゲートチェックリスト

| # | 判定項目 | 証拠ソース | ステータス |
|---|---------|------------|-----------|
| 1 | すべてのスプリントタスクが QA を通過している | Evidence Collector のタスク毎スクリーンショット | ☐ |
| 2 | すべての API エンドポイントが検証済み | API Tester の回帰レポート | ☐ |
| 3 | 性能ベースラインが満たされている（P95 < 200ms） | Performance Benchmarker のレポート | ☐ |
| 4 | ブランド整合性が確認されている（95% 以上） | Brand Guardian の監査 | ☐ |
| 5 | 致命的なバグがない（P0/P1） | Test Results Analyzer のサマリ | ☐ |
| 6 | すべての受け入れ基準が満たされている | タスク別検証 | ☐ |
| 7 | すべての PR のコードレビューが完了している | Git 履歴の証拠 | ☐ |

## ゲート判定

**ゲートキーパー**: Agents Orchestrator

- **PASS**: 機能完了のアプリケーション → Phase 4 を起動
- **CONTINUE**: さらにスプリントが必要 → Phase 3 を継続
- **ESCALATE**: システム的な問題 → Studio Producer の介入

## Phase 4 への引き渡し

``markdown
## Phase 3 → Phase 4 Handoff Package

### For Reality Checker:
- Complete application (all features implemented)
- All QA evidence from Dev↔QA loops
- API Tester regression results
- Performance Benchmarker baseline data
- Brand Guardian consistency audit
- Known issues list (if any accepted limitations)

### For Legal Compliance Checker:
- Data handling implementation details
- Privacy policy implementation
- Consent management implementation
- Security measures implemented

### For Performance Benchmarker:
- Application URLs for load testing
- Expected traffic patterns
- Performance budgets from architecture

### For Infrastructure Maintainer:
- Production environment requirements
- Scaling configuration needs
- Monitoring alert thresholds
```

---

*フェーズ3は、すべてのスプリントタスクが QA を通過し、すべての API エンドポイントが検証され、性能ベースラインが満たされ、致命的なバグが残っていないときに完了します。*
