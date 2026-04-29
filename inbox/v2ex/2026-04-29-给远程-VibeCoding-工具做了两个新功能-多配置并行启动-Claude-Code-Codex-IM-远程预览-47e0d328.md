---
title: "给远程 VibeCoding 工具做了两个新功能：多配置并行启动 Claude Code / Codex + IM 远程预览"
source: v2ex
url: "https://www.v2ex.com/t/1209512"
author: "jazzenchen"
date: 2026-04-29
score: 0
tags: ["Gemini", "Claude", "coding agent", "DeepSeek", "AI"]
---

# 给远程 VibeCoding 工具做了两个新功能：多配置并行启动 Claude Code / Codex + IM 远程预览

给远程 VibeCoding 工具做了两个新功能：多配置并行启动 Claude Code / Codex + IM 远程预览
大家好，之前在 V2EX 发过自己在制作的工具 VibeAround ，收到了一些宝贵的反馈意见。加上自己日常使用 coding agent 的过程中，也发现除了模型能力、开发工具能力之外，还有很多 workflow 上的小摩擦。
比如我自己购买了 Claude Code 和 Codex 订阅，但还是想试试看 DeepSeek V4 或者小米 MiMo 的 API ，尤其是同时多开不同设置的 Claude Code 或 Codex 来对比模型能力；
再比如远程用飞书或者微信指挥 Claude Code / Codex 干活时，想预览一下当前进展，或者把做好的内容分享给朋友、同事等等。
于是最近就在 VibeAround 里补上了两个能力：Launch 和 Preview。
Launch：配置一键切换、命令行多开
有类似能力的工具不少，比如大名鼎鼎的 cc-switch ，不过很少看到可以同时用不同配置开启多个命令行窗口的，也很少有在切换配置时不改动原始 Claude Code / Codex 配置文件的。这也是我做 Launch 功能时的主要目标。
不多赘述，直接上图：



Preview：快速预览本地 VibeCoding 的结果，并可以分享出去
Preview 是另一个我自己用得很多的功能。
虽然之前的 VibeAround 支持 IM 远程控制，也可以在浏览器上直接访问命令行，但如果想看到实际效果，还是要回到电脑旁边，或者让 AI 去部署到云服务上，都不是很方便。
现在 Preview 利用了 tunnel 通道，走了一个更直接的流程：agent 做完东西之后，通过反向代理直接生成预览链接，在浏览器、手机或 IM 里立刻就能打开看。

…(内容已截断)

## 涉及话题
- Gemini
- Claude
- coding agent
- DeepSeek
- AI

[原文链接](https://www.v2ex.com/t/1209512)
