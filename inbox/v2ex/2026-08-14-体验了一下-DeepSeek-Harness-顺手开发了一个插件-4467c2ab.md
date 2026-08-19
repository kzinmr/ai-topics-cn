---
title: "体验了一下 DeepSeek Harness 顺手开发了一个插件"
source: v2ex
url: "https://www.v2ex.com/t/1234412"
author: "luzhong"
date: 2026-08-14
score: 0
tags: ["DeepSeek"]
---

# 体验了一下 DeepSeek Harness 顺手开发了一个插件

体验了一下 DeepSeek Harness ，顺手开发了一个插件：万能文本转换器。
把 PDF 、Word 、PPT 、Excel 、EPUB 、CSV 等文档一键转换为 Markdown，Agent 可以直接读取和处理，无需再为解析各种文档格式发愁。
特性

支持 Word （.doc/.docx ）、PowerPoint （.ppt/.pptx ）、Excel （.xls/.xlsx ）、PDF 、EPUB 、RTF 、CSV 、OpenDocument （.odt/.ods/.odp ）
输出 GitHub-Flavored Markdown ，保留表格、列表、标题结构
自动检测格式，也可手动指定
基于 Rust 原生绑定（@firecrawl/anydoc ），无需 Python 、无外部进程、不阻塞事件循环

安装
dsh plugin --profile web add github:beancookie/dsh-plugin-anydoc

使用
对 Agent 说一句：
请将 /path/to/report.pdf 转换为 Markdown
即可自动调用工具完成转换。
链接

GitHub： https://github.com/beancookie/dsh-plugin-anydoc
欢迎 star 与反馈！

## 涉及话题
- DeepSeek

[原文链接](https://www.v2ex.com/t/1234412)
