---
title: "在 Windows 上部署 Woodpecker agent ，实现 Windows 上的 CI"
source: v2ex
url: "https://www.v2ex.com/t/1212542"
author: "AhFei"
date: 2026-05-13
score: 0
tags: ["ai"]
---

# 在 Windows 上部署 Woodpecker agent ，实现 Windows 上的 CI

我需要在 Windows 上编译 flutter 应用，因此需要在 Windows 系统上部署 Woodpecker agent 。
下面是我花了一整天的时间，探索出的方案，可以完美运行。
前置准备

在 Windows 上安装 git
把这个路径加入环境变量里系统的 PATH C:\Program Files\Git\usr\bin，这里面提供了 cat 等工具
在 Woodpecker 网页上注册一个 agent token ，参考 https://woodpecker-ci.org/docs/administration/configuration/agent#using-agent-token
建议安装 curl ，下载网址 https://curl.se/windows/ ，下载后就是一个可执行文件，将之放到任意文件夹，然后将其所在目录添加到环境变量里
建议安装 Woodpecker 的 git 插件 https://woodpecker-ci.org/plugins/git-clone ，clone 仓库需要它，也是一个单纯的可执行文件，下载后，推荐放到 C:\woodpecker_plugin ，然后把这个路径添加到环境变量里

安装

创建 C:\tmp 作为工作目录。因为 Windows 对路径名称有长度限制，而 agent 默认的工作目录路径很长，对于 flutter 项目，很容易触发长度限制导致编译失败
在 https://github.com/woodpecker-ci/woodpecker/releases 里下载对应的 agent ，需要和服务端的版本号一样



…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1212542)
