---
title: "做了个 macOS 菜单栏小工具：同时跑多个 Codex 任务时一眼看状态"
source: v2ex
url: "https://www.v2ex.com/t/1231028"
author: "fizzy798"
date: 2026-07-30
score: 0
tags: ["ai", "OpenAI", "Prompt"]
---

# 做了个 macOS 菜单栏小工具：同时跑多个 Codex 任务时一眼看状态

同时开着几个 Codex Desktop / CLI 任务时，我经常要反复切回 Codex 确认：哪些还在跑、哪些已经有结果、哪些在等我批准或回答。
所以做了 AgentMicro：一个本地优先、只读的 macOS 菜单栏小工具，专门观察 Codex 任务状态。
它会在菜单栏图标和下拉菜单里显示最近任务：

白色：空闲
绿色：有未读完成结果
蓝色：正在思考/执行
橙色：等待批准、回答或浏览器交互
红色：当前任务遇到阻塞错误

正在工作的任务会排在最前面；每行显示任务标题、项目、当前 turn 已运行多久，快速模式还会标一个闪电。点击 Codex Desktop 任务可直接回到对应会话。
几个边界也写得比较严格：

只读取已知的本地 Codex 进程与会话元数据，不上传任务标题、Prompt 、回复、源代码或命令输出
不需要 Full Disk Access ，也不读 Keychain
基础模式不需要辅助功能权限；可选的增强检测只有用户主动开启后才会本地只读识别当前选中任务与可见的审批/错误控件，不会点击、输入或批准
目前只做 Codex 观察与跳转，不做 token/额度监控、不代替用户控制任务

项目是独立的社区维护开源项目，基于 CodexBar 的部分底座开发；与 OpenAI 和 CodexBar 维护者没有官方隶属关系。
macOS 14+，支持 Apple Silicon 和 Intel 。

项目： https://github.com/fizzy718/AgentMicro

下载： https://github.com/fizzy718/AgentMicro/releases/latest
欢迎试用，尤其想听听大家对状态语义、菜单栏信息密度和多任务工作流的反馈。

## 涉及话题
- ai
- OpenAI
- Prompt

[原文链接](https://www.v2ex.com/t/1231028)
