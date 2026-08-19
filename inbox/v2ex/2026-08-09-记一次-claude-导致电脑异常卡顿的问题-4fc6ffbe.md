---
title: "记一次 claude 导致电脑异常卡顿的问题"
source: v2ex
url: "https://www.v2ex.com/t/1233048"
author: "trumpmaga"
date: 2026-08-09
score: 0
tags: ["claude", "ai"]
---

# 记一次 claude 导致电脑异常卡顿的问题

平时 claude 开发，一直都是开着 Bypass permissions ，这次改 bug 的时候，claude 模拟 CPU 高负载的场景，写了如下的 bash 脚本，一共运行了 60 个 while 循环，脚本有问题导致进程没有杀掉，CPU 给我占满卡了一阵子。v 友平时开发是开着 Bypass permissions 吗，怎么避免这种情况。
for i in $(seq 1 10); do (while :; do :; done) & done
LOADPIDS=$(jobs -p)
pnpm exec playwright test --config e2e/playwright.config.ts --grep-invert @real --retries=0 --reporter=line 2>&1 | grep -E "Error|Expected|Received|✘|passed|failed" | head -30
kill $LOADPIDS 2>/dev/null; echo "=== load released ==="' < /dev/null && pwd -P >| /tmp/claude-8095-cwd

## 涉及话题
- claude
- ai

[原文链接](https://www.v2ex.com/t/1233048)
