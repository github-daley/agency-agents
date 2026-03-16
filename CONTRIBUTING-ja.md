# 🤝 The Agency への貢献（日本語訳）

貢献していただきありがとうございます！このガイドは、エージェントを追加・改善する際の主な手順と期待事項を要約したものです。

## 🧭 主要な貢献フロー

1. リポジトリをフォークしてください。
2. 適切なカテゴリ（例: `engineering/`, `design/`, `marketing/` など）を選びます。
3. 既存のエージェントの構成に合わせて新しい `.md` ファイルを作成します（テンプレートに従うこと）。
4. 実際にそのエージェントを使ってテストし、動作や記述を確認します。
5. PR を作成し、説明とテスト内容を明記してください。

## 📄 エージェントファイル構造（推奨）

YAML フロントマター（例）:

```markdown
---
name: Agent Name
description: 一行での説明
color: cyan
emoji: 🎯
vibe: 親しみやすい性格の一文
services:
  - name: Service Name
    url: https://service.example
    tier: free
---
```

本文は大きく2つのグループに分けます:

- Persona（Identity, Communication Style, Critical Rules）
- Operations（Core Mission, Technical Deliverables, Workflow Process, Success Metrics）

## 🔍 レビューと PR のポイント

- 小さな PR（基本的に1つの `.md`）が最も歓迎されます。
- 大規模なツール変更や多ファイルに跨る変更は事前に Discussion を開いてください。
- 生成物（`integrations/` 以下）はコミットしないでください。

## ✅ チェックリスト

- テンプレートに従っている
- 最低限の frontmatter（name, description, color）を含む
- 実用的なコード例や成果物、成功指標を含む

---

このファイルはリポジトリの CONTRIBUTING.md を日本語化した要約です。より詳細な手順や例は元の CONTRIBUTING.md を参照してください。
