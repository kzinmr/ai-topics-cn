---
title: "做了一个文档转 Markdown 工具：支持 PDF/Docx/PPTX，想听听大家的反馈"
source: v2ex
url: "https://www.v2ex.com/t/1219399"
author: "xlwu1064442747"
date: 2026-06-10
score: 3
tags: ["Prompt", "RAG", "LLM", "AI"]
---

# 做了一个文档转 Markdown 工具：支持 PDF/Docx/PPTX，想听听大家的反馈

最近在整理自己的知识库和写 AI Prompt 的时候，发现把各种格式的文档（ PDF, Word, PPT 等）转换成干净的 Markdown 是一件挺头疼的事。市面上的工具要么排版乱，要么就是收费昂贵且流程繁琐。
于是我动手做了这个小站：​Document to Markdown​。
做这个工具的初衷
现在的 AI 工具（ LLMs ）对 Markdown 的理解能力远高于纯文本或复杂的 HTML 。我希望建立一个简单的 Workflow ，让大家能快速把手头的各种“硬核”文档变成 AI 友好、笔记软件友好的 Markdown 格式。
目前支持的功能
多格式支持：​ PDF, DOCX, PPTX, XLSX, HTML, CSV, 甚至还有 EPUB 。
结构还原：​ 尽量保留了原文档的标题层级、列表和表格（表格转换是我花精力最多的地方）。
隐私保护：​ 采用 Request-only 模式，我们不保存用户上传的原文件，也不持久化生成的 Markdown ，只做实时转换。
开发者友好：​ 已经规划了 API 接入，方便集成到大家自己的 RAG 或自动化流程中。
为什么需要大家的反馈？​
目前产品还在早期阶段，虽然我自己测试了很多样例，但文档格式千奇百怪，肯定还有很多坑：
转换质量：​ 复杂的 PDF 或嵌套表格转换效果是否符合预期？
交互体验：​ 目前的上传和预览流程是否顺手？
功能需求：​ 除了现有的格式，大家是否还需要支持其他冷门格式（如特定代码格式或 Wiki 语法）？
网站地址：​ https://documenttomarkdown.com/
目前提供免费的 Trial 次数（登录后每天有 10 次免费额度），欢迎大家随意“蹂躏”。如果觉得好用，或者有任何想吐槽的地方，请直接在评论区留言。
每一条建议我都会认真看，非常感谢！

## 涉及话题
- Prompt
- RAG
- LLM
- AI

[原文链接](https://www.v2ex.com/t/1219399)
