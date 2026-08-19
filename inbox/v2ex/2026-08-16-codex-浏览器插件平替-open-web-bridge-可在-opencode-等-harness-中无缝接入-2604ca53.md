---
title: "codex 浏览器插件平替 open-web-bridge，可在 opencode 等 harness 中无缝接入"
source: v2ex
url: "https://www.v2ex.com/t/1234823"
author: "woniu9527"
date: 2026-08-16
score: 0
tags: ["对齐"]
---

# codex 浏览器插件平替 open-web-bridge，可在 opencode 等 harness 中无缝接入

open-web-bridge 是一个给 opencode 这类 harness 补上浏览器能力的 CLI 工具。 能力上和 codex 自带的 chrome 插件对齐，另外多了几样它没有的。因为是野生插件，可以提供一些正规插件不能做的事情，也更好 DIY 。
为啥需要这个呢？
一是 opencode 这类工具官方不提供这个能力。二是 playwright 这种路线会丢登录态。三是解决风控问题。playwright 那类方案不只是没有登录态，更严重的是会明显吃到更强的风控。 从我自己的使用体验出发，即使是 cloakbrowser 、camoufox 这种专门做反检测的浏览器， 效果也不如直接在真实浏览器里装一个插件。
仓库
https://github.com/woniu9524/open-web-bridge

## 涉及话题
- 对齐

[原文链接](https://www.v2ex.com/t/1234823)
