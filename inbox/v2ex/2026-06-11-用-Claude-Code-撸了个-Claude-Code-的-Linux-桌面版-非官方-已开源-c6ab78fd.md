---
title: "用 Claude Code 撸了个 Claude Code 的 Linux 桌面版（非官方），已开源"
source: v2ex
url: "https://www.v2ex.com/t/1219766"
author: "ydxred"
date: 2026-06-11
score: 0
tags: ["Claude", "MCP", "claude"]
---

# 用 Claude Code 撸了个 Claude Code 的 Linux 桌面版（非官方），已开源

官方的 Claude Code 桌面版只有 macOS / Windows ，Linux 只能用命令行。我自己用
Linux ，就做了个非官方桌面版，已开源。
思路很简单：不是重写客户端，而是用 Electron 套一个真实终端（ xterm.js +
node-pty ），里面跑你本机装好的 claude CLI 。所以命令行有的功能它全有——slash
命令、MCP 、插件、hooks 、skill 、权限交互，一个不少，只是多了个窗口外壳。
做了这些：

多标签页会话，每个标签可在不同目录
可视化「恢复会话」选择器（鼠标点选历史会话，不用敲 claude --resume ）
12 种界面语言（含阿拉伯语 RTL ）、5 套配色主题
打包成 AppImage 和 .deb ，应用图标 + Dock 集成

技术栈 Electron + xterm.js + node-pty ，在 Ubuntu 24.04 (Wayland + GNOME)
上开发测试。踩的坑（ chrome-sandbox 、libfuse2 、原生 Wayland
剪贴板不同步）都写在 README 里了。
GitHub： https://github.com/ydxred/claude-desktop
Release （ AppImage / deb ）： https://github.com/ydxred/claude-desktop/releases
纯个人项目、非官方，欢迎试用 / 提 issue 。

## 涉及话题
- Claude
- MCP
- claude

[原文链接](https://www.v2ex.com/t/1219766)
