---
title: "最近把我们的 Amazon Scrape API 封装成了 Agent Skill，顺便聊聊为什么数据层对电商 Agent 来说这么关键"
source: v2ex
url: "https://www.v2ex.com/t/1211499"
author: "pangolin2023"
date: 2026-05-09
score: 0
tags: ["AI", "大模型", "ai", "推理", "Cursor", "Claude"]
---

# 最近把我们的 Amazon Scrape API 封装成了 Agent Skill，顺便聊聊为什么数据层对电商 Agent 来说这么关键

先说背景：我们做 Pangolinfo 已经有一段时间了，核心产品是 Amazon Scrape API ，服务的主要是需要批量采集亚马逊数据的开发者和跨境电商团队。
最近 Agent 这波起来之后，陆续有用户问能不能直接在 OpenClaw 、Claude Code 、Cursor 这类工具里调用我们的数据能力。于是我们在原有 API 基础上封装了一套 Skill ，叫 Pangolinfo Amazon Scraper Skill，想借这个机会和大家聊聊。
先说一个容易被忽视的问题：数据对电商 Agent 意味着什么
现在很多人在讨论 Agent 的推理能力、工具调用、工作流编排，但做跨境电商的场景有个特殊性——亚马逊的数据是实时在变的。
价格每天在动，竞品库存随时清空，Best Sellers 榜单每小时刷新，新品 Review 在大促期间几百条往上涌。
如果你的 Agent 是基于静态知识或者昨天的快照在做决策，那分析出来的结论可能已经过期了。真正有价值的电商 Agent ，数据底座必须是实时的、全量的、结构化的。
这也是我们做这件事的出发点。
自己抓行不行？客户踩过的坑
客户在寻找我们之前，也经历过"自己写爬虫"的阶段，几乎都遇到过几个坎：

亚马逊的风控在持续收紧，Canvas 指纹、WebGL 检测、行为分析，普通 Playwright 脚本并发一上去就是 503 或者无限验证码
原始 HTML 动辄几百 KB ，直接喂给大模型不只是 token 贵的问题，更容易产生幻觉，字段解析出错
亚马逊页面结构隔一段时间就改，selector 维护成本极高

所以我们选择在云端把这层全部消化掉，对外只暴露干净的结构化 JSON 。
Skill 具体能做什么
安装一行命令：

…(内容已截断)

## 涉及话题
- AI
- 大模型
- ai
- 推理
- Cursor
- Claude

[原文链接](https://www.v2ex.com/t/1211499)
