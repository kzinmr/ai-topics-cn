---
title: "开源了一个 Hugging Face 桌面客户端:断点续传下载、支持 hf-mirror、缓存可视化清理,全平台零遥测"
source: v2ex
url: "https://www.v2ex.com/t/1227067"
author: "BOSSZHUO"
date: 2026-07-13
score: 0
tags: ["transformer", "llama", "ai", "rag"]
---

# 开源了一个 Hugging Face 桌面客户端:断点续传下载、支持 hf-mirror、缓存可视化清理,全平台零遥测

分享一个自己写的开源项目:Oh My HuggingFace —— 一个非官方的 Hugging Face Hub 桌面客户端,macOS / Windows / Linux 全平台。

官网:https://ohmyhf.com


GitHub:https://github.com/oh-my-hf/ohmyhf (Apache-2.0,求个 star)



为什么做这个
天天泡 HF Hub 的应该都懂:用浏览器下几十 GB 的模型权重太痛苦了——不能断点续传、没有队列、不能限速;HF 缓存目录悄悄吃掉几百 GB 硬盘也没个地方看;关注的组织和 Daily Papers 更新全靠手动刷网页。所以干脆写了个桌面端把这些都管起来。
对国内用户比较实用的一点
内置自定义 Hub 地址 + 代理设置:在「设置 → 网络」里把 Hub 地址改成 https://hf-mirror.com 就能直接走镜像浏览和下载,也可以单独配代理。Token 只会发给你配置的 endpoint 和 huggingface.co,不会带到 CDN 跳转目标上。
主要功能

下载管理器:断点续传、多线程并行、队列、限速、SHA-256 校验、系统通知。文件直接落在标准 HF 缓存目录结构里,transformers、huggingface-cli 等工具无缝复用,不搞私有格式。


缓存可视化:扫描本地 HF 缓存,按仓库看磁盘占用,一键清理过期 revision 。




三栏浏览:模型 / 数据集 / Spaces / Daily Papers,键盘优先(Cmd/Ctrl+K 命令面板),虚拟列表秒开,模型卡片即时渲染,文件树 + 文件预览。




关注 & 收件箱:关注用户 / 组织 / 仓库 / 论文,有更新发系统通知。





…(内容已截断)

## 涉及话题
- transformer
- llama
- ai
- rag

[原文链接](https://www.v2ex.com/t/1227067)
