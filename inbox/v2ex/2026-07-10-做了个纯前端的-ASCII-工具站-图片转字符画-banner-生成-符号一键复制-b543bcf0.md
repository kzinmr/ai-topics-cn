---
title: "做了个纯前端的 ASCII 工具站：图片转字符画、banner 生成、符号一键复制"
source: v2ex
url: "https://www.v2ex.com/t/1226506"
author: "HeStudy"
date: 2026-07-10
score: 0
tags: ["ai"]
---

# 做了个纯前端的 ASCII 工具站：图片转字符画、banner 生成、符号一键复制

平时偶尔需要查 ASCII 码表、复制一些特殊符号（箭头、制表符这类），每次都是搜一个满屏广告的老站凑合用，索性自己做了一个：
https://getascii.com
目前有这些工具：
图片转 ASCII 字符画（拖一张图进去就行，支持调宽度/字符集/反色）
文字转 ASCII banner 大字
常用符号一键复制（箭头、制表符、数学符号、颜文字）
完整 ASCII 码表 + 一个交互式键盘映射图（点键盘上的键显示对应的 dec/hex 码）
进制转换器（ hex/dec/bin ↔ ASCII ）
几个实现上的点：
Astro 构建的纯静态站，所有工具都是纯客户端计算，图片不会上传到任何服务器
没有账号系统，没有付费墙，打开就用
整站是绿色荧光终端风（ CRT 扫描线 + JetBrains Mono ），算是给终端审美交个作业
顺手给它做了个 25 秒的宣传片：
https://www.youtube.com/watch?v=AjzU5mw1PrI
都是刚需驱动做的，工具的优先级和交互细节还在迭代，欢迎拍砖 —— 特别想知道大家还缺什么 ASCII 相关的小工具。

## 涉及话题
- ai

[原文链接](https://www.v2ex.com/t/1226506)
