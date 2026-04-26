---
title: "Qwen (通义千问) — Alibaba Cloud LLM"
type: concept
tags: [LLM, chinese-ai, open-source, multimodal, coding-agent, alibaba]
created: 2026-04-20
updated: 2026-04-26
aliases: ["通义千问", "Qwen3", "Qwen3.5", "Qwen-Coder"]
source_lang: zh-CN
---

# Qwen (通义千问) — Alibaba Cloud LLM

|| | |
|---|---|---|
| **開発元** | Alibaba Cloud (阿里云) |
| **代表モデル** | Qwen3-Max, Qwen3.5-Plus, Qwen3-Coderシリーズ |
| **アーキテクチャ** | Dense + MoE（Qwen3.5はMoE 3970B総パラメータ/170B活性化） |
| **オープンソース** | 400+モデル公開、Apache 2.0 / カスタムライセンス |
| **累計ダウンロード** | 10億回突破（全球）、衍生モデル超20万 |
| **ウェブサイト** | [tongyi.aliyun.com](https://tongyi.aliyun.com/) |
| **GitHub** | [github.com/QwenLM/Qwen](https://github.com/QwenLM/Qwen) |
| **コミュニティ** | 魔搭社区 (ModelScope)、HuggingFace |

## 概要

Qwen（通义千问）はAlibaba Cloudが開発する大規模言語モデルシリーズ。2023年の初代公開以降、継続的にモデル性能を向上させ、2026年のQwen3.5シリーズで**全球最強オープンソースモデル**の地位を確立した。テキスト・画像・视频のネイティブマルチモーダル対応、119言語サポート、Agent能力の大幅強化が 특징。オープンソースモデルとしての累計ダウンロード10億回という数字は、DeepSeek・Meta・OpenAIらを合計したものを上回る。

## モデル系列 (2026年版)

### Qwen3.5シリーズ（2026年2月披露）

#### Qwen3.5-Plus（开源旗舰）
- **総パラメータ**: 3970億（397B）、**活性化**: ~170億
- **アーキテクチャ**: MoE（Mixture of Experts）+ 自研ゲーティング技術（NeurIPS 2025最佳論文）
- **コンテキスト**: 最大100万（1M）tokens（视频入力対応）
- **特徴**: 原生多模态 — 視覚とテキスト混合pretrainingによりテキスト専用モデルから完全移行
- **ベンチマーク**:
  - MMLU-Pro: 87.8点（GPT-5.2超）
  - GPQA（博士級难题）: 88.4点（Claude 4.5超）
  - IFBench: 76.5点（歴代最高）
  - BFCL-V4, Browsecomp: Gemini 3 Pro超
- **推論効率**: 32Kコンテキストで8.6倍、256Kコンテキストで最大19倍高速化
- **API価格**: **0.8元/百万Token**（約0.11ドル）
- ** License**: オープンソース（开源）

#### Qwen3.5-Max（旗舰推理モデル）
- Qwen3.5シリーズ中最強の複雑任務特化モデル
- Qwen3.5-Plusより高スコア、ただし速度・コストは劣る
- 複雑な推論・分析任務向け

#### Qwen3.5-Omni-Plus（全模态原生）
- テキスト・画像・视频・音声の完全統合
- Vibe Coding能力の自然涌现

### Qwen3.6シリーズ（2026年最新）

#### リリース概要（2026年4月24日〜25日）
Qwen3.6シリーズは、Alibabaの次世代モデル群。Qwen3.5-Plusの3970億パラメータ（MoE 3970B総/170B活性化）からさらに進化。

#### Qwen3.6-Max-Preview（旗舰预览版）
- Qwen3.6シリーズの旗舰モデル（商用API経由で提供中）
- Qwen3.5-Maxの後継。より複雑な推論・分析任務に特化
- 「preserve_thinking」機能: 推論過程をユーザーに開示（DeepSeek-V4のDeep Thinkingに対抗）

#### Qwen3.6-Plus
- 视觉语言モデル。Vibe Coding体験が大幅に改善
- Qwen3.5-Plusの後継。より高速な推論

#### Qwen3.6-Flash
- 高速・低成本定位
- 数学・コード推理・空間知性が強化
- API価格: Qwen3.5-Plusよりさらに低く設定（0.8元/MTok以下）

#### Qwen3-VL-Plus
- 视觉理解特化。空間認知・マルチモーダル思考が強化

#### Qwen3-Coderシリーズ
- **最大パラメータ**: 235B（MoE、30B活性化）、最小0.6Bまで展開
- **対応言語**: 119言語・方言
- **訓練データ**: 36兆token（Qwen2.5比2倍）
- **License**: Apache 2.0
- **混合思考模式（核心功能）**:
  - **思考模式**: 複雑アルゴリズム・架构設計時に深度段階的推理
  - **非思考模式**: 简单コード生成時にミリ秒級応答
  - **智能切替**: 任務复杂度に応じて自動切り替え

### Qwen3-Max（旗舰モデル / 未开源）
- Qwen3-Max-Thinkingとして登場
- Qwen3.5-Plusよりも高性能だが速度和コストで劣る
- 商用APIとして百炼平台에서 제공

## Qwen-Coder シリーズ（2025年4月发布）

Qwen-CoderはAlibabaのコード特化モデル。

- **发布时间**: 2025年4月
- **最大パラメータ**: 235B（MoE、30B活性化）、最小0.6Bまで展開
- **対応言語**: 119言語・方言
- **訓練データ**: 36兆token（Qwen2.5比2倍）
- **License**: Apache 2.0

### 混合思考模式（核心 inovação）
- **思考模式（Thinking Mode）**: 複雑アルゴリズム・架构設計時に深度段階的推理
- **非思考模式（Fast Mode）**: 简单コード生成時にミリ秒級応答
- **智能切替**: 任務复杂度に応じて自動切り替え

### Qwen3-Coder ベンチマーク
| ベンチマーク | 性能 |
|-------------|------|
| HumanEval | ~90%（推定量） |
| SWE-bench Verified | ~75%+（推定量） |
| 対応言語数 | 119+ |

## Agent能力と生态系

### Qwen3.5のAgent機能
- **百万级Agent対応**: 非同期強化学習フレームワークで端到端3-5倍加速
- **自律操作**: スマホ・PCの自主操作（跨应用データ整理、自動化流程実行）
- **购物Agent**: 2026年1月15日发布。春節期間（6日間）で**1.2億笔注文**を処理し、世界初の大规模商業化検証を達成

### Qwen-Agentプラットフォーム
- 百炼（Bailian）平台: Qwen原生、企业级LLM服务
- Qwen-Agent SDK: エージェント開発フレームワーク
- **対応Plugin**: 淘宝、高德地图、支付宝、阿里健康等阿里エコシステム完全統合

## Qwenのオープンソース成就

| 指標 | 数値 |
|------|------|
| 累计开源モデル数 | 400+ |
| 全球ダウンロード | 10億+ |
| 月間ダウンロード上位比較 | DeepSeek〜Meta〜OpenAI〜智谱〜Kimi〜MiniMaxの合計の2-8倍 |
| 衍生モデル数 | 20万+ |
| 対応言語数 | 201言語 |

## 価格戦略

| モデル | 価格（百炼API） |
|--------|----------------|
| Qwen3.5-Plus | **0.8元/MTok** |
| Qwen3.5-Max | （非开源、商业APIのみ） |
| Qwen3.6-Flash | （高速・低成本定位） |

Qwen3.5の価格はDeepSeek-V3の低价戦略に対抗するも、国産モデル中最安値はまだDeepSeekが維持。

## 関連コンセプト

- [[concepts/deepseek]] — 競合・比較対象
- [[concepts/china-ai-agent-ecosystem]] — Qwen-Agentプラットフォーム
- [[concepts/china-ai-coding-assistants]] — Qwen-Coderの位置づけ
- [[concepts/mcp]] — Qwen-AgentのMCP対応
- [[concepts/china-open-source-ai]] — ModelScope（魔搭）生态系

## 出典

- [阿里云开发者: Qwen3.5发布 — 以小胜大，每百万Token仅0.8元](https://developer.aliyun.com/article/1713691)
- [Qwen3-Coder 公式サイト](https://www.qwen3coder.com/zh)
- [Alibaba Cloud 百炼 模型列表](https://www.alibabacloud.com/help/zh/model-studio/models)
- [知乎: 阿里千问大模型2026年最新动态：Qwen3.5系列重磅发布](https://zhuanlan.zhihu.com/p/2008846603730048341)
- [GitHub: QwenLM/Qwen](https://github.com/QwenLM/Qwen)