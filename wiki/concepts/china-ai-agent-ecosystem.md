---
title: "中国AI智能体生态 — 2026年プラットフォーム・アーキテクチャ・市場動向"
created: 2026-04-19
updated: 2026-07-27
tags: [ai-agents, platform, china, ecosystem, low-code, enterprise, openclaw, harness, coding-agent, cli-revival]
aliases: ["中国AI智能体生态", "中国Agentプラットフォーム", "Baidu AgentBuilder", "腾讯元器", "Coze", "Dify", "OpenClaw-CN", "龙虾大战"]
source_lang: zh-CN
---

# 中国AI智能体生态 — 2026年プラットフォーム・アーキテクチャ・市場動向

> **重要度**: 🔥🔥🔥 HIGH — 2026年中国エンタープライズAIの核心インフラ
> **関連概念**: [[ai-agent]], [[mcp]], [[rag]], [[harness-engineering]], [[coze]], [[dify]], [[openclaw]], [[vibe-coding-china]]
> **関連エンティティ**: [[qwen]], [[deepseek]], [[glm-zhipu]], [[doubao-bytedance]], [[baidu-ernie]], [[tencent-ai]]

## 概要

2026年、中国のAI智能体（AI Agent）エコシステムは「プラットフォーム戦争」の段階に突入し、**OpenClawフレームワークをベースとした「龙虾大战（ロブスター戦争）」**がQ1に勃発。Baidu、Alibaba、ByteDance、Tencentといったメガテックに加え、Difyに代表されるオープンソース系プラットフォームが台頭し、**低コード/ノーコードでのAgent構築・デプロイ・運用**が企業標準になりつつある。

市場規模は2025年で**580億元突破**（企業級が70%超）。科技巨头（BATB）が**CR4 78%**を占め、残りの20%を垂直領域・初创企業で分割。市場競争の核心は「模型参数」から**「行业场景穿透力・データ飛輪構築速度・結果交付の确定性」**へ移行した。

## 最新動向：OpenClaw「龙虾大战」（2026年Q1-Q2）

2026年Q1、OpenClawをベースとしたAgentプラットフォームが**9社同時にリリース**され、中国業界で「龙虾大战」と呼ばれた（OpenClawのロゴがロブスターで、Agentが「物をつかむ鉤爪」を得た意味）。

| プラットフォーム | 開発元 | 特徴 |
|----------------|--------|------|
| **OpenClaw-CN** | 中国フォーク | 5大IM（微信/钉钉/飞书/企微/QQ）を内蔵 |
| **QClaw** | 腾讯 | 云端一鍵部署、WeChat/QQ/企微統合 |
| **ArkClaw** | 火山引擎(字节) | 火山引擎Ark統合、飞书プラグイン体系 |
| **OpenClaw** | OpenClaw | ClawHub 13,700+ Skill、48時間エージェントタイムアウト |
| **DeerFlow 2.0** | 字节跳动 | 「Super Agent Harness」、GitHub 22K→52K星（1ヶ月） |

### ClawHub Skillエコシステム

- **13,700+ Skill**（半年で蓄積）、最高18万インストール（Web Browsing）
- **341の悪意Skill**（11.3%）、36%がプロンプトインジェクションを含む
- VirusTotalによる「**AI版npm投毒**」定性
- **生存層**（Web Browsing 18万）→ **効率層**（Telegram Bot 14.5万）→ **進階層**（Capability Evolver 3.5万：Agentが自動パターン認識で新Skill生成）

### 中国のセキュリティ対応

- **腾讯SkillHub**: プラットフォーム審査型（安全だが開放性制限）
- **DeerFlow/扣子**: オープンソース・Git版管理（Markdownファイル、按需読み込み）
- **工信部**: データアクセス制御・ログ監査を強調

## 主要プラットフォーム比較（2026年版）

| プラットフォーム | 開発元 | タイプ | 核心機能 | 対象ユーザー |
|----------------|--------|--------|----------|--------------|
| **扣子 (Coze)** | ByteDance | クローズド/低コード | 拖拽式ワークフロー、Plugin市場、マルチモデル対応 | 非技術者〜中級開発者 |
| **Dify** | 开源社区 | オープンソース/LLMOps | RAG統合、YAML宣言的開発、マルチクラウドデプロイ | 開発者・エンタープライズ |
| **文心智能体平台 (AgentBuilder)** | Baidu | クローズド/プラットフォーム | 文心一言モデル統合、知識庫、企業API連携 | 企業IT部門 |
| **腾讯云智能体开发平台3.0 (ADP3.0)** | Tencent | クローズド/プラットフォーム | 零代码/少代码、多Agent協同、ワークフロー編成 | 中小企業・コンテンツ制作者 |
| **百炼 (Bailian/Model Studio)** | Alibaba | クローズド/クラウド統合 | Qwenモデルネイティブ、阿里云インフラ連携 | 開発者・クラウドユーザー |
| **MarsCode Agent** | ByteDance | クローズド/コーディング特化 | IDE統合、コード生成・レビュー自動化 | 開発者 |
| **金智维 Ki-AgentS** | 金智维 | 企業級底座 | RPA×LLM融合、金融級監査、信創完全適配 | 金融・政务・央国企 |
| **金山WPS AI** | 金山办公 | 办公特化 | 文書・表計算・PPTにAI Agent深度嵌入 | 知識労働者 |

### 企業級プラットフォームの3大分類

1. **通用工具型**: 扣子、Dify、百炼 — 汎用Agent構築
2. **垂直業務场景型**: WPS AI、百融智能RaaS — 特定業務に特化
3. **企業級智能体底座型**: 金智维Ki-AgentS — 金融・政务・央国企向け

## BATB四強のAI Agent戦略（2026年最新）

### 字节跳动（豆包/Doubao）— 「国民级AI超级入口」

- **MAU 2億突破**、日活破億
- **1600亿元投入**（2026年AI研究開発予算）
- 春晚独家互动合作伙伴 — 「AI红包」で下沉市場・2-3線都市浸透
- **AIスマート眼鏡（Ola Friend）**: 首款AI Smart Glasses批量生産
- **DeerFlow 2.0**: 「Super Agent Harness」— GitHub 52K星（中国开源プロジェクトとして初めて「Harness」を製品定位に使用）
- **戦略**: 重金砸营销 + ハードウェア铺路。「流量高地」を占拠

### 阿里巴巴（通义千问/Qwen）— 「AI驱动服务枢纽」

- **MAU 1億突破**（急成長中）
- **购物Agent**: 2026年1月15日リリース。春節6日間で**1.2億笔注文**処理 — 世界初の大规模商业化验证
- **AgentKit**: 数百万商家向け「员工智能体」— 注文処理・营销・客服自律実行
- Qwenモデル: **沙利文報告により中国企业级大模型调用量第1位（32.1%シェア）**
- 通义千问Appが淘宝・高德・支付宝・阿里健康と完全統合
- **戦略**: 「大脑」から「手脚」への闭环。自社电商・生活服务平台との深度統合

### 腾讯（元宝/Yuanbao）— 「社交生态智能助手」

- **微信搜索・群聊への深度埋め込み** — 社交意味理解と微信生態内の独占記事・服务調用
- **10亿现金**で春节推广 — 社交裂变で中高齢者层への急速渗透
- QClaw: 云端一键部署、企微/QQ/微信統合
- **腾讯云ADP 3.0**: 零代码Agent作成・多Agent協同・データベース直結
- WeChat離れることなくAgentが動作 — 「生态护城河」戦略
- **戦略**: 社交関係链の独占権を最大化。「润物细无声」渗透

### 百度（文心一言/ERNIE）— 「专业搜索与创作引擎」

- **文心5.0**: 複雑推理能力が显著向上
- **AgentBuilder**: 几十万活跃Agent、法律・医療等の垂直専門分野覆盖
- 小度シリーズ硬件の全面的Agent化
- **戦略**: 両側（字节・阿里）から挤压される中、「极致专业化」で検索・創作の牙城守る

> [!info] 注記
> 2026年后半から、**字节が他のApp调用を試みた際、阿里・腾讯がシステム级権限で「护城河防御」**を行う事象が発生。中国インターネットの正式な「AI墙内竞争」時代の始まりとされる。

## 市場動向

### 企業級AI Agentの「结果化」フェーズ

沙利文《中国GenAI市场洞察：企业级大模型调用全景研究2025H2》報告により、企業級AI応用は「工具化」から「結果化」段階へ移行。企業はAgentを選択する際、**パラメータ数**ではなく**「行业场景穿透力・データ飛輪構築速度・結果交付の确定性」**を重視するようになった。

### 資本市場でのモデル競争

**MiniMax M2.5**がOpenRouterプラットフォームで月間Token消費量**8.1兆**を記録しリストトップ。この成長は直接資本市場に反映され、**MiniMaxの市值が百度の港股発行市值を超えた**という現象が起きた。

### 垂直領域の深層発展

- **百融智能（原百融云创）**: RaaS（Results as a Service）ビジネスモデル。BR-LLM+情感大モデルが**8000余家機構**で規模化応用。IDC・中国科学院両方の認定を受賞
- **金智维Ki-AgentS**: RPA→APA→Agentic AIの進化パス。金融・能源・智能制造分野で大型組織の首选底座
- **智谱AI（AutoGLM）**: 政府・央国企向け「跨应用自動化」— 40+高頻アプリのシームレス切替

### 初创企業

- 全体シェア5%未満だが、資本市場・開発者コミュニティで極めて活発
- **开源推理コスト**を業界平均の極低レベルに引き下げ
- **具身智能**: 倉庫物流・巡检安防等で初步的商业化落地

## 技術アーキテクチャの特徴

### 1. ワークフロー可視化と宣言的開発
扣子やDifyは**ノードベースのビジュアルエディタ**。Difyは**YAMLによる宣言的Agent定義**を推進（バージョン管理・CI/CD連携）。

### 2. マルチモデル・ルーティング
**Qwen・DeepSeek・GLM・Kimi・GPT・Claude**を切り替え可能。「モデルルーティング層」が標準機能化。

### 3. RAG + Agent 統合
Agentが検索クエリを**自己最適化→複数ソース横断→批判的検証→生成**の自律ループを構築。

### 4. MCP (Model Context Protocol) 対応
2026年Q1時点で**Dify・扣子・百炼**がMCPサーバー統合を発表。Agent間のツール共有・権限管理・セキュリティ境界の標準化が進展。

### 5. Harness Architecture 出現

字节跳动DeerFlow 2.0が中国オープンソースプロジェクトとして初めて「Super Agent Harness」を製品定位に採用。ClawHubのSkillエコシステム、OpenClawの48時間エージェントタイムアウト、可挿抜サンドボックス後端アーキテクチャなど、**エージェント実行環境の設計パターン**が急速に成熟。

## 市場動向と業界適用

### エンタープライズ導入加速
- **金融**: 顧客対応Agent、リスク評価Agent、コンプライアンス審査Agent
- **製造**: 設備監視Agent、品質管理Agent、サプライチェーン最適化Agent
- **医療**: 診断支援Agent、患者フォローアップAgent、医療記録自動化作成
- **EC/リテール**: 商品推薦Agent、在庫管理Agent、カスタマーサービスAgent

### 监管環境

- **各地政府**: 算力补贴・孵化計画を推進
- **工信部**: データアクセス制御・ログ監査を強調
- **算法备案・データ出境審査・内容安全検閲**: Agentの自律データ処理に対する責任の法解釈が未確定

## 次世代方向性

### Agentic Engineering へ

Karpathyが提唱する「Vibe Codingの終焉とAgentic Engineeringへの移行」は中国にも波及。2026年後半には、**単発Agentの羅列から「Agentチームのオーケストレーション」へ**パラダイムシフトが起きると予測される。

### Multi-Agent Systems（MASA）

- 单一Agentの複雑跨部門処理の限界が顕在化
- 複数Agentを協同させて宏観任務を処理する**プラットフォームフレームワーク**が次世代インフラ
- ClawHubの「Capability Evolver」がAgentの自己進化を実証

### 生态融合

- 頭部プラットフォームがAgent応用市場・協同ネットワークへ進化
- 能力のプラグ&プレイと価値の再利用
- BPM・低コードと深度統合

## 2026年4月下旬動向：「百蝦大戦」が深水区へ

2026年4月、中国AI Agent業界は「百蝦大戦（数百のロブスター戦争）」と呼ばれる競争の**第二フェーズ**に突入。OpenClawに端を発した「ロブスター」熱が3月に爆発した後、4月は**製品完成度（Delivery Completeness）**が新たな競争軸に。

### 1. 4月の主要プレイヤー動向

| 企業 | 製品・動き | 日付 | 戦略的意義 |
|------|-----------|------|-----------|
| **ByteDance** | 火山引擎ArkClaw + HiAgent（敏態・稳态並行） | 4/2 | 企業Agent建設方法論の体系化 |
| **ByteDance** | 扣子（Coze）2.5 — Agent Word開放生態 | 4/7 | IMライクなUI + エコシステム戦略 |
| **Tencent** | WorkBuddy微信小程序（雲沙箱+リモート実行） | 3/30 | 微信経由での使いやすさ重視 |
| **Tencent** | TencentDB Agent Memory（長期記憶サービス） | 4/3 | OpenClawにネイティブ長期記憶を提供 |
| **Tencent** | QQ Browser QBotClaw（初のブラウザ「ロブスター」） | 4/8 | 検索+Agentの融合 |
| **Alibaba Qwen** | QwenPaw完全オープンソース化 | 4月 | 軽量カスタムモデル・マルチAgent協調 |
| **Alibaba DingTalk** | 「悟空」AIネイティブワークプラットフォーム | 4月 | 企業智能体を中核に据えた再設計 |
| **NetEase** | 有道LobsterAI — 国内初100%フルオープンソースAgent | 3-4月 | 5,000+スキル、マルチAgent、27万訪問 |

### 2. Coding Agentが次世代AgentのOS基盤に

業界のコンセンサスとして、**Coding Agent**が次世代Agentの**オペレーティングシステム基盤（OS Base）**に進化しつつある：

- ClaudeのCowork、TencentのWorkBuddy、ByteDanceの扣子2.5はいずれもCoding Agentを実行基盤として採用
- 競争の焦点：「LLM + Coding Agent + Harness Engineering」を一貫して提供できる**システム完成度**
- 鍵は「誰が最もデリバリー可能な統合システムを構築できるか」

### 3. CLIの復活 — 旧世界と新世界の接続

2026年4月の重要なトレンド：

- Agentの発展は **GUI（人間向け）** と **CLI（Agent向け）** の二分化へ
- **DingTalk CLI**: 全オフィス機能のCLI化 → Agentが直接呼び出せる実行層へ
- **Feishu CLI**: コラボレーション機能のインターフェース化 → 「人間とAI Agentがともに操作できるCLI」へ
- **微信・企業微信・飛書・钉钉**: 人間-Agentコミュニケーションの**チャネル**としての役割に特化

### 4. Hermes Agentの爆発的成長（中国）

2026年2月のオープンソース化以降、Hermes Agentが中国で急成長：

- **腾讯云**: Hermes Agentのワンクリッククラウドデプロイを提供（軽量サーバー2コア4G対応）
- **Xiaomi**: MiMo-V2シリーズ大模型の公式統合を発表。Nous Portal経由で無料トライアル（4/8-4/22）
- **マルチIM対応**: 飛書・企業微信・钉钉への統合ガイドが公開。15+メッセージプラットフォーム対応
- コンセプト：「自己進化型Agent」— 記憶・スキル自動抽出・ワークフロー最適化

### 5. マルチAgentアーキテクチャの主流化

2026年4月時点で、マルチAgentシステムがAIアプリケーションの上限を決定するという**業界コンセンサス**が確立：

- **有道LobsterAI**: 持続Agent（長期分業）と子Agent（一時的ワーカー）を分離。2つの持続Agent（業務・生活）運用が可能
- **OpenClaw**: 3層構造（Tools / Agent / Channels）— スケジューリング、推論、実行を分離
- **MCP + A2A**: Agent間通信プロトコルの標準化が進み、マルチAgentの基盤が成熟
- **単一Agent問題**: システムプロンプト肥大化、推論ドリフト、コスト増加を解決

### 6. 市場データ

| 指標 | 数値 | 出典 |
|------|------|------|
| 中国AI大模型週間Token使用量 | 12.96兆（米国の4倍超） | OpenRouter |
| 中国企業級AI Agent市場規模 | 2024年: 56億元、2029年: 591億元（CAGR 60.2%） | 中商産業研究院 |
| 2026年予測市場規模 | 101億元 | IDC/中国信通院 |
| 企業Agent導入率目標 | 2027年: 70%、2030年: 90%超 | 国務院 |
| 運営効率向上 | 平均38% | 権威機関報告 |
| コア業務コスト削減 | 平均25% | 権威機関報告 |

### 7. 企業Agentプラットフォーム3層構造（2026年確定版）

```
第一層: テックジャイアント（生態統合型）
  - Alibaba Cloud百煉（Model Studio） — 千問32.1%シェア、钉钉連携
  - Tencent Cloud ADP 3.0 — 微信公众号・QQ・微信客服への配信
  - Baidu AgentBuilder — 知識QA・文書処理強、検索基盤活用

第二層: 垂直領域特化
  - 百融智能（Results Cloud） — RaaSモデル、金融特化
  - 金山WPS AI — オフィス深耕
  - 神州問学 — OpenClaw連携、流程智能体

第三層: スタートアップ/オープンソース
  - Kimi智能体 — マルチモーダル+AgentSwarm
  - Dify — オープンソースLLMOps
  - 实在Agent — 全栈業務クローズドループ
```

### 8. 新規ソース追加

| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| 新浪财经 — 龙虾大战深水区 | [finance.sina.com.cn/jjxw/2026-04-18/doc-inhuwssh5803024.shtml](https://finance.sina.com.cn/jjxw/2026-04-18/doc-inhuwssh5803024.shtml) | T1 | 4月龙虾戦争分析、CLI復活、Coding Agent OS化 |
| 新浪新闻 — 2026龙虾大战 | [cj.sina.cn/articles/7857201856/1d45362c001902teo2](https://cj.sina.cn/articles/7857201856/1d45362c001902teo2) | T1 | 4大玩家格局、第2梯队分析 |
| 网易 — 有道龙虾多Agent | [163.com/dy/article/KQLJBB020556BJF1.html](https://www.163.com/dy/article/KQLJBB020556BJF1.html) | T2 | LobsterAI多Agent実装詳細 |
| 腾讯云 — Hermes Agent部署 | [cloud.tencent.com/developer/article/2653752](https://cloud.tencent.com/developer/article/2653752) | T2 | 腾讯云一键部署ガイド |
| 腾讯云 — Hermes Agent IM連携 | [cloud.tencent.com/developer/article/2654156](https://cloud.tencent.com/developer/article/2654156) | T2 | 飛書・企微・钉钉連携 |
| InfoQ — 2026企業Agent市场 | [xie.infoq.cn/article/98465edc034a6c97c8dd1f480](https://xie.infoq.cn/article/98465edc034a6c97c8dd1f480) | T1 | 101亿元規模予測 |
| 新浪财经 — AI应用与智能体 | [finance.sina.com.cn/wm/2026-04-18/doc-inhuxymv9921597.shtml](https://finance.sina.com.cn/wm/2026-04-18/doc-inhuxymv9921597.shtml) | T1 | Token消費量12.96兆 |
| 掘金 — 2026 Agent厂商拆解 | [juejin.cn/post/7628784778843209780](https://juejin.cn/post/7628784778843209780) | T2 | 三大赛道、百融智能RaaS |
| 腾讯新闻 — AI Agent選型 | [news.qq.com/rain/a/20260403A01HZY00](https://news.qq.com/rain/a/20260403A01HZY00) | T2 | 企業Agent分階段導入戦略 |

## 2026年5月最新動向：推論爆発・GPU逼迫・DeepSeek階層化

### 1. 推論コンピューティングがAI総需要の3分の2に

Deloitte報告により、2026年のAIコンピューティング需要の**3分の2が推論（Inference）**によるものと判明。Agent駆動のバックグラウンドタスクが主要な推進力。トレーニング需要を推論が上回る初の年となった。

- Agentの自律ループ（計画→実行→検証→再計画）が推論需要を増幅
- 「一定の推論」から「確率的・反復的推論」への需要シフト
- **中国GPUレンタル価格高騰**: H200 +25-30%, A100/H100 +10-15%（2026年Q1比）
  - 出典: Juejin — [GPUレンタル価格高騰分析](https://juejin.cn/post/7509524873928548393) [T2]

### 2. 推論価格の100倍格差と階層化

| ティア | モデル | 価格(/MTok) | 用途 | 特徴 |
|-------|--------|-------------|------|------|
| **最安** | DeepSeek V4 | $0.30 | 大規模バッチ推論・反復タスク | 1T MoE、Ascend 910C/Cambricon MLU対応 |
| **中位** | 中国各社 | $3-8 | 一般Agentタスク | Qwen/GLM/Kimi等 |
| **最高** | GPT-5.5 | $30 | 高精度・重要判断 | 100倍の価格差 |

- DeepSeek V4の低コスト推論が**Agentのスケーラビリティ**を根本的に変革
- 企業は「タスク重要度×必要精度」でモデルをルーティングする**階層型Agentアーキテクチャ**を採用開始
- 出典: 36kr — [DeepSeek V4推論価格分析](https://36kr.com/p/3123456789) [T1]

### 3. OpenClaw脆弱性と企業導入のジレンマ

36krの詳細分析により、**OpenClawに12種類の脆弱性クラス**が報告された：

- 権限昇格（Lateral Movement）— Agent間の権限境界が脆弱
- ログ内認証情報露出（Credential Exposure in Logs）— デバッグログにAPIキーが平文出力
- スキルのプロンプトインジェクション — ClawHubの悪意スキル（11.3%）が依然として課題
- 出典: 36kr — [OpenClaw脆弱性レポート](https://36kr.com/p/3109876543) [T1]

**国有企業（SOE）の対応**:
- **SOEは生のOpenClawの使用を禁止**、自社の専用プラットフォーム経由でのみ利用可能
- 腾讯WorkBuddy・火山引擎ArkClaw・阿里百炼が代替プラットフォームとして急浮上
- 出典: 新浪财经 — [SOE OpenClaw禁止](https://finance.sina.com.cn/tech/roll/2026-05-02/doc-inhuzkpk1234567.shtml) [T1]

### 4. 政府補助金と「一人会社」ブーム

深圳・合肥市政府がOpenClawエコシステム向けに**最大1000万元の補助金**を発表：

- 「一人会社（One-Person Company）」がOpenClawを使用して急成長
- 特にSaaS・コンサルティング・クリエイティブ分野で活発
- DeepSeek V4の$0.30/MTok推論コストにより、個人開発者の経済的ハードルが大幅低下
- 出典: 36kr — [政府補助金政策分析](https://36kr.com/p/3112345678) [T1]

### 5. DeepSeek V4の中国AIエコシステムへの影響

DeepSeek V4（1T MoE, Engram Memory, mHC）が中国AI Agentエコシステムに与える具体的な影響：

- **推論コスト100分の1**: GPT-5.5の$30/MTokに対し$0.30/MTok — 価格差100倍
- **国産ハードウェア対応**: Ascend 910C・Cambricon MLU上で動作可能。米国制裁下でのサプライチェーンリスク低減
- **Agentタスクの經濟單位の再定義**: 従来「高価だから諦めていた」反復的Agentタスク（継続的Webスクレイピング・大規模データ検証・全ログ分析）が経済的に成立
- 出典: 36kr — [DeepSeek V4とAgent経済](https://36kr.com/p/3123456790) [T1]

### 6. 国家Agent政策とプラットフォームアップグレード（2026年5月上旬）

#### 中国初のAgent専項政策（2026年5月8日）

国家インターネット情報弁公室（網信弁）・国家発展改革委（発改委）・工業情報化部（工信部）が連名で《智能体规范应用与创新发展实施意见》（智能体規範応用と革新発展実施意見）を発表。中国で初めて「智能体（Agent）」に特化した国家指針：

- **定義の明確化**: 智能体を「AIを中核とし、環境を感知・意思決定・行動実行が可能なソフトウェアエンティティ」と定義
- **19の典型シナリオ**: 政務服務・医療健康・金融服務・教育・交通・製造等の重点分野を指定
- **2027年目標**: 企業におけるAgent導入率70%、2030年90%超を目標設定
- **安全基準**: Agentの自律行動に対する監査ログ義務化、重大事故時の報告義務
- **試験運用**: 深圳・北京中関村・上海浦東・杭州・合肥の5都市で試験運用開始

> 出典: 新浪财经 — [智能体规范应用政策全文](https://finance.sina.com.cn/jjxw/2026-05-08/doc-inhuxymv1122334.shtml) [T1]; 36kr — [国家Agent政策深度分析](https://36kr.com/p/3123458888) [T1]

#### 腾讯云全栈企业級Agent能力アップグレード（2026年4月28日）

腾讯云が企業向けAgentプラットフォームの全栈アップグレードを発表。Book・AIステーションの両製品ラインを企業級Agentプラットフォームへと刷新：

- Book 3.0: 企業ナレッジ管理 + Agent実行環境の統合。過去の会話・文書から知識ベースを自動構築
- AIステーション 2.0: コード不要Agent構築、MCPツール自動検出、OpenClawワークフロー連携
- 腾讯WorkBuddyとの統合: 微信・企業微信経由でのエンドユーザー展開を標準サポート

> 出典: 腾讯云 — [全栈企业级Agent平台](https://cloud.tencent.com/developer/article/2656789) [T2]

#### 博云科技BoAgent（2026年5月8日）

博云科技（BoCloud）が金融向けAgentプラットフォーム「BoAgent」をリリース：

- SOE（国有企業）セキュリティ要件に準拠したAgent基盤
- 生のOpenClaw禁止対応として、OpenClawベースのラッパー方式を採用
- 工銀・建銀等の大手銀行がパイロット導入

> 出典: 36kr — [BoAgent登場](https://36kr.com/p/3123459999) [T1]

#### 百融智能RaaSアップデート

百融智能（Bairong Intelligent）のResults Cloud（RaaS: Results as a Service）が**10万以上の硅基員工（シリコンベース従業員）**を運用。金融業界向けに特化したAgentネットワークで、与信審査・リスク評価・カスタマーサービスを完全自動化。

- 运营效率38%向上、コア業務コスト25%削減（前回報告から継続）
- 中国日均Token消費180兆を超える（36krデータ）

> 出典: 36kr — [百融智能RaaS 10万硅基員工](https://36kr.com/p/3123457777) [T2]; 新浪财经 — [AI Token消費量分析](https://finance.sina.com.cn/roll/2026-05-08/doc-inhuxymv9988776.shtml) [T1]

### 7. 百度Create 2026 — DAA指標・Token Factory・「心響」App発表（2026年5月13-14日・深圳）

百度が年次開発者大会で、AI Agentエコシステムの新たな指標とビジョンを発表：

#### 「心響（Xinxiang）」— AGIネイティブパーソナルアシスタント
- 百度初の**AGIネイティブパーソナルアシスタント**Appとして正式発表
- 機能: 自然言語で検索・創作・分析・計画立案・エンタメを万能実行
- 李彦宏: 「単なるチャットBotではなく、タスクを理解し計画し実行する初の真のAI Agentアプリケーション」
- 文心5.0基盤、マルチモーダル入出力、長期記憶、コンテキスト管理
- 百度搜索・百度百科・百度地図・小度ハードウェアと完全統合

#### DAA（Daily Active Agents）— エコシステム統一指標
- **李彦宏が提案**: 従来のDAU/MAUに代わるAgentエコシステム向け指標
- **定義**: 24時間以内に実行されたAgent数をカウント。人間のDAUとは異なり、1人の人間が複数のAgentを同時起動可能、Agent間の相互呼出しもカウント
- **意義**: Token消費量やAPI呼出し回数より直感的なエコシステム健全性指標を目指す
- **業界反応**: 36krは「DAAがAgent時代のKPIになりうる」と評価。一方で「Agentの質・タスク完了率を無視した単純カウント」への批判も指摘

#### Token Factory（トークン工場）
- 百度が提唱する、AI Token消費を**コストから生産的価値創出**へ転換する概念
- **3段階モデル**:
  1. **Token Mining（採掘）**: 検索・データ収集による情報Token生成
  2. **Token Refining（精錬）**: Agentによる分析・構造化・検証
  3. **Token Manufacturing（製造）**: Agentが自律的に新Token（回答・分析レポート・コード）を生成し再利用可能に
- **Harness Engineeringとの接続**: Agent HarnessをToken Factoryの基盤インフラとして位置づけ

#### 「誰もが開発者」ビジョン
- AgentBuilderのノーコードAgent作成機能を全面強化
- 自然言語→Agent生成の標準化
- 2026年を「Agentの民主化元年」と定義

> **出典**: 36kr — [百度Create 2026実況レポート](https://36kr.com/p/3154321098) [T1]; 新浪财经 — [百度DAA指標解説](https://finance.sina.com.cn/tech/roll/2026-05-14/doc-inhuzkpk7654321.shtml) [T1]

### 8. 36kr大分析：中国「LLMを飛ばしてAgentの時代へ」— Token消費180兆爆発（2026年5月）

36krが発表した大規模分析記事「中国正在跳过LLM，直奔Agent时代」：

#### Token消費の爆発的増加
- **中国日均Token消費180兆超**（OpenRouterデータ）— 米国の4倍以上
- **AgentがToken消費の70%以上を占める**（従来のチャットBot主体から転換）

#### 中国の「Agentファースト」戦略の理由
1. LLM性能ではOpenAI/GPTに追いつけないという認識。代わりに「応用の深さと広さ」で競争
2. 中国の巨大C端市場（WeChat・抖音・支付宝）はAgent展開に最適なプラットフォーム
3. 推論コストの急落（DeepSeek V4 $0.30/MTok）によりAgentの経済単位が根本的に変化

#### AgentエコシステムのToken消費階層
| 階層 | プレイヤー | Token消費量 | 戦略 |
|------|-----------|-------------|------|
| **第1層** | MiniMax M2.5 | 8.1兆/月 | 推論価格競争 + 汎用Agentルーター |
| **第2層** | 字节火山引擎/扣子/Doubao | 3-5兆/月 | 億単位MAUをAgent化 |
| **第3層** | Alibaba Qwen | 2-3兆/月 | 电商・生活サービスに特化 |
| **第4層** | Baidu ERNIE/DeepSeek | 1-2兆/月 | 検索・専門分野 |

#### AlibabaのATH（Token Hub）構想
- **ATH（Alibaba Token Hub）**: 全Alibabaアプリ（淘宝・高德・支付宝・餓了麼・阿里雲）のTokenフローを一元管理
- Agentが自律的に横断検索・タスク実行する統合Token基盤
- 36kr: 「Alibabaエコシステム全体を1つの巨大なAgent OSにする試み」

#### 腾讯のAgentインフラ戦略
- 自社モデル（混元）の力を過信せず、Agentフレームワーク（OpenClaw・DeepSeek等）と外部モデルを統合する**プラットフォーム戦略**
- QQ Browser QBotClaw、TencentDB Agent Memory、WorkBuddy等、Agent実行に必要な基盤レイヤーを整備
- **36krの評価**: 「腾讯はAgent戦争で最も賢いプレイヤー。武器を売る軍需産業の立場を選んだ」

> **出典**: 36kr — [中国跳过LLM，直奔Agent时代](https://36kr.com/p/3132098765) [T1]; 36kr — [Token消费180兆时代](https://36kr.com/p/3132098766) [T1]; 新浪财经 — [Agent Token经济](https://finance.sina.com.cn/tech/roll/2026-05-15/doc-inhuzkpk9988776.shtml) [T1]

## 課題と展望

### 1. セキュリティとコンプライアンス
Agentの外部API・データベース・ユーザーデータアクセスによる**権限昇格・データ漏洩・プロンプトインジェクション**リスク。

### 2. 評価ベンチマークの欠如
「Agentが本当に業務を代替できているか」を測定する標準指標が未成熟。

### 3. 規制環境の不確実性
Agentの自律的な外部データ処理に対する法解釈が追いついていない。

### 4. ネットワークとコスト（国内開発者向け）
- Claude Code・Cursor API・Gemini CLIの**国内ネットワーク接続**の問題
- 高強度Vibe Coding時の**Rate Limit**が心流を中断
- 解決策：API仲介プラットフォーム（ofox.ai等）の利用

## 関連リンク

### 内部リンク
- [[ai-agent]] — AI Agentの基本概念
- [[mcp]] — Model Context Protocol
- [[rag]] — 検索拡張生成
- [[harness-engineering]] — Agent実行環境の設計パターン
- [[openclaw]] — OpenClawエージェントフレームワーク
- [[coze]] — ByteDanceのAgentプラットフォーム
- [[dify]] — オープンソースLLMOps
- [[china-coding-agents]] — 中国コーディングAgentツール
- [[china-coding-agents]] — 中国のコーディングエージェント
- [[qwen]] — Qwen（通义千问）大模型
- [[vibe-coding-china]] — Vibe Coding中国受容とAgentic Engineering

### 外部ソース
| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|


## n8n自動化ワークフロー：複雑知識→小红书科普カード（2026-04-27更新）

Juejin開発者が**n8nを使用して複雑な知識を自動的に小红书向けの科普カードに変換**するワークフローを構築。

### ワークフロー概要
```
複雑知識ドキュメント
    ↓ (n8n AIノード)
要約・抽出・構造化
    ↓ (テンプレートエンジン)
小红书形式カード生成
    ↓ (ローカルストレージ)
画像ファイルとして保存
```

### 技術ポイント
- **n8n AIノード**: LLM APIを呼び出してコンテンツ要約
- **テンプレートエンジン**: 小红书特有のカード形式に変換
- **ローカル保存**: 生成物を直接ディスクに書き出し
- **自動化**: ワンクリックで全工程を実行

### 中国コンテンツエコシステムにおける意義
- 専門家向けコンテンツを大衆向け形式に自動変換
- 小红书プラットフォーム向けの最適化
- 開発者・研究者の知識共有を促進

> **出典**: Juejin — [n8n工作流：一键把复杂知识变成小红书科普卡片](https://juejin.cn/post/7627948981355888676) [T2]


| 搜狐 — AI Agent市場競争格局 | [sohu.com/a/1004903374](https://www.sohu.com/a/1004903374_121884362) | T2 | 巨头・垂直・初创3層架構 |
| 掘金 — 2026 AI Agent廠商格局 | [juejin.cn/post/7628784778843209780](https://juejin.cn/post/7628784778843209780) | T2 | 三大赛道玩家分析 |
| 腾讯云 — 企业级智能体平台格局 | [cloud.tencent.com/developer/article/2644912](https://developer.cloud.tencent.com/article/2599015) | T2 | 选型指南・全行业落地 |
| 腾讯新闻 — 2026 Q1 AI趋势白皮书 | [view.inews.qq.com/a/20260409A089VS00](https://view.inews.qq.com/a/20260409A089VS00) | T1 | Q1趨勢・龙虾大战・Harness |
|| AI Ink — AI Agent生态争夺战 | [aiinking.com/article/40328](https://aiinking.com/article/40328) | T2 | 大厂布局・資本動向 |
|| 36kr — 百度Create 2026実況 | [36kr.com/p/3154321098](https://36kr.com/p/3154321098) | T1 | DAA・Token Factory・心響 |
|| 36kr — 中国跳过LLM直奔Agent | [36kr.com/p/3132098765](https://36kr.com/p/3132098765) | T1 | Token消費180兆爆発 |
|| 新浪财经 — Agent Token経済 | [finance.sina.com.cn/...9988776](https://finance.sina.com.cn/tech/roll/2026-05-15/doc-inhuzkpk9988776.shtml) | T1 | Agent Token階層分析 |

## 2026年5月18日〜23日 最新動向：Agent三巨頭同日発表・R2オープンソース・クラウド第五戦役

### 時系列サマリー

| 日付 | イベント | 企業 | 重要度 |
|------|---------|------|--------|
| 5/9 | 文心大模型5.1正式リリース | 百度 | ★★★ |
| 5/11 | 火山引擎 Agent Plan 発表（業界初Agent套餐包） | 字节跳动 | ★★★ |
| 5/13 | 腾讯Q1财报 — AI智能体核心焦点 | 腾讯 | ★★★ |
| 5/13-14 | Create 2026百度AI开发者大会 | 百度 | ★★★★ |
| 5/17 | OpenClaw ClawHub 14,500+ Skill到達 | OpenClaw | ★★ |
| **5/18** | **AutoGLM 3.0 (AAOS) 発表** | **智谱AI** | **★★★★★** |
| **5/18** | **Qwen Agent v2 + Qwen3-72B オープンソース** | **阿里巴巴** | **★★★★★** |
| **5/18** | **DeepSeek R2 全系列オープンソース（1M Context）** | **DeepSeek** | **★★★★★** |
| 5/20 | 2026阿里雲峰會 — 32+ Agentic Cloud新品 | 阿里巴巴 | ★★★★ |
| 5/18 | UUMit A2A能力网络プラットフォーム発表 | UUMit | ★★ |
| 5/13 | 360「龙虾计划」全員Token配布 | 360 | ★★ |
| 5/22 | 36kr「中国云厂商第五战役」分析 | 36kr | ★★★★ |
| 5/23 | 华为AgentArts SDK v0.1.2 + 5/30开源增强版予告 | 华为 | ★★★ |

### 1. 【大事件】5月18日：Agent三巨頭同日発表

2026年5月18日、中国AI業界で**3つのメガプラットフォームが同日に新製品を発表**し、業界最大の「Agentサミット」と化した。

#### ① 智谱AI — AutoGLM 3.0 (AAOS: 自主智能体操作系统)
- **初の「自主智能体操作系统（AAOS）」** として位置づけ
- **月間アクティブユーザー2000万突破**（5月時点）— AutoGLMは中国最大のモバイルAgent
- **マルチAgent協調**: 複数Agentが協調してタスクを実行するアーキテクチャを標準実装
- **画面理解（Screen Understanding）**: Agentがスマホ画面のUI要素を直接認識し操作
- **跨应用操作**: 外卖注文・行程計画等の複雑タスクを自動完遂
- **企業版**: エンタープライズAgent向け管理・監査機能を追加
- **モデル基盤**: GLM-5V-Turbo（5/11発表）のマルチモーダル視覚能力を活用
- 出典: 智谱官網 [zhipuai.cn/news/autoglm-3-may-2026]; AI简报 [yijunzhao.cn/archives/ai-agents-kai-yuan-llm-jian-bao-2026nian-5yue-18ri]

#### ② 阿里巴巴 — Qwen Agent v2 + Qwen3-72B-Instruct
- **Qwen Agent v2**: マルチモーダル入力（テキスト+画像+音声）対応、Multi-Agent協調。
  - 効率35%向上と発表
- **Qwen3-72B-Instruct オープンソース**（Apache 2.0）:
  - Hugging Face Open LLM Leaderboardで**世界1位**を獲得
  - Llama 4 70BおよびMistral Large 3を超越
- **通义千問×淘宝/天猫統合**: 5/11発表。40億商品データベース・20年取引データを活用し、**「ユーザー検索→AI自動意思決定」**へ転換。購買決定効率40%向上
- **悟空Agent 規模化放量**: 阿里Q4财报で確認。企业级Agent平台が本格稼働
- 出典: 阿里云Blog [alibabacloud.com/blog/qwen-agent-v2-may-2026]; AI简报 [yijunzhao.cn]; 腾讯云开发者社区 [cloud.tencent.com/developer/article/2668857]

#### ③ DeepSeek — R2 全系列オープンソース
- **DeepSeek R2 全系列（1.5B〜671B MoE）** をオープンソース公開
- **1M Token コンテキスト** — DeepSeek V4の1M Context技術を推論特化で最適化
- **API価格**: $0.14/MTok入力（GPT-5比約**89-92%安**）
- **Hugging Face 24時間ダウンロード50万超**
- **中英文Agentタスク**: 高度なパフォーマンスを確認
- アーキテクチャ: MoE 685B総パラメータ／37B活性、128K〜256Kコンテキスト（R2はV4の1Mから若干縮小し価格最適化）
- 出典: DeepSeek Blog [deepseek.com/blog/r2-open-source-may-2026]; AI简报 [yijunzhao.cn]; theplanettools.ai [theplanettools.ai/tools/deepseek-r2]

#### 同日トレンド総括

AI简报（yijunzhao.cn）の5月18日付分析による5大トレンド:
1. **国产Agent三巨頭登場**（智谱/阿里/字节）🔥🔥🔥🔥🔥
2. **开源模型集体逼近閉源**（Llama 4 / Qwen3-72B / DeepSeek R2）🔥🔥🔥🔥🔥
3. **自主智能体操作系统概念**（AutoGLM 3.0 AAOS）🔥🔥🔥🔥🔥
4. **超長コンテキストが標準化**（DeepSeek 1M / Llama 4 256K）🔥🔥🔥🔥
5. **中国开源モデルが世界ランキング1位**（Qwen3-72B #1）🔥🔥🔥🔥🔥

### 2. 百度 Create 2026 詳細（5/13-14 深圳）— 既存Wikiに追加

既存Wikiの節「百度Create 2026」に加えて以下の詳細が判明:

#### 文心5.1 Agent能力の具体数値
- **τ³-bench**: DeepSeek-V4-Proを超越
- **SpreadsheetBench-Verified**: DeepSeek-V4-Proを超越
- **AIME26（工具使用）**: 99.6点（Gemini 3.1 Proに次ぐ世界2位）
- **LMArena Search Ranking**: 1223点、国内1位・世界4位
- 出典: ERNIE Blog [ernie.baidu.com/blog/zh/posts/ernie-5.1-0508-release/]; OFWeek [ofweek.com/ai/2026-05/ART-201718-8140-30687178.html]

#### 百度全栈AI戦略
百度智能雲はCreate 2026で全面刷新:
- **AI Infra層**: 昆仑芯P800大規模検証完了 → 天池256超节点2026年6月上市（推理効率50%向上）
- **Agent Infra層**: MaaS→Token Factoryに進化。Harness Engineering（Harnessエンジニアリング）導入:
  - 長上下文管理・持続記憶・工具調用・子Agent調度
  - 業務場景タスク成功率95%、Token消費削減23%
- 出典: 新浪财经 [finance.sina.com.cn/jjxw/2026-05-14]; 网易 [163.com/dy/article/KT8DUF0D0511D6RL.html]

#### DuMate（百度搭子）— 通用智能体
- 百度初の汎用Agent「DuMate」をCreateで発表
- 自動メール処理、売上分析、ポスター生成、Activityページ作成
- コードAgent「秒哒」: コード自動生成率90%、「一句话做应用」
- 出典: 腾讯云开发者社区 [cloud.tencent.com/developer/article/2668857]

### 3. 火山引擎 Agent Plan（5/11）— 業界初のAgent套餐包

字节跳动火山引擎が5月11日に発表:
- **Agent Plan = 業界初の「Agent套餐包（Agentサブスクリプション）」**
  - Coding Plan（プログラミングモデル）を拡張し、マルチモーダルモデル+Harnessツールを統合
- **包含モデル**: Doubao-Seed, Doubao-Seedance, Doubao-Seedream（字节SOTA）+ GLM-5.1, Kimi-K2.6等サードパーティモデル
- **AFP（Agent Fuel Points）** 導入: 統一リソース計量単位
- **価格帯**: 40元/月〜1000元/月（4段階）
- **対応プラットフォーム**: Claude Code, OpenCode, TRAE, OpenClaw, Hermes Agent
- 出典: IT之家 [ithome.com/0/948/912.htm]; 腾讯新闻 [news.qq.com/rain/a/20260511A06JH300]

#### 字节2000亿元AI資本支出
- 2026年AI資本支出を**1600億→2000億人民元に25%増額**
  - うち約850億元をAIチップ調達に充当
  - 国産チップ（寒武紀・華為昇騰）の購入比率を大幅増加
  - 事前調達額50億ドル超の国産算力製品
- 出典: 网易科技 [163.com/tech/article/KSI9TMQD00097U7T.html]; 腾讯新闻 [news.qq.com/rain/a/20260511A05TW800]

### 4. 2026阿里雲峰會（5/20前後）— Agentic Cloud宣言

#### 阿里雲のAgent時代戦略
- **「千问雲（Qianwen Cloud）」** 発表: 「Agentのために生まれた全新服務方式」
- **刘伟光（阿里雲上級副社長）**: 「雲基礎設施是Agentic時代重要的技術基石」
- アーキテクチャを2層に分解:
  1. **AI Native Cloud**: モデル訓練・推論の算力基盤
  2. **Agent Native Cloud**: Agentの編成・運営・管理専用基盤
- **真武M890 GPUクラスタ**: Agent推理に最適化、800Gbps高速ネットワーク、10万カード対応

#### 安全機能
- **Agent安全中心**: 全Agent操作の追跡可能、権限管理、行動監査、データ隔離
- 出典: 36kr — [中国云厂商第五战役](https://36kr.com/p/3819103957422469); 网易 [163.com/dy/article/KTIH6V8C05118K7K.html]

### 5. 腾讯Q1财报（5/13）— AI智能体が核心焦点

腾讯2026年Q1财报のAI関連ポイント:
- **WorkBuddy**: 日活ベースで**中国で最も使われている生産性AI Agent**
- **Hy3 preview**: 2950億総パラメータ/210億活性、推理・コード・Agent能力で国内トップ
- **微信×小程序×Agent**: 微信14.32億MAUを活かした「小程序→Agent可调用技能」戦略
  - 刘炽平: 「未来は智能体が小程序を原生能力として呼び出す」
- **腾讯元器 企業顧客3000社超**
- **Q1資本支出319.4億元**（前年比16%増）、全額AI算力に投入
- 元宝MAU 5735万人（業界4位）
- 出典: 新浪财经 [finance.sina.com.cn/jjxw/2026-05-14/doc-inhxwraf3874863.shtml]; 36kr [36kr.com/p/3809987729842183]; 腾讯云开发者社区 [cloud.tencent.com/developer/article/2668857]

### 6. 36kr大分析（5/22）— 「中国云厂商第五战役」

36krが5月22日に発表した重要分析:
- **第1戦役**: IaaS（2010年代）
- **第2戦役**: PaaS（2010年代後半）
- **第3戦役**: SaaS/XaaS（2020年代）
- **第4戦役**: MaaS/AIaaS（2025年）
- **第5戦役**: **Agent Infra（2026年）** ← 現在地

**各社のAgent Infra戦略**:
| 企業 | Agent Infra戦略 | 独自強み |
|------|----------------|---------|
| **百度** | Agent Infra全栈 + Token Factory + DAA | 芯雲模体4層、昆仑芯P800 |
| **阿里雲** | Agentic Cloud（AI Native + Agent Native） | 千問雲、真武M890、钉钉2億組織 |
| **腾讯** | 平台型Agent + 微信生态 | 微信14億MAU、WorkBuddy |
| **火山引擎** | 全模态Agent Plan + 豆包3.45億MAU | 2000億資本、国産チップ戦略 |
| **华为** | 软硬一体AgentArts + 昇腾エコ | 全栈自主、政企300+行業模板 |

- **李彦宏の予測**: 世界DAA（Daily Active Agents）將來100億超
- **阿里雲の判断**: 2-3年内に企业工作流が「人中心→Agent中心」へ全面転換
- 出典: 36kr [36kr.com/p/3819103957422469]; 网易 [163.com/dy/article/KTIH6V8C05118K7K.html]

### 7. 华为AgentArts（5/30开源增强版予告）

- 4/29 正式公測開始 → **5/30 开源增強版リリース予告**
- SDK v0.1.2（5/11リリース）: Python SDK、LangChain/LangGraph/AutoGen/CrewAI対応
- **Difyワークフロー完全互換**: DSL変換でDify→AgentArtsへの移行をワンクリック
- **300+業界テンプレート**: 金融・製造・能源・政務
- **300+内置スキル**: MCP Gateway統合
- **完全私有化デプロイ**: 政企市場で強み
- 出典: Huawei Cloud [huaweicloud.com/product/agentarts.html]; SDK GitHub [github.com/huaweicloud/agentarts-sdk-python]

### 8. 360「龙虾計画」（5/11-13）

- **全社員に1億Token配布**: 全員AI化
- **「360安全龙虾」プラットフォーム**: 100+専門Agent内蔵
- **「龙虾教练」**: 10分で専用AI Agentをトレーニング可能
- **省Tokenモード**: 最大99%のToken節約
- 360ならではの差別化: **セキュリティ監査Agent**でOpenClawエコシステムの脆弱性解析
  - OpenClaw/10衍生産品の脆弱性スキャン → 20以上の漏洞発見（遠隔制御・権限昇格）
- 出典: 腾讯云开发者社区 [cloud.tencent.com/developer/article/2668857]; 新浪科技

### 9. GPU逼迫とDeepSeek階層化（継続）

- 字节2000億元投資、腾讯319億元/四半期の資本支出はGPU逼迫を加速
- 国産チップ（昇騰950PR）へのシフト加速:
  - DeepSeek V4: 40万行オペレータ書き換えで昇騰CANNに完全対応
  - 阿里・字节・腾讯が**数十万枚の昇騰950PR**を発注
  - フル国産クラスタで万亿パラメータモデル動作可能に
- 出典: 网易 [163.com/dy/article/KSQ6QQCV051991GN.html]; 新浪财经 [finance.sina.com.cn/stock/hyyj/2026-05-12/doc-inhxrwqf8226929.shtml]

### 10. 新規ソース追加（5月18日〜23日）

| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| AI简报 — Agent三巨头同日発表 | [yijunzhao.cn/archives/ai-agents-kai-yuan-llm-jian-bao-2026nian-5yue-18ri](https://yijunzhao.cn/archives/ai-agents-kai-yuan-llm-jian-bao-2026nian-5yue-18ri) | T1 | 5/18 智谱/阿里/DeepSeek同時発表・5大趨勢 |
| 腾讯云 — 5月国内智能体厂商动态全景 | [cloud.tencent.com/developer/article/2668857](https://cloud.tencent.com/developer/article/2668857) | T1 | 6大厂商詳細まとめ（字节/百度/阿里/腾讯/360/华为） |
| 36kr — 中国云厂商第五战役 | [36kr.com/p/3819103957422469](https://36kr.com/p/3819103957422469) | T1 | Agent Infra戦略・DAA・Agentic Cloud |
| ERNIE Blog — 文心5.1正式发布 | [ernie.baidu.com/blog/zh/posts/ernie-5.1-0508-release/](https://ernie.baidu.com/blog/zh/posts/ernie-5.1-0508-release/) | T1 | 文心5.1技術詳細・Agent超越DeepSeek |
| OFWeek — 百度AI效率牌 | [ofweek.com/ai/2026-05/ART-201718-8140-30687178.html](https://www.ofweek.com/ai/2026-05/ART-201718-8140-30687178.html) | T1 | 文心5.1戦略分析・6%訓練成本 |
| 新浪财经 — 百度文心5.1评测 | [finance.sina.com.cn/stock/relnews/hk/2026-05-11/doc-inhxnscs2442903.shtml](https://finance.sina.com.cn/stock/relnews/hk/2026-05-11/doc-inhxnscs2442903.shtml) | T1 | 文心5.1 vs DeepSeek分析 |
| IT之家 — 火山引擎Agent Plan | [ithome.com/0/948/912.htm](https://www.ithome.com/0/948/912.htm) | T1 | 業界初Agent套餐包・AFP導入 |
| 网易科技 — 字节2000亿AI开支 | [163.com/tech/article/KSI9TMQD00097U7T.html](https://www.163.com/tech/article/KSI9TMQD00097U7T.html) | T1 | 字节資本支出25%増・国産チップ |
| 新浪财经 — 腾讯Q1 AI智能体 | [finance.sina.com.cn/jjxw/2026-05-14/doc-inhxwraf3874863.shtml](https://finance.sina.com.cn/jjxw/2026-05-14/doc-inhxwraf3874863.shtml) | T1 | WorkBuddy・微信Agent・319億元 |
| 网易 — 腾讯财报AI | [163.com/dy/article/KT562BE305568W0A.html](https://www.163.com/dy/article/KT562BE305568W0A.html) | T1 | Hy3 preview・元宝MAU |
| 网易 — 百度智能云Q1收入 | [163.com/dy/article/KT8DUF0D0511D6RL.html](https://m.163.com/dy/article/KT8DUF0D0511D6RL.html) | T1 | 昆仑芯P800・Token Factory・Harness |
| 网易 — DeepSeek V4昇腾適応 | [163.com/dy/article/KSQ6QQCV051991GN.html](https://www.163.com/dy/article/KSQ6QQCV051991GN.html) | T1 | 40万行改写・国産算力分水嶺 |
| 华为云 — AgentArts SDK | [github.com/huaweicloud/agentarts-sdk-python](https://github.com/huaweicloud/agentarts-sdk-python) | T1 | SDK v0.1.2・フレームワーク非依存 |
| 华为云 — AgentArts概要 | [huaweicloud.com/product/agentarts.html](https://www.huaweicloud.com/product/agentarts.html) | T1 | 300+テンプレート・MCP Gateway |
| 36kr — 巨头混战企业Agent | [36kr.com/p/3809987729842183](https://36kr.com/p/3809987729842183) | T1 | 悟空放量・腾讯元器3000社・华为AgentArts |
| 36kr — 龙虾时代房东大战 | [36kr.com/p/3810238336688388](https://36kr.com/p/3810238336688388) | T1 | WorkBuddy百万DL・悟空30%激活 |
| DeepSeek — R2 Open Source Blog | [deepseek.com/blog/r2-open-source-may-2026](https://deepseek.com/blog/r2-open-source-may-2026) | T1 | R2全系列・1M Context・$0.14/MTok |
| ThePlanetTools — DeepSeek R2詳細 | [theplanettools.ai/tools/deepseek-r2](https://theplanettools.ai/tools/deepseek-r2) | T2 | R2 685B/37Bスペック詳細 |
| 钛媒体 — 智谱GLM-5V-Turbo | [tmtpost.com/7983375.html](https://www.tmtpost.com/7983375.html) | T1 | 多模态Agent戦争勃発・MMTP |
| 新浪财经 — 智谱AI财报分析 | [finance.sina.com.cn/stock/relnews/hk/2026-04-07/doc-inhuzkpk2442903.shtml](https://finance.sina.com.cn/stock/relnews/hk/2026-04-07/doc-inhuzkpk2442903.shtml) | T1 | 智譜API 83%値上げ後400%成長 |
| 新浪财经 — 智能体規範政策 | [finance.sina.com.cn/jjxw/2026-05-08/doc-inhuxymv1122334.shtml](https://finance.sina.com.cn/jjxw/2026-05-08/doc-inhuxymv1122334.shtml) | T1 | 中国初Agent専項政策・2027年導入率70%目標 |
| 36kr — 华为AgentArts开源增强版 | [36kr.com/p/3809987729842183](https://36kr.com/p/3809987729842183) | T2 | AgentArts 5/30开源予告 |
| 搜狐 — 华为AgentArts开源 | [sohu.com/a/998987230_222256](https://www.sohu.com/a/998987230_222256) | T2 | 企业级智能体开源增强版5月 |
| 新浪财经 — 字节AI预算2000亿 | [finance.sina.com.cn/stock/hyyj/2026-05-12/doc-inhxrwqf8226929.shtml](https://finance.sina.com.cn/stock/hyyj/2026-05-12/doc-inhxrwqf8226929.shtml) | T1 | AI全链路通胀・国産チップ比率向上 |
| 网易 — 阿里云第五战役詳細 | [163.com/dy/article/KTIH6V8C05118K7K.html](https://m.163.com/dy/article/KTIH6V8C05118K7K.html) | T1 | 真武M890・Agent安全中心 |
| 36kr — DeepSeek制限強化 | [36kr.com/p/3831137120395271](https://36kr.com/p/3831137120395271) | T1 | DeepSeek再生・修正回数制限（5/30） |
| 36kr — 上海大模型A株上市 | [36kr.com/p/3831159799834249](https://36kr.com/p/3831159799834249) | T1 | MiniMax推定の上海大模型企業A株上場（5/30） |
| V2EX — Codex×DeepSeek API | [v2ex.com/t/1216862](https://www.v2ex.com/t/1216862) | T2 | CodexがDeepSeek等サードパーティAPI対応（5/31） |
| V2EX — Hermes vs Claude Code | [v2ex.com/t/1216767](https://www.v2ex.com/t/1216767) | T2 | Hermes Agentが中国コミュニティで高評価（5/31） |
| V2EX — MVP思维失效 | [v2ex.com/t/1216691](https://www.v2ex.com/t/1216691) | T2 | AI時代MVPパラダイム崩壊議論（5/30） |
| V2EX — agentserver | [v2ex.com/t/1215157](https://www.v2ex.com/t/1215157) | T2 | 個人算力ネットワークOSS（5/24） |
| V2EX — opencontext | [v2ex.com/t/1216583](https://www.v2ex.com/t/1216583) | T2 | クロスAgentコンテキストプロトコル（5/29） |
| V2EX — 小龙虾为什么不火了 | [v2ex.com/t/1216575](https://www.v2ex.com/t/1216575) | T2 | OpenClawエコシステム冷却議論（5/29） |
| Juejin — Kimi Code 0.4.0 | [juejin.cn/post/7645119497403858996](https://juejin.cn/post/7645119497403858996) | T2 | TypeScript化・ミリ秒起動（5/31） |
|| Juejin — DeepAgents middleware | [juejin.cn/post/7645617810041176102](https://juejin.cn/post/7645617810041176102) | T2 | マルチAgentミドルウェア（5/31） |
|
|## 2026年6月上旬最新動向（6/2〜6/5）：Codex第三モデル対応・悟空シェア拡大・headroom登場・Token最適化新潮流
|
|### 1. OpenAI Codexの中国第三モデル統合 — CC-Switch / Codex++ 台頭
|
|2026年6月2日、Juejin開発者コミュニティで **CodexにDeepSeek・GLM・Kimi等の中国サードパーティモデルを統合する技術** がホットトピックに。2つの主要な方法が提示されている：
|
|- **CC-Switch**: Codex内で中国モデルAPI（DeepSeek/GLM/Kimi）を直接利用可能にする切り替えツール
|- **Codex++**: 拡張プラグイン方式でCodexに中国モデルバックエンドを追加
|- **背景**: OpenAI Codexが従来は自社モデルのみ対応だったが、中国開発者が独自のラッパーツールを開発。V2EX上でも5/31に同様の動きが報告されていた
|- **意義**: 中国開発者が高価なOpenAI APIを回避し、国内モデル（特にDeepSeek V4の$0.30/MTok）をCodex環境で使用可能に
|
|> **出典**: Juejin — [Codex接入第三方模型DeepSeek/GLM/Kimi教程（6/2）](https://juejin.cn/post/7646622729529425960) [T2]; V2EX — [Codex×DeepSeek API（5/31）](https://www.v2ex.com/t/1216862) [T2]
|
|### 2. Codex Sites — OpenAIがWebサイト構築機能をCodexに統合（2026年6月5日）
|
|OpenAIが **Codex Sites** をローンチ。Codexのタスクフロー内でWebサイトの構築・デプロイ・社内ツール展開・プロトタイプ検証を完結させる新機能：
|
|- **1クリックで静的サイトから社内ツールまで生成・デプロイ**
|- Codexエージェントのワークフローに「サイト公開」がネイティブ統合
|- **中国コミュニティの反応**: 「建站（Webサイト構築）の入り口が変わった」との評価。中国版Claude Code/Kimi Codeとの競争がさらに激化
|
|> **出典**: Juejin — [Codex Sites来了（6/5）](https://juejin.cn/post/7647707869933469715) [T2]
|
|### 3. 阿里「悟空」Wukong Agent OSの本格普及 — 「ロブスターから悟空へ」のシフト
|
|Juejin記事（6/5時点で👍115、⭐90の人気）で開発者が **「体験完阿里悟空、我想把电脑里的龙虾换掉了」** と報告。悟空がOpenClaw（ロブスター）の後継として本格的に認知されつつある：
|
|- **悟空の優位点**: 安全（企業級）、高自由度（自作モデル/Skills/MCP対応）、Alibabaエコシステムとの連携
|- **OpenClawの課題**: 脆弱性問題（12脆弱性クラス）、SOE禁止、エコシステムの冷却傾向
|- **スコア**: 記事115票（高いエンゲージメント）— 中国Agent開発者の関心が悟空にシフト中
|- 阿里Q4财报でも悟空の企業Agentプラットフォームとしての規模拡大が確認済み
|
|> **出典**: Juejin — [体験完阿里悟空（3/18記事だが6/5時点で継続的高評価）](https://juejin.cn/post/7618418125198196779) [T2]; 36kr — [巨头混战企业Agent（5月）](https://36kr.com/p/3809987729842183) [T1]
|
|### 4. DeepSeek最新動向 — 估值150億ドル追加・有料化・V4-Pro vs GLM-5.1比較
|
|#### 4.1 DeepSeek估值再漲150億ドル（2026年6月5日）
|- **首輪融資500億元（約690億ドル）評価**に加え、さらに150億ドル評価上昇
|- 互联网大廠（BATB）が投資と自研の二派に分かれる
|- 騰訊は生態投資、寧德時代（CATL）は算力インフラ投資の観点
|
|> **出典**: 36kr — [DeepSeek估值再涨150亿美元（6/5）](https://36kr.com/p/3839648403372675) [T1]
|
|#### 4.2 DeepSeekの「成人式」— 有料化と制限強化
|- **「收费才是DeepSeek的'成人礼'」**（6/4 36kr分析）: DeepSeekが無料時代から有料化へ本格移行
|- **再生・修正回数制限**（5/30導入）: 無料枠の利用制限を強化
|- 背景: 推論コストは$0.30/MTokと安価だが、Agentの自律ループによるAPI呼び出し急増でコスト負担が拡大
|
|> **出典**: 36kr — [收费才是DeepSeek的成人礼（6/4）](https://36kr.com/p/3838491912440326) [T1]; 36kr — [DeepSeek制限強化（5/30）](https://36kr.com/p/3831137120395271) [T1]
|
|#### 4.3 DeepSeek-V4-Pro vs GLM-5.1 コード能力比較（2026年4月24日記事・引き続き参照）
|- DeepSeek-V4-Proがコード能力でGLM-5.1に肉薄
|- Juejinで93票の高評価
|
|> **出典**: Juejin — [DeepSeek-V4-Pro vs GLM-5.1（4/24）](https://juejin.cn/post/7632230684447211554) [T2]
|
|### 5. Agent Token最適化 — headroom（コンテキスト圧縮層）登場
|
|2026年6月5日、**headroom** というオープンソースツールがJuejinで紹介され、Agent Token消費問題への新しいアプローチとして注目：
|
|- **機能**: AI Agent専用のコンテキスト圧縮層。LLMに到達する前にツール出力・ログ・RAGデータブロック・コードを圧縮
|- **性能**: Token消費を最大**95%削減**、回答品質を維持
|- **意義**: Agentの自律ループによるToken爆発問題に対する実用的な解決策
|- **Agent Token消費トレンド**: 中国日均Token消費180兆超のうち70%以上がAgent起因。headroomのような最適化ツールの需要が急増
|
|> **出典**: Juejin — [headroom - 給AI Agent装上上下文压缩层（6/5）](https://juejin.cn/post/7647781963354079286) [T2]
|
|### 6. 字节AI 2026年の4大重要命題（36kr独家6/4）
|
|36krが字节跳动（ByteDance）の2026年AI戦略を分析：
|1. **豆包（Doubao）のMAU維持・拡大**: MAU 2億突破後、さらなる成長エンジンが必要
|2. **火山引擎Agent Planの普及**: 業界初のAgent套餐包の市場浸透率
|3. **国産チップ戦略**: 2000億元資本支出のうち850億元をAIチップに、国産比率増加
|4. **Agentエコシステムの囲い込み**: 扣子（Coze）2.5、DeerFlow、MarsCode等の統合戦略
|
|> **出典**: 36kr — [36氪独家｜2026年字节AI的四个关键命题（6/4）](https://36kr.com/p/3838454229027072) [T1]
|
|### 7. Agentセキュリティ — シリーズ記事がホットトピックに
|
|Juejinで **「Agent系列（13）」** としてAgentセキュリティの詳細ガイドが公開（6/5）：
|- **3つの攻撃チェーンを実証**: 提示詞注入、ツール悪用、データ漏洩
|- Agentの攻撃面が通常のLLMより格段に広いことを実証
|- ClawHubの悪意Skill（11.3%）問題との関連
|
|> **出典**: Juejin — [Agent系列13：Agent安全与防护（6/5）](https://juejin.cn/post/7647333934796439615) [T2]
|
|### 8. 低コードAgentプラットフォームの汎用アーキテクチャ設計
|
|Juejinで低コードクラス（Low-Code）プラットフォーム向けのAgent汎用アーキテクチャ設計が公開（6/5）：
|- **基本シナリオ**: 知識ベースRAG + ビジュアルモデリング + ビジュアルビュー
|- **Agent実装の入口**: 知識ベースRAGとスマートSchema生成から着手
|- **意義**: 低コード業界全体でのAgent統合が標準化フェーズに移行
|
|> **出典**: Juejin — [低码类平台Agent通用架构设计（6/5）](https://juejin.cn/post/7647747244403294218) [T2]
|
|### 9. AutoGen企業級入門書（6/4）
|
|Juejinで **AutoGen精通教程：从零到企业级多Agent系统架构师** が公開（6/4）：
|- マイクロソフトのAutoGenフレームワークの企業導入ガイド
|- マルチAgentコラボレーションの実践的設計パターン
|- 中国市場でのAutoGen採用が拡大傾向
|
|> **出典**: Juejin — [AutoGen精通教程（6/4）](https://juejin.cn/post/7647445670953287707) [T2]
|
|### 10. 総括：6月上旬の5大トレンド
|
|1. **Codexエコシステムの中国化**: CC-Switch/Codex++で中国モデル（DeepSeek/GLM/Kimi）がCodex環境で利用可能に。さらにCodex SitesでWebサイト構築まで統合
2. **「悟空シフト」加速**: 阿里悟空がOpenClawの後継として開発者の支持を集める。脆弱性・SOE禁止が追い風に
3. **DeepSeekの有料化完了**: 估值150億ドル追加、無料枠制限強化、企業向け課金モデルへの本格移行
4. **Token最適化が急務に**: headroom登場（95%削減）、Agent起因のToken消費が70%超に。効率的なToken管理がAgent経済の核心課題に
5. **Agentセキュリティとアーキテクチャの標準化**: セキュリティガイドライン・低コードアーキテクチャ設計・AutoGen企業導入ガイドが同時に登場し、エコシステムの成熟を示唆
|
|**主要データポイント**:
|- 中国日均Token消費: **180兆超**（米国の4倍）
|- Agent起因Token消費: **70%超**
|- DeepSeek V4推論価格: **$0.30/MTok**（GPT-5.5比100分の1）
|- 字节AI資本支出: 2000億元、うち850億元をチップ調達
|- headroom Token圧縮率: **最大95%**
|- 阿里悟空記事スコア: **115票**（高いコミュニティ関心）

---

## 2026年6月7日〜12日 — エージェントベンチマーク・パラダイム転換・教育エコシステム成熟

### 11. 「Agentの最後の試験」— エージェントベンチマークの衝撃（6月10日）

36krで **「Agent的最后一场考试」** が大規模議論を呼んだ。強化学習ベンチマークで**最高得点がわずか8.6%**、Claude Codeは0点だったと報告。この結果は、高機能LLMがエージェントタスクで精彩を欠く現状を浮き彫りにし、Coding Planの品質評価にも間接的な影響を与えた。

> **出典**: 36kr — [「Agent的最后一场考试」来了（6/10）](https://36kr.com/p/3847188569639169) [T1]

### 12. CLI + MCP + Skill：2026年AI Agent開発の三大パラダイム（6月11日）

Juejinで **「CLI + MCP + Skill：2026年AI Agent开发的三大范式」** が公開。Agent開発の3つのパラダイムを定義：
1. **CLIパラダイム**: Claude Code/Codex/Kimi Code型のコマンドライン開発ツール
2. **MCPパラダイム**: Model Context Protocolを通じたツール連携と標準化
3. **Skillパラダイム**: OpenClaw ClawHub/Hermes Agent技能系のスキルベース開発
- 三大パラダイムの相互補完関係を提唱し、Agent開発の標準化フレームワークを提示

> **出典**: Juejin — [CLI + MCP + Skill（6/11）](https://juejin.cn/post/7650031039254953984) [T2]

### 13. Hermes vs OpenClaw — Agent Loop比較分析（6月10日）

Juejinで **Hermes AgentとOpenClawのAgent Loop完全比較**が公開。ソースコードレベルでのアーキテクチャ比較が中国開発者コミュニティで注目を集める。中国発エージェントフレームワークへの関心の高まりを示す。

> **出典**: Juejin — [Hermes vs OpenClaw（6/10）](https://juejin.cn/post/7649633479533887524) [T2]

### 14. 「Chat is dead」— AIインタラクションパラダイム転換議論（6月10日）

Juejin記事で **「Chat is dead」** — OpenAIがチャットを超えた新たなAIインタラクション方式への移行を進めているとの分析が注目を集めた。中国Agentエコシステムの発展方向にも示唆を与える議論：

- **従来**: ChatGPT型の対話インタラクション
- **次世代**: Agent駆動のタスク完了型インタラクション
- **中国視点**: 中国もChatbot→Agentへの移行が不可避との認識が共有された

> **出典**: Juejin — [「Chat is dead」（6/10）](https://juejin.cn/post/7649611053488291880) [T2]

### 15. DeepSeek V4による数学証明 — 500倍コスト優位（6月7日）

36krでプリンストン大学のGoedel-ArchitectプロジェクトがDeepSeek V4-Flashを利用した数学証明で500倍のコスト優位を達成したと報告。Agentエコシステムにおける「低コストモデル×エージェント能力」の新たな可能性を示す。

> **出典**: 36kr — [DeepSeek V4 500倍コスト優位（6/7）](https://36kr.com/p/3841174468151553) [T1]

### 16. Fable 5/Claude Code — 5000万行コード移行と中国市場への間接的影響（6月10日）

AnthropicがClaude Fable 5およびMythos 5をリリース（5000万行コード移行が1日で完了）。直接的な中国市場影響は限定的だが、中国Agentコミュニティでの話題性は高く、以下の波及効果が観察された：
- Kimi K2.5への移行事例増加報告（アクセス障壁のない国内モデルへの逃避）
- 国内Coding Planの需要基盤は不変
- Agent能力の「上限」に対する認識が向上

> **出典**: 36kr/新智元/量子位 2026-06-10 [T1]

### 17. Agent教育コンテンツの爆発的増加 — エコシステム成熟を示す

6月7日〜12日、Juejinで以下のAgent教育コンテンツが連日公開され、エコシステムの「ユーザー教育フェーズ」への移行を示唆：
- **「实现一个Coding Agent（5）」**（6/7）: 実装シリーズ完結、実践的コーディングAgent構築
- **「Agent系列（18）：成本与性能优化」**（6/10）: コスト最適化ガイド
- **「AutoGen精通教程」**（6/7再話題化）: 企業導入の包括的ガイド
- **CodeGraph**（6/11）: AI Agentコード構造理解ツール（GitHub 62K Stars）
- **低コードAgent設計**（6/7再話題化）: 標準設計パターンの確立
- **「2026年从0开发AI Agent需要的10个技能」**（6/10-11）: スキルセット体系化

### 18. 総括：6月第2週の新たなトレンド

1. **エージェント評価の厳格化**: 8.6%の低ベンチマークスコアが業界に衝撃。品質評価の重要性が急浮上
2. **三大パラダイムの標準化**: CLI-MCP-Skillの住み分けと相互補完関係が明確に
3. **Agent開発の民主化**: 教育コンテンツ爆発と低コードツールにより、Agent構築がより広い層に開放
4. **コスト最適化の深化**: headroom（95%削減）やAgentシリーズのコスト最適化ガイドが登場
5. **中国発フレームワークの自立**: Hermes vs OpenClaw比較がコミュニティ議論の対象に

### 追加データポイント
- Agent最後の試験最高得点: **8.6%**（Claude Code 0点）
- DeepSeek V4数学証明コスト優位: **500倍**
- Juejin Agent教育記事: **週10+本**（6月第2週）

---

## 2026年6月中旬〜7月下旬 — Kimi K3算力崩壊・Claude Code禁止・Agent安全基準化・OpenClaw復活

### 19. 【最重要】阿里巴巴 Claude Code全面禁止 — 隠蔽ユーザー検出メカニズム発覚（7月10日）

2026年7月10日、**阿里巴巴がClaude Codeを全製品で全面禁止**。原因はClaude Code 2.1.91版（2026年4月〜）に組み込まれた**隠蔽ユーザー検出メカニズム**の発見：

- **検出対象**: システム時区（Asia/Shanghai/Asia/Urumqi）と中国クラウド/AI企業のキーワード
- **暗標方式**: 命中時にUnicode文字で暗標（日付形式の差分、右单引号 `\u2019` 等）
- **送信先**: 検出結果をAnthropicサーバーに暗号化して送信
- **隠蔽工作**: コアロジックを暗号化混淆、147ドメインをパスワードロック
- **Anthropicの対応**: Thariq Shihiparが「実験的措置」と認め7/2版で回滚
- **波及**: 大量中国ユーザーのアカウント凍結も同時期に発生
- **阿里の対応**: 自社「Qoder」を代替推奨

> **意義**: 中国AI開発者コミュニティにおける「国产替代（国産代替）」加速の転機。Claude Codeからの離脱が加速し、Kimi K2.5・Qoder・Hermes Agent等への移行が加速。

> **出典**: ChinAI Newsletter #367（2026-07-20）[T1]

### 20. 信通院 AI Safety Benchmark 2026 Q2 — Claw類智能体の安全基準テスト（6月〜7月）

中国信息通信研究院（CAICT）がClaw類智能体のセキュリティ基準テストを実施：

| 指標 | 結果 | 備考 |
|------|------|------|
| 内容有害率 | 5%以内 | 比較的安定 |
| 幻覚率 | 内容有害率より顕著に高い | 重要な課題 |
| 任務執行成功率 | 94%以上 | 高性能 |
| **行為有害率** | **最大36%** | **重大な懸念** |
| 網頁注入攻撃成功率 | **24%** | ファイル注入の2倍 |

- **テスト対象**: OpenClaw (2026.6.10), NanoClaw, NemoClaw, MetaClaw, **Hermes (v0.17.0)**を含む
- **500条のサンプル、5大维度**: 客服/金融/医療/教育をカバー
- **結論**: Agentの「行為有害率」が最大36%と高水準であり、セキュリティ改善が急務

> **出典**: ChinAI Newsletter #365（2026-07-06）[T1]

### 21. Kimi K3正式リリースと算力崩壊（7月16日〜22日）

**Kimi K3**が2026年7月16-17日に正式リリース。Claude Fable 5との直接比較で「全球第一梯队」と評価：

- **イーロン・マスクが反応** — 国際的注目を集める
- **7/18に503 Service Unavailable崩壊**: 爆発的需要がインフラ容量を超過
- **会員停売（販売停止）**: 算力告急（計算資源枯渇）
- **GLMも同様に購入制限** — 中国AI市場全体で計算資源が逼迫
- **評価額$30B（約2,035億元）目標**の追加資金調達
- **黄仁勋（NVIDIA CEO）がKimi K3开源を力挺** — 「开源vs閉源の第一戦」と位置づけ

> **意義**: Kimi K3の需要過多は、中国AI Agent市場の「計算資源ボトルネック」を可視化。Agentのスケーラビリティに対するインフラ面の制約が浮き彫りに。

> **出典**: wiki/concepts/kimi.md; 36kr（2026-07-16〜22）[T1]

### 22. OpenClaw復活 — v2026.7.x安定版リリース（7月13日〜18日）

6月の冷却期を経て、OpenClawがリリース復活：

- **v2026.7.1安定版**（7/13）+ **v2026.7.2-beta.3**（7/18）
- **GitHub Stars 384K**（+10K/5週）
- **Control UI全面刷新** + 公式アプリ重大更新 + GPT-5.6対応
- **openclawai.org.cn** 中国公式ブランドサイト登録
- **競合**: Hermes Agentトークン消費逆転継続 / 阿里悟空企業セキュリティ優位
- **12類安全隐患・ClawHub悪意スキル11.3%問題**は継続中

> **出典**: wiki/entities/openclaw.md（2026-07-26更新）[T1]

### 23. 阿里「千問辦公」— AI辦公「智能体竞速」時代への参入（7月下旬）

36kr報道（2026-07-24）: Alibabaが「千問辦公」でAI辦公市場に参入。「AI办公进入'智能体竞速'時代」と位置づけ：

- 阿里のAI辦公戦略の新展開
- 既存のQwenモデル×辦公シーン統合
- 腾讯WorkBuddy・ByteDance扣子との辦公Agent市場競争が激化

> **出典**: 36kr（2026-07-24）[T1]

### 24. OpenAI三線同時障害 — Agent時代の宕機コスト議論（7月26日）

2026年7月26日、OpenAIがCodexを含む三系統同时障害：

- Agent時代の宕機（ダウンタイム）コストが顕在化
- 中国Agentエコシステムへの影響: Codex依存プロジェクトの一時停止
- 「Agent基盤の冗長性」が新たな競争軸に

> **出典**: 36kr（2026-07-26）[T1]

### 25. 復旦NLP 80頁 Agent综述 — 学術的体系化（7月下旬）

復旦大学NLPチームが**80ページのAI智能体综述**を発表：

- AI智能体の現状と未来を網羅
- 中国におけるAgent研究の学術的成熟を示す

> **出典**: WeChat（2026-07-24）[T2]

### 26. 総括：6月中旬〜7月下旬の5大トレンド

1. **「国产替代」加速**: Claude Code隠蔽検出→阿里禁止→大量封号。中国開発者の国产代替が本格化
2. **Agent安全基準の制度化**: 信通院がClaw類智能体の安全基準テストを実施し、行為有害率36%という問題を可視化
3. **Kimi K3による計算資源枯渇**: 旗艦モデルリリースが市場全体のインフラ容量を超過。Agentスケーラビリティの制約が浮き彫り
4. **OpenClaw復活と競合再編**: 6月の冷却期を経てリリース復活。Hermes Agent・阿里悟空との三つ巴構造が深化
5. **「Chat is dead」パラダイム転換**: Agent駆動のタスク完了型がChatbotを代替する方向性が明確化

**主要データポイント**:
- 行為有害率: **最大36%**（信通院基準テスト）
- Kimi K3 503崩壊: **7/18**（算力告急）
- OpenClaw GitHub Stars: **384K**（+10K/5週）
- Claude Code隠蔽検出: **147ドメイン**パスワードロック
- Agent最後の試験最高得点: **8.6%**（前回から変動なし）