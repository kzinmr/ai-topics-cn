---
title: "Daniel Han (@danielhanchen)"
created: 2026-04-18
updated: 2026-04-18
tags: [person, llm, fine-tuning, open-source-ai, quantization, gpu-optimization, unsloth]
aliases: ["danielhanchen", "Daniel Han", "UnslothAI"]
source_lang: en
---

# Daniel Han (@danielhanchen)

@UnslothAI 創設者・CEO。YC S24出身。元NVIDIA MLエンジニア。LLMのファインチューニングと推論最適化の第一人者。Unslothを通じてオープンソースAIの民主化を推進。

## プロフィール

| 項目 | 詳細 |
|------|------|
| ハンドル | @danielhanchen |
| 名前 | Daniel Han |
| 所属 | UnslothAI (CEO & Founder) |
| Xフォロワー | 31.9K |
| X投稿数 | 3,304 |
| アカウント作成 | 2016年4月 |
| 所在地 | サンフランシスコ、カリフォルニア |
| GitHub | [danielhanchen](https://github.com/danielhanchen) — 1.9k followers |
| ウェブサイト | [unsloth.ai](https://unsloth.ai) |
| LinkedIn | [danielhanchen](https://www.linkedin.com/in/danielhanchen/) |
| AI focus year | 2023+ |

## 自己紹介（X bioより）

> Building @UnslothAI . Faster RL / training. LLMs bug hunter. OSS package. YC S24. Prev ML at NVIDIA. Hyperlearn used by NASA. San Francisco

「UnslothAIを構築中。より高速なRL/トレーニング。LLMバグハンター。オープンソースパッケージ。YC S24出身。元NVIDIA MLエンジニア。HyperlearnはNASAで使用。」

## 経歴

- **UnslothAI** — 創設者 & CEO（2024年〜現在）
  - Y Combinator S24バッチ
  - オープンソースLLMファインチューニングプラットフォーム
- **NVIDIA** — MLエンジニア（以前）
  - GPU最適化と機械学習基盤技術
- **RAPIDS cuML** — 主要コントリビューター
  - NVIDIAのGPU機械学習ライブラリ
- **Hyperlearn** — 創設者
  - 2-2000倍高速なMLアルゴリズム、50%少ないメモリ使用量
  - NASAでも使用される高性能MLライブラリ
- **Scipy, PyTorch, Pandas** — オープンソースコントリビューター

## 主なプロジェクト

### Unsloth (unslothai/unsloth)
- ローカルでのLLMファインチューニングと推論を高速化するオープンソースプラットフォーム
- 62k stars, 5.4k forks on GitHub
- Qwen3.5、Gemma、DeepSeekなどの主要モデルをサポート
- LoRA/QLoRAによる効率的なファインチューニング
- GGUFエクスポート対応（llama.cpp、Ollama、LM Studio）
- [unslothai/unsloth](https://github.com/unslothai/unsloth)

### Unsloth Studio
- モデルのトレーニング、実行、エクスポートを統合したWeb UI
- プリコンパイル済みllama.cpp + mambaバイナリで10倍高速
- bun, uvによる6倍高速インストール、ディスク使用量50%削減
- デスクトップアプリ + ショートカット起動対応

### Hyperlearn (unslothai/hyperlearn)
- 2-2000x高速なMLアルゴリズム
- 50%少ないメモリ使用量
- 新旧全てのハードウェアで動作
- NASAでも使用されている高性能MLライブラリ
- [unslothai/hyperlearn](https://github.com/unslothai/hyperlearn) — 2.4k stars

## 投稿スタイル・特徴

### 技術的詳細の共有
- **ベンチマーク重視**: MMMU、KLDなどの定量的評価を積極的に共有
- **実用的なアドバイス**: VRAM使用量、パフォーマンス改善の具体的な数値を提供
- **オープンソース擁護**: 無料・アクセス可能なAIツール開発を推進

### 採用促進・コミュニティビルディング
- **Unslothチャレンジ**: 5つの技術課題で$500K/年+エクイティの求人キャンペーン
  - 「47ポイント獲得でUnslothAIへのオファー」
  - 経験やPhDは不要、実力で評価
- **技術的専門性**: FSDP2、QLoRA、torch.compileのグラフブレーク削除など深い技術課題を出題

### 最新モデルへの迅速対応
- Qwen3.5、Llama 3.2などの新モデルリリース後すぐにファインチューニングサポートを提供
- 「Qwen3.5 can now be fine-tuned locally with Unsloth via LoRA using only 10GB VRAM」
- マルチモーダルモデルのベンチマーク比較も実施

## 最近の投稿（2026年）

### Qwen3.5 ローカルファインチューニング
> "Qwen3.5 can now be fine-tuned locally with Unsloth via LoRA using only 10GB VRAM. You can then export to GGUF for llama.cpp, Ollama, LM Studio inference! Unsloth also supports Qwen3.5‑35B‑A3B LoRA, using ~74GB VRAM (1x H100)"

10GB VRAMでQwen3.5のローカルファインチューニングを実現。GGUFエクスポートにより様々な推論エンジンで利用可能。

### Unsloth Studio アップデート
> "New Unsloth Studio update! 1. 10x faster via pre-compiled llama.cpp + mamba binaries 2. 6x faster, -50% less disk space installs via bun, uv 3. Studio is now in PATH + `unsloth studio update` works 4. Lots of UI UX improvements"

Unsloth Studioの大規模アップデート。パフォーマンスとユーザビリティの両面で大幅改善。

### Qwen3.6 量子化ベンチマーク
> "We ran Qwen3.6-35B-A3B GGUF KLD benchmarks of all our dynamic quants and other providers. 1. Nearly all Unsloth quants..."

Unslothの動的量子化技術が他社を上回るパフォーマンスを示す。

### 技術チャレンジ採用キャンペーン
> "We made 5 challenges and if you score 47 points we'll offer you $500K/year + equity to join us at @UnslothAI! No experience or PhD needed."

実力主義の採用方針。5つの技術課題:
1. nf4 / BnB 4bit を Triton に変換
2. FSDP2 を QLoRA で動作させる
3. torch.compile のグラフブレークを削除

## オンラインプレゼンス

| プラットフォーム | リンク |
|-----------------|--------|
| X (Twitter) | [@danielhanchen](https://x.com/danielhanchen) |
| GitHub | [danielhanchen](https://github.com/danielhanchen) — 1.9k followers |
| LinkedIn | [danielhanchen](https://www.linkedin.com/in/danielhanchen/) |
| ウェブサイト | [unsloth.ai](https://unsloth.ai) |
| Unsloth GitHub | [unslothai/unsloth](https://github.com/unslothai/unsloth) — 62k stars |

## 関連ページ

- [[unsloth]] — Unslothファインチューニングガイド
- [[llm]] — 大規模言語モデル
- [[fine-tuning]] — ファインチューニング技術
- [[gguf]] — GGUF形式と量子化
- [[gpu-optimization]] — GPU最適化

## 出典

| 種別 | ソース | URL |
|------|--------|-----|
| プロフィール | X @danielhanchen | https://x.com/danielhanchen |
| プロフィール | GitHub | https://github.com/danielhanchen |
| 投稿 | Yahoo Search | https://search.yahoo.com/search?p=site:x.com/danielhanchen |
| プロジェクト | Unsloth GitHub | https://github.com/unslothai/unsloth |
| ウェブサイト | Unsloth | https://unsloth.ai |
