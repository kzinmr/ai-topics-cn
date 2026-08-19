---
title: "几年前我开源的德扑 Solver 拿了 2.3k Star，现在我用 CUDA 将它重写，速度翻了 4 倍且完全免费"
source: v2ex
url: "https://www.v2ex.com/t/1225615"
author: "icybee"
date: 2026-07-07
score: 11
tags: ["AI"]
---

# 几年前我开源的德扑 Solver 拿了 2.3k Star，现在我用 CUDA 将它重写，速度翻了 4 倍且完全免费

V 友们好，我是 cybee 。
几年前，我写过一个开源的德州扑克 CPU 求解器（ bupticybee/TexasSolver），当时运气不错，在 GitHub 上拿了 2.3k Stars ，也感谢不少 V 友当时的支持和 PR 。
不过搞过 Game AI 或者博弈论的哥们应该知道，计算 GTO （纳什均衡）底层的 CFR （虚拟遗憾最小化）算法，对算力的要求是无底洞。传统的桌面端软件（比如业界标杆 PioSolver 或者我之前的 CPU 版）全靠堆 CPU 核心，跑一个复杂的树往往要等很久。现在市面上也流行云端方案，但基本都是按月订阅，价格不菲。
作为一个对高性能计算（ HPC ）有点执念的程序员，我一直想把这玩意儿的计算瓶颈解决掉。所以这两年，我把底层引擎用 C++ 和 CUDA 彻底重写了一遍，把庞大的矩阵运算和树遍历转移到了 GPU 上。
今天算是一个里程碑，正式发布 TexasSolver GPU 版本，并且决定 完全免费 提供给所有人使用。
官网地址： https://bupticybee.github.io/texassolver_gpu_page/
目前软件还在 Beta 阶段，V 站懂并行计算、CUDA 优化或者喜欢打德扑的大佬很多，非常欢迎大家下载下来跑一跑，狠狠地给我提 Bug 和优化建议。如果在 CFR 算法或者从 CPU 迁移到 GPU 的工程实现上有什么想交流的，也欢迎在帖子里随时探讨~

## 涉及话题
- AI

[原文链接](https://www.v2ex.com/t/1225615)
