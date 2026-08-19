---
title: "做了一个带知识库 RAG 问答的 macOS GitHub Stars 工具，想听听大家的建议"
source: v2ex
url: "https://www.v2ex.com/t/1229165"
author: "dong2go"
date: 2026-07-22
score: 0
tags: ["MCP", "Claude", "llama", "embedding", "RAG", "AI", "LLM"]
---

# 做了一个带知识库 RAG 问答的 macOS GitHub Stars 工具，想听听大家的建议

最近一直在做一个 macOS 工具，叫 Starcat 。从最初简单的 stars 同步到现在加入知识库 RAG 问答，想分享一下进展和设计思路，听听大家的反馈。
起因
我自己的 GitHub Stars 已经一千八百多个了。刚开始 star 是收藏，后来变成「以后再看」，再后来就是精神负债了。最近一次触发我的是：想找一个以前 star 过的 Swift 剪贴板管理工具，记不清名字，在 GitHub Stars 页面翻了快 20 分钟。找到了，但这个过程让我觉得——GitHub 提供了「收藏」，但没提供「找回」。
所以我做了 Starcat ，一个 macOS 原生应用。最开始做了最基础的事：把 stars 同步到本地，三栏管理，支持标签、笔记、阅读状态、全文搜索、AI 摘要。

最近在做的：知识库 RAG 问答
但最近最花精力的功能是知识库 RAG。这个东西的动机很简单：有时候你需要的不是「搜到一个 repo 」，而是「回答一个问题」。
举个例子。我想知道「我收藏的 SwiftUI 项目里，哪些用了 Core Data 做本地存储？」。这不是一个搜索词能表达的问题。GitHub 搜索帮不了我，全文搜索也帮不了我——因为这个问题需要理解「用了 Core Data 做本地存储」这个语义，然后在我本地几百个 repo 的 README 、笔记、摘要里找到匹配的内容，最后综合成答案。
RAG 工作台做的事情就是：

理解你的自然语言问题。
从你的知识库（你主动筛选入库的 repo ，不是全部 stars ）里做混合检索——本地 FTS5 全文 + 本地 embedding 向量。
找到相关的 README 段落、笔记片段、AI 摘要。
把这些上下文和你的问题一起发给 LLM ，生成带引用的回答。
每个结论都链接回具体 repo 和段落，你可以点进去验证。



…(内容已截断)

## 涉及话题
- MCP
- Claude
- llama
- embedding
- RAG
- AI
- LLM

[原文链接](https://www.v2ex.com/t/1229165)
