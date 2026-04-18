---
title: "为什么该停止使用Ollama：开源伦理之争"
source: "v2ex"
url: "https://www.v2ex.com/t/1206839"
date: "2026-04-18"
tags: ['ollama', 'open-source', 'ethics', 'llama-cpp']
triage: "✅ Take"
scraped: "2026-04-18T09:28:22.156321"
---

# 为什么该停止使用Ollama：开源伦理之争

- **Source:** v2ex
- **URL:** https://www.v2ex.com/t/1206839
- **Date:** 2026-04-18
- **Tags:** ollama, open-source, ethics, llama-cpp
- **Triage:** ✅ Take

## 原帖

**作者:** catazshadow · 4 小时前 · 571 次点击

原文：https://sleepingrobots.com/dreams/stop-using-ollama/

> "Ollama wrapped that work in a nice CLI, raised VC money on the back of it, spent over a year refusing to credit it, forked it badly, shipped a closed-source app alongside it, and then pivoted the whole thing toward cloud services. At every decision point where they could have been good open-source citizens, they chose the path that made them look more self-sufficient to investors."

总之就是开源小偷，还尝试锁死用户。

## 原文推荐的替代方案

**llama.cpp** 是底层引擎。它有 OpenAI 兼容的 API 服务器 (llama-server)、内置的 Web UI、对上下文窗口和采样参数的完全控制，并且吞吐量持续优于 Ollama。2026 年 2 月，Gerganov 的 ggml.ai 加入了 Hugging Face 以确保项目的长期可持续性。它是真正的社区驱动、MIT 许可证、有 450+ 贡献者在积极开发。

**llama-swap** 处理多模型编排，按需加载、卸载和热切换模型，通过单一 API 端点。配合 LiteLLM，你可以获得一个统一的 OpenAI 兼容代理，在多个后端之间路由并支持正确的模型别名。

**LM Studio** 提供 GUI。它在底层使用 llama.cpp，暴露所有调节参数，并支持任何 GGUF 模型而不会锁定用户。

**Jan** 是另一个开源桌面应用，具有简洁的聊天界面和本地优先设计。

**Msty** 提供精美的 GUI，支持多模型和内置 RAG。

**koboldcpp** 是另一个选项，带有 Web UI 和广泛的配置选项。

Red Hat 的 **ramalama** 也值得关注，这是一个容器原生的模型运行器，明确地在显眼位置标注了其上游依赖。这正是 Ollama 从一开始就应该做的。

**附言:** 还有 ollama 的性能更差。

## 讨论回复

**anbabubabiluya:** 有大佬能推荐一个部署平台吗？我也觉得 ollama 太慢了，显卡是 5060ti 16g，最好能直接在 Windows 跑

**tool2dx:** ollama 不慢的，我显卡比你还差，只有 12G 显存，但是电脑是双显卡，加起来就有 24G 显存。运行 ollama 上的 qwen3.6 35b-q4 版本，如果优化后没爆显存，速度满速飞起。默认是爆显存 8%，速度降为 1/6，超慢。

**catazshadow (OP):** lm studio 似乎可以
