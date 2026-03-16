# GitHub Copilot 統合

The Agency は GitHub Copilot と互換性があり、変換は不要です。`.md` と YAML フロントマター形式でそのまま利用できます。

## インストール

```bash
# 全エージェントを GitHub Copilot のエージェントディレクトリへコピー
./scripts/install.sh --tool copilot

# あるいはカテゴリ単位で手動コピー
cp engineering/*.md ~/.github/agents/
cp engineering/*.md ~/.copilot/agents/
```

## エージェントの有効化

GitHub Copilot セッション内でエージェント名を指定して呼び出します：

```
Activate Frontend Developer and help me build a React component.
```

```
Use the Reality Checker agent to verify this feature is production-ready.
```

## エージェントの構成

エージェントは部門ごとに整理されています。詳細は [main README](../../README.md) を参照してください。