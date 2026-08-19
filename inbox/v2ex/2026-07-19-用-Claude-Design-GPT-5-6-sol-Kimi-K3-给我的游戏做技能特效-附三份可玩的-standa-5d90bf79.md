---
title: "用 Claude Design / GPT-5.6-sol / Kimi K3 给我的游戏做技能特效，附三份可玩的 standalone"
source: v2ex
url: "https://www.v2ex.com/t/1228361"
author: "joeeey9303"
date: 2026-07-19
score: 0
tags: ["gpt", "GPT", "ai", "KIMI", "prompt", "claude", "Kimi", "Claude", "AI", "kimi"]
---

# 用 Claude Design / GPT-5.6-sol / Kimi K3 给我的游戏做技能特效，附三份可玩的 standalone

在业余时间做一款哥特埃及题材类吸血鬼幸存者的 roguelike 游戏（ Phaser 4.1 + H5 ）。美术、特效、UI 全部靠 AI 流水线产出，分享一下这套 pipeline 跑到今天的样子，以及最近一次挺有意思的实验。
这是游戏实际跑起来的样子：

技能特效(VFX) 生成 pipeline
核心思路：把「设计」当成一份可验收的工程交付(pipeline with skills)，而不是一句 prompt 。

Handoff 包生成 skill：每个设计需求打成一个自包含 zip —— 真实游戏截图、机制数值表、视觉正交规则（新技能不和老技能相似）、性能预算等。这个 zip 会扔给 claude desgin 作为需求，并且定义交付标准。
生成：设计系统返回一个自包含的交互式 standalone HTML （底部有链接） —— 不是一张图，是能玩的可调参数的网页，还要暴露一个脚本化 API 方便我自动验收让 AI 接入。
独立验收：用 Playwright 录像截图，跑一套硬性 gate 后丢给另一个模型盲评打分。
移植：过审的 standalone 走 takeover 流程进 Phaser —— 深读它的源码（ painter / 时间轴 / 锚点），±5% 保真门，真机 ADB 录像验证。

痛点
之前所有的 vfx 都是通过 claude desgin 做设计后产出 standalone html 后介入游戏，但是 claude 这玩意经常不够用或者就 you account has been suspended, 所以必须找个 alternaive.

…(内容已截断)

## 涉及话题
- gpt
- GPT
- ai
- KIMI
- prompt
- claude
- Kimi
- Claude
- AI
- kimi

[原文链接](https://www.v2ex.com/t/1228361)
