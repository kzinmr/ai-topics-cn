---
title: "Linkly AI Note：极简的卡片笔记，用 Markdown 存储在本地"
source: v2ex
url: "https://www.v2ex.com/t/1232052"
author: "blueeon"
date: 2026-08-04
score: 1
tags: ["ChatGPT", "Claude", "MCP", "AI"]
---

# Linkly AI Note：极简的卡片笔记，用 Markdown 存储在本地

造了一个新轮子：笔记。👉下载👈

它是我们主产品 LinklyAI 的一部分。开发这个功能前，我们犹豫了两个月；最终上线后，只用了 1 分钟，我就感觉这功能非常有用。
我是一个非常重度的笔记用户。我自己的本地用 Markdown 编写的笔记就有 6400 条，从十几年以前开始，就在持续不断地用各种笔记软件记录。在没有 AI 之前，我最后深度使用的笔记软件只剩下三个：

Notion：我最核心的笔记库，写了几千条了
Flomo：它太适合去记一些零碎的想法和思考，所以里面也记了两三百条非常短的、碎片化的笔记
Obsidian：流行的 Markdown 编辑器和知识库应用

所以有这个需求以后，一直都比较抗拒去开发笔记功能。直到搭档把笔记功能的第一版开发出来后，上手后的那一刻，我才意识到为什么要造这个轮子：
当我在 Claude Code 里面问了一句：“我刚刚写的那条笔记你怎么看？”的时候，Claude Code 调 CLI 立即就知道我说的是哪一条笔记，然后就开始展开讨论。
这种无缝的感觉简直太爽了！而且相同的体验，在 ChatGPT 和 Claude 的网页版里面也能用，借助 Linkly AI 自带的 MCP 隧道功能，ChatGPT 和 Claude 的网页版也能直接读写笔记。
怪不得这么多人开发 AI 笔记！
核心差异有下面几个：

在记录端，参考了很多卡片笔记的做法，保持极简，支持有限的格式，比较适合语音输入法录入
文件用 Markdown 保存在本地，一条笔记一个 Markdown
可以通过 MCP 、CLI 甚至直接读文件的方式被本地 Agent 使用
因为文件格式非常简单，其他软件的笔记，可以让 Codex 一键转换过来。比如 flomo 的导出文件
免费/离线/

希望有人喜欢

## 涉及话题
- ChatGPT
- Claude
- MCP
- AI

[原文链接](https://www.v2ex.com/t/1232052)
