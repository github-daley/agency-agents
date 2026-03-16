# 🔌 統合（Integrations）

このディレクトリには、The Agency の統合とエージェント型コーディングツール向けの変換フォーマットが含まれます。

## サポートされているツール

- **Claude Code** — `.md` 形式のエージェントをそのまま利用できます
- **GitHub Copilot** — `.md` 形式のエージェントをそのまま利用できます
- **Antigravity** — `antigravity/` にある各エージェントは `SKILL.md` として配布されます
- **Gemini CLI** — 拡張と `SKILL.md` ファイルで提供されます
- **OpenCode** — `.md` エージェントファイルを `.opencode/agents/` に生成します
- **OpenClaw** — `SOUL.md` / `AGENTS.md` / `IDENTITY.md` を含むワークスペースを生成します
- **Cursor** — `.mdc` ルールファイルを生成します（プロジェクト単位）
- **Aider** — すべてのエージェントを `CONVENTIONS.md` にまとめます
- **Windsurf** — `.windsurfrules` へまとめて出力します

## クイックインストール

```bash
# 検出されたすべてのツール向けにインストール
./scripts/install.sh

# 個別ツールのインストール例
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool claude-code

# Gemini CLI は生成ファイルが必要
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

プロジェクトスコープのツール（OpenCode、Cursor、Aider、Windsurf）では、ターゲットプロジェクトのルートからインストーラを実行してください。

## 統合ファイルの再生成

エージェントを追加・変更した場合、統合ファイルを再生成します：

```bash
./scripts/convert.sh
```

---

## Claude Code

The Agency は元々 Claude Code 向けに設計されています。変換は不要で、`.md` + YAML フロントマター形式でそのまま動作します。

```bash
cp -r <category>/*.md ~/.claude/agents/
# あるいは一括インストール:
./scripts/install.sh --tool claude-code
```

詳細は [claude-code/README.md](claude-code/README.md) を参照してください。

---

## GitHub Copilot

The Agency は GitHub Copilot とも互換性があります。エージェントを直接 `~/.github/agents/` や `~/.copilot/agents/` にコピーして利用できます。

```bash
./scripts/install.sh --tool copilot
```

詳細は [github-copilot/README.md](github-copilot/README.md) を参照してください。

---

## Antigravity

各エージェントは `~/.gemini/antigravity/skills/` に `agency-` プレフィックス付きのスキルとしてインストールされます。

```bash
./scripts/install.sh --tool antigravity
```

詳細は [antigravity/README.md](antigravity/README.md) を参照してください。

---

## Gemini CLI

エージェントは Gemini CLI 拡張としてパッケージされます。新しいクローンからインストールする場合は、生成ステップが必要です。

```bash
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

詳細は [gemini-cli/README.md](gemini-cli/README.md) を参照してください。

---

## OpenCode

各エージェントは `.opencode/agents/` にプロジェクトスコープの `.md` ファイルとして生成されます。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool opencode
```

詳細は [opencode/README.md](opencode/README.md) を参照してください。

---

## OpenClaw

各エージェントは `SOUL.md`, `AGENTS.md`, `IDENTITY.md` を含むワークスペースとして生成されます。インストールの前にワークスペースを生成してください：

```bash
./scripts/convert.sh --tool openclaw
```

その後インストールします：

```bash
./scripts/install.sh --tool openclaw
```

詳細は [openclaw/README.md](openclaw/README.md) を参照してください。

---

## Cursor

各エージェントは `.mdc` ルールファイルになります。ルールはプロジェクト単位で利用します。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool cursor
```

詳細は [cursor/README.md](cursor/README.md) を参照してください。

---

## Aider

全エージェントを単一の `CONVENTIONS.md` にまとめ、Aider はプロジェクトルートにこのファイルがあると自動的に読み込みます。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool aider
```

詳細は [aider/README.md](aider/README.md) を参照してください。

---

## Windsurf

全エージェントを単一の `.windsurfrules` ファイルにまとめて出力します。プロジェクトルートからインストールしてください。

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool windsurf
```

詳細は [windsurf/README.md](windsurf/README.md) を参照してください。