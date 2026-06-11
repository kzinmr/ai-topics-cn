---
title: "为什么我的 AgentTeam 无法是这样的？"
source: v2ex
url: "https://www.v2ex.com/t/1216719"
author: "konakona"
date: 2026-05-30
score: 2
tags: ["Claude"]
---

# 为什么我的 AgentTeam 无法是这样的？

版本
我好像从 2.1.x （ 4 月底版本） 开始就用不起，我看到有些网友可以用上，狠狠羡慕了。前几天升级了 Claude ，还是用不上。
当前版本是： 2.1.148 (Claude Code)
测试用消息
接下来，请准备 Agent Team ，必须使用 Split panes 模式，每个 teammate 一个 pane 。
创建 3 个角色：
玩家 1
玩家 2
玩家 3

这 3 个玩家一直分别从 0 到 10 数数，每隔 2 秒数 1 次，数完了依次通报给 Lead ，然后由 Lead 告诉我。
Lead 要每隔 2 秒监督这 3 个角色有正确的数数，如果有任意玩家没有按预期每隔 2 秒（你可以预设 3 秒就是 timeout ）就立刻告诉我。
坚决不可以由 Lead 自行完成 3 个角色的工作，如果发现必须这么做，则终止 Team 的工作并用 Claude 日志向我汇报。


无论是复杂项目开发，还是简单的轮询，AgentTeam 中的子 Agent 完全不会工作，不会消耗 tokens ，无法分派任务。Lead 包办所有任务。

问题截图

## 涉及话题
- Claude

[原文链接](https://www.v2ex.com/t/1216719)
