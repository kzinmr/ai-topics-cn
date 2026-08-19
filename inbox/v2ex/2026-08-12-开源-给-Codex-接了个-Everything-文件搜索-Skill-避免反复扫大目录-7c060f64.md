---
title: "[开源] 给 Codex 接了个 Everything 文件搜索 Skill ，避免反复扫大目录"
source: v2ex
url: "https://www.v2ex.com/t/1233975"
author: "soarinsky"
date: 2026-08-12
score: 0
tags: ["coding agent", "AI Agent", "Claude"]
---

# [开源] 给 Codex 接了个 Everything 文件搜索 Skill ，避免反复扫大目录

最近在 Windows 上用 Codex ，发现它为了找几个文件，有时会直接 rg --files 或递归扫项目目录。
但电脑上本来就一直开着 Everything ，索引已经有了，再让 Agent 自己扫一遍感觉挺浪费。
所以做了一个小 Skill：
everything-fast-file-search-skill
GitHub：
https://github.com/soarinsky1/everything-fast-file-search-skill
主要功能：
直接调用 Everything 官方 CLI es.exe
支持限定 Root 、关键词、扩展名和最大结果数
支持 CSV / JSON 输出
候选缩小后可选 SHA-256
Everything 只负责定位候选，不替 Agent 判断哪个文件才是“最终版”
目前已经更新到 v1.1.0 ，这几天实际使用过程中顺便修了 PowerShell 5.1 参数传递和 Everything IPC Error 8 的一些问题，也加了 regression tests 。
定位很简单：
已经有 Everything 索引，就尽量别让 AI Agent 再递归扫大目录。
如果也在 Windows 上用 Codex / Claude Code / 其他 coding agent ，欢迎帮忙试试。
有问题可以直接提 Issue ；觉得有用的话，也欢迎顺手点个 Star 。
MIT License 。

## 涉及话题
- coding agent
- AI Agent
- Claude

[原文链接](https://www.v2ex.com/t/1233975)
