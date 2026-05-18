---
title: "手写LLM推理框架时，内存管理99%的人会踩的坑 | TFFInfer解析(五)——Tensor 张量系统与内存抽象（下）"
source: juejin
url: "https://juejin.cn/post/7640059283657195546"
author: "Clark11"
date: 2026-05-17
score: 0
tags: ["LLM", "推理", "人工智能"]
---

# 手写LLM推理框架时，内存管理99%的人会踩的坑 | TFFInfer解析(五)——Tensor 张量系统与内存抽象（下）

目录 1. Memory 类：raw pointer 的 RAII 封装 2. 分配器体系：从抽象到实现 3. CPU 与 GPU 分配器的差异 4. MemManager 与 Tensor 的协作关

> 👍 0   👁️ 0   ⭐ 1

## 涉及话题
- LLM
- 推理
- 人工智能

[原文链接](https://juejin.cn/post/7640059283657195546)
