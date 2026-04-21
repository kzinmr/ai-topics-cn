---
title: "发一个如何通过 cc-switch 让 Claude Code 使用免费的英伟达模型的教程"
source: v2ex
url: "https://www.v2ex.com/t/1207444"
author: "Dengddd"
date: 2026-04-21
score: 6
tags: ["OpenAI", "claude", "Claude"]
---

# 发一个如何通过 cc-switch 让 Claude Code 使用免费的英伟达模型的教程

1. 注册英伟达 NIM ，这步就不详细说了，网上都有教程。
2. 打开 cc-switch ，添加供应商找到 Nvidia

 
 
3. 请求地址不需要变，填上 API key ，注意 API 格式为：OpenAI Chat Completions

 
 
4. 填写模型，注意要写完整模型供应商/模型名，不知道怎么写的可以直接点击右上角获取模型列表

 

5. 配置完模型后打开设置，找到代理，打开这两个选项

 
 
6. 配置完这些后直接启动 claude code 就可以使用了，不过是真的慢。

目前在 Claude code Cli 下使用没有问题，但是在 VS Code 的插件中使用会报错，插件中对话中断，实际还在运行

 

猜测是消息格式的问题

## 涉及话题
- OpenAI
- claude
- Claude

[原文链接](https://www.v2ex.com/t/1207444)
