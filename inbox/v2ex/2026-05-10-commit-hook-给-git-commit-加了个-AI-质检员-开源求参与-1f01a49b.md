---
title: "[commit-hook] 给 git commit 加了个 AI 质检员，开源求参与"
source: v2ex
url: "https://www.v2ex.com/t/1211698"
author: "v2reach"
date: 2026-05-10
score: 0
tags: ["AI", "llama", "Anthropic", "ai", "LLM", "OpenAI"]
---

# [commit-hook] 给 git commit 加了个 AI 质检员，开源求参与

团队 commit message 质量一直是个头疼事——「 fix bug 」「 update code 」满天飞，CR 时大量时间花在纠正描述上。

于是写了 commit-hook：一个 git `commit-msg` hook ，commit 时自动拿 diff 跟 message 对账，LLM 判定不匹配就拦截并给出改进建议。

仓库： https://github.com/Casper-Mars/commit-hook

**目前 MVP 已跑通**，Python CLI ，`uv tool install` 一行装完，`commit-hook init` 自动配置 hook 。支持 OpenAI / Anthropic / Ollama / 自定义 API 。

发这个帖子主要是想找同路人一起打磨：

---

**提 Issue：边界场景需要更多真实反馈**

现在核心链路通了，但我很清楚还有不少需要完善的地方：
- 大 diff 截断策略是否合理？你遇到过被截掉关键变更的情况吗？
- 敏感文件过滤现在走黑名单，是否应该切白名单？
- 团队场景下 `[skip-validate]` 的权限控制怎么做？
- LLM 判定的准确率怎么量化、怎么持续优化？

如果你的团队有 commit 规范方面的痛点，欢迎开 issue 聊。

---

**提 PR：有几个方向特别适合社区贡献**

技术栈 Python 3.10+，`uv` 管理，结构清晰好上手：
- 输出美化——现在终端红绿字够用，但谁想搞个 TUI 展示评分细节？
- diff 智能摘要——大 diff 场景下的压缩/摘要策略优化
- 多模型对比模式——双模型打分取均值，降低单模型误判

…(内容已截断)

## 涉及话题
- AI
- llama
- Anthropic
- ai
- LLM
- OpenAI

[原文链接](https://www.v2ex.com/t/1211698)
