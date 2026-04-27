---
title: "Claude Code 也能玩 Galgame —— 灵魂杀手 Agent 及 skill 创建器"
source: v2ex
url: "https://www.v2ex.com/t/1206215"
author: "DouglasDong"
date: 2026-04-15
score: 0
tags: ["大模型", "Claude", "ai"]
---

# Claude Code 也能玩 Galgame —— 灵魂杀手 Agent 及 skill 创建器

清明节到现在做了两周的个人 Agent ，最近整合了一下能力，并做了一下跨平台测试，终于算是到了能发布的状态
： https://github.com/Xeonice/soul-killer
用三句话简单介绍一下这个项目

提供一个 REPL 二进制程序，用户安装后，通过 openrouter 的模型 + Exa.ai / Tavily 搜索引擎，即可基于互联网资料创建自己的 Soul （人物）、World （世界书）
结合 Soul 、World 即可生成对应剧情的 Galgame skill ，直接运行 skill 即可启动游戏，初次启动游戏需要生成剧本
Galgame Skill 支持存档、分支路线展示、剧本缓存，用户通过选项推动游戏，支持多结局和多分支路线

运行效果


随便说说
顺便可以简单说一说做这个项目的灵感和初衷，以及解决的个人问题：
确切地说，整个项目的灵感是被《同事 skill 》所启发的
https://github.com/titanwings/colleague-skill
看到这个 skill 的效果后，刚好最近在公司也在做 PPTX 的生成 Agent
https://pptx-openxml-renderer.vercel.app/
结合之前写过的专栏：
从零开始的 Galgame 制作生活 —— 序章 [剧本]
，瞬间就萌发了一个想法：是不是能用 Agent 去快速上线 Claude skill 格式的 Galgame ？借助大模型的能力去做剧本、场景，甚至于后面做代码的实时生成？
于是，经过了 14 天的反复迭代后，最终形成了这个 Agent 项目。

…(内容已截断)

## 涉及话题
- 大模型
- Claude
- ai

[原文链接](https://www.v2ex.com/t/1206215)
