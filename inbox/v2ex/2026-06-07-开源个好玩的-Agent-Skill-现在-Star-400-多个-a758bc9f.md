---
title: "开源个好玩的 Agent Skill，现在 Star 400 多个"
source: v2ex
url: "https://www.v2ex.com/t/1218588"
author: "bysocket"
date: 2026-06-07
score: 0
tags: ["Claude", "AI", "Cursor"]
---

# 开源个好玩的 Agent Skill，现在 Star 400 多个

大家很多公司在做出海网站，那这个可以拿过去功劳了。这个工具是我自己做 SEO 时的痛点产物，希望能帮到更多人。
https://github.com/JeffLi1993/seo-audit-skill
可复用的单页面 SEO 审计 Agent Skill 。给一个 URL ，输出结构化 HTML 审计报告，包含可执行的修复建议。
最佳实践
1 、运行 npx skills add JeffLi1993/seo-audit-skill ，然后发起审计，例如：audit this page: https://example.com 。根据生成的报告（ reports/<hostname>-audit.html ），自行过一遍：哪些问题与你的业务目标相关、哪些可以忽略。
2 、把报告（或报告中的关键段落）交给 Cursor 或 Claude Code ，让 AI 根据报告一项一项协助修复即可。
项目
开源 + 免费，欢迎大家用起来、提 PR 、多交流！
GitHub 地址： https://github.com/JeffLi1993/seo-audit-skill

## 涉及话题
- Claude
- AI
- Cursor

[原文链接](https://www.v2ex.com/t/1218588)
