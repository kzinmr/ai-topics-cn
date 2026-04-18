---
title: "AI Agent（智能体）— 中国語圏での議論動向"
created: 2026-04-15
updated: 2026-04-18
tags: [ai-agents, llm, concept, china]
aliases: ["AI Agent", "智能体", "AIエージェント", "Agentic AI"]
source_lang: zh-CN
---

# AI Agent（智能体）— 中国語圏での議論動向

> **トレンド順位**: #2（2026-04-18 集計）  
> **言及数**: 135件（36kr, Juejin, V2EX, WeChat）— 4ソース横断  
> **注目度**: 🔥🔥🔥🔥🔥  
> **推移**: 21件(04-15) → 80件(04-16) → 92件(04-17a) → 117件(04-17b) → **135件(04-18)**

## 概要

「智能体（AI Agent）」は、2026年4月現在、中国語圏のテック系メディアにおいて最も議論されている概念の一つである。ChatGPT、Claude、Gemini など主要 LLM がいずれもエージェント機能を前面に押し出す中、中国のテック・コミュニティでは「Agent とは結局何なのか」という基礎的な問いから、実装パターン、規制問題、次世代アーキテクチャに至るまで、多層的な議論が展開されている。

Juejin（掘金）上の人気解説記事では、Agent を「**今、全員が口にしているバズワード**」と位置づけ、単なるチャットボットとの本質的な違いを解説している[^1]。本稿では、中国語圏の一次ソースに基づき、AI Agent をめぐる定義・実践・規制の現況を整理する。

## 定義の変遷

### チャットボットから自律型システムへ

中国語圏での Agent の理解は、以下のように段階的に深化してきた：

| 段階 | 特徴 | 中国語での表現 |
|------|------|----------------|
| **Prompt 工学期** | プロンプトの工夫で LLM の出力を制御 | 「多加几个词就能让 GPT 听话」 |
| **Agent 期** | ツール呼び出し・計画・記憶を持つ自律システム | 「智能体」 |
| **Harness 期** | Agent を包括するシステム設計思想 | 「驾驭框架」 |

Juejin の技術記事では、この三段階を **Prompt → Agent → Harness** と整理し、「まだプロンプトを数語追加すれば GPT が言うことを聞くと思っている段階の人もいる（有人还停留在多加几个词就能让 GPT 听话的阶段）」と現状の認識格差を指摘している[^4]。

### 概念の分類整理

Prompt、Agent、Function Call、Skill、[[mcp|MCP]] など関連概念が乱立する中、Juejin 上で109件のいいねと226件のブックマークを獲得した分類記事[^5]が広く参照されている。この記事は「Prompt、Agent、Function Call、Skill、MCP，傻傻分不清楚？（区別がつかない？）」というタイトルで、各概念の境界を明確に定義した。

## Harness 概念の台頭

V2EX で注目を集めたのは、arXiv プレプリント（2604.08224）「Externalization in LLM Agents」の54ページにわたるサーベイ論文の要約スレッドである[^3]。この論文は LLM エージェントの統一的フレームワークとして以下の4要素を提唱している：

```
┌─────────────────────────────────┐
│           Harness               │
│  ┌───────┐  ┌────────┐         │
│  │Memory │  │Skills  │         │
│  └───────┘  └────────┘         │
│  ┌───────────────────┐         │
│  │   Protocols       │         │
│  │  (MCP等の通信規約) │         │
│  └───────────────────┘         │
│         ┌─────┐                │
│         │ LLM │                │
│         └─────┘                │
└─────────────────────────────────┘
```

**核心的洞察**: 外部ツールはモデル自体を強化するのではなく、**困難なタスクをより容易なタスクに変換する**。具体的には、想起（recall）を認識（recognition）に変えるメカニズムとして機能する。これは [[harness-engineering]] の基礎的な設計原理として注目されている。

## 中国語圏での実践事例

### マルチエージェント協調：GLM-5.1 の事例

[[glm-zhipu|智譜（Zhipu）]]の GLM-5.1 を用いた AI プログラミングの実践報告が Juejin で話題となった[^7]。注目すべきデータポイント：

- **23個のエージェント**が同時稼働
- マルチエージェント協調パイプラインを構築
- **1日で1,556メッセージ**を処理、クラッシュなし

これは [[claude-code]] などの海外ツールと比較する文脈でも議論されており、中国国産 LLM のエージェント能力の実用水準を示す事例として引用されている。

### 端末側エージェント（端侧 Agent）

モバイル端末上でのエージェント展開も活発に研究されている。Zero-Copy スクリーン知覚技術により、画面の内容をリアルタイムで認識し、端末上で自律的にタスクを実行するエージェントの構築が報告されている[^8]。

### RAG + Agent の統合実践

V2EX 上では、個人開発者が RAG（Retrieval-Augmented Generation）と Agent を統合した「Chat2Report」というプロダクトを開発した事例が共有されている[^9]。レポート自動生成に特化したこの実装は、独立開発者コミュニティにおける Agent 活用の典型例である。

### 注目プロジェクト

Juejin では「推荐几个牛逼的 AI Agent 项目（おすすめの凄い AI Agent プロジェクト）」と題した実践的なプロジェクト紹介記事も人気を集めている[^6]。

## エージェント権限と規制問題

中国語圏の Agent 議論において最も特徴的なのは、**規制・責任問題への早期からの注目**である。

36kr の記事では、以下のリスクシナリオが具体的に論じられている[^2]：

> 「智能体越权、系统瘫痪、数据外泄——那張賠償帳單、誰来签字？」  
> （エージェントの越権行為、システム麻痺、データ漏洩——その賠償請求書に、誰がサインするのか？）

この議論の核心は、Agent が **「コパイロット（copilot）」から「オートパイロット（autopilot）」へ** 移行する過程で生じる責任の空白地帯にある：

- **越権行為**: Agent が付与された権限を超えて行動した場合の法的責任
- **システム障害**: Agent の自律動作に起因するシステム障害の賠償責任
- **データ漏洩**: Agent がアクセスするデータの範囲と漏洩リスク

中国の AI 規制環境（生成式 AI 管理弁法等）との関連で、この問題は今後さらに重要性を増すと考えられる。

## 関連概念の整理

中国語圏の議論に基づく概念マップ[^5]：

| 概念 | 定義 | 位置づけ |
|------|------|----------|
| **Prompt** | LLM への指示文 | 最も基礎的なインターフェース |
| **Function Call** | LLM が外部関数を呼び出す仕組み | Agent の構成要素 |
| **Skill** | 再利用可能なタスク実行単位 | Agent の能力モジュール |
| **Agent** | 自律的に計画・実行・修正を行うシステム | 中核概念 |
| **[[mcp|MCP]]** | Model Context Protocol。ツール連携の標準規約 | Agent 間・ツール間の通信層 |
| **Harness** | Agent を含むシステム全体の設計枠組み | Agent の上位概念 |

## 2026-04-17 更新：Agent議論の爆発的拡大

前回トリアージ（04-15）21言及から**117言及**へ急増。WeChatメディアも含め4ソース横断となり、「ホットトピック」最高ランクを維持。

### Agent Skillsの体系化
- 「万字干货！Agent Skills从入门到精通」が掘金で大反響
- 2026年最も学ぶべきAI技能としてSkillsを推奨
- Claude Code、OpenClaw、Hermes Agent全てのAgentがSkillsに依存
- Source: [Agent Skills入門](https://juejin.cn/post/7628903339975540763) (T1: juejin)

### Agentアーキテクチャ論争：Hermes vs OpenClaw
- 「小龙虾该换爱马仕了？」（ロブスターをエルメスに乗り換えるべき？）が暘金で話題
- [[openclaw]]創業者Peter Steinbergerが[[anthropic|Anthropic]]に一時アカウント凍結された事件が発端
- オープンソースAgentフレームワークの商業矛盾が表面化
- Source: [Hermes Agent vs OpenClaw](https://juejin.cn/post/7629549824972488710) (T1: juejin)

### 復旦NLPチーム80頁Agent総説
- 復旦大学NLPチームが80ページの大規模Agent総説論文を発表
- AI智能体の現状と将来を体系的に整理
- WeChatメディア（機器学习算法与自然言語処理）経由で拡散
- Source: [復旦NLP Agent総説](https://weixin.sogou.com/) (T4: WeChat)

### [[function-calling]]の基盤技術としての再認識
- 「从对话到动作：用 Function Calling 把 LLM 接到真实 API」が注目
- Agentの核心メカニズムとしてのFunction Callingの解説が活発化
- Source: [Function Calling実装ガイド](https://juejin.cn/post/7629289037941915667) (T1: juejin)

### OpenAI Agents SDK大型アップデート
- 沙箱執行、ファイルシステムツール、可配置記憶を追加
- Agent開発が「動く」から「プロダクション対応」への転換点
- Source: [OpenAI Agents SDK大升级](https://juejin.cn/post/7628623224711315465) (T1: juejin)

### Tokenコスト問題
- 「Token成本失控？两大开源方案如何重构AI编程成本结构」がAgent運用の現実的課題を提起
- 30分のAgentセッションで大量のコンテキスト窓を消費する問題
- Source: [Token成本失控](https://juejin.cn/post/7629598336643366958) (T1: juejin)

## 04-18更新 — Agentエコシステムの拡大（2026-04-18）

前回（04-17b）117言及から**135言及**へ増加（**+15%**）。4ソース横断（Juejin, V2EX, 36kr, WeChat）を維持しつつ、議論の重心が「Agent とは何か」という定義論から、**Skills エコシステム・デプロイメント・実用ワークフロー**へと明確にシフトしている。

> **言及数推移**: 21件(04-15) → 80件(04-16) → 92件(04-17a) → 117件(04-17b) → **135件(04-18)**

### Agent Skills エコシステムの本格化

「万字干货！Agent Skills从入门到精通」（沃垠AI）が掘金で大きな反響を得ており、**「2026年最值得学习的AI技能是Skills（2026年に最も学ぶ価値のあるAI技能はSkillsだ）」**と明確に宣言している[^10]。前回更新で指摘した Skills の体系化トレンドがさらに加速し、独立した概念ページとして切り出す規模に達した。

→ 詳細は [[agent-skills]] を参照

### Hermes Agent（Nous Research）の中国語圏への浸透

Nous Research がオープンソースで公開した **Hermes Agent** が、中国語圏で急速に注目を集めている。

- Juejin で「一天一个开源项目（第75篇）」シリーズとして紹介され、**自己進化型 AI Agent（自我进化 AI Agent）**として位置づけられた[^11]
- V2EX では「Windows 一键部署 Hermes AI Agent」と題したデプロイガイドが複数投稿され、**個人開発者によるローカルデプロイメント**のハードルが急速に下がっている
- 前回更新の「Hermes vs OpenClaw」論争と合わせ、オープンソース Agent フレームワークの選択肢として定着しつつある

### Open Computer Use — オープンソース Computer Agent

V2EX で「开源 Open Computer Use」が共有された[^12]。デスクトップ操作を自律的に実行するコンピュータエージェントのオープンソース実装であり、Anthropic の Computer Use やOpenAI の Operator に対するオープンソース代替として議論されている。端侧 Agent（端末側エージェント）の流れと合流し、**GUI 操作の自動化**が Agent の主要ユースケースとして確立しつつある。

### n8n ワークフロー × Agent の統合

「n8n工作流：一键把复杂知识变成小红书科普卡片（n8nワークフロー：ワンクリックで複雑な知識を小紅書の科普カードに変換）」が掘金で紹介された[^13]。ノーコード/ローコードのワークフロー自動化ツール n8n と Agent を組み合わせ、コンテンツ生成パイプラインを構築する実践例である。Agent が単体ツールから**ワークフロー・オーケストレーションの構成要素**へと進化している傾向を示す。

### AI時代のキラーアプリ議論

V2EX で「什么会成为 AI 时代的杀手级应用？（AI時代のキラーアプリは何になるか？）」というスレッドが立ち[^14]、Agent 関連の議論が展開されている。単一の「キラーアプリ」ではなく、**Agent を基盤としたエコシステム全体**が次世代のプラットフォームになるという見方が主流であり、Skills・Harness・MCP といった本ページで追跡してきた概念群がそのまま議論のフレームワークとして参照されている点が注目に値する。

### 04-18 時点の傾向まとめ

| 傾向 | 04-17b | 04-18 | 変化 |
|------|--------|-------|------|
| 総言及数 | 117 | 135 | +15% |
| 定義・概念論 | 主流 | 継続 | 新規参入者向け記事が持続 |
| Skills エコシステム | 萌芽 | **本格化** | 独立概念ページ化 |
| デプロイメント実践 | 散発 | **急増** | Hermes Agent 中心 |
| ワークフロー統合 | — | **新出** | n8n 等との連携事例 |
| Computer Agent | 端侧Agent言及 | **OSS実装共有** | Open Computer Use |

## 関連リンク

### 内部リンク

- [[mcp]] — Model Context Protocol の詳細
- [[claude-code]] — Anthropic のコーディングエージェント
- [[glm-zhipu]] — 智譜 GLM シリーズ
- [[harness-engineering]] — Harness 設計論
- [[function-calling]] — Agentの基盤メカニズム
- [[openclaw]] — OpenClaw Agentフレームワーク
- [[agent-skills]] — Agent Skillsエコシステム
- [[hermes-agent]] — Nous Research の自己進化型 Agent
- [[vector-db]] — Agentの長期記憶ストア

### 外部ソース（中国語）

| # | タイトル | ソース | ティア | URL |
|---|---------|--------|--------|-----|
| 1 | 人人都在说的 Agent，到底是个什么东西？ | Juejin（掘金） | Tier-2 技術コミュニティ | https://juejin.cn/post/7599299048302772267 |
| 2 | 智能体越权…那張賠償帳單、誰来签字？ | 36kr | Tier-1 テックメディア | https://36kr.com/p/3767348033126918 |
| 3 | arXiv 2604.08224 サーベイ要約スレッド | V2EX | Tier-2 技術フォーラム | https://www.v2ex.com/t/1206029 |
| 4 | Prompt → Agent → Harness 三段階論 | Juejin（掘金） | Tier-2 技術コミュニティ | https://juejin.cn/post/7628556428008882202 |
| 5 | Prompt、Agent、Function Call、Skill、MCP 分類解説 | Juejin（掘金） | Tier-2 技術コミュニティ | https://juejin.cn/post/7614205951297732654 |
| 6 | 推荐几个牛逼的 AI Agent 项目 | Juejin（掘金） | Tier-2 技術コミュニティ | — |
| 7 | Agent 用于 AI 编程（GLM-5.1 実践） | Juejin（掘金） | Tier-2 技術コミュニティ | https://juejin.cn/post/7627818680535957556 |
| 8 | 端侧 Agent（Zero-Copy スクリーン知覚） | Juejin（掘金） | Tier-2 技術コミュニティ | — |
| 9 | RAG + Agent 実践（Chat2Report） | V2EX | Tier-2 技術フォーラム | — |
| 10 | 万字干货！Agent Skills从入门到精通 | Juejin（掘金） | Tier-2 技術コミュニティ | https://juejin.cn/post/7628903339975540763 |
| 11 | 一天一个开源项目（第75篇）：Hermes Agent | Juejin（掘金） | Tier-2 技術コミュニティ | https://juejin.cn/post/7629561452530237459 |
| 12 | 开源 Open Computer Use | V2EX | Tier-2 技術フォーラム | https://www.v2ex.com/t/1206760 |
| 13 | n8n工作流：复杂知识→小红书科普カード | Juejin（掘金） | Tier-2 技術コミュニティ | — |
| 14 | 什么会成为 AI 时代的杀手级应用？ | V2EX | Tier-2 技術フォーラム | https://www.v2ex.com/t/1206768 |

---

[^1]: 「人人都在说的 Agent，到底是个什么东西？」Juejin, 2026. https://juejin.cn/post/7599299048302772267
[^2]: 「智能体越权、系统瘫痪、数据外泄——那張賠償帳單、誰来签字？」36kr, 2026. https://36kr.com/p/3767348033126918
[^3]: arXiv 2604.08224「Externalization in LLM Agents」サーベイ要約. V2EX, 2026. https://www.v2ex.com/t/1206029
[^4]: 「Prompt → Agent → Harness」三段階論. Juejin, 2026. https://juejin.cn/post/7628556428008882202
[^5]: 「Prompt、Agent、Function Call、Skill、MCP，傻傻分不清楚？」Juejin, 2026. https://juejin.cn/post/7614205951297732654
[^6]: 「推荐几个牛逼的 AI Agent 项目」Juejin, 2026.
[^7]: 「Agent 用于 AI 编程」GLM-5.1 マルチエージェント実践報告. Juejin, 2026. https://juejin.cn/post/7627818680535957556
[^8]: 端侧 Agent・Zero-Copy スクリーン知覚. Juejin, 2026.
[^9]: RAG + Agent 実践「Chat2Report」. V2EX, 2026.
[^10]: 「万字干货！Agent Skills从入门到精通」沃垠AI. Juejin, 2026. https://juejin.cn/post/7628903339975540763
[^11]: 「一天一个开源项目（第75篇）：Hermes Agent - Nous Research 开源的自我进化 AI Agent」 Juejin, 2026. https://juejin.cn/post/7629561452530237459
[^12]: 「开源 Open Computer Use」 V2EX, 2026. https://www.v2ex.com/t/1206760
[^13]: 「n8n工作流：一键把复杂知识变成小红书科普卡片」 Juejin, 2026.
[^14]: 「什么会成为 AI 时代的杀手级应用？」 V2EX, 2026. https://www.v2ex.com/t/1206768
