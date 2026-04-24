---
title: "GPT — OpenAIの言語モデルシリーズ"
created: 2026-04-24
updated: 2026-04-24
tags: [concept, model, llm, gpt, openai, chatgpt]
aliases: ["GPT", "gpt", "ChatGPT", "chatgpt", "GPT-5", "GPT-5.5", "GPT-4", "GPT-4o", "GPT-3.5", "GPT Image"]
source_lang: zh-CN
---

# GPT — OpenAIの言語モデルシリーズ

## 概要

GPT（Generative Pre-trained Transformer）はOpenAIが開発する大規模言語モデルのシリーズ。GPT-3（2020）から始まり、GPT-3.5（ChatGPT基盤）、GPT-4、GPT-4o、GPT-4.5、GPT-5と進化を続けている。2026年4月時点では**GPT-5.5が内部テスト中に漏洩**し、中国AIコミュニティで大きな話題となっている。

> **トレンド順位**: #3（2026-04-10〜24集計、**74言及**）⬆️
> **ソース**: 36kr, Juejin, V2EX, WeChat（全4ソース）
> **重要度**: 極めて高 — 中国語圏AIディスコースで最も言及されるエンティティの一つ

## 沿革とバージョン

### GPTシリーズの進化

| バージョン | リリース | 特徴 |
|-----------|---------|------|
| **GPT-3** | 2020年 | 1750億パラメータ、few-shot学習の先駆者 |
| **GPT-3.5** | 2022年 | ChatGPTの基盤。実用化でAI民主化を推進 |
| **GPT-4** | 2023年 | 推論能力・多模態（画像入力）を追加 |
| **GPT-4o** | 2024年 | Omni（多模態原生）。「o」はomniの略 |
| **GPT-4.5** | 2026年 | 推論特化モデル。GPT-5の技術検証 |
| **GPT-5** | 2026年（推定） | 次の次世代フラグシップ |
| **GPT-5.5** | 2026年4月（漏洩） | Codex内部テスト環境からリーク |

### GPT-5.5漏洩事件（2026-04-23）

Codexプラットフォームの内部テスト環境が誤って生産環境に公開され、**GPT-5.5**、「**风速狗**（Arcanine）」、「**海森堡**」、そして神秘な「**Glacier**」が同時に公開された。

> **出典**: 36kr（新智元）— [GPT-5.5，刚刚泄露了](https://36kr.com/p/3779080911049986) [T1]

OpenAIのSam Altmanが以前「Transformerよりも偉大なアーキテクチャ」について言及していたことから、GPT-5.5がその新アーキテクチャを実装している可能性が議論されている。

## ChatGPT Images 2.0（2026-04）

OpenAIは**ChatGPT Images 2.0**をリリースし、中国AIコミュニティで大きな反響を呼んだ。

- **GPT-5の生図能力**: GPT-5時代の画像生成がChatGPTに統合
- **Nano Bananaとの比較**: GoogleのNano Bananaを凌駕する性能と評価
- **デザイナー業界への影響**: 「设计真要完了」（デザイン業界が終わる）との声
- **大米刻字機能**: 写真に文字を刻む高品質なエッチング生成が可能

> **出典**: 36kr（机器之心）— [ChatGPT Images 2.0震撼发布](https://36kr.com/p/3777060252780800) [T1]
> **出典**: 36kr（新智元）— [奥特曼亲自上阵，Images 2.0登顶王座](https://36kr.com/p/3777221631150343) [T1]

## GPT-Proの「神级」進化（2026-04）

GPT Proが速度を**4倍**に向上させる「神级操作」でアップデートされ、中国ユーザーの間でGPT-5.5の早期登場説が浮上した。

> **出典**: 36kr（新智元）— [突然变强，速度翻4倍](https://36kr.com/p/3774954392519177) [T1]

## CodexとGPTの統合

OpenAIのCodex（Mac版「超级龙虾」）はGPTシリーズをネイティブに統合。GPT-5.4 HarnessがCodexに7つのサンドボックス環境として統合され、AIエージェントとしての自律性が大幅に向上した。

> **出典**: 36kr — [OpenAI彻底重构Codex](https://36kr.com/p/3770202199323136) [T1]
> **出典**: V2EX — [GPT Codex情報](https://www.v2ex.com/t/1206503) [T1]

## 中国コミュニティでのGPT議論

### 低価格サブスクリプション問題

中国コミュニティではGPTの低価格利用（「低价 GPT」）が長期間の話題となっている。

- **GPT Codexサブスクリプション脆弱性** — アングラで流通していた低価格サブスクリプションがOpenAI公式に露見
- **GPT Plus無料利用チュートリアル** — X（旧Twitter）から搬入された「白嫖 GPT Plus 教程」
- **Session 授权充值ツール** — クレジットカード決済問題に対する解決策共有
- **海鲜市场でのGPT Plus検索** — 中古市場でのGPT Plus取引方法の議論

> **出典**: V2EX — 複数スレッド [T1]

### GPT Image 2.0の生図性能

V2EXで「gpt-image-2 生图确实很顶啊」に代表されるように、GPT Image 2.0の生成品質が中国ユーザーから高く評価されている。

## GPTシリーズの技術的特徴

### Transformerアーキテクチャ

GPTは**逆Transformer**アーキテクチャ（デコーダのみ）を採用。自己注意機構により長文脈の理解と生成を可能にしている。GPT-5.5の漏洩で、「Transformerを超える新アーキテクチャ」への移行が注目されている。

### 推論能力の進化

- **Chain of Thought（CoT）**: GPT-4以降、推論プロセスを外部化
- **GPT-5推論特化**: 推論に特化したGPT-5がGPT-4oの推論能力を大幅に凌駕
- **GPT-5.4 Harness**: 7つの推論環境をCodexに統合

### 多模態統合

GPT-4o以降、画像・音声入力・出力をネイティブにサポート。GPT-5.5でさらに多模態能力が強化される見込み。

## 関連エンティティ

| エンティティ | 関係性 |
|-------------|--------|
| [[openai]] | OpenAI — GPTの開発元 |
| [[claude-opus-4-7]] | AnthropicのClaude Opus 4.7 — GPT-5の主要競合 |
| [[claude-code]] | Claude Code — GPT Codexの主要競合 |
| [[gemini-google]] | Gemini — GoogleのGPT競合 |
| [[qwen]] | Qwen（通义千问）— GPTの中国代替 |
| [[deepseek]] | DeepSeek — GPTの中国代替 |
| [[kimi-moonshot]] | Kimi — GPTの中国代替 |

## GPT vs 競合モデル比較

| 次元 | GPTシリーズ | [[claude-opus-4-7]] | [[gemini-google]] | [[qwen]] |
|------|------------|---------------------|-------------------|----------|
| フラグシップ | GPT-5.5（テスト中） | Claude Opus 4.7 | Gemini 2.5 Pro | Qwen3.5 |
| 推論 | GPT-5推論特化 | Claude Opus 4.7 | Gemini 2.5 Pro | Qwen3.5 reasoning |
| 多模态 | GPT-4o以降、GPT-5.5強化 | Claude 4以降 | Gemini原生多模态 | Qwen3.5原生多模态 |
| コーディング | GPT Codex | Claude Code | Gemini Code Assist | Qwen Code |
| 画像生成 | GPT Image 2.0 | Claude Artifacts | Imagen | Qwen VL |

## 中国語圏でのGPT関連トレンド（2026年4月）

| 日付 | 主要トピック |
|------|-------------|
| 04-15 | GPT-4o vs Claude Opus 4.6 コーディング比較 |
| 04-16 | ChatGPT Plus 低価格利用設定 |
| 04-17 | GPT Codexサブスクリプション脆弱性暴露 |
| 04-18 | GPT Image 2.0 vs Nano Banana 比較 |
| 04-20 | GPT Proが速度4倍に「神级」進化 |
| 04-21 | Codex多模态コンテキスト（スクリーンショット） |
| 04-22 | ChatGPT Images 2.0正式リリース |
| 04-23 | **GPT-5.5漏洩事件** — Arcanine, 海森堡, Glacier |

## 関連概念

- [[claude-code]] — Claude CodeのFunction Calling実装
- [[openai]] — GPT開発元のOpenAI企業ページ
- [[function-calling]] — GPTの外部API呼び出し機能
- [[multi-agent|AI Agent]] — GPTを活用したエージェント構築
- [[harness-engineering]] — GPT Harness Engineering
- [[mcp]] — GPTとMCP統合

## ソース信頼性

| ソース | Tier | 信頼度 |
|--------|------|--------|
| 36kr | T1 | ○ 業界ニュース |
| 掘金 | T1 | ○ 技術解説 |
| V2EX | T1 | ○ 実務者の議論 |
| WeChat | T2 | △ 媒体記事 |
