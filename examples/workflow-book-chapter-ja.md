# ワークフロー例：書籍章の開発

> 著者のラフな素材（ボイスメモや断片的なメモ）を戦略的な第一稿の章に仕上げるための、単一エージェント中心のワークフロー。

## いつ使うか

声のメモや断片、戦略的メモはあるが、まとまった章の草稿がない場合に使います。目的は一般的な代筆ではなく、著者のパーソナルな語りを活かしつつ、カテゴリ上のポジショニングを強化する草稿を作ることです。

## 使用エージェント

| エージェント | 役割 |
|--------------|------|
| Book Co-Author | ソース素材をバージョン管理された章草稿に変換し、編集ノートと次の修正の質問を提示する |

## 起動例

```text
Activate Book Co-Author.

Book goal: Build authority around practical AI adoption for Mittelstand companies.
Target audience: Owners and operational leaders of 20-200 person businesses.
Chapter topic: Why most AI projects fail before implementation starts.
Desired draft maturity: First substantial draft.

Raw material:
- Voice memo: "The real failure happens in expectation setting, not tooling."
- Notes: Leaders buy software before defining the operational bottleneck.
- Story fragment: We nearly rolled out the wrong automation in a cabinetmaking workflow because the actual problem was quoting delays, not production throughput.
- Positioning angle: Practical realism over hype.

Produce:
1. Chapter objective and strategic role in the book
2. Any clarification questions you need
3. Chapter 2 - Version 1 - ready for review
4. Editorial notes on assumptions and proof gaps
5. Specific next-step revision requests
```

## 期待される出力形式

Book Co-Author は次の 5 部分で応答します：

1. `Target Outcome`
2. `Chapter Draft`
3. `Editorial Notes`
4. `Feedback Loop`
5. `Next Step`

## 品質基準

- 草稿は一人称であること
- 章は一つの明確な約束と内部論理を持つこと
- 主張は出典に基づくか、仮定として明示されること
- 一般的な励まし文は除く
- 出力は具体的な修正質問で終わること（あいまいな受け渡しで終わらない）
