---
title: "Baidu（百度）— 文心一言/ERNIEと中国AI検索大手"
created: 2026-04-18
updated: 2026-04-18
tags: [china, llm, company, search, multimodal, erenie, open-source-ai]
aliases: ["百度", "文心一言", "ERNIE", "Wenxin", "WenXin Yiyan", "文心", "文小言", "Baidu AI"]
source_lang: ja
---

# Baidu（百度）— 文心一言/ERNIEと中国AI検索大手

> **言及数**: 6件（2026-04-18集計時点、継続増加中）
> **重要度**: 高 — 中国検索最大手、国内LLM開発のリーディングカンパニー
> **関連**: [[llama-meta]], [[gpu-sanctions-china]], [[chinai-348-compute-year-review]]

## 概要

**百度（Baidu, Inc.）**は、中国最大の検索エンジン企業であり、2026年4月現在、AIアシスタント**文心（Wenxin）**を通じて中国国内で最もアクティブなAIユーザーベースを擁している。基盤技術は自社開発の**文心大模型（ERNIE Large Model）**シリーズ。

## 企業情報

| 項目 | 内容 |
|------|------|
| **正式名称** | 百度在線網絡技術有限公司（Baidu, Inc.） |
| **創業者** | 李彦宏（Robin Li） |
| **設立** | 2000年1月 |
| **本社** | 中国・北京 |
| **主力事業** | 検索エンジン、AIアシスタント（文心）、自動運転（Apollo）、クラウド |
| **AIブランド** | 文心（旧: 文心一言 → 文小言 → 文心） |
| **基盤モデル** | ERNIE（文心大模型）シリーズ |

## ERNIE（文心大模型）の進化史

ERNIE（Enhanced Representation through kNowledge IntEgration）は、Baiduが2019年から開発する大規模言語モデルシリーズ。

| バージョン | リリース | パラメータ | 特徴 |
|-----------|---------|-----------|------|
| **ERNIE 1.0** | 2019年3月 | 110M（ベース） | 中国語に特化した事前学習、知識グラフ統合 |
| **ERNIE 2.0** | 2019年7月 | — | 継続的マルチタスク学習フレームワーク |
| **ERNIE 3.0** | 2021年 | — | 大規模知識強化言語表現 |
| **文心一言（ERNIE Bot）** | 2023年3月 | — | チャットボット版、Web＋アプリでリリース |
| **ERNIE 4.0** | 2023年10月 | — | GPT-4クラスの性能を主張 |
| **ERNIE 4.5** | 2025年3月 | 454B（MoE, アクティブ38B） | 10種類のバリエーション、マルチモーダル対応 |
| **ERNIE X1** | 2025年3月 | — | 推論特化モデル、DeepSeek-R1に対抗 |
| **ERNIE 5.0** | 2026年1月 | **2.4兆（2.4T）** | 原生全模態大モデル、40以上のベンチマークでSOTA |

## ERNIE 5.0（文心5.0）— 2026年の主力モデル

2026年1月にリリースされた**原生全模態大モデル**。2.4兆パラメータを擁し、40以上の権威あるベンチマークでGemini-2.5-ProやGPT-5-Highを上回る性能を達成。

### アーキテクチャの特徴

- **原生全模態統一建模**: テキスト・画像・音声・動画を単一の自帰納ネットワークで統合
- **超稀疏MoE**: 全2.4Tパラメータ中、Tokenあたり<3%のみをアクティブ化
- **モダリティ非依存ルーティング**: 専門家プールをモダリティ別ではなくToken特徴で動的に割り当て
- **弾性訓練（Once-For-All）**: 1回の訓練で複数のサブモデル設定を最適化

### 統一モデリングアプローチ

| モダリティ | 技術 | 説明 |
|-----------|------|------|
| テキスト | NTP + MTP | 次Token予測＋複数Token予測で推論スループット向上 |
| 視覚 | NFSP | 次フレーム・次スケール予測、画像を単一フレームのビデオとして扱う |
| 音声 | NCP | 次コーデック予測、意味内容から音響詳細まで階層的にモデリング |

### 訓練基础设施

- **フレームワーク**: 飛桨（PaddlePaddle）ベースの独自混合並列戦略
- **コンテキスト拡張**: 8K → 128Kの段階的ウィンドウ拡張
- **RLパイプライン**:
  - **U-RB**（Unbiased Replay Buffer）: 長尾分布サンプルの効率化
  - **MISC/WPSM**: エントロピー崩壊の緩和、難例最適化
  - **AHRL**（Adaptive Hint-based RL）: 段階的「思考骨格」プロンプトによる重推論タスクの足場作り

### 性能評価

- **テキスト能力**: 知識、論理推論、コード、指示追従、エージェントツール呼び出しで業界トップクラス
- **多モーダル理解**: 40以上のベンチマークでGemini-2.5-Pro、GPT-5-Highを上回る
- **画像生成**: 垂直特化モデルに匹敵する高忠実度
- **動画生成**: 業界リーディングレベル
- **音声理解**: TUT2017等で業界最佳
- **テキスト→音声**: 競争力ある性能

## 文心アプリのブランド変遷

```
2023年3月: 文心一言（Wenxin Yiyan）リリース
         ↓
2024年9月: 「文小言（Wen Xiaoyan）」に分割・ブランドアップグレード
           （百度の「新検索」スマートアシスタントとして位置付け）
         ↓
2025年11月: 「文心（Wenxin）」に再ブランドアップグレード
         ↓
2026年1月: ERNIE 5.0（2.4Tパラメータ）搭載
```

### アプリ機能

- **AI検索**: 位置ナビ、医療、専門知識、映画・文学作品、表、マインドマップ対応
- **マルチモーダル検索**: 深層検索、音声検索、画像検索、曖昧検索
- **動画通話**: リアルタイムAIビデオ通話
- **AI PPT**: プレゼンテーション自動生成
- **AIグループチャット**: 複数エージェント同時呼び出し対応
- **AI翻訳**: 多言語対応
- **コミック生成**: 写真＋説明文から複数ページコミックを生成
- **画像編集**: 多種類のスタイライズド画像処理
- **デジタルヒューマン**: 超リアルなAIアバター
- **ファイル転送**: クロスデバイス対応

## 中国AIエコシステムでの位置付け

### データ資産化との関係

[[chinai-348-compute-year-review]]で言及された郭冉（Asia Society Policy Institute）の論文によると：

> 「成功したテック企業（Baidu, Alibaba, Tencentなど）は、政府の行政手続きが重すぎるためデータ資源の有効活用に消極的」
> — 趙志剛（中国財政科学研究院）

2024年1月のデータ資産化政策施行時点でも、Baiduはデータ資産計上に慎重な姿勢を示したとされる。

### 国産チップとの連携

- ERNIE 4.5-VL-28B-A3B-ThThinkingなど一部モデルはオープンソース化
- 華為昇騰（Ascend）などの国産AIチップ上での推論最適化を推進
- GPU制裁下でもモデル開発の継続性を維持

### 市場での位置

| 指標 | 値 |
|------|-----|
| 文心アプリMAU | 2億以上（2026年1月時点） |
| 2026年春節キャンペーン | 新規ユーザー8倍増、グループチャット参加者80倍増 |
| App Store人気DL効率 | 上位4位（2026年2月14日） |

## ERNIE vs 競合モデル

| モデル | 開発元 | パラメータ | 特徴 |
|--------|--------|-----------|------|
| ERNIE 5.0 | Baidu | 2.4T（MoE） | 原生全模態、業界SOTA |
| GPT-5-High | OpenAI | — | クローズド、マルチモーダル |
| Gemini 2.5 Pro | Google | — | クローズド、マルチモーダル |
| DeepSeek-R1 | DeepSeek | 671B（MoE） | 推論特化、オープンソース |
| Qwen3-235B | 阿里雲 | 235B（MoE） | 多言語対応 |
| Claude Opus 4.7 | Anthropic | — | 推論スケーリング |
| GLM-5 | 智譜AI | 744B（MoE） | SWE-bench 77.8 |

## 関連リンク

### 内部リンク
- [[llama-meta]] — MetaのオープンソースLLM（ERNIEのベースとなった技術）
- [[gpu-sanctions-china]] — 中国GPU制限の文脈
- [[chinai-348-compute-year-review]] — 中国計算力産業回顧（Baidu言及あり）
- [[qwen]] — 阿里雲系競合
- [[deepseek]] — オープンソース競合
- [[china-ai-superapp-race]] — 中国AIスーパーアプリ競争

### 外部ソース
| ソース | URL | ティア | 概要 |
|---|---|---|---|
| ERNIE 5.0公式ブログ | [ernie.baidu.com/blog/zh/posts/ernie5.0/](https://ernie.baidu.com/blog/zh/posts/ernie5.0/) | T1 | ERNIE 5.0技術詳細 |
| 文心一言 | [yiyan.baidu.com](https://yiyan.baidu.com/) | T1 | AIアシスタント公式 |
| Baiduwiki | [baike.baidu.com/en/item/WenXin/17679](https://baike.baidu.com/en/item/WenXin/17679) | T2 | 文心百科 |
| GitHub | [github.com/paddlepaddle/ernie](https://github.com/paddlepaddle/ernie) | T1 | ERNIE 4.5公式リポジトリ |
| PR Newswire | [prnewswire.com/news-releases/baidu-unveils-ernie-5-0](https://www.prnewswire.com/news-releases/baidu-unveils-ernie-5-0-and-a-series-of-ai-applications-at-baidu-world-2025--ramps-up-global-push-302614531.html) | T2 | ERNIE 5.0グローバル展開発表 |
| Yahoo Finance | [finance.yahoo.com/news/baidu-ai-models-continue-expand](https://finance.yahoo.com/news/baidu-ai-models-continue-expand-202334075.html) | T2 | MAU 2億突破報道 |
