---
title: "Claude Code封号复盘 — IP检测机制深度分析"
created: 2026-04-20
updated: 2026-04-20
tags: [claude, anthropic, security, china]
aliases: ["Claude封号", "IP检测", "ASN检测"]
source_lang: zh-CN
---

# Claude Code封号复盘 — IP检测机制深度分析

## 概要

V2EX用户复盘了三个Claude账号被封的经历，发现IP检测远比表面复杂：不同检测工具结论矛盾、Cogent AS174等被标记为hosting而非ISP、ASN type与Company type分离检测。

## 关键发现

### 检测工具结论不一致

同一IP在不同工具的检测结果：

| 工具 | ASN Type | 结论 |
|------|----------|------|
| ipinfo.io | ISP | 「双ISP家宽属性」 |
| ipapi.is | hosting | Cogent AS174实际是hosting |

> 「ipinfo说是ISP，ipapi.is说是hosting？」

### 真正有效的IP特征

根据排查经验，需同时满足：
1. ASN type = ISP（非hosting）
2. Company层面type = ISP（非hosting）
3. Privacy = false（无VPN/代理）
4. 多工具交叉验证一致

### 被封号的共同特征

- 买了「双ISP家宽VPS」，号称家宽属性
- 信任单一检测工具（ipinfo）
- 实际上ASN和Company层面都是hosting
- 不到六周被封

## 建议的检测流程

1. **多工具交叉验证**
   - ipinfo.io
   - ipapi.is
   - ip2location
   - bgpview.io

2. **检查层级**
   - ASN层面type
   - Company层面type
   - 两者必须一致

3. **使用习惯**
   - 不要频繁换IP
   - 不要共享账号
   - 长期稳定使用老账号

## 关联内容

- [[anthropic|Anthropic]] — Claude账号问题
- [[claude-code|Claude Code]] — 封号影响

## 出处

- **V2EX**: [用了三个月Claude Code被封了，复盘下我排查IP问题的过程](https://www.v2ex.com/t/1207240) | 2026-04-20 | score:77
- **tags**: `Anthropic`, `Claude`