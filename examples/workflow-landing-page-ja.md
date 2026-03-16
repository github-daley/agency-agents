# マルチエージェントワークフロー：ランディングページスプリント

> 4 つのエージェントを使って 1 日でコンバージョン最適化されたランディングページを出荷する。

## シナリオ

新製品のランディングページが必要で、見栄えがよく、コンバージョンし、当日中に公開できることが条件です。

## エージェントチーム

| エージェント | 役割 |
|--------------|------|
| Content Creator | コピー作成 |
| UI Designer | レイアウトとコンポーネント仕様作成 |
| Frontend Developer | 実装 |
| Growth Hacker | コンバージョン最適化 |

## ワークフロー概要

### 朝：コピー + デザイン（並列）

**Step 1a — Content Creator を起動**

```
Activate Content Creator.

Write landing page copy for "FlowSync" — an API integration platform
that connects any two SaaS tools in under 5 minutes.

Target audience: developers and technical PMs at mid-size companies.
Tone: confident, concise, slightly playful.

Sections needed:
1. Hero (headline + subheadline + CTA)
2. Problem statement (3 pain points)
3. How it works (3 steps)
4. Social proof (placeholder testimonial format)
5. Pricing (3 tiers: Free, Pro, Enterprise)
6. Final CTA

Keep it scannable. No fluff.
```

**Step 1b — UI Designer を並列で起動**

```
Activate UI Designer.

Design specs for a SaaS landing page. Product: FlowSync (API integration platform).
Style: clean, modern, dark mode option. Think Linear or Vercel aesthetic.

Deliver:
1. Layout wireframe (section order + spacing)
2. Color palette (primary, secondary, accent, background)
3. Typography (font pairing, heading sizes, body size)
4. Component specs: hero section, feature cards, pricing table, CTA buttons
5. Responsive breakpoints (mobile, tablet, desktop)
```

### 午前中：ビルド

**Step 2 — Frontend Developer を起動**

```
Activate Frontend Developer.

Build a landing page from these specs:

Copy: [paste Content Creator output]
Design: [paste UI Designer output]

Stack: HTML, Tailwind CSS, minimal vanilla JS (no framework needed).
Requirements:
- Responsive (mobile-first)
- Fast (no heavy assets, system fonts OK)
- Accessible (proper headings, alt text, focus states)
- Include a working email signup form (action URL: /api/subscribe)

Deliver a single index.html file ready to deploy.
```

### 午後：最適化

**Step 3 — Growth Hacker を起動**

```
Activate Growth Hacker.

Review this landing page for conversion optimization:

[paste the HTML or describe the current page]

Evaluate:
1. Is the CTA above the fold?
2. Is the value proposition clear in under 5 seconds?
3. Any friction in the signup flow?
4. What A/B tests would you run first?
5. SEO basics: meta tags, OG tags, structured data

Give me specific changes, not general advice.
```

## タイムライン（例）

| 時間 | 活動 | エージェント |
|------|------|--------------|
| 9:00 | コピー + デザイン開始（並列） | Content Creator + UI Designer |
| 11:00 | ビルド開始 | Frontend Developer |
| 14:00 | 第一版完成 | — |
| 14:30 | コンバージョンレビュー | Growth Hacker |
| 15:30 | フィードバック適用 | Frontend Developer |
| 16:30 | 出荷 | Vercel/Netlify へデプロイ |

## キーパターン

1. コピーとデザインは独立して並列で行う
2. フロントエンドは両方の出力を受け取って統合する
3. Growth Hacker のレビューは具体的な変更提案であること
4. 各ステップは時間箱を守ること（scope creep を防ぐ）
