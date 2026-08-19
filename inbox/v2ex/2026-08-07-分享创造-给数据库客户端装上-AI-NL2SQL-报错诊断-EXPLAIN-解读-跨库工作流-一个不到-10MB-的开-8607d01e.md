---
title: "[分享创造] 给数据库客户端装上 AI： NL2SQL、报错诊断、EXPLAIN 解读、跨库工作流，一个不到 10MB 的开源工具"
source: v2ex
url: "https://www.v2ex.com/t/1232833"
author: "flyxl"
date: 2026-08-07
score: 0
tags: ["mcp", "Anthropic", "OpenAI", "AI", "DeepSeek", "MCP"]
---

# [分享创造] 给数据库客户端装上 AI： NL2SQL、报错诊断、EXPLAIN 解读、跨库工作流，一个不到 10MB 的开源工具

断断续续写了几个月，DataZen 终于到了 v0.0.8 。起因很朴素：日常要连 PostgreSQL 、MySQL ，偶尔还要看 Redis ，商业客户端要订阅，DBeaver 功能全但启动和内存都偏重。于是用 Tauri v2 + Rust + React 自己搓了一个桌面客户端，安装包不到 10MB ，GPLv3 开源，macOS 和 Windows 都支持。
主界面长这样：一个窗口管理所有连接，PostgreSQL / MySQL / SQLite / Redis 混在一起也没问题。

🤖 AI 这块是重头
最常用的是自然语言生成 SQL 。想不起来表名或函数？直接说人话，AI 会结合当前库的表结构生成 SQL ，流式输出，点一下就能执行：

写错 SQL 也不用再去搜索引擎了。报错之后点「诊断」，AI 会告诉你错在哪、为什么错，修正后的 SQL 一键应用。比如我把 SELECT 拼成 SELEC，AI 直接指出少了字母 T：

慢查询怎么优化？ EXPLAIN 执行计划可视化，树形展示每一步的代价，再让 AI 解读瓶颈在哪：

📊 图表
查询结果不用导出到 Excel 了。一键从表格切到图表，自动推断字段类型、智能推荐图表类型，折线、柱状、饼图、散点、面积五种，支持导出 PNG / SVG：

⚙️ Workflow 跨库自动化
这版我最满意的功能：用 YAML 把「查数 → 分析 → 决策」固化成流程，支持跨库执行。比如从 PG 订单库查出订单，再去 MySQL 物流库补物流信息：

每个步骤可以绑定不同连接，支持条件分支、循环、错误策略（ abort / skip / fallback ），还能在界面、MCP 或者 AI 对话里直接跑。
其他值得一提的


…(内容已截断)

## 涉及话题
- mcp
- Anthropic
- OpenAI
- AI
- DeepSeek
- MCP

[原文链接](https://www.v2ex.com/t/1232833)
