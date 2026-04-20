---
title: "ChatGLM (智谱清言) — Zhipu AI"
type: concept
tags: [LLM, chinese-ai, open-source, agent, zhipu, multimodal]
created: 2026-04-20
updated: 2026-04-20
aliases: ["智谱清言", "GLM-4", "GLM-5", "Zhipu AI", "智谱AI"]
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
| **开源** | GLM-4.7, GLM-4.6V, CogAgent-9B 等开源済み |
| **プラットフォーム** | [chatglm.cn](https://chatglm.cn/), [open.bigmodel.cn](https://open.bigmodel.cn/) |
| **ウェブサイト** | [zhipuai.cn](https://www.zhipuai.cn/zh) |

## 概要

智谱（Zhipu AI）は清華大学知識工研究室を渊泉とする中国発の大手独立LLM企業。2025年3月31日に香港上場（02513.HK）を果たし、中国大型独立LLM厂商として初の上場企業となった。GLM系列の独自アーキテクチャ基础上に、GLM-5では**智能体工程（Agent Engineering）**に特化した训练てコーディング・Agent能力开源SOTAを実現。OpenClaw（AutoClaw）のローカルPC Agent製品や、智谱清言のコンシューマーAIアシスタントなど、B2CとB2B両面で展开。

## モデル系列

### GLM-5 / GLM-5.1（2025年旗舰）

- **GLM-5**: 智谱面向智能体工程推出的全新旗舰基座モデル
  - SWE-bench Verified、Terminal Bench 2.0 等**开源SOTA、比肩 Claude Opus 4.5**
  - 工具调用（Function Calling）与长链路执行能力大幅强化
  - **开源**: 权重公开済み

- **GLM-5.1**: GLM-5の改良版
  - 新旗舰として注册即享2000万Tokens提供
  - Coding・智能体・数理推理・PPT生成の全能型

- **GLM-5-Turbo**: 龙虾场景（AutoClaw）向け
  - Agent核心能力の训练層深層最適化
  - 工具调用能力と长链路実行能力特化

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

## 上市公司としての智谱

- **股票代码**: 02513.HK（香港证券交易所）
- **2026年3月31日**: 智谱首份业绩报告发布（2025年度）
- 中关村自主大模型产业联盟の理事长单位
- **注册资本**: 1.5亿元超

## コーディング能力

GLM-5のコーディング能力は开源モデル最高の座を争う:

- **SWE-bench Verified**: 开源SOTA、Claude Opus 4.5比肩
- **Terminal Bench 2.0**: 智能体编程核心榜单开源SOTA
- CodeGeeX（智谱発）も同時に展开 — Intelとの協業でAIPC版提供済み

## プラットフォーム機能（bigmodel.cn）

| 機能 | 説明 |
|------|------|
| **智能体市场** | 精选智能体、千行百业対応 |
| **联网搜索** | リアルタイムWeb検索統合 |
| **MCP** | Model Context Protocol対応 |
| **知识库** | RAG統合 |
| **模型微调** | 十分钟で微调完了 |

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