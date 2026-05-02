---
title: SenseNova-U1 — 商汤原生統一理解+生成MoTモデル
created: 2026-05-02
updated: 2026-05-02
tags: [model, multimodal, mot, mixture-of-thought, sensetime, open-source, transformer]
aliases: ["SenseNova-U1", "商汤SenseNova-U1", "SenseTime MoT"]
source_lang: zh-CN
---

# SenseNova-U1 — 商汤原生統一理解+生成MoTモデル

## 概要

商汤科技（SenseTime）がオープンソース化した**SenseNova-U1**は、「Thinking with Visual Primitives」路線をさらに推し進めた**Mixture of Thought (MoT)** アーキテクチャを採用したネイティブ統一理解・生成モデル。VAE不要、独立テキストエンコーダー不要という設計が特徴。

## 技術的特徴

### Mixture of Thought (MoT) アーキテクチャ

- **VAE不使用**: 従来のマルチモーダルモデルが依存していたVariational Autoencoderを排除
- **独立テキストエンコーダー不使用**: テキスト処理を統一モデル内に統合
- **原生統一**: 理解（理解）と生成（生成）を単一アーキテクチャで処理
- **Transformerベース**: SenseNova-U1はTransformer架构を採用

### OpenAI/DeepSeekとの路線比較

| 次元 | OpenAI GPT-5系 | DeepSeek V4-MoT | 商汤 SenseNova-U1 |
|------|---------------|-----------------|-------------------|
| アプローチ | Thinking with Images | Visual Primitives | Mixture of Thought |
| VAE | 使用 | 不使用 | 不使用 |
| テキストエンコーダー | 独立 | 独立 | 統合 |
| 可視性 | ブラックボックス | 中間視覚アンカー明示化 | 統一架构 |

> **出典**: V2EX — [商汤开源SenseNova-U1](https://www.v2ex.com/t/1209910) [T1]
> **出典**: 36kr — [DeepSeek多模态技术范式公布](https://36kr.com/p/3789208597372165) [T1]

## 関連リンク

### 内部リンク

- [[multimodal]] — マルチモーダルAIの文脈
- [[transformer]] — 基盤技術
- [[deepseek]] — Visual Primitives路線の先駆
- [[mixture-of-thought]] — MoTアーキテクチャの概念

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| V2EX — 商汤开源SenseNova-U1 | [v2ex.com/t/1209910](https://www.v2ex.com/t/1209910) | T2 | 技術仕様議論 |
| 36kr — DeepSeek多模态技术范式 | [36kr.com/p/3789208597372165](https://36kr.com/p/3789208597372165) | T1 | MoT文脈での言及 |
