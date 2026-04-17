---
title: "做了个 Go 的 MCP Server 框架，一行代码把 Gin API 接入 AI"
source: v2ex
url: "https://www.v2ex.com/t/1206602"
author: "zhangpanda"
date: 2026-04-17
score: 4
tags: ["MCP", "Claude", "AI", "Cursor", "mcp"]
---

# 做了个 Go 的 MCP Server 框架，一行代码把 Gin API 接入 AI

最近 MCP 协议挺火的，Claude Desktop 、Cursor 、Kiro 都支持了。但 Go 生态里现有的库（ mcp-go 、官方 SDK ）都是 SDK 级别的，写个 Tool 要一堆样板代码。
所以做了个框架叫 GoMCP ，核心卖点：

struct tag 自动生成 JSON Schema ，不用手写
一行代码把现有 Gin 路由导入为 MCP Tool
中间件、分组、认证这些框架级的东西都有

最实用的场景：你已经有个 Gin 项目，想让 AI 能调接口：
adapter.ImportGin(s, ginRouter, adapter.ImportOptions{
    IncludePaths: []string{"/api/v1/"},
})

就这样，所有路由自动变成 MCP Tool 。
GitHub: https://github.com/zhangpanda/gomcp ( https://github.com/zhangpanda/gomcp)
欢迎试用，有问题随时提 issue 。

## 涉及话题
- MCP
- Claude
- AI
- Cursor
- mcp

[原文链接](https://www.v2ex.com/t/1206602)
