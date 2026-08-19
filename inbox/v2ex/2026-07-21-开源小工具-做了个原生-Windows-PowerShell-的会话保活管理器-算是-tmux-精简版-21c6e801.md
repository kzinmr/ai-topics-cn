---
title: "开源小工具: 做了个原生 Windows PowerShell 的会话保活管理器, 算是 tmux 精简版"
source: v2ex
url: "https://www.v2ex.com/t/1228855"
author: "dualface"
date: 2026-07-21
score: 1
tags: ["ai"]
---

# 开源小工具: 做了个原生 Windows PowerShell 的会话保活管理器, 算是 tmux 精简版

一直很喜欢 tmux, 尤其是就算关闭终端窗口也不会丢会话. 但是 Windows 里如果不用 WSL, 就没找到靠谱的类似方案. 折腾了一阵 msys2 的 tmux, 一言不合就卡死, 也找不到原因.
后来干脆自己糊了一个, 啊哈哈.
https://github.com/dualface/qscreen/blob/main/README_CN.md
只实现了最小功能集, 重点就是原生 Windows PowerShell 的会话保活和切换. 也加了个状态栏和会话列表界面, 切割窗口这些功能就没做了.
来两张截图就懂了.




顺便再宣传一下我的 QuickTUI, 我可以负责任的说是市面上对远程终端支持最好的 iOS App. 很多细节功能用了就知道多么爽.
网址: https://quicktui.ai/

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1228855)
