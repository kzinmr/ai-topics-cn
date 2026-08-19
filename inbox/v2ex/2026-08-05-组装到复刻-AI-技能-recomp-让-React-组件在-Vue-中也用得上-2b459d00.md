---
title: "组装到复刻-AI 技能 recomp 让 React 组件在 Vue 中也用得上"
source: v2ex
url: "https://www.v2ex.com/t/1232269"
author: "brickhu"
date: 2026-08-05
score: 0
tags: ["编程助手", "Cursor", "AI", "Claude", "AI agent", "ai"]
---

# 组装到复刻-AI 技能 recomp 让 React 组件在 Vue 中也用得上

recomp 是一个面向前端开发的组件复刻技能（支持主流 AI agents ），它解决了组件库框架（例如 React ）和你项目开发框架（例如 SolidJS ）不一致的问题：指导 AI 阅读组件库文档，把组件的交互和行为模式复刻成适配你框架的 headless(无头) 组件源码和使用示范——所有产出直接展示在对话里，复制即用. https://github.com/brickhu/skills/recomp


现在的设计组件库，为什么你都用不上？
不是它们不好——shadcn/ui 、Radix 、MUI 、Ant Design ，一个比一个精致。问题出在"用得上"这三个字上。
深夜 23:47 ，你正在为自己的 App 打磨一个日期选择组件。你发现了 shadcn/ui 的 DatePicker ，很惊艳，交互模式也基本符合你的要求。你花了大把时间研究它的安装使用流程，把使用文档翻了个遍——然而一个根本问题始终绕不过去：框架不对。它只支持 React ，而你的项目用的是 SolidJS 。
其实，我们选用第三方设计组件库时，普遍都会面临这么几个问题：

框架对不上：JSX 、hooks 、受控组件，复制过来直接报错——最精致的组件库几乎全是 React 写的，而你用的是 SolidJS / Vue / Svelte
样式对不上：组件库用 Tailwind 写的，你的项目用的是 StyleX / CSS-in-JS ，class 满天飞，接不进来
设计对不上：组件库自带一套 design token ，跟你的设计系统打架，改起来比重写还累

这就是前端开发者的普遍困境：我们想用别人的轮子来解放生产力，但不是每一个轮子（组件）都适合你的底盘（框架）——于是你只能安慰自己"回头自己写一个"。
组件库是"成品菜"，你要的其实是"菜谱"

…(内容已截断)

## 涉及话题
- 编程助手
- Cursor
- AI
- Claude
- AI agent
- ai

[原文链接](https://www.v2ex.com/t/1232269)
