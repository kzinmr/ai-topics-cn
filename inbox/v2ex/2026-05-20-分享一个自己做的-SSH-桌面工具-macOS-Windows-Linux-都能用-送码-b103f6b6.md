---
title: "分享一个自己做的 SSH 桌面工具， macOS / Windows / Linux 都能用 [送码]"
source: v2ex
url: "https://www.v2ex.com/t/1213996"
author: "dushixiang"
date: 2026-05-20
score: 90
tags: ["Claude", "AI"]
---

# 分享一个自己做的 SSH 桌面工具， macOS / Windows / Linux 都能用 [送码]

大家好，我做了一个桌面端 SSH 终端管理工具，叫 Termark。
官网：https://www.termark.app
简单说，它是给经常连服务器的人用的。平时要找机器、找账号、找密钥、开终端、传文件、做端口转发、批量查几台机器状态、看日志、问 AI 报错原因，这些事情单独看都不复杂，但每天重复很多次就很烦。
Termark 想解决的就是这些碎事。

功能

资产管理：SSH / Telnet / 串口 / 本地终端 / NextTerminal
终端：多标签、分屏、搜索、自动重连、命令片段、关键字高亮
文件传输：SFTP 、目录跟随、文件夹上传、批量下载、lrzsz / ZModem
批量执行：多台机器同时执行命令，输出独立显示
端口转发：本地转发、远程转发、规则保存
会话记录：终端录制、回放、下载录像
AI 助手：跟随当前终端上下文，支持多会话、对话历史、模型切换、命令确认
外部 CLI：给 Codex / Claude / OpenCode 调用资产、执行命令、上传下载文件
同步：官方同步、WebDAV 、S3 、iCloud 、本地目录，客户端加密后上传
安全和兼容：本地数据加密、应用锁、GBK 、老旧主机算法、keyboard-interactive 、SSH keepalive

开源吗？
不开源。
我知道很多人会先问这个。但我自己的判断是，很多人真正看中的不是“开源”两个字，而是能不能免费用、会不会被订阅绑住、基础功能是不是够完整。
所以 Termark 的策略是：本地功能免费使用。
日常 SSH 、SFTP 、端口转发、命令片段、AI 助手、NextTerminal 资产访问这些都可以免费用。收费主要放在云同步、多设备授权、进阶能力和后续服务上。
移动端计划下个月开始开发，到时候也会围绕多设备同步继续做。
和其他工具比，优势是什么？

…(内容已截断)

## 涉及话题
- Claude
- AI

[原文链接](https://www.v2ex.com/t/1213996)
