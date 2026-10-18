---
title: "我们的 coding agent 会在任务做到一半时停下来，不报错，日志空白，你们遇到过吗？"
source: v2ex
url: "https://www.v2ex.com/#"
author: "(no name)"
date: 2026-10-17
score: 0
collected: 2026-10-17
tags: ["Coding Agent", "Claude Code", "Codex", "Gemini CLI"]
---

# 我们的 coding agent 会在任务做到一半时停下来，不报错，日志空白，你们遇到过吗？

我们在一个多 Agent 编排平台上跑了几万个 coding session，反复遇到一种故障：任务执行到一半，模型生成一段没有工具调用、也没有实质最终回复的空闲 assistant turn，会话静默结束。没有非零退出码、没有超时、没有异常堆栈，日志里只有正常消息序列中一个不起眼的空回合。结果文件没有写、任务没有完成，但会话看起来是"成功"的，编排器继续往下走，直到后面的校验才撞上。

跨三个供应商出现：OpenAI Codex issue #36596（"silently stops mid-task, no error"）、Anthropic Claude Code issue #56247（"Premature turn termination"）、Google Gemini CLI issue #22633。

排查中排除的嫌疑：
- **不是上下文窗口用尽**：故障会话的上下文中位数只有 66%，同仓库正常会话有 98% 的
- **不是压缩边界**：故障分布与压缩事件位置无关
- **不是某个特定工具**：跨工具均匀分布
- **不是模型版本回归**：跨多个模型版本都有，基线率 1.04%

最硬的证据：同一份任务，坏会话 24/58 步是空闲 turn，重跑 3 次变成 11/48。输入一致、行为不一致——不是确定性 bug。

论文 arXiv 2608.01995 附录 A 给出量化基线：健康会话 24,556 步里空闲步占 1.04%，任务成功率 94%。空闲率从 0 升到 11%–36% 是会话退化的明确前兆。

我们的缓解方案（从无效到有效排序）：
- 无效：提示词强调"不要中途停止"
- 无效：单纯加大 max turns
- 部分有效：检测空闲 turn 后自动重入下一轮，任务完成率 58% 提升到 89%
- 有效：空闲率监控（滚动窗口超 15% 就重建会话）+ 把"写文件/提交结果"从依赖模型自觉改为外部钩子强制校验

结论：这不是某个模型或供应商的问题，是 turn-based agent 架构的共性缺陷。模型输出协议里"无 tool call + 无实质内容"被默认解释为"回合结束"，而模型在长会话中随机进入这种状态的概率不为零。

> 👍 0   👁️ 0   ⭐ 0

## 涉及话题
- Coding Agent
- Claude Code
- Codex
- Gemini CLI

[原文链接](https://www.v2ex.com/#)
