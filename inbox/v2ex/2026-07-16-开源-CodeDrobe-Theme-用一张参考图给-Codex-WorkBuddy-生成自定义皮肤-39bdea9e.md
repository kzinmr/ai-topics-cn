---
title: "[开源] CodeDrobe Theme：用一张参考图给 Codex / WorkBuddy 生成自定义皮肤"
source: v2ex
url: "https://www.v2ex.com/t/1227872"
author: "AIGC2D"
date: 2026-07-16
score: 0
tags: ["AI", "OpenAI"]
---

# [开源] CodeDrobe Theme：用一张参考图给 Codex / WorkBuddy 生成自定义皮肤

最近 Codex 换皮肤在抖音、闲鱼挺火，甚至看到有人把一套 Codex 皮肤标价 199 元。
这说明自定义界面确实有需求，但我们更想把它做成一套可复用、可维护、可以让 AI 直接操作的开源工具。
所以最近把 CodeDrobe 的主题运行时、应用适配器和 Agent Skill 重新整理了一遍。现在 codedrobe-theme 不再只支持 OpenAI Codex ，也支持腾讯 WorkBuddy 。
项目目前全部开源。

它能做什么
安装 Skill 后，可以直接给 AI 一张参考图片，然后告诉它：

参考这张图片，帮我生成一个 Codex 皮肤。保留原生交互，生成可移植的主题包，并在真实应用中验证首页和会话页。

也可以直接要求：

把这套视觉风格同时做成 Codex 和 WorkBuddy 皮肤。

Skill 会完成这些工作：

分析参考图的配色、材质和视觉元素
分别读取 Codex / WorkBuddy 的实时界面结构
为两个应用生成各自的主题 CSS
把共享图片和应用专属样式打包成 .codedrobe-theme
在真实应用中应用主题并截图验证
应用更新导致主题错位后，重新分析 DOM 并修复
随时移除主题并恢复原生界面

一个主题包可以同时包含 Codex 和 WorkBuddy 两套目标样式，不需要为每个应用复制一套 Skill 。
安装
安装 codedrobe-theme Skill：
npx skills add CodeDrobe/skills \
  --skill codedrobe-theme \
  --global \
  --agent codex \
  --yes

安装运行时：
npm install --global @codedrobe/core
codedrobe apps


…(内容已截断)

## 涉及话题
- AI
- OpenAI

[原文链接](https://www.v2ex.com/t/1227872)
