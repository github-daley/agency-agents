# Antigravity 統合

61のAgencyエージェントをAntigravityのスキルとしてインストールします。各エージェントは `agency-` プレフィックスが付与され、既存スキルとの衝突を避けます。

## インストール

```bash
./scripts/install.sh --tool antigravity
```

このコマンドは `integrations/antigravity/` 配下のファイルを `~/.gemini/antigravity/skills/` にコピーします。

## スキルの有効化

Antigravityではスラグ（slug）でエージェントを指定します：

```
Use the agency-frontend-developer skill to review this component.
```

利用可能なスラグの例：
- `agency-frontend-developer`
- `agency-backend-architect`
- `agency-reality-checker`
- `agency-growth-hacker`

## 再生成

エージェントを変更したらスキルファイルを再生成してください：

```bash
./scripts/convert.sh --tool antigravity
```

## ファイル形式

各スキルは Antigravity 互換の `SKILL.md` ファイルで、以下のようなフロントマターを持ちます：

```yaml
---
name: agency-frontend-developer
description: Expert frontend developer specializing in...
risk: low
source: community
date_added: '2026-03-08'
---
```
