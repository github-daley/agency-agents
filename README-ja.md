# 🎭 The Agency: AIスペシャリストがワークフローを変える

このリポジトリは、ドメイン特化型のAIエージェント（Markdown形式）を集めたカタログです。各エージェントはフロントマター（YAML）と本文（パーソナ/ワークフロー/成果物）を持ち、さまざまなツール向けに変換・インストールできます。

## ⚡ クイックスタート

1. エージェントをローカルにコピーして使う（Claude Code向け推奨）:

```bash
cp -r agency-agents/* ~/.claude/agents/
# 例: "Hey Claude, activate Frontend Developer mode and help me build a React component"
```

2. 参照用として利用する:

- 各エージェントは以下を含みます: アイデンティティ、コアミッション、技術成果物、成功指標、ワークフロー

3. 他ツールとの連携（変換 → インストール）:

```bash
# 変換: 各ツール向けの統合ファイルを生成します
./scripts/convert.sh
# 対象ツールのみ変換する場合:
./scripts/convert.sh --tool cursor

# 生成したファイルをインストール（対話式）
./scripts/install.sh
# 特定ツールにだけインストールする場合:
./scripts/install.sh --tool copilot
```

※ 注意: このリポジトリでは `integrations/` 以下は生成物です。手元で `convert.sh` を実行してから `install.sh` を使ってください。

---

## 🔌 マルチツール統合（概要）

サポートする主なツール:

- Claude Code — ネイティブ `.md` エージェント
- GitHub Copilot — `~/.github/agents/`, `~/.copilot/agents/`
- Antigravity / Gemini CLI — SKILL.md 形式
- Cursor — `.cursor/rules/`（プロジェクトスコープ）
- Aider / Windsurf — 単一の変換ファイル（CONVENTIONS.md / .windsurfrules）
- OpenCode / OpenClaw / Qwen Code — 各フォーマットに変換

変換の流れ:

1. source: `/<category>/*.md`（例: engineering/）
2. `./scripts/convert.sh` が `integrations/<tool>/` に各ツール用のファイルを生成
3. `./scripts/install.sh` が `integrations/` からユーザーのツール設定ディレクトリへコピー

---

## 使いどころ

- エージェントの追加や改善は、まずソースの `.md` を編集します。
- 生成物を直接編集せず、`convert.sh` と `install.sh` のワークフローに従ってください。

## ライセンス

このリポジトリのライセンスはリポジトリルートの `LICENSE` を参照してください。
