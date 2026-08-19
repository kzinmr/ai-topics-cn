---
title: "VS Mind: 体验最好的 VS Code 思维导图，完全开源"
source: v2ex
url: "https://www.v2ex.com/t/1225075"
author: "funboyhu"
date: 2026-07-05
score: 0
tags: ["AI", "ai"]
---

# VS Mind: 体验最好的 VS Code 思维导图，完全开源

最近在用 AI 写文档，我习惯在 VS Code 里干活，就想顺便在编辑器里画思维导图。搜了一圈扩展，体验都不太对：

有的是专有/二进制格式，Git diff 看不懂，协作也麻烦
有的库很老，界面能用但几乎不能拖拽改结构，改个节点位置都费劲
还有一类是把 Markdown 渲染成导图，适合展示，不太适合一边想一边改、反复整理

我想要的是：就在 VS Code 里，像正常文件一样打开，能拖节点、能就地改字、改完继续写文档。所以自己撸了一个扩展 VS Mind ，基于开源的 simple-mind-map ，完全免费且开源。
大概能做的事：


拖拽节点、平移缩放画布，双击改文字


50+ 主题、多种布局，支持导出 PNG/SVG


JSON 存文件，可以和 AI / 分屏源码一起用


中英文界面
Marketplace 搜 VS Mind 就行：
https://marketplace.visualstudio.com/items?itemName=rainlin.vs-mind
源码： https://github.com/Rainlin007/vs-mind
第一版，肯定还有粗糙的地方。如果你也在 VS Code 里写东西、又需要先把思路理清楚，欢迎试试

## 涉及话题
- AI
- ai

[原文链接](https://www.v2ex.com/t/1225075)
