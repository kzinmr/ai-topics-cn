---
title: Anthropic IP封鎖とKYC — 中国ユーザーへの影響
created: 2026-05-02
updated: 2026-05-02
tags: [anthropic, claude, ip-ban, kyc, china-ai]
aliases: ["Anthropic封鎖", "IP Ban問題", "KYC"]
source_lang: zh-CN
---

# Anthropic IP封鎖とKYC — 中国ユーザーへの影響

## 概要

AnthropicのClaudeプラットフォームは、中国本土ユーザーに対するアクセス制限を強化している。2026年4月〜5月にかけて、IP封鎖（Ban）と本人確認（KYC）の二重の壁が中国開発者に深刻な影響を与えている。

## IP封鎖の実態

### 事例: 3ヶ月で3回目の封鎖

V2EXスレッド「**用了三个月 Claude Code 被封了，复盘下我排查 IP 问题的过程**」（スコア77）において、以下の詳細な分析が報告された：

#### 1. 「双ISP家宽」の罠

- Cogent AS174の「双ISP」VPSを購入
- ipinfo.ioではASN type: ISP、privacy: false、VPN/プロキシ検出なし
- ping0でも風控値が低い表示
- 結果：6週間で封鎖

#### 2. 検出ツールの矛盾

| ツール | ASN type | 判定 |
|--------|----------|------|
| ipinfo.io | ISP | 安全 |
| ipapi.is | **hosting** | **危険** |

- 同じIPでも検出ツールによって結果が異なる
- ipapi.isはASN層とCompany層を分けて表示
- Cogent AS174の実際のtypeはhosting

#### 3. ToDeskの副作用

- ToDesk（リモートデスクトップ）が`disablesleep`を1に設定
- 合盖不熄屏（カバーを閉じてもスリープしない）問題の原因
- リモートデスクトップソフトウェア共通のバグ可能性

## KYC（本人確認）の導入

### 身分認証メカニズム

AnthropicがClaudeプラットフォームに以下の本人確認を導入：

- **政府発行身分証明書**（パスポート、運転免許証、国民身份证）
- **ライブ自撮り**（リアルタイム写真）
- 第三者パートナーPersona Identities経由で実施

### 中国ユーザーへの影響

- 中国居民身份证での認証可否が不透明
- 海外企業への政府ID提出への抵抗
- 代替モデル（[[kimi-moonshot]]、[[glm-zhipu]]、[[minimax]]）への移行加速

## V2EXコミュニティの反応

- 「Anthropic真是绝了，刚收完钱就把我踢了」（スコア32）
- 「 Anthropic 宣布在 Claude 平台推行身份验证机制」（スコア80）
- 「如何在国内受限网络环境下使用官方claude或codex等模型」（スコア34）

## 対処法

1. **IP対策**: 複数の検出ツールで事前に確認
2. **モデル切替**: 国産モデルの活用（GLM、Kimi、MiniMax）
3. **API聚合**: 複数ソースからのアクセス確保
4. **ローカルデプロイ**: 开源モデルの活用

## 出典

| ソース | URL | スコア | ティア |
|--------|-----|--------|--------|
| V2EX — IP封鎖分析 | https://www.v2ex.com/t/1207240 | 77 | T1 |
| V2EX — KYC導入 | https://www.v2ex.com/t/1206060 | 80 | T1 |
| V2EX — Anthropic追放 | https://www.v2ex.com/t/1208892 | 32 | T1 |
| 36kr — 身分認証分析 | https://36kr.com/p/3769358632497922 | - | T1 |

## 関連ページ

- [[anthropic]] — AI研究企業
- [[claude-code]] — AIコーディングエージェント
- [[kimi-moonshot]] — 中国代替モデル
- [[glm-zhipu]] — 中国オープンソースLLM
