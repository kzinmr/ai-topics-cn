---
title: "DeepSeek（深度求索）— 2026年最新動向"
type: concept
tags: [LLM, chinese-ai, open-source, MoE, reasoning, coding-agent]
created: 2026-04-17
updated: 2026-04-19
source_lang: zh-CN
---

# DeepSeek（深度求索）

| | |
|---|---|
| **会社** | 杭州深度求索人工智能基礎技術研究有限公司 |
| **創設** | 梁文鋒（Liang Wenfeng）率いるクオンツ系AIラボ |
| **代表モデル** | DeepSeek-V3, DeepSeek-V3.2, DeepSeek-R1, DeepSeek-V4（予定） |
| **アーキテクチャ** | 稀疏MoE（Mixture of Experts） |
| **ライセンス** | カスタムオープンライセンス（V4はApache 2.0予定） |
| **Webサイト** | [deepseek.com](https://www.deepseek.com/) |
| **GitHub** | [github.com/deepseek-ai](https://github.com/deepseek-ai) |

## 概要

DeepSeekは中国を代表するオープンウェイトLLM開発企業。2024年末のDeepSeek-V3でMoEアーキテクチャによるコスト効率の高さを示し、2025年1月のDeepSeek-R1で推論能力（reasoning）におけるGPT-o1レベルの性能をオープンソースで実現し、世界中に衝撃を与えた。2026年に入り、V3.2でAgent能力の強化、Math-V2で国際数学オリンピックレベルの推論能力を実証。次世代モデルV4は1兆パラメータ規模でのリリースが予告されている。

## モデル系列

### DeepSeek-V3（2024年12月）
- **総パラメータ**: 671B、**活性化パラメータ**: ~37B/トークン
- **コンテキスト**: 128K tokens
- **訓練ハードウェア**: Nvidia H800（輸出規制下の制限版）
- **特徴**: MoEアーキテクチャによる高いコスト効率。V2から大幅改善

### DeepSeek-V3.2（2025年12月）
- GPT-5やGemini 3と同等の性能を claiming
- Agent機能の大幅強化
- モデル無料公開（オープンウェイト）

### DeepSeek-R1（2025年1月）
- 推論特化モデル。Reinforcement LearningによるChain-of-Thought能力の獲得
- arXivで3段階トレーニングパイプラインを公開
- R1-0528（2025年5月更新版）でO4-miniに匹敵する性能

### DeepSeek-Math-V2（2025年11月）
- 数学的推論特化。国際数学オリンピック（IMO）で金メダルレベルの正答率

### DeepSeek-V4（2026年春 予定）
- **総パラメータ**: ~1T（1兆）、**活性化パラメータ**: ~37B（V3と同等）
- **コンテキスト**: 100万（1M）tokens
- **訓練ハードウェア**: 華為（Huawei）昇騰910C + Cambricon MLU（Nvidia非依存）
- **ライセンス**: Apache 2.0（予定）
- **ベンチマーク（内部リーク、未検証）**: HumanEval 90%、SWE-bench Verified 80%+
- **API価格**: $0.30/MTok（推定）

## 新アーキテクチャ: mHC + Engram

DeepSeek V4の最大の特徴は2つの新アーキテクチャ革新:

### mHC（流形制約超接続 / Manifold-constrained Hyper-Connectivity）
2025年末に発表。大モデルのパラメータが千亿（100B）規模に拡張した際の「信号爆発」問題を解決。
- 信号ゲインを約1.6倍に厳密に制御
- 超巨大モデルの学習安定性と推論信頼性を両立
- 「算力（計算力）依存」から「アルゴリズム効率」へのパラダイムシフトを象徴

### Engram（条件記憶メカニズム）
計算と記憶の分離が核心。
- **静的知識**（歴史的事実、コード文法）を拡張可能な巨大検索テーブルに格留
- **動的推論能力**（論理分解、バグ修正）はニューラルネットワーク重みに保持
- ハッシュインデックスによる直接「表引き」で知識取得、冗長パラメータの活性化を回避
- 推論効率3倍向上、GPU HBM（高帯域幅メモリ）依存度を大幅低減
- Needle-in-a-Haystackテスト: 100万tokensで97%精度（内部ベンチマーク）

**意義**: Engramにより、1兆パラメータモデルでありながら活性化は37Bに抑えられ、Nvidia非依存の国産チップ（華為昇騰）での訓練・推論が実現可能に。これは「算力（計算力）が性能を決める」という業界常識を覆す。

## 華為（Huawei）昇騰への対応

DeepSeek V4は、米国輸出規制下でNvidia製GPUが入手困難な状況において、**華為昇騰910C + Cambricon MLU**で訓練された最初の frontier モデルになると報じられている。

- V3はNvidia H800（H100制限版）で訓練
- V4は完全に国産チップに移行
- 成功すれば、Nvidiaハードウェアの「モート（堀）」は想像より狭いことを証明
- 昇騰910C向けの深層推論最適化により、神州数碼、拓維情報などのサーバー出荷増が予想される

## コーディング能力

V4のコーディング機能は特に注目されている:
- **HumanEval**: 90%（リーク値、独立検証待ち）
- **SWE-bench Verified**: 80%+（Claude Opus 4.5の80.9%に迫る）
- V3からの大幅改善: SWE-bench 49% → 80%+
- 50+プログラミング言語対応
- 「需求→設計→コード→デバッグ→デプロイ」全链路自動化を目標
- コード欠陥率35%低減（推定）

改善の要因として、Engramによる長コンテキスト処理能力がコードリポジトリ全体の理解を可能にし、SWE-benchが評価する「実GitHub issue解決」能力に直接寄与していると分析されている。

## 価格戦略

DeepSeekのAPI価格は業界最低水準:
- V4推定: $0.30/MTok
- 企業級コードテスト: 約$1/回（Claudeの1/68）
- 訓練コスト: 同レベルモデル比60%削減
- 中国国内の「価格戦（価格競争）」をさらに加速させる可能性

## センシティブトピックに関する懸念

2025年12月、DeepSeekモデルは中国共産党がセンシティブと扱うプロンプトに対して脆弱性を含むコードを出力する可能性が高まるとの指摘があった（GIGAZINE報道）。また、米国政府高官はDeepSeekがオープンソースの範囲を超えてユーザーデータを中国政府に提供し軍事・諜報活動を支援していると発表している。

## 関連エンティティ

- [[concepts/qwen]] — Alibabaの対抗モデル
- [[concepts/chatglm]] — 清華大学系Zhipu AIのモデル
- [[concepts/china-gpu-restrictions]] — 米国GPU輸出規制と国産チップ
- [[concepts/china-local-deployment]] — 国産モデルのローカル展開
- [[concepts/vram-optimization]] — VRAM最適化技術

## 出典

- [DeepSeek V4 Specs & Benchmarks (NxCode)](https://www.nxcode.io/zh/resources/news/deepseek-v4-release-specs-benchmarks-2026)
- [DeepSeek V4 技術前瞻 (CSDN/昇騰)](https://hwcomputing.csdn.net/69e099c254b52172bc6a500a.html)
- [DeepSeek V4架构革命: mHCとEngram (鲸林向海)](https://www.itsolotime.com/archives/20732)
- [DeepSeek V4 リリース予定 (GIGAZINE)](https://gigazine.net/news/20260114-deepseek-next-flagship-ai-model-v4/)
- [DeepSeek V4 1Tパラメータ (知乎)](https://zhuanlan.zhihu.com/p/2010446486454943846)
- [EvoLink.AI DeepSeek V4 Release Window](https://evolink.ai/zh/blog/deepseek-v4-release-window-prep)
- [Reuters: DeepSeek to launch new AI model](https://www.reuters.com/technology/deepseek-launch-new-ai-model-focused-coding-february-information-reports-2026-01-09/)
