---
title: "Copilot 插件和 VSCode 更新后不显示 IntelliSense 解决方案"
source: v2ex
url: "https://www.v2ex.com/t/1218233"
author: "Zhuzhuchenyan"
date: 2026-06-05
score: 0
tags: ["copilot", "Copilot", "AI"]
---

# Copilot 插件和 VSCode 更新后不显示 IntelliSense 解决方案

正常情况（ IntelliSense 和 Copilot 提示同时出现）


更新后情况（只有 Copilot 提示）


解决办法,添加如下配置

"editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": false
}

https://www.reddit.com/r/vscode/comments/1tn6pxd/copilot_is_breaking_the_intellisense_so_annoying/

虽说现在都是 AI 写代码了，但是公司里一些古老屎山还是需要人工干预写一点，一觉起来点个更新后写代码怎么写怎么难受

## 涉及话题
- copilot
- Copilot
- AI

[原文链接](https://www.v2ex.com/t/1218233)
