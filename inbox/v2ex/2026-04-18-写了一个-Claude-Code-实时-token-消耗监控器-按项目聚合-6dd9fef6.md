---
title: "写了一个 Claude Code 实时 token 消耗监控器，按项目聚合"
source: v2ex
url: "https://www.v2ex.com/t/1206874"
author: "SIFT2009"
date: 2026-04-18
score: 0
tags: ["Claude", "claude", "ai", "Ai"]
---

# 写了一个 Claude Code 实时 token 消耗监控器，按项目聚合

写了一个 Claude Code 实时 token 消耗监控器，按项目聚合，带 TUI
用 Claude Code 做项目开发的时候，经常开好几个会话切来切去，到了月底看账单才发现某个项目烧了几十刀。Claude 自带的 /cost 只能看当前会话，没有项目维度的聚合，也不能实时看。
所以写了 cc-monitor 这个小工具，核心就几个功能：
能做什么

按项目聚合 — 同时监控多个项目的 token 消耗和费用
实时 TUI — 终端界面每 2 秒刷新，最近的操作记录会自动轮播
双数据源 — JSONL 日志（精确）+ PostToolUse Hook （实时时序）
费用估算 — 按模型定价自动算，Sonnet / Opus / Haiku 都支持
Compact 检测 — 自动识别上下文压缩，显示节省了多少 token

安装使用
git clone https://github.com/SagesAi/claude-cost-monitor.git
cd claude-cost-monitor
python -m pip install -e .
cc-monitor-install    # 一键安装 hook
cc-monitor &          # 后台启动 monitor
cc-monitor-tui        # 启动终端 UI

TUI 长这样
┌─────────────────────────────────────────────────────────────────┐
│ cc-monitor  ● hook  ● jsonl  refreshed 14:38:42  total: $7.72   │

…(内容已截断)

## 涉及话题
- Claude
- claude
- ai
- Ai

[原文链接](https://www.v2ex.com/t/1206874)
