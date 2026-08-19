---
title: "[开源] agy-staff: 让 Gemini 成为 Codex / Claude Code 的员工"
source: v2ex
url: "https://www.v2ex.com/t/1235732"
author: "pkuwkl"
date: 2026-08-19
score: 0
tags: ["推理", "Claude", "Gemini", "Anthropic", "多模态", "GPT"]
---

# [开源] agy-staff: 让 Gemini 成为 Codex / Claude Code 的员工

Repo: https://github.com/keli-wen/agy-staff

其实是把 Antigravity 做成了 Codex / Claude 的 subagent 插件 agy-staff 。让 Gemini 为另外的模型打工。

为什么会想做这个东西呢？主要是我 agentic engineering 中遇到的一些痛点：

目前速度快的模型通常效果不佳；而能力更强的模型，推理速度通常较慢（点名 GPT 5.6 Sol），而且额度不足。
Gemini 会员的获取成本较低，但如何高效利用它的额度呢？目前它的能力还不适合作为一个 ochestrator 。

自 Gemini 3.5 Flash 之后，其实 Gemini Flash 开始有潜在的生态位（高效的执行者）。但彼时它的能力还是太差了，用户（例如我）没办法信任它。但随着迭代到 Gemini 3.7 Flash ，它的能力较之于自己有了一次跃升，明显可靠不少。所以让 Codex 或 Claude Code 中的顶级模型通过 grill 和 review 得到解决问题的 spec / insights ，让 Gemini 作为接受派遣它们的员工，并完成具体工作。这个流程似乎能有效的解决我上述提到的两个痛点。而且 Antrigravity CLI 还可以原生调用 Nano Banana 加上 Gemini 系列模型在多模态/前端领域的能力，在不那么注重执行的领域（营销，分析，设计）它也可以成为 Codex / Claude 强大的助手（尤其是 Claude 无法原生生图）

所以我做了对应的插件，目前提供五种常用角色：

staffer：通用任务，也可以调用 Antigravity 原生能力生成图片
researcher：代码库调研 / Deep Research

…(内容已截断)

## 涉及话题
- 推理
- Claude
- Gemini
- Anthropic
- 多模态
- GPT

[原文链接](https://www.v2ex.com/t/1235732)
