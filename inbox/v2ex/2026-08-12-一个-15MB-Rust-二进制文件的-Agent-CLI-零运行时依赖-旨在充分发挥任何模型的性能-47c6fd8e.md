---
title: "一个 15MB Rust 二进制文件的 Agent CLI，零运行时依赖，旨在充分发挥任何模型的性能"
source: v2ex
url: "https://www.v2ex.com/t/1233880"
author: "Koimiao"
date: 2026-08-12
score: 4
tags: ["推理", "Qwen"]
---

# 一个 15MB Rust 二进制文件的 Agent CLI，零运行时依赖，旨在充分发挥任何模型的性能

Ante 是一个仅 15MB 的二进制文件，它管理着自己的推理引擎。添加一个 GGUF 文件，即可在您自己的硬件上拥有一个完整的编码代理：无需 API 密钥，无需帐户，模型调用也永远不会离开您的计算机。

GitHub link:https://github.com/AntigmaLabs/ante
🙏希望感兴趣的朋友们能帮忙点点 star⭐️

实测：电脑是 MacBook Pro M4 Max ，基于当前可⽤运⾏内存，提示最适合的可运⾏离线⼤模型为 Qwen3.6 27B （ 17GB ）。并且本地跑起来，切换、对话都⼗分⽅便。Ante 对本地模型做全⽣命周期管理：模型下载、加载前预估、启动停⽌。

## 涉及话题
- 推理
- Qwen

[原文链接](https://www.v2ex.com/t/1233880)
