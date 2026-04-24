---
title: "微调/Fine-tuning — 大規模モデルの特定ドメイン適応"
created: 2026-04-24
updated: 2026-04-24
tags: [concept, fine-tuning, training, peft, lora, qlora, trl, axolotl, unsloth, grpo-rl-training]
aliases: ["微调", "fine-tuning", "模型微调", "LoRA", "QLoRA", "PEFT", "全量微调", "参数高效微调", "低秩适配"]
source_lang: zh-CN
---

# 微调/Fine-tuning — 大規模モデルの特定ドメイン適応

## 概要

**微调（Fine-tuning）**は、事前学習済みLLMを特定のドメインやタスクに合わせて追加学習する技術。2026年4月時点では、**LoRA/QLoRA**が主流の低コスト微调手法として定着し、中国AIコミュニティで広く活用されている。

> **トレンド順位**: #4（2026-04-10〜24集計、**59言及**）⬇️
> **ソース**: 36kr, 掘金, V2EX（全3ソース）
> **重要度**: 高 — 中国モデルの専門化・最適化の基盤技術

## 微调の基本概念

### 微调 vs 学習 vs 推論

| 段階 | 目的 | データ | 計算量 |
|------|------|--------|--------|
| **学習（Pre-training）** | 基盤知識の獲得 | 全インターネットスコープ | 極めて高い |
| **对齐（Alignment）** | 人間との対話適応 | 人間のフィードバック | 高い |
| **微调（Fine-tuning）** | 特定ドメイン適応 | ドメイン特化データ | 中 |
| **推論（Inference）** | 実際の使用 | なし（テストデータのみ） | 低い |

### 微调のタイプ

| タイプ | 説明 | コスト | 用途 |
|--------|------|--------|------|
| **全量微调** | 全パラメータを調整 | 高い | ドメイン特化 |
| **LoRA/QLoRA** | 低ランクアダプタ | **低い** | **主流** |
| **Prefix-tuning** | プレフィックスベクトル | 低 | タスク特化 |
| **P-tuning** | プロンプト最適化 | 最低 | シンプルタスク |

## LoRA（Low-Rank Adaptation）

### LoRAの原理

LoRAは、重み更新を**低ランク行列**の積として表現するPEFT手法。

- **低コスト**: 全パラメータの0.1%〜1%のみを学習
- **高速**: GPUメモリ要件が大幅に削減
- **交換可能**: 異なるタスクのLoRAアダプタを簡単に切り替え

### QLoRA（Quantized LoRA）

QLoRAは**量化済みモデル**にLoRAを適用する手法。

- **4-bit量化 + LoRA**: さらにメモリを節約
- **ノートPCでも可能**: 16GB VRAMで70BモデルのLoRA微调
- **中国コミュニティ**: QLoRA微调が最も人気のある微调手法

## 主要な微调ツール

### Axolotl

Axolotlは**YAMLベース**の微调フレームワーク。

- **宣言型設定**: YAMLで微调設定を記述
- **多モデル対応**: Qwen、Llama、Mistralなど対応モデルが多い
- **中国モデル**: Qwen3.5などの中国モデルにも対応

> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]

### Unsloth

Unslothは**2〜5倍的高速**な微调フレームワーク。

- **速度向上**: 2〜5倍の微调速度
- **メモリ削減**: メモリ使用量が半分以下
- **PyTorchベース**: 既存のPyTorchコードと互換

> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]

### TRL（Transformer Reinforcement Learning）

TRLはHugging Face提供の**RLHF/DPO/GRPO**微调フレームワーク。

- **RLHF**: 人間のフィードバックによる強化学習
- **DPO**: Direct Preference Optimization — 簡易对齐
- **GRPO**: Group Relative Policy Optimization — 新对齐手法

## GRPO/RL微调

### GRPO（Group Relative Policy Optimization）

GRPOは**Group Relative**の最適化手法。

- **RLHFの進化**: 従来のRLHFを改善
- **複数ポリシー比較**: グループ内で相対的なポリシー比較
- **中国モデル**: Qwen、DeepSeekのGRPO微调が議論されている

> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]

### DPO（Direct Preference Optimization）

DPOは**RLHFを簡略化**する对齐手法。

- **RL不要**: 従来のRLHFの複雑さを排除
- **シンプル**: 直接的な最適化
- **中国モデル**: Qwen、Yiなどの中国モデルでDPO微调

## 中国AIコミュニティでの微调議論

### Qwen3.5の微调

> **出典**: 36kr — [Qwen3.5: 通义千问2026年最强AI](https://36kr.com/p/3770898401608068) [T1]
> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]

### Qwen3.5のGRPO微调

> **出典**: 36kr — [Qwen3.5: 通义千问2026年最强AI](https://36kr.com/p/3770898401608068) [T1]

### 微调の産業応用

> **出典**: 36kr — [微调](https://36kr.com/p/3772698836912642) [T1]
> **出典**: V2EX — [微调](https://www.v2ex.com/t/1206531) [T1]

## 微调の技術的特徴

### データ準備

- **SFTデータ**: Supervised Fine-Tuning用の指示データ
- **对齐データ**: RLHF/DPO用のペアデータ
- **ドメインデータ**: 特定ドメインのテキストデータ

### 学習ハイパーパラメータ

| パラメータ | 典型的値 | 影響 |
|-----------|---------|------|
| Learning Rate | 1e-5 〜 5e-5 | 学習速度 |
| Batch Size | 16〜64 | 安定性 |
| Epochs | 1〜3 | 過学習防止 |
| LoRA Rank (r) | 8〜64 | 表現力 |
| LoRA Alpha | 16〜128 | スケール |

## 微调 vs RLHF/对齐

| 次元 | 微调（Fine-tuning） | RLHF/对齐 |
|------|---------------------|-----------|
| 目的 | ドメイン適応 | 人間との対話適応 |
| データ | ドメイン特化指示データ | 人間の好み/フィードバック |
| 手法 | LoRA、全量微调 | RLHF、DPO、GRPO |
| 計算量 | 中 | 高い（特にRLHF） |
| 出力 | 特定ドメインの応答 | 安全・有用な応答 |

> **注**: RLHF/对齐も广义の微调に含まれる。

## 関連エンティティ

| エンティティ | 関係性 |
|-------------|--------|
| [[qwen]] | Qwen3.5 — 中国モデルの微调が主流 |
| [[deepseek]] | DeepSeek — GRPO微调の議論 |
| [[y]] | Yi — DPO微调の議論 |

## 関連概念

- [[peft-fine-tuning]] — PEFTのLoRA/QLoRA
- [[fine-tuning-with-trl]] — TRLのRLHF/DPO
- [[grpo-rl-training]] — GRPO/RL微调の詳細
- [[axolotl]] — Axolotl YAML微调設定
- [[unsloth]] — Unsloth的高速微调
- [[pytorch-fsdp]] — FSDP分散微调
- [[huggingface-hub]] — Hugging Face Hubの微调モデル配布

## ソース信頼性

| ソース | Tier | 信頼度 |
|--------|------|--------|
| 36kr | T1 | ○ 業界ニュース |
| 掘金 | T1 | ○ 技術解説 |
| V2EX | T1 | ○ 実務者の議論 |
