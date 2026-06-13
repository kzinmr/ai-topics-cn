---
title: "HiFloat4 — 華為Ascendチップ用4bit訓練フォーマット"
created: 2026-05-05
updated: 2026-05-05
tags: [huawei, ascend, quantization, training, low-precision, format, concept]
aliases: ["HiFloat4", "HiF4", "ハイフロート4"]
source_lang: zh-CN
---

# HiFloat4 — 華為Ascendチップ用4bit訓練フォーマット

> **重要度**: 高 — 輸出規制下の中国AIハードウェア効率化の重要トレンド
> **関連**: [[gpu-sanctions-china]], [[quantization]], [[vram-optimization]]

## 概要

HiFloat4（HiF4）は華為（Huawei）が自社Ascend NPU向けに開発した**4bit精度のAI訓練・推論用データフォーマット**である。Open Compute Project標準のMXFP4フォーマットとの比較検証で、HiFloat4が有意に優位な結果を示したことが2026年5月に報告された。

輸出規制によりNVIDIA H100などの先端GPUを大量入手できない中国企業にとって、**自社ハードウェアに最適化された低精度フォーマット**の開発は、計算効率を最大化する生存戦略となっている。HiFloat4はこの文脈で登場した重要な技術開発である。

## 技術的詳細

### 比較実験

華為研究チームは3種類のモデルでHiFloat4とMXFP4をBF16（16bit Brain Float）ベースラインに対して比較した：

| モデル | HiFloat4相対誤差 | MXFP4相対誤差 | 備考 |
|--------|-----------------|--------------|------|
| OpenPangu-1B | ≈1.0% | ≈1.5% | 華為自社モデル |
| Llama3-8B | <1% | ≈1.5% | オープンウェイト |
| Qwen3-MoE-30B | <1% | ≈1.5% | MoEアーキテクチャ |

### 安定化テクニックの差異

- **HiFloat4**: RHT（Random Hadamard Transform）のみでBF16損失の≈1%以内に到達
- **MXFP4**: RHT + 確率的丸め + トランケーションフリースケーリングの3つのテクニックを組み合わせ、ようやく≈1.5%に到達

モデルが大型化するほどHiFloat4の相対的優位性が拡大する傾向が確認された。

### アーキテクチャ的位置づけ

HiFloat4は華為の既存フォーマット**HiFloat8**（[[import-ai-454]]で言及）のさらに下位精度版である。4bitという極低精度でありながら、BF16フルプレシジョンに近い学習損失を達成できることが実証された。

## 地政学的文脈

### 輸出規制と効率化の相関

この開発は以下の構造的要因と密接に関連している：

1. **NVIDIA先端GPUの入手不可**: H100/A100などの高性能GPUが対中輸出制限の対象
2. **Ascend NPUへの依存**: 華為の自社AIアクセラレータ（昇騰910B/C等）が代替プラットフォームとして台頭
3. **効率最大化の圧力**: 同一チップでより多くの計算をこなすため、低精度フォーマットの開発が加速

> 「Our goal is to enable efficient FP4 LLM pretraining on specialized AI accelerators with strict power constraints. We focus on Huawei Ascend NPUs, which are domain-specific accelerators designed for deep learning workloads」
> — 華為研究チーム

### 中国チップメーカー全体のトレンド

HiFloat4の登場は、中国企業が**自社ハードウェアプラットフォームに明示的に結合した低精度データフォーマット**を独自開発する broader trend の一部である。この傾向は以下の理由で重要：

- **エコシステムの囲い込み**: 特定フォーマットが自社チップに最適化されることで、ソフトウェアスタックの独立性が高まる
- **CUDAモートへの対抗**: NVIDIA CUDAエコシステムに対抗する独自AIスタック構築の一環（[[gpu-sanctions-china]]のTileLang/Engramと同方向性）
- **効率競争**: 絶対的な計算力では劣っても、アルゴリズム・フォーマットレベルの最適化で追いつく戦略

## 関連研究

- **HiFloat4 Format for Language Model Pre-training on Ascend NPUs** (arXiv) — 原論文
- [[import-ai-454]] — Jack Clarkによる詳細分析と地政学的文脈
- [[gpu-sanctions-china]] — 中国AIチップ自立化の包括的文脈

## ソース

- [Import AI 454: Automating alignment research; safety study of a Chinese model; HiFloat4](https://importai.substack.com/p/import-ai-454) (2026-05-04)
- HiFloat4 Format for Language Model Pre-training on Ascend NPUs (arXiv)
