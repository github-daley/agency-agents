# Aider 統合

すべての61のAgencyエージェントを1つの `CONVENTIONS.md` ファイルにまとめています。Aiderはプロジェクトルートにこのファイルがあると自動的に読み込みます。

## インストール

```bash
# プロジェクトルートから実行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool aider
```

## エージェントの有効化

Aiderセッション内でエージェント名を指定して使用します：

```
Use the Frontend Developer agent to refactor this component.
```

あるいは：

```
Apply the Reality Checker agent to verify this is production-ready.
```

## 手動での利用

`CONVENTIONS.md` を直接渡すこともできます：

```bash
aider --read CONVENTIONS.md
```

## 再生成

```bash
./scripts/convert.sh --tool aider
```