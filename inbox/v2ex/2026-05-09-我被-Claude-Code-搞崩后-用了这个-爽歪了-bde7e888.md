---
title: "我被 Claude Code 搞崩后，用了这个，爽歪了"
source: v2ex
url: "https://www.v2ex.com/t/1211492"
author: "zoomcmj"
date: 2026-05-09
score: 0
tags: ["对齐", "AI", "Claude"]
---

# 我被 Claude Code 搞崩后，用了这个，爽歪了

最近被 Claude Code 和 codex 搞崩了几次仓库后，发现现在很多 AI Coding 最大的问题已经不是“不会写代码”，而是改着改着就开始跑偏，需求越做越歪，AI 还特别喜欢生成一大堆繁杂代码，最后看半天都不知道它到底改了啥。。。
官方 spec-kit 我也试了，确实屌，AWS 也应用了这个企业级的框架，但感觉有点重。所以自己搞了个更轻量一点的 mini-spec-kit：
mini-spec-kit
核心思路就是别让 AI 上来直接一顿乱改，而是先理解需求、确认范围，梳理需求，制定计划，对齐需求，再一步一步实现，然后自动测试。
比较适合 Claude Code 、Codex 配合 Hermes 调度 这种 agent coding 场景，又比较不那么费 token 。
目前还在持续折腾，欢迎提建议。😂

## 涉及话题
- 对齐
- AI
- Claude

[原文链接](https://www.v2ex.com/t/1211492)
