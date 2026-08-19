---
title: "Gitea Runner Manager：把 act_runner 装进原生图形界面"
source: v2ex
url: "https://www.v2ex.com/t/1230838"
author: "duguying"
date: 2026-07-29
score: 0
tags: ["ai"]
---

# Gitea Runner Manager：把 act_runner 装进原生图形界面

自托管 CI 一直是件麻烦事：装一条 Runner 要找二进制、手写 config.yaml、拼凑注册 Token 、想个办法让它常驻后台、还要再去翻日志排查任务失败。act_runner 的命令行虽然称职，但全靠文档和记忆堆出来的体验，对只想跑构建的个人开发者并不友好。
Gitea Runner Manager（下称 GRM ）正是为了把这堆零碎操作压缩到「四步点击」而生的——它是一款同时提供 macOS 版（ SwiftUI 菜单栏应用）和 Windows 版（ WinUI 3 桌面应用）的图形化管理器，覆盖 act_runner 从下载安装、注册、守护进程启停到实时日志查看的全部生命周期。

官网：https://grm.duguying.net

一、为什么需要它
Gitea Actions 是目前最易自托管的 CI 方案之一，但 act_runner 的注册流程历来有点「反人类」：

注册 Token 是一次性、立刻过期的，从 Gitea 控制台复制回来再粘贴进命令行这一步容易误操作；
注册成功后 Gitea 下发的 HASHED-TOKEN 长效令牌落在 .runner 里，普通用户很难知道它存在哪、能不能改；
Runner 想常驻得用 systemd / launchd / nssm 各写一套，跨平台时每台机器重抄一次；
任务失败后想看 daemon 输出，要么开终端 tail -f，要么钻进 journalctl。

GRM 把这些路径都收编到了 UI 里：Token 怎么传、HASHED-TOKEN 落在哪、daemon 怎么启停、日志在哪看——全部图形化。
二、核心特性
1. 一站式 Runner 生命周期

下载安装：从 Gitea 官方 API 拉取 act_runner 版本列表，Windows 版对下载的二进制做 SHA256 校验；

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1230838)
