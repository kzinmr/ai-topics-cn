---
title: "做了一个让多台临时 GPU 接力训练同一 checkpoint 的开源项目，招募受控 Beta 测试"
source: v2ex
url: "https://www.v2ex.com/t/1229905"
author: "fffffffchopin"
date: 2026-07-26
score: 0
tags: ["qwen", "ai", "llm", "Qwen", "lLM"]
---

# 做了一个让多台临时 GPU 接力训练同一 checkpoint 的开源项目，招募受控 Beta 测试

整合大家的闲置算力
CrowdTensor 是一个开源的志愿模型训练协议。每台机器只领取一个有边界的 LoRA work unit ，完成后提交 delta ；机器离开时，Coordinator 保留已经验证的 checkpoint ， 之后由其他设备继续。
我们已经完成一次 Qwen2.5-7B/GSM8K 256 步实跑：旧的两组 T4x2 在第 128 步 全部删除，新的两组 Runtime 从中央 checkpoint 恢复并完成剩余训练。当前网站上 也运行着一个 SmolLM2/WikiText-2 Founding Campaign 。
现在是受控工程 Beta ，不是 permissionless 网络，也没有投毒/Sybil 安全或生产 SLA 。想招募愿意测试一个 work unit 、审阅 7B RFC 或检查安全边界的开发者。
网站： https://crowdtensor.24.199.118.54.nip.io
GitHub： https://github.com/Ffffffffchopin/CrowdTensor
7B RFC： https://github.com/Ffffffffchopin/CrowdTensor/blob/main/docs/campaigns/qwen25-7b-gsm8k-rfc.md
Beta 申请： https://github.com/Ffffffffchopin/CrowdTensor/issues/new?template=beta_enrollment.yml

## 涉及话题
- qwen
- ai
- llm
- Qwen
- lLM

[原文链接](https://www.v2ex.com/t/1229905)
