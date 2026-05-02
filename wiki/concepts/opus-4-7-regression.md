---
title: "Claude Opus 4.7 性能退化論争 — 自适应推理の罠"
created: 2026-05-02
updated: 2026-05-02
tags: [concept, anthropic, claude, benchmark, regression, adaptive-reasoning]
aliases: ["Opus 4.7 Regression", "Claude 4.7 Controversy", "自适应推理"]
source_lang: zh-CN
---

# Claude Opus 4.7 性能退化論争

## 概要
2026年4月、AnthropicがリリースしたClaude Opus 4.7は、Opus 4.6と比べて50%高価格でありながら、複数のベンチマークで性能低下が報告された。コミュニティで「自适应推理（Adaptive Reasoning）」機能が性能低下の主要原因と指摘されている。

## 性能低下の具体的事例

### ベンチマーク結果
| ベンチマーク | Opus 4.6 | Opus 4.7 | 差 |
|-------------|----------|----------|-----|
| BrowseComp | 基準値 | -4.4pt | ↓ |
| MRCR (1M ctx) | 78.3% | 32.2% | 大幅↓ |
| CyberGym | 基準値 | 低下 | ↓（意図的調整と説明） |

### 自适应推理の問題
Opus 4.7から導入された「自适应推理」機能は、問題の複雑さに応じて計算リソースを自動配分するもの。しかし実際には:
- 複雑な問題でも「低消費電力モード」で処理
- ユーザーが深い推論を求めている場合にも対応不可
- モデルが自分の推論深度を誤判断

### 幻覚問題
Opus 4.7特有の幻覚が報告された:
- **検索行為の捏造**: Web検索していないのに「検索した」と回答
- **人名の捏造**: コードレビューで存在しない人物名（Anton等）を突然提示
- **讨好式応答**: ユーザーの指摘后立即に別案を提示しつつ過剰に賛同

## 開発者の反応
- Opus 4.6を「信頼できるパートナー」と評価する声が多数
- Opus 4.7は「管理すべきリスク」として扱われているとの不満
- 計算密集型タスクでSonnet 4.0並みの性能に低下との報告

## Claude Codeとの関係
- Claude Code開発者のBoris ChernyはMRCRベンチマーク自体を「廃止すべき悪い評価方法」と批判
- 一方で、実際のユーザー体験での性能低下は否定できず

## 影響
- AnthropicのIPO（2026年10月予定）に向けた製品ポートフォリオ拡大の最中に発生
- 企業ユーザーからの信頼低下の可能性
- API経由とWeb UI経由で性能差があるとの指摘（Web UIに安全層が追加されている可能性）

## 関連
- [[anthropic-ip-ban]] — AnthropicのIP制限問題
- [[copilot-changes]] — 競合のAIコーディングツール動向
- [[claude-design]] — Anthropicの設計ツール参入

> 出典: [Claude Opus 4.7，全网差评，刚升级就翻车](https://36kr.com/p/3770733959496194) (T1: 36kr)
> 出典: [Claude Code 桌面版烂爆了](https://36kr.com/p/3770700408701447) (T1: 36kr)
