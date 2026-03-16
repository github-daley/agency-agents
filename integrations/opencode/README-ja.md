# OpenCode 統合

OpenCode 向けに、`.md` 形式のエージェントを `.opencode/agents/` に生成します。コンバータは名前付き色を16進のカラーコードに変換し、`mode: subagent` を追加してサブエージェントとして動作させます。

## インストール

```bash
# プロジェクトルートから実行
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

この操作により `.opencode/agents/<slug>.md` がプロジェクト内に作成されます。

## 有効化

OpenCode では `@` プレフィックスでサブエージェントを呼び出します：

```
@frontend-developer help build this component.
```

またはエージェントピッカーから選択できます。

## エージェント形式

生成されるファイルには次のようなフロントマターが含まれます：

```yaml
---
name: Frontend Developer
description: Expert frontend developer specializing in modern web technologies...
mode: subagent
color: "#00FFFF"
---
```

- **mode: subagent** — メインのタブ循環には表示されず、オンデマンドで利用されます
- **color** — 名前色は自動で16進に変換されます

## プロジェクトスコープ

`.opencode/agents/` のエージェントはプロジェクトスコープです。グローバルで使いたい場合は以下へコピーします：

```bash
mkdir -p ~/.config/opencode/agents
cp integrations/opencode/agents/*.md ~/.config/opencode/agents/
```

## 再生成

```bash
./scripts/convert.sh --tool opencode
```