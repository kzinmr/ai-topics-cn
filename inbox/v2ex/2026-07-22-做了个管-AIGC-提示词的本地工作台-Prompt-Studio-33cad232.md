---
title: "做了个管 AIGC 提示词的本地工作台 —— Prompt Studio"
source: v2ex
url: "https://www.v2ex.com/t/1229091"
author: "innerpeace03"
date: 2026-07-22
score: 0
tags: ["ai", "prompt", "AI", "Prompt"]
---

# 做了个管 AIGC 提示词的本地工作台 —— Prompt Studio

先放地址（纯静态、无后端，打开即用）：
https://prompt-studio-7gh.pages.dev
为什么做这个
起因是身边一个做漫剧 / AI 短视频的朋友，她的 prompt 和素材全靠飞书文档 + 手动复制粘贴管理。
同一段角色设定、画风描述，在几十条 prompt 里被物理复制了几十遍 —— 真实样本里同一段片段重复出现了 16 次。
改一个设定就得全文档翻着改，漏一处就出错。
市面上要么是「以图为中心」的图库（ MJ / Civitai 那种），要么是通用文档（ Notion / 飞书），
都没解决「同一段提示词在很多地方被重复、想改一处就同步所有引用」这件事。所以自己动手做了一个。
它是什么
一句话：浏览器里运行、数据全在本地、单人用的「提示词 + 素材」工作台。
核心就一件事 —— 消灭 prompt 片段的物理重复：

片段层 + 规则层两级可复用资源，prompt 里用「引用」而不是复制粘贴
改一次片段，所有引用它的 prompt 同步更新
项目内多看板整理，prompt 和它生成出来的结果图 / 视频放在一起核对
组装好的完整 prompt 一键复制，拿去外部平台出图

技术实现

纯前端：React + TypeScript + Vite + Tailwind
数据用 File System Access API 直接读写你选的本地文件夹（配 IndexedDB ），
不上传、不联网、没有账号，关掉服务照样是你磁盘上的文件
部署在 Cloudflare Pages ，但这只是把静态页面挂上去，数据依然全在本地

已知限制

只支持桌面版 Chrome / Edge （依赖 File System Access API ，Safari / Firefox 不支持）
桌面工具，窄窗口会挡（暗色默认，长时间沉浸编辑的场景）

…(内容已截断)

## 涉及话题
- ai
- prompt
- AI
- Prompt

[原文链接](https://www.v2ex.com/t/1229091)
