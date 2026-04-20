---
title: "做了个 Claude Code 多账号切换启动器，不用再反复 /login 了"
source: v2ex
url: "https://www.v2ex.com/t/1207236"
author: "purewater2018"
date: 2026-04-20
score: 0
tags: ["MCP", "ai", "Claude", "claude"]
---

# 做了个 Claude Code 多账号切换启动器，不用再反复 /login 了

背景：自己有 2 个 Claude Pro 账号轮着用，5 小时限制一到就得 /login 重登，非常烦。
试过社区的 cc-switch ，但它核心是切 API 供应商配置，加两个官方 OAuth 账号时第二个会把第一个覆盖掉。Claude Code 1.0.61 之后支持 --settings 手动指定配置文件，也能用，就是每次都要敲路径。
于是索性做了个小工具，叫 Claude Launcher ，专门解决官方多账号切换的问题。
它做了什么

每个账号一个独立加密 profile，互不覆盖
列表点一下就切号，自动把对应 token 写入 Claude Code 的共享凭证
双向 token 同步：Claude Code 后台刷新的新 token 会同步回 profile ，下次启动用最新的
自动安装 Claude Code（首次使用免手动配置）
Windows 自动检测并安装 Git Bash
UI 里选模型 / 权限模式 / effort / --continue，自动拼启动参数
macOS / Linux / Windows 三端可用


技术栈
Go + Wails ，原生窗口，启动快，不吃内存。
Profile 用 AES 加密 + 机器 ID 绑定，换机失效（避免 profile 文件被直接复制走）。
启动终端的方式按平台区分：

macOS：osascript 调 Terminal.app
Linux：gnome-terminal → xterm → konsole 依次 fallback
Windows：git-bash.exe -c，支持代理环境变量

使用流程

OAuth 登录 Claude 账号（或从本机 Keychain / .credentials.json 一键导入）
给 profile 命名

…(内容已截断)

## 涉及话题
- MCP
- ai
- Claude
- claude

[原文链接](https://www.v2ex.com/t/1207236)
