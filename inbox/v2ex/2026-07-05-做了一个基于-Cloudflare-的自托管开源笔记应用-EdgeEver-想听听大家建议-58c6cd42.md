---
title: "做了一个基于 Cloudflare 的自托管开源笔记应用 EdgeEver，想听听大家建议"
source: v2ex
url: "https://www.v2ex.com/t/1225143"
author: "mayinshi"
date: 2026-07-05
score: 0
tags: ["Claude", "ai", "AI Agent", "MCP"]
---

# 做了一个基于 Cloudflare 的自托管开源笔记应用 EdgeEver，想听听大家建议

最近做了一个开源项目 EdgeEver，想来分享一下，也听听 V 友的建议。
项目地址： https://github.com/msh01/edgeever

在线演示： https://demo.edgeever.org
Demo 账号：ee-demo

Demo 密码：demo#dZ6Q29Zjfor%
它的定位是：基于 Cloudflare 全家桶自托管的开源笔记工作区，有点像一个更轻量、开放数据、适合个人部署的 Evernote / 印象笔记替代品。
为什么做这个：

我自己还是比较喜欢经典印象笔记那种三栏结构：笔记本树、笔记列表、编辑区
但现在很多商业笔记产品越来越重，迁移和导出也不够自由
Memos 这类工具很轻，但和传统笔记本/三栏工作流又不太一样
Cloudflare Workers + D1 + R2 的免费额度对个人知识库其实挺合适，不太需要维护服务器

目前已经有的功能：

三栏布局，支持无限级嵌套笔记本
富文本编辑，底层是 TipTap / ProseMirror
笔记历史版本
图片和附件，前端本地压缩后上传到 R2
多选合并笔记、多选移动笔记、笔记本拖拽排序
PWA ，桌面和手机浏览器都能用
已有笔记支持离线草稿和本地同步队列
REST API / OpenAPI / CLI
MCP endpoint ，可以授权给 Codex 、Claude Code 等 Agent 读取和整理笔记

部署方式大概是：Fork 仓库，配置 Cloudflare 登录态，然后执行：
bun install
EDGE_EVER_PASSWORD='<首次登录密码>' bun run deploy:setup
bun run deploy:doctor
bun run deploy


…(内容已截断)

## 涉及话题
- Claude
- ai
- AI Agent
- MCP

[原文链接](https://www.v2ex.com/t/1225143)
