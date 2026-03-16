# Claude Code 統合

The Agency は Claude Code 向けに作られており、変換は不要です。`.md` と YAML フロントマター形式のままで動作します。

## インストール

```bash
# 全エージェントを Claude Code のエージェントディレクトリへコピー
./scripts/install.sh --tool claude-code

# あるいはカテゴリ単位で手動コピー
cp engineering/*.md ~/.claude/agents/
```

## エージェントの有効化

Claude Code セッション内でエージェント名を指定して呼び出します：

```
Activate Frontend Developer and help me build a React component.
```

```
Use the Reality Checker agent to verify this feature is production-ready.
```

## エージェントの構成

エージェントは部門ごとに整理されています。詳細は [main README](../../README.md) を参照してください。