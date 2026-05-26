---
title: "Codeg V0.14.0：多智能体协作来了，可以在一个会话里 claude code 干活，子智能体 codex 或 gemini 来 review"
source: v2ex
url: "https://www.v2ex.com/t/1215153"
author: "molicloud"
date: 2026-05-24
score: 3
tags: ["gemini", "claude", "智能体"]
---

# Codeg V0.14.0：多智能体协作来了，可以在一个会话里 claude code 干活，子智能体 codex 或 gemini 来 review

邀请大佬们体验一下，多智能体协作的爽感。
可以在任意主智能体里发起对话，然后其它 N 个子智能体协作（支持 claude code 、codex 、gemini 、opencode 等）。

比如我经常有这样的场景，使用 claude code 开发，然后 codex 来 review （自我感觉 codex 大局观强，claude code 的编码能力强），然后把 codex 的 review 发给 claude code ，claude code 基本都回复的情况属实，然后接着干活，每次都需要重复的手动操作一遍。
我捣腾多了之后就一直想着实现多智能体协作，在 claude code 把需求开发完了之后 codex 自动 review 代码，然后 claude code 评估，接着处理，在一个会话里自动把流程跑完。
现在多智能体协作已支持，诚邀大佬们体验一波，另外可以使用这个特性，结合一些 skills 或工具，可以碰撞一些意想不到的火花。
开源地址： https://github.com/xintaofei/codeg

## 涉及话题
- gemini
- claude
- 智能体

[原文链接](https://www.v2ex.com/t/1215153)
