---
title: "win 系统下 codexcli 在 vscode 启动的终端中无法通过滚轮查看消息记录的修复开源分支"
source: v2ex
url: "https://www.v2ex.com/t/1231537"
author: "xuanp1985"
date: 2026-08-02
score: 0
tags: ["cursor", "Cursor"]
---

# win 系统下 codexcli 在 vscode 启动的终端中无法通过滚轮查看消息记录的修复开源分支

在 win 平台使用以 vscode 为基础的二开 ide 的时候启动 ide 内的 terminal 运行 codexcli 时有 codexcli 的 tui 覆盖富文本滚轮规则导致滚轮无法直接滚动查看消息的问题。
针对上述问题做了一个修复版本分支并开源
开源仓库地址：GitHub： https://github.com/Little-Z7/codex-cursor-rich
Release： https://github.com/Little-Z7/codex-cursor-rich/releases/tag/v0.146.0-cursor.1 
项目简介：
• ##  [开源]  codex-cursor-rich
解决 Codex 在 Cursor/VS Code 的 WSL 终端中无法用滚轮回看历史的问题。

保留颜色、Markdown 、代码块等富文本样式
支持鼠标滚轮查看历史输出
不覆盖官方 codex
相关测试 86/86 通过

安装后运行：
codex-cursor-rich
GitHub： https://github.com/Little-Z7/codex-cursor-rich
Release： https://github.com/Little-Z7/codex-cursor-rich/releases/tag/v0.146.0-cursor.1

## 涉及话题
- cursor
- Cursor

[原文链接](https://www.v2ex.com/t/1231537)
