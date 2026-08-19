---
title: "Pi Coding Agent"
source: v2ex
url: "https://www.v2ex.com/t/1229821"
author: "Livid"
date: 2026-07-25
score: 1
tags: ["DeepSeek", "AI", "Coding Agent", "openai"]
---

# Pi Coding Agent

Pi 是 Flask 作者 Mitsuhiko 参与的 Coding Agent 项目。
https://pi.dev/
安装：
curl -fsSL https://pi.dev/install.sh | sh

然后打开 ~/.pi/agent/models.json 放入以下内容：
{
  "providers": {
    "v2ex": {
      "baseUrl": "https://edge.v2ex.com/chat/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_V2EX_ACCESS_TOKEN",
      "models": [
        { "id": "coder" },
        { "id": "coder-m3" },
        { "id": "coder-ds4" }
      ]
    }
  }
}

不过这样的话，会使用的是 Pi 的相当保守的默认值，如果要发挥这 3 个模型的全部能力，需要用这个更详细的配置：
{
  "providers": {
    "v2ex": {
      "baseUrl": "https://edge.v2ex.com/chat/v1",
      "api": "openai-completions",
      "apiKey": "0de43952-f09b-49b9-8c2b-2510ed59860c",
      "models": [
        {
          "id": "coder",
          "name": "GLM-5.2",
          "contextWindow": 976000,

…(内容已截断)

## 涉及话题
- DeepSeek
- AI
- Coding Agent
- openai

[原文链接](https://www.v2ex.com/t/1229821)
