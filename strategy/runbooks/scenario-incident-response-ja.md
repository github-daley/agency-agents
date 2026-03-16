# 🚨 ランブック: インシデント対応

> **モード**: NEXUS-Micro | **期間**: 数分〜数時間 | **エージェント数**: 3–8

---

## シナリオ

本番環境で何かが壊れ、ユーザーに影響が出ている。迅速な対応が重要だが、正しく対処することも重要です。本ランブックは検知からポストモーテムまでをカバーします。

## 深刻度分類

| レベル | 定義 | 例 | 応答時間 |
|--------|------|----|---------|
| **P0 — Critical** | サービス完全停止、データ損失、セキュリティ侵害 | データベース破損、DDoS、認証システム障害 | 即時（全員対応） |
| **P1 — High** | 主要機能の停止、大幅な性能劣化 | 決済処理停止、50% 超のエラー率、遅延が 10 倍 | < 1 時間 |
| **P2 — Medium** | 影響が限定された機能障害、回避策あり | 検索機能不具合、非クリティカルな API エラー | < 4 時間 |
| **P3 — Low** | 表示上の問題や小さな不具合 | スタイリングバグ、タイプミス、小さな UI グリッチ | 次スプリント |

## 応答チーム（深刻度別）

### P0 — Critical レスポンステーム

| Agent | Role | Action |
|-------|------|--------|
| **Infrastructure Maintainer** | Incident commander | 範囲評価、対応の調整 |
| **DevOps Automator** | Deployment/rollback | 必要ならロールバックを実行 |
| **Backend Architect** | Root cause investigation | システムの診断 |
| **Frontend Developer** | UI 側の調査 | クライアント側の診断 |
| **Support Responder** | ユーザーコミュニケーション | ステータスページ更新、ユーザー通知 |
| **Executive Summary Generator** | ステークホルダー向け連絡 | リアルタイムの経営向け更新 |

### P1 — High レスポンステーム

| Agent | Role |
|-------|------|
| **Infrastructure Maintainer** | Incident commander |
| **DevOps Automator** | Deployment support |
| **Relevant Developer Agent** | Fix implementation |
| **Support Responder** | User communication |

### P2 — Medium レスポンステーム

| Agent | Role |
|-------|------|
| **Relevant Developer Agent** | Fix implementation |
| **Evidence Collector** | Fix の検証 |

### P3 — Low レスポンステーム

| Agent | Role |
|-------|------|
| **Sprint Prioritizer** | バックログに追加 |

## インシデント対応シーケンス

### ステップ 1: 検知とトリアージ（0–5 分）

```
TRIGGER: Alert from monitoring / User report / Agent detection

Infrastructure Maintainer:
1. Acknowledge alert
2. Assess scope and impact
   - How many users affected?
   - Which services are impacted?
   - Is data at risk?
3. Classify severity (P0/P1/P2/P3)
4. Activate appropriate response team
5. Create incident channel/thread

Output: Incident classification + response team activated
```

### ステップ 2: 調査（5–30 分）

```
PARALLEL INVESTIGATION:

Infrastructure Maintainer:
├── Check system metrics (CPU, memory, network, disk)
├── Review error logs
├── Check recent deployments
└── Verify external dependencies

Backend Architect (if P0/P1):
├── Check database health
├── Review API error rates
├── Check service communication
└── Identify failing component

DevOps Automator:
├── Review recent deployment history
├── Check CI/CD pipeline status
├── Prepare rollback if needed
└── Verify infrastructure state

Output: Root cause identified (or narrowed to component)
```

### ステップ 3: 軽減（15–60 分）

```
DECISION TREE:

IF caused by recent deployment:
  → DevOps Automator: Execute rollback
  → Infrastructure Maintainer: Verify recovery
  → Evidence Collector: Confirm fix

IF caused by infrastructure issue:
  → Infrastructure Maintainer: Scale/restart/failover
  → DevOps Automator: Support infrastructure changes
  → Verify recovery

IF caused by code bug:
  → Relevant Developer Agent: Implement hotfix
  → Evidence Collector: Verify fix
  → DevOps Automator: Deploy hotfix
  → Infrastructure Maintainer: Monitor recovery

IF caused by external dependency:
  → Infrastructure Maintainer: Activate fallback/cache
  → Support Responder: Communicate to users
  → Monitor for external recovery

THROUGHOUT:
  → Support Responder: Update status page every 15 minutes
  → Executive Summary Generator: Brief stakeholders (P0 only)
```

### ステップ 4: 解決の検証（修正後）

```
Evidence Collector:
1. Verify the fix resolves the issue
2. Screenshot evidence of working state
3. Confirm no new issues introduced

Infrastructure Maintainer:
1. Verify all metrics returning to normal
2. Confirm no cascading failures
3. Monitor for 30 minutes post-fix

API Tester (if API-related):
1. Run regression on affected endpoints
2. Verify response times normalized
3. Confirm error rates at baseline

Output: Incident resolved confirmation
```

### ステップ 5: ポストモーテム（48 時間以内）

```
Workflow Optimizer leads post-mortem:

1. Timeline reconstruction
   - When was the issue introduced?
   - When was it detected?
   - When was it resolved?
   - Total user impact duration

2. Root cause analysis
   - What failed?
   - Why did it fail?
   - Why wasn't it caught earlier?
   - 5 Whys analysis

3. Impact assessment
   - Users affected
   - Revenue impact
   - Reputation impact
   - Data impact

4. Prevention measures
   - What monitoring would have caught this sooner?
   - What testing would have prevented this?
   - What process changes are needed?
   - What infrastructure changes are needed?

5. Action items
   - [Action] → [Owner] → [Deadline]
   - [Action] → [Owner] → [Deadline]
   - [Action] → [Owner] → [Deadline]

Output: Post-Mortem Report → Sprint Prioritizer adds prevention tasks to backlog
```

## コミュニケーションテンプレート

### ステータスページ更新（Support Responder）

```
[TIMESTAMP] — [SERVICE NAME] Incident

Status: [Investigating / Identified / Monitoring / Resolved]
Impact: [Description of user impact]
Current action: [What we're doing about it]
Next update: [When to expect the next update]
```

### 経営向けアップデート（Executive Summary Generator — P0 のみ）

```
INCIDENT BRIEF — [TIMESTAMP]

SITUATION: [Service] is [down/degraded] affecting [N users/% of traffic]
CAUSE: [Known/Under investigation] — [Brief description if known]
ACTION: [What's being done] — ETA [time estimate]
IMPACT: [Business impact — revenue, users, reputation]
NEXT UPDATE: [Timestamp]
```

## エスカレーションマトリクス

| 条件 | エスカレート先 | アクション |
|------|---------------|-----------|
| P0 が 30 分で解決しない場合 | Studio Producer | 追加リソース、ベンダーエスカレーション |
| P1 が 2 時間で解決しない場合 | Project Shepherd | リソースの再配分 |
| データ侵害が疑われる場合 | Legal Compliance Checker | 規制通知の検討 |
| ユーザーデータが影響を受けた場合 | Legal Compliance Checker + Executive Summary Generator | GDPR/CCPA 通知 |
| 収益への影響が $X を超える場合 | Finance Tracker + Studio Producer | ビジネス影響の評価 |
