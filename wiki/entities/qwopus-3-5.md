---
title: "Qwopus 3.5 — Qwen3.5-27Bベース社区微调モデル"
created: 2026-04-22
updated: 2026-04-22
tags: [llm, model, china, open-source-ai, qwen, reasoning]
aliases: ["Qwopus", "Qwopus3.5", "qwopus"]
source_lang: zh-CN
---

# Qwopus 3.5 — Qwen3.5-27Bベース社区微调モデル

> **トレンド順位**: #20+（2026-04-22集計、低言及）
> **ソース**: Juejin
> **重要度**: 中 — 社区驱动のReasoning SFT実験

## 概要

**Qwopus3.5**は、開発者**Jackrong (JIRONG)**が公开发表したオープンソース大语言モデルシリーズ。名称は「**Qwen + Opus**」に由来し阿里の`Qwen3.5-27B`を基底部モデルとして、OpenAIの`o3-mini`や`Opus 4.7`のReasoning手法を取り込んだ独自の训练プロセスは「**Reasoning SFT**」と呼称されている。

27Bパラメータ規模で「**Reasoning SFT 释放推理潜力**」（思考する力を解放）という定位。社区（オープンソースコミュニティ）発のまま人气が急上昇しており、Juejinで技术解説記事が始まっている。

## 技术的特徴

### Reasoning SFTアプローチ

従来のSFT（Supervised Fine-Tuning）と异なり、**Reasoning SFT**は：

- 思考过程（Chain-of-Thought）の生成方法を訓練
- 「thinking budget」（思考量制御）を調整可能に
- 27B规模でも大きなモデルに匹敵する推論能力を実現

### 性能評価

Juejin记事では「**Qwopus3.5 — 用 Reasoning SFT 释放 27B 模型的推理潜力**」として：

- OpenAI o3-mini比较で竞争力ある结果
- Qwen3.5-27B基底部比で明显的な推理向上
- 社区驱动的開発・改善サイクル

> 「基底部は阿里のQwen3.5-27B、训练目標はOpenAIのOpusから思考パターンを抽出」
> — Juejin、2026-04-22

## 関連リンク

- [[qwen]] — 基底部モデル（Qwen3.5-27B）
- [[openai]] — 目标としたOpusモデル