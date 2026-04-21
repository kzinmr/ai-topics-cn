---
title: "GridMove for macOS：按窗口任意地方移动窗口，或者快速调整为自定义布局"
source: v2ex
url: "https://www.v2ex.com/t/1207558"
author: "duix"
date: 2026-04-21
score: 0
tags: ["Claude", "AI"]
---

# GridMove for macOS：按窗口任意地方移动窗口，或者快速调整为自定义布局

链接：
GridMove
演示
点击窗口任意处，移动（可跨屏）

不同屏幕，设定不同布局，并且快速应用

（ P.S. 猜一下上面的演示图是什么软件做的。）
Homebrew 安装
brew install mirtlecn/tap/GridMove
# 没签名，需要解除隔离
xattr -dr com.apple.quarantine /Applications/GridMove.app

用法

设定一个鼠标快捷键（默认是中键），要是像我一样鼠标按键很多，就设置成侧键。按了就能移动窗口
或者按键修饰键（默认是 Ctrl + Shift + Cmd ）后，用左键点击窗口也行。这是为了让触摸板也能单独操作。
默认是只是移动窗口，如果设置了默认进入布局模式，或者按一下 Shift / 右键，就能快速指定窗口的大小和位置

设置页面，截图


其他说明

本意是希望借这个项目实现一个我完全不懂没接触过的东西，体验下 Codex 。换句话说，没写过 swift ，也没搞过 macOS 任何应用开发。全部是 Codex （主要）和 Claude Code （让它改了下 overlay 的渲染）写的。所有对话沟通的提示词我也放上去了（ P.S. 很长）
这个是当初的 Windows 版本的复刻。但因为 macOS 窗口 API 很多缺失（窗口层级，space 切换，移动到不同的 space ），所以比原来的功能差很多

产品解决的小问题：
Codex 的额度用不完，消耗一下
鼠标按键太多，我想只用鼠标就能完成快捷的窗口移动和布局；改进下多屏移动窗口的体验。
有一个副屏，想始终占满全屏，主屏就用自己的自定义布局


可能有同类产品，不过不在乎。

后记

整体上，Codex 令人惊艳，MVP 几乎是一个计划书给定 10 分钟可以构建完成品

…(内容已截断)

## 涉及话题
- Claude
- AI

[原文链接](https://www.v2ex.com/t/1207558)
