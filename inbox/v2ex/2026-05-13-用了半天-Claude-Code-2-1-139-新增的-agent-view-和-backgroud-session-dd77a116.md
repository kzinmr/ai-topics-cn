---
title: "用了半天 Claude Code 2.1.139 新增的 agent view 和 backgroud session，有用但还是有不少问题"
source: v2ex
url: "https://www.v2ex.com/t/1212534"
author: "cadl"
date: 2026-05-13
score: 0
tags: ["Claude", "claude"]
---

# 用了半天 Claude Code 2.1.139 新增的 agent view 和 backgroud session，有用但还是有不少问题

260511 发布的 2.1.139 版本的 changelog 里第一项就是 Added agent view (Research Preview)。还比较少有地在 changelog 里加上了 agent view 的文档链接: https://code.claude.com/docs/en/agent-view
不知道大家用了这个功能没。今天白天尝试使用了小半天，发现有挺多亮点，也有一些槽点。也想听听大家关于它的看法。
agent view 是啥
这个 agent view 可以直接并行启动 claude session ，产生的 session 默认就使用 worktree 隔离了，可以并行执行没有文件冲突。而它启动的 background session ，是由一个独立的 supervisor 管理执行的，脱离了终端或者这个 agent view 仍会保持执行，关闭终端之后，background session 也会继续执行。 
使用 ps 查看进程，可以看到一个 claude daemon run --spawned-by xxxx PPID 为 1 的 supervisor 进程。我在一直没有留意过以前是否有这个 supervisor 进程。刚刚回退到 2.1.138 版本，貌似并不会启动它。在新版本里，使用 claude agents 、claude —bg 、\bg 时，就会启动这个 supervisor 进程。
使用体验
今天使用下来还是有几个明显不顺手的地方：

启动的 session 必开 worktree, 但是 session 列表上看不到分支的状态(能否合并、是否已合并等等)。导致要不断在 agent view 以外来确认分支状态……

…(内容已截断)

## 涉及话题
- Claude
- claude

[原文链接](https://www.v2ex.com/t/1212534)
