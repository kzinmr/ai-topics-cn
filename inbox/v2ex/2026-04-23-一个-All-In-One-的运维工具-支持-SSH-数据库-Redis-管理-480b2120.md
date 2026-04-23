---
title: "一个 All In One 的运维工具，支持 SSH、数据库、Redis 管理"
source: v2ex
url: "https://www.v2ex.com/t/1208061"
author: "CodFrm"
date: 2026-04-23
score: 2
tags: ["Claude", "ai", "Gemini", "AI Agent", "AI", "编程助手"]
---

# 一个 All In One 的运维工具，支持 SSH、数据库、Redis 管理

平时操作服务器环境，经常要打开好几个工具来回切换，于是做了 OpsKat ，一个 All In One 的运维工具，将用到的需要管理的服务器资产集中起来，再也不用像之前一样，跳来跳去了。
另外还集成了 AI Agent 系统，让运维工作更加轻松。
为什么又造一个轮子
说实话市面上 SSH 工具、数据库客户端、Redis GUI 一抓一大把，但我自己的工作流大概是这样：

Tabby 连 SSH
DataGrip 看数据库
TinyRDM 看 Redis
偶尔还要翻一下 k8s 、grafana 、es 等等

凭据散落在各处，切换窗口能切到怀疑人生。更麻烦的是线上排查问题，经常要 SSH 进跳板机 → 连数据库 → 回 SSH 看日志 → 再去 Redis 看缓存，脑子里要同时维护好几个终端上下文。
OpsKat 就想把这些统一到一个软件里面来，SSH 、MySQL/PostgreSQL/MongoDB 、Redis 、SFTP 巴拉巴拉的全弄进来，而且还做了个 AI Agent ，一句话就可以开始帮我排查问题、运维资产了。
AI Agent 这块是怎么做的
做完基础的资产管理后，发现既然连接池和凭据都在应用里了，接上 AI Agent 就顺理成章。场景大概是：

"帮我看一下 web-01 上 nginx 最近的错误日志" → AI 自己 SSH 上去 tail
"统计一下 db-prod 里 users 表各 status 的数量" → AI 通过 SSH 隧道执行 SQL
"检查一下 k3s 集群健康状况" → AI 自动跑 kubectl 并汇总

当然 AI 操服务器肯定不能乱来，需要做好审计和控制：

策略组：SSH 命令 / SQL / Redis 都可以配白黑名单，SQL 用 Parser 解析，没带 WHERE 的 DELETE/UPDATE 直接拦掉

…(内容已截断)

## 涉及话题
- Claude
- ai
- Gemini
- AI Agent
- AI
- 编程助手

[原文链接](https://www.v2ex.com/t/1208061)
