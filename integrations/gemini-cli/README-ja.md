# Gemini CLI 統合

61のAgencyエージェントを Gemini CLI の拡張としてパッケージします。拡張は `~/.gemini/extensions/agency-agents/` にインストールされます。

## インストール

```bash
# まず Gemini CLI 用の統合ファイルを生成
./scripts/convert.sh --tool gemini-cli

# 次に拡張をインストール
./scripts/install.sh --tool gemini-cli
```

## スキルの有効化

Gemini CLI ではエージェント名で参照します：

```
Use the frontend-developer skill to help me build this UI.
```

## 拡張の構成

```
~/.gemini/extensions/agency-agents/
  gemini-extension.json
  skills/
    frontend-developer/SKILL.md
    backend-architect/SKILL.md
    reality-checker/SKILL.md
    ...
```

## 再生成

```bash
./scripts/convert.sh --tool gemini-cli
```
