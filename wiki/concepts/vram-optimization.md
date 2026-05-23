---
title: "显存优化（VRAM Optimization） — KVキャッシュ圧縮・量子化・推論効率化"
created: 2026-04-23
updated: 2026-05-23
tags: [inference, vram-optimization, kv-cache, quantization, optimization, china]
aliases: ["显存优化", "VRAM最適化", "KV Cache Compression", "PagedAttention", "KVキャッシュ圧縮"]
source_lang: zh-CN
---

# 显存优化（VRAM Optimization） — KVキャッシュ圧縮・量子化・推論効率化

> **重要度**: 🔥🔥 HIGH — 大規模モデルのローカル推論・クラウドデプロイメントの基盤技術
> **関連概念**: [[china-local-deployment]], [[pagedattention]], [[gguf-quantization]], [[speculative-decoding]], [[flash-attention]]
> **関連エンティティ**: [[vllm]], [[unsloth]]

## 概要

LLM推論におけるVRAM（显存）最適化は、中国AIコミュニティで最も関心の高い技術テーマの一つ。モデル重量の量子化に加え、**KVキャッシュのメモリ効率が推論スループットとコンテキスト長を決定**する。2026年春にはMIT・NVIDIA・浙江大学によるTriAttention等新手法が発表され、業界の関心をさらに高めている。

## 1. KVキャッシュ — 推論のボトルネック

### メモリ消費の内訳

推論におけるVRAM消費は以下の2要素に大別される：

```
VRAM総使用 = モデル重量 + KVキャッシュ + 計算バッファ
```

- **7Bモデル (Q4_K_M)**: 重量 ≈ 4.9GB
- **32KコンテキストのKVキャッシュ (FP16)**: ≈ 4GB
- **合計**: RTX 4060 8GBではギリギリ

この計算は以下の式で求められる：

```python
def kv_cache_memory(n_layers, n_heads_kv, head_dim, context_length, dtype_bytes=2):
    """KVキャッシュメモリ使用量 (GB)"""
    bytes_total = 2 * n_layers * n_heads_kv * head_dim * context_length * dtype_bytes
    return bytes_total / (1024**3)
```

> **要約**: コンテキストが長くなるほど、KVキャッシュがモデル重量を追い越す。32K以上では**KVキャッシュの量子化が必須**になる。

## 2. PagedAttention — vLLMの核心技術

### 原理

PagedAttentionは、オペレーティングシステムの仮想メモリ分页（Paging）思想をAttentionに適用した画期的な手法：

1. **物理ブロック池化**: GPU显存を固定サイズ（16トークン）の物理ブロックに分割し、グローバルブロックプールを構築
2. **論理-物理マッピング**: 各シーケンスに軽量ページテーブル（Page Table）を維持し、論理ブロックから物理ブロックへのマッピングを管理
3. **必要なときに割り当て**: 動的に物理ブロックを割り当て、事前に固定長を予約する浪費を排除
4. **共有メカニズム**: copy-on-write（CoW）により、同じプロンプトから派生する複数の生成サンプルがKVキャッシュを共有可能

### パフォーマンス

LLaMA-7B + A100 80GBでのベンチマーク：

| 指標 | 従来フレームワーク | vLLM (PagedAttention) | 向上幅 |
|------|-------------------|----------------------|--------|
| スループット (tok/s) | 1,200 | 4,850 | **+304%** |
| 显存利用率 | 38% | 92% | **+142%** |
| 100並列P99レイテンシ (ms) | 1,850 | 420 | **77%↓** |

### 中国クラウドでの実装

vLLMのPagedAttentionは、主要中国クラウドプラットフォームでネイティブサポートされている：

- **阿里云PAI**: vLLM最適化版、QPSで従来比3倍
- **腾讯云TI**: PagedAttention + 连续批処理（Continuous Batching）
- **火山引擎ArcLake**: vLLMネイティブ統合、GPUプールの動的スケジューリング

## 3. TriAttention — 最新研究（2026年4月）

MIT、NVIDIA、浙江大学の共同研究チームが**TriAttention**を提案した：

- **KVキャッシュ圧縮手法**: フルAttentionの精度を維持しつつ、**2.5倍のスループット向上**、**10.7倍のKVメモリ削減**を実現
- **RoPE（Rotary Position Embedding）活用**: 現代のLLMで広く使われているRoPE位置エンコーディングを基盤に、**直近のトークンのみ**を重要とみなして推論
- **長連鎖推論対応**:  retrieval headに関連するトークンが数千トークン後に重要になるような推論チェーンにも対応
- **Q/K集中特性発見**: 異なるモデルアーキテクチャ間で同一のQ/K集中パターンが観測され、ドメイン固有の特性ではないことが確認

## 4. KVキャッシュ量子化

モデル重量量子化（GGUF Q4_K_Mなど）とは異なり、**推論中にリアルタイムでKVキャッシュを圧縮**する技術：

### 量子化レベル

| 設定 | メモリ使用量 | 精度損失 | 用途 |
|------|-------------|----------|------|
| `f16`（デフォルト） | 基準 | なし | 高品質推論 |
| `q8_0` | f16の1/2 | 非常に微小 | 品質/コストのバランス |
| `q4_0` | f16の1/4 | 2-3% | 8GB GPUでの32Kコンテキスト |

**OllamaのKVキャッシュ量子化**:

```bash
# 環境変数でKVキャッシュ量子化レベルを設定
export OLLAMA_KV_CACHE_TYPE=q4_0
ollama serve
```

### 適応的KVキャッシュ量子化

コンテキスト長に基づいて量子化レベルを動的に切り替えるアプローチが注目されている：

- **短コンテキスト (<4K)**: FP16（量子化不要）
- **中コンテキスト (4K-32K)**: INT8
- **長コンテキスト (>32K)**: INT4/Q4

## 5. Unsloth Dynamic 2.0 — モデル特化量子化

Unslothチームが発表した**Dynamic 2.0**は、標準的な「一様量子化」を超えたモデル特化アプローチ：

### 3つの核心技術

1. **逐層差異化量子化**: アテンション層、FFNの初期層など、重要な層は8-bit/16-bitを保持。他の層を低精度に圧縮
2. **モデル特化設計**: 各モデルのアーキテクチャに合わせた量子化マップを個別生成。Gemma 3の重要層とMiniMax-M2.7の重要層は異なる位置にある
3. **高品質キャリブレーションデータ**: Wikipediaテキストだけでなく、150万トークン以上の対話形式データセットをハンドキュレーション

### モEアーキテクチャ対応

MoE（Mixture of Experts）モデルの**専門家層**に特殊な量子化MXFP4_MOEフォーマットを適用。DeepSeek-V3/R1/MiniMax-M2.7などのMoEモデルで特に効果的。

### 評価

Unsloth Dynamic 2.0のKL散度は、標準imatrix量子化を全面的に凌駕。Unslothチームの言葉：

> 「Accuracy is Not All You Need」— 正確性は同じでも、答えの「フリップ率」（正解が誤解に、誤解が正解に変わる）は全く異なる次元。KL散度が量子化の真の品質を示す。

## 6. その他最適化技術

### 连续批処理（Continuous Batching）

vLLMのPagedAttentionと組み合わせて、異なる長さのリクエストを動的にバッチ処理。GPU計算ユニットを常に満載状態に維持。

### 異種メモリ管理（次期展望）

- **CPU-GPU階層化**: 活発でないKVブロックをCPUメモリに退避
- **ブロックプリフェッチ**: アクセスパターンに基づく予測的ブロック読み込み
- **分散分页**: 複数GPU間のブロック協調管理

### FlashAttention-3

注意力計算のメモリ効率を大幅に改善。128K以上の長文コンテキストで必須の技術。中国のモデル開発コミュニティ（Qwenチームなど）が採用を推進。

## 7. 実践ガイド — 中国開発者向け

### RTX 4060 8GBでの運用

- **7Bモデル (Q4_K_M)** + **KVキャッシュ (q4_0)** → 8GBコンテキストまで
- **7Bモデル (Q4_K_M)** + **KVキャッシュ (f16)** → 4GBコンテキスト
- 32Kコンテキストが必要な場合は、**CPUオフロード**または**Qwen2.5-32BのMoE活用**を検討

### Mac M3 Max 128GBでの運用

- **70Bモデル (Q8_0)**: 243GB必要 → 128GBでは不可能。Q4に落とすか、Qwen2.5-32B-Q8_0が現実的
- **MiniMax-M2.7 UD-IQ4_XS (108GB)**: 128GBで15+ tok/s
- MLXネイティブ版: `mlx-community/MiniMax-M2.7-4bit` (120GB)

### Ollama最適化設定

```bash
# /etc/systemd/system/ollama.service 環境変数
Environment="OLLAMA_NUM_PARALLEL=4"      # 並列リクエスト数
Environment="OLLAMA_MAX_LOADED_MODELS=4"  # 同時ロードモデル数
Environment="OLLAMA_KV_CACHE_TYPE=q4_0"   # KVキャッシュ量子化
Environment="OLLAMA_FLASH_ATTENTION=1"    # FlashAttention有効化
```

## 課題と展望

### 現在の課題

1. **VRAMの壁**: 70B+モデルを低VRAMで高精度に動作させることは依然として困難
2. **MoE最適化**: 2026年後半にはMoEアーキテクチャのローカル最適化が焦点に
3. **国産チップ対応**: 昇騰/寒武紀/BirenでのVRAM最適化ツールチェーンは未成熟

### 2026年の展望

- **LLaMA-3.1 128K**と中国モデルの長文コンテキスト競争が激化
- **Speculative Decoding**の普及で推論速度の2-3倍向上が一般化
- **PagedAttention + INT4 KVキャッシュ**の組み合わせが、8GB GPUでの32Kコンテキスト推論を可能にする

## 2026年5月時点の最新動向

- **Qwen3.6-35B-A3B MoEのVRAM特性**: アクティブパラメータ3B（全体35B）のMoE構造により、通常推論では~12GB VRAM（Q4量子化）で動作。8Kコンテキストで約5-6GB、32Kコンテキストで約8-9GBのVRAM消費。RTX 4060 Ti (8GB)でも短めのコンテキストで動作可能。
- **DeepSeek-V4 Engram Memory**: 長期コンテキストの効率的な保持により、100Kトークン以上の推論でもKVキャッシュ増大を抑制。従来のPagedAttention + INT4 KVキャッシュと比較して~40%のVRAM削減を実現。
- **TriAttention (MIT/NVIDIA/ZJU)**: 2026年4月に発表されたKVキャッシュ圧縮手法。全Attentionと同等の品質を維持しつつ、スループット2.5倍。中国モデルへの適用事例が増加中。

## 2026年5月〜5月23日 最新アップデート

### 1. TriAttention v0.2.0 リリース（2026-04-22）— SGLangバックエンド・マルチハードウェア対応

- **v0.2.0正式リリース**（2026-04-22）: SGLangを第一級推論バックエンドとして追加（vLLMに加え）。MLX (Apple Silicon) 実験的サポート、AMD GPU (HIP/ROCm) コミュニティポート。
- **SGLang統合**: `triattention.sglang` モジュールにより、スケジューラ/ワーカーフック、per-head KVコンパクション、TP対応統計シャーディングを提供。`python -m triattention.sglang --model-path <path>` で起動可能。上流のSGLang変更不要（PR #24691）。
- **マルチバックエンド**:
  - vLLM: 安定版（本番パス）
  - SGLang: v0.2.0で新規追加
  - MLX (Apple Silicon M1-M4): 実験的
  - llama.cpp (ggml/ROCm): コミュニティ（AMD GPU対応、TriAttention + TurboQuantで~6.8× KV削減）
  - NVIDIA DGX Spark (GB10/sm-121): コミュニティ有効化
- **LongLive対応**: ARビデオ生成にTriAttentionのKVキャッシュ圧縮を適用
- **vLLMプラグイン自動検出**: インストール後、vLLMが自動的にTriAttentionプラグインを発見・有効化。コード変更不要。
- **設定可能な環境変数**: `TRIATTN_RUNTIME_KV_BUDGET`（デフォルト2048）、`TRIATTN_RUNTIME_DIVIDE_LENGTH`（128）、`TRIATTN_RUNTIME_WINDOW_SIZE`（128）など。
- **注意事項**: prefix cachingは非対応（自動無効化）、prefill chunkが大きすぎるとOOM発生可能性。
- ソース: [github.com/WeianMao/triattention/releases/tag/v0.2.0](https://github.com/WeianMao/triattention/releases/tag/v0.2.0)

### 2. Ollama v0.30.0 プレリリースシリーズ — アーキテクチャ大転換（2026年5月）

- **v0.30.0-rc20〜rc23**（2026-05-13〜05-22）: GGMLベースから**llama.cpp直接統合**へのアーキテクチャ移行。GGUFファイル形式のネイティブ互換性。
- **GGML廃止**: 従来のGGML抽象レイヤーを廃止し、llama.cppに直接対応。これにより上流のllama.cpp最適化、新量子化方式、ハードウェアサポートを迅速に取り込み可能。
- **Apple Silicon MLX加速**: MシリーズMacでMLXネイティブアクセラレーションを提供。統一メモリアーキテクチャを最大活用。
- **既知の問題**（プレリリース）: `laguna-xs.2`未対応、`llama3.2-vision`未対応。
- **ステータス**: 安定版v0.24.0維持推奨（本番環境）。最終v0.30.0タグ待ち。
- ソース: [github.com/ollama/ollama/releases/tag/v0.30.0-rc23](https://github.com/ollama/ollama/releases/tag/v0.30.0-rc23), [appselfhost.com](https://appselfhost.com/ollama-v0-30-0-rc21-released-architecture-shift-to-native-llama-cpp-support/)

### 3. SGLang v0.5.11→v0.5.12（2026-05-05〜05-16）— DeepSeek V4最適化本格化

- **v0.5.11**（2026-05-05）: CUDA 13 + Torch 2.11への移行。Decode Radix Cache for PD Disaggregation対応。Mooncakeインクリメンタル転送対応。
- **v0.5.12**（2026-05-16）: **HiCache for DeepSeek V4**（UnifiedRadixTree上）— #24691。HiSparse FP8 KV cache via flashmla_kv backend。
- **HiCacheエコシステム**:
  - UnifiedRadixTree対応フレームワーク（#23316）
  - SWA HiCache統合（#23391）
  - DeepSeek V4 DSAモデル用HiCache（#24691）
  - Mooncake store経由SSDオフロード（#24277）
  - 非同期圧縮 + デコードによるスループット向上
- **MegaMoE最適化**:
  - W4A4 MegaMoEカーネル — 精度損失ほぼなしで高速化（#25052）
  - Marlin/FlashInfer W4A8 MoEカーネル on Hopper（#24816, #24986）
  - 最適化MHC + DeepGemm pipeline（#24775）
- **PD Disaggregation進展**:
  - Pipeline Parallelism + PD対応 for DeepSeek V4（#24700）
  - Decode-side RadixCache（#19746）
  - HiSparse PD DRAM直接転送（#21591）
- **ロードマップ**: エージェントワークロード向け分散KVCacheシステム（#21846）— HiCache・HiSparse・PP・Eagleのエンドツーエンド統合を目標。
- ソース: [github.com/sgl-project/sglang/releases/tag/v0.5.12](https://github.com/sgl-project/sglang/releases/tag/v0.5.12)

### 4. DeepSeek V4 — vLLM最適化詳細

- **vLLM公式ブログ**（2026-04-24）: DeepSeek V4のKVキャッシュ最適化詳細。
  - **1MコンテキストでKVキャッシュわずか9.62 GiB**（bf16）— V3.2推定83.9 GiBの**8.7分の1**。
  - **実際の運用**: indexer cacheはFP4、attention cacheはFP8 — bf16比でさらに約2倍削減。
  - **カーネル融合**: Compressor + RMSNorm + RoPE + cache挿入を単一カーネルに融合（1.4-3倍高速化）。
  - **Fused Q norm + KV RoPE + K insert**: 水平融合で10-20倍高速化。
  - **パラレル実行**: c128a層でmain KV圧縮とSWAトークン挿入を並列実行（5-6%レイテンシ低減）。
  - **今後の最適化**: DeepGEMM MegaMoEカーネル、Paged prefillカーネル。
- **ROCm DeepSeek V4 Tritonカーネル**（PR #41812）: ROCm（AMD MI355x）上のDeepSeek V4 sparse MLAをTritonカーネルで実装。2026-05-11マージ。
- **SM12x DeepSeek V4対応**（PR #40899）: Blackwell SM12x（RTX 50xx）向けTriton sparse MLA fallbackパス。2026-04-26マージ済み。
- **TurboQuant + MLA融合デコード**（PR #41803）: DeepSeek MLA向けTriton融合TurboQuantデコードバックエンド。k8v4で1.16-1.96倍スループット向上（2026-05-14）。
- ソース: [vllm.ai/blog/2026-04-24-deepseek-v4](https://vllm.ai/blog/2026-04-24-deepseek-v4), github.com/vllm-project/vllm

### 5. 北京大学 GQLA — 同一モデルパラメータでH100とH20の両方に最適化（2026年5月）

- **GQLA（Grouped Query Latent Attention）**: arXiv:2605.15250（2026年5月発表）。DeepSeekのMLAを最小限の変更で拡張。
- **同一重みで2つの実行パス**:
  - **GQAパス**: H20向け（4224 bytes/token、計算/データ比38.8、22.1万token/s）
  - **MQA吸収パス**: H100向け（1152 bytes/token、計算/データ比242、35.4万token/s）
- **再学習不要**: デプロイ時にワンタイム変換するだけ。両パスの出力は数学的に同一。
- ソース: [techwalker.com/2026/0522/3187912](https://www.techwalker.com/2026/0522/3187912.shtml)

### 6. 昇腾 Ascend 910C — 推論最適化最新動向

- **SGLang昇腾GDNカーネル最適化**（PR #24597）: Qwen3.6-27B（48 GDN層 + 16 full-attention層）のchunked prefillメタデータ事前計算により、TTFT最大12.2%削減、スループット9.5%向上（2026-05-11）。
- **FlashAttention-NPU**: Ascend 910B/910C向けFlashAttention実装。Paged KV Cache、MQA/GQA、variable-length sequences対応。CANN 8.5.0+必須。
- **Ascend CloudMatrix384**: INT8量子化によりメモリ帯域幅消費を大幅削減。DeepSeekモデルの推論に最適化。PDC（Prefill-Decode-Caching）分離アーキテクチャ。
- **DeepSeek V4 on Ascend**: DeepSeek V4はHuawei Ascend NPUを第一級サポート。vLLM-Ascendコミュニティフォーク活用推奨。7Bモデルで~45 tok/s、14Bモデルで~22 tok/s（1×910B）。
- ソース: [github.com/sgl-project/sglang/pull/24597](https://github.com/sgl-project/sglang/pull/24597), [arxiv.org/html/2506.12708v2](https://arxiv.org/html/2506.12708v2), [github.com/MinghuasLab/flash-attention-npu](https://github.com/MinghuasLab/flash-attention-npu)

### 7. 寒武紀 Cambricon MLU — ツールチェーン状況

- **MagicMind推論エンジン**: MLIRベースのグラフコンパイル技術。FP32/FP16/INT16/INT8対応。MLU370シリーズでResNet-50、Transformer、VGG16等でGPU対抗性能。
- **mlu-ops v1.8.1**（2026-01-06）: BANG C++ベースの高性能オペレーター実装。90名のコントリビューター。
- **Cambricon PyTorch (torch_mlu)**: PyTorchコミュニティ統合。CNToolkit/CNNL/CNCL依存。PyTorch 2.4.0対応。
- **DeepSeek V4との関係**: V4は昇腾910Bと寒武紀MLUでトレーニングされた最初のフロンティアモデル（論文公開済み）。
- ソース: [cambricon.com](https://cambricon.com/index.php?a=lists&catid=378), [github.com/Cambricon/mlu-ops](https://github.com/Cambricon/mlu-ops)

### 8. 新たなKVキャッシュ圧縮研究（2026年3月〜5月）

| 手法 | 出典 | 公開日 | 圧縮率 | 特徴 |
|------|------|--------|--------|------|
| **CompilerKV** | arXiv:2602.08686 | 2026-02 | 512 token budgetでFullKVの97.7% | リスク適応型・ヘッド異質性考慮 |
| **EchoKV** | arXiv:2603.22910 | 2026-03 | 圧縮率0.5でほぼロスレス | 層間・層内類似性活用、軽量ネットで残差KV予測 |
| **DeltaKV** | arXiv:2602.08005 | 2026-02 | 元の29%まで削減 | 残差ベース圧縮 + Sparse-vLLM（2倍スループット） |
| **LongFlow** | arXiv:2603.11504 | 2026-03 | 80%圧縮、11.8倍スループット | 推論モデル向け、FlashAttention融合カーネル |
| **KVTC** | ICLR 2026 | 2025-11 | 20倍圧縮（ロスレス）〜40倍+ | PCA+適応量子化+エントロピー符号化 |
| **CompressKV** | ICLR 2026 | 2026 | 予算0.7%で精度90% | Semantic Retrieval Heads + 層適応割当 |
| **Fast KVzip** | arXiv:2601.17668 | 2026-01 | 70%削除、ほぼロスレス | ゲーティングベース、バックプロパゲーション不要 |
| **Compressed PagedAttention (Zipage)** | arXiv:2603.08743 | 2026-03 | 95%性能維持、2.1倍高速化 | PagedAttention + トークン単位追い出し統合 |
| **TurboQuant** | ICLR 2026 | 2026-03 | 4-bit非対称量子化、最大75%削減 | 外れ値認識、RTX 5070Tiで512Kコンテキスト |
| **KVSculpt** | arXiv:2603.27819 | 2026-03 | KL発散3.5-4.1倍改善 | L-BFGS最適化 + 最小二乗 + 適応予算配分 |
| **KV-CAT** | arXiv:2605.05971 | 2026-05 | トレーニング時KV圧縮性誘導 | マスキング戦略で圧縮しやすい表現を学習 |

### 9. Qwen3.6 MoE VRAM最適化 — ローカル推論実測データ

- **Qwen3.6-35B-A3B（MoE）**:
  - Q4_K_M量子化: 21.2 GB VRAM、24.1 tok/s（RTX 4090）
  - IQ4_XS: 17.7 GB、最大262Kコンテキスト
  - アクティブ3Bのみ、256専門家中9専門家/トークンを起動
  - `--n-cpu-moe`オフロード: 16GB GPUで18-28 tok/s（8-10専門家GPU常駐、20専門家CPU）
  - Native 262Kコンテキスト（ハイブリッドAttention: 30 Gated DeltaNet + 10 GQA層）
- **Qwen3.6-27B（Dense）**:
  - UD-Q5_K_XL: 18.65 GB、156K最大コンテキスト
  - 64層中16層のみKVキャッシュ保持（3:1 DeltaNet:GatedAttn）
  - SWE-bench Verified: 77.2（27B Dense）vs 73.4（35B MoE）
- **TurboQuant KV圧縮**: llama.cpp PR #20969。Randomized Hadamard Transform + Lloyd-Max量子化。3.5 bpw。トークンあたりKV ~14KB（FP16の64KBから4.6倍圧縮）。NIAH 100%維持。
- **Sparse V（注意ゲート付き値逆量子化）**: 注意重みが10⁻⁶以下の位置のV逆量子化をスキップ。最大22.8%デコード速度向上。任意のKV量子化形式で動作可能。
- ソース: [craftrigs.com](https://craftrigs.com/guides/qwen3-6-moe-cpu-offload-n-cpu-moe-fit-on-guide/), [wal.sh/research/qwen3.6-local-first-inference](http://wal.sh/research/qwen3.6-local-first-inference/), [zoliben.com](https://zoliben.com/en/posts/2026-04-23-qwen-36-35b-vs-27b-benchmark-results/)

### 10. PagedAttention派生 — PagedEviction（2026年）

- **PagedEviction**: vLLMのPagedAttentionと完全互換のブロック単位KVキャッシュ追い出し手法。FlashAttentionカーネル変更不要。
- **Prefill時**: ブロック分割前にトークン単位重要度評価
- **Decode時**: 最新ブロック完了後に1ブロック全体を追い出し（フラグメンテーション最小化）
- **パフォーマンス**: 1024 token予算でFull Cache比0.5-1.5 ROUGE差以内、スループット最大3.1倍。LLaMA-1B/3B/8Bでレイテンシ10-12%低減。
- ソース: ACL 2026 Findings, [arxiv.org/pdf/2509.04377](https://arxiv.org/pdf/2509.04377)

## 関連リンク

### 内部リンク
- [[china-local-deployment]] — 大規模モデルのローカルデプロイメント
- [[pagedattention]] — vLLMのページベースAttention
- [[gguf-quantization]] — GGUF量子化フォーマット
- [[speculative-decoding]] — 予測的デコーディング
- [[flash-attention]] — FlashAttention最適化

### 外部ソース
| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| 阿里云 — PagedAttention原理 | [developer.aliyun.com/article/1685154](https://developer.aliyun.com/article/1685154) | T2 | vLLMのPagedAttention詳解 |
| 阿里云 — PagedAttention最適化 | [developer.aliyun.com/article/1664805](https://developer.aliyun.com/article/1664805) | T2 | 設計理念と実装メカニズム |
| 昇騰 — vLLM PagedAttention | [ascendai.csdn.net](https://ascendai.csdn.net/69792ffea16c6648a98589e1.html) | ❌ | CSDN除外（参照のみ） |
| 163 — MiniMax-M2.7量子化 | [163.com/dy/article/KQB87POB0519EA27](https://www.163.com/dy/article/KQB87POB0519EA27.html) | T3 | Unsloth Dynamic 2.0詳解 |
| MIT/NVIDIA/TriAttention | [marktechpost.com/2026/04/11/triattention](https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/?amp=) | T2 | KVキャッシュ圧縮の新研究 |
| 谢先斌 — Ollama設定 | [xiexianbin.cn/ai/ollama](https://www.xiexianbin.cn/ai/ollama/index.html) | T2 | Ollama環境変数・最適化 |
| 掘金 — Ollama+Qwen2026 | [juejin.cn/post/7603677143214473231](https://juejin.cn/post/7603677143214473231) | T1 | 2026最新版Ollama部署ガイド |
| TriAttention v0.2.0 | [github.com/WeianMao/triattention/releases](https://github.com/WeianMao/triattention/releases) | T1 | SGLangバックエンド追加 |
| SGLang v0.5.12 | [github.com/sgl-project/sglang/releases/tag/v0.5.12](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) | T1 | DeepSeek V4 HiCache正式対応 |
| vLLM DeepSeek V4 Blog | [vllm.ai/blog/2026-04-24-deepseek-v4](https://vllm.ai/blog/2026-04-24-deepseek-v4) | T1 | KVキャッシュ9.62GiB@1M |
| Ollama v0.30.0-rc | [github.com/ollama/ollama/releases](https://github.com/ollama/ollama/releases/tag/v0.30.0-rc23) | T1 | llama.cpp直接統合移行 |
| 北大GQLA | [techwalker.com/2026/0522/3187912](https://www.techwalker.com/2026/0522/3187912.shtml) | T2 | H100/H20両最適化 |
