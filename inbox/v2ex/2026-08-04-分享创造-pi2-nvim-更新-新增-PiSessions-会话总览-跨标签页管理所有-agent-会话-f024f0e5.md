---
title: "分享创造： pi2.nvim 更新 —— 新增 :PiSessions 会话总览，跨标签页管理所有 agent 会话"
source: v2ex
url: "https://www.v2ex.com/t/1232028"
author: "yuez"
date: 2026-08-04
score: 0
tags: ["AI", "ai", "编程助手", "coding agent"]
---

# 分享创造： pi2.nvim 更新 —— 新增 :PiSessions 会话总览，跨标签页管理所有 agent 会话

上次发帖介绍了 pi2.nvim 1.0 ，这次带来一个重要更新：会话列表（:PiSessions）。
先给新来的朋友简单介绍：pi2.nvim 是 pi coding agent 的 Neovim 前端，基于 alex35mil/pi.nvim 深度扩展的 fork （上游的功劳归上游），在后台跑 pi --mode rpc，把 AI 编程助手完整搬进编辑器。设计上「一个标签页 = 一个会话」，多任务时经常同时开好几个标签页跑不同的 agent 。
新功能 :PiSessions：所有活跃会话的实时总览
一个只读窗口列出全部活跃会话，每行 = 标签页编号 + 状态点 + 会话名：

状态点快闪：agent 正在干活（流式输出 / 执行工具）
慢闪：正在压缩上下文（ compaction ）
常亮警告色：有待处理的 attention 请求
绿灯闪烁：别的标签页的回合完成了，你还没看
红灯闪烁：上次回合出错，你还没看
常亮暗淡：空闲
常亮错误色：会话已退出

会话名优先取 :PiSessionName 设置的名称，否则回退到第一条用户消息。按 <CR> / o 直接跳到对应标签页并打开聊天，r 刷新会话名，q 关闭。
实现上的两个细节：所有标签页共享同一个 buffer ，一次重绘同步刷新所有视图；更新完全事件驱动、零轮询。
配置：
require("pi").setup({
  sessions_list = {
    mode = "follow",   -- "follow" | "side" | "float"
    position = "left",
    width = 40,
    height = 12,
    float = { width = 0.5, height = 0.5 },

…(内容已截断)

## 涉及话题
- AI
- ai
- 编程助手
- coding agent

[原文链接](https://www.v2ex.com/t/1232028)
