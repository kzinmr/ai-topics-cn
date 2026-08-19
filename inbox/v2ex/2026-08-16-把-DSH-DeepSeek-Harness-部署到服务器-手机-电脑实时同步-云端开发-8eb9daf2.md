---
title: "把 DSH（DeepSeek Harness）部署到服务器：手机、电脑实时同步，云端开发"
source: v2ex
url: "https://www.v2ex.com/t/1234815"
author: "longbill"
date: 2026-08-16
score: 0
tags: ["DEEPSEEK", "ai", "AI", "deepseek", "DeepSeek"]
---

# 把 DSH（DeepSeek Harness）部署到服务器：手机、电脑实时同步，云端开发

适用场景：你有一台服务器，想把 DeepSeek Harness 的浏览器界面（ Web GUI ）跑在上面，让家里的电脑、公司的电脑、甚至手机浏览器都能登录使用，用 AI 帮你写代码、跑任务。本文基于 DSH 0.1.0-rc.6 + Ubuntu 22.04/24.04 + nginx + pm2 的实际部署经验整理。

为什么需要服务器 + 反代
DSH 的 Web 界面（dsh --profile web）默认只监听 127.0.0.1:3080，而且出于安全考虑**禁止 --host 0.0.0.0**（ CLI 直接报错：防止把远程代码执行能力暴露到公网）。所以正确姿势是：
浏览器（手机/电脑）──► nginx （ 80/443 ）──► dsh web （ 127.0.0.1:3080 ）

nginx 做反向代理 + 登录保护 + 移动端适配，DSH 本身只在本机回环地址提供服务。

架构总览

dsh web：实际服务，监听 127.0.0.1:3080 
dsh-webui-auth 插件： 登录认证（未认证的浏览器拿不到任何资源） 
pm2： 守护进程 + 开机自启 
nginx： 对外入口，反代 + 移动端缩放 + manifest 直出 


第一步：安装 DSH
需要 Node.js ^22.19.0 || >=24.0.0：
npm install -g @deepseek-ai/dsh
dsh --version   # 验证安装

第二步：初始化 web profile 并安装认证插件
dsh --profile web 首次运行时自动初始化 profile （目录在 ~/.dsh/profiles/web）。先装登录认证插件（需要 pnpm ，Node 自带 corepack ）：
corepack enable pnpm

…(内容已截断)

## 涉及话题
- DEEPSEEK
- ai
- AI
- deepseek
- DeepSeek

[原文链接](https://www.v2ex.com/t/1234815)
