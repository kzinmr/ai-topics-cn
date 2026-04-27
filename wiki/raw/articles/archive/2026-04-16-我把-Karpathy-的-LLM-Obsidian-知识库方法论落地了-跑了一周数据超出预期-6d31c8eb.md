---
title: "我把 Karpathy 的 LLM + Obsidian 知识库方法论落地了，跑了一周数据超出预期"
source: v2ex
url: "https://www.v2ex.com/t/1206458"
author: "mansunyunxin"
date: 2026-04-16
score: 0
tags: ["LLM", "ai", "AI", "Claude", "CLAUDE", "MCP", "RAG", "ChatGPT"]
---

# 我把 Karpathy 的 LLM + Obsidian 知识库方法论落地了，跑了一周数据超出预期

最近把 Karpathy 那套「 LLM + Obsidian 个人知识库」方法论真正落地了。不是简单抄概念，是搭了一套能跑的系统：自动 Ingest 文章、自动体检、自动同步。跑了三天，数据说话。

## Karpathy 说了什么

他的核心洞察：**不要把 LLM 当搜索引擎用，让它像程序员维护代码库一样帮你维护 Wiki 。**

现在大部分人用 AI 管知识的套路是 RAG：上传文档，提问，AI 检索相关片段，生成回答。ChatGPT 文件上传、NotebookLM 都是这个路数。

问题在于：**没有积累。** 每次都得从头来，问完了答案就没了，知识从来没被真正沉淀下来。

他的方案是：让 AI 持续地、增量式地构建和维护一个 Wiki——结构化的、互相链接的 Markdown 文件集合。添加新资料时，AI 会读资料、提取关键信息、更新相关实体页面、修正矛盾点。知识编译一次，然后持续保持最新。

## 三层架构

- **Raw Sources**：原始资料层，只读不变
- **The Wiki**：LLM 生成和维护的知识库层
- **The Schema**：规则文件，对 Claude Code 来说就是 CLAUDE.md

## 三个核心操作

1. **Ingest**：往 Wiki 里录入新资料，可能牵动 10-15 个 Wiki 页面的更新
2. **Query**：对着 Wiki 提问，好的回答可以回存到 Wiki 里变成新页面，知识在复利增长
3. **Lint**：定期体检，找矛盾点、过时信息、孤儿页面

## 我的落地实践

核心是一个 Obsidian Vault ，叫 brain：

```
brain/
├── ontology.md       # 知识索引
├── SCHEMA_OPS.md    # 操作规则

…(内容已截断)

## 涉及话题
- LLM
- ai
- AI
- Claude
- CLAUDE
- MCP
- RAG
- ChatGPT

[原文链接](https://www.v2ex.com/t/1206458)
