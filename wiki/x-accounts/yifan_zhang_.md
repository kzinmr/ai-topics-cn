---
name: "Yifan Zhang"
handle: "@yifan_zhang_"
url: "https://x.com/yifan_zhang_"
category: "researcher-engineer"
followers: "8.3K"
joined: "October 2022"
bio: "PhD at @Princeton University, Princeton AI Lab Fellow. LLM Reasoning & RL, Language Modeling & Pretraining. Prev @Seed"
---

# Yifan Zhang (@yifan_zhang_)

**カテゴリ:** researcher-engineer  
**フォロワー:** 8.3K  
**投稿数:** 617  
**参加:** October 2022

## プロフィール

- **PhD Candidate** at Princeton University, Princeton AI Lab Fellow
- 指導教官: Prof. Mengdi Wang, Prof. Andrew Yao (姚期智), Prof. Quanquan Gu
- 研究分野: LLM Reasoning & Reinforcement Learning, Language Modeling & Pretraining, Attention Mechanisms, Model Architectures
- 既往: Seed Foundation Model Team (ByteDance) Top Seed research intern, UCLA AGI Lab 客員PhD
- ウェブサイト: [YFZ.ai](https://yfz.ai/)
- GitHub: [yifanzhang-pro](https://github.com/yifanzhang-pro) (314 followers)
- 所在地: New York Metropolitan Area
- 学歴: Tsinghua University (学士), Princeton University (博士課程)

## 主要プロジェクト

### MathCode
- 数学定理の自動形式化・証明AIエージェント
- 自然言語で数式を入力 → Lean 4での形式化 → コンパイル・チェック・修復ループによる証明
- v0.0.2ではCodexをデフォルトエンジンに採用、Claude API対応
- GitHub: [math-ai-org/mathcode](https://github.com/math-ai-org/mathcode)
- "Math is the frontier of superintelligence" — 理論研究の完全自律型エージェントシステムを目指した構想

### TPA (Tensor Product Attention)
- NeurIPS 2025 Spotlight (Top 3%)
- GQAとMLAより高性能かつ高速な新しいattentionメカニズム
- arXiv: [2501.06425](https://arxiv.org/abs/2501.06425)
- GitHub: [tensorgi/TPA](https://github.com/tensorgi/TPA)
- 共著: Yifan Zhang*, Yifeng Liu*, Huizhuo Yuan, Zhen Qin, Yang Yuan, Quanquan Gu, Andrew C Yao

### GRAPE (Group Representational Position Encoding)
- ICLR 2026 採択
- 新しい位置エンコーディング手法
- arXiv: [2512.07805](https://arxiv.org/abs/2512.07805)
- GitHub: [model-architectures/GRAPE](https://github.com/model-architectures/GRAPE)
- 共著: Yifan Zhang, Zixiang Chen, Yifeng Liu, Zhen Qin, Huizhuo Yuan, Kangping Xu, Yang Yuan, Quanquan Gu, Andrew C Yao

### RPG (KL-Regularized Policy Gradient for LLM Reasoning)
- ICLR 2026 採択
- LLM推論のためのKL正則化ポリシー勾配アルゴリズムの設計
- DeepSeek V3.2 と Thinking Machines Tinker にも参照
- arXiv: [2505.17508](https://arxiv.org/abs/2505.17508)
- GitHub: [complex-reasoning/RPG](https://github.com/complex-reasoning/RPG)

### Deep Delta Learning
- 2025年、arXiv: 2601.00417
- 共著: Yifan Zhang, Yifeng Liu, Mengdi Wang, Quanquan Gu (Princeton & UCLA)

### MiniMax M2 技術分析 (Oct 2025)
- 230Bパラメータ、10BアクティブパラメータのSparse MoEモデル (Hailuo AI)
- **GPT-OSS類似構造**: Full AttentionとSliding Window Attention (SWA)のインターリーブ
  - グローバルコンテキストとローカルウィンドウの併用による効率化
  - Gemma 3と同様のアプローチ
- **Per-layer QK Norm**: 各attentionヘッドが固有の学習可能RMSNormを持つ
  - Sebastian Raschkaが「LLM Architecture Gallery」で独立項目として言及
  - 従来の共有QK-Normからヘッド固有への進化
- **独立したRoPE設定**: Full Attention部とSWA部がそれぞれ独自のRoPE theta設定
- **FlashAttentionの優位性**: 低精度学習・推論（FP8/FP4）においてFlashAttentionが線形Attentionより効果的であることを強調
- 投稿は439Kビュー、584いいね、313ブックマークを獲得
- 「AI Labs are doing real science, instead of Pride and Prejudice!」

### AutoMathText
- ACL 2025 Findings 採択
- Zero-shot生成的分類器による数学テキストの自律的データ選択
- arXiv: [2402.07625](https://arxiv.org/abs/2402.07625)
- GitHub: [yifanzhang-pro/AutoMathText](https://github.com/yifanzhang-pro/AutoMathText)

### Cumulative Reasoning
- TMLR 採択
- 大規模言語モデルによる累積推論
- arXiv: [2308.04371](https://arxiv.org/abs/2308.04371)
- GitHub: [iiis-ai/cumulative-reasoning](https://github.com/iiis-ai/cumulative-reasoning)

### GPM (General Preference Model)
- ICML 2025 採択
- Bradley-Terryモデルを超える一般的な言語モデルアライメント用Preferenceモデル
- arXiv: [2410.02197](https://arxiv.org/abs/2410.02197)
- GitHub: [general-preference/general-preference-model](https://github.com/general-preference/general-preference-model)

### FlashSampling
- 高速かつメモリ効率的な正確サンプリング手法
- arXiv: 2603.15854
- 共著: Tomas Ruiz*, Zhen Qin*, Yifan Zhang†, Xuyang Shen, Yiran Zhong, Mengdi Wang†

### Seed 2.0
- ByteDance Seed Foundation Model Team 参加
- 技術レポート: Seed2.0 Model Card — 「Towards Intelligence Frontier for Real-World Complexity」

## 最近の投稿傾向 (2026年4月時点)

- **Minimax M2 技術分析**: GPT-OSS類似構造（Full Attention + Sliding Window Attentionのインターリーブ）、各attentionヘッド固有のlearnable RMSNorm (per-layer QK-Norm)、Full/SWA部で独立したRoPE theta設定、低精度(FP8/FP4)でのFlashAttention優位性を指摘。439K views, 584 likes, 313 bookmarks
- **TPA NeurIPS Spotlight 発表**: Tensor Product Attentionの採択を報告 (Oct 2025)
- **MathCode V4**: "V4, next week" — 次世代数学証明エージェントのリリース予告 (pinned post, 393 likes, 615K views)
- **Gram Newton-Schulz**: Muonの最適化手法を2倍高速化した数学的等価計算手法の紹介
- **数学的形式証明**: 「Math is the frontier of superintelligence. It always has been, and it always will be.」— 自律型理論研究エージェントへのビジョン発信

## 関心分野

- LLM Reasoning & Reinforcement Learning
- Tensor Product Attention / Attention Mechanisms
- 数学的定理自動証明 (Lean 4)
- Model Architecture Design
- データキュレーションと事前学習
- General Preference Models
- AI Safety and Alignment

## 関連

- [[yifanzhang-pro]] — GitHub組織: math-ai-org, tensorgi, complex-reasoning, model-architectures, general-preference, iiis-ai
- [[mengdi-wang]] — 指導教官 (Princeton)
- [[andrew-yao]] — 指導教官 (Tsinghua/Princeton)
- [[quanquan-gu]] — 指導教官 (UCLA)
- [[skyler-miao]] — Minimax関連で言及

## ソース

- https://yfz.ai/
- https://github.com/yifanzhang-pro
- https://x.com/yifan_zhang_
- https://github.com/math-ai-org/mathcode
- https://github.com/tensorgi/TPA
- https://github.com/complex-reasoning/RPG
