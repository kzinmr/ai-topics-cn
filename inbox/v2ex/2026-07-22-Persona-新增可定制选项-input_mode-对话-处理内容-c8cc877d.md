---
title: "Persona 新增可定制选项 input_mode: 对话 | 处理内容"
source: v2ex
url: "https://www.v2ex.com/t/1229176"
author: "Livid"
date: 2026-07-22
score: 0
tags: ["AI"]
---

# Persona 新增可定制选项 input_mode: 对话 | 处理内容

如果你在做一个 AI 角色用于翻译（类似 DeepL）或者语法检查/文本润色（类似 Grammarly），那么你可能会遇到这样的场景：
你需要用户输入的所有文本都被当作是要处理的数据，而不是指令。
现在 V2EX AI Persona 提供了对这样场景的支持：

这个新选项 input_mode 的默认值是「对话」，也就是用户的输入，会被当作指令 + 数据进行处理。
如果是切换到「处理内容」，那么用户的输入会全部被当作要处理的数据喂给 Persona 的系统设定。
这是基于这个新功能做的三个 AI 角色：
Orwell Writer
基于 George Orwell 的英文写作的 6 规则，对输入文本进行语法检查及改写：
https://edge.v2ex.com/persona/orwell
效果演示 https://edge.v2ex.com/chat/68010457d2674b1fa1f486c2a5ed48cc
Translator
用户输入的任何文本，都会被翻译成中文：
https://edge.v2ex.com/persona/translator
效果演示 https://edge.v2ex.com/chat/8b0fee95e1e945ba848871a54bcb3ab2
Dict
输入任何单词，为你提供释义、发音、例句、词源、相关词列表，及这个单词在文学作品中被使用的例子。
https://edge.v2ex.com/persona/dict
效果演示 https://edge.v2ex.com/chat/8683dbd73ce840db95f840601c90aca0

## 涉及话题
- AI

[原文链接](https://www.v2ex.com/t/1229176)
