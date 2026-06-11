---
title: "Browser for AI Agent —— 让 AI 通过你的浏览器读取登录态页面、调用页面工具"
source: v2ex
url: "https://www.v2ex.com/t/1215754"
author: "594mantou"
date: 2026-05-26
score: 0
tags: ["MCP", "rag", "AI Agent", "AI", "Claude", "Cursor", "prompt", "ai"]
---

# Browser for AI Agent —— 让 AI 通过你的浏览器读取登录态页面、调用页面工具

背景
我经常想让 AI Agent 帮我看 Gmail 、内网 CRM 、本地服务这种没法用普通 HTTP 抓的页面，
后来干脆做了个浏览器扩展 + 本地 Native Host ，把已经登录的浏览器当作 AI 的入口。

它能做什么

读取浏览器：当前 Tab 的 HTML 、Cookie 、localStorage 、页面错误、截图，
AI Agent 都能直接拿到，登录态、内网、localhost 都没问题。
操控浏览器：在扩展后台执行脚本，让 AI 自主开关 Tab 、管理窗口、拦截请求。
页面工具：可以订阅工具集（比如 Gmail 的 write_email_draft ），
也支持页面通过 WebMCP API 自己注册工具，AI 直接调用，比临时写脚本更可靠。


适用场景

让 AI 帮你整理收件箱、写邮件草稿、提取报表
让 AI 读 CRM 、Jira 、内部 Dashboard 这种登录态页面
让 AI 自己开几个 Tab 做研究后再汇总

我的实际例子：

总结一个页面内容写到飞书文档（飞书的工具集也是让 AI 自己在浏览器中探险写出来的）
让 AI 填写 WebStore 的页面
我相信未来还有很多事情可以干，我会补充内置的工具集，也欢迎大家提交自己工具集到市场（如果是企业内的可以在公司内分发，用户可以通过 js/json url 订阅的）

安装
扩展 + Native Host ，安装完欢迎页会引导一键给 Claude / Codex / Cursor / VS Code / Zed 配 MCP 。
开源 MIT ，Chrome / Firefox 都可以。
⚠️ 安全提醒：你的 AI Agent 能读你的浏览器，意味着 prompt injection 也能。
只连可信的 Agent ，只装可信的工具集。

…(内容已截断)

## 涉及话题
- MCP
- rag
- AI Agent
- AI
- Claude
- Cursor
- prompt
- ai

[原文链接](https://www.v2ex.com/t/1215754)
