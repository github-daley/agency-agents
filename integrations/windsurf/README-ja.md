# Windsurf 統合

61のAgencyエージェントを単一の `.windsurfrules` ファイルにまとめます。ルールはプロジェクト単位で利用されます。

## インストール

```bash
# プロジェクトルートから実行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool windsurf
```

## エージェントの利用

Windsurf ではプロンプト内でエージェント名を指定して使用します：

```
Use the Frontend Developer agent to build this component.
```

## 再生成

```bash
./scripts/convert.sh --tool windsurf
```