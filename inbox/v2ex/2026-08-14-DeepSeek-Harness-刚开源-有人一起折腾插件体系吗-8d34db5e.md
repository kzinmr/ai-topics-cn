---
title: "DeepSeek Harness 刚开源，有人一起折腾插件体系吗？"
source: v2ex
url: "https://www.v2ex.com/t/1234514"
author: "tuotuolala"
date: 2026-08-14
score: 0
tags: ["ai", "deepseek", "DeepSeek"]
---

# DeepSeek Harness 刚开源，有人一起折腾插件体系吗？

DeepSeek Harness 刚开源，这两天看了几个测试结果。比起单纯看跑分，我更关心插件到底好不好装、版本会不会冲突，碰到权限和依赖问题该怎么查。
先放两张比较直观的图。
第一张是同一个计时器任务的四组结果，截图里四组配置都通过了当前检查。

第二张是同一个游戏场景下，DeepSeek Harness 、Reasonix 和 Codex 的结果对比。

我拉了一个 deepseek-harness 插件实验室 群，准备和群里的人一起编写《 DeepSeek Harness：即插即用的实战指南》。先列了个大纲：

安装启动与第一个任务
插件目录、Manifest 和加载方式
插件安装、更新、卸载与版本兼容
常用插件的实际测试
模型对比与复现方法
Shell 、网络和数据权限
常见报错与排查记录
从零写一个插件
插件安全与许可证
社区实测清单与兼容表

不打算闭门写完再发，谁踩到坑就顺手留一份能复现的记录，也欢迎做插件的人进来聊后续规划。
GitHub Discussion：
https://github.com/deepseek-ai/deepseek-harness/discussions/1477
群二维码：

二维码有效期到 8 月 21 日，过期后我会在 GitHub Discussion 里更新。
这是社区自发交流，不代表 DeepSeek 官方。

## 涉及话题
- ai
- deepseek
- DeepSeek

[原文链接](https://www.v2ex.com/t/1234514)
