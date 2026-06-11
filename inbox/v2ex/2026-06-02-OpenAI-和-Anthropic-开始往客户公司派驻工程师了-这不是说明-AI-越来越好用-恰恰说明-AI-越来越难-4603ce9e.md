---
title: "OpenAI 和 Anthropic 开始往客户公司派驻工程师了——这不是说明 AI 越来越好用，恰恰说明 AI 越来越难落地"
source: v2ex
url: "https://www.v2ex.com/t/1217425"
author: "zengdan2024"
date: 2026-06-02
score: 1
tags: ["GPT", "AI", "function calling", "LLM", "RAG", "ai", "Claude", "Anthropic", "prompt", "OpenAI"]
---

# OpenAI 和 Anthropic 开始往客户公司派驻工程师了——这不是说明 AI 越来越好用，恰恰说明 AI 越来越难落地

聊一个我最近关注到的趋势——
OpenAI 和 Anthropic 都在组建一种叫 FDE （ Forward Deployed Engineer ，前沿部署工程师）的团队。把工程师直接派到客户公司内部，驻场帮客户搭 AI 系统。
这个角色不新——Palantir 大概 20 年前就发明了这种模式，当时是派工程师去政府机构、在保密网络上驻场开发。
但 AI 时代 FDE 复活了，而且复活的原因很值得想清楚。
FDE 复活的根本原因是：AI 落地的真正瓶颈不在 API ，在"翻译"。
我做 AI 咨询快两年了。最深的一个感受是——客户买的不是模型、不是 API 、不是 token 。客户买的是"有人能听懂我的业务痛点，然后把它变成 AI 能解决的问题"。
这个"翻译"过程，API 文档教不了，demo 演示不了，销售 PPT 更不行。必须有一个人坐在客户的办公室里，花几天到几周的时间，真正理解这家公司的业务流程、数据结构、组织政治、合规约束——然后把这些翻译成 agent workflow 、RAG 架构、eval 策略。
OpenAI 和 Anthropic 组建 FDE 团队，本质上是承认了一件事——
"我们的 API 再好，客户自己也用不好。必须派人过去。"
这跟我之前写的"AI 能力和人的使用能力之间的鸿沟"是同一件事。FDE 就是用来填这道鸿沟的人。
但 FDE 模式有一个结构性问题——他们不是中立的。
OpenAI 派来的 FDE 会推荐什么方案？ OpenAI 的。Anthropic 派来的 FDE 会推荐什么方案？ Anthropic 的。
这不是因为他们不专业。是因为激励结构决定了他们只能推荐自家产品。他们的 KPI 是"让客户深度使用我们的平台"，不是"给客户找到最好的方案"。

…(内容已截断)

## 涉及话题
- GPT
- AI
- function calling
- LLM
- RAG
- ai
- Claude
- Anthropic
- prompt
- OpenAI

[原文链接](https://www.v2ex.com/t/1217425)
