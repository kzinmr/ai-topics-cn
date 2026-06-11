---
title: "[开源] 《织经》—— Claude Code Workflows 深度剖析， 29 章实战手册"
source: v2ex
url: "https://www.v2ex.com/t/1216289"
author: "attention"
date: 2026-05-28
score: 1
tags: ["AGI", "CLAUDE", "Claude", "agi", "MCP", "AI Agent", "claude"]
---

# [开源] 《织经》—— Claude Code Workflows 深度剖析， 29 章实战手册

「经之以天，纬之以地。」—— 《左传·昭公二十八年》

两千年前，织工以经线为骨、纬线为肉，一梭一梭织就锦缎。经，是结构——纵贯始终、张紧不移；纬，是功能——穿梭其间、变化万千。

今天，编排 AI Agent 亦复如是：meta 与 phase 是「经」——确定性的结构骨架，预先张紧、不可动摇； agent()、parallel()、pipeline() 是「纬」——在骨架中穿梭执行的智能单元。经线决定流水线的形状，纬线填入真正的工作。

本书因此得名 —— 织经。


━━━━━━━━━━━━━━━━━━━━━━━━━━━━

一、CLAUDE_CODE_WORKFLOWS 是什么

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Claude Code 新增了一个实验性特性：Workflows 。需要在 claude code v2.1.148+ 的版本中通过 ultrawork 命令调用。

Claude Code Workflows 的核心思路很简单 —— 用户通过一段纯 JavaScript 脚本，用 agent() / parallel() / pipeline() / phase() 这几个原语，确定性地编排多个 subagent 。能 git 管理、能分享、能断点续传。

这和我们以往在 claude code 中用 Subagents / Agent Teams / Skills / MCP 都不一样。之前的多 agent 方案，要么靠提示词去「请求」模型调度（模型会跳步、会忘、会跑偏），要么社区自己造轮子模拟控制流。Claude 官方的 Workflows 直接把编排逻辑从提示词里拿出来，放进了「确定性代码」。


…(内容已截断)

## 涉及话题
- AGI
- CLAUDE
- Claude
- agi
- MCP
- AI Agent
- claude

[原文链接](https://www.v2ex.com/t/1216289)
