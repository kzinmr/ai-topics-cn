---
title: "[开源] apkgo - 一行命令把 APK 发布到 8 家国内安卓商店，原生支持 AI Agent"
source: v2ex
url: "https://www.v2ex.com/t/1209675"
author: "KevinLiao"
date: 2026-04-30
score: 1
tags: ["AI Agent", "Cursor", "Claude", "ai"]
---

# [开源] apkgo - 一行命令把 APK 发布到 8 家国内安卓商店，原生支持 AI Agent

做安卓的同学应该都知道国内发版的痛 —— 华为、小米、OPPO 、vivo 、荣耀、应用宝、

蒲公英、fir.im 各有各的后台、各有各的 API 、各有各的坑。fastlane 在国内基本

用不上，每家都得自己写脚本维护。

apkgo 是我维护的开源 CLI ，目标就是干掉这块重复劳动：

  apkgo upload -f app.apk --store huawei,xiaomi,oppo,vivo

一行命令并发发到所有配好的商店，结构化 JSON 输出，CI/CD 友好。

仓库： https://github.com/KevinGong2013/apkgo

这次更新里我比较得意的几个点：

1. 原生 AI Agent 集成。Claude Code / Cursor / Windsurf 等 40+ agent 一键装：

     npx skills add KevinGong2013/apkgo

   让 agent 直接帮你发版。

2. doctor 命令预检凭证。不用真传一个 APK 才知道华为的 service account 配错了：

     apkgo doctor -s huawei -p com.example.app

3. 凭证安全做到位。--creds-from 支持从 Vault / AWS SM 读凭证，全程不落盘、

   不进 env ；多机协作可以用 apkgo config export 导出 AES-256-GCM 加密的配置。

4. 每家商店的非显然行为都吃掉了。OPPO 异步任务状态、vivo 的两层错误码、

   腾讯没有 list 接口要 app_id_map ……这些都封装好了。

5. 不想用命令行的同事可以用 apkgo serve 起本地 Web GUI ，或者直接用托管版


…(内容已截断)

## 涉及话题
- AI Agent
- Cursor
- Claude
- ai

[原文链接](https://www.v2ex.com/t/1209675)
