---
title: Tencent AI (騰訊AI) — 中国テック巨人のAI戦略
created: 2026-04-18
updated: 2026-04-28
tags: [company, ai, china, tech-giant, tencent]
aliases: ["Tencent AI", "騰訊AI", "Tencent", "腾讯"]
source_lang: zh-CN
---

# Tencent AI (騰訊AI) — 中国テック巨人のAI戦略

> **拠点**: 深圳
> **CEO**: 馬化騰（Pony Ma）、劉熾平（Martin Lau、総裁）
> **首席AI科学家**: 姚順雨（Yao Shunyu、元OpenAI研究員）
> **エコシステム**: WeChat (微信) 13億ユーザー
> **重要度**: 高 — WeChatエコシステム×AI×混元底座でスーパーアプリ最有力

## 概要

Tencent（騰讯）は中国最大のソーシャルメディア・ゲーム企業。WeChat（微信）という13億ユーザーのスーパーアプリを保有し、AI統合において最も強力なポジションにある。2025年末に姚順雨を首席AI科学家に招聘し、AI研究開発体制を抜本的に再編。混元（Hunyuan）を「会社級底座（企業レベル基盤）」に格上げした。

## AI製品ポートフォリオ（2026年4月時点）

### 基盤モデル: 混元 (Hunyuan)
- **最新モデル**: Hy3 Preview（2026年4月23日公開、オープンソース）
  - 295B総パラメータ / 21B活性（MoE）
  - 256Kコンテキスト、快慢思考融合
  - SWE-bench Verified 74.4%、推論効率40%改善
  - 前OpenAI研究員・姚順雨リーダーシップ下で開発
- **HY 2.0シリーズ**（2025年12月）: Instruct/Think両モデル、406B/32B活性
- **統合先**: 元宝、CodeBuddy、WorkBuddy、QQ、腾讯文档、微信検索
- **詳細**: [[tencent-hunyuan]]

### Agentプラットフォーム: QClaw
- 国内版: 10日で100万ユーザー、微信小程序経由
- 海外版（2026年4月）: WhatsApp/Telegram対応、Googleログイン
- OpenClawベースの極簡パッケージ、V2でマルチAgent対応
- **詳細**: [[tencent-qclaw]]

### C端アプリ: 元宝 (Yuanbao)
- 腾讯のネイティブAIアプリ
- 2025年春にDeepSeekモデルを併用、2026年4月にHy3 Previewを主力に
- 長文要約、コード生成、画像理解、会議サポート

### B端/開発者向け
- **CodeBuddy**: AIコーディングアシスタント
- **WorkBuddy**: 企業向けAIワークフロー
- **腾讯云TokenHub**: 混元APIプラットフォーム（¥1.2/百万tokens〜）
- **ima**: ナレッジプラットフォーム

## 組織再編と人材戦略

### 姚順雨のリーダーシップ（2025年末〜）
- 前OpenAI研究員を首席AI科学家に招聘
- LLMチームとAI Infraを一元管理
- AI Lab主力メンバーを混元チームに統合
- 「実用主義」路線へ転換 — ベンチマークより実際のワークフロー重視

### AI人材採用
- OpenAI、Meta、GoogleからトップAI研究者を積極的に採用
- 採用ペースは中国テック企業で最速
- 2025年度業績公告で「混元3.0、元宝、WorkBuddy、QClaw」をAI投資実効プロジェクトとして初公開

## WeChat × AI 戦略

- **微信AI Agent**（開発中）: 13億ユーザーのWeChatにネイティブAIを統合
- OpenClaw/QClawエコシステムが微信に接続済み
- 公众号（公式アカウント）、小程序（ミニプログラム）へのAI統合
- 決済、ソーシャル、ミニプログラムの既存インフラをAIで強化

## 市場ポジション

| 指標 | 値 |
|------|-----|
| WeChat MAU | 13億+ |
| QClaw国内ユーザー | 10日で100万 |
| 混元Hy3トークン価格 | ¥1.2/百万tokens（入力最低） |
| SWE-bench Verified | 74.4%（Claude Opus 4.6: 80.8%） |

## 課題と展望

### 課題
- **C端での存在感**: 元宝でDeepSeekと混元が併存、混元単独ブランディングが課題
- **微信Agent未発表**: 最大の潜在力だがまだ噂段階
- **最高精度での差**: SWE-benchでAnthropicに差

### 展望
- 2026年下期にHy3.0正式版リリース
- WeChatエコシステムへの全面統合が実現すれば中国最大のAIユーザーベース
- QClaw海外展開でグローバル市場に参入

## 競合他社

- **ByteDance/Doubao**: DAU1億、Seedモデル群、システムレベル統合
- **Alibaba/Qwen**: フルスタックAI、EC統合、Qwen Image 2.0
- **Baidu/文心一言**: ERNIE 5.0（2.4T）、中国AI検索最大手
- **DeepSeek**: オープンソース推論モデル、一時元宝に採用
- **Moonshot AI/Kimi**: K2.6（1T MoE）、長文コンテキストに強み

## 関連

- [[tencent-hunyuan]] — 騰訊自研の基盤LLMシリーズ
- [[tencent-qclaw]] — 極簡AIエージェントプラットフォーム
- [[openclaw]] — QClawのベースとなったOSSフレームワーク
- [[baidu-ernie]] — 競合：百度ERNIE 5.0
- [[qwen]] — 競合：Alibaba Qwen
- [[deepseek]] — 競合：DeepSeek
- [[kimi-moonshot]] — 競合：月之暗面 Kimi
- [[china-ai-superapp-race]] — 中国AIスーパーアプリ競争

## ソース

- [混元Hy3 Preview公式リリース（2026-04-23）](https://hy.tencent.com/hy3-preview)
- [Tencent QClaw Global Launch — Tencent公式](https://www.tencent.com/en-us/articles/2202318.html)
- [QClaw V2リリース — 腾讯云](https://cloud.tencent.com/developer/article/2653629)
- [字母AI — 混元Hy3 preview評価](https://www.sohu.com/a/1013810561_116132)
- [ChinAI #345 — WeChat×AI統合戦略](https://chinai.substack.com)


## 騰訊のAI不安：10年前のQQボットに隠された戦略（2026-04-29更新）

Juejin記事「腾讯的 AI 焦虑，藏在十年前的 QQ 机器人里」が、**騰訊のAI戦略の歴史的ルーツ**を10年前のQQボットに求める分析を提示。

### 分析の核心
- **QQボットの先見性**: 2016年時点で既にAIボット生态を構築
- **AI不安の文脈**: 騰訊がAI分野で後れを取っているとの自己認識
- **戦略的回帰**: 過去のQQボット経験を活用した現AI戦略
- **エコシステム優位性**: WeChat×QQの統合プラットフォーム戦略

### 中国AIエコシステムにおける騰訊の位置
- アリババ・バイドゥ・テンセントのAI競争において、騰訊は「応用・統合」に強み
- QQボット時代の経験が現在のAI Agent開発に活かされている
- WeChatミニプログラム生态との連携で独自ポジションを構築

### 混元大モデル × WeChatグループ投入の皮肉
騰訊は**10億元を投資**し、最先端の混元大モデルをWeChatグループに投入した。しかし、ユーザーが最も楽しんでいるのは依然として**10年前のQQボットの機能**。これは、騰訊のAI戦略における「技術先行・ユーザー後追い」のパラドックスを浮き彫りにしている。

- **技術面**: 混元大モデルは高度な能力を有する
- **ユーザー体験**: 単純なボット機能の方が受け入れられている
- **戦略的示唆**: AI統合において、ユーザーの既存行動パターンを無視した新機能投入は限定的な効果しか生まない

> 「腾讯的 AI 焦虑，藏在十年前的 QQ 机器人里」
> （騰訊のAI不安は、10年前のQQボットに隠されている）

> **出典**: Juejin — [腾讯的 AI 焦虑，藏在十年前的 QQ 机器人里](https://juejin.cn/post/7599591405312933929) [T2]

- [Tencent 2025年度業績公告 — AI投資プロジェクト初公開](https://www.tencent.com)
