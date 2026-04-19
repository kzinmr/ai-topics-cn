---
title: "1000 行 rust 实现一个类似于 pytorch 的轻量级自动微分库"
source: v2ex
url: "https://www.v2ex.com/t/1207027"
author: "StepfenShawn"
date: 2026-04-19
score: 0
tags: ["ai", "gpt", "GPT"]
---

# 1000 行 rust 实现一个类似于 pytorch 的轻量级自动微分库

最近在学习神经网络原理，分享一下自己用 Rust 写的轻量级自动微分库 ferris-grad。
Features

PyTorch 风格的 autograd 引擎
核心代码不到 1000 行，纯 Rust 实现
零外部依赖（仅使用 rust 标准库实现核心反向传播部分）

包含什么？
实现仅仅包含了 3 个文件构成:

| 模块 | 功能 |
|------|------|
| scalar.rs | 标量计算图 + 反向传播 |
| tensor.rs | 张量操作 |
| nn.rs | 神经网络层 |
能做什么？

训练 MLP(~50 行代码)
实现一个 mini GPT(~350 行代码)
... 

代码示例：
实现了一个 Pytorch 风格的 api:  
use anyhow::Result;
use ferris_grad::{Tensor, nn::Module};

fn main() -> Result<()> {
    let a = Tensor::from_vec(vec![1.0.into(), 2.0.into(), 3.0.into()], [3, 1].into())?;
    let b = Tensor::rand([3, 1].into())?;
    let c = &a * &b;
    println!("{}", c);
    Ok(())
}

本项目的灵感来源：

micrograd - Karpathy 的 python 微型 autograd 引擎  
microgpt - Karpathy 博客中的极简 GPT 实现

GitHub 仓库地址: https://github.com/StepfenShawn/ferris-grad
目前只能调用 CPU,后续研究一下如何在 GPU 上实现  

…(内容已截断)

## 涉及话题
- ai
- gpt
- GPT

[原文链接](https://www.v2ex.com/t/1207027)
