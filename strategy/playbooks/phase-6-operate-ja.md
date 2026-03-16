# 🔄 フェーズ6 プレイブック — 運用と進化

> **期間**: 継続 | **エージェント数**: 12+（ローテーション） | **ガバナンス**: Studio Producer

---

## 目的

持続的な運用と継続的改善。プロダクトは公開済み — ここから成長させる。終了日はなく、市場にある限りこのフェーズが回る。

## 事前条件

- [ ] Phase 5 品質ゲート合格（安定したローンチ）
- [ ] Phase 5 引き渡しパッケージ受領
- [ ] 運用カデンツが確立されている
- [ ] 基準となるメトリクスが記録されている

## 運用カデンツ

### 常時（常に稼働）

| エージェント | 責務 | SLA |
|--------------|------|-----|
| **Infrastructure Maintainer** | システムの稼働性、性能、セキュリティ | 99.9%稼働、MTTR < 30分 |
| **Support Responder** | カスタマーサポート、問題解決 | 初動応答 < 4時間 |
| **DevOps Automator** | デプロイパイプライン、ホットフィックス | 1日に複数デプロイ可能 |

### 日次

| エージェント | 活動 | 出力 |
|--------------|------|------|
| **Analytics Reporter** | KPIダッシュボード更新 | 日次メトリクススナップショット |
| **Support Responder** | チケットの振り分けと解決 | サポートチケット要約 |
| **Infrastructure Maintainer** | システムヘルスチェック | ヘルスステータスレポート |

### 週次

| エージェント | 活動 | 出力 |
|--------------|------|------|
| **Analytics Reporter** | 週次パフォーマンス分析 | 週次アナリティクスレポート |
| **Feedback Synthesizer** | ユーザーフィードバック統合 | 週次フィードバックサマリ |
| **Sprint Prioritizer** | バックログ整備 + スプリント計画 | スプリント計画 |
| **Growth Hacker** | 成長チャネル最適化 | グロースメトリクスレポート |
| **Project Shepherd** | 横断調整 | 週次ステータスアップデート |

### 隔週

| エージェント | 活動 | 出力 |
|--------------|------|------|
| **Feedback Synthesizer** | 深堀分析 | 隔週インサイトレポート |
| **Experiment Tracker** | A/Bテスト分析 | 実験結果サマリ |
| **Content Creator** | コンテンツ実行 | 公開コンテンツレポート |

### 月次

| エージェント | 活動 | 出力 |
|--------------|------|------|
| **Executive Summary Generator** | Cレベル向け報告 | 月次エグゼクティブサマリ |
| **Finance Tracker** | 財務レビュー | 月次財務報告 |
| **Legal Compliance Checker** | 規制モニタリング | コンプライアンス状況報告 |
| **Trend Researcher** | 市場インテリジェンス更新 | 月次マーケットブリーフ |
| **Brand Guardian** | ブランド一貫性監査 | ブランドヘルスレポート |

### 四半期

| エージェント | 活動 | 出力 |
|--------------|------|------|
| **Studio Producer** | 戦略ポートフォリオレビュー | 四半期戦略レビュー |
| **Workflow Optimizer** | プロセス効率監査 | 最適化レポート |
| **Performance Benchmarker** | 性能回帰テスト | 四半期性能レポート |
| **Tool Evaluator** | テックスタックレビュー | 技術的負債評価 |

## 継続的改善ループ

```
MEASURE (Analytics Reporter)
    │
    ▼
ANALYZE (Feedback Synthesizer + Data Analytics Reporter)
    │
    ▼
PLAN (Sprint Prioritizer + Studio Producer)
    │
    ▼
BUILD (Phase 3 Dev↔QA Loop — mini-cycles)
    │
    ▼
VALIDATE (Evidence Collector + Reality Checker)
    │
    ▼
DEPLOY (DevOps Automator)
    │
    ▼
MEASURE (back to start)
```

### フェーズ6での機能開発

新機能は圧縮されたNEXUSサイクルに従う：

```
1. Sprint Prioritizer selects feature from backlog
2. Appropriate Developer Agent implements
3. Evidence Collector validates (Dev↔QA loop)
4. DevOps Automator deploys (feature flag or direct)
5. Experiment Tracker monitors (A/B test if applicable)
6. Analytics Reporter measures impact
7. Feedback Synthesizer collects user response
```

## インシデント対応プロトコル

### 重大度レベル

| レベル | 定義 | 応答時間 | 決定権 |
|--------|------|---------|-------|
| **P0 — 重大** | サービス停止、データ喪失、セキュリティ侵害 | 即時 | Studio Producer |
| **P1 — 高** | 主要機能の障害、大幅な劣化 | < 1時間 | Project Shepherd |
| **P2 — 中** | 小さな機能不具合、回避策あり | < 4時間 | Agents Orchestrator |
| **P3 — 低** | 表面的な問題、次スプリントへ | 次のスプリント | Sprint Prioritizer |

### インシデント対応シーケンス

```
DETECTION (Infrastructure Maintainer or Support Responder)
    │
    ▼
TRIAGE (Agents Orchestrator)
    ├── Classify severity (P0-P3)
    ├── Assign response team
    └── Notify stakeholders
    │
    ▼
RESPONSE
    ├── P0: Infrastructure Maintainer + DevOps Automator + Backend Architect
    ├── P1: Relevant Developer Agent + DevOps Automator
    ├── P2: Relevant Developer Agent
    └── P3: Added to sprint backlog
    │
    ▼
RESOLUTION
    ├── Fix implemented and deployed
    ├── Evidence Collector verifies fix
    └── Infrastructure Maintainer confirms stability
    │
    ▼
POST-MORTEM
    ├── Workflow Optimizer leads retrospective
    ├── Root cause analysis documented
    ├── Prevention measures identified
    └── Process improvements implemented
```

## グロースオペレーション

### 月次グロースレビュー（Growth Hacker主導）

```
1. Channel Performance Analysis
   - Acquisition by channel (organic, paid, referral, social)
   - CAC by channel
   - Conversion rates by funnel stage
   - LTV:CAC ratio trends

2. Experiment Results
   - Completed A/B tests and outcomes
   - Statistical significance validation
   - Winner implementation status
   - New experiment pipeline

3. Retention Analysis
   - Cohort retention curves
   - Churn risk identification
   - Re-engagement campaign results
   - Feature adoption metrics

4. Growth Roadmap Update
   - Next month's growth experiments
   - Channel budget reallocation
   - New channel exploration
   - Viral coefficient optimization
```

## 財務運用

### 月次財務レビュー（Finance Tracker）

```
1. Revenue Analysis
   - MRR/ARR tracking
   - Revenue by segment/plan
   - Expansion revenue
   - Churn revenue impact

2. Cost Analysis
   - Infrastructure costs
   - Marketing spend by channel
   - Team/resource costs
   - Tool and service costs

3. Unit Economics
   - CAC trends
   - LTV trends
   - LTV:CAC ratio
   - Payback period

4. Forecasting
   - Revenue forecast (3-month rolling)
   - Cost forecast
   - Cash flow projection
   - Budget variance analysis
```

## コンプライアンス運用

### 月次コンプライアンスチェック（Legal Compliance Checker）

```
1. Regulatory Monitoring
   - New regulations affecting the product
   - Existing regulation changes
   - Enforcement actions in the industry
   - Compliance deadline tracking

2. Privacy Compliance
   - Data subject request handling
   - Consent management effectiveness
   - Data retention policy adherence
   - Cross-border transfer compliance

3. Security Compliance
   - Vulnerability scan results
   - Patch management status
   - Access control review
   - Incident log review

4. Audit Readiness
   - Documentation currency
   - Evidence collection status
   - Training completion rates
   - Policy acknowledgment tracking
```

## 戦略的進化

### 四半期戦略レビュー（Studio Producer）

```
1. Market Position Assessment
   - Competitive landscape changes (Trend Researcher input)
   - Market share evolution
   - Brand perception (Brand Guardian input)
   - Customer satisfaction trends (Feedback Synthesizer input)

2. Product Strategy
   - Feature roadmap review
   - Technology debt assessment (Tool Evaluator input)
   - Platform expansion opportunities
   - Partnership evaluation

3. Growth Strategy
   - Channel effectiveness review
   - New market opportunities
   - Pricing strategy assessment
   - Expansion planning

4. Organizational Health
   - Process efficiency (Workflow Optimizer input)
   - Team performance metrics
   - Resource allocation optimization
   - Capability development needs

Output: Quarterly Strategic Review → Updated roadmap and priorities
```

## フェーズ6成功指標

| カテゴリ | 指標 | 目標 | オーナー |
|----------|------|------|---------|
| **信頼性** | システム稼働率 | > 99.9% | Infrastructure Maintainer |
| **信頼性** | MTTR | < 30分 | Infrastructure Maintainer |
| **成長** | 月次ユーザー増 | > 20% | Growth Hacker |
| **成長** | 活性化率 | > 60% | Analytics Reporter |
| **定着** | Day 7 retention | > 40% | Analytics Reporter |
| **定着** | Day 30 retention | > 20% | Analytics Reporter |
| **財務** | LTV:CAC | > 3:1 | Finance Tracker |
| **財務** | ポートフォリオROI | > 25% | Studio Producer |
| **品質** | NPSスコア | > 50 | Feedback Synthesizer |
| **品質** | サポート解決時間 | < 4時間 | Support Responder |
| **コンプライアンス** | 規制遵守率 | > 98% | Legal Compliance Checker |
| **効率** | デプロイ頻度 | 複数/日 | DevOps Automator |
| **効率** | プロセス改善 | 20%/四半期 | Workflow Optimizer |

---

*フェーズ6は終了日がなく、製品が市場にある限り継続する。継続的改善サイクルが製品を前進させる。重要な新機能や方針転換時にはNEXUSパイプライン（Sprint/Micro）を再起動できる。*
