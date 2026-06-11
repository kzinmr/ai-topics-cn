---
title: "Fractal Skills：给 AI Agent 一副不会过期的缰绳"
source: v2ex
url: "https://www.v2ex.com/t/1216210"
author: "tobb"
date: 2026-05-28
score: 0
tags: ["AI Agent", "coding agent"]
---

# Fractal Skills：给 AI Agent 一副不会过期的缰绳

困境
让 agent 改一个模块，信心满满地 accept。跑起来才发现：它用的是一个三个月前已经被重构掉的接口。你翻开代码仓库，发现那个接口的废弃决策其实写在某个 ADR 里，但 agent 根本没见过。
问题不在 agent 的能力，而在它的上下文。agent 做决策依赖项目级的上下文文档——AGENTS.md、设计决策记录、模块合约。但文档是人类写的，人类会忘记更新，于是文档就漂移了。决策过期了。目录级的 AGENTS.md 消失了。
Fractal Skills 是什么
Fractal Skills 是一套面向 coding agent 项目的文档编排技能组。它的核心思路很简单：软件是按层次组织的，上下文也应该按层次组织。
它定义了三层上下文协议：



层级
作用域
做什么




L1
项目根
全局拓扑、入口点、跨模块约束


L2
目录 / 限界上下文
局部所有权、作用域边界、成员模块


L3
源文件
当前合约：输入、输出、角色、不变量

你的项目不仅是代码的分层，决策记录、工程笔记、技术调研、复盘报告、任务规格都是 agent 做判断时需要的材料。Fractal Skills 用一个 docs/ 目录，给每一类文档划定了明确的 lane：
your-project/
└── docs/
    ├── decisions/        # 设计决策：当前真相，不是 ADR 坟场
    ├── engineering/      # 工程笔记：实现细节、性能数据、技术债务
    ├── research/         # 技术调研：探索、备选方案、实验记录
    ├── postmortem/       # 故障复盘：根因、修复、预防
    ├── specs/            # 任务规格：PRD → 可执行任务分组

…(内容已截断)

## 涉及话题
- AI Agent
- coding agent

[原文链接](https://www.v2ex.com/t/1216210)
