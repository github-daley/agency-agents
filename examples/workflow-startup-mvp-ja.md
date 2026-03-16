# マルチエージェントワークフロー：スタートアップMVP

> アイデアからリリースまで複数のエージェントを調整するステップバイステップの例です。

## シナリオ

あなたは SaaS の MVP（リモートチーム向けのチームレトロスペクティブツール）を作ります。4 週間で動くプロダクト、ユーザーサインアップ、コア機能、ランディングページを出荷する必要があります。

## エージェントチーム

| エージェント | このワークフローでの役割 |
|--------------|-------------------------|
| Sprint Prioritizer | プロジェクトを週ごとのスプリントに分解する |
| UX Researcher | クイックなユーザーインタビューでアイデアを検証する |
| Backend Architect | API とデータモデルを設計する |
| Frontend Developer | React アプリを構築する |
| Rapid Prototyper | 最速で初版を動かす |
| Growth Hacker | 構築中にローンチ戦略を計画する |
| Reality Checker | 各マイルストーンで品質ゲートを担当する |

## ワークフロー（概要）

### Week 1: Discovery + Architecture

**Step 1 — Sprint Prioritizer を起動**

```
Activate Sprint Prioritizer.

Project: RetroBoard — a real-time team retrospective tool for remote teams.
Timeline: 4 weeks to MVP launch.
Core features: user auth, create retro boards, add cards, vote, action items.
Constraints: solo developer, React + Node.js stack, deploy to Vercel + Railway.

Break this into 4 weekly sprints with clear deliverables and acceptance criteria.
```

### Week 2: Build Core Features

Frontend と Rapid Prototyper が API 仕様を受け取りながらボードビューを優先して開発します。

### Week 3: Polish + Landing Page

Growth Hacker がランディングページのコピーとチャネルを計画し、フロントエンドが組み上げます。

### Week 4: Launch

Reality Checker による最終確認を経て、公開判定（GO / NO-GO）を行います。

## キーパターン

1. 各エージェントの出力は次のエージェントの入力になる（シーケンシャルハンドオフ）
2. 並列作業を適切に組み合わせる（例：UX 調査とスプリント設計は同時に走る）
3. 品質ゲート（Reality Checker）は中間とローンチ前に必ず入れる
4. コンテキストは可能な限り完全に渡す（コピペで貼り付ける）

## ヒント

- ステップ間ではエージェントの出力をコピペして渡してください。要約ではなくフル出力が理想です。
- Reality Checker が問題を指摘したら、該当スペシャリストに戻して修正を行い、再度チェックするループを回してください。
- 手動ワークフローに慣れたら、Orchestrator を使って自動化を検討しましょう。
