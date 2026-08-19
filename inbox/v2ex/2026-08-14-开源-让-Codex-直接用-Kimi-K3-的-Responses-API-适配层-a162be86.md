---
title: "[开源]让 Codex 直接用 Kimi K3 的 Responses API 适配层"
source: v2ex
url: "https://www.v2ex.com/t/1234505"
author: "yihy8023"
date: 2026-08-14
score: 3
tags: ["推理", "OpenAI", "Anthropic", "kimi", "Kimi"]
---

# [开源]让 Codex 直接用 Kimi K3 的 Responses API 适配层

我写了一个把 OpenAI Responses API 转成 Kimi Coding 的 Anthropic Messages API 的工具，欢迎大家使用。
原因：new-api 协议转换不好用，sub2api 转换 Responses-> Messages 的也不好使，给 sub2api 提 PR 也没什么反馈，也不想自己维护 fork 。干脆自己写个转换服务得了。
代码是 kimi3 在 codex 中写的，自己也在用，kimi code 套餐明年七月到期前我应该会维护。
镜像：ghcr.io/jianyun8023/kimi-responses-adapter:latest
仓库： https://github.com/jianyun8023/kimi-responses-adapter
特点：

rust 锈化
完整支持 thinking 轮次回传：Kimi 的 thinking + signature 会塞进 Responses 的 reasoning.encrypted_content ，下一轮原样还原，不丢推理上下文
支持 Kimi 的联网搜索（ web_search ），自动转成 Responses 的 web_search_call item
函数调用双向映射，包括增量参数流式输出
无状态、不存任何凭证，API key 每次请求原样透传给 Kimi ，自己部署在哪都行
非 Responses 的路径（/v1/messages 、/v1/chat/completions 等）原样代理和透传
配置模型映射 codex-auto-review → kimi-for-coding-highspeed ，可以让 codex 自动审核脚本。

## 涉及话题
- 推理
- OpenAI
- Anthropic
- kimi
- Kimi

[原文链接](https://www.v2ex.com/t/1234505)
