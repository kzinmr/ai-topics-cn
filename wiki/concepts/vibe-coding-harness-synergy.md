---
title: "Harness Engineering与Blind Vibe Coding的适用边界"
created: 2026-04-20
updated: 2026-04-20
tags: [harness-engineering, vibe-coding, ai-agents, coding-agents]
aliases: ["Harness适用场景", "Blind Vibe Coding"]
source_lang: zh-CN
---

# Harness Engineering与Blind Vibe Coding的适用边界

## 概要

V2EX用户realize一个反直觉的观察：**Harness工程主要价值在于Blind Vibe Coding场景**（不review代码）。对于需要「先发散再收敛」的重构工作，Harness难以持续成功，因为Human-in-the-loop不可替代。

## Blind Vibe Coding的典型特征

一个「地狱级维护难度」的真实案例：
- `app.py` 超过1万行，混杂streamlit交互/业务逻辑/数据库操作
- 没有`CLAUDE.md`、spec等文档
- infra层封装了三家模型但未统一遵守interface
- 目录层级毫无规律，大量死代码

> 「Harness简直就是为这种Blind Vibe Coding场景而生的」

## Harness的核心价值

| 问题 | Harness解法 |
|------|-------------|
| 不Review代码 | 用规则/工具替代工程师基本素养 |
| 项目腐坏加速 | 延缓腐坏速度 |
| 缺乏规范 | 内置Best Practice Spec |

## Harness的局限

### 重构场景不适用

重构的核心挑战：
1. 开始时没有清晰目标
2. 面临各种权衡和妥协
3. 需要**先发散再收敛**
4. 对上下文要求更广更深

> 「这个过程不是对目标的收敛，而是需要先发散再收敛」

### Human-in-the-loop不可替代

重构过程需要人来判断：
- 哪个目标更优
- 权衡取舍的优先级
- 何时收敛到最终方案

## 关键结论

```
Harness最佳场景 = Blind Vibe Coding（规则替代素养）
Harness局限场景 = 重构（需要Human-in-the-loop）
```

未来技术框架可能不仅是代码本身，还需包含**Best Practice Spec / AGENTS.md**。

## 相关概念

- [[harness-engineering|Harness Engineering]]
- [[vibe-coding|Vibe Coding]]
- [[ai-agent|AI Agent]]

## 出处

- **V2EX**: [Harness的适用场景，可能主要还是在Blind Vibe Coding](https://www.v2ex.com/t/1207269) | 2026-04-20 | score:0
- **tags**: `AI`, `anthropic`, `AI Agent`, `gemini`, `openai`