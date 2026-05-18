---
title: "gemini cli 登录不上（被封禁）"
source: v2ex
url: "https://www.v2ex.com/t/1210902"
author: "yinzhou"
date: 2026-05-07
score: 0
tags: ["ai", "gemini", "Gemini"]
---

# gemini cli 登录不上（被封禁）

这是一份为您整理后的文字，逻辑更清晰、阅读体验也更好。
Gemini CLI 登录故障排查记录
针对 Gemini CLI 无法完成登录的问题，我花费了较长时间进行排查。以下是详细的过程复盘，希望能为遇到类似情况的开发者提供参考。

故障现象

使用 Gemini CLI 的 Sign in with Google 授权登录。
浏览器显示登录成功并跳转回终端，但 CLI 未进入登录状态，而是直接提示“请输入 API Key”。
痛点：全过程没有任何 Error Log 报错，即便通过 omx 辅助排查，也无法定位具体原因。


排查难点
由于系统静默失败（ Silent Failure ），没有任何错误信息输出，导致排查方向一度不明。起初怀疑是网络或环境配置问题，但始终无法证实。


关键突破与原因分析
后来联想到该账号曾用于 Anti-gravity 相关的反向代理操作，怀疑是账号权限或封禁问题。


验证方法：尝试直接登录 Anti-gravity 。
定位原因：登录 Anti-gravity 后，系统立刻弹出了明确的错误提示。原来是 Anti-gravity 端的服务被封禁，进而连锁反应导致关联的 Gemini CLI 登录流程异常中断。

解决方案

直接动作：由于错误根源在 Anti-gravity 侧，前往对应的平台提交申诉（ Appeal ）即可。
总结经验：若遇到 Gemini CLI 登录后反复跳回 API Key 输入界面的情况，大概率是底层的 Google 账号权限或关联服务被风控，建议通过其他关联工具查看是否有隐藏的报错信息。

## 涉及话题
- ai
- gemini
- Gemini

[原文链接](https://www.v2ex.com/t/1210902)
