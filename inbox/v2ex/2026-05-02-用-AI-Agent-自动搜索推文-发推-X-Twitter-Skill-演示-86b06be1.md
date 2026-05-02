---
title: "用 AI Agent 自动搜索推文、发推 — X (Twitter) Skill 演示"
source: v2ex
url: "https://www.v2ex.com/t/1209965"
author: "gbin"
date: 2026-05-02
score: 1
tags: ["AI", "AI Agent", "编程助手", "ai", "AI agent", "Cursor", "Claude"]
---

# 用 AI Agent 自动搜索推文、发推 — X (Twitter) Skill 演示

做了一个 X (Twitter) 的 AI Agent Skill ，让你的编程助手（ Claude Code 、Cursor 等）可以直接操作 Twitter：搜索推文、看用户资料、发推、点赞、转推、关注等。
Demo

演示流程：输入一句话让 AI 搜索 "Agent Authentication" 相关推文 → AI 自动调用脚本搜索 → 展示结果 → 确认后自动发送回复。全程在终端完成。
工作原理
基于 SigCLI —— 一个 AI Agent 认证工具。你只需要在浏览器登录一次 x.com ，sig 就会提取并加密保存 cookie ，之后 AI Agent 通过 sig run x 拿到凭证来调用脚本。
# 安装
npm install -g @sigcli/cli
npx @sigcli/skills x

# 登录（只需一次）
sig login https://x.com

# AI Agent 就可以用了
sig run x -- python3 scripts/x_search.py --query "AI agents"

除了 X ，还有这些 Skill



Skill
平台
能做什么




Outlook
邮件
收发邮件、搜索、管理文件夹


Slack
聊天
读消息、搜索、发消息


Reddit
论坛
浏览、搜索、发帖、评论


Hacker News
论坛
浏览、搜索、评论、投票


YouTube
视频
搜索、看评论、点赞、订阅


Bilibili
视频
热门、搜索、点赞、投币


LinkedIn
职场
看资料、搜索职位、发帖


V2EX
论坛
热帖、搜索、发帖、回复

完整列表和文档： https://sigcli.ai/skills/
链接


…(内容已截断)

## 涉及话题
- AI
- AI Agent
- 编程助手
- ai
- AI agent
- Cursor
- Claude

[原文链接](https://www.v2ex.com/t/1209965)
