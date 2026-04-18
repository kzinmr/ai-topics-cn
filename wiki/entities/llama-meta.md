---
title: "Llama（Meta）— Meta AIのオープンソースLLMファミリ"
created: 2026-04-18
updated: 2026-04-18
tags: [llm, model, open-source-ai, company, us, meta, multimodal]
aliases: ["Llama", "Meta Llama", "LLaMA", "Meta", "Llama 4", "Llama 3", "Muse Spark"]
source_lang: en
---

# Llama（Meta）— Meta AIのオープンソースLLMファミリ

> **言及数**: 8件（2026-04-18集計時点、継続増加中）
> **重要度**: 高 — 世界最大のオープンソースLLMエコシステム
> **関連**: [[open-source-death]], [[deepseek]], [[qwen]]

## 概要

**Llama**（Large Language Model Meta AI）は、[[meta]]（Meta Platforms, Inc.）が開発する大規模言語モデル（LLM）ファミリ。2023年2月の初版リリース以来、オープンウェイトモデルのデファクトスタンダードとして、世界中の開発者・研究コミュニティに影響を与えている。2026年4月現在、後継モデル**Muse Spark**がリリースされている。

## モデル進化史

| バージョン | リリース | パラメータ | コンテキスト | 特徴 |
|-----------|---------|-----------|-------------|------|
| **LLaMA 1** | 2023年2月 | 7B〜65B | 2,048 tokens | 研究目的限定、非商用 |
| **Llama 2** | 2023年7月 | 7B, 13B, 70B | 4,096 tokens | 商用利用可能、RLHF導入 |
| **Llama 3** | 2024年4月 | 8B, 70B | 8,192 tokens | 30言語対応、CyberSecEval導入 |
| **Llama 3.1** | 2024年7月 | 8B, 70B, **405B** | 128K tokens | 初の超大規模モデル、IBM watsonx連携 |
| **Llama 3.3** | 2024年末 | 70B | — | 最適化版 |
| **Llama 4 Scout** | 2025年4月 | 109B（MoE, アクティブ17B） | 10M tokens | 初のネイティブマルチモーダル |
| **Llama 4 Maverick** | 2025年4月 | 不明 | — | Llama 4シリーズのフル版 |
| **Muse Spark** | 2026年4月 | — | — | Llamaの後継モデル（Meta Superintelligence Labs） |

## Llama 4の特徴（2025年4月）

### Scoutモデル
- **MoEアーキテクチャ**: 総パラメータ109B、アクティブ17B/トークン
- **16エキスパート**: 効率的な推論処理
- **10Mトークンコンテキスト**: 超長文処理が可能
- **シングルH100で動作**: 高い効率性
- **ネイティブマルチモーダル**: テキスト+画像の統合処理

### Maverickモデル
- Scoutの上位版
- クラス最高のマルチモーダル性能
- 単一GPUでの効率運用を重視

## オープンソース戦略とライセンス

### Llama 2以降のライセンス変更
- **Llama 2**: 研究・商用利用可能（超大規模サービスに制限あり）
- **Llama 3**: さらに緩和されたライセンス
- **Llama 4**: Community License Agreement + Acceptable Use Policy
  - ソースはアクセス可能だが、真のオープンソース（OSI定義）ではない
  - 利用制限条項が含まれる

> **注意**: Llama 4のライセンスは「source-available」であり、厳密にはオープンソースではない。[[open-source-death]]の文脈で議論されるケースの一つ。

## 中国エコシステムでのLlama

### Llama派生モデルの活用
中国の開発者コミュニティでは、Llamaをベースとした派生モデルが広く活用されている：

- **DeepSeek-R1**: Llamaアーキテクチャをベースにした推論特化モデル
  - 671Bパラメータ（MoE）、164Kコンテキスト
  - OpenAI-o1相当の性能をオープンウェイトで提供
  - MITライセンス（商用利用可能）

- **Qwen3**: 阿里雲系のLlama派生モデル
  - 235B総パラメータ（アクティブ22B）
  - 思考モード/非思考モードの切り替え機能
  - 100言語以上対応

### 「Llamaエコシステム」の意義
Metaのオープンウェイト戦略により：
1. 中国企業が最先端LLMアーキテクチャにアクセス可能
2. 制裁下でもモデル開発のベースラインを維持
3. コミュニティ全体で改善・最適化が進行

## Muse Sparkへの移行（2026年4月）

2026年4月、Meta Superintelligence Labsは**Muse Spark**をLlamaの後継としてリリースした。これにより：
- Llamaブランドは事実上の終焉
- 新しいライセンス体系の導入が予想される
- オープンウェイト戦略の継続性に注目が集まる

## ベンチマーク性能

### 主要ベンチマーク（Llama 3.1 405B時点）
- **MMLU**: 最先端レベル
- **GSM8K**: 数学的問題解決で高評価
- **HumanEval**: コーディング能力で競争力
- **CyberSecEval**: セキュリティ耐性の独自評価

### Llama 4 vs 競合
| モデル | 開発元 | 備考 |
|--------|--------|------|
| Llama 4 Scout | Meta | MoE 109B、効率重視 |
| GPT-OSS-120B | OpenAI | MoE 120B、Apache 2.0 |
| Qwen3-235B | 阿里雲 | MoE 235B、多言語 |
| DeepSeek-R1 | DeepSeek | MoE 671B、推論特化 |

## 関連リンク

### 内部リンク
- [[open-source-death]] — オープンソースLLMの商業化とライセンス問題
- [[deepseek]] — Llama派生モデルの代表格
- [[qwen]] — 阿里雲系のLlama派生
- [[claude-opus-4-7]] — 競合クローズドモデル
- [[meta]] — Meta Platforms, Inc.

### 外部ソース
| ソース | URL | ティア | 概要 |
|---|---|---|---|
| Meta AI Blog | [ai.meta.com/blog/llama-4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) | T1 | Llama 4公式発表 |
| Wikipedia | [en.wikipedia.org/wiki/Llama_(language_model)](https://en.wikipedia.org/wiki/Llama_(language_model)) | T1 | Llamaの歴史 |
| SiliconFlow | [siliconflow.com](https://www.siliconflow.com/articles/zh-Hant/the-best-meta-llama-models-in-2025) | T2 | 2026年ベストLlamaモデル比較 |
| GPT-trainer | [gpt-trainer.com](https://gpt-trainer.com/blog/llama+4+evolution+features+comparison) | T2 | Llama 4進化解説 |
