# 🔍 フェーズ0 プレイブック — インテリジェンス＆ディスカバリー

> **期間**: 3–7日 | **エージェント数**: 6 | **ゲートキーパー**: Executive Summary Generator

---

## 目的

リソースを投入する前に機会を検証する。問題、マーケット、規制環境が理解されるまでは構築を開始しない。

## 事前条件

- [ ] プロジェクトブリーフまたは初期コンセプトが存在する
- [ ] ステークホルダーのスポンサーが決まっている
- [ ] ディスカバリーフェーズの予算が承認されている

## エージェント起動シーケンス

### Wave 1: 並列起動（Day 1）

#### 🔍 Trend Researcher — マーケットインテリジェンスリード

```
Activate Trend Researcher for market intelligence on [PROJECT DOMAIN].

Deliverables required:
1. Competitive landscape analysis (direct + indirect competitors)
2. Market sizing: TAM, SAM, SOM with methodology
3. Trend lifecycle mapping: where is this market in the adoption curve?
4. 3-6 month trend forecast with confidence intervals
5. Investment and funding trends in the space

Sources: Minimum 15 unique, verified sources
Format: Strategic Report with executive summary
Timeline: 3 days
```

#### 💬 Feedback Synthesizer — ユーザーニーズ分析

```
Activate Feedback Synthesizer for user needs analysis on [PROJECT DOMAIN].

Deliverables required:
1. Multi-channel feedback collection plan (surveys, interviews, reviews, social)
2. Sentiment analysis across existing user touchpoints
3. Pain point identification and prioritization (RICE scored)
4. Feature request analysis with business value estimation
5. Churn risk indicators from feedback patterns

Format: Synthesized Feedback Report with priority matrix
Timeline: 3 days
```

#### 🔍 UX Researcher — ユーザー行動分析

```
Activate UX Researcher for user behavior analysis on [PROJECT DOMAIN].

Deliverables required:
1. User interview plan (5-10 target users)
2. Persona development (3-5 primary personas)
3. Journey mapping for primary user flows
4. Usability heuristic evaluation of competitor products
5. Behavioral insights with statistical validation

Format: Research Findings Report with personas and journey maps
Timeline: 5 days
```

### Wave 2: 並列起動（Day 1、Wave 1 と独立）

#### 📊 Analytics Reporter — データレンドスケープ評価

```
Activate Analytics Reporter for data landscape assessment on [PROJECT DOMAIN].

Deliverables required:
1. Existing data source audit (what data is available?)
2. Signal identification (what can we measure?)
3. Baseline metrics establishment
4. Data quality assessment with completeness scoring
5. Analytics infrastructure recommendations

Format: Data Audit Report with signal map
Timeline: 2 days
```

#### ⚖️ Legal Compliance Checker — 規制スキャン

```
Activate Legal Compliance Checker for regulatory scan on [PROJECT DOMAIN].

Deliverables required:
1. Applicable regulatory frameworks (GDPR, CCPA, HIPAA, etc.)
2. Data handling requirements and constraints
3. Jurisdiction mapping for target markets
4. Compliance risk assessment with severity ratings
5. Blocking vs. manageable compliance issues

Format: Compliance Requirements Matrix
Timeline: 3 days
```

#### 🛠️ Tool Evaluator — 技術ランドスケープ

```
Activate Tool Evaluator for technology landscape assessment on [PROJECT DOMAIN].

Deliverables required:
1. Technology stack assessment for the problem domain
2. Build vs. buy analysis for key components
3. Integration feasibility with existing systems
4. Open source vs. commercial evaluation
5. Technology risk assessment

Format: Tech Stack Assessment with recommendation matrix
Timeline: 2 days
```

## 収束点（Day 5–7）

すべての 6 エージェントが報告を提出します。Executive Summary Generator が次を統合します。

```
Activate Executive Summary Generator to synthesize Phase 0 findings.

Input documents:
1. Trend Researcher → Market Analysis Report
2. Feedback Synthesizer → Synthesized Feedback Report
3. UX Researcher → Research Findings Report
4. Analytics Reporter → Data Audit Report
5. Legal Compliance Checker → Compliance Requirements Matrix
6. Tool Evaluator → Tech Stack Assessment

Output: Executive Summary (≤500 words, SCQA format)
Decision required: GO / NO-GO / PIVOT
Include: Quantified market opportunity, validated user needs, regulatory path, technology feasibility
```

## 品質ゲートチェックリスト

| # | 判定基準 | 証拠ソース | ステータス |
|---|-----------|------------|-----------|
| 1 | 市場機会が検証されている（TAM が最小閾値を超えている） | Trend Researcher レポート | ☐ |
| 2 | ≥3 の検証済みユーザー課題がある | Feedback Synthesizer + UX Researcher | ☐ |
| 3 | ブロッキングなコンプライアンス問題がない | Legal Compliance Checker マトリックス | ☐ |
| 4 | 主要指標とデータソースが特定されている | Analytics Reporter の監査 | ☐ |
| 5 | 技術スタックの実現可能性が評価されている | Tool Evaluator の評価 | ☐ |
| 6 | Executive Summary が GO/NO-GO 推奨を含む | Executive Summary Generator | ☐ |

## ゲート判定

- **GO**: Phase 1 — Strategy & Architecture に進む
- **NO-GO**: 調査結果をアーカイブし、学びを文書化してリソースを再配分する
- **PIVOT**: 調査に基づいて範囲/方向を修正し、ターゲットディスカバリーを再実施する

## Phase 1 への引き渡し

```markdown
## Phase 0 → Phase 1 Handoff Package

### 引き継ぐドキュメント:
1. Market Analysis Report (Trend Researcher)
2. Synthesized Feedback Report (Feedback Synthesizer)
3. User Personas and Journey Maps (UX Researcher)
4. Data Audit Report (Analytics Reporter)
5. Compliance Requirements Matrix (Legal Compliance Checker)
6. Tech Stack Assessment (Tool Evaluator)
7. Executive Summary with GO decision (Executive Summary Generator)

### 主要な制約:
- [Legal Compliance Checker による規制制約]
- [Tool Evaluator による技術的制約]
- [Trend Researcher による市場タイミング制約]

### Sprint Prioritizer 向けの優先ユーザーニーズ:
1. [Feedback Synthesizer からの課題1]
2. [UX Researcher からの課題2]
3. [Feedback Synthesizer からの課題3]
```

---

*Phase 0 は、Executive Summary Generator が 6 つのディスカバリーエージェントからの証拠に基づく GO 判定を出した時点で完了します。*
