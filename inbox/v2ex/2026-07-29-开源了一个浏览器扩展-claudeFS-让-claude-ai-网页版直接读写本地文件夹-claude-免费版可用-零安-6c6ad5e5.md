---
title: "开源了一个浏览器扩展 claudeFS：让 claude.ai 网页版直接读写本地文件夹， claude 免费版可用，零安装"
source: v2ex
url: "https://www.v2ex.com/t/1230854"
author: "totoismi"
date: 2026-07-29
score: 1
tags: ["claude", "ai", "MCP", "Anthropic", "Claude"]
---

# 开源了一个浏览器扩展 claudeFS：让 claude.ai 网页版直接读写本地文件夹， claude 免费版可用，零安装

网页版 Claude 一直有个痛点：改本地文件要来回复制粘贴。官方方案是装 Claude Desktop ，但我想要个零安装的。
于是做了这个扩展（ MV3 ，Chrome/Edge ）：claude.ai 页面上授权一个本地文件夹，Claude 就能在对话里直接读、搜索、编辑里面的文件，像个轻量 agent 。
原理：claude.ai 有一套给 Claude Desktop 用的私有 postMessage 接口，扩展模拟这个握手把自己注册成 MCP server ，从而在浏览器标签页里解锁工具调用。文件读写走浏览器的 File System Access API——没有本地进程、不监听端口、不需要 API Key ，claude.ai 免费版就能用。
隐私：扩展自身不向任何服务器发送数据，代码开源可查。Claude 读到的文件内容只进入你当前的 claude.ai 对话，等同于你手动粘贴给它。文件夹授权只存在浏览器本地 IndexedDB 。
安全：所有写操作（写入/编辑/移动/删除）真正保存前都弹 diff 确认框，你看过改动再放行；拒绝则文件不动。
可能局限：依赖未公开接口，Anthropic 随时可能改接口导致失效；文件夹授权是按设备的。与 Anthropic 无关联。
GitHub （ MIT ）： https://github.com/vincentping/claudeFS
Edge 商店（一键安装）： https://microsoftedge.microsoft.com/addons/detail/claudefs/mfngoeppdmboplcgllagnnggehdcigna
Chrome 商店审核中，目前可源码加载（无需构建）。
欢迎拍砖，接口细节和踩坑都可以聊。

## 涉及话题
- claude
- ai
- MCP
- Anthropic
- Claude

[原文链接](https://www.v2ex.com/t/1230854)
