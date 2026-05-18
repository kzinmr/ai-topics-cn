---
title: "GitHub Models 免费旧模型 API，包含 openai 旧模型"
source: v2ex
url: "https://www.v2ex.com/t/1212214"
author: "longxinglink"
date: 2026-05-12
score: 0
tags: ["gpt", "openai", "llama", "ai", "deepseek", "inference", "OpenAI"]
---

# GitHub Models 免费旧模型 API，包含 openai 旧模型

两个关键参数
Base URL : https://models.github.ai/inference
API Key  : 你的 GitHub Token （当 API Key 用）


⚠️ GitHub Models 的聊天接口和模型列表接口是分开的，不走同一个地址：

聊天：https://models.github.ai/inference/chat/completions ✅
模型列表：https://models.github.ai/catalog/models（不是 OpenAI 标准的 /models）



获取 Token （ API Key ）

GitHub → 头像 → Settings
左侧底部 → Developer settings
Personal access tokens → Fine-grained tokens → Generate new token
Repository access 选 Public repositories
Permissions 展开 Account permissions（不是 Repository permissions ）→ 找到 Models → 设为 Read-only
其余不动，点 Generate token，复制保存


模型名称
调用时需加厂商前缀，例如：

openai/gpt-4o
openai/gpt-4o-mini
deepseek/deepseek-r1
meta/meta-llama-3.3-70b-instruct

完整列表：github.com/marketplace/models

常见问题
客户端提示"获取模型失败"但能正常聊天？

…(内容已截断)

## 涉及话题
- gpt
- openai
- llama
- ai
- deepseek
- inference
- OpenAI

[原文链接](https://www.v2ex.com/t/1212214)
