---
title: "做了一个本地文档转 Markdown / RAG 知识包工具 MDtool，招募小范围测试"
source: v2ex
url: "https://www.v2ex.com/t/1228134"
author: "hunteryjm666"
date: 2026-07-17
score: 0
tags: ["RAG", "AI", "Embedding"]
---

# 做了一个本地文档转 Markdown / RAG 知识包工具 MDtool，招募小范围测试

大家好，我最近在做一个本地优先的文档整理工具 MDtool，现在想招募一小批愿意实际使用并反馈问题的测试用户。
它不是单纯把 PDF 转成 Markdown ，而是希望把比较杂乱的资料整理成后续可以用于 Obsidian 、知识库和 RAG 的内容。
目前能做什么

PDF 、Word 、PPT 、Excel 、图片和音频转 Markdown
批量处理与失败文件隔离
本地 OCR 、音频转写和基础清理
标题层级、元数据、结构感知分块和质量报告
输出 Obsidian 目录或 RAG 知识包
桌面版可以选择使用自己的 API Key 做可选 AI 清理；不开启时基础流程仍可使用

需要特别说明：当前的 RAG 功能负责整理和分块，不会生成 Embedding 或建立向量库。后续入库时，文档 Embedding 与 Query Embedding 应使用同一个模型、版本和向量维度。
当前测试平台

macOS： Apple Silicon ，ZIP 测试包；尚未完成 Developer ID 签名和 Apple 公证
Windows： Windows 10/11 x64 便携 ZIP ；解压完整目录后运行，尚未代码签名，也还没有完成完整 Windows 真机回归
Android： Android 7.0+、64 位 ARM ； OCR 和中文离线转写模型随 APK 提供，不申请联网、相机、麦克风或全盘存储权限

三个版本都属于小范围测试包，不是应用商店正式版。请保留源文件，不要为了运行测试版关闭系统安全机制；如果系统直接阻止运行，请停止安装并反馈。
测试权益

当前免费，不需要账号，没有支付或激活入口
基础单文件 Markdown 转换不限次数
批量、RAG 知识包和 Obsidian 输出共用 10 次高级体验
单次批量最多 20 个文件

下载与完整测试说明：

…(内容已截断)

## 涉及话题
- RAG
- AI
- Embedding

[原文链接](https://www.v2ex.com/t/1228134)
