---
title: "做了一个 macOS 菜单栏小工具，用来统一看 Vercel / Railway / GitHub 等部署状态"
source: v2ex
url: "https://www.v2ex.com/t/1215333"
author: "xiangwu"
date: 2026-05-25
score: 0
tags: ["ai"]
---

# 做了一个 macOS 菜单栏小工具，用来统一看 Vercel / Railway / GitHub 等部署状态

大家好，我做了一个小工具：DeployBar 。
它是一个免费、开源、local-first 的 macOS 菜单栏 App ，用来统一查看不同平台的部署状态，适合项目分散部署在多个 provider 的情况。
目前支持：

Vercel
Railway
Netlify
Render
Cloudflare Pages
DigitalOcean App Platform
Heroku
GitHub Deployments
GitLab Deployments

几个特点：

原生 macOS App ，不是 Electron
没有后端服务，不需要注册账号
Provider token 存在 macOS Keychain
支持部署状态变化通知
MIT 开源

安装：
brew install --cask snapre/tap/deploybar

GitHub：
https://github.com/snapre/DeployBar
官网：
https://deploy.bar
现在还比较早期，想听听大家反馈：

这类菜单栏部署状态工具对你有用吗？
你更关心部署成功 / 失败状态，还是失败日志和诊断信息？
本地 Keychain 存 token + 开源代码，这个信任模型是否能接受？

欢迎拍砖。

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1215333)
