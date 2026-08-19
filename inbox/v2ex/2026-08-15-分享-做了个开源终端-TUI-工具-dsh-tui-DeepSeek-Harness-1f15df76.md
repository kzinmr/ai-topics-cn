---
title: "[分享] 做了个开源终端 TUI 工具： dsh-tui (DeepSeek Harness)"
source: v2ex
url: "https://www.v2ex.com/t/1234696"
author: "tomowang"
date: 2026-08-15
score: 0
tags: ["deepseek", "LLM", "DeepSeek", "ai"]
---

# [分享] 做了个开源终端 TUI 工具： dsh-tui (DeepSeek Harness)

最近在尝试 DeepSeek 官方的 agent harness （ dsh ），官方自带的是 web-app 和 headless 两种前端，平时用终端用的比较多，正好学习写了个 TUI —— dsh-tui 。

项目地址： https://github.com/tomowang/dsh-tui
npm： https://www.npmjs.com/package/@tomowang/dsh-tui

快速安装:
dsh plugin --profile tui add @tomowang/dsh-tui

dsh --profile tui
dsh --profile tui --resume <sessionId>           # reopen a persisted session
dsh --profile tui --agent-preset <presetId>      # start a fresh session on a given preset
dsh --profile tui --dump-config                  # inspect the composed plugin tree

是什么
dsh-tui 是一个 out-of-tree 的 dsh bundle ，同时也是一个 Cordis 插件。原理上和官方 dsh-web-app / dsh-headless 一样，都是叠在 @deepseek-ai/dsh-base 之上，模型适配、工具调用、会话持久化、沙箱和审批策略这些全部留在 dsh-base 里没动，dsh-tui 只负责终端侧的输入和渲染，算是给 dsh 换了个「壳」。
功能


…(内容已截断)

## 涉及话题
- deepseek
- LLM
- DeepSeek
- ai

[原文链接](https://www.v2ex.com/t/1234696)
