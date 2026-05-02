---
title: Mixture of Thought (MoT) — 次世代マルチモーダルAIアーキテクチャ
created: 2026-05-02
updated: 2026-05-02
tags: [concept, multimodal, architecture, mot, transformer, visual-reasoning]
aliases: ["MoT", "Mixture of Thought", "混合思考"]
source_lang: zh-CN
---

# Mixture of Thought (MoT) — 次世代マルチモーダルAIアーキテクチャ

## 概要

Mixture of Thought (MoT、混合思考) は、2026年4月〜5月にかけて中国AI業界で注目された新しいマルチモーダルAIアーキテクチャの概念。従来の「VAE + 独立テキストエンコーダー」のパイプラインを廃し、**理解と生成を単一モデル内で統一**するアプローチ。

## 技術的背景

### 従来のマルチモーダルパイプラインの課題

1. **VAE依存**: 画像を潜在空間に圧縮する過程で情報損失
2. **独立エンコーダー**: テキストと画像を別々に処理し、後で融合
3. **パイプラインの複雑さ**: 複数モデルの組み合わせによるメンテナンスコスト

### MoTのアプローチ

- **原生統一**: 単一Transformerアーキテクチャでテキスト・画像・推論を統合
- **VAE不要**: 直接的な視覚表現処理
- **独立テキストエンコーダー不要**: 統一モデル内の共有表現

## 主要実装

### DeepSeek "Thinking with Visual Primitives"

- 座標を「思考単位」として推論チェーンに嵌入
- 境界框（Bounding Box）と点座標を推論の基本単位とする
- 7056倍の視覚圧縮を実現
- → 詳細: [[deepseek]]

### 商汤 SenseNova-U1

- MoTアーキテクチャを採用した初のオープンソース統一モデル
- VAE不使用、独立テキストエンコーダー不使用
- 理解+生成を単一モデルで処理
- → 詳細: [[sense-nova-u1]]

## OpenAIとの路線比較

| 次元 | OpenAI | MoT (DeepSeek/商汤) |
|------|--------|---------------------|
| 思考方法 | Thinking with Images | Thinking with Visual Primitives / Mixture of Thought |
| 内部処理 | ブラックボックス | 中間視覚アンカー明示化 |
| アーキテクチャ | 複数モデル連携 | 単一統一モデル |
| 重点 | 汎用視覚ワークベンチ | 推論過程の透明化・検証可能性 |

## 業界への影響

- **Turing Award受賞者**による「AI Agent最終是數據庫問題」発言と並び、マルチモーダルAIの根本的アプローチの転換点として注目
- 中国発のアーキテクチャ革新が、OpenAI/Anthropic主導の路線に対抗する形で登場

> **出典**: V2EX — [商汤开源SenseNova-U1](https://www.v2ex.com/t/1209910) [T1]
> **出典**: 36kr — [DeepSeek多模态技术范式公布](https://36kr.com/p/3789208597372165) [T1]
> **出典**: 36kr — ["我可能不再建议学计算机"](https://36kr.com/p/3788895533095937) [T1]

## 関連リンク

### 内部リンク

- [[deepseek]] — MoT路線の先駆的実装
- [[sense-nova-u1]] — 商汤のMoT実装
- [[multimodal]] — マルチモーダルAIの文脈
- [[transformer]] — 基盤技術
- [[agent-database-problem]] — Turing Award受賞者の批判的視点
