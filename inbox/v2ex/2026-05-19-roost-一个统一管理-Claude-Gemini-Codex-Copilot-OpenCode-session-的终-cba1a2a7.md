---
title: "roost 一个统一管理 Claude/Gemini/Codex/Copilot/OpenCode session 的终端工具"
source: v2ex
url: "https://www.v2ex.com/t/1213843"
author: "endoffight"
date: 2026-05-19
score: 1
tags: ["Claude", "Copilot", "AI", "Gemini"]
---

# roost 一个统一管理 Claude/Gemini/Codex/Copilot/OpenCode session 的终端工具

日常开发中频繁切不同 AI coding tool ，会话散落在各处不好找，写了个小工具统一管理。
roost 做的事很简单：扫描本机已安装的 AI coding tool 的数据目录，把所有项目的会话聚到一个 TUI 里，一键 resume 或新建。
支持的平台：Claude 、Gemini 、Codex 、Copilot 、OpenCode
主要功能：

项目→会话两级浏览，按最近活跃排序
Enter resume 会话，n 选择 agent 新建会话
/ 搜索、Tab 按平台过滤、Space 批量选择删除
两种 resume 模式：replace （替换进程，退出回 shell ）和 suspend （子进程，退出回 TUI ）
支持 --list --json 输出，可对接脚本
各平台额外参数通过 ~/.roost/roost.yaml 配置

安装：go install github.com/phpgao/roost@latest
GitHub: https://github.com/phpgao/roost
欢迎使用，欢迎提 BUG

## 涉及话题
- Claude
- Copilot
- AI
- Gemini

[原文链接](https://www.v2ex.com/t/1213843)
