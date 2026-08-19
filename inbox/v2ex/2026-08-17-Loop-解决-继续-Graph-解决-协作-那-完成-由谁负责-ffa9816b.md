---
title: "Loop 解决“继续”， Graph 解决“协作”，那“完成”由谁负责？"
source: v2ex
url: "https://www.v2ex.com/t/1235026"
author: "Exia2"
date: 2026-08-17
score: 0
tags: ["大语言模型", "智能体", "AI", "LLM", "Claude", "ai", "推理"]
---

# Loop 解决“继续”， Graph 解决“协作”，那“完成”由谁负责？

从 Loop 到 Graph ，然后呢？
2026 年 7 月，Peter Steinberger 发了一条很短的帖子：

Are we still talking loops or did we shift to graphs yet?

这句话引发了近期关于 Loop 与 Graph Engineering 的讨论。
AnyPal 是一个面向软件工程的 Agent Harness ，目标是让 AI 参与需求拆解、任务执行、代码修改、测试验证、问题处理以及最终交付。 在实际开发过程中，我们逐渐发现，当 Agent 开始承担更长、更复杂的工程任务后，单纯让它“继续运行”并不能解决所有问题。
这个问题也正好对应了我们开发时遇到的一个实际问题：让 Agent 持续运行，与让复杂软件工程真正完成，并不是一回事。
Loop 解决持续行动，Graph 解决多个执行单元的拆分、并行与协作。但当任务跨越多个文件、模块和会话后，还需要处理依赖、状态、验证、冲突以及“什么才算完成”等问题。
AnyPal 的实践因此逐渐形成了一套分层机制：Loop 负责局部行动，Goal 负责会话内工作，Graph 负责运行时编排，而 Plan 、Issue 、依赖关系、Session 、Nudge 、Adversary 和验证证据负责维护更长期的工程状态。
本文不讨论 Loop 和 Graph 谁更先进，也不给 Graph Engineering 下行业定义，而是讨论：
如果 Loop 解决了“继续做”，Graph 解决了“怎么协作”，那么复杂软件工程中的“完成”，应该由什么来保证？
AnyPal：面向复杂工程的确定性交付体系
助推器、软件工程级逐级分解、依赖并行、会话隔离，以及与 Graph Engineering 的对照
摘要

…(内容已截断)

## 涉及话题
- 大语言模型
- 智能体
- AI
- LLM
- Claude
- ai
- 推理

[原文链接](https://www.v2ex.com/t/1235026)
