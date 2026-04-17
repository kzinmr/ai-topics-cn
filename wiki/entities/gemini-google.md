---
title: "Gemini/Google — Google AI基盤モデルとオープンソースGemma"
created: 2026-04-17
updated: 2026-04-17
tags: [llm, model, google, gemini, gemma, inference, open-source-ai]
aliases: ["Gemini", "Google AI", "Gemma"]
source_lang: zh-CN
---

# Gemini/Google — Google AI基盤モデルとオープンソースGemma

## 概要

Geminiは[[openai|OpenAI]]のGPTシリーズ、[[anthropic|Anthropic]]のClaudeと並ぶGoogle DeepMindの主力AIモデルファミリー。中国語圏ではGemini Pro/Ultraのマルチモーダル能力と、オープンソースのGemmaシリーズ（特にGemma 4）が注目を集めている。

> **トレンド順位**: #6（2026-04-17集計、33言及）
> **ソース**: 36kr, juejin, v2ex（全3ソースタイプで言及）

## 最新動向（2026年4月）

### Gemma 4 31B — オープンソース新星
- **Gemma 4 31B**がリリースされ、最大256Kコンテキストをサポート
- 能力面でQwen3.5 397Bに匹敵するとの評価（掘金 教程記事）
- 中国語圏ではワンクリックデプロイガイドが人気
- Source: [教程上新丨一键部署Gemma 4 31B](https://juejin.cn/post/7629524163644981311) (T1: juejin)

### Transformer×RNN ハイブリッドアーキテクチャ
- Googleが**Transformer+RNNの融合**アーキテクチャを発表
- VRAMのボトルネックを打破し、超長コンテキストを解放
- RNNに「成長可能な記憶（可生长记忆）」メカニズムを導入
- 機器之心が速報・解説を展開
- Source: [Transformer与RNN合体](https://36kr.com/p/3770765015991049) (T2: 机器之心 via 36kr)

### Gemini「降智」問題
- V2EXで「GeminiとGoogleのAIモードが深刻に劣化」との報告が相次ぐ
- Gemini Proの性能低下を指摘するユーザーが増加
- Google AI Studioが課金モデルへの移行を開始（「aistudio 也要开始收费了？」）
- Source: [现在 Google 的 Gemini 和 AI 模式降智的厉害啊](https://www.v2ex.com/t/1206722) (T1: v2ex)

### 闲鱼での低価格アカウント問題
- 闲鱼（中国フリマ）で低価格Gemini Proアカウントが出回り、アカウント乗っ取り被害が発生
- 中国国内での「詐欺コストゼロ」問題が顕在化
- Source: [买了咸鱼低价 Gemini pro 账号差点被盗](https://www.v2ex.com/t/1206537) (T1: v2ex)

### 神秘モデルの出現
- Gemma 4 31Bを超えるランキングの神秘モデルが出現
- Qwenとは正面対決を避け、「速さ」と「トークン節約」を差別化ポイントに
- Source: [神秘模型排名超 Gemma 4 31B](https://36kr.com/p/3770448836870663) (T1: 36kr)

## 中国語圏での位置づけ

| 観点 | 状況 |
|------|------|
| 人気度 | #6トレンド（33言及）、3ソース横断 |
| 競合 | [[claude-opus-4-7]]、GPT-5.4、[[qwen]] |
| 強み | マルチモーダル、Gemmaオープンソース、超長コンテキスト研究 |
| 弱み | 中国からのアクセス制限、「降智」への不満、API安定性 |
| 代替需要 | Gemma → 中国国内デプロイ需要（[[qwen]]・[[glm-zhipu]]と競合） |

## 関連ページ

- [[openai]] — GPTシリーズとの直接競合
- [[anthropic]] — Claudeとの比較
- [[qwen]] — Gemma 4の比較対象として頻出
- [[glm-zhipu]] — 中国オープンソースモデル比較
- [[ai-agent]] — Geminiベースのエージェント構築
- [[vector-db]] — Gemini Embeddingとの連携

## ソース信頼性

| ソース | Tier | 信頼度 |
|--------|------|--------|
| 36kr（机器之心経由） | T2 | ◎ 高品質な技術解説 |
| V2EX | T1 | ○ ユーザー体験レポート |
| 掘金 | T1 | ○ 実装チュートリアル |
