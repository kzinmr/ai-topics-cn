---
title: "oss-skills： 18 个开源开发技能，让 Agent 像资深维护者一样做开源"
source: v2ex
url: "https://www.v2ex.com/t/1232916"
author: "veotax"
date: 2026-08-08
score: 0
tags: ["claude", "ai", "Claude"]
---

# oss-skills： 18 个开源开发技能，让 Agent 像资深维护者一样做开源

Hi V 友们 👋
现在的 Agent 写代码基本够用了。但真把一个项目开源出去，写代码可能只占 20%，剩下 80% 是这些事：

选哪个许可证？ Apache-2.0 和 MIT 到底差在哪
这个改动算 minor 还是 major ？改个默认值算不算 breaking
CI 为什么在 fork 的 PR 上永远是红的
有人提了个 3000 行的 PR ，我不想合，怎么关掉才不至于把人得罪走
发了个坏版本，是该删掉还是该 deprecate

这些问题的答案 Agent 大多答不准，或者答得很「正确但没用」——比如你问它 semver 怎么办，它跟你说「请仔细遵守语义化版本规范」。
所以我做了 oss-skills：18 个按需加载的 Agent 技能，把这部分判断力补上。
GitHub: https://github.com/the-open-agent/oss-skills

一、装完之后是什么效果
你：   我想把这个内部工具开源。

Agent：[加载 open-source-playbook → repo-bootstrap → license-and-legal]

       先读了仓库。有三件事得排在其他所有事情前面：

       1. commit 8f3a91c 里有一个 AWS key （ src/config.py ，在 4b2e 被删掉了）。
          它仍然在历史记录里 —— 去轮换掉。重写历史属于清理，不属于补救。
       2. 没有 LICENSE 。按现状，任何人在法律上都不可以使用这个项目。
          Apache-2.0 合适：你们有企业贡献者，专利授权条款是有意义的。
       3. README 只有一行。对 95% 的访客来说，那就是整个产品页。


…(内容已截断)

## 涉及话题
- claude
- ai
- Claude

[原文链接](https://www.v2ex.com/t/1232916)
