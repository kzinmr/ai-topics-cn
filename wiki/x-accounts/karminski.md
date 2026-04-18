---
title: "Karminski (karminski-牙医)"
created: 2026-04-17
updated: 2026-04-18
tags: [person, china, llm, open-source-ai, tooling]
aliases: ["karminski3", "karminski-牙医", "張旭紅", "AlphaArea"]
source_lang: zh-CN
---

# Karminski (karminski-牙医)

中国AIエコシステムの技術コメンテーター、オープンソースハードウェア愛好家、KCORES共同創設者。X(Twitter)で@karminski3として活動。

## プロフィール

| 項目 | 詳細 |
|------|------|
| ハンドル | @karminski3 |
| 本名 | 張旭紅（karminski-牙医） |
| Xフォロワー | 36.2K |
| 投稿数 | 4,610+ |
| 所在地 | アジア/北京 |
| アカウント作成 | 2018年12月 |
| 認証 | Verified account |

## 経歴

- **KCORES** 共同創設者 — 消費者向けエレクトロニクス、AI、10GbEネットワーク、家庭用NAS、ホムラボ、ヴィンテージ電子機器をカバーするオープンソースハードウェア愛好家コミュニティ
- **IllaSoft** 元ディレクター
- **KingsoftOffice** (金山軟件) 元ディレクター
- **Juejin** (掘金) 元ディレクター

## 自己紹介（X bioより）

> A coder, road bike rider, server fortune teller, electronic waste collector, co-founder of KCORES, ex-director at IllaSoft, KingsoftOffice, Juejin.

「コーダー、ロードバイクライダー、サーバー占い師、電子廃棄物コレクター」

## オンラインプレゼンス

| プラットフォーム | リンク |
|-----------------|--------|
| X (Twitter) | [@karminski3](https://x.com/karminski3) |
| GitHub | [karminski](https://github.com/karminski) |
| KCORES公式サイト | [kcores.com](https://kcores.com) |
| ブログ | [kcores.com/blog](https://kcores.com/blog) |
| Bilibili | [AlphaArea](https://space.bilibili.com/1292029) |
| YouTube | [AlphaArea](https://www.youtube.com/@AlphaArea) |
| 知乎 (Zhihu) | [karminski](https://www.zhihu.com/people/karminski/posts) |
| ベント | [bento.me/dr-karminski](https://bento.me/dr-karminski) |
| Strava | 活動中 |

## 主なプロジェクト

### KCORES LLM Arena
- 大規模言語モデルの比較・評価プラットフォーム
- URL: [llm-arena.kcores.com](https://llm-arena.kcores.com)

### Fan Lord
- Supermicro X-Seriesマザーボードのファン制御用Windows GUIツール
- プリセットファン速度調節と手動調節モードをサポート
- GitHub: [KCORES/fan-lord](https://github.com/KCORES/fan-lord)

### Core-to-Core Latency Plus
- CPUコア間通信遅延を測定するツール
- CPUキャッシュ一貫性プロトコルを使用した比較交換操作による遅延計測
- 「CPUがグルーコアかどうかを判定できる」と自称
- GitHub: [KCORES/core-to-core-latency-plus](https://github.com/KCORES/core-to-core-latency-plus)

### KCORES 大言語模型推理専用VRAMティアリスト
- GPUメモリ帯域幅に焦点を当てたVRAMランキング
- mlc-llmなどの並列フレームワークでllama-3.1-70b等のモデルを実行した際の帯域幅可用性をスコア化
- URL: [vmem-for-llms.kcores.com](https://vmem-for-llms.kcores.com/)

### ストリーミングJSON-JS
- JSONストリーミング処理ライブラリ
- GitHub: [karminski/streaming-json-js](https://github.com/karminski/streaming-json-js)

### Pineapple (菠萝语言)
- 手書きの再帰的下降パーサを持つプログラミング言語デモ
- GitHub: [karminski/pineapple](https://github.com/karminski/pineapple)

## AI関連の投稿・活動

### 半塊RTX4090で70B大言語模型を動かす
- 2024年7月19日投稿
- ChatGPT以降、「貧乏なハードウェアでLLMを動かした」系の記事が溢れる中、モデルが小さすぎたり速度が遅すぎたりする問題を指摘
- **目標**: 半分のRTX 4090予算で、70Bクラスの量子化モデルを、オンラインAIと同等の快適な会話速度で動かす
- Bilibili動画: [BV1DH4y1c7gK](https://www.bilibili.com/video/BV1DH4y1c7gK)

### KCORESフォーラム (cyberbus.net)
- AI、LLM、オープンソースハードウェアに関する議論の場
- 中国語圏の技術コミュニティとして機能

## 最近のポスト（2026年）

### PaddleOCR-VL: CVPR 2026入选
> "开年就入选CVPR, 0.9B小模型如何拿下OCR SOTA? ... 这次 Paddle 团队入选的一篇《PaddleOCR-VL: Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing》,思路非常棒"

- OmniDocBench v1.5で0.9Bパラメータ+2.5K视觉トークンで92.62の総合スコアを達成
- テキスト/数式/表/読み取りの各カテゴリで高精度

### vector-db-bench: LLMバックエンドコード能力テスト
> "主流大模型都跑完了，给大家正式带来大模型后端代码能力测试——vector-db-bench!"

- LLMがベクトルデータベース実装を書く能力をベンチマーク
- perf打火焰図をLLMに自動生成させるAgentを実装
- Gemini 3.1 Proの性能劣化を指摘: "gemini-3.1-pro performs significantly worse than gemini-3.0-pro"
- Gemini 3.1 ProはAgentタスクを早期に終了させる傾向がある

### MiMo-V2シリーズ分析
> "MiMo-V2-Pro の Agent 能力相比 MiMo-V2-Flash 提升主要体现在面向日..."

- MiMo-V2-Omniはオフィスシーン向け最適化
- Word、スプレッドシート、PPT生成を「ほぼ最終稿レベル」で実行
- 2026年高考志願智能填报デモを作成

### M2.7 オープンウェイト予告
> "M2.7 open weights coming in ~2 weeks. still actively iterating just updated a new version on yesterday — noticeably better on OpenClaw."

## 投稿スタイル・特徴

- 技術的な詳細を重視した実用的なコンテンツ
- ハードウェアとLLMの交差点に強い関心（GPU最適化、量子化、推論効率）
- オープンソース/ハードウェア愛好家コミュニティ（"垃圾佬"＝ジャンクPC愛好家）との接点
- 中国語圏の開発者視点からのAIエコシステム評論
- BilibiliやYouTubeでの動画コンテンツも制作
- ベンチマーク主導: 自らテスト環境を構築し定量比較

## 関連ページ

- [[kcores]] — KCORES組織
- [[deepseek]] — DeepSeek（KCORES LLM Arenaで評価対象）
- [[qwen]] — Qwen/通义千問（同社元雇用主のAlibaba）
- [[glm-zhipu]] — GLM/智譜AI

## 出典

| 種別 | ソース | URL |
|------|--------|-----|
| プロフィール | X @karminski3 | https://x.com/karminski3 |
| プロフィール | GitHub karminski | https://github.com/karminski |
| プロジェクト | KCORES公式サイト | https://kcores.com |
| ブログ | KCORESブログ | https://kcores.com/blog |
| 動画 | Bilibili AlphaArea | https://space.bilibili.com/1292029 |
| ベント | bento.me | https://bento.me/dr-karminski |
| オーガニゼーション | KCORES GitHub | https://github.com/kcores |
