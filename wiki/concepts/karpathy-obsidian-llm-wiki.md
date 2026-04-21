---
title: "LLM+Obsidian知识库 — Karpathy方法论的落地实践"
created: 2026-04-16
updated: 2026-04-16
tags: [llm, rag, memory, ai-agents, tooling]
aliases: ["知识库", "个人知识管理", "LLM Wiki"]
source_lang: zh-CN
---

# LLM+Obsidian知识库 — Karpathy方法论的落地实践

## 概要

Karpathy提出「让AI像程序员维护代码库一样维护Wiki」的方法论：三层架构（Raw Sources / Wiki / Schema），三个核心操作（Ingest/Query/Lint）。V2EX用户实际落地并验证有效。

## Karpathy的核心洞察

> 「不要把LLM当搜索引擎用，让它像程序员维护代码库一样帮你维护Wiki。」

### 传统RAG的问题
- 每次从头来，问完答案就消失
- **没有积累**
- 知识从未被真正沉淀

### Karpathy方案
让AI持续地、增量式地构建和维护Wiki——结构化的、互相链接的Markdown文件集合。

## 三层架构

```
┌─────────────────┐
│  Raw Sources    │  ← 只读不变
├─────────────────┤
│    The Wiki     │  ← LLM生成和维护的知识库层
├─────────────────┤
│    Schema       │  ← 规则文件（如CLAUDE.md）
└─────────────────┘
```

## 三个核心操作

| 操作 | 作用 | 效果 |
|------|------|------|
| **Ingest** | 往Wiki录入新资料 | 可能牵动10-15个页面更新 |
| **Query** | 对着Wiki提问 | 好回答可回存变成新页面，知识复利 |
| **Lint** | 定期体检 | 找矛盾点、过时信息、孤儿页面 |

## 实践案例

核心是一个Obsidian Vault（brain），包含：
- `ontology.md` — 知识索引
- `SCHEMA_OPS.md` — 操作规则
- 自动化：自动Ingest文章、自动体检、自动同步

### 落地效果
「跑了三天，数据说话」，一周后数据超出预期。

## 与传统RAG对比

| 维度 | 传统RAG | LLM Wiki |
|------|---------|----------|
| 知识积累 | 无 | 持续沉淀 |
| 知识复用 | 低 | 高（跨查询） |
| 维护成本 | 低 | 高（需要定期Lint） |
| 准确性 | 检索依赖 | 结构化验证 |

## 关联概念

- [[rag|RAG]] — 本方法论旨在解决RAG的积累问题
- [[cc-monitor|cc-monitor]] — Claude Code相关工具
- [[ai-agent|AI Agent]] — 这种Wiki维护本身就是Agent行为
- [[mcp|MCP]] — 可用于实现自动化Ingest

## 出处

- **V2EX**: [我把Karpathy的LLM+Obsidian知识库方法论落地了，跑了一周数据超出预期](https://www.v2ex.com/t/1206458) | 2026-04-16 | score:0
- **tags**: `LLM`, `ai`, `AI`, `Claude`, `CLAUDE`, `MCP`, `RAG`, `ChatGPT`