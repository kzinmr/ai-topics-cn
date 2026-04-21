---
title: "ClipImg — Agent CLI图片粘贴工具"
created: 2026-04-15
updated: 2026-04-15
tags: [tooling, coding-agents, llm, china]
aliases: ["clipimg", "WSL2图片粘贴"]
source_lang: zh-CN
---

# ClipImg — Agent CLI图片粘贴工具

## 概要

ClipImg解决了一个WSL2+Docker环境下Agent CLI无法直接粘贴图片的痛点：通过共享文件夹映射，截图自动落盘到共享目录，粘贴时自动获取Docker内访问路径。单1MB exe，无外部依赖。

## 背景痛点

在WSL2+Docker沙盒环境下使用Agent CLI（如Claude Code）时：
- Windows下的截图无法直接粘贴让AI"看到"
- 手动传图流程繁琐

## 解决方案

### 核心思路

```
Windows截图 → 自动落盘到共享文件夹 → 粘贴时自动获取Docker内访问路径
```

### 功能特性

| 功能 | 说明 |
|------|------|
| 图片粘贴 | 直接粘贴到Agent CLI |
| 文件复制 | 支持复制文件到Docker |
| 快速预览 | 预览已粘贴内容 |
| 开机自启 | 自动启动后台服务 |
| 单执行文件 | ~1MB，无外部依赖 |

## 技术细节

- **开发工具**：智谱GLM-5.1作为主力RD，1人兼任PM+QA
- **开发周期**：约一周闲暇时间
- **Code Review参与者**：GitHub Copilot OPUS 4.6、GPT-5.4
- **开源**：保留迭代文档

## 适用场景

- WSL2+Docker内使用Claude Code/Codex CLI
- 需要截图给AI看的场景
- 无复杂依赖的简洁工具

## 出处

- **V2EX**: [ClipImg，一款方便往WSL2+Docker环境中的各种Agent CLI粘贴图片甚至文件的开源小工具](https://www.v2ex.com/t/1206209) | 2026-04-15 | score:0
- **GitHub**: [Shawlaw/clipimg-for-wsl2](https://github.com/Shawlaw/clipimg-for-wsl2)
- **tags**: `AI`, `GPT`, `Copilot`