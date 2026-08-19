---
title: "做了一个 Agent 生成 HTML / Markdown 后的分享和反馈工具，找 10 个人用真实材料跑一遍"
source: v2ex
url: "https://www.v2ex.com/t/1228051"
author: "sevenzyx"
date: 2026-07-17
score: 0
tags: ["MCP", "Claude"]
---

# 做了一个 Agent 生成 HTML / Markdown 后的分享和反馈工具，找 10 个人用真实材料跑一遍

最近一直用 Claude Code 和 Codex 做 Markdown 文档、HTML 演示稿，还有一些可交互的页面。生成已经挺快了，后面这一段还是很别扭：
文件在 Agent 的远程 workspace 里，发给别人看要先想办法放到网上。意见回来后又散在微信、Slack 、截图里，最后还得重新整理一遍给 Agent 。
所以做了 PreApp 。现在的流程是：

Agent 通过 Skill 、CLI 或 MCP 发布 HTML / Markdown ；
别人打开链接直接看，可以划选文字、点图片或页面元素留言，不用注册；
反馈带着版本和位置回到 Agent ，Agent 再改下一版。

我自己刚用一个 checkout HTML 跑了两轮，最后是 v1 到 v4 、6 条反馈、2 次反馈回流。
现在想找 10 个人拿真实但可脱敏的材料跑一遍。适合这几种情况：

你会用 Claude Code 、Codex 或其他本地 Agent 做文档、报告、HTML PPT ；
这些内容需要发给同事、客户或朋友看；
你愿意告诉我安装、发布或反馈回流具体卡在哪一步。

免费，大概 20 分钟。我会跟到第一次 publish 出分享链接，不需要你先研究文档。
愿意试的直接回一下你用的 Agent ，以及材料是 HTML 还是 Markdown 。
产品： https://preapp.app
CLI / Skill / MCP： https://github.com/serrendypity/preapp-agent

## 涉及话题
- MCP
- Claude

[原文链接](https://www.v2ex.com/t/1228051)
