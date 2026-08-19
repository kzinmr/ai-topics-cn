---
title: "[开源] LLM-Bridge：把 Claude Code / Codex / Antigravity 三个订阅统一成一个 OpenAI 兼容 API"
source: v2ex
url: "https://www.v2ex.com/t/1225337"
author: "mahui"
date: 2026-07-06
score: 0
tags: ["推理", "多模态", "ChatGPT", "LLM", "llm", "OpenAI", "claude", "gpt", "Claude", "prompt", "Anthropic"]
---

# [开源] LLM-Bridge：把 Claude Code / Codex / Antigravity 三个订阅统一成一个 OpenAI 兼容 API

同时订阅了 Claude 、ChatGPT 和 Google Antigravity 之后，我发现额度散在三个 CLI 里，每个交互方式还都不一样。于是写了这个本地网关：把三家的 CLI 包成一个 OpenAI 兼容端点，自带一个聊天 UI ，个人多设备用。
GitHub： https://github.com/mahui/llm-bridge （ MIT ）

它做什么

一个 base_url，通吃三家模型：claude/claude-sonnet-5、codex/gpt-5.5、agy/claude-sonnet-4.6-thinking……任何 OpenAI SDK 客户端改一行就能接
鉴权完全复用各家 CLI 自己的登录态——不碰、不提取、不重放任何 OAuth token。今年上半年 Anthropic 封杀第三方 token 复用那波大家都见过了，这个项目从设计上就只走官方 harness （ claude-agent-sdk / codex exec / agy -p），被封的路一行代码都没有
模型列表尽量动态：codex 读 CLI 自己的缓存，agy 直接 agy models，不用追着上游改版本号
内置 Web UI：多会话并发流式、provider 信号色（一眼看出回复出自哪家）、日夜主题、设置页（ API key / system prompt / 推理深度）
API 视图带 playground：选个模型直接在页面里试跑，cURL/Python/JS 示例代码跟着你选的模型自动生成


一些实现上有意思的点


…(内容已截断)

## 涉及话题
- 推理
- 多模态
- ChatGPT
- LLM
- llm
- OpenAI
- claude
- gpt
- Claude
- prompt
- Anthropic

[原文链接](https://www.v2ex.com/t/1225337)
