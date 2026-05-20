---
title: "[开源] 大禹治库 Skill：一次 Harness Engineering 实践，把 AI 协作规则沉淀进仓库"
source: v2ex
url: "https://www.v2ex.com/t/1213541"
author: "AllenDarwin"
date: 2026-05-18
score: 0
tags: ["openai", "Claude", "OpenAI", "AI", "AI Agent"]
---

# [开源] 大禹治库 Skill：一次 Harness Engineering 实践，把 AI 协作规则沉淀进仓库

大家好，分享一个最近整理出来的开源项目：Dayu Harness Skill ，也叫「大禹治库」。
项目地址：
https://github.com/kinoward/dayu-harness-skill
如果这个方向对你有帮助，也欢迎 Star ；如果试用中遇到问题，或者觉得某些设计不符合真实项目习惯，也欢迎直接提 Issue 。
为什么做这个
它的核心想法来自 Harness Engineering：人不再只是在每次对话里反复提醒 AI Agent ，而是把项目约束、协作规则和反馈机制沉淀到仓库里，让 Agent 在一个更明确、更可检查的工程环境中工作。
我理解这个项目大概是：

人类定义意图、边界和反馈回路； Agent 执行具体任务；仓库负责沉淀长期事实；脚本和 CI 负责机械化检查。

如果用一张图概括，它大概是这个流向：

如果图片没有正常显示，可以先看这个简化版：
聊天提示 / PR 评论 / 口头约定 / 旧文档
        |
        v
Dayu Harness Skill 分析、融合、部署
        |
        v
AGENTS.md + docs/harness + hooks + CI + sensors
        |
        v
Agent 读取项目地图 -> 执行任务 -> 脚本检查 -> 经验回写仓库

想解决的问题
这个项目想解决的问题也比较具体：
现在很多项目已经开始让 Claude Code 、Codex 或其他 Agent 参与开发、审查、排障和文档维护，但规则经常散在聊天记录、PR 评论、口头约定和旧文档里。结果就是每次开新会话、换新工具、换新成员，都要重新解释一遍项目规则。

…(内容已截断)

## 涉及话题
- openai
- Claude
- OpenAI
- AI
- AI Agent

[原文链接](https://www.v2ex.com/t/1213541)
