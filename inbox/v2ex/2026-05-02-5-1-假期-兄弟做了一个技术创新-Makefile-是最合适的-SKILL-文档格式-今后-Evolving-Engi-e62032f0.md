---
title: "5.1 假期，兄弟做了一个技术创新， Makefile 是最合适的 SKILL 文档格式，今后“Evolving Engineering”靠他了！"
source: v2ex
url: "https://www.v2ex.com/t/1209983"
author: "achangzhou"
date: 2026-05-02
score: 0
tags: ["AI", "claude", "ai"]
---

# 5.1 假期，兄弟做了一个技术创新， Makefile 是最合适的 SKILL 文档格式，今后“Evolving Engineering”靠他了！

项目地址： https://github.com/Teaonly/SKILL.make 
这个项目的思想，用 Makefile 来风格化 SKILL 文档，利用 Makefile 内置的 DAG 功能，并且搭配 一定意义上的语法，优点如下：

可以降低原始 MD 格式的 Token 消耗；
SKILL 更加容易阅读，也更适合 AI 使用，因为天然的 DAG ，就是 Plan Mode ；
Makefile 非常适合审计（ git 跟踪，调用统计），为今后的 Self-Evolving 工程做好扎实准备；

我完全自动化转换旧的 SKILL.md ，采用 Makefile 风格，平均文件尺寸减少 15%。

File                                       SKILL.md SKILL.make   Change
---------------------------------------- ---------- ---------- --------
caveman                                        1916       1714     -10%
design-an-interface                            3366       2789     -17%
domain-model                                   3512       3376      -3%
edit-article                                    721        692      -4%

…(内容已截断)

## 涉及话题
- AI
- claude
- ai

[原文链接](https://www.v2ex.com/t/1209983)
