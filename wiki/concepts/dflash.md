---
title: "DFlash — ブロック拡散モデルによる高速予測デコーディング"
created: 2026-04-26
updated: 2026-04-26
tags: [inference, speculative-decoding, diffusion-model, optimization, parallel-decoding]
aliases: ["DFlash", "Block Diffusion", "予測デコーディング", "speculative decoding", "block diffusion"]
source_lang: en
---

# DFlash — ブロック拡散モデルによる高速予測デコーディング

> **重要度**: 🔥🔥🔥 CRITICAL — 推論速度の6倍加速を実現する革新的なspeculative decoding手法
> **関連概念**: [[speculative decoding]], [[vram-optimization]], [[quantization]], FlashAttention, [[in-context-learning]]
> **関連エンティティ**: [[qwen]], [[deepseek]], [[vllm]]

## 概要

**DFlash**はZ-Lab（ Jian Chen, Yesheng Liang, Zhijian Liu）によって開発された、**ブロック拡散モデル**を推論加速に活用する革新的なspeculative decodingフレームワーク。

従来の予測デコーディング（EAGLE-3等）がautoregressiveなdraftingに制限され、最大2-3倍の加速にとどまっていたのに対し、DFlashは**ブロックレベルの並列拡散**により、**Qwen3-8Bで最大6倍の無損失加速**を実現。EAGLE-3の約2.5倍速。

論文: [arxiv.org/abs/2602.06036](https://arxiv.org/abs/2602.06036)
GitHub: [z-lab/dflash](https://github.com/z-lab/dflash) (2,284+ ⭐)
モデル: [HuggingFace Z-Lab DFlash Collection](https://huggingface.co/collections/z-lab/dflash)

## 予測デコーディング — 基本原理

LLM推論は本質的に逐次的：各トークンは直前のトークンに依存する。予測デコーディングはこのボトルネックを解消する：

1. **小さなdraftモデル**が複数のトークンを提案
2. **大きなtargetモデル**がそれらを並列で検証
3. 検証通過トークンを出力、未通過トークンから再推論

**ボトルネック**: draftモデル自体が低速。EAGLE-3はautoregressiveにトークンを1つずつ生成するため、並列性が限られ、2-3倍加速が実質上限。

## DFlashの核心洞察：Target Knows Best

> 大規模autoregressive LLMの隠れ特徴量（hidden features）は、**複数の未来トークンに関する情報を暗黙に含む**（Samragh et al., 2025の観測）。

DFlashはこの洞察を活用：
- tinyなdiffusion draftモデルに「ゼロから推論」させるのではなく、**targetモデルの深層特徴量をコンテキストとして注入**
- targetモデルの**推論能力**とdiffusion modelの**並列生成速度**を融合

## アーキテクチャ詳細

### 1. Feature Fusion（特徴融合）

PrefillまたはVerification終了後：
- targetモデルの**均一にサンプリングされた複数の層**から隠れ特徴量を抽出
- 軽量なprojection layerで**cross-layer情報を融合** → コンパクトなtarget context featureに変換

### 2. KV Injection（KV注入）← **核心イノベーション**

- 融合した特徴量を**draftモデルの全層のKey/Value投影**に直接注入
- draftモデルのKVキャッシュに保存され、draftingイテレーション間で再利用
- **EAGLE-3との決定的差異**: EAGLE-3はtarget featuresを第一層の入力としてのみ注入 → 信号が層を重ねるごとに薄れる。DFlashは全層に注入 → 信号が維持され、acceptance lengthが深度に応じてスケール

### 3. Parallel Diffusion Drafting（並列拡散Drafting）

- 豊かなコンテキスト（+直前に検証済みのトークン）に条件付けられ、draftモデルが**単一フォワードパスでブロック全体を予測**
- ブロック内のすべてのマスク位置が**並列にデコード**
- autoregressive draftingの逐次コストがlinearに増加するのに対し、diffusion draftingのコストは**ほぼflat**（トークン数に依存しない）

### モデル構成

- **embeddingとLM head**: targetモデルから再利用（学習不要）
- **中間層のみ学習**: パラメータ数を最小限に維持
- **ブロック構築**: responseからanchorトークンをランダムサンプリング → anchorをブロックの第一位置とし、残りをmaskして並列予測
- **訓練アテンション**: 同じブロック内は双方向アテンション、異なるブロック間はアテンション禁止（Sparse Attention）

## パフォーマンス

### ベンチマーク

| モデル | 加速倍率 | 検証条件 |
|--------|---------|---------|
| Qwen3-8B | **6×** (lossless) | greedy decoding (temp=0) |
| Qwen3-4B (naive 5-layer) | ~3× | target conditioningなし |

### EAGLE-3との比較

| 指標 | EAGLE-3 | DFlash | 差異 |
|------|---------|--------|------|
| 方式 | autoregressive drafting | parallel diffusion drafting | 根本的差異 |
| アーキテクチャ | 1層のみ（低レイテンシ要請） | マルチ層（並列により可能） | デプス vs レイテンシ |
| target conditioning | 第一層のみ | 全層のKV注入 | 信号強度 |
| 最大加速 | 2-3× | 6× | **2.5倍向上** |
| 16トークン生成レイテンシ | 高（逐次） | 低（並列） | DFlashが有利 |

### 設計の深層理由

autoregressive draftersはトークンを1つずつ生成 → draftingコストがトークン数にlinearに増加 → レイテンシ低減のため極めて浅いアーキテクチャ（1層）に制約 → 品質が制限される。

diffusion draftersは全トークンを単一フォワードパスで生成 → draftingコストがflat → **深い表現力豊かなモデル**を使えてもレイテンシペナルティなし。DFlashで16トークン生成するマルチ層モデルは、EAGLE-3の8トークン生成する1層モデルより**レイテンシが低い**。

## 対応モデル一覧

| Target Model | DFlash Draft Model |
|-------------|-------------------|
| Qwen3.5-122B-A10B | z-lab/Qwen3.5-122B-A10B-DFlash |
| Qwen3.6-35B-A3B | z-lab/Qwen3.6-35B-A3B-DFlash |
| Qwen3.5-35B-A3B | z-lab/Qwen3.5-35B-A3B-DFlash |
| Qwen3.5-27B | z-lab/Qwen3.5-27B-DFlash |
| Qwen3.5-9B | z-lab/Qwen3.5-9B-DFlash |
| Qwen3.5-4B | z-lab/Qwen3.5-4B-DFlash |
| Qwen3-Coder-30B-A3B | z-lab/Qwen3-Coder-30B-A3B-DFlash |
| Qwen3-Coder-Next | z-lab/Qwen3-Coder-Next-DFlash |
| Qwen3-8B (non-thinking) | z-lab/Qwen3-8B-DFlash-b16 |
| Qwen3-4B (non-thinking) | z-lab/Qwen3-4B-DFlash-b16 |
| Kimi-K2.5 | z-lab/Kimi-K2.5-DFlash |
| LLaMA-3.1-8B-Instruct | z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat |
| gpt-oss-20b | z-lab/gpt-oss-20b-DFlash |
| gpt-oss-120b | z-lab/gpt-oss-120b-DFlash |

Coming soon: Qwen3.5-397B-A17B, GLM-5.1

## Inferenceバックエンド

### vLLM

```bash
vllm serve Qwen/Qwen3.5-27B \
  --speculative-config '{"method": "dflash", "model": "z-lab/Qwen3.5-27B-DFlash", "num_speculative_tokens": 15}' \
  --attention-backend flash_attn \
  --max-num-batched-tokens 32768
```

### SGLang

```bash
export SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1
python -m sglang.launch_server \
    --model-path Qwen/Qwen3.5-35B-A3B \
    --speculative-algorithm DFLASH \
    --speculative-draft-model-path z-lab/Qwen3.5-35B-A3B-DFlash \
    --speculative-num-draft-tokens 16 \
    --tp-size 1 \
    --attention-backend trtllm_mha \
    --speculative-draft-attention-backend fa4 \
    --mem-fraction-static 0.75 \
    --trust-remote-code
```

### Transformers

```python
from transformers import AutoModel, AutoModelForCausalLM, AutoTokenizer

draft = AutoModel.from_pretrained("z-lab/Qwen3-8B-DFlash-b16", trust_remote_code=True).eval()
target = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-8B").eval()
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-8B")

generate_ids = model.spec_generate(
    input_ids=model_inputs["input_ids"],
    max_new_tokens=2048,
    temperature=0.0,
    target=target,
)
```

### MLX

Apple Silicon対応。`pip install -e ".[mlx]"`でインストール。Apple M5 ProでQwen3/Qwen3.5モデルをテスト済み。

## DFlashの意義：Diffusion LLMの役割の再定義

> DFlashは、diffusion LLMsの役割を根本から再定義する。

- 大規模なdLLMをautoregressive qualityに追従させるのではなく、**diffusionをdraftingステージに限定**
- **並列性の inherent な利点を活用**し、autoregressive推論の加速にのみ集中
- target-model conditioningにより、**高いacceptance rate**を実現
- speculative verificationが**出力品質を保証**するため、diffusion modelの生成品質は重要ではない

このパラダイムシフトにより、**軽量なdiffusion adapter**のトレーニングにリソースを集中でき、実用的な推論加速を達成。

## 中国AIコミュニティでの文脈

- **Qwenチーム**: Qwen3.5/3.6/3-CoderシリーズのDFlash draftモデルをZ-Labと共同で公開
- **Moonshot/Kimi**: Kimi-K2.5のDFlash draftモデルも公開 — 中国発モデルの推論加速競争
- **gpt-oss**: OpenAIのgpt-oss 20B/120BのDFlash draftも利用可能 — 中国コミュニティでの活用可能性
- **SGLang vLLM**: 中国AIコミュニティでの主要推論フレームワークであるSGLangとvLLMの両方でサポート

## 課題と展望

1. **vLLM公式統合**: 現状はnightlyビルドのみ。公式リリース待ち
2. **トレーニングレシピ公開予定**: Z-Labはトレーニングレシピを近日公開予定 → カスタムDFlash draftを任意のLLM用に訓練可能に
3. **スライディングウィンドール**: 超長文コンテキスト/エージェントユースケースでexperimentalなsliding_window_sizeオプション提供
4. **モデル依存性**: 現在対応モデルは限定的（Qwen中心）。他のアーキテクチャ（Mistral、Yi等）への適用は未検証
5. **Thinkモデル対応**: Qwen3のthinkingモード非対応 — non-thinkingモデルのみ対応

## 関連技術との比較

| 手法 | 方式 | 最大加速 | target conditioning | 並列性 |
|------|------|---------|-------------------|--------|
| EAGLE-3 | autoregressive drafting | 2-3× | 第一層のみ | 低い |
| DiffuSpec | diffusion drafting | 不明 | なし | 高い |
| SpecDiff-2 | diffusion drafting | 不明 | なし | 高い |
| **DFlash** | **block diffusion** | **6×** | **全層KV注入** | **高い** |
