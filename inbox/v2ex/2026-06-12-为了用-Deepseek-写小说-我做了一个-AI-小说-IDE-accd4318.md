---
title: "为了用 Deepseek 写小说，我做了一个 AI 小说 IDE"
source: v2ex
url: "https://www.v2ex.com/t/1220075"
author: "garaguru"
date: 2026-06-12
score: 0
tags: ["Deepseek", "AI", "OpenAI"]
---

# 为了用 Deepseek 写小说，我做了一个 AI 小说 IDE

Deepseek 写小说真是太好用了，便宜、效果好，而且还没有任何内容限制
不过试过用聊天 AI 写小说的都知道，Chat 非常容易忘掉比较久的上下文，而且画风不稳定容易崩
市面上的都试了一波，没发现特别喜欢的适合我的 AI 小说 Agent 工具，有的太复杂太重，有的太古早长篇写作不稳定
我就自己用 codex 做了一个 AI 小说 IDE ，我自己感觉还是非常好用的，分享给大家
https://github.com/alfredxw/nova/blob/master/img/ide.png
目前已经支持：

像 IDE 一样管理作品文件：文件树、Markdown 编辑、多 Tab 、全局搜索、章节统计
创作 Agent：可以读取选区、读取文件、引用资料库、调用工具，并写入草稿或章节
结构化资料库：角色、世界观、地点、势力、规则、物品等可以沉淀为长期设定
渐进式上下文：不会把完整历史和全部设定无脑塞给模型，按来源和上限组织上下文
互动故事模式：可以用同一套设定试跑剧情分支、角色行动和场景记忆（类似酒馆）
版本管理：基于 go-git 支持保存、Diff 、恢复、定时保存和 Agent 大量输出自动保存
Skills：可以给不同 Agent 配置创作技能，比如初始化设定、续写章节、整理资料库等
Agents：自定义不同 Agent 提示与 Skills ，自定义文风
自动化：定时任务，review 、自动续写等
中英文界面、浅色/深色主题、OpenAI 兼容模型配置、Windows/MacOS/Linux 全平台

除了写自己的故事，也支持了导入 AI 酒馆角色卡（方便预设互动）、导入既有小说（方便写同人或者改编）
目前项目还在 Beta ，迭代很快，希望听到大家的反馈

…(内容已截断)

## 涉及话题
- Deepseek
- AI
- OpenAI

[原文链接](https://www.v2ex.com/t/1220075)
