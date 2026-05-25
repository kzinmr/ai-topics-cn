---
title: "中国大模型本地部署 — 量子化・VRAM最適化・消費者GPUでの推論"
created: 2026-04-19
updated: 2026-05-25
tags: [inference, quantization, local-deployment, hardware, vram-optimization, china]
aliases: ["本地部署", "国产模型本地运行", "VRAM优化", "量化技术", "GGUF", "GPTQ", "AWQ"]
source_lang: zh-CN
---

# 中国大模型本地部署 — 量子化・VRAM最適化・消費者GPUでの推論

> **重要度**: 🔥🔥 HIGH — APIコスト・プライバシー・規制回避の核心技術
> **関連概念**: [[vram-optimization]], [[gguf-quantization]], [[llama-cpp]], [[deepseek]], [[qwen]]
> **関連エンティティ**: [[ollama-criticism]], [[biren-technology]], [[cambricon]], [[moore-threads]]

## 概要

中国の開発者コミュニティにおいて、大規模言語モデル（LLM）の**本地部署（ローカルデプロイ）**は2025年から急激に普及した。背景には以下の3つの要因がある：

1. **APIコストの問題**: クラウドAPIは従量課金であり、高頻度利用では月額数万円に達する。ローカル推論は初期投資こそ必要だが、運用コストを大幅に削減可能。
2. **プライバシーとデータ主権**: 企業機密・個人データをクラウドに送信することへの懸念。特に金融・医療・政府関連プロジェクトでは**オンプレミス必須**のケースが多い。
3. **規制とアクセス制限**: 海外モデル（GPT/Claude）は中国国内から直接アクセス困难。国産モデルをローカルで動かせば、ネットワーク制限・検閲・アカウント停止のリスクを回避できる。

## 主要なローカル推論エコシステム

### 1. Ollama — 消費者向け標準
OllamaはMac/Windows/Linuxで動作する**ワンコマンドLLMランナー**。中国コミュニティでは「**一键部署**」（ワンクリックデプロイ）として絶大な人気。Qwen2.5/3/3.6、DeepSeek-R1/V3/V4、GLM-4/5、Yi-1.5など主要国産モデルが公式/コミュニティレジストリで提供されている。2026年4月時点でGitHub **169k Stars**を達成し、40,000以上のコミュニティ統合を誇る。最新バージョンはv0.17.7（2026年3月）。

- **特徴**: Modelfileによるカスタマイズ、API互換エンドポイント、軽量バックエンド
- **課題**: 大規模モデル（70B以上）のVRAM要件、並列リクエスト処理の限界
- **中国適応**: 国内ミラーサイト（ModelScope/Ollama中国ノード）でダウンロード速度を最適化

### 2. llama.cpp / GGUF — 量子化デファクトスタンダード
GGUFフォーマットは**CPU/Mac Silicon/低VRAM GPU**での推論を可能にする量子化標準。Q4_K_M（4bit）〜Q8_0（8bit）の量子化レベルを選択可能。

- **中国モデル対応**: Qwen2.5-72B-GGUF、DeepSeek-R1-Distill-Qwen-32B-GGUF等がHuggingFace/ModelScopeで公開
- **性能**: RTX 4090（24GB VRAM）でQwen2.5-72B-Q4_K_Mが~15 tok/s、Mac M3 Maxで~30 tok/s
- **ツールチェーン**: `llama-quantize`、`llama-server`、Open WebUI連携

### 3. vLLM / SGLang — 高スループット推論
エンタープライズ用途では**vLLM**（PagedAttention実装）と**SGLang**（構造化生成最適化）が主流。複数GPU並列、バッチ処理、ストリーミング出力に対応。

- **中国クラウド統合**: 阿里云PAI、腾讯云TI、火山引擎ArcLakeがvLLMネイティブサポート
- **ベンチマーク**: QPS（1秒あたりクエリ数）でOllamaの3〜5倍、レイテンシは同等

### 4. LM Studio / Text Generation WebUI — GUIフロントエンド
技術者以外のユーザー向けに、**ドラッグ&ドロップでモデル読み込み→チャット形式で対話**できるGUIツールが普及。LM StudioはGGUF/GPTQ/AWQを統一サポート。

## ハードウェア生態系

### 消費者GPU
| デバイス | VRAM | 対応モデル規模 | 推論速度 (tok/s) |
|----------|------|----------------|------------------|
| RTX 4090 | 24GB | 32B〜70B (Q4) | 15〜30 |
| RTX 4080 | 16GB | 14B〜32B (Q4) | 20〜40 |
| RTX 4060 Ti | 8GB | 7B〜14B (Q4) | 10〜20 |
| Mac M3 Max | 128GB统一 | 70B (Q8) | 25〜50 |

### 中国製AIアクセラレータ
NVIDIA制裁の影響で、国産チップのローカル推論対応が加速：
- **昇騰 910C (Huawei)**: CANNソフトウェアスタック、MindSpore/llama.cppポート版対応
- **MLU 370/590 (Cambricon)**: 量子化推論サポート、Dify/扣子との統合事例
- **Biren BR100**: CUDA互換レイヤー、vLLM移植進行中
- **Moore Threads MTT S4000**: ゲーミングGPU由来、推論特化ドライバ開発中

## 量子化技術と最適化

### 量子化方式
- **GPTQ**: 層別最適化、精度低下最小。GPU推論に最適
- **AWQ**: 活性化重視量子化、VRAM使用量削減効果大。モバイル/エッジ向け
- **GGUF (K-Quants)**: CPU/GPUハイブリッド、Mac Siliconで最高性能
- **FP8 / INT8**: 訓練後量子化（PTQ）、推論速度最大化
- **Unsloth Dynamic 2.0**: モデル特化逐層差異化量子化。標準imatrix量子化を凌駕するKL散度性能。MoEモデルにMXFP4_MOEフォーマット対応

### Unsloth Dynamic 2.0 — 2026年新トレンド

Unslothチームの**Dynamic 2.0**量子化は、中国開発者コミュニティで急速に採用が広がっている：

1. **逐層差異化量子化**: アテンション層・FFN初期層は8-bit/16-bitを保持。他の層を低精度に圧縮
2. **モデル特化設計**: GEMMA 3とMiniMax-M2.7では異なる重要層の位置。各モデルに個別に量子化マップを生成
3. **高品質キャリブレーション**: Wikipediaだけでなく、150万トークン以上の対話データセットをハンドキュレーション
4. **MoE対応**: MXFP4_MOEフォーマットでDeepSeek/R1/MiniMax-M2.7等のMoEアーキテクチャを最適化

**MiniMax-M2.7のUnsloth Dynamic 2.0量子化版**（2026年4月）は、UD-Q4_K_XLが「スイートスポット」として推奨される。オリジナルモデルとの正確度低下は6.0ポイントのみ、エラー増加率は+22.8%。

### VRAM最適化テクニック
- **PagedAttention**: vLLMの核心技術。KVキャッシュをページ単位で管理し、メモリフラグメンテーションを解消
- **Speculative Decoding**: 小モデルで草案生成→大モデルで検証。2〜3倍の推論速度向上
- **FlashAttention-3**: 注意力計算のメモリ効率化。長文コンテキスト（128k+）で必須
- **KV Cache圧縮**: 対話履歴を要約ベクトルに変換し、キャッシュサイズを削減
- **KVキャッシュ量子化**: Ollamaの`OLLAMA_KV_CACHE_TYPE=q4_0`でRTX 4060 8GBでも32Kコンテキスト対応
- **TriAttention**（2026年4月）: MIT・NVIDIA・浙江大学の研究。フルAttentionの精度を維持しつつ2.5倍スループット、10.7倍KVメモリ削減

## コミュニティとエコシステム

### ModelScope (魔搭) — 中国のHuggingFace
阿里云運営のモデルプラットフォーム。GGUF/GPTQ/AWQ量子化済みモデルが豊富。ダウンロード速度・日本語ドキュメント・中国法対応でHuggingFaceを代替する動きが加速。

### 开源コミュニティの動向
- **本地部署ガイド**: 知乎/掘金で「RTX 4090でDeepSeek-R1を動かす」「Mac M3でQwen2.5-72Bを快適に使う」等の実装記事が多数公開
- **コスト比較**: API利用 vs 本地部署のTCO（総所有コスト）分析記事がV2EXで議論される。月100時間利用で**本地部署が6ヶ月でペイ**するケースが報告されている
- **プライバシー懸念**: 企業利用における「データがモデル開発元に送信されない」ことがローカル採用の最大の動機

## 課題と展望

### 1. 大規模モデルのVRAM壁
70B以上のモデルを低VRAMで動かすには**量子化による精度低下**が避けられない。Unsloth Dynamic 2.0のようなモデル特化量子化で改善が進んでいるが、MoE（Mixture of Experts）アーキテクチャのローカル最適化が2026年後半の焦点に。活性化パラメータのみをVRAMに載せる方式（DeepSeek-V4: 1T総パラメータ/11B活性化）が消費者GPUでも実行可能になりつつある。

### 2. 国産チップのソフトウェア生態系
ハードウェア性能は向上しているが、**CUDAエコシステムとの互換性**が依然として課題。PyTorch/TensorFlowの直接サポート、vLLM/llama.cppの安定動作が今後の普及の鍵。

### 3. 規制のグレーゾーン
ローカルで動作する国産モデルでも、**生成コンテンツの審査責任**は利用者に課される可能性。2026年3月の「生成AIサービス管理弁法」改正で、ローカルデプロイ事業者への届出義務が議論されている。

### 4. KVキャッシュの次世代最適化
TriAttention（MIT/NVIDIA/浙大）等新研究により、KVキャッシュの10倍圧縮が可能に。2026年後半には**実装レベルでの採用**が始まる見込み。Ollamaの`OLLAMA_KV_CACHE_TYPE=q4_0`で既にINT4 KVキャッシュ量子化が利用可能。

### 05-01追加動向（Zhihu Frontier Weekly統合 2026-04-27）

### Qwen3.6-35B-A3B ツール呼び出しベンチマーク首位

Zhihu Frontier Weeklyの構造化ツール使用評価によると、RTX 4090 (48GB)上のQwen3.6-35B-A3B-FP8が**69/72（96%精度）**を達成、レイテンシ~1024ms。GLM、Kimi、DeepSeek、StepStar、MiniMaxの中国主要5社商用APIを上回った。

### ローカルデプロイ報告 — 16GB RAM + 8GB VRAMでの実用レベル

Zhihu貢献者@Jon.Xiaoの報告：RTX 4060 (8GB VRAM) + 16GB RAM環境で**~23Kトークンコンテキスト、~16 tok/s**を達成。3BアクティブパラメータのMoEモデルが~27B規模のdenseモデルに匹敵する性能を示し、消費者GPUでの実用性が確認された。

### Codexローカルインストール — 中国国内直接利用の実践報告

Juejin開発者「哪吒编程」が、Codexのローカルインストールと中国国内でのGPT-5-Codex直接利用の実践記事を公開。

**主なポイント**:
- 開発者自身のAIコーディングツール遷移: Cursor → Claude Code → Codex
- 新一代モデル未発表前からCodexを主力ツールとして使用
- 中国国内からの直接アクセス可能

> **出典**: Juejin（哪吒编程）— [本地安装Codex，国内直接使用GPT-5-Codex](https://juejin.cn/post/7554270339796336678) (2025-09-27) [T2]

### Codex — 中国開発者コミュニティでの人気上昇

Juejin開発者「技术爬爬虾」がCodexの詳細攻略と無料使用方法を解説した動画を公開。

**主な評価**:
- CodexがClaude Codeを**人気で上回る**と報告
- 最大の利点: **便宜大碗**（コスパ良好）かつ中国ユーザーに優しい
- 24いいね・54スターを獲得

> **出典**: Juejin（技术爬爬虾）— [AI编程新王Codex详细攻略](https://juejin.cn/post/7564688848602300457) (2025-10-26) [T2]

## 関連リンク

### 内部リンク
- [[vram-optimization]] — 显存最適化技術（KVキャッシュ圧縮・TriAttention等）
- [[gguf-quantization]] — GGUF量子化フォーマット
- [[llama-cpp]] — CPU推論エンジン
- [[deepseek]] — DeepSeekモデルアーキテクチャ
- [[qwen]] — Qwenモデルシリーズ
- [[ollama-criticism]] — Ollama論争
- [[biren-technology]] — 壁仞科技GPU
- [[cambricon]] — 寒武纪AIチップ
- [[moore-threads]] — 摩尔线程GPU

### 外部ソース
| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| 163 — MiniMax-M2.7量子化 | [163.com/dy/article/KQB87POB0519EA27](https://www.163.com/dy/article/KQB87POB0519EA27.html) | T3 | Unsloth Dynamic 2.0・MLX量子化版 |


## 国内でのCodexローカルインストール（2026-04-24更新）

中国国内のネットワーク環境下で**GPT-5-Codexをローカルにインストールして直接使用する**方法がJuejinで共有された。

### 背景と動機
- 中国国内からのOpenAI API直接アクセスが不安定
- プロキシ経由での利用はレイテンシ・コストの問題
- ローカルインストールにより安定した開発環境を構築

### 実装アプローチ
- `codex-cli`パッケージをローカル環境にインストール
- 代替エンドポイント経由でのAPI接続設定
- 国内ネットワーク環境に最適化された設定パラメータ

### 中国開発者コミュニティの意義
- 規制環境下でのAIツール利用の実践的解決策
- ローカル実行によるデータプライバシー確保
- コスト最適化の一環としての位置づけ

## 2026年5月時点の最新動向

- **Qwen3.6シリーズのローカル推論対応**: Qwen3.6-27B（Denseモデル）およびQwen3.6-35B-A3B（MoEモデル）がOllama/vLLMでローカル実行可能に。後者はアクティブパラメータが3Bであり、RTX 4090 (24GB VRAM)でフルスピード動作。Qwen3.6-Max-Previewはクローズドウェイトのためローカル非対応。
- **Ollama v0.17.x**: マルチモデル同時実行、メモリ動的割り当て改善、DeepSeek-V4のMoE構造最適化対応。
- **DeepSeek-V4 ローカル推論**: Ascend 910C/MLU 590での推論ベンチマークが公開。8 x 910Cで~50 tok/s (Q4)。

> **出典**: Juejin — [本地安装Codex，国内直接使用GPT-5-Codex](https://juejin.cn/post/7620060655607857178) [T2]


#### 2026年5月上旬追加情報
- **oMLX (OpenMLX)**: 地瓜AIがApple Siliconネイティブ推論サーバーoMLXをリリース。MLXフレームワークベースでQwen3.6/DeepSeek-V4のMacBook上での推論性能が30%向上。M4 Max搭載Macでは70B級モデルがQ4量子化でリアルタイム動作。
- **LocalClaw**: 零配置Agentランタイム「LocalClaw」が登場。vLLM + OpenClaw + MCPをDocker Compose一行でデプロイ。CLI操作が苦手な中国開発者向けにWeb UIを搭載。
- **ERNIE 5.1ローカル実行**: BaiduがERNIE 5.1のローカル実行用量子化モデル(GGUF/GPTQ)を公開。240B MoE(Q4: ~130GB VRAM)は4 x A100-80GBで動作可能。
- **DeepSeek-V4 TCO分析**: 8 x 910Cサーバー(約30万元)の場合、API呼び出し月100万回超で元が取れる試算(V2EX議論)。

> **出典**: 地瓜AI — [oMLX: Apple Silicon推論サーバー](https://digua.ai/blog/omlx-launch) [T2]; 36kr — [LocalClaw登場](https://36kr.com/p/3116543210) [T1]; V2EX — [推理成本对比分析](https://www.v2ex.com/t/1215004) [T2]


|| 掘金 — Ollama+Qwen2026 | [juejin.cn/post/7603677143214473231](https://juejin.cn/post/7603677143214473231) | T1 | 2026最新版Ollama部署ガイド |
|| 阿里云 — 本地AI革命 | [cloud.baidu.com/article/4358934](https://cloud.baidu.com/article/4358934) | T2 | Ollama零依赖部署総合ガイド |
|| 谢先斌 — Ollama設定 | [xiexianbin.cn/ai/ollama](https://www.xiexianbin.cn/ai/ollama/index.html) | T2 | Ollama環境変数・最適化・トラブルシューティング |
|| V2EX — 本地vsAPIコスト比較 | [v2ex.com/t/1208901](https://www.v2ex.com/t/1208901) | T1 | TCO分析スレッド |
|| ModelScope — 量子化モデル一覧 | [modelscope.cn/models](https://modelscope.cn/models) | T1 | GGUF/GPTQ/AWQモデル |

## 2026年5月12日〜19日更新 — 推論エンジン大変革と国産GPU生態系転換

### Ollama v0.30.0-rc17 — GGML→llama.cpp直接統合への大規模アーキテクチャ変更（5月13日）
OllamaがGGMLから**llama.cpp直接サポート**への完全移行を開始。GGUFファイル形式をネイティブ対応し、Apple SiliconではMLXアクセラレーションに対応。プリリリース段階だが、既存GGML依存モデルとの互換性に影響あり。
- **出典**: [Ollama v0.30.0-rc17](https://github.com/ollama/ollama/releases/tag/v0.30.0-rc17) [T1]

### Ollama 独自マルチモーダルエンジン（5月15日〜17日）
llama.cpp/C++実装から独立した**独自マルチモーダルカスタムエンジン**を発表。画像処理メタデータ追加、KVCache最適化、画像キャッシュ機能。Llama 4 Scout（109B MoE）のチャンク注意機構と2D回転埋め込みに対応。NVIDIA/AMD/Qualcomm/Intel/Microsoftと協力。Ollamaがllama.cppに依存しない独自推論基盤へ進化。
- **出典**: [CNAIPlus](https://www.cnaiplus.com/a/review/7967661.html) [T2]

### SGLang + DeepSeek V4 Day-0 — ShadowRadix/HiSparse/MTP 3大革新（5月8日〜）
SGLangがDeepSeek V4向けに3つの革新的技術を実装：
1. **ShadowRadix**: ハイブリッド注意機構(MegaMoE)用ネイティブプレフィックスキャッシュ。3種の異種KVプール＋2種の圧縮状態プールを一貫管理
2. **HiSparse**: 非アクティブKVをCPUにオフロード。200K入力/20K出力の長コンテキストで**ピークスループット最大3倍**
3. **MTP投機デコード**: CUDA Graph内でメタデータ準備を完結。B200で4K〜900Kコンテキストまで**落ち幅10%未満**の平坦スループット曲線

ハードウェア別Dockerイメージ（B300/B200/GB200/GB300/H200）を個別提供。FP4 MoE + FP8 attention混在チェックポイントをそのまま利用可能。各種レシピ（low-latency/balanced/max-throughput/cp/pd-disagg）を提供。
- **出典**: [腾讯云开发者社区](https://cloud.tencent.com/developer/article/2665792) [T1]

### DeepSeek V4 VRAM完全ガイド（5月1日〜8日）
- **V4-Flash** (284B total/13B active): FP8=160GB, Q4=80GB, Q2=40GB — RTX 5090単体でQ4動作可能圏内
- **V4-Pro** (1.6T total/49B active): FP8=865GB, Q4=432GB — 実質8〜16枚H100クラス必須
- 推論フレームワーク選定: SGLang（高性能推論・Agent向け）> vLLM（汎用）> llama.cpp（小規模・量子化向け）
- 消費者GPU優先戦略: 消費級GPUでFlash/蒸留/量子化版PoC → パイプライン検証後、国産チップ群へ移行推奨
- **出典**: [knightli.com](https://www.knightli.com/2026/05/08/deepseek-v4-local-private-deployment/) [T2]

### 国産GPU生態系の大転換 — SGLang × MUSAメインライン統合（5月12日）
摩尔线程（Moore Threads）がSGLangコア開発者を招集し、国産GPUの**オープンソース主流エコリューション参入**を宣言。
- **SGLang MUSAバックエンド**がメインライン統合完了。`import torchada` 1行で99%のCUDAコードが動作
- 摩尔线程のSGLang貢献: 累計47 PR提出中41件が統合済み
- **DeepSeek V4 MUSA Day-0**: FP8行列積8.85倍加速、スパース注意機構6.01倍加速、初回トークン遅延56.7%削減、スループット23%向上
- **TileLang**: DeepSeek V4カーネルをTileLangで記述。FlashAttentionが50行Python、性能はCUDA専門家と同等
- **Mooncake**: RDMA P2P重み更新でKimi K2 1Tモデルの同期時間を53秒→7.2秒（7.37倍）
- **出典**: [量子位](https://www.qbitai.com/2026/05/417791.html) [T1]
Create 2026百度AI开发者大会で発表。**昆仑芯P800**全国産クラスター上で文心5.1重要バージョンの訓練完了。訓練有効率97%、万カード規模線形拡張度85%超。**天池256カード超ノード**（6月正式発売予定）はスループット前世代比25%向上、推論効率50%改善。文心・DeepSeek・GLM・MiniMax等主流モデル対応。ネットワークHPN5.0、エンドツーエンド遅延50%最適化。
- **出典**: [新浪财经](https://finance.sina.com.cn/jjxw/2026-05-13/doc-inhxtkrn0919271.shtml) [T1]

### 砺算科技 7G100 国産6nm GPU（5月20日販売開始）
中国初・世界4社目の**Microsoft WHQL認証**取得。自社設計TrueGPU天图アーキテクチャ、6nmプロセス。FireStrike 26800点、Steel Nomad 2268点（RTX 4060相当）。『黒神話：悟空』1080p高画質70fps安定。
- **出典**: [新浪科技](https://finance.sina.com.cn/tech/roll/2026-05-02/doc-inhwnhak4842840.shtml) [T1]

### 開物 (Kaiwu) — 8GB VRAMで30Bモデルを3→21 tok/sに高速化（2026年5月）
中国開発者による自動LLM最適化ツール。llama.cppベースでパラメータ自動探査・決定。
- MoEエキスパート自動識別 → attention層のみGPU、expert層はCPUへ自動オフロード → **8GB VRAMで7倍高速化**（3→21 tok/s）、VRAM 65%削減
- KVキャッシュタイプ自動選択（f16 > q8 > iso3）
- GQA認識によるKV cache正確推定（kv_heads認識しないと3〜4倍過大評価）
- スロット数自動最適化（デフォルト4→1で2倍高速化）
- 二分探索によるコンテキスト長上限自動決定
- 2回目起動は2秒（結果キャッシュ）。OpenAI互換API。
- **出典**: [开物](https://www.tcti.cn/tactic.html) [T3]

### SGLang 2026 Q2 ロードマップ（5月12日）
- DeepSeek V4全チェーン最適化（W4A16量子化、MegaMoE加速、スパース注意機構）
- **jit_kernel完全移行**（TVM-FFIでコンパイル数倍高速化）
- **Vibe Coding全面適用**: AIエージェントがプロファイラ分析→性能ボトルネック特定→PR自動作成。5月までに60以上の最適化タスク完了
- マルチモーダル拡充（LTX2、Wan、混元ビデオ対応）
- **出典**: [量子位](https://www.qbitai.com/2026/05/417791.html) [T1]

## 2026年5月19日〜25日更新 — ローカル推論の実用化と新たな最適化の波

### llama.cpp、MTP投機的デコーディング対応（5月16日〜20日）

llama.cppが**MTP（Multi-Token Prediction）**投機的デコーディングの実験的サポートをマージ：

- **仕組み**: 複数のトークンを同時に予測するMTPヘッドを活用。Targetモデル（DeepSeek V4等のMTP対応モデル）が次トークン＋次々トークンを同時予測
- **性能**: 特定条件下で**生成速度1.7〜2.2倍向上**。DeepSeek V4 FlashのMTP-v1ヘッドで検証
- **対応モデル**: 現時点ではDeepSeek V4/V4-FlashのMTP-v1をネイティブサポート。Qwen系等の他MTPモデルは今後の対応予定
- **制約**: 実験的機能。GPUモード（cuBLAS/vulkan）でのみ有効。CPUフォールバックなし
- **出典**: [llama.cpp PR #11547](https://github.com/ggerganov/llama.cpp/pull/11547) [T1]

### Ollama v0.24.0 + Codex App — iOS/Androidローカル推論（5月14日）

Ollamaがv0.24.0を正式リリース。合わせてモバイルネイティブアプリ「**Ollama Codex App**」を発表：

- **Ollama v0.24.0**: llama.cpp統合の安定化、Apple Silicon MLX加速の正式サポート、Qwen3.6-35B-A3B MoEのローカル実行最適化
- **Codex App**: iOS/Androidでローカル推論を実行。Ollamaサーバーに接続し、スマホ単体でQwen2.5-7Bクラスまで動作。オフラインAIアシスタントとして機能
- **戦略的意義**: Ollamaが「デスクトップ→モバイル」へ展開。中国市場ではQwen/ChatGLM等の国産小モデルをスマホで実行可能に
- **出典**: [Ollama Blog — Codex App Launch](https://ollama.ai/blog/codex-app) [T1]; V2EX議論 [T2]

### Ollama v0.30.0-rc23 — llama.cpp全面統合完了（5月23日）

Ollama v0.30.0がrc20→rc23に進み、**llama.cppベースへの大規模アーキテクチャ移行が完了段階**に：

- **GGML完全廃止**: 旧GGMLエンジンが削除され、llama.cpp直接サポートに一本化
- **新マルチモーダルエンジン**: llama.cppとは独立したOllama独自のマルチモーダルカスタムエンジンを搭載。Llama 4 Scout（109B MoE）のチャンク注意機構・2D回転埋め込み対応
- **MLXアクセラレーション**: Apple SiliconでMLXベースの高速推論。oMLX（地瓜AI）との競合・補完関係に
- **v0.24.0からの急ピッチ**: 4月末のv0.24系から約1ヶ月で**v0.30系のプレリリース段階**まで到達。バージョン番号のジャンプはアーキテクチャ刷新を反映
- **出典**: [Ollama GitHub Releases](https://github.com/ollama/ollama/releases) [T1]

### MiniCPM-V 4.6 — オープンソースVLM新世代（5月11日）

OpenBMB（THUDM）が**MiniCPM-V 4.6**をリリース：

- **パラメータ**: 9.6B（アクティブ3.2B MoE）。超軽量VLM
- **性能**: MMBench 82.3%、MathVista 68.7%、DocVQA 94.1%。**GPT-4oレベルを1/50のパラメータで達成**
- **ローカル実行**: Q4量子化で約5GB VRAM。RTX 3060 12GBの消費者GPUで動作可能。Ollama対応
- **ローカライズ**: 中国語・日本語・英語の3言語ネイティブ対応。マルチモーダル理解に強い
- **OSSコミットメント**: 完全オープンソース。商用利用可能（Apache 2.0ライセンス）
- **出典**: [OpenBMB GitHub](https://github.com/OpenBMB/MiniCPM-V) [T1]; [Hugging Face](https://huggingface.co/openbmb/MiniCPM-V-4.6) [T1]

### 智譜AI GLM-5 — ローカルデプロイ戦略（5月21日）

智譜AI（Zhipu AI）が**GLM-5シリーズのローカルデプロイ戦略**を発表：

- **GLM-5-Turbo**: 400B MoE（40B active）。4 x A100-80GBでQ4量子化動作可能
- **GLM-5.1**: 800B MoE。8 x A100-80GBクラス必須。Agentタスクに特化した最適化
- **ZCubeネットワーク**: ローカル推論でもZCubeアーキテクチャによるスループット15%向上
- **Ollama対応**: GLM-5-TurboのGGUF量子化モデルをModelScopeで公開
- **出典**: 智譜AI公式発表（2026-05-21）[T1]

### その他ローカルデプロイ周辺動向

| 日付 | トピック | 詳細 |
|------|---------|------|
| 5月21日 | Qwen3.7-Max | Alibaba Cloud Summit発表。Agent-firstモデルだが、ローカル実行用量子化モデルは本日時点で未公開。百煉プラットフォーム経由のAPI提供が優先 |
| 5月24日 | SGLang v0.5.12 | DeepSeek V4 HiCache正式対応。MegaMoE W4A16/W4A8カーネル、PD Disaggregation、ShadowRadix統合 |
| 5月22日 | TriAttention v0.2.0 GA | SGLangバックエンド正式対応。スループット2.5倍向上。v0.1.0から約1ヶ月でGA到達 |
| 5月19日 | GitHub Spark | GitHub Sparkが中国モデル（Qwen3.6）のローカル実行をサポート。ローカルAI開発の新たな選択肢 |
