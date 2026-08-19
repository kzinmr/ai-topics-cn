---
title: "Zedis：用 Rust 写的 Redis GUI，以及让 AI 帮忙改界面的一点感想"
source: v2ex
url: "https://www.v2ex.com/t/1230237"
author: "treexie"
date: 2026-07-27
score: 4
tags: ["AI"]
---

# Zedis：用 Rust 写的 Redis GUI，以及让 AI 帮忙改界面的一点感想

最近把自用的 Redis 客户端 Zedis 又打磨了一轮，发出来给大家看看。
项目地址： https://github.com/vicanso/zedis
Zedis 是原生 GUI （ Rust + GPUI ，和 Zed 同一套 UI 栈），不是套一层 WebView 。目标很简单：日常连 Redis 、翻 key 、改数据、偶尔排个障，开着不别扭。
 
主要特性（按使用频率）
连接与工作区
• 多服务器管理，支持常见连接方式（含 SSH 隧道等）
• 多 Tab：不同实例 / 不同上下文可以并排开着
• 状态栏看延迟、内存、连接状态，点一下能进对应工具页
键空间
• 按分隔符分层的键树（默认 :，可配最大深度）
• 类型 / TTL / 关键词筛选
• 收藏、最近打开、右键批量操作（删、设 TTL 、导出等）
数据类型编辑
• 基础五件套：String / Hash / List / Set / ZSet
• Stream 、RedisJSON 、Bitmap 、HyperLogLog 、TimeSeries
• GEO 有单独的「雷达图」视图，不是干巴巴一张表
• 大 value 有门槛，避免一把把几百万字节拖进编辑器
搜索与命令
• 命令面板、最近 key （类似 ⌘P ）
• 跨连接的多库 key 搜索（⌘⇧F 一类快捷键）
• 内嵌终端跑命令，键盘快捷键覆盖常用路径
运维向工具
• Metrics / 慢日志 / 内存分析 / 客户端列表 / MONITOR
• 配置编辑、ACL 、拓扑（含 Cluster 相关）、持久化状态
• Lua 脚本库、Functions 、键空间通知
• 只读 / 安全模式，少误点生产
安全与体验
• 配置里的密码等敏感字段可按本机密钥加密
• 危险操作有确认（生产环境文案会更狠一点）
• 多语言、主题、持续小版本迭代

…(内容已截断)

## 涉及话题
- AI

[原文链接](https://www.v2ex.com/t/1230237)
