---
title: "最近给 专门为 C++模块化打造的构建工具 增加了 gcc16/mingw 支持, 可以一键在 Linux 上构建出 windows 的 exe 程序, 欢迎体验 mcpp"
source: v2ex
url: "https://www.v2ex.com/t/1227579"
author: "Sunrisepeak"
date: 2026-07-15
score: 1
tags: ["mcp", "ai"]
---

# 最近给 专门为 C++模块化打造的构建工具 增加了 gcc16/mingw 支持, 可以一键在 Linux 上构建出 windows 的 exe 程序, 欢迎体验 mcpp

mcpp 构建工具, 对增加了更多工具链的支持 目前已经覆盖主流的 linux/macos/winodws
支持部分的 跨 cpu 架构和操作系统的 交叉编译构建 C++项目, 欢迎大家体验反馈

mcpp 项目: https://github.com/mcpp-community/mcpp


最小验证 + 支持的工具链集合
mcpp new hello && cd hello
mcpp build --target x86_64-windows-gnu
wine target/../hello.exe





Target
Convention toolchain
Status




x86_64-linux-gnu
gcc (Linux default) or llvm
✅


x86_64-linux-musl
gcc 16, fully static
✅


aarch64-linux-musl
gcc 16, fully static — cross from x86_64 (qemu-verified) or native
✅


x86_64-windows-gnu
gcc 16 MinGW-w64 — native on Windows, cross from Linux (wine-verified)
✅


x86_64-windows-msvc
msvc@system (detected VS/BuildTools) or llvm ¹ (Windows default)
✅


aarch64-macos
llvm (macOS default)
✅


riscv64-linux-musl
—
🔄


aarch64-linux-gnu
—
🔄


x86_64-macos
—
🔄


…(内容已截断)

## 涉及话题
- mcp
- ai

[原文链接](https://www.v2ex.com/t/1227579)
