---
title: "pagegrok 本地 AI 接入网页理解，浏览器页面选区解读"
source: v2ex
url: "https://www.v2ex.com/t/1212007"
author: "kuhung"
date: 2026-05-11
score: 0
tags: ["llama", "Gemini", "大模型", "AI"]
---

# pagegrok 本地 AI 接入网页理解，浏览器页面选区解读

pagegrok 是笔者自身需求出发，构建的一个浏览器插件。简单来说就是，通过插件形式，直接选读当前页面区域，再和本地/远端的大模型交互。

差异比较：

可选择本地模型，做简单的主题提取，适合敏感数据
为什么不把链接丢给各类大模型？因为有些简单任务，不需要也不想再跳转其他页面，看完就算数了
相较于成熟同类产品 page-assist ，本产品逻辑简单，还没到大而全的地步
相较于问问 Gemini ，那就是可以自己控制不受网络 ip 影响
不用复制粘贴，支持页面框选，仅关注用户关心的区域

路线图：

支持更多的本地模型框架，目前线上仅 Ollama ，下一版本支持 oMLX 和 LM Studio
调整为侧边栏模式，方便交互

https://www.pagegrok.org/
一句话总结：简单的、本地 AI 网页内容交互插件

## 涉及话题
- llama
- Gemini
- 大模型
- AI

[原文链接](https://www.v2ex.com/t/1212007)
