---
title: OpenClaw — オープンソースAIエージェント
created: 2026-05-02
updated: 2026-09-01
tags: [concept, agent, open-source, openclaw, china]
aliases: ["OpenClaw", "open-claw", "オープンクロー"]
source_lang: zh-CN
---

# OpenClaw — オープンソースAIエージェント

## 概要

OpenClawは、2026年4〜5月に中国で急成長したオープンソースAIエージェントプロジェクト。Juejinで「阿里出手了！终于不怕OpenClaw烧token啦、直接算力自由〜」と報道され、個人開発者から注目されている。

## 特徴

### トークン効率最適化

- 阿里（Alibaba）がOpenClawのトークン消費問題に対処
- 「算力自由」（計算リソースの自由な利用）を実現するアプローチ
- 個人開発者にとって実用的なコストパフォーマンス

### 自動投稿機能

- Juejinでは「用OpenClaw实现小红书自动发帖」が報告
- 小红书（Xiaohongshu/RED）への自動コンテンツ投稿
- MCP（Model Context Protocol）との統合により、プラットフォーム横断的な自動化が可能

### コミュニティ評価

- V2EXで「OpenClaw, Hermes, Mercury或其他，哪个个人Agent能真正投入使用？」と議論
- 個人Agentの実用性比較で常に名前が挙がる
- 376k+ Starを獲得（GitHub v2026.5.28時点で376K）

## 競合エージェントとの比較

| エージェント | 特徴 | 開発元 |
|---|---|---|
| OpenClaw | オープンソース、トークン効率 | コミュニティ |
| Claude Code | 高品質、MCP統合 | Anthropic |
| Hermes | 多機能、スキルシステム | Nous Research |
| Mercury | 軽量、高速 | 不明 |
| Codex | OpenAI純正、電話認証必須 | OpenAI |

## 業界への影響

- 個人Agentの実用化が加速
- オープンソースAgentと商用Agentの競争が激化
- 「Agentは最終的にデータベース問題」という批判に対し、OpenClawは実務重視のアプローチで応える

> **出典**: Juejin — [阿里出手了！终于不怕OpenClaw烧token啦](https://juejin.cn/post/7610637031321698330) [T1]
> **出典**: Juejin — [用OpenClaw实现小红书自动发帖](https://juejin.cn/post/7615379311402467354) [T1]
> **出典**: V2EX — [OpenClaw, Hermes, Mercury或其他](https://www.v2ex.com/t/1209907) [T2]

## 関連リンク

### 内部リンク

- [[agent-skills]] — Agentのスキル機能
- [[mcp]] — Model Context Protocol
- [[china-coding-agents]] — 中国のコーディングエージェント
- [[claude]] — Claudeモデル
- [[hermes-agent]] — Hermes Agent

### 外部ソース

| ソース | URL | ティア | 概要 |
|---|---|---|---|
| Juejin — OpenClaw烧token | [juejin.cn/post/7610637031321698330](https://juejin.cn/post/7610637031321698330) | T1 | 阿里の最適化 |
| Juejin — OpenClaw小红书 | [juejin.cn/post/7615379311402467354](https://juejin.cn/post/7615379311402467354) | T1 | 自動投稿機能 |
| V2EX — Agent比較 | [v2ex.com/t/1209907](https://www.v2ex.com/t/1209907) | T2 | 実用性議論 |

## 2026年5月下旬最新動向

### ▼ v2026.5.28 リリース: 376K Stars、マルチプロバイダー対応とAgentランタイム改善（5月30日）

OpenClawはGitHubで376K Starを記録。v2026.5.28リリースで以下を対応:

- **マルチプロバイダー対応拡大**: Claude Opus 4.8、Fal Krea画像生成、NVIDIAモデルカタログ、MiniMaxストリーミング音楽、音声モデルカタログ
- **Codex/エージェント改善**: サブエージェントのcwd/workspace分離強化、セッションロックのタイムアウト解放、フックコンテキストのprompt-local化
- **GitHub Copilot agent runtime** と **Codex Supervisor** プラグインパッケージを追加
- **iOSアプリ**: Pro Command、Chat、Agents、Settings、hosted push relay、realtime Talkをgatewayセッションに接続
- **Workboard**: アクティブエージェントの作業追跡とハンドオフ用コーディネーションツール

### ▼ v2026.5.27: OpenAI埋め込みプロバイダーとセキュリティ境界強化（5月28日）

- **Memory**: OpenAI互換embeddingプロバイダー（ローカル/ホステッドエンドポイント対応）
- **Providers**: Pixverse動画生成プロバイダー追加
- **セキュリティ**: 信頼できないグループプロンプトメタデータをシステムプロンプト外にルーティング、QQBotフォールバック承認ボタンをゲート、admin権限によるノード/デバイスロール承認を必須化
- **Gateway/パフォーマンス**: 読み取り専用セッションキャッシュ、プラグインメタデータフィンガープリントキャッシュ、分離cronプロンプトキャッシュ最適化

### ▼ 主要開発者: @steipete、@yetval、@luoyanglangら

v2026.5.27/28リリースで最も貢献が多い開発者:
- @steipete: リリースマネージャー、コア改善
- @yetval: Codexランタイム、プロバイダーauth改善
- @luoyanglang: エージェントランタイム、compaction改善
- @vincentkoc: プロバイダー拡張、音声モデルカタログ

**出典**: GitHub OpenClaw Releases v2026.5.28, v2026.5.27

## 2026年9月: 「时代的眼泪」化と拡散優位論の反証（ChinAI #373 / 量子位 2026-08-31）

### ▼ ブームから半年での「集体悼念」フェーズ（量子位・梦瑶）

2025年11月底のローンチから約100日で25万+Star（3月3日、React超え）、3月末に33万+、8月時点で38万+Star・Fork 8万超とGitHub史上最大の成長曲線を描いた一方、言及量は実質ゼロに近くなり、X上では「集体悼念」（集体追悼）対象化。「AI圈连时代的眼泪保质期都开始按月算了」と揶揄される。プロジェクト自体は存活（開発継続・8月も更新）だが、話題性は「春风化雨」＝大厂派生品に移転。

### ▼ 派生30+款と各社の低価格化（「原厂代打」）

- **腾讯**: WorkBuddy（一键部署+微信远程操控）、QClaw
- **百度**: DuMate+龙虾全家桶（桌面/云端/手机/安全/家用虾）
- **网易有道**: LobsterAI（本地个人Agent、Skills/MCP/IM远程）
- **智谱**: AutoClaw（本地一键部署、预装Skills、飞书接続、「自进化」へ）
- **火山引擎**: ArkClaw（7×24稼働、Runtime・多Agent协作へ拡張）
- **MiniMax**: MaxClaw（Alibaba Cloud Harness Era連携は[[minimax]]参照）

### ▼ 衰退要因の技術分析（量子位）

1. **Token烧钱**: 24時間常時稼働Agentはコンテキスト維持・ツール呼び出し・失敗リトライで枯渇（「第七天：救啊，我Token呢？」）
2. **权限と安全のジレンマ**: Meta安全責任者がメール権限を開放→Agentがメール削除を停止できなかった事件に象徴される「贾维斯に近づけるほど权限が必要、权限が大きいほど失控代价が大きい」構造矛盾
3. **原厂harnessへの置換**: OpenAI Agents SDK（文件操作/命令执行/长任务/沙箱运行をmodel-native harnessとしてバンドル）、Codex完結Harnessにより、自前構成（モデル選択・権限設定・Skill投入）の価値が消失。関心の軸は「どう安定して働かせるか」＝[[harness-engineering]]へ移行
4. **遗产**: OpenClawの失敗＝次段Agentの論点（手脚付与・抑制、常時稼働とコスト、自由と回収）を先出し実演。「人人养一个OpenClaw」→「人人琢磨造更靠谱的OpenClaw」

### ▼ 創作者 Peter Steinberger（@steipete）の動向

2026年2月にOpenAIへ正式加入、Codex/個人Agent方向。Software Factory概念（Agent集団の自己反復＋人の役割は目標設定と検収）を主張。Dropbox共同創業者Drew Houstonと各$100万を出捐しOmacom Foundation founding patronに（Linux桌面普及のためのインフラ・OSS支援）。

### ▼ 「中国の拡散優位論」の反証（Jeff Ding解説コメント）

- NBC News（SecurityScorecard経由）「中国でのOpenClaw利用は米国比ほぼ倍」→ CFR研究員が「China's diffusion advantage」論拠に転用。しかし同一SecurityScorecard実データ（8/29検索）は米国18.7k / 中国17.0kで、倍差主張は誤読か旧データ
- OpenClawは拡散指標として不適: 採用閾値の高さ（モデル選択・データ接続・Skill統合が自前）＋token消費＋セキュリティ問題
- 拡散がクラウド経由で進むなら、中国は米国の後塵を拝む蓋然性が高い（「China's AI Implementation Gap」＝云计算採用の遅れ）
- JPMorgan: OpenClaw系Agent（AutoClaw/MaxClaw）への熱狂は中国科技株の短期的押し上げ要因だが、主要クラウド事業者の売上成長率は2025→2026、2026→2027と減速予測

**出典**: ChinAI #373（Jeff Ding、2026-08-31）/ 量子位「OpenClaw: It rose to fame, it was loved, and now it's over」— raw: `wiki/raw/articles/substack.com--redirect-5118dff9-...--b40d9114.md`

