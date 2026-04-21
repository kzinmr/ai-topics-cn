---
title: "mini-cc — 轻量级AI编程智能体核心框架"
created: 2026-04-19
updated: 2026-04-19
tags: [coding-agents, ai-agents, llm, open-source, china]
aliases: ["mini-cc", "轻量级编程Agent"]
source_lang: zh-CN
---

# mini-cc — 轻量级AI编程智能体核心框架

## 概要

mini-cc是一个完全使用TypeScript编写的轻量级AI编程Agent核心框架，采用纯函数式编程范式，精简了大模型、工具系统、记忆上下文与事件循环。

## 核心特性

### 1. 多模型兼容

| 模型类型 | 支持情况 |
|---------|---------|
| Claude (Anthropic API) | 原生支持 |
| OpenAI兼容模型 | 原生支持 |
| 国产模型（Qwen/DeepSeek/Kimi） | 完美适配 |

切换方法：修改`.env`环境变量即可一键切换底层大脑。

### 2. 沉浸式「思考」体验

- **流式输出**：告别漫长等待
- **思维链(CoT)可视化**：实时呈现AI推导和思考过程
- **推理模型深度适配**：支持Qwen-Max、DeepSeek-R1等带`reasoning_content`的模型

### 3. Tool Use系统

- **BashTool**：终端执行权限，帮你自动`npm install`、`git commit`、运行测试等
- **FileReadTool**：读取本地代码库，支持突破长度限制的智能截断
- **安全沙盒**：高危命令被有效拦截

## 技术架构

```
mini-cc
├── 模型抽象层（多模型兼容）
├── 工具系统（Tool Use）
├── 记忆上下文管理
└── 事件循环（核心驱动）
```

- **语言**：TypeScript
- **编程范式**：纯函数式（Functional Programming）
- **设计理念**：摒弃复杂历史包袱，精简到极致

## 与其他框架对比

| 框架 | 定位 | 复杂度 |
|------|------|--------|
| [[claude-code|Claude Code]] | 生产级完整方案 | 高 |
| [[openclaw|OpenClaw]] | 多智能体协作 | 中高 |
| **mini-cc** | 轻量核心框架 | 低 |
| [[cursor|Cursor]] | IDE集成 | 中 |

## 适用场景

- 学习Agent原理（轻量可改造）
- 自建编程智能体（替换Claude Code作为核心）
- 嵌入式集成（TS项目中的Agent能力）

## 出处

- **V2EX**: [mini-cc：打造你的专属轻量级AI编程智能体](https://www.v2ex.com/t/1206969) | 2026-04-19 | score:3
- **tags**: `Qwen`, `智能体`, `Claude`, `AI`, `OpenAI`, `Kimi`, `DeepSeek`, `通义千问`, `大模型`, `Tool Use`, `推理`