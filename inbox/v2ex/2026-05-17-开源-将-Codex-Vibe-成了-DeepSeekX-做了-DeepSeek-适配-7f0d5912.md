---
title: "[开源] 将 Codex Vibe 成了 DeepSeekX , 做了 DeepSeek 适配"
source: v2ex
url: "https://www.v2ex.com/t/1213367"
author: "Cycle0079"
date: 2026-05-17
score: 2
tags: ["DEEPSEEK", "deepseek", "DeepSeek", "GPT"]
---

# [开源] 将 Codex Vibe 成了 DeepSeekX , 做了 DeepSeek 适配

Codex 用习惯了, 但总是用 GPT5.5 也不是个事, 于是花了一周, 基于 Codex CLI 的开源库作为二开Github 地址, 适配了 DeepSeek 的 /chat/completions 接口. 这样能节省大量开发时间, 能使用上大米价格一样的 DeepSeek Token, 也能保持 Codex 使用习惯的一致.
安装
npm install -g @meomeo-dev/deepseekx@0.131.0-deepseekx.3

版本说明: 0.131.0 表示 codex 的版本, deepseekx.3 为 deepseekx 的小版本. 表示在 0.131.0 版本进行适配时发布的第三个小版本.
开发流程就是 codex 上游有新版后, 拉去新版本然后适配, 版本跟随 codex. 主要一个人没太多精力, 只能做适配, 基础设施靠 codex 开源. 由于设备有限仅真机实跑了 Mac-X64 和 Mac-RAM64, 其余设备仅跑了 Github 免费的 CI Hosted Runners
使用
和使用 codex 一样, 环境变量中配置好 DEEPSEEK_API_KEY 后, 进入仓库目录启动即可:
export DEEPSEEK_API_KEY="sk-..."

cd /path/to/my-project

deepseekx

使用时注意, 建议开启 deepseek-v4-pro xhigh 来确保最大性能,能确保幻觉率在可控范围. 
另外做了缓存命中率, 在编写 1 万代码的网站时, deepseek-v4-pro + 384K 窗口, 命中率在 99.4579% .

## 涉及话题
- DEEPSEEK
- deepseek
- DeepSeek
- GPT

[原文链接](https://www.v2ex.com/t/1213367)
