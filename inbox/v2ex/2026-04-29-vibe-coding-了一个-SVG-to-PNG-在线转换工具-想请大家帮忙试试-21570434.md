---
title: "vibe coding 了一个 SVG to PNG 在线转换工具，想请大家帮忙试试"
source: v2ex
url: "https://www.v2ex.com/t/1209502"
author: "ruguodev"
date: 2026-04-29
score: 0
tags: ["prompt", "AI"]
---

# vibe coding 了一个 SVG to PNG 在线转换工具，想请大家帮忙试试

最近用 vibe coding 做了一个小工具：SVG to PNG Converter。
地址: https://svg-to-png.io

起因很简单。我平时经常会遇到一些 SVG 需要转 PNG 的场景，比如图标、logo 之类。刚好现在 vibe coding 盛行，所以就想自己做一个：

文件不上传，转换在浏览器里完成
支持批量转换，最多一次 20 个 SVG
可以设置 1x / 2x / 4x 或自定义宽高
支持透明、白色、黑色背景
无水印

这次比较有意思的是，整个项目基本是通过 vibe coding 推起来的，一边描述需求，一边让 AI 生成，再自己 review 、调试、修改。
实际做下来感觉，AI 对这种「结构明确的小工具站」效率确实很高，但也不是一句 prompt 就能完事。
比如 SVG 转 PNG 看起来只是读文件、画 canvas 、导出 blob ，但真正处理起来会遇到不少细节。
AI 能很快把架子搭起来，但这些产品细节还是需要自己判断。不然很容易变成 demo 能跑，但实际使用不顺手。
另外这次做页面设计的时候，我参考了一个挺有意思的网站：
https://getdesign.md/
各位在自己做项目的时候，可以去找一个喜欢的风格，把对应的 Design.md 下载到项目，让 AI 按照这个规范开发即可。
目前站点已经可以正常用，不过还在继续打磨。后面可能会加：

其他格式互转
SVG 清理 / 压缩选项
一些面向设计师和前端的导出 preset

各位大佬帮忙试试看，尤其是各种比较奇怪的 SVG 文件。如果遇到转换失败、尺寸不对、透明背景异常、字体渲染不一致之类的问题，欢迎反馈。
工具地址: https://svg-to-png.io
另外，比如这种小工具还有什么值得加的功能，或者独立工具站在产品和 SEO 上还有哪些可以优化的方向。

## 涉及话题
- prompt
- AI

[原文链接](https://www.v2ex.com/t/1209502)
