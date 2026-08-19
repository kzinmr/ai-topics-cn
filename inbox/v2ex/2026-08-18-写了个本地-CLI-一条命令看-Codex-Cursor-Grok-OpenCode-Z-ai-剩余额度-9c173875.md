---
title: "写了个本地 CLI：一条命令看 Codex / Cursor / Grok / OpenCode / Z.ai 剩余额度"
source: v2ex
url: "https://www.v2ex.com/t/1235350"
author: "NoOneAI"
date: 2026-08-18
score: 2
tags: ["Cursor", "ai", "Claude", "ChatGPT", "OpenAI", "cursor", "coding agent"]
---

# 写了个本地 CLI：一条命令看 Codex / Cursor / Grok / OpenCode / Z.ai 剩余额度

最近本地 coding agent 越装越多。真正卡手的往往不是模型选哪个，是开一个长任务前，不知道这家订阅还剩多少额度。

每个厂商一张账本，入口还不一样：有的在网页 dashboard ，有的绑桌面登录态，有的看 ChatGPT 套餐。额度接口基本都不当公开稳定 API 文档化。

所以写了 ai-quota 。非官方，一条命令读本机已有登录态，把 Codex 、ZCode/Z.ai 、OpenCode Go 、Grok 、Cursor 的剩余额度打出来。默认只读。Token 不出本机，只发给对应厂商。

注意：

- 不是官方工具，接口随时可能变或挂
- Claude 还没接
- Codex 用的是 ChatGPT 登录，不是 OpenAI API key
- Cursor 读的是桌面端登录，不是 cursor-agent login

仓库： https://github.com/hunterzhang86/ai-quota

有同类痛点的可以试试。也欢迎拍接口变更和缺的厂商。

## 涉及话题
- Cursor
- ai
- Claude
- ChatGPT
- OpenAI
- cursor
- coding agent

[原文链接](https://www.v2ex.com/t/1235350)
