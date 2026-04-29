---
title: "Vibe Coding 了一个浏览器侧边栏 AI Agent， AGPL3.0 开源"
source: v2ex
url: "https://www.v2ex.com/t/1208874"
author: "maotoumao"
date: 2026-04-27
score: 0
tags: ["AI", "MCP", "AI Agent"]
---

# Vibe Coding 了一个浏览器侧边栏 AI Agent， AGPL3.0 开源

RT ，之前也做过一些开源项目，出发点都是自用，觉得还可以就分享出来，这次也一样

整个项目包括站点都是 vibe coding 的产物，不过写完后发现只顾着 review AI 生成的代码内容，没留意代码的文件命名风格不一致... 不过也不影响使用就是了
github: https://github.com/maotoumao/Cebian

站点： https://cebian.catcat.work/zh/
背景
做这个小项目大概的出发点是一系列在用浏览器的时候可以偷懒的场景：

工作/生活中会涉及到一些英文场景（比如回复邮件，PR review 等等），之前需要先让 AI 翻译/润色，然后再填到输入框，如果直接润色好自己填进去会省点事
对于网页总结/翻译 等这种需求，不想开其他软件的会员，想充分利用从各种渠道蹭到的 token plan
希望 AI 能理解一些重复性的网页操作，然后能以 skill/memory 的形式学会，然后帮我自动操作浏览器
打开 n 个 tab ，然后忘记自己刚才打开了哪个，只好一个一个点..

功能
大概是常规的 AI Agent 的功能，支持各种 Open AI Compatible 的 AI provider 、自定义 instruction 、slash command 、MCP （ http ）、skills ；
和 agent 对话的时候可以直接选中页面中的某个元素、录制操作、上传文件等
使用场景

除了上面想到的那些以外，感觉还可以用来做 rpa ，自动化测试之类的；不过都是后话了.. 先把这个能满足自己使用场景的最小版本发出来~

有需要的小伙伴可以试试~ 万一有用呢 :D

## 涉及话题
- AI
- MCP
- AI Agent

[原文链接](https://www.v2ex.com/t/1208874)
