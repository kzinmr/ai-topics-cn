---
title: "PowerShell 和 Codex 在打架？可以试试这份提示词"
source: v2ex
url: "https://www.v2ex.com/t/1228204"
author: "knowckx"
date: 2026-07-18
score: 23
tags: ["大模型", "AI"]
---

# PowerShell 和 Codex 在打架？可以试试这份提示词

今天花时间写了篇 codex 下使用 PowerShell 的文章 在 V2EX 上也发一份
背景
最近半年一直 Windows 下使用 Codex 开发项目，逐渐把开发环境打造得更接近 Linux 下的开发体验。最近看到很多人反馈 PowerShell 和 Codex 打架的情况，因为这问题我之前就解决了，所以想分享下我的方案。  
现在这套环境谈不上多复杂，主要有两个重点：

先把终端环境统一，再用提示词把大模型的命令习惯掰过来。
先安装 pwsh 7 和 Windows Terminal
如果你还在使用系统自带的 Windows PowerShell 5.1 ，我建议先换成现代 shell：PowerShell 7 （ pwsh ）。
至于 PowerShell 5.1 和 PowerShell 7 的区别，可以找 AI 给你解释一下，但是结论不变:

现代 Windows 开发环境最好统一到 pwsh 7 。
可以直接用 winget安装：
winget install --id Microsoft.PowerShell --source winget

也可以从 PowerShell 官方安装页面 下载 MSI 安装包手动安装。
安装后验证，在命令行中输出版本号:
PS C:\Users\AAA> pwsh -v
PowerShell 7.x

原生的 PowerShell 界面很丑，所以必安装另一个 Windows 神器 Windows Terminal

它的价值不只是好看，而是把 pwsh、Git Bash 、远程 SSH 等环境放在同一个窗口里管理，支持标签页、分屏、统一的字体和编码设置。平时一边让 Codex 在一个窗口里执行命令，一边查看日志或运行服务，效率会高很多。

…(内容已截断)

## 涉及话题
- 大模型
- AI

[原文链接](https://www.v2ex.com/t/1228204)
