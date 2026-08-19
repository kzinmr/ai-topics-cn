---
title: "微软正在开发基于 snaplayout 的工作区功能。"
source: v2ex
url: "https://www.v2ex.com/t/1235717"
author: "flyficks"
date: 2026-08-19
score: 2
tags: ["deepseek"]
---

# 微软正在开发基于 snaplayout 的工作区功能。

前情提要
如果有人用过 power toys 中的工作区功能，应该知道它并不是基于 window 原生 snap layout(也就是 win+z 或者是拖拽窗口到顶部出现的布局栏)实现的，而是单纯的通过坐标的位置复现。
而 lz 前两天想要找一个通过 snaplayout 实现的工作区软件，发现并没有，问了一下 codex 是因为微软没有公开这个功能的接口。然后我用 codex 逆向找到了这个接口，叫 WindowsUdk.UI.Shell.SnapLayoutManager 。位置是在 C:\Windows\System32\windowsudk.shellcommon.dll 里。在这里我并没有太过在意，因为 lz 本身虽然专业对口，但是大学生涯基本什么都没学，只是让 codex 继续实现这个软件。后续在实现基本功能但是很多 bug 的时候 codex 没额度了，所以就暂时搁置了。
然后今天配置了一下 deep seek harness ，为了测试让他看了一下这个软件。后面问着问着就问到软件的可复用性，因为 lz 的系统是 Windows 最新的 27h2 29639.1000.  所以 deepseek 把从 21H2 到最新 24H2 的七个版本的这份 DLL 全部下载下来做了静态分析。
结论
这里因为 lz 没有任何专业知识储备，直接展示了 deep seek 的原话，如下：

…(内容已截断)

## 涉及话题
- deepseek

[原文链接](https://www.v2ex.com/t/1235717)
