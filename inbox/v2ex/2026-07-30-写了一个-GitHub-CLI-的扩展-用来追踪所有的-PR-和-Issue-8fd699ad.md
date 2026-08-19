---
title: "写了一个 GitHub CLI 的扩展，用来追踪所有的 PR 和 Issue"
source: v2ex
url: "https://www.v2ex.com/t/1231091"
author: "shadeofgod"
date: 2026-07-30
score: 0
tags: ["AI Agent"]
---

# 写了一个 GitHub CLI 的扩展，用来追踪所有的 PR 和 Issue

最近给自己做了个小工具：GitHub Workbench 。
起因很简单：我手上的 PR 和 issue 越来越多，而且散在不同 repo 里。每天在 GitHub 里来回翻，很容易漏掉该 review 、该回复，或者刚有新进展的事情。
它会把和我相关的 PR / issue 聚到一个地方，顺手加了几个我自己很需要的功能：

直接看到 AI Agent 的 review reaction ，知道它正在 review ，还是已经处理完成；
汇总最新活动，包括评论、review 、commit 、label 和 review request ；
有重要更新时发系统通知；
PR 上显示 Codex/CC 正在工作的状态
Browser 和 TUI 两种界面，直接复用本机 gh 登录。

项目地址： https://github.com/zoubingwu/gh-workbench
安装也很简单：
gh extension install zoubingwu/gh-workbench
gh workbench

先解决我自己的信息过载问题，分享出来看看有没有同样被 PR 和 issue 淹没的人 😄

## 涉及话题
- AI Agent

[原文链接](https://www.v2ex.com/t/1231091)
