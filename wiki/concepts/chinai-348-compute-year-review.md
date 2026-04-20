---
title: "ChinAI #348 — 2025年中国計算力産業回顧：熱狂、成長の痛み、価値回帰"
created: 2026-04-18
updated: 2026-04-18
tags: [china, compute, gpu, semiconductor, industry-analysis, newsletter]
aliases: ["ChinAI #348", "China Compute Year in Review 2025", "中国算力産業2025年回顧"]
source_lang: zh-CN
---

# ChinAI #348 — 2025年中国計算力産業回顧：熱狂、成長の痛み、価値回帰

> **出典**: [ChinAI #348: China's Compute Year in Review](https://chinai.substack.com/p/chinai-348-chinas-compute-year-in) by Jeffrey Ding (Feb 23, 2026)
> **元記事**: 雷峰網「2025中国算力产业纪事：狂热、阵痛与价值回归」by 刘艺伦
> **重要度**: 高 — 中国GPU/半導体産業の2025年動向を網羅

## 概要

Jeffrey DingのChinAI #348（2026年2月23日）は、雷峰網（Leiphone）の劉芸倫による2025年中国計算力（算力）産業回顧記事を翻訳・解説したもの。中国のGPU・AI推論チップ・クラウドエコシステムにおける2025年の主要トレンドを4つの軸で分析している。

## 主要トピック

### 1. 一体机（All-in-One Machine）ブームの崩壊

2025年初頭、[[deepseek]]の hospitals・地方政府・軍隊への展開において「一体机」（all-in-one machine）が主要な普及手段として注目された。

- 2025年1月頃：業界会議・技術展示会・空港広告で一体机が「市場の寵児」として持て囃される
- 2025年5月（わずか4ヶ月後）：**「明日黄花」**（時代の遅れ）と化す
- 問題点：
  - ディスティールド版DeepSeekモデルのみ搭載
  - ハードウェアアップグレードなしでのソフトウェア更新が困難
  - ベンダーは短期売上重視、購入者はPR目的
  - 持続的活用には組織的・技術的投資が必要だが、多くの企業がメンテナンス能力不足で断念

> 「一体机ビジネスの真のモートは技術的プレミアムではなく、ハードウェア専門性を通じて蓄積された顧客関係とチャネルネットワークである」
> — 劉芸倫（雷峰網）

### 2. 算力リース（Compute Leasing）の狂騒と詐欺スキームの摘発

中国の計算力リース市場におけるバブルと整理：

- クラウドプロバイダーが計算力プロジェクトを内部で分割
- 一部のプロバイダーは実際の業務の20%しか請け負わないのに、財務諸表では100%の収益を計上（株価操縦目的）
- 周宇（財務リース会社GM）：「**上場企業が算力コンセプト株として自らを hype し、株価を釣り上げるのは極めて一般的だ。多くの企業は当初から計算力ビジネスを実際に開発する意図などなく、単に時価総額を2倍にする口実として使っていた**」

この問題については[[chinese-ai-compute-ecosystem]]も参照。

### 3. 中国GPU「四小龍」のIPOラッシュ — Nvidiaへの挑戦

中国のGPUスタートアップ4社が相次いでIPOを目指している：

| 企業 | 中国名 | 注目ポイント |
|------|--------|-------------|
| **Moore Threads** | 摩尔线程 | 中国GPU四小龍の一つ |
| **Muxi (MetaX)** | 沐曦 | 中国GPU四小龍の一つ |
| **Illuvatar CoreX** | 天数智芯 | 中国GPU四小龍の一つ |
| **Biren** | 璧仭科技 | 中国GPU四小龍の一つ |

> [!note] 補足（Jeffrey Ding注釈）
> - データセンターは大量のメモリチップ（DRAM, DDR4）を消費する
> - 関連記事：「八位CEO拆解正在失效的算力共识」— 算力合意の崩壊を8人のCEOが分析

**重要な戦略シフト**: これらの新興企業はNvidiaの最上位トレーニングチップとの競争ではなく、**Nvidia RTX 4090（AI推論チップ）**との競争を目指している。

> 「我々は必ず国産計算力プロジェクトを実施する。現在、国産チップ上場企業と深く議論している」
> — 算力リース会社プロジェクトマネージャー

### 4. 中国データ経済の政策実験

郭冉（Asia Society Policy Institute）の論文「Assetizing, Trading, Franchising: China's Strategy for Building a National Data Economy」が紹介された：

- **データ資産化**: 2024年1月施行、データを企業資産として認識する政策
- 2024年時点で上場企業の2%（199社）がデータ資産を計上、総額$3.09億
- 民間企業より国有企業の方がデータ資産化に積極的
- 趙志剛（中国財政科学研究院）：「**成功したテック企業（Baidu, Alibaba, Tencentなど）は、政府の行政手続きが重すぎるためデータ資源の有効活用に消極的**」

## 関連するGovAIレポート

### UAEのデータセンター建設優位性？

Amelia Michael（GovAI）のレポートは、従来の常識に反する findings を示した：

- **米国は依然としてデータセンター建設で構造的優位性を持つ**
  - エネルギーコストが（意外にも）安い
  - 自然環境がより適している
  - 国内データセンター産業が堅牢
  - 唯一の劣位：建築コストと許認可の遅延

### 推論スケーリングとAIガバナンス

Toby Ord（GovAI）の推論スケーリング分析：

- 推論時のスケーリングが急速に進むと：
  - オープンウェイトモデルの重要性が相対的に低下
  - 最初のヒューマンレベルモデルの影響が緩和
  - フロンティアAIのビジネスモデルが変化
  - 電力集約型データセンターの必要性が減少
  - トレーニング計算量閾値に依存するAIガバナンス措置が弱体化する可能性

## 関連リンク

### 内部リンク

- [[moore-threads]] — 中国GPU四小龍の一つ
- [[deepseek]] — 一体机ブームの起点となったモデル
- [[chinese-ai-compute-ecosystem]] — 中国計算力リースエコシステム
- [[gpu-sanctions-china]] — 中国GPU制限の文脈
- [[llama]] — MetaのオープンソースLLM（中国エコシステムで参照）
- [[baidu-ernie]] — Baiduの文心一言（データ資産化で言及）

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| ChinAI #348 | [substack.com/p/chinai-348](https://chinai.substack.com/p/chinai-348-chinas-compute-year-in) | T2 | 計算力産業回顧の翻訳 |
| 雷峰網原文 | [m.leiphone.com/category/industrynews/rjHHq7gP8NqXlrY5.html](https://m.leiphone.com/category/industrynews/rjHHq7gP8NqXlrY5.html) | T1 | 一体机展開の真実 |
| 郭ran論文 (ASPI) | — | T2 | 中国データ経済政策 |
| GovAI UAEデータセンター | — | T2 | データセンター建設優位性分析 |
| Toby Ord 推論スケーリング | — | T2 | AIガバナンスへの影響 |
| ChinAI #339 | [substack.com/p/chinai-339](https://chinai.substack.com/p/chinai-339-chinas-cloud-ecosystem) | T2 | クラウドエコシステム統制フェーズ |
