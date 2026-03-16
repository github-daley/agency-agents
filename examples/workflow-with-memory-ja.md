# マルチエージェントワークフロー：永続メモリを使ったスタートアップMVP

> [workflow-startup-mvp.md](workflow-startup-mvp.md) にある同じスタートアップMVPワークフローですが、エージェント間の状態を MCP メモリサーバーで管理します。もうコピペによる引き継ぎは不要です。

## 手動引き継ぎの問題

通常のワークフローでは、エージェント間の遷移は次のようになります。

```
Activate Backend Architect.

Here's our sprint plan: [paste Sprint Prioritizer output]
Here's our research brief: [paste UX Researcher output]

Design the API and database schema for RetroBoard.
...
```

あなたがその接着剤の役割を担います。エージェント間で出力をコピペし、何が完了したかを追跡し、途中でコンテキストが失われないことを祈ります。小さなプロジェクトでは機能しますが、次のときに破綻します：

- セッションがタイムアウトして出力を失う
- 複数のエージェントが同じコンテキストを必要とする
- QA が失敗して以前の状態に巻き戻す必要がある
- プロジェクトが数日〜数週間にまたがる

## 解決策

MCP メモリサーバーを導入すると、エージェントは成果物をメモリに保存し、必要なときに自動で取り出せます。引き継ぎは次のようになります：

```
Activate Backend Architect.

Project: RetroBoard. Recall previous context for this project
and design the API and database schema.
```

エージェントはメモリを検索して RetroBoard に関するコンテキスト（以前のスプリント計画や調査ブリーフ）を見つけ、そこから作業を再開します。

## セットアップ

`remember`、`recall`、`rollback` 操作をサポートする任意の MCP 互換メモリサーバーをインストールしてください。セットアップ方法は [integrations/mcp-memory/README.md](../integrations/mcp-memory/README.md) を参照してください。

## シナリオ

標準ワークフローと同じ：SaaS のチーム・レトロスペクティブツール（RetroBoard）、MVP に 4 週間、開発者は 1 人。

## エージェントチーム

| エージェント | このワークフローでの役割 |
|--------------|-------------------------|
| Sprint Prioritizer | プロジェクトを週ごとのスプリントに分解する |
| UX Researcher | クイックなユーザーインタビューでアイデアを検証する |
| Backend Architect | API とデータモデルを設計する |
| Frontend Developer | React アプリを構築する |
| Rapid Prototyper | 可能な限り速く初版を動かす |
| Growth Hacker | 構築中にローンチ戦略を計画する |
| Reality Checker | 各マイルストーンで品質ゲートを担当する |

各エージェントのプロンプトにはメモリ統合のセクションが含まれます（追加方法は [integrations/mcp-memory/README.md](../integrations/mcp-memory/README.md) を参照）。

## ワークフロー

### Week 1: Discovery + Architecture

**Step 1 — Sprint Prioritizer を起動**

```
Activate Sprint Prioritizer.

Project: RetroBoard — a real-time team retrospective tool for remote teams.
Timeline: 4 weeks to MVP launch.
Core features: user auth, create retro boards, add cards, vote, action items.
Constraints: solo developer, React + Node.js stack, deploy to Vercel + Railway.

Break this into 4 weekly sprints with clear deliverables and acceptance criteria.
Remember your sprint plan tagged for this project when done.
```

Sprint Prioritizer はスプリント計画を生成し、`sprint-prioritizer`, `retroboard`, `sprint-plan` のタグでメモリに保存します。

**Step 2 — UX Researcher を並列で起動**

```
Activate UX Researcher.

I'm building a team retrospective tool for remote teams (5-20 people).
Competitors: EasyRetro, Retrium, Parabol.

Run a quick competitive analysis and identify:
1. What features are table stakes
2. Where competitors fall short
3. One differentiator we could own

Output a 1-page research brief. Remember it tagged for this project when done.
```

UX Researcher は調査ブリーフを作成し、`ux-researcher`, `retroboard`, `research-brief` のタグでメモリに保存します。

**Step 3 — Backend Architect に引き継ぎ**

```
Activate Backend Architect.

Project: RetroBoard. Recall the sprint plan and research brief from previous agents.
Stack: Node.js, Express, PostgreSQL, Socket.io for real-time.

Design:
1. Database schema (SQL)
2. REST API endpoints list
3. WebSocket events for real-time board updates
4. Auth strategy recommendation

Remember each deliverable tagged for this project and for the frontend-developer.
```

Backend Architect はメモリからスプリント計画と調査ブリーフを自動で参照し、スキーマと API 仕様を `backend-architect`, `retroboard`, `api-spec`, `frontend-developer` のタグで保存します。

### Week 2: Build Core Features

**Step 4 — Frontend Developer と Rapid Prototyper を起動**

```
Activate Frontend Developer.

Project: RetroBoard. Recall the API spec and schema from the Backend Architect.

Build the RetroBoard React app:
- Stack: React, TypeScript, Tailwind, Socket.io-client
- Pages: Login, Dashboard, Board view
- Components: RetroCard, VoteButton, ActionItem, BoardColumn

Start with the Board view — it's the core experience.
Focus on real-time: when one user adds a card, everyone sees it.
Remember your progress tagged for this project.
```

Frontend Developer は API 仕様をメモリから取得してビルドを進めます。

**Step 5 — 中間で Reality Check を実行**

```
Activate Reality Checker.

Project: RetroBoard. We're at week 2 of a 4-week MVP build.

Recall all deliverables from previous agents for this project.

Evaluate:
1. Can we realistically ship in 2 more weeks?
2. What should we cut to make the deadline?
3. Any technical debt that will bite us at launch?

Remember your verdict tagged for this project.
```

Reality Checker はこれまでのすべての納品物（スプリント計画、調査ブリーフ、スキーマ、API 仕様、フロントエンド進捗）を参照でき、あなたがそれらを集めて貼り付ける必要はありません。

### Week 3: Polish + Landing Page

**Step 6 — Frontend Developer 続行、Growth Hacker 開始**

```
Activate Growth Hacker.

Product: RetroBoard — team retrospective tool, launching in 1 week.
Target: Engineering managers and scrum masters at remote-first companies.
Budget: $0 (organic launch only).

Recall the project context and Reality Checker's verdict.

Create a launch plan:
1. Landing page copy (hero, features, CTA)
2. Launch channels (Product Hunt, Reddit, Hacker News, Twitter)
3. Day-by-day launch sequence
4. Metrics to track in week 1

Remember the launch plan tagged for this project.
```

### Week 4: Launch

**Step 7 — 最終 Reality Check**

```
Activate Reality Checker.

Project: RetroBoard, ready to launch.

Recall all project context, previous verdicts, and the launch plan.

Evaluate production readiness:
- Live URL: [url]
- Test accounts created: yes
- Error monitoring: Sentry configured
- Database backups: daily automated

Run through the launch checklist and give a GO / NO-GO decision.
Require evidence for each criterion.
```

### QA が失敗したとき：ロールバック

標準ワークフローでは Reality Checker が成果物を拒否した場合、該当スペシャリストに戻って説明し直します。メモリを使うと回復ループが短くなります：

```
Activate Backend Architect.

Project: RetroBoard. The Reality Checker flagged issues with the API design.
Recall the Reality Checker's feedback and your previous API spec.
Roll back to your last known-good schema and address the specific issues raised.
Remember the updated deliverables when done.
```

Backend Architect は Reality Checker が指摘した箇所を正確に参照し、自分の以前の成果物を呼び出し、チェックポイントにロールバックして修正を行い、すべてを自動で管理できます。

## Before and After

| Aspect | Standard Workflow | With Memory |
|--------|------------------|-------------|
| **Handoffs** | エージェント間で出力をコピペ | エージェントが必要なものを自動で想起 |
| **Context loss** | セッションタイムアウトで消える | メモリがセッションを越えて保持 |
| **Multi-agent context** | N 個のエージェントから手動でコンテキストを集める | エージェントがプロジェクトタグでメモリ検索 |
| **QA failure recovery** | 問題点を手動で説明して戻す | エージェントがフィードバックを呼び出してロールバック |
| **Multi-day projects** | 毎セッションでコンテキスト再構築が必要 | エージェントが中断したところから開始 |
| **Setup required** | なし | MCP メモリサーバーをインストール |

## 主要パターン

1. **すべてをプロジェクト名でタグ付け**: これにより参照が可能になります。各メモリは `retroboard` のようなタグを持ちます。
2. **受け手のエージェントにタグ付け**: Backend Architect が API 仕様を作成したら `frontend-developer` をタグに追加して、フロントエンドが見つけられるようにします。
3. **Reality Checker は全体可視化を得る**: すべてのエージェントが作業をメモリに保存するので、Reality Checker はあなたが手で集めることなくプロジェクトのすべてを呼び出せます。
4. **ロールバックは手動の取り消しに代わる**: 何かが失敗したらチェックポイントへ戻して修正を行います。

## ヒント

- すべてのエージェントを同時に変更する必要はありません。まず最も頻繁に使うエージェントにメモリ統合を追加し、徐々に拡張してください。
- メモリ命令はプロンプトです。LLM がそれを解釈し、必要に応じて MCP ツールを呼び出します。文面はあなたのスタイルに合わせて調整できます。
- `remember`, `recall`, `rollback`, `search` をサポートする任意の MCP 互換メモリサーバーがこのワークフローで動作します。
