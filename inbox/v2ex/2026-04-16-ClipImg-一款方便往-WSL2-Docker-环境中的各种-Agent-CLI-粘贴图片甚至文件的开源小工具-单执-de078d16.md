---
title: "ClipImg，一款方便往 WSL2 + Docker 环境中的各种 Agent CLI 粘贴图片甚至文件的开源小工具，单执行文件"
source: v2ex
url: "https://www.v2ex.com/t/1206209"
author: "Shawlaw"
date: 2026-04-15
score: 0
tags: ["GPT", "Copilot", "AI"]
---

# ClipImg，一款方便往 WSL2 + Docker 环境中的各种 Agent CLI 粘贴图片甚至文件的开源小工具，单执行文件

Why
在 WSL2 + Docker 沙盒环境下使用 Agent CLI 时，我发现 Windows 下的截图并不能直接粘贴进去让 AI“看到”，就有点不太方便。
正好，手上刚订了智谱的 CodingPlan ，一于用这个“锤子”来试试这个“钉子”。
How
非常简单直接的思路：
既然 Windows 和 WSL2 内的 Docker 实例是可以映射同一个文件夹的，那么就在截图的时候把图片落盘到对应文件夹，然后在粘贴的时候贴入 Docker 实例内的访问路径。
What
项目地址： https://github.com/Shawlaw/clipimg-for-wsl2
除了解决上述的 Why 之外，还支持了复制文件、快速预览、开机自启的功能，并且以 1MB 左右大小的 exe 单执行文件交付，无外部依赖。
简单，而且我觉得好用。
由智谱 GLM-5.1 作为主力 RD ，我兼任 PM + QA ，这么一个“团队”用差不多一周的闲暇时间开发出来的；在 1.0.6 版本迭代后，Github Copilot 的 OPUS 4.6 和 GPT-5.4 各参与了一次 codeReview 。
项目内除了开源项目源码，还保留了迭代文档，方便感兴趣的朋友查看。
欢迎各位下载使用，如果有帮到你，不妨帮我点个 Star ，谢谢~
More
创作确实很有意思，只是如果在大半夜入睡前还在和 AI 猛聊的话，那脑子会太亢奋进而导致睡眠质量下降，所以创作工作的时间点我觉得自己还是要稍微控制一下。

## 涉及话题
- GPT
- Copilot
- AI

[原文链接](https://www.v2ex.com/t/1206209)
