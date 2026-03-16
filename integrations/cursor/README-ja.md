# Cursor 統合

61のAgencyエージェントを Cursor の `.mdc` ルールファイルに変換します。ルールは**プロジェクト単位**で利用します。

## インストール

```bash
# プロジェクトルートから実行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool cursor
```

この操作により `.cursor/rules/<agent-slug>.mdc` がプロジェクトに作成されます。

## ルールの有効化

Cursorではプロンプト内でエージェントを参照します：

```
@frontend-developer Review this React component for performance issues.
```

あるいはフロントマターで常時適用する設定にできます：

```yaml
---
description: Expert frontend developer...
globs: "**/*.tsx,**/*.ts"
alwaysApply: true
---
```

## 再生成

```bash
./scripts/convert.sh --tool cursor
```