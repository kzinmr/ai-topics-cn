---
title: "做了一个 macOS 菜单栏小工具： AI997，让 AI Agent 跑任务时 Mac 不锁屏"
source: v2ex
url: "https://www.v2ex.com/t/1230244"
author: "jinfeng333"
date: 2026-07-27
score: 0
tags: ["AI Agent", "Cursor", "claude", "Claude", "ai", "AI", "cursor"]
---

# 做了一个 macOS 菜单栏小工具： AI997，让 AI Agent 跑任务时 Mac 不锁屏

大家好，最近用 Claude Code / Codex / Cursor 跑任务时经常遇到一个问题：人去倒杯水、吃个饭，Mac 自己熄屏锁住了，Web coding / Agent 任务也容易中断。
所以做了一个很小的 macOS 菜单栏 App ，叫 AI997。
一句话：人类下班，AI 997 。




它的作用很简单：点一杯“电子咖啡”，Mac 在对应时间里保持亮屏，不熄屏、不锁屏、不睡眠。时间到了自动恢复系统原来的行为。
功能：

2 小时：小加一班，适合改 bug
10 小时：白班连夜班，适合跑一个完整工作日
24 小时：997 全勤，适合通宵任务
无限模式：直到手动宣布下班
菜单栏实时倒计时
可随时加钟 +2h
到点自动通知
本地检测 claude / cursor / codex 等 Agent 进程，不联网

实现上用的是 macOS 的 IOKit 电源断言，和系统 caffeinate 是同一类机制。它不会改系统设置，也不需要管理员权限；退出 App 或手动下班后，系统原来的锁屏/睡眠策略会立即恢复。
目前是 v1.0.0 ，自用和分享给朋友都可以。还没做 Apple 公证，所以首次打开会被 macOS 提示“无法验证开发者”，右键打开即可。
GitHub：
https://github.com/wujunze/ai997
下载：
https://github.com/wujunze/ai997/releases/tag/v1.0.0
欢迎试用，也欢迎提建议。后面可能会补 Developer ID 公证、更多 Agent 状态展示，以及更好玩的“咖啡续杯”交互。

## 涉及话题
- AI Agent
- Cursor
- claude
- Claude
- ai
- AI
- cursor

[原文链接](https://www.v2ex.com/t/1230244)
