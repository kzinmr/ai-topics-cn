---
title: "做了一个 Neovim 里的 AI 编程 Agent 前端 pi2.nvim，开源求交流"
source: v2ex
url: "https://www.v2ex.com/t/1231354"
author: "yuez"
date: 2026-07-31
score: 0
tags: ["coding agent", "prompt", "Claude", "AI", "agi"]
---

# 做了一个 Neovim 里的 AI 编程 Agent 前端 pi2.nvim，开源求交流

背景
一直在用 pi coding agent 做日常开发，它是一个极简的终端 AI 编程 agent （类似 Claude Code / Codex CLI ，但更轻量、可定制）。上游有个 Neovim 前端 alex35mil/pi.nvim，我在上面加了不少自己需要的功能，越加越多，最后独立成了 pi2.nvim（π²），MIT 开源。

声明：pi2.nvim 是 alex35mil/pi.nvim 的 fork ，基础架构（ RPC 桥接、chat 布局、diff review 、session 管理）全部来自上游，在此致谢。本文只聊 fork 新增的部分。

演示
Agent 读文件 → 编辑 → 验证，带实时流式输出和 :PiTree 会话树导航：

相比上游多了什么

直接 bash 模式（!cmd）：在 prompt 里 ! 开头跑 shell ，输出流式进可折叠块，自动加入上下文
:PiTree 会话树导航：跳回会话任意历史节点，可选摘要放弃的分支、重新编辑 prompt 发送（相当于 pi TUI 的 /tree）
Per-tab 模型锁定：一个 tab 切模型不会污染其它 tab 的新会话
图片附件压缩：Retina 截图发送前自动缩放（ sips / magick / ffmpeg 自动探测），避免几 MB 的 PNG 吃 token
剪贴板图片自动附加、readline 风格 prompt 历史、未发送草稿持久化
双击 <Esc> 中断、prompt 状态栏（ spinner / 队列 / 中断提示，永远不滚走）
gf 打开光标下路径、grep/find 结果进 quickfix 、左侧面板、pi 改文件自动 reload buffer
可选 render-markdown.nvim 渲染引擎

安装

…(内容已截断)

## 涉及话题
- coding agent
- prompt
- Claude
- AI
- agi

[原文链接](https://www.v2ex.com/t/1231354)
