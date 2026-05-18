---
title: "升级到 fedora 44 后在 konsole 里打字时 cpu 占用很高的问题有 v 友也遇到了吗？"
source: v2ex
url: "https://www.v2ex.com/t/1210067"
author: "wniming"
date: 2026-05-03
score: 5
tags: ["ai"]
---

# 升级到 fedora 44 后在 konsole 里打字时 cpu 占用很高的问题有 v 友也遇到了吗？

fedora 42 在 konsole 打字时 konsole 进程的 cpu 占用是正常的，在按着按键不松的情况下连续输入同一个字符 konsole 进程的 cpu 占用只有百分之十几，升级到 fedora 44 后就变成将近百分之百了，我用 perf record 分析了一下 cpu 占用高的原因，结果如下：
Samples: 12K of event 'cpu_core/cycles/P', Event count (approx.): 10384837753
  Children      Self  Command          Shared Object                  Symbol
+   91.73%     0.00%  konsole          konsole                        [.] _start
+   91.73%     0.00%  konsole          libc.so.6                      [.] __libc_start_main@@GLIBC_2.34
+   91.73%     0.00%  konsole          libc.so.6                      [.] __libc_start_call_main
+   91.73%     0.00%  konsole          konsole                        [.] main
+   91.73%     0.00%  konsole          libQt6Core.so.6.10.3           [.] QCoreApplication::exec()

…(内容已截断)

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1210067)
