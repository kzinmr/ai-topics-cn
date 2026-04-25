---
title: "大项目中大家真的会用 Spec-Driven Development 吗？"
source: v2ex
url: "https://www.v2ex.com/t/1208418"
author: "CodeY99"
date: 2026-04-25
score: 22
tags: ["openai", "AI"]
---

# 大项目中大家真的会用 Spec-Driven Development 吗？

https://openai.com/zh-Hans-CN/index/harness-engineering/ 中提到要把 Spec & Planning & Tasks 进度放进 git 仓库中，大家实践中真的会这么做吗？但是我看 codex 仓库内根本没这些东西，而且很多 Spec 他们都是放在的 Issue 中讨论的。
我自己也用 Openspec ，但实际使用中各种地方不顺手

openspec 会自己生成一堆 design & propsoal 很多都是正确的废话，给人 Review 就很困难，找不到重点
执行完还是有些 Bug ，这种再写回到 Spec 让他修复感觉很 tricky ，明明是 AI 特定问题，结果却要写到给人看的文档中。
生成的 Spec 你要严格按照他的流程来，执行 Task 等等。但是加上 Bug 修复。总时间感觉不如用 Planning 功能，再加少量提示词修正顺手，还不用考虑后续文档和代码对不上的问题。
据说有人碰到过 Spec 合并 delta 对不上的问题。

请教一下大家日常怎么实践的？

## 涉及话题
- openai
- AI

[原文链接](https://www.v2ex.com/t/1208418)
