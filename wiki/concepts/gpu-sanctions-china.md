---
title: "中国GPU制裁・半導体輸出制限 — 米中AI競争と国産化動向"
created: 2026-04-18
updated: 2026-04-18
tags: [china, semiconductor, gpu, regulation, sanctions, nvidia, huawei, compute, geopolitics]
aliases: ["GPU制裁", "中国半導体輸出制限", "米中AIチップ競争", "中国GPU自主化"]
source_lang: ja
---

# 中国GPU制裁・半導体輸出制限 — 米中AI競争と国産化動向

> **重要度**: 高 — 中国AI産業全体に影響する地政学的要因
> **関連**: [[chinai-348-compute-year-review]], [[cambricon]], [[moore-threads]], [[huawei-ascend]]

## 概要

米国による中国向けAIチップ・半導体製造装置の輸出制限は、2022年から段階的に強化され、2025〜2026年にかけて中国AI産業の構造変化を引き起こしている。この制限は中国企業にとって短期的な打撃であると同時に、**国産GPU・AIチップの自立を加速させる**という逆説的な効果を産んでいる。

## 米国輸出制限の推移

### 2022年：最初のAIチップ禁止
- NVIDIA A100/H100など高性能GPUの対中輸出を禁止
- 軍事転用可能な技術の流出防止が目的
- 対象企業には中国軍関連機関（「国防七子」大学など）を含む

### 2023-2024年：制限の拡大
- 規制対象の拡大（H20などダウンバージョン版も制限対象に）
- 半導体製造装置の輸出管理も強化
- 中国企業が迂回ルートで入手するケースも発覚

### 2025年：全面切断への移行
- AIチップ封鎖が3段階の算力コントロールに発展
- 両側協議によるグローバル禁止条項の導入
- 華為（Huawei）の昇騰（Ascend）チップ使用を制限する条項も追加
- **NVIDIA CEO黄仁勋**：「中国市場シェア95%→0%。完全に退出した」— 約500億ドルの機会損失

### 2026年：MATCH Act（硬件技術多辺協調管制法案）
- 2026年4月2日、米国下院で正式提出
- 両党議員による推進
- **高端チップ製造装置の全面切断**を目指す
- 既存の約40カ国対象の制限を**グローバル対象に拡大**する草案
- 輸出には米商務省の許可が必要に
- **閾値**: 1,000 GPU（GB300）未満は簡易審査、超えると事前承認＋追加条件
- 200,000 GPU超の超大規模配置は、ホスト国の安全保障約束と米国AI投資の「対等」投資が条件

> **出典**: [BBC](https://www.bbc.com/zhongwen/articles/cdj88l4kw9xo/simp)、[eet-china.com](https://www.eet-china.com/mp/a485761.html)、[Bloomberg via Yahoo Finance](https://hk.finance.yahoo.com/news/%E7%BE%8E%E5%9C%8B%E6%93%9A%E6%82%89%E6%93%AC%E5%B0%87ai%E6%99%B6%E7%89%87%E5%87%BA%E5%8F%A3%E7%AE%A1%E5%88%B6%E6%93%B4%E5%B1%95%E8%87%B3%E5%85%A8%E7%90%83-%E8%BC%9D%E9%81%94%E5%92%8Camd%E5%8B%A2%E5%8F%97%E8%A1%9D%E6%93%8A-181220024.html) [T1-T2]

## 中国国産GPU/AIチップの台頭

制裁は中国の**半導体自立**を加速させている。

### 寒武紀（Cambricon）— 「中国のNVIDIA」
- 2022年の制裁後、研究開発に大幅投資
- **思元590チップ**: NVIDIA H100の8〜9割の性能
- **2025年実績**:
  - 売上高：約65億人民元（前年比+450%以上）
  - 初の本業黒字化（2024年：4.5億赤字 → 2025年：20.5億黒字）
  - チップ出荷数：2025年14.5万枚（2024年：2.6万枚）
  - 2026年3月時点で時価総額5,000億人民元
- **主要顧客**: 中国三大通信会社、Alibaba、Baidu、ByteDance
- **ゴールドマン・サックス予想**: 2030年に出荷200万枚超

> **出典**: [數位時代](https://www.bnext.com.tw/article/90629/cambricon-ai100-2026) [T2]

### 中国GPU「四小龍」— 推論チップでNvidia 4090に挑戦
[[chinai-348-compute-year-review]]で詳述。Moore Threads、沐曦（Muxi）、天数智芯（Illuvatar CoreX）などがIPOを目指し、トレーニングではなく**推論用チップ**で競争。

### 華為（Huawei）昇騰（Ascend）
- 中国国内のAIチップシェア20%に到達（IDC 2025年データ）
- 2025年中国市場AI GPU総出荷400万枚中、国産半導体165万枚

### 制裁回避の実態
- 北航、哈工大などの「国防七子」大学が、Super Microサーバー経由でNVIDIA A100を入手していたことが発覚（2026年3月）
- Super Micro関係者3名が25億ドル相当のAI技術密輸で起訴

> **出典**: [DW.com](https://www.dw.com/zh/%E5%8C%97%E8%88%AA%E5%93%88%E5%B7%A5%E5%A4%A7%E7%AD%89%E8%BF%91%E6%9C%9F%E5%85%A5%E6%89%8B%E6%90%AD%E8%BD%BD%E6%95%8F%E6%84%9F%E9%AB%98%E7%AB%AFai%E8%8A%AF%E7%89%87%E7%9A%84%E8%B6%85%E5%BE%AE%E6%9C%8D%E5%8A%A1%E5%99%A8/a-76562789) [T1]

## 中国AI産業への影響

### 短期的な課題
- 最先端トレーニング用チップへのアクセス制限
- 外国製GPUの迂回調達コスト増
- 軍事関連機関のAI研究への直接的影響

### 中長期的な構造変化
- **国産チップへのシフト加速**: 制裁が「中国版NVIDIA」育成の触媒に
- **推論重視**: トレーニングより推論用チップの開発にリソース集中
- **成熟プロセスの活用**: 先端プロセスでなくてもAIアプリケーションは運用可能
- **AI多元化輸出**: 高付加価値サプライチェーンの構築

## 関連リンク

### 内部リンク
- [[chinai-348-compute-year-review]] — 2025年中国計算力産業回顧
- [[cambricon]] — 寒武紀（中国GPU企業）
- [[moore-threads]] — 摩尔threads（中国GPU四小龍）
- [[nvidia]] — NVIDIA（制裁対象の中心企業）
- [[huawei-ascend]] — 華為のAIチップ
- [[deepseek]] — 制裁下でも低コストモデルを実現

### 外部ソース
| ソース | URL | ティア | 概要 |
|---|---|---|---|
| BBC | [bbc.com/zhongwen](https://www.bbc.com/zhongwen/articles/cdj88l4kw9xo/simp) | T1 | H200解禁と中国の慎重姿勢 |
| 數位時代 | [bnext.com.tw](https://www.bnext.com.tw/article/90629/cambricon-ai100-2026) | T2 | 寒武紀の詳細分析 |
| DW | [dw.com](https://www.dw.com/zh/北航哈工大等近期入手搭载敏感高端ai芯片的超微服务器/a-76562789) | T1 | 制裁回避の実態 |
| Bloomberg | [finance.yahoo.com](https://hk.finance.yahoo.com/news/美國據悉擬將ai晶片出口管制擴展至全球-181220024.html) | T1 | MATCH Act草案 |
| eet-china | [eet-china.com](https://www.eet-china.com/mp/a485761.html) | T2 | 150日カウントダウン記事 |
| 通信世界 | [cww.net.cn](https://www.cww.net.cn/article?id=606333) | T2 | 国産チップの「単点突破」脱却 |
