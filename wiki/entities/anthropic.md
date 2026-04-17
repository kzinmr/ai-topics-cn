---
title: Anthropic — AI研究企業
created: 2026-04-17
updated: 2026-04-17
tags: [company, lab, ai-safety, claude, anthropic]
aliases: ["Anthropic", "anthropic"]
source_lang: zh-CN
---

# Anthropic — AI研究企業

> **トレンド順位**: #4（2026-04-17集計、41言及）
> **ソース**: 36kr, Juejin, V2EX（全3ソース）
> **重要度**: 高 — Claudeシリーズ開発元、AI安全のリーディングカンパニー

## 概要

Anthropicは、OpenAIの元研究者らによって設立されたAI研究企業。Claudeシリーズの大規模言語モデル（[[claude-code]], [[claude-opus-4-7]]）の開発元として知られる。2026年4月現在、中国語圏のAIディスコースにおいて**41件の言及**があり、OpenAI（40件）と拮抗する注目度を誇っている。

## 最新動向（2026年4月17日）

### Claude Opus 4.7 リリース

Anthropicは2026年4月16日に**Claude Opus 4.7**を正式リリース。SWE-bench Verifiedで87.6%（+6.8pt）、CursorBenchで70%（+12pt）を達成。視覚処理能力も約3倍に向上。詳細は[[claude-opus-4-7]]参照。

36krは「Opus 4.7 压根没想做"最强模型"：各位吹Claude的速度都跟不上Anthropic 的节奏了」（Opus 4.7は元々「最強モデル」を目指していなかった：Claudeを吹く連中の速度はAnthropicのペースに追いついていない）と報じた。

> **出典**: 36kr — [https://36kr.com/p/3770336476578568](https://36kr.com/p/3770336476578568) [T1]

### 強制身分認証（KYC）導入

AnthropicがClaudeプラットフォームへのアクセスに**政府発行身分証明書 + 手持ち自撮り**による実名認証を義務化したことが中国語圏で大きな波紋を広げている：

- **中国大陸ユーザーへの影響**: 中国居民身份证が認証に使用できるか不透明
- **プライバシー懸念**: 海外企業への政府ID提出への抵抗
- **代替モデルへの移行加速**: [[kimi-moonshot]]、[[glm-zhipu]]、[[coding-plan]]への流入

36krは「一本正经的Claude"身份验证"，藏着赛道最残酷的博弈」（真面目なClaude身分認証の裏に、業界最も残酷な駆け引きが隠されている）と分析。

V2EXでは「大家的 Claude 弹了 kyc 嘛」（みんなのClaudeにKYCポップアップ出た？）というスレッドが立ち、掘金でも「彻底疯狂，Claude居然要上传身份证！」（完全に狂気、Claudeがまさか身分証アップロードを要求するとは！）と題した記事が16いいねを獲得。

> **出典**: 36kr — [https://36kr.com/p/3769358632497922](https://36kr.com/p/3769358632497922) [T1]
> **出典**: V2EX — [https://www.v2ex.com/t/1206627](https://www.v2ex.com/t/1206627) [T1]
> **出典**: 掘金 — [https://juejin.cn/post/7628825069887799339](https://juejin.cn/post/7628825069887799339) [T2]

### Nature論文「潜意識伝染」

Anthropicの研究チームが**Nature**学術誌で「**潜意識伝染**」（Subconscious Propagation）を主題とする重要論文を発表。AIモデルの安全性に関する新たな知見を示した。

詳細は[[ai-safety-subconscious]]参照。

### AI安全の「安全承諾」問題

36krは「硅谷大模型的"安全承诺"，正让世界失去安全感」（シリコンバレー大モデルの「安全承諾」が、逆に世界を不安にしている）と報じた。Anthropicの安全声明が実際のセキュリティ確保に繋がっているかという疑問が提起されている。

> **出典**: 36kr — [https://36kr.com/p/3770223251866372](https://36kr.com/p/3770223251866372) [T1]

## Claude Routines & Hooks

AnthropicはClaude Codeに**Routines**（定时任务）と**Hooks**（フック）機能を追加。Claude Codeを自律型開発エージェントへと進化させた。

- **Routines**: スケジュール・API・GitHubイベントをトリガーとする自動実行
- **Hooks**: ワークフローの各段階にカスタムロジックを注入

中国メディアはこれを「云端员工」（クラウド従業員）と表現。

## Anthropic vs OpenAI 競争構造

| 次元 | Anthropic | OpenAI |
|------|-----------|--------|
| フラグシップ | Claude Opus 4.7 | GPT-5.4 |
| エージェント | [[claude-code]] | [[claude-code]] (Codex) |
| ベンチマーク | SWE-bench 87.6% | 非公開 |
| 安全アプローチ | Nature論文、KYC導入 | GPT-5.4-Cyber |
| 中国市場 | KYCでアクセス制限 | Codex「超级龙虾」で攻勢 |

36krの分析では「奥特曼又得失眠」（Sam Altmanはまた眠れない）と評され、Opus 4.7の性能向上がOpenAIを脅かしている状況が描かれている。

## 関連リンク

### 内部リンク

- [[claude-code]] — Anthropicの主力製品
- [[claude-opus-4-7]] — 最新フラグシップモデル
- [[ai-safety-subconscious]] — Nature論文
- [[kimi-moonshot]] — 中国代替モデル
- [[glm-zhipu]] — 中国オープンソースLLM

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| 36kr — Opus 4.7分析 | [36kr.com/p/3770336476578568](https://36kr.com/p/3770336476578568) | T1 | Anthropicのペース論 |
| 36kr — 安全承諾 | [36kr.com/p/3770223251866372](https://36kr.com/p/3770223251866372) | T1 | AI安全の逆説 |
| 36kr — 身分認証分析 | [36kr.com/p/3769358632497922](https://36kr.com/p/3769358632497922) | T1 | KYC問題の深層 |
| V2EX — KYC議論 | [v2ex.com/t/1206627](https://www.v2ex.com/t/1206627) | T1 | ユーザー反応 |
