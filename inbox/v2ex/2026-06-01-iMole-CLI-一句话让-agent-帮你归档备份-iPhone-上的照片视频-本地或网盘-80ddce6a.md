---
title: "iMole CLI：一句话让 agent 帮你归档备份 iPhone 上的照片视频，本地或网盘"
source: v2ex
url: "https://www.v2ex.com/t/1217158"
author: "plane"
date: 2026-06-01
score: 0
tags: ["rag", "claude"]
---

# iMole CLI：一句话让 agent 帮你归档备份 iPhone 上的照片视频，本地或网盘

0x01
mole 很棒，但是他只支持 mac 。我想要让我的 claude code 或者 codex 去帮我整理 iPhone 的相册，优化下存储空间，顺便也做个备份。
所以我做了一个 iPhone 版本的 mole ，命名为：iMole。

0x02
iMole 的使用非常简单，把你的 iPhone 连接上你的电脑（最好是 mac 电脑），然后让 agent 自己使用 iMole 帮你检测优化。
直接把 github 地址 https://github.com/chenhg5/imole 丢给你的 agent 去安装执行。
比如：你可以告诉你的 agent ，帮我把去年在日本的照片备份下网盘吧，然后他就会帮你开始操作了。

使用示例：
# 查看存储占用
imole scan --summary

# 找出最大的视频文件
imole scan --top 20 --only videos

# 备份 90 天前的视频
imole backup --to ~/iphone-backup --only videos --older-than 90d --dry-run
imole backup --to ~/iphone-backup --only videos --older-than 90d

# 删除已备份的文件
imole clean --manifest ~/iphone-backup/manifest.json --yes

查看空间统计：
imole scan --summary
Scanning media…
Querying app storage…
iMole Storage Summary

Media:     28.9GiB · 9960 files
  Photos:  10.3GiB · 6579 files

…(内容已截断)

## 涉及话题
- rag
- claude

[原文链接](https://www.v2ex.com/t/1217158)
