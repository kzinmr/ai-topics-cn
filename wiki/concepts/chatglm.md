---
title: "ChatGLM (智谱清言) — Zhipu AI"
type: concept
tags: [LLM, chinese-ai, open-source, agent, zhipu, multimodal]
created: 2026-04-20
updated: 2026-04-30
aliases: ["智谱清言", "GLM-4", "GLM-5", "GLM-5.1", "GLM-5-Turbo", "Zhipu AI", "智谱AI"]
source_lang: zh-CN
---

# ChatGLM (智谱清言) — Zhipu AI

|| | |
|---|---|---|
| **開発元** | 北京智谱华章科技股份有限公司（Zhipu AI） |
| **設立** | 2019年（清華大学知識工研究室出身） |
| **上場** | 香港交易所 02513.HK |
| **代表モデル** | GLM-5, GLM-5.1, GLM-4.7, GLM-4.6V, GLM-PC |
| **アーキテクチャ** | GLM（General Language Model）独自アーキテクチャ |
| **开源** | GLM-4.7、GLM-4.6V、CogAgent-9B 等开源済み |
| **最新モデル** | GLM-5、GLM-5.1、GLM-5-Turbo |
| **プラットフォーム** | [chatglm.cn](https://chatglm.cn/)、[open.bigmodel.cn](https://open.bigmodel.cn/)、[z.ai](https://z.ai) |
| **ウェブサイト** | [zhipuai.cn](https://www.zhipuai.cn/zh) |

## 概要

智谱（Zhipu AI）は清華大学知識工研究室を渊泉とする中国発の大手独立LLM企業。2025年3月31日に香港上場（02513.HK）を果たし、中国大型独立LLM厂商として初の上場企業となった。GLM系列の独自アーキテクチャ基础上に、GLM-5では**智能体工程（Agent Engineering）**に特化した训练てコーディング・Agent能力开源SOTAを実現。OpenClaw（AutoClaw）のローカルPC Agent製品や、智谱清言のコンシューマーAIアシスタントなど、B2CとB2B両面で展开。

## モデル系列

### GLM-5（2026年2月） / GLM-5.1（2026年4月7日）

- **GLM-5**: 智谱面向智能体工程推出的全新旗舰基座モデル
  - **総パラメータ**: 744B MoE、活性化パラメータ約40B
  - **訓練ハードウェア**: 華為昇騰（Nvidia不使用）
  - SWE-bench Verified、Terminal Bench 2.0 等**开源SOTA、比肩 Claude Opus 4.5**
  - 工具调用（Function Calling）与长链路执行能力大幅強化
  - **开源**: 权重公開済み

- **GLM-5.1（2026年4月7日リリース、MITライセンス）**: GLM-5のLong-Horizon Task（長程タスク）特化改良版
  - **コンテキスト**: 200K tokens、**最大128K出力**
  - **8時間自律実行**: 単一コードタスクに対し最大8時間連続動作。計画・実行・テスト・最適化を自律ループ
  - **655回以上反復、6,000回以上のツールコール**で戦略を自己修正
  - **デモ実績**: 8時間で完全なLinuxデスクトップ環境（ファイルブラウザ・ターミナル・テキストエディタ・システムモニタ・計算機・ゲーム）をゼロから構築
  - **戦略的自己変化**: 反復〜90回目で全データ探索からクラスタリング手法に、〜240回目で2段階パイプラインに移行。全実行中に6回の構造的戦略シフト
  - **KernelBench Level 3**: 実MLワークロードで3.6xの幾何平均高速化
  - **API価格**: $1.00/百万tokens（入力）、$3.20/百万tokens（出力）
  - **LLMエージェント連携**: Claude Code、OpenClaw、Cline等のOpenAI互換コーディングツールと直接統合可能
  - **ローカル推論**: vLLM/SGLang対応、GitHubにセットアップガイド公開
  - **重み**: HuggingFaceとModelScopeでMITライセンス公開（FP8版も同時公開）

  **ベンチマーク比較**:
  | ベンチマーク | GLM-5.1 | GPT-5.4 | Claude Opus 4.6 | Gemini 3.1 Pro |
  |-------------|---------|---------|----------------|---------------|
  | SWE-Bench Pro | **58.4%** | 57.7% | 57.3% | — |
  | CyberGym | **68.7** | 拒否ケースあり | 拒否ケースあり | 拒否ケースあり |
  | Humanity's Last Exam | 31.0% | 39.8% | — | **45.0%** |
  | GPQA-Diamond | 86.2 | **92.0** | — | **94.3** |
  | Vending-Bench 2（収益） | $5,634 | — | **$8,018** | — |

  **制約（公式発表より）**:
  - デッドエンド（行き詰まり）の早期認識が必要
  - 数千回のツールコール後に一致性を維持する課題
  - 明確な成功指標がないタスクでの自己評価の信頼性
  - 総合コードスコアではOpus 4.6の約94.6% — 推理力・創造的タスクにはなお隔たり
  
- **GLM-5V-Turbo（2026年4月2日）**: 視覚・動画からコード生成可能なマルチモーダルコーディングモデル
  - 画面イメージ/動画から直接コード生成
  - AIエージェントに「目」を与えることがコンセプト
  - OpenClaw基盤モデルとしても機能

### GLM-4.7（2024年主力开源モデル）

- 智谱清言の后台モデル
- テキスト生成・写作・编程・画像理解対応
- 128K长上下文

### GLM-4.6V（开源视觉推理モデル）

- **100B级开源视觉推理モデル**として全球效果出众
- 原生支持工具调用（Function Calling）
- 自动完成任务
- 128K长上下文
- **开源**: 权重公開済み

### CogAgent-9B（PC Agent基座モデル / 2024年12月开源）

- GLM-PCの基座モデル
- 屏幕截图のみでHTML等のテキスト情報 없이動作
- PC操作自动化の核心モデル
- **开源**: [github.com/THUDM/CogAgent](https://github.com/THUDM/CogAgent)

## Agent製品

### AutoGLM

- 自主规划・推理・执行能力を持つAgentモデル
- 任务规划・データ希少・策略最適化の問題解决
- **持续自我改进能力**を持つのが特长
- 2024年11月のAgent OpenDayで发布
- 50步骤以上の长步骤操作、跨app実行に対応

### AutoClaw（澳龙 / 2025年发布）

- 国内首款一键安装の本地OpenClaw客户端
- 内置 **50+ Skills**
- AutoGLM浏览器操作能力集成
- 下载地址: autoclaw.zhipuai.cn
- PC上のあらゆる操作を自動化できる小龙虾形状のAgent

### GLM-PC（2024年11月内测）

- 「像人一样操作计算机」の目标
- 画面截图だけでPC操作（跨应用、ファイル操作等）
- CogAgent-9Bが基座

### z.ai（2026年新プラットフォーム）

- 智谱の新しい統一プラットフォーム
- GLM-5旗舰モデル、薄切りAPI服务
- AutoClaw・智谱清言・AutoGLM・Zread.ai等を統合
- 2026年4月時点で運用開始
- MCP（Model Context Protocol）対応を公式サポート
- RAG統合の知识库機能
- 10分钟で完了するモデル微调サービス
- 智能体市场で精选智能体、千行百业対応

## 上市公司としての智譜（2025年度業績）

- **株式コード**: 02513.HK（香港証券取引所）
- **2025年度業績（2026年3月31日発表、上場後初）**:
  - **総収入**: 7.24億元（前年比+131.9%）
  - **粗利**: 2.97億元（前年比+68.7%）
  - **調整後純損失**: 31.82億元（前年比+29.1%）
  - **MaaSプラットフォームARR**: 約17億元（前年比60倍増）
  - **MaaS API粗利率**: 18.9%（前年比約5倍改善）
  - **中国トップ10インターネット企業中9社がGLMを深層統合**
  - **登録ユーザー**: 400万突破
  - **サービス対象国**: 218以上の国と地域
- **2026年Q1 API値上げ83%** → **呼び出し量400%増**（量価同時上昇）
- 中関村自主大模型産業連盟の理事長単位
- **登録資本金**: 1.5億元超
- **株価動向（2026年4月）**: GLM-5.1発表翌日に11.49%高→868HK$、時価総額3,872億HK$
  - DeepSeek V4値下げ競争の影響で4月27日914.5HK$（-2.19%）

## コーディング能力

GLM-5のコーディング能力は开源モデル最高の座を争う:

- **SWE-bench Verified**: 开源SOTA、Claude Opus 4.5比肩
- **Terminal Bench 2.0**: 智能体编程核心榜单开源SOTA
- **GLM-5.1**: 2000万Tokens無料登録でCoding・智能体・数理推理・PPT生成の全能型
- CodeGeeX（智谱発）も同時に展开 — Intelとの協業でAIPC版提供済み

## プラットフォーム機能（bigmodel.cn / z.ai）

| 機能 | 説明 |
|------|------|
| **智能体市场** | 精选智能体、千行百业対応 |
| **联网搜索** | リアルタイムWeb検索統合 |
| **MCP** | Model Context Protocol対応（2026年4月正式サポート） |
| **知识库** | RAG統合 |
| **模型微调** | 十分钟で微调完了 |

## 2026年4月最近の動向

### Coding Plan無制限週次クォータ廃止（2026年4月30日）

4月22日、智譜AIはGLM Coding Planの「無制限週次クォータ」サブスクリプションプランの自動更新を2026年4月30日午前10時（北京時間）をもって停止すると発表。過剰な使用量増加により旧プランの持続が困難と判断。影響を受けるユーザーには2ヶ月分の新プラン相当の補償を提供。

### OpenClaw・Hermes・SillyTavernがGLM Coding Plan正式対応

智譜AI製品マネージャーのLi氏が、OpenClaw、Hermes、SillyTavernの3プロジェクトをGLM Coding Planの正式サポート対象として発表。その他のツールは個別ケースごとに評価。

### Z.aiブランディング

海外市場では「Zhipu AI」から「Z.ai」へのブランド統一を推進中。z.aiプラットフォームはすでに運用開始。

### DeepSeek V4との競合

DeepSeek V4の大幅値下げ（出力$0.87/百万tokens vs GLM-5.1の$4.4/百万tokens）により短期的な株価影響を受けたが、GLM-5.1の8時間自律コード実行能力は独自のポジショニングを確立。CEO張鵬は「Tokenの質が価格を決める」と、量的競争ではなく質的差別化戦略を強調。

## 関連コンセプト

- [[concepts/deepseek]] — 競合・比較対象
- [[concepts/qwen]] — Alibabaの対抗モデル
- [[concepts/china-ai-agent-ecosystem]] — 智谱のAgentプラットフォーム位置づけ
- [[concepts/dify]] — 智谱も対応するオープンソースLLMOps
- [[concepts/mcp]] — GLMのMCP対応

## 出典

- [Zhipu AI 公式サイト](https://www.zhipuai.cn/zh)
- [BigModel.cn Open Platform](https://open.bigmodel.cn/)
- [智谱清言](https://chatglm.cn/)
- [GitHub: THUDM/GLM-4](https://github.com/THUDM/GLM-4)
- [GitHub: THUDM/CogAgent](https://github.com/THUDM/CogAgent)
- [LLM-Red-Team/glm-free-api](https://github.com/LLM-Red-Team/glm-free-api) — GLM-4-Plus逆向API