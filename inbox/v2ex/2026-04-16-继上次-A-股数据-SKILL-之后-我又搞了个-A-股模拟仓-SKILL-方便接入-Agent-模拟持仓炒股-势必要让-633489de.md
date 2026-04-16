---
title: "继上次 A 股数据 SKILL 之后，我又搞了个 A 股模拟仓 SKILL，方便接入 Agent 模拟持仓炒股，势必要让 AI 帮我赚钱"
source: v2ex
url: "https://www.v2ex.com/t/1206214"
author: "should"
date: 2026-04-15
score: 3
tags: ["ai", "AI"]
---

# 继上次 A 股数据 SKILL 之后，我又搞了个 A 股模拟仓 SKILL，方便接入 Agent 模拟持仓炒股，势必要让 AI 帮我赚钱

继 A 股数据 SKILL 之后，我又做了一个新能力：a-share-paper-trading。
这个 SKILL 的目标很直接——让 Agent 不只是“会分析”，还能在模拟仓里完成从选股、下单、持仓跟踪到复盘评估的一整套流程，先把策略在低风险环境里跑通，再决定是否进入实盘流程。
你可以把它理解为一个“策略试炼场”：

先验证交易逻辑是否稳定，而不是靠感觉拍脑袋
用一致的规则管理仓位、交易节奏和风险暴露
持续观察策略表现，及时发现问题并迭代
让研究、执行、复盘形成闭环，减少无效试错

安装也很直接（ https://clawhub.ai/shouldnotappearcalm/a-share-paper-trading ）：
clawhub install a-share-paper-trading

如果这个方向对你有帮助，欢迎支持一下：

点个 Star，让更多人看到这个项目 （ https://github.com/shouldnotappearcalm/a-share-skill ）
提 Issue，告诉我你在实战里遇到的真实需求
提交 PR，一起把 A 股 Agent 交易工具链做得更完整、更可靠

这次也把几个常用选股/决策 SKILL 一起串起来：

a-share-strategy-mainboard-multi-swing-defensive

主板流动性池 + 趋势回踩，给出买入参考和卖出信号，适合做日常候选池筛选。
macd-trend-resonance-stock-picker

均线定方向、MACD 定节奏，输出 A/B/C/D 分级候选，适合盘前选强弱。
macd-second-golden-cross

聚焦“底背离 + 零轴下二次金叉”修复结构，给出观察/试错/放弃三档决策，适合低位修复场景。

## 涉及话题
- ai
- AI

[原文链接](https://www.v2ex.com/t/1206214)
