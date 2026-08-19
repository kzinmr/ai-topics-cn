---
title: "用自然语言操作 adb shell，我写了 nl2sh 这个单文件 Android AI Agent"
source: v2ex
url: "https://www.v2ex.com/t/1232501"
author: "ErnestSu"
date: 2026-08-06
score: 0
tags: ["对齐", "OpenAI", "llama", "Kimi", "AI Agent", "DeepSeek"]
---

# 用自然语言操作 adb shell，我写了 nl2sh 这个单文件 Android AI Agent

我平时老在一台 Android 电视上调试，adb shell 是怎么也绕不开的：查应用版本号要 dumpsys package | grep，看内存得记住 /proc/meminfo 的路径。命令本身都不难，但天天敲就烦。后来我就想，能不能直接说一句"看看内存"，让程序自己把命令跑了，再用大白话把结果告诉我——nl2sh 就是这么来的。
它干的事很简单：你把自然语言交给 OpenAI 兼容的模型，模型通过 Tool Calling 生成 shell 命令，在本地做风险分类、等你确认后再执行，真实输出再回传给模型，继续往下对话。
整个程序是一个用 stable Rust 写的单文件 Android 可执行文件，adb push 到 /data/local/tmp 就能跑。设备上既不需要 Termux ，也不需要 Python 运行时。
为什么不直接用 Termux 或写个 App
Termux 得在设备上装一整套环境，分发和升级都重。App 方案要走用户态拿 shell 或 root ，路径更绕。
nl2sh 选了交叉编译这条路：NDK r28c 、API 26 起步，出 aarch64 和 armv7 两个 ABI 的产物，Android 8 以上的主流设备都能覆盖。
执行链路和安全模型
在我的测试机（ API 34 的 Android 电视）上，执行链固定四步：模型生成命令 → 本地分类 → 用户确认 → 执行。
风险分四级：只读、修改、危险、严重。默认策略下：

只读命令：自动执行
修改命令：弹一次确认
危险命令：二次确认

内置检测覆盖了 rm -rf、格式化、块设备写入、递归改根目录权限、重启关机、分区擦除、remount 等。自定义规则只能往高风险调，不能松绑内置检查。
有几条硬规矩：

模型决定不了确认流程、风险等级和 root 提升

…(内容已截断)

## 涉及话题
- 对齐
- OpenAI
- llama
- Kimi
- AI Agent
- DeepSeek

[原文链接](https://www.v2ex.com/t/1232501)
