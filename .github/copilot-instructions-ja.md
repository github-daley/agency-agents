# The Agency リポジトリ用 Copilot 指示（日本語）

以下は、このリポジトリで Copilot セッションや類似の AI アシスタントを実行する際に有用なリポジトリ固有の情報です。

## 実行可能なコマンド（リポジトリルートで実行）

```bash
# エージェントの基本的な検証（リント）
./scripts/lint-agents.sh

# 単一ファイルだけ検証する例
./scripts/lint-agents.sh engineering/engineering-frontend-developer.md

# すべてのエージェントを各ツール向けに変換（integrations/ 生成）
./scripts/convert.sh

# 特定ツールのみ変換
./scripts/convert.sh --tool cursor

# 生成済みの integrations/ をローカルツールにインストール（コピー）
./scripts/install.sh --tool copilot
```

- `lint-agents.sh` が PR で実行される検証スクリプトです。`name`, `description`, `color` の frontmatter を必須としてチェックします。
- `convert.sh` はソースの `.md` を読み、`integrations/<tool>/` に各ツール向けのファイルを生成します。
- `install.sh` は `integrations/` の生成物をユーザー環境へコピーします（実行は任意・推奨は手動実行）。

## 高レベル構造

- ソース（真の編集対象）はカテゴリ配下の Markdown ファイル（例: `engineering/`）です。
- 変換 → インストール の流れを守ることで生成物を直接編集する必要はありません。

## 主要な作法

- frontmatter に `name`, `description`, `color` を必須で含める。
- `Identity`, `Core Mission`, `Critical Rules` 等のセクションヘッダを分けると OpenClaw への出力が整備されます。
- 生成物はコミットしない（`integrations/` は生成対象）。

## 注意点

- `convert.sh` は `academic/` や `sales/` も処理しますが、`lint-agents.sh` のデフォルト走査には含まれないカテゴリがあります（カテゴリ間で検証範囲が微妙に異なるため、該当カテゴリは注意して確認してください）。

---

必要なら、他のファイルも順次日本語翻訳して `{file-name}-ja.md` を作成します。続けて翻訳を希望されるか指示してください（この作業では `install.sh` を実行しません）。