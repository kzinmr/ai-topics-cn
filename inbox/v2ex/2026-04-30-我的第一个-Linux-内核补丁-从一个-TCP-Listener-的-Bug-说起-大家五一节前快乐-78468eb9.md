---
title: "我的第一个 Linux 内核补丁：从一个 TCP Listener 的 Bug 说起（大家五一节前快乐）"
source: v2ex
url: "https://www.v2ex.com/t/1209526"
author: "swananan"
date: 2026-04-30
score: 85
tags: ["LLM", "AI"]
---

# 我的第一个 Linux 内核补丁：从一个 TCP Listener 的 Bug 说起（大家五一节前快乐）

https://jt26wzz.com/posts/0016-my-first-linux-kernel-patch-fixing-a-tcp-listener-bug/

上面是博客地址链接，文章全程手搓，主要写了三部分：一个是怎么发现 Bug 的，然后是给内核社区提补丁的全过程（期间得到多个大佬的帮助），最后是我对开源社区运作新的理解（特别是和血汗大厂工作的区别对比）。

上次分享博客，很多人吐槽我博客的阅读体验有点差，这次我特别用 AI 调整了一下，优化了字体和行间隔，加了侧边栏，开头加上了 TL:DR 摘要，还调整了高亮特效，这次应该好很多了。如果有什么新的反馈，随时写在下面，反正一个小小的静态博客，LLM 都能搞定😉。

## 涉及话题
- LLM
- AI

[原文链接](https://www.v2ex.com/t/1209526)
