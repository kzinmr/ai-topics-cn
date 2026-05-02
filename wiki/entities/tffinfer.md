---
title: TFFInfer — C++製LLM推論フレームワーク
created: 2026-05-02
updated: 2026-05-02
tags: [tool, llm, inference, cpp, cuda, gguf, open-source]
aliases: ["TFFInfer", "LLM-TFFInfer"]
source_lang: zh-CN
---

# TFFInfer — C++製LLM推論フレームワーク

> **トレンド順位**: Juejinで技術解析シリーズが注目を集める
> **ソース**: Juejin [T1]
> **重要度**: 中 — C++20 + CUDAのゼロスクラッチLLM推論フレームワーク、実装詳細の技術的価値が高い

## 概要

TFFInferは、C++20とCUDAでゼロから開発された大規模言語モデル（LLM）推論フレームワーク。約3万行のコードベースを持ち、GGUF形式のモデルロードから計算図構築、CUDAカーネル実行までの完全な推論パイプラインを実装。2026年4月-5月にかけてJuejinで連載技術解析記事が公開され、注目されている。

## 技術アーキテクチャ

### 対応モデル・フォーマット

- **GGUF形式**: llama.cpp互換の単一ファイル（またはマルチファイル分割）ウェイトコンテナ
- **量子化対応**: Q8_0等
- **テスト済みモデル**: Qwen3-8B

### 技術スタック

| カテゴリ | 技術 | バージョン | 用途 |
|---------|------|-----------|------|
| プログラミング言語 | C++20 | - | コアロジック、テンプレートメタプログラミング |
| GPUバックエンド | CUDA | 12.x | GPU演算子実装 |
| ビルドシステム | CMake | 3.18+ | クロスプラットフォームビルド |
| ロギング | Google glog | v0.7.1 | 高性能ログ記録 |
| タスクスケジューリング | Taskflow | v3.10.0 | DAGタスクフローエンジン |
| 数学最適化 | libdivide | v5.2.0 | 高速除算演算 |
| JSON解析 | nlohmann/json | v4.0.0 | 設定ファイル解析 |
| GEMM最適化 | NVIDIA CUTLASS | - | 行列積演算最適化 |

### モジュール構成

```
TFFInfer/
├── src/
│   ├── runtime/           # 推論ランタイム（LLMInferRuntime）
│   ├── model/             # モデル層
│   │   ├── loader/        # ローダー/ディテクター/クリエイター
│   │   ├── memory/        # テンソル/メモリ管理
│   │   └── vocab/         # 語彙処理
│   ├── graph/             # 計算図
│   │   ├── optimizer/     # 図最適化
│   │   └── scheduler/     # タスクスケジューリング
│   ├── operator/          # 演算子実装
│   │   ├── cuda/          # CUDAカーネル（FlashAttention/GEMM/RoPE等）
│   │   └── cpu/           # CPUカーネル（バックアップ）
│   └── manager/           # バッチ/メモリ/デバイス管理
├── third_party/           # 外部依存
├── test/                  # テスト
└── cmake/                 # ビルド設定
```

## GGUFLoader 解析パイプライン

TFFInferのモデルロードは以下の5段階で構成:

| ステップ | 関数 | 役割 |
|---------|------|------|
| 0 | `FileLoader`/`FileMMap` 構築 | ファイルオープン、メモリマッピング |
| 1 | `check_file` | GGUFマジックナンバー（4バイト）検証 |
| 2 | `load_header` | バージョン、テンソル数(`_n_tensors`)、KV数(`_n_kv`)読込 |
| 3 | `load_kv_meta` | KVメタデータ循環読込 → `ModelContext::_kv` |
| 4 | `load_model_config` | KVから推論必要フィールドを`ModelConfig`に抽出 |
| 5 | `load_tensor_info` | 各テンソルの名前・次元・タイプ・ファイル内オフセット読込、`ModelWeight`マップ構築 |

### 静的登録マクロ

フォーマット検出とローダーの分離設計により、新フォーマット追加時に`ModelDetectorBase`/`ModelLoaderBase`を独立登録可能:

```cpp
GGUFDetector: REGISTER_MODULE_OBJECT(..., MODEL_DETECTOR_FLAG, "gguf")
GGUFLoader:   REGISTER_MODULE_OBJECT(..., MODEL_LOADER_FLAG, "gguf")
```

### FileMMapによるメモリマッピング

`ModelConfig::_use_mmap`が真の場合:
- `mmap(..., PROT_READ, MAP_SHARED, ...)` でファイルマッピング
- `posix_fadvise(..., POSIX_FADV_SEQUENTIAL)` でシーケンシャル読込ヒント
- NUMA環境では`POSIX_MADV_RANDOM`等策略でプリフェッチ制御

## 推論ランタイム — LLMInferRuntime

```cpp
class LLMInferRuntime {
    ModelConfig _model_config;
    std::shared_ptr<LLMVocabulary> _vocabulary_ptr;
    std::shared_ptr<ModelLoaderBase> _model_loader;
    std::shared_ptr<ModelCreatorBase> _model_creator;

    std::shared_ptr<Graph> _prefill_graph_ptr;   // プリフェイル図
    std::shared_ptr<Graph> _decode_graph_ptr;    // デコード図
    std::shared_ptr<Graph> _mem_graph_ptr;       // メモリ管理図

    std::shared_ptr<GraphOptimizer> _graph_optimizer;
    std::shared_ptr<LLMMemManager> _mem_manager_ptr;
    std::shared_ptr<LLMTaskFlowManager> _task_manager;
    std::shared_ptr<LLMBatchManager> _llm_batch_manager_ptr;
    std::shared_ptr<DeviceManager> _device_manager;

    std::unordered_map<int, std::shared_ptr<LLMKVCache>> _kv_cache_ptr;
};
```

### CUDAカーネル

- Flash Attention
- 量子化GEMM（Q8_0等）
- RoPE（Rotary Position Embedding）
- 要素別演算（RMSNorm, SiLU, GeLU, Softmax等）

## 現状の制限

- ⚠️ GGUF形式のみ対応（他フォーマット拡張が必要）
- ⚠️ 単一GPU推論（マルチGPU並列未実装）
- ⚠️ 静的バッチ処理（Continuous Batching未実装）
- ⚠️ モデル対応限定的（現状Qwen3-8Bのみ検証済み）

## リポジトリ

- **Gitee**: https://gitee.com/NKK_Ovit/tffinfer
- **GitHub**: https://github.com/NKKdev/TFFInfer
- **コード行数**: 約30,000行

## 関連リンク

### 内部リンク

- [[qwen]] — 対応モデル（Qwen3-8B）
- [[deepseek]] — GGUF形式の主要利用者
- [[llama-cpp]] — GGUF形式の発祥プロジェクト

### 外部ソース

| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| Juejin — TFFInferプロジェクト解析(三) | https://juejin.cn/post/7634860379343962121 | T2 | モデルロードの詳細技術解析 |
