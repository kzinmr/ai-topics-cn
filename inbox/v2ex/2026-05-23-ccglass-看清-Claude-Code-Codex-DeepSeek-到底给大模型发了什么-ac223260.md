---
title: "ccglass：看清 Claude Code / Codex / DeepSeek 到底给大模型发了什么"
source: v2ex
url: "https://www.v2ex.com/t/1215001"
author: "jianshuo"
date: 2026-05-23
score: 1
tags: ["OPENAI", "coding agent", "DEEPSEEK", "llama", "prompt", "大模型", "Claude", "Kimi", "ANTHROPIC", "DeepSeek"]
---

# ccglass：看清 Claude Code / Codex / DeepSeek 到底给大模型发了什么

做了个小工具 ccglass ，一条命令就能看到这些 coding agent 到底往大模型发了什么。
GitHub： https://github.com/jianshuo/ccglass
为什么做
我一直想看清 Claude Code 、Codex 这类 agent CLI 实际发出去的请求——完整的
system prompt 、每一个 tool 的 schema 、消息历史、还有每次请求的 token / 缓存 /
花了多少钱。问题是：这些都是 Node / 原生程序，根本不理 HTTP_PROXY /
HTTPS_PROXY，所以 Charles 、mitmproxy 都抓不到；而 patch fetch 那类方案，
客户端一更新就废。
怎么做到的
关键点：这些 CLI 都允许用环境变量改 API 的 base url
（ ANTHROPIC_BASE_URL 、OPENAI_BASE_URL 、DEEPSEEK_BASE_URL ）。
ccglass 就在本地起一个会记日志的反向代理，把客户端指过去，再转发给真正的 API 。
客户端自己跟真 API 走 HTTPS ，你只截本地这一跳的明文 HTTP——不用装 CA 证书、
不碰 TLS pinning 、没有 MITM 。
能看到什么

实时请求流，点开看完整 system prompt + 全部工具 schema
消息历史里 tool_use 和对应的 tool_result 按 call_id 配对、同色标记
一个 agent loop 的「 flow 」视图：模型选了哪个工具 → 本地执行 → 结果喂回去
每次请求精确的 token / 缓存命中率 / 花费
两次请求的 diff ，能看到这一轮到底新增了哪些上下文、哪些被缓存命中

零依赖 Node ，一条命令，像 ollama 那样：

…(内容已截断)

## 涉及话题
- OPENAI
- coding agent
- DEEPSEEK
- llama
- prompt
- 大模型
- Claude
- Kimi
- ANTHROPIC
- DeepSeek

[原文链接](https://www.v2ex.com/t/1215001)
