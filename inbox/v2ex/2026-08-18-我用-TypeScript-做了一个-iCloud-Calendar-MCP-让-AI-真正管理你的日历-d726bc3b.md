---
title: "我用 TypeScript 做了一个 iCloud Calendar MCP，让 AI 真正管理你的日历"
source: v2ex
url: "https://www.v2ex.com/t/1235320"
author: "iceywu"
date: 2026-08-18
score: 0
tags: ["Cursor", "AI", "Claude", "mcp", "MCP"]
---

# 我用 TypeScript 做了一个 iCloud Calendar MCP，让 AI 真正管理你的日历

我用 TypeScript 做了一个 iCloud Calendar MCP
AI 已经可以写代码、查资料和管理文件，现在它也可以管理你的 iCloud 日历。
最近我开源了 iCloud Calendar MCP：一个使用 TypeScript 开发、通过 CalDAV 连接 Apple iCloud Calendar 的 MCP Server 。

GitHub： https://github.com/IceyWu/icloud-calendar-mcp
npm： https://www.npmjs.com/package/icloud-calendar-mcp

它能做什么
接入支持 MCP 的客户端后，可以直接用自然语言操作日历：

查询我明天的日程。


明天上午十点创建一个 30 分钟的项目讨论。


检查明天下午有没有时间冲突。


把周五的会议调整到下周一上午。

目前提供这些工具：

查询日历和事件
创建、修改和删除事件
检查日程冲突
计算忙闲时间
处理全天事件、时区、提醒和参与者
支持 RRULE 重复事件及 occurrence 查询

快速开始
准备好 Apple 账户邮箱和应用专用密码。不要使用 Apple 账户主密码。
在 MCP 客户端中添加：
{
  "mcpServers": {
    "icloud-calendar": {
      "command": "npx",
      "args": ["-y", "icloud-calendar-mcp"],
      "env": {
        "ICLOUD_USERNAME": "you@example.com",
        "ICLOUD_APP_PASSWORD": "xxxx-xxxx-xxxx-xxxx"
      }
    }
  }
}


…(内容已截断)

## 涉及话题
- Cursor
- AI
- Claude
- mcp
- MCP

[原文链接](https://www.v2ex.com/t/1235320)
