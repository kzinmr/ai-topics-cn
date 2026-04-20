---
title: "复刻了一个 Magic UI 的 Border Beam 效果（Vue 3 版本）"
source: v2ex
url: "https://www.v2ex.com/t/1207121"
author: "taobeer"
date: 2026-04-20
score: 1
tags: ["agi"]
---

# 复刻了一个 Magic UI 的 Border Beam 效果（Vue 3 版本）

[分享] 复刻了一个 Magic UI 的 Border Beam 效果（ Vue 3 版本）
最近在浏览项目时被 React 社区 Magic UI 的 Border Beam （边框流光）动效吸引，觉得这种光效非常适合提升 UI 卡片或按钮的质感。
因为平时习惯使用 Vue 3 进行开发，但在社区里没找到特别完善的 Vue 适配版，于是花点时间把它迁移到了 Vue 3 ，并针对一些细节做了重构。
主要实现与调整

Vue 3 原生支持：基于 Composition API 重写，适配 Vue 3.5+ 环境，支持 useId 等新特性。
性能优化：底层动画完全依赖 CSS @property 和圆锥渐变，由 GPU 加速，不会干扰主线程的运行逻辑。
圆角自适应：内置了简单的圆角检测逻辑，能自动识别并适配第一个子元素的 border-radius，多数情况下无需手动传参。
样式隔离：针对多个组件同时在页面使用的场景，做了动态 ID 生成和样式作用域处理，避免了全局变量污染。

相关链接
目前代码已发布至 npm ，包名为 border-beam-vue3。

在线 Demo：https://mooniitt.github.io/border-beam-vue/
GitHub 地址：https://github.com/mooniitt/border-beam-vue3
代码写得比较直接，主要是想分享给有类似需求的朋友，希望能帮大家节省一点折腾的时间。如果有 Bug 或改进建议，欢迎在 GitHub 提 Issue 或 PR ，谢谢。

## 涉及话题
- agi

[原文链接](https://www.v2ex.com/t/1207121)
