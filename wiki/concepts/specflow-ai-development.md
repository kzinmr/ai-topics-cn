---
title: "SpecFlow — AI时代的设计驱动开发范式"
created: 2026-04-20
updated: 2026-04-20
tags: [ai-agents, coding-agents, tooling, llm]
aliases: ["AI开发范式", "设计驱动开发", "spec-driven"]
source_lang: zh-CN
---

# SpecFlow — AI时代的设计驱动开发范式

## 概要

当AI生成代码比例从70%升至接近100%时，真正的瓶颈不再是「怎么写」而是「想让系统长成什么样」。SpecFlow是一种「设计前置」的开发范式：先定义spec，再让AI按设计实现，持续Q&A修正行为。

## 核心观点

### 实现变廉价，结构变稀缺

> 「当 AI 开始参与之后，这个前提消失了：代码可以很快生成，甚至几乎没有成本，可系统却开始变得越来越混乱。」

- **传统模式**：代码 → 设计 → bug修
- **SpecFlow模式**：设计(spec) → AI实现 → Q&A修正 → 结构收敛

### 关键转变

| 传统开发 | AI时代开发 |
|---------|-----------|
| 实现是最稀缺资源 | 设计是最稀缺资源 |
| 代码是核心资产 | spec是核心资产 |
| 人执行，AI辅助 | AI执行，人指导 |

## SpecFlow原则

1. **Spec-first**：所有开发从设计文档开始
2. **AI按设计实现**：代码生成必须遵循spec约束
3. **持续Q&A**：通过问答修正系统行为
4. **结构收敛**：逐步让系统结构明晰化

## 适用场景

- 中长期项目（维护周期长）
- 多人协作项目（需要共同遵守的设计语言）
- AI参与度高（>70%代码由AI生成）

## 与Harness Engineering的对比

| 维度 | [[harness-engineering|Harness]] | SpecFlow |
|------|----------------------|----------|
| 核心 | 规则/约束 | 设计/spec |
| 目标 | 防止项目腐坏 | 构建正确结构 |
| 适用场景 | Blind Vibe Coding | 设计驱动开发 |
| 自动化程度 | 高（规则内化） | 中（需人工spec） |

## 工具

- [SpecFlow GitHub](https://github.com/Bingordinary/SpecFlow)

## 出处

- **V2EX**: [code is cheap, show me your design — 分享一个我的AI时代的软件开发范式](https://www.v2ex.com/t/1207234) | 2026-04-20 | score:1
- **tags**: `AI`