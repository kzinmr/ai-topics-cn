---
title: "RLHF/对齐 — 人間のフィードバックによるLLMの対話最適化"
created: 2026-04-24
updated: 2026-04-24
tags: [concept, rlhf, alignment, dpo, grpo, safety, ethics, instruct-model, 对齐]
aliases: ["RLHF", "rlhf", "对齐", "alignment", "RLHF/DPO", "DPO", "GRPO", "human-feedback", "安全对齐", "instruct-model"]
source_lang: zh-CN
---

# RLHF/对齐 — 人間のフィードバックによるLLMの対話最適化

## 概要

**RLHF（Reinforcement Learning from Human Feedback）**と**对齐（Alignment）**は、LLMを人間の価値観・期待・安全基準に合わせて調整する技術。2026年4月時点では、**GRPO（Group Relative Policy Optimization）**と**DPO（Direct Preference Optimization）**が主流の对齐手法となっている。

> **トレンド順位**: #4（2026-04-10〜24集計、**59言及**）⬇️
> **ソース**: 36kr, 掘金（全2ソース）
> **重要度**: 高 — 中国モデルの安全对齐が主要議論

## RLHFの基本概念

### RLHFの3段階プロセス

| 段階 | 目的 | 技術 |
|------|------|------|
| **1. SFT** | 指示モデルの初期化 | 监督微调 |
| **2. Reward Model** | 人間の好みを学習 | 好みデータで学習 |
| **3. RL最適化** | Rewardを最大化 | PPO/RLOO/GRPO |

### 对齐（Alignment）の概念

对齐はRLHFを含む**広義の対話最適化**概念。

- **安全对齐**: 有害な出力を防止
- **価値对齐**: 人間の価値観に合わせた応答
- **有用性对齐**: 実用的な応答の生成

## 主要な对齐手法

### RLHF — 従来の手法

**PPO（Proximal Policy Optimization）**に基づくRLHF。

- **3つのモデル**: Policy、Reward、Critic
- **複雑**: 3つのモデルの同時学習が必要
- **安定性**: 訓練が不安定になりやすい

### DPO（Direct Preference Optimization）

DPOは**RLを省略**し、直接好みを最適化する。

- **2つのモデル**: PolicyとReferenceのみ
- **シンプル**: RLHFよりも訓練が安定
- **中国モデル**: Qwen、Yiなどの中国モデルでDPO微调

> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]

### GRPO（Group Relative Policy Optimization）

GRPOは**Group Relative**の最適化手法。

- **複数ポリシー比較**: グループ内で相対的なポリシー比較
- **Reward Model不要**: 従来のRLHFよりシンプル
- **中国モデル**: Qwen3.5のGRPO微调が議論されている

> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]

## 中国AIコミュニティでの对齐議論

### Qwen3.5のGRPO对齐

> **出典**: 36kr — [Qwen3.5: 通义千问2026年最强AI](https://36kr.com/p/3770898401608068) [T1]
> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]

### 对齐の安全性

> **出典**: 36kr — [对齐](https://36kr.com/p/3775665553782274) [T1]

## 对齐の技術的特徴

### 好みデータ（Preference Data）

对齐の核となる**ペアデータ**。

- **ペア構造**: （良い応答、悪い応答）のペア
- **収集方法**: 人間のラベリング、LLM生成、実使用データ
- **規模**: 数万〜数百万のペア

### Reward Model

人間の好みを学習する**評価モデル**。

- **スコアリング**: 各応答にスコアを付与
- **比較**: 応答間の相対的な優先度を学習
- **中国モデル**: Qwen、DeepSeekのReward Model

## 对齐 vs 学習 vs 微调

| 段階 | 目的 | データ | 手法 |
|------|------|--------|------|
| 学習（Pre-training） | 基盤知識 | 全インターネット | 自己教師あり |
| 对齐（Alignment） | 人間の価値観 | 好みデータ | RLHF/DPO/GRPO |
| 微调（Fine-tuning） | ドメイン適応 | 指示データ | LoRA/SFT |

> **注**: 对齐も广义の微调に含まれる。

## 安全对齐（Safety Alignment）

### 有害出力の防止

- **プロンプトインジェクション**: 悪意あるプロンプトからの保護
- **有害コンテンツ**: 暴力・差別・違法コンテンツの生成防止
- **プライバシー**: 個人情報保護

### 中国の对齐規制

- **生成式AI規制**: 中国の生成式AIサービス管理弁法
- **对齐要求**: 中国モデルの安全对齐が法的に義務付け
- **审查**: 中国モデルの输出审查

## 関連エンティティ

| エンティティ | 関係性 |
|-------------|--------|
| [[qwen]] | Qwen3.5 — GRPO对齐の議論 |
| [[deepseek]] | DeepSeek — 对齐手法の議論 |
| [[y]] | Yi — DPO微调の議論 |
| [[openai]] | OpenAI — ChatGPTのRLHF对齐 |

## 関連概念

- [[fine-tuning-with-trl]] — TRLのRLHF/DPO/GRPO実装
- [[grpo-rl-training]] — GRPO/RL微调の詳細
- [[peft-fine-tuning]] — PEFTのLoRA/QLoRA
- [[evaluating-llms-harness]] — LLM評価ハーンレス
- [[unsloth]] — Unslothの高速对齐

## ソース信頼性

| ソース | Tier | 信頼度 |
|--------|------|--------|
| 36kr | T1 | ○ 業界ニュース |
| 掘金 | T1 | ○ 技術解説 |
