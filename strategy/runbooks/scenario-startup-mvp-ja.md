# 🚀 ランブック: スタートアップ MVP 構築

> **モード**: NEXUS-Sprint | **期間**: 4–6 週間 | **エージェント数**: 18–22

---

## シナリオ

スタートアップの MVP を構築し、短期間でプロダクトマーケットフィットを検証する。速度と品質の両方が重要です。アイデアから実際にユーザーが利用するプロダクトへ、4–6 週間で到達することを目指します。

## エージェントロスター

### 常時稼働するコアチーム

| Agent | Role |
|-------|------|
| Agents Orchestrator | パイプラインコントローラ |
| Senior Project Manager | 仕様→タスクの変換 |
| Sprint Prioritizer | バックログ管理 |
| UX Architect | 技術的基盤の設計 |
| Frontend Developer | UI 実装 |
| Backend Architect | API と DB |
| DevOps Automator | CI/CD とデプロイ |
| Evidence Collector | 各タスクの QA |
| Reality Checker | 最終品質ゲート |

### Week 3 以降に起動される Growth チーム

| Agent | Role |
|-------|------|
| Growth Hacker | 獲得戦略 |
| Content Creator | ローンチコンテンツ |
| Social Media Strategist | ソーシャルキャンペーン |

### 必要に応じたサポートチーム

| Agent | Role |
|-------|------|
| Brand Guardian | ブランドアイデンティティ |
| Analytics Reporter | 指標とダッシュボード |
| Rapid Prototyper | 迅速な検証実験 |
| AI Engineer | AI 機能がある場合 |
| Performance Benchmarker | ロードテスト前の性能検証 |
| Infrastructure Maintainer | 本番環境構築 |

## 週次の実行計画

### Week 1: 発見とアーキテクチャ（Phase 0 + Phase 1 を圧縮）

```
Day 1-2: Compressed Discovery
├── Trend Researcher → Quick competitive scan (1 day, not full report)
├── UX Architect → Wireframe key user flows
└── Senior Project Manager → Convert spec to task list

Day 3-4: Architecture
├── UX Architect → CSS design system + component architecture
├── Backend Architect → System architecture + database schema
├── Brand Guardian → Quick brand foundation (colors, typography, voice)
└── Sprint Prioritizer → RICE-scored backlog + sprint plan

Day 5: Foundation Setup
├── DevOps Automator → CI/CD pipeline + environments
├── Frontend Developer → Project scaffolding
├── Backend Architect → Database + API scaffold
└── Quality Gate: Architecture Package approved
```

### Week 2–3: コアビルド（Phase 2 + Phase 3）

```
Sprint 1 (Week 2):
├── Agents Orchestrator manages Dev↔QA loop
├── Frontend Developer → Core UI (auth, main views, navigation)
├── Backend Architect → Core API (auth, CRUD, business logic)
├── Evidence Collector → QA every completed task
├── AI Engineer → ML features if applicable
└── Sprint Review at end of week

Sprint 2 (Week 3):
├── Continue Dev↔QA loop for remaining features
├── Growth Hacker → Design viral mechanics + referral system
├── Content Creator → Begin launch content creation
├── Analytics Reporter → Set up tracking and dashboards
└── Sprint Review at end of week
```

### Week 4: 仕上げとハードニング（Phase 4）

```
Day 1-2: Quality Sprint
├── Evidence Collector → Full screenshot suite
├── Performance Benchmarker → Load testing
├── Frontend Developer → Fix QA issues
├── Backend Architect → Fix API issues
└── Brand Guardian → Brand consistency audit

Day 3-4: Reality Check
├── Reality Checker → Final integration testing
├── Infrastructure Maintainer → Production readiness
└── DevOps Automator → Production deployment prep

Day 5: Gate Decision
├── Reality Checker verdict
├── IF NEEDS WORK: Quick fix cycle (2-3 days)
├── IF READY: Proceed to launch
└── Executive Summary Generator → Stakeholder briefing
```

### Week 5–6: ローンチと成長（Phase 5）

```
Week 5: Launch
├── DevOps Automator → Production deployment
├── Growth Hacker → Activate acquisition channels
├── Content Creator → Publish launch content
├── Social Media Strategist → Cross-platform campaign
├── Analytics Reporter → Real-time monitoring
└── Support Responder → User support active

Week 6: Optimize
├── Growth Hacker → Analyze and optimize channels
├── Feedback Synthesizer → Collect early user feedback
├── Experiment Tracker → Launch A/B tests
├── Analytics Reporter → Week 1 analysis
└── Sprint Prioritizer → Plan iteration sprint
```

## 重要な意思決定

| Decision Point | When | Who Decides |
|---------------|------|-------------|
| コンセプトの Go/No-Go | Day 2 の終わり | Studio Producer |
| アーキテクチャ承認 | Day 4 の終わり | Senior Project Manager |
| MVP の機能範囲 | スプリント計画時 | Sprint Prioritizer |
| 本番準備 | Week 4 Day 5 | Reality Checker |
| ローンチ時期 | Reality Checker が READY の後 | Studio Producer |

## 成功基準

| 指標 | 目標 |
|------|------|
| ライブまでの時間 | ≤ 6 週間 |
| コア機能完了率 | MVP スコープの 100% |
| 初回ユーザー登録 | ローンチ後 48 時間以内 |
| 初週のシステム稼働率 | > 99% |
| 取得したユーザーフィードバック数 | ローンチ後 2 週間で ≥ 50 回 |

## よくある落とし穴と対策

| Pitfall | Mitigation |
|---------|------------|
| ビルド中のスコープ拡大 | Sprint Prioritizer が MoSCoW を強制 — “Won't” は実際に実施しない |
| スケール向けの過剰設計 | Rapid Prototyper のマインドセット — まず検証し、後で拡張 |
| 速度優先で QA を省略 | Evidence Collector は EVERY task に対して実行 — 例外なし |
| 監視なしでローンチ | Infrastructure Maintainer が Week 1 に監視を設定 |
| フィードバック機構がない | Analytics とフィードバック収集を Sprint 1 に組み込む |
