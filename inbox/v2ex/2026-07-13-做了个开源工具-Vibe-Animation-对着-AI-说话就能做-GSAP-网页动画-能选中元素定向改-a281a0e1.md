---
title: "做了个开源工具 Vibe Animation：对着 AI 说话就能做 GSAP 网页动画，能选中元素定向改"
source: v2ex
url: "https://www.v2ex.com/t/1227053"
author: "royluo"
date: 2026-07-13
score: 0
tags: ["Claude", "ai", "AI", "MCP"]
---

# 做了个开源工具 Vibe Animation：对着 AI 说话就能做 GSAP 网页动画，能选中元素定向改

今年大家都在「 vibe coding 」，我就想——动画能不能也 vibe 一下？于是做了 Vibe Animation：用自然语言描述场景，Claude Agent 直接生成 GSAP 动画，浏览器里实时预览；选中哪个元素就跟 AI 说哪个，改完一键导出 MP4/GIF/JSON 。
GitHub： https://github.com/luogao/animation-studio


它想解决什么
写 GSAP 是件「会的人很爽、不会的人很劝退」的事：要懂时间轴、easing 、SVG path 、stagger……光让一个 logo 弹跳着出现，可能就得调半天曲线。
而让 AI 直接「写」一段动画代码，又会丢上下文——你说「把那个圆放大」，它根本不知道是哪个圆，只能把整个场景重写一遍，越改越乱。
所以我想了个办法：让 AI 能看到画布、能被你「指」着改。

怎么用

用一句话描述你要的动画，比如「一个橙色方块从左边滑进来，弹两下停住」
Agent 在画布里实时画出来（是真 GSAP 时间轴，不是帧序列）
画布上点选任意元素 → 对话框里说「这个改大一点」→ 它只动这一个
满意了导出 MP4/WebM/GIF ，或导出 SceneConfig JSON 丢给 Remotion 做最终成片


几个我比较得意的设计

选中即上下文：核心。点哪个 actor ，就把它的 id/类型/当前状态带进对话，Agent 只改这一个，不重写全局
真实 GSAP 而非预录：预览就是浏览器里跑的真实时间轴，所见即所得，暂停/回放/拖时间轴都对
git 式版本树：每次 AI 修改是一个草稿，提交成版本，随时回滚任意节点，历史只增不改；多项目互不干扰
配色/字体让 AI 出方案：给个主色，Agent 生成几套和谐调色板（带 WCAG 对比度校验）让你挑；字体同理

…(内容已截断)

## 涉及话题
- Claude
- ai
- AI
- MCP

[原文链接](https://www.v2ex.com/t/1227053)
