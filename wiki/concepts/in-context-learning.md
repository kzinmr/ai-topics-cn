---
title: In-context Learning（ICL）— コンテキスト内学習
created: 2026-04-23
updated: 2026-04-23
tags: [concept, llm, prompt-engineering, icl]
aliases: ["In-context Learning", "ICL", "コンテキスト内学習", "内文学習", "In-Context Learning"]
source_lang: zh-CN
---

# In-context Learning（ICL）— コンテキスト内学習

> **トレンド順位**: —（2026-04-23初出）
> **ソース**: 掘金
> **重要度**: 中 — LLMの動作原理を説明する基本概念

## 概要

In-context Learning（ICL、コンテキスト内学習）は、大規模言語モデルが**学習パラメータを変更せずに**、プロンプト内の例（examples）からパターンを抽出してタスクを実行する能力。中国語圏のAIコミュニティでは「**内文学習**」または「**インコンテキストラーニング**」として知られる。

典型的な例：
- 「北京 → China」「東京 → Japan」「巴黎 → ?」とプロンプトに例を示すと、モデルは「France」を返す
- 明示的なfine-tuningなしで、タスクの仕方を「学ぶ」

## 中国AIコミュニティでの議論

2026年4月20日、掘金で「**大模型根本不是「学会了」，它只是会「看例子」**」（大模型根本不是「学会了」，它只是会「看例子」）という記事が投稿され、以下の要点が議論されている：

1. **LLMは実際に「学習」していない** — パラメータ更新なしでコンテキスト内のパターンを模倣
2. **Few-shot promptingの重要性** — 例の質が出力品質に直接影響
3. **Chain-of-Thoughtとの関係** — ICLはCoT（思考連鎖）と組み合わせて効果的
4. **Limitations** — コンテキストウィンドウの制限、ノイズへの脆弱性

> **出典**: 掘金 — [https://juejin.cn/post/7630730075692449855](https://juejin.cn/post/7630730075692449855)

## ICLと関連概念

| 概念 | 関係性 |
|------|--------|
| [[function-calling]] | ICLの特殊形態（ツール使用例を含むプロンプト） |
| [[vibe-coding]] | ICLの応用（コード例を提示して生成） |
| [[prompt-agent-function-call-skill-mcp]] | ICLがMCP/Function Callingの基盤 |
| [[langchain]] | LangChainはICLを活用したテンプレートシステム |
| [[ai-agent]] | エージェントはICLを活用してタスクを遂行 |

## 研究文献

- **GPT-3 Paper** (2020): In-context Learningの概念を初めて体系的に記述
- **Learning to Prompt** (2021): 自動few-shot exemplar selection
- **Chain-of-Thought Prompting** (2022): ICLに推論ステップを付加

## 関連リンク

### 外部ソース

| ソース | URL | 概要 |
|---|---|---|
| 掘金 — ICL解説 | [juejin.cn/post/7630730075692449855](https://juejin.cn/post/7630730075692449855) | ICLの基本概念解説 |
