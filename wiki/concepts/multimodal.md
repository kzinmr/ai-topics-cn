---
title: "多模态/Multimodal — 複数のモダリティを統合するAI"
created: 2026-04-24
updated: 2026-04-24
tags: [concept, multimodal, vision, audio, image-generation, video-generation]
aliases: ["多模态", "multimodal", "多模态大模型", "多模态理解", "多模态生成", "audio", "video-generation", "image-generation", "vision"]
source_lang: zh-CN
---

# 多模态/Multimodal — 複数のモダリティを統合するAI

## 概要

多模态（Multimodal）AIは、**テキスト・画像・音声・動画・3D**など複数のモダリティ（情報形式）を統合して理解・生成するAI技術。2026年4月時点では、**画像生成から動画生成まで**、多模态AIが急速に進化している。

> **トレンド順位**: #5（2026-04-10〜24集計、**44言及**）⬆️
> **ソース**: 36kr, 掘金, WeChat（全3ソース）
> **重要度**: 高 — 画像生成・動画生成が主要議論

## 多模态AIの進化

### モダリティの統合

| モダリティ | 対応 | 代表モデル |
|-----------|------|-----------|
| テキスト | NLP、LLM | GPT-5、Qwen3.5 |
| 画像 | 画像理解・生成 | GPT-4o、GPT Image 2.0 |
| 音声 | 音声認識・合成 | GPT-4o Audio |
| 動画 | 動画生成・理解 | Kling、Sora |
| 3D | 3Dモデル生成 | Luma、Sora 3D |
| データ | チャート分析 | GPT-4o Data |

### GPT-4o — Omni（多模态原生）

OpenAIのGPT-4oは**「o」= Omni**（全モダリティ）を象徴するモデル。テキスト・画像・音声の入出力を**統一アーキテクチャ**で実現。

> **出典**: 36kr（机器之心）— [ChatGPT Images 2.0震撼发布](https://36kr.com/p/3777060252780800) [T1]

## 画像生成（Image Generation）

### GPT Image 2.0

OpenAIの**GPT Image 2.0**は2026年4月にChatGPTに統合された画像生成モデル。

- **GPT-5の生図能力**: GPT-5時代の画像生成がChatGPTで利用可能に
- **Nano Bananaとの比較**: GoogleのNano Bananaを凌駕する性能
- **大米刻字機能**: 写真に文字を刻む高品質なエッチング
- **デザイナー業界への影響**: 「设计真要完了」との声

> **出典**: 36kr — [ChatGPT Images 2.0震撼发布](https://36kr.com/p/3777060252780800) [T1]
> **出典**: 36kr — [奥特曼亲自上阵，Images 2.0登顶王座](https://36kr.com/p/3777221631150343) [T1]

### Google Nano Banana

Googleの画像生成モデル**Nano Banana**がGPT Image 2.0と比較されている。

> **出典**: 36kr — [ChatGPT Images 2.0震撼发布](https://36kr.com/p/3777060252780800) [T1]

### Qwen3.5 VL（Vision Language）

AlibabaのQwen3.5シリーズには**VL（Vision Language）**バージョンがあり、画像理解・生成に対応。

> **出典**: 36kr — [Qwen3.5: 通义千问2026年最强AI](https://36kr.com/p/3770898401608068) [T1]

## 動画生成（Video Generation）

### Sora — OpenAIの動画生成

OpenAIの**Sora**はテキストから動画を生成するモデル。

> **出典**: V2EX — [Sora情報](https://www.v2ex.com/t/1206471) [T1]

### Kling — 快手の動画生成

快手（Kuaishou）の動画生成モデル**Kling**は中国コミュニティで注目。

> **出典**: 36kr — [Kling: 快手2026年最强视频生成模型](https://36kr.com/p/3772736600571392) [T1]

### Sora 3D — 3D動画生成

> **出典**: V2EX — [Sora 3D](https://www.v2ex.com/t/1206523) [T1]

### Sora vs Sora 2 — 動画生成の進化

> **出典**: 36kr — [Sora vs Sora 2](https://36kr.com/p/3772009673836290) [T1]

## 多模态理解（Multimodal Understanding）

### GPT-4oの多模态理解

GPT-4oは画像・音声・テキストを**リアルタイム**で同時に理解。

### GPT Codexの多模态コンテキスト

GPT Codexは**スクリーンショットの添付**をネイティブにサポート。

> **出典**: 36kr — [OpenAI彻底重构Codex](https://36kr.com/p/3770202199323136) [T1]

### 音频理解（Audio Understanding）

> **出典**: 36kr — [音频理解](https://36kr.com/p/3776293841008770) [T1]

## 中国AIコミュニティの多模态議論

### Qwen3.5 VL

> **出典**: 36kr — [Qwen3.5: 通义千问2026年最强AI](https://36kr.com/p/3770898401608068) [T1]
> **出典**: V2EX — [Qwen VL](https://www.v2ex.com/t/1206476) [T1]

### 多模态AIの産業応用

> **出典**: 36kr — [多模态AI](https://36kr.com/p/3773142580475778) [T1]
> **出典**: 掘金 — [多模态AI](https://www.juejin.cn/post/7602710927546552330) [T1]

## 多模态技術の進化

### アーキテクチャ進化

| アーキテクチャ | 特徴 | 代表 |
|---------------|------|------|
| 単一モダリティ | テキストのみ | GPT-3 |
| マルチタスク | 単一アーキテクチャで複数モダリティ | GPT-4o |
| ネイティブ多模态 | 各モダリティをネイティブに統合 | GPT-5.5 |

### 生成技術

- **Diffusion**: 画像生成の主流（Stable Diffusion、DALL-E）
- **Flow Matching**: より効率的な生成
- **Autoregressive**: テキスト生成モデルの画像拡張
- **Video Diffusion**: 動画生成（Sora、Kling）

## 関連エンティティ

| エンティティ | 関係性 |
|-------------|--------|
| [[openai]] | GPT-4o、GPT Image 2.0、Soraの開発元 |
| [[google]] | Gemini、Nano Bananaの開発元 |
| [[qwen]] | Qwen VLのQwen3.5 VL |
| [[deepseek]] | DeepSeekの多模态対応 |
| [[kimi-moonshot]] | Kimiの多模态対応 |

## 多模态 vs テキストLLM

| 次元 | テキストLLM | 多模态AI |
|------|-----------|---------|
| 入力 | テキスト | テキスト＋画像＋音声＋動画 |
| 出力 | テキスト | テキスト＋画像＋音声＋動画 |
| アーキテクチャ | デコーダのみ | 統一アーキテクチャ |
| 応用 | 文章生成、分析 | 画像生成、動画生成、デザイン |
| 計算量 | 相対的に低い | 相対的に高い |

## 関連概念

- [[gpt]] — GPTシリーズの多模态進化
- [[openai]] — GPT-4o、GPT Image 2.0の開発元
- [[claude-opus-4-7]] — Claudeの多模态対応
- [[function-calling]] — 多模态AIの外部ツール連携
- [[multi-agent|AI Agent]] — 多模态エージェント

## ソース信頼性

| ソース | Tier | 信頼度 |
|--------|------|--------|
| 36kr | T1 | ○ 業界ニュース |
| V2EX | T1 | ○ 実務者の議論 |
