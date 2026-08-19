---
title: "做了一个 chrome 插件，让 agent 自动化你的浏览器"
source: v2ex
url: "https://www.v2ex.com/t/1230768"
author: "cobiao"
date: 2026-07-29
score: 4
tags: ["Claude", "ai", "AI agent"]
---

# 做了一个 chrome 插件，让 agent 自动化你的浏览器

独立开发者，做了个 Chrome 扩展 WebCLI ，刚上架商店，来求点真实反馈。
我平时工作学习基本就在 terminal 和浏览器之间，一直想把浏览器这边的重复操作也自动化掉。类似的插件试了一圈，要么太重，要么功能太受限，干脆自己写一个，顺便当作学习。
它做的事很简单: 把你登录的 Chrome 变成外部 AI agent 的手。本身没有 agent 、没有界面，只有一个显示连接状态的 popup; 外部 agent 你自己搭(Claude Code 、Codex ，或者任何能发 HTTP 请求的东西)，WebCLI 只负责执行。
一共 25 个工具，开关标签页、读页面、点击输入、搜索抓链、截图这些，解包不到 300 KB ，基本覆盖手动能在浏览器里做的事。
怎么用，很简单：

webstore 安装 WebCLI
让你的 agent 安装 skill(npx skills add whitefoxx/webcli-skills -g)，然后 agent 就知道怎么使用了

权限有点多(debugger、<all_urls> 这类)，慎重，因为它做的就是代替你操作整个浏览器。过几天我整理下代码，然后开源出来，目前只开源了 skills
商店: https://chromewebstore.google.com/detail/webcli/jnhfdhpafndcbppkphhfpecflhogngge
daemon + skill(已开源): https://github.com/whitefoxx/webcli-skills

## 涉及话题
- Claude
- ai
- AI agent

[原文链接](https://www.v2ex.com/t/1230768)
