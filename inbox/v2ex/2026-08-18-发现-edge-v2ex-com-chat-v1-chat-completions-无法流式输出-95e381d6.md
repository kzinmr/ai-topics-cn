---
title: "发现 edge.v2ex.com/chat/v1/chat/completions 无法流式输出"
source: v2ex
url: "https://www.v2ex.com/t/1235418"
author: "kingapi"
date: 2026-08-18
score: 1
tags: ["AI", "DeepSeek", "prompt"]
---

# 发现 edge.v2ex.com/chat/v1/chat/completions 无法流式输出

用 AI 分析得结果：
DeepSeek Harness 发送的请求没有问题：确实带上了 "stream": true，接收的也是标准的
text/event-stream。
2. 为什么没有逐字打字机效果：
• 从 +1094ms 到 +3425ms 的 2.3 秒里，V2EX 服务端/网关并没有逐字输出；
• 在第 3.4 秒，V2EX 直接把生成好的全部内容打包在单一的一个 SSE Chunk（Chunk #3）里下发。
• 收到这个包后，客户端只能一次性把整段文字显示出来。
3. 根本原因：V2EX 的 coder-ds4-0731 角色在服务端或 Cloudflare 边缘代理层开启了
响应缓冲（Buffering），未进行按 Token 实时 Flush。
自己测试得结果：
curl -N -X POST "https://edge.v2ex.com/chat/v1/chat/completions" \
   -H "Authoriza>       -H "Authorization: Bearer xxxx" \
>       -H "Content-Type: application/json" \
>       -H "Accept: text/event-stream" \
>       -d '{
el": "coder-ds4->         "model": "coder-ds4-0731",
>         "messages": [
>           {"role": "user", "content": "请从 1 数到 5，每个数字之间稍微说一句话。"}
>         ],
>         "stream": true,

…(内容已截断)

## 涉及话题
- AI
- DeepSeek
- prompt

[原文链接](https://www.v2ex.com/t/1235418)
