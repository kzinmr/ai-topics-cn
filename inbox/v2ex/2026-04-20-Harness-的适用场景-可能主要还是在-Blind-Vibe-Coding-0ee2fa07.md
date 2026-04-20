---
title: "Harness 的适用场景，可能主要还是在 Blind Vibe Coding"
source: v2ex
url: "https://www.v2ex.com/t/1207269"
author: "dingyaguang117"
date: 2026-04-20
score: 0
tags: ["AI", "anthropic", "ai", "AGI", "AI Agent", "gemini", "CLAUDE", "openai"]
---

# Harness 的适用场景，可能主要还是在 Blind Vibe Coding

周末的时候非技术的朋友找我帮忙看一个他 Vibe Coding 的项目，说 UI 反应特别慢，AI 给他的解释是 Steamlit 框架原理的问题。
我本着学习的态度看了下他的代码：

app.py 超过 1 万行，里面混杂了 streamlit 交互逻辑、业务逻辑，甚至还有数据库操作
没有 CLAUDE.md 、spec 等
infra 层封装了 openai 、gemini 、anthropic 三家模型调用，有 interface 但是不是每家都遵守。业务层有调用接口的，有直接调用具体实现的。
目录层级毫无规律
大量死代码

基本上是地狱级维护难度。
我突然意识到，Harness 简直就是为这种 Blind Vibe Coding 场景（不 Review 代码）而生的。 用 Harness 规则、工具替代工程师的基本素养的能力，能大大延缓 Blind Vibe Coding 的项目腐坏速度。 可能未来的技术框架，其内容可能不仅仅是代码本身，还得包含一套 Best Practice Spec / AGENTS.md. 
另一方面，我对使用 Harness 能否持续成功 Blind Vibe Coding 感到怀疑。随着需求的迭代甚至反复，即使是真人工程师在维护，项目也难免出现腐坏，更不要说还不是 AGI 的 AI Agent 。 因此重构工作的重要性，会随着时间推移逐步升高。 但重构在开始的时候，经常没有一个清晰的目标，可能要面临各种各样的权衡和妥协，对上下文的要求也更广更深。 这个过程不是对目标的收敛，而是需要先发散再收敛（这也是为什么很多插件都会有类似 /brainstorm 这个 SKILL ）。 这个过程需要 human in the loop ，否则可能永远无法实现收敛，或者收敛到一个不那么好的目标上。

…(内容已截断)

## 涉及话题
- AI
- anthropic
- ai
- AGI
- AI Agent
- gemini
- CLAUDE
- openai

[原文链接](https://www.v2ex.com/t/1207269)
