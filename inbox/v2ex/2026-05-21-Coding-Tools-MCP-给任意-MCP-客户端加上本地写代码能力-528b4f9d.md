---
title: "Coding Tools MCP：给任意 MCP 客户端加上本地写代码能力"
source: v2ex
url: "https://www.v2ex.com/t/1214464"
author: "tfu"
date: 2026-05-21
score: 0
tags: ["MCP", "ChatGPT", "Claude", "mcp"]
---

# Coding Tools MCP：给任意 MCP 客户端加上本地写代码能力

最近在折腾 MCP ，顺手做了一个小工具：Coding Tools MCP 。
一句话概括：
给支持 MCP 的客户端接一个本地代码仓库操作后端，让它能读文件、搜代码、打 patch 、跑命令、看 git diff 。
它不是一个 Agent ，也不绑某个模型，更像是一个本地 coding runtime 。
大概流程是这样：
MCP 客户端
↓
Coding Tools MCP
↓
本地项目目录
↓
读代码 / 搜索 / 修改 / 跑测试 / 看 git diff
也就是说，只要你的客户端支持 MCP ，就可以把它接到本地项目上，让他获得代码编辑的相关能力，变成 Codex/Claude Code 青春版
举个例子：比如说 ChatGPT 网页版就是一个 MCP 客户端，支持加入 MCP 服务，那么下面就以 ChatGPT 网页版为例，详细说明一下这个项目有什么用
1 、首先 Clone 仓库到本地或者任意的能够运行代码进行开发的机器上
git clone https://github.com/xyTom/coding-tools-mcp

2 、安装相关依赖
cd coding-tools-mcp
python -m pip install -e ".[dev]"

3 、运行 Coding Tools MCP 服务
coding-tools-mcp --workspace /path/to/repo
/path/to/repo 这个路径替换为你实际需要开发的项目文件夹路径

4 、运行内网穿透服务
scripts/tunnel.sh cloudflared /path/to/repo
/path/to/repo 这个路径替换为你实际需要开发的项目文件夹路径



…(内容已截断)

## 涉及话题
- MCP
- ChatGPT
- Claude
- mcp

[原文链接](https://www.v2ex.com/t/1214464)
