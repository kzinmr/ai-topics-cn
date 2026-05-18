---
title: "封号丢了 Claude 对话数据？曲线救国系列之让 Copilot 达到 Claude 网页对话的效果"
source: v2ex
url: "https://www.v2ex.com/t/1210085"
author: "uxn"
date: 2026-05-03
score: 1
tags: ["Claude", "ChatGPT", "Copilot", "AI"]
---

# 封号丢了 Claude 对话数据？曲线救国系列之让 Copilot 达到 Claude 网页对话的效果

为 GitHub Copilot 网页版补上 SVG 显示能力：一个不成熟的油猴脚本
我最常用的网页 AI 是 ChatGPT 。
但前段时间因为有 giffgaff 的卡，就尝试着使用了 Claude 网页版。结果顿时惊为天人：

用 ChatGPT 的时候，原来过的是苦日子啊。

然后我就用着 Claude Free 版本和 Claude 网页彻夜长谈。
不是付不起 Claude Pro ，只是一直听大家说 Claude 封号封得厉害，所以我就先观望一下，看看是不是真的能封到我。
不出所料，大概五天不到，账号就被封了。
哇，真的很难受。
倒不是说号没了有多严重，而是：

对话记录没了。

这个很伤。
对话里存着思路，存着推演过程，存着很多还没整理出来的东西。结果数据说没就没？

我一开始想做“防封浏览器”
后来我就在想，是不是可以搞一个防封浏览器。
但很快意识到，这东西即便做出来，其实也很被动。
因为你什么时候被封，最终还是 Claude 官方一句话的事情。
那退而求其次，我做个油猴脚本导出对话总可以吧？
但问题是，我号都已经没了。
其次，我看到 GreasyFork 上已经有兄弟做了导出 Claude 对话的脚本，所以这方面也没必要重复造轮子了。

转向 GitHub Copilot 网页版
后面我就一直在想：

丢数据这件事情真的很糟心。

既然 Claude 官方网页风险这么大，那能不能避开 Claude 官方？
比如 GitHub Copilot 网页版里也不是没有 Sonnet 和 Opus 。
然后我就发现，虽然 Copilot 网页版里的 Sonnet 体验不一定比 Claude 官方差，但它在网页显示能力上，和 Claude 官网差得有点多。
例如我们让 Claude 做架构设计时，Claude 经常会自动调用 SVG 来画结构图。

…(内容已截断)

## 涉及话题
- Claude
- ChatGPT
- Copilot
- AI

[原文链接](https://www.v2ex.com/t/1210085)
