---
title: Qwen（通义千问）— 阿里云大模型旗舰
created: 2026-04-17
updated: 2026-05-10
tags: [llm, model, china, open-source-ai, alibaba, qwen, agentic-coding, ai-infrastructure]
aliases: ["Qwen", "通义千问", "qwen", "Qwen3.5", "Qwen3-Coder", "Qwen3.6", "Qwen3.6-Plus", "Qwen3.6-27B", "Qwen3.6-35B-A3B"]
source_lang: zh-CN
---

# Qwen（通义千问）— 阿里云大模型旗舰

> **トレンド順位**: #12（2026-04-17集計）→ 2026年4月最新で急上昇
> **ソース**: 36kr, Juejin, V2EX, WeChat, Zhihu, Yahoo Finance, MarkTechPost（6+ソース）
> **重要度**: 高 — 中国エンタープライズ大モデル呼び出し量シェア第1位（32.1%）

## 概要

Qwen（通义千问）は、**阿里巴巴（Alibaba Group）**が開発する大規模言語モデルシリーズ。2026年4月現在、中国エンタープライズ市場において大モデル呼び出し量シェア**32.1%**を占め、沙利文報告により**中国企业级大模型调用量第1位**に位置づけられている。

AlibabaはQwenを中核とした**フルスタックAI戦略**を展開：モデル（Qwen）→ インフラ（Alibaba Cloud + Zhenwu AIチップ）→ エコシステム（Taobao/Tmall, Alipay, Ele.me, DingTalk）→ エンタープライズアプリケーション（Wukong, Qwen App）。

Apache 2.0ライセンスでオープンソースリリースを推進し、Qwen3.6シリーズ（0.8B〜397B MoE）をHugging Face Hubで公開。proprietaryモデルではQwen3.6 Plusが2026年4月2日にリリースされ、1Mコンテキストとalways-on chain-of-thoughtを備える。

## AlibabaのAI戦略と市場影響

### 3800億元（$69B）3か年投資計画

Alibabaは2026年4月、**3年間で3800億元（約$690億）**をAIとクラウドインフラに投資すると発表した。これは従来の計画を上回る大規模なCapExであり、以下の目標を目指す：

- **2029年までにクラウド・AI収益$1000億**
- **国内AI計算資源の完全自立**（Nvidia依存からの脱却）
- **エンタープライズAI市場でのシェア拡大**（現在32.1%）

この投資は短期利益を圧迫している。2025年12月四半期、GAAP純利益は**66%減の$22億**に低下。しかし、クラウド部門（Cloud Intelligence Group）は**36%増の¥433億**を記録し、AI製品は**10四半期連続で三桁成長**を示している。

### Zhenwu AIチップ — 垂直統合のシリコン層

2026年4月8日、Alibabaと**中国电信（China Telecom）**は広東省韶関市に**10,000個のZhenwu AIチップ**搭載のAIデータセンターを公開した。これは中国国内設計AIチップの大規模実装としては最大級。

- **初段デプロイ**: 10,000チップ（2026年4月）
- **計画スケール**: 100,000チップ
- **ワークロード**: 数百億パラメータ規模のモデル訓練・推論
- **運営**: China Telecomが資産を所有・運用、Alibabaがチップ設計（T-Head）

2026年2月時点で**47万個以上**出荷済み。将来的には**玄鉄（XuanTie）C950-5 CPU**（RISC-Vベース）もagentic AI向けに追加。

### フルスタック4層垂直統合

| 層 | 要素 | 役割 |
|------|------|------|
| **シリコン** | Zhenwu AIチップ, 玄鉄 CPU | 訓練・推論のハードウェア基盤 |
| **クラウド** | Alibaba Cloud（中国シェア第1位） | インフラ・デプロイメント |
| **モデル** | Qwenシリーズ（OSS + proprietary） | AI知能の中核 |
| **アプリケーション** | Wukong, Qwen App, 钉钉, ERP | エンタープライズ・消費者向け |

この垂直統合により、AlibabaはNvidia依存を減らし、中国国内のAI自立ニーズに応える。

### S字カーブと市場予測

AlibabaのAI投資は典型的な**S字カーブ**の早期段階にある。AWS/AzureがクラウドS字カーブで成功したのと同様、Alibabaがエンタープライズ採用を勝ち取れば株価は**$200**へ到達する可能性もある。しかし、収益化の遅延や国内競争（Baidu, Tencent, ByteDance, DeepSeek）が激化すれば、**$100**前後でレンジBOUNDとなるリスクもある。

> **出典**: [Bitget News — Qwen 3.6 Marks Alibaba's Push](https://www.bitget.com/news/detail/12560605360273), [Yahoo Finance — Qwen3.6 Plus Targets Enterprise AI](https://finance.yahoo.com/markets/stocks/articles/alibaba-qwen3-6-plus-targets-070714378.html), [Simply Wall St — Zhenwu-Powered AI Cluster](https://simplywall.st/stocks/us/retail/nyse-baba/alibaba-group-holding/news/will-alibabas-new-zhenwu-powered-qwen36-plus-ai-cluster-chan)

## Qwen3.6シリーズ（2026年4月最新）

### Qwen3.6-Plus — 新proprietary Flagship（2026年4月2日）

Alibabaの最新flagshipモデル。エンタープライズワークフロー向けに設計され、Wukong（AI企業向けプラットフォーム）とQwen Appに統合。

- **1M native context**（2,000ページ相当のテキストを1プロンプトで処理）
- **Always-on chain-of-thought**（思考/非思考トグル廃止、全プロンプトでデフォルト推論）
- **Agentic coding**に最適化（MCPMark、DeepPlanningで業界首位）
- **マルチモーダル推論**: 画像・動画・テキスト統一処理
- **視覚コーディング**: UIスクリーンショット、手描きワイヤーフレーム、プロトタイプから即時フロントエンドコード生成
- **推論速度**: ~158 tok/s（Claude Opus 4.6の1.7倍、GPT-5.4の2倍）
- **価格**: $0.325/M入力、$1.95/M出力（Claude Opus 4.6の約17分の1）
- **アーキテクチャ**: 397B総パラメータ、17B active（sparse MoE）
- **ベンチマーク**: Terminal-Bench 65.4%（Claude Opus 4.6を大幅に凌駕）、MCPMark首位
- OpenRouterで無料プレビュー期間（2026年3月30-31日）

> **出典**: [Alibaba Cloud Community — Qwen3.6-Plus Announcement](https://www.alibabacloud.com/blog/603000)

### Qwen3.6-Max-Preview — 最大旗舰预览版（2026年4月20日頃）

Qwen3.6-Plusの上位バージョン。**五大核心升级**:

1. **世界知識大幅增强** — 幻觉显著降低、長文本知識推理強化
2. **指令遵循能力质变** — 複雑長指令・多步骤任务・严格格式出力が安定
3. **智能体Agent能力大幅提升** — 長程計画・多輪工具呼び出し・複雑任務分解
4. **编程能力飞跃** — コード理解・プロジェクト開発・Debug・多言語工程化が全球第一梯队レベル
5. **新增思考保留功能（preserve_thinking）** — モデルの全程推論思考チェーンを完全保存

SWE-bench Pro、Terminal-Bench 2.0、SkillsBench、QwenClawBench、QwenWebBench、SciCodeの**6項主要プログラミングベンチマーク**でQwen3.6-Plusを全面超越。

> **出典**: [新浪新闻 — 阿里通义千问发布新一代旗舰](https://www.sina.cn/news/detail/5289894780869670.html)

### Qwen3.6-35B-A3B のツール呼び出しベンチマーク首位（2026年4月）

Zhihu Frontier Weeklyの構造化ツール使用評価（structured tool-use evaluation）において、**Qwen3.6-35B-A3B-FP8**が69/72（96%）の精度を記録。これはGLM、Kimi、DeepSeek、StepStar、MiniMaxを含む**中国主要5大商用APIを凌駕**する結果。RTX 4090（48GB）環境で~1024msのレイテンシを達成し、ローカル実行においても実用レベルのパフォーマンスを示した。

> **出典**: Zhihu Frontier Weekly — [From DeepSeek V4 to Kimi K2.6](https://zhihufrontier.substack.com/p/from-deepseek-v4-to-kimi-k2-6) (2026-04-27) [T1]
> **出典**: Zhihu — [Qwen3.6-35B-A3B性能分析](https://www.zhihu.com/question/2028243224301454445) [T1]

### Qwen3.6-35B-A3B — オープンソース稀疏MoE（2026年4月16日）

- **35B total / ~3B active**（256 experts、8 routed + 1 shared）
- **Native 262,144 token** context（YaRNで~1Mへ拡張）
- **Apache 2.0**（商用利用自由）
- **Claude Opus 4.7の~82%**の集計パフォーマンス
- **MCP Atlasツール使用**: 62%（知識タスク: 97%）
- **Ollama、LM Studio、Jan.ai、llama.cpp、vLLM**でローカル実行可能
- **AMD Instinct GPU** Day-0サポート

> **出典**: [Qwen Blog — Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b)

### Qwen3.6-27B — オープンソース密型（2026年4月22日）

Qwen3.6シリーズの**最初のdense（非MoE）モデル**。27Bパラメータで397B MoEを凌駕するパフォーマンスを発揮。

- **27B密型アーキテクチャ**（単一H100 GPUで動作）
- **Gated DeltaNet線形注意 + 伝統的自己注意のハイブリッド**
- **Thinking Preservation**メカニズム（新機能）— 会話履歴 across で推論トレースを保持、トークン消費削減 + KVキャッシュ効率化
- **ベンチマーク成績**:
  - SWE-bench Verified: **77.2%**（Qwen3.5-397B-A17Bの~74%を凌駕、Claude Opus 4.6の80.8%に迫る）
  - Terminal-Bench 2.0: **59.3%**（Claude Opus 4.6と**完全にマッチ**）
  - QwenWebBench: **1487**（Qwen3.5-27Bの1068から大幅向上）
  - SWE-bench Pro: **53.5%**（Qwen3.5-397B-A17Bの50.9%を凌駕）
  - SkillsBench Avg5: **48.2%**（Qwen3.5-27Bの27.2%から77%相対改善）
- **2 weight variants**: BF16 (`Qwen/Qwen3.6-27B`) および FP8量子化版（block size 128）
- **SGLang、vLLM、KTransformers、HF Transformers**互換
- **262K native context**（YaRNで1Mへ拡張）

> **出典**: [Qwen Blog — Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b), [TokenMix Review](https://tokenmix.ai/blog/qwen-3-6-27b-review-dense-beats-moe-2026)

### Qwen3.6-Max-Preview のクローズドウェイト転換（2026年4月20日）

2026年4月20日、AlibabaはQwen3.6-Max-Previewのリリースと同時に**重要な戦略転換**を発表した：

1. **クローズドウェイト化**: Qwen3.5まで継続してきたオープンソース路線を初めて転換し、Max-Previewを**プロプライエタリ専用モデル**に設定
2. **無料ティア廃止**: Max-Preview発表と同日にQwen Codeの無料枠（Qwen OAuth無料枠）を終了。ユーザーはOpenRouter・Fireworks・阿里云百炼への移行を推奨
3. **OpenAI/Anthropic両API互換**: OpenAI仕様とAnthropic仕様の両方でリクエストを受け付ける新API設計
4. **コーディング6ベンチマーク首位**: SWE-bench Pro・Terminal-Bench 2.0・SkillsBench・QwenClawBench・QwenWebBench・SciCodeで首位を主張

この転換は「Alibabaはオープンソース」という前提での戦略設計が通用しなくなったことを意味する。Qwen3.6シリーズのOSS提供は35B-A3B（MoE）と27B（Dense）に限定され、フラッグシップ性能はクローズドウェイトで提供される新体制に移行した。

> **出典**: [Uravation — Qwen 3.6-Plus完全ガイド](https://uravation.com/media/qwen36-plus-alibaba-agent-model-guide-v2-2026/)

### Qwen3-Coder — コーディング特化（480B MoE / 35B active）

コード生成・理解に特化したバージョン。Claude Code、Cursorと比較する記事が掘金・V2EXで多数投稿。CodingPlan（[[coding-plan]]）においてKimi K2.6およびGLM-4.7と並んでバンドル提供。

### Qwen Code — AIエージェント開発環境（v0.14.xアップデート）

2026年4月、Qwen Codeは**v0.14.0〜v0.14.5**の一連のバージョンをリリースし、AIコーディングアシスタントから「自律エージェントシステム」への進化を遂げた。

**主な新機能（v0.14.3〜v0.14.5、2026年4月16日）**:

1. **スマートツール並列実行**: 読み取り専用ツール（検索、ファイル読み込み等）を自動的にバッチ並列実行。書き込み操作は直列実行を維持し安全性を確保。多ツールシナリオで応答時間が大幅に短縮。
2. **Fork子エージェント**: サブタスク分割時に子エージェントが親エージェントのコンテキストを自動継承。大規模タスクの分割実行に最適。
3. **CJK分詞ナビゲーション**: Ctrl+左/右方向キーで中日韓文字の単語単位ジャンプ。混合入力を含むターミナル操作の体験が大幅に改善。
4. **/review コードレビュー改善**: LLMに依存しない静的チェック（確定分析）、自動修正提案、セキュリティ強化チェックを追加。
5. **Telegram・钉钉・WeChat統合**: チャンネル経由でサーバーをリモート制御可能に。スマートフォンからコード修正・ログ確認・スクリプト実行が可能。
6. **Cron Jobs（/loopコマンド）**: 定期的なコードテスト・自動ビルド・ログ監視をスケジュール実行。手動crontab編集が不要。
7. **/plan 事前計画モード**: 実行前にファイル構造と実行手順を整理し、ユーザー確認後に実行。成功率が顕著に向上。
8. **サブエージェントのモデル分割**: 強力なモデルを全体計画に、軽量モデルを個別タスクに割り当て、トークン消費を最適化。
9. **子エージェントの承認モード継承**: 親エージェントの承認設定を自動継承。重複設定不要。
10. **Qwen OAuth無料枠終了**: 2026年4月15日をもって無料枠終了。OpenRouter・阿里云百炼・Fireworksへの移行を推奨。

> **Qwen3.6-PlusはOpenRouterで日間1.4兆Tokenを記録**: リリース僅か1日でOpenRouter日次API呼び出しランキングで世界1位を達成。単一モデルとしての1日1.4兆TokenはOpenRouter史上最高記録（出典: 新浪科技）

> **出典**: [Qwen Code 週報 (2026-04-16)](https://qwenlm.github.io/qwen-code-docs/zh/blog/weekly-update-2026-04-16/), [新浪新闻 — Qwen Code更新](https://www.sina.cn/news/detail/5286584468638183.html)

### 価格競争 — Qwen3-Max 50%値下げ

2026年の中国AI価格戦争でQwen3-Maxの料金が最大50%引き下げ。trillion-parameter閉鎖モデルながら、競争激化により価格破壊を起こしている。

### Qwen3.6-Flash — 軽量高速モデル（2026年4月16日）

Qwen3.6シリーズの軽量版として **Qwen3.6-Flash** が阿里云百炼に追加。Qwen3.5-Flashの後継で、Qwen3.6-35B-A3Bをベースに高速推論に最適化。価格はQwen3.6-Plusの約1/10で、リアルタイム対話・チャット・基本的なコード補完に適する。

> **出典**: [阿里云百炼 模型上下架与更新](https://help.aliyun.com/zh/model-studio/newly-released-models) (2026-04-16)

## 通义灵码 (Lingma) — AI IDE正式版リリース（2026年5月）

通义灵码（Lingma）はQwenモデルを搭載したAlibabaのAIプログラミングアシスタント。2026年5月、**Lingma IDE**（VS Codeベースの独立AI IDE）が正式版としてリリースされた。

### Lingma IDE 正式版 主要機能

| 機能 | 説明 |
|------|------|
| **Agentic Ask** | 以前のAsk(質問)モードをAgentic化。エンジニアリング感知・Web検索ツールを自律的に呼び出し、プロジェクトに即した回答が可能に。手動ファイル追加が不要。 |
| **NES（行間編集予測）** | Next Edit Suggestion。現在のコードコンテキスト・カーソル位置・変更パターンに基づき、次に行うべきコード編集を予測。Tabキーで適用可能。 |
| **Inline Chat（行間会話）** | コードエディタ内で直接会話。ファイルを離れずにコード修正・質問が可能。 |
| **プログラミングエージェント** | Qwen3モデル搭載。タスク記述から自律的に工程感知・コード検索・端末実行・MCPツール呼び出しを実行。 |
| **長期記憶** | 過去の会話から開発者の好み・プロジェクトルールを自動記憶。 |
| **Quest モード** | 自律プログラミング。ユーザー入力の意図を認識し最適な能力へ自動ルーティング。 |
| **プラグイン不要** | VS CodeのLingmaプラグインは非推奨化、IDEへの移行推奨。 |

### 戦略的意義

Lingma IDEのリリースは、AlibabaがAIコーディングアシスタント市場で **Cursor/Claude Codeに直接対抗する製品**を投入したことを意味する。従来の「VS Codeプラグイン」から「独立AI IDE」への移行により、NESやInline Chatなどプラグイン側では実装困難な機能を統合。Qwen-Coder-Qoderモデル（Qwen-Coderベースの強化学習特化モデル）を搭載し、Cursor Composer-1を超越するタスク解決率を主張。

> **出典**: [阿里云开发者社区 — 通义灵码5月更新](https://developer.aliyun.com/article/1665770), [Lingma IDE 更新日志](https://help.aliyun.com/zh/lingma/product-overview/changelogs-of-lingma-ide)

## 通义实验室 (Tongyi Lab) — 研发背景与组织变革

**通义实验室**は、阿里巴巴（Alibaba Group）のAI大モデル研究機関。Qwen（通义千问）シリーズの生み出し元。

### 歴史と沿革

- **2014年**: **iDST（数据科学与技术研究院）**設立。AI核心技術の研究開発に着手。
- **2017年**: iDSTが**达摩院（DAMO Academy）**に改組。同年、中国初の機械学習プラットフォーム「PAI」を阿里云がリリース。
- **2020年**: 多模态大模型プロジェクト**M6**始動。
- **2021年10月**: M6の最大パラメータ規模が**10兆（10 trillion）**に到達。当時世界最大級のアプリトレーニングモデル。
- **2022年**: **通义实验室（Tongyi Lab）**が正式設立。M6等の研究成果を基盤に、9月に「通义」シリーズ大モデルを発表。
- **2023年4月**: **通义千问（Qwen）**大语言モデルシリーズ正式リリース。
- **2024年5月**: モデル名が「Qwen」から**「通义（Tongyi）」**へ改名。「通义」は『漢書』の一節「天地の常道、古今の通義（天地の常なる道理、古今の通じる義理）」に由来し、AIが万物に応用可能な原理と法則を持つことを象徴。
- **2026年**: Qwenシリーズは「通义」ブランドの下で展開（通义千问、通义万相等）。

### 2026年4月の組織大刷新

2026年4月8日、CEO**吴泳铭（Eddie Wu）**はAI関連の組織再編を発表。通义实验室の戦略的ポジションが格上げされた。

| 組織変更 | 詳細 |
|------|------|
| **通义大模型事业部** | 通义实验室が**通义大模型事业部**へ昇格。**周靖人（Zhou Jingren）**が責任者に就任。 |
| **集团技术委员会** | 新設。CEO吴泳铭が議長。**周靖人**（首席AI架构师・モデル設計）、**李飞飞（Feidao）**（阿里云CTO・インフラ）、**吴泽明**（集团CTO・推論プラットフォーム）を構成員に据える。 |
| **ATH事业群** | 3月に設立された**Alibaba Token Hub（ATH）**事業群の一環として、モデル層・アプリ層の統合を加速。 |

この再編は、Lin Junyang（林俊旸/千问元技術責任者）の退職後、グループレベルでAIリソースを集中配置し、**「システマティックキャンペーン（体系化された総力戦）」**体制へ移行する目的がある。周靖人は技術派として「AIの司令塔」としての役割を強化。

### 主な研究アウトプット

大モデル研究以外に、以下のようなフレームワーク・ツールを公開：

- **DeepResearch**: 複数ステップの検索・分析を行うDeep Research Agent。
- **Qwen-Agent**: エージェント開発フレームワーク。
- **FunAudio**: 音声・マルチモーダル音声モデル（2025年9月リリース）。
- **Qwen3-VL-Embedding / Reranker**: マルチモーダル情報検索用モデル（2026年1月8日开源）。
- **WebDev, EvalScope, ms-swift, AgentScope** 等。

### Qwen3.6-Max プレビュー価格設定

2026年4月時点のQwen3.6-Max-Previewの料金:
- **$1.30/M 入力トークン**（Alibaba Cloud Model Studio）
- **$7.80/M 出力トークン**
- **90% cache hit割引**: $0.13/M（キャッシュヒット時）
- OpenRouterでは若干異なる: $1.04/M 入力、$6.24/M 出力
- Claude Opus 4.7より入力は安いが、劇的な価格破壊ではない
- ※プレビュー段階でSLAなし、本番利用はGAリリース待ち

> **出典**: [Awesome Agents — Qwen 3.6 Max Review](https://awesomeagents.ai/reviews/review-qwen-3-6-max/) (2026-05)

### 2026年5月初旬のベンチマーク位置づけ更新

2026年5月初旬時点、SWE-bench Pro Leaderboardは急速に変動:
- **Claude Mythos Preview**: 77.8%（首位）
- **Claude Opus 4.7 (Adaptive)**: 64.3%
- **GPT-5.5**: 58.6%
- **Qwen3.6-Max**: 発売時の4月下旬に首位だったが、Claude Mythosに抜かれた

Terminal-Bench 2.0ではQwen3.6-MaxとClaude Opus 4.7が**65.4%でタイ**。GPT-5.4は75.1%でリード。AA Intelligence Index v4.0ではQwen3.6-Maxは**52点**（203モデル中3位、GPT-5.4 58点, Claude Opus 4.7 56点に次ぐ）。

QwenWebBench（Webアプリ・データ可視化・SVG生成に特化したフロントエンド評価）では、Maxの**ELO 1,558**がClaude Opus 4.5の1,182を大きく引き離し、Alibabaが正当に首位を主張できる領域。

> **出典**: [Awesome Agents — Qwen 3.6 Max Review](https://awesomeagents.ai/reviews/review-qwen-3-6-max/) (2026-05)

### Qwen-Scope: 稀疏自己符号化器（SAE）による可解釋性モジュール（2026年4月30日オープンソース）

2026年4月30日、AlibabaはQwenの内部機構を「X線のように」可視化する**Qwen-Scope**をオープンソース公開。従来のAttention可視化ツールとは異なり、**稀疏自己符号化器（Sparse Autoencoder, SAE）**をQwenモデルの隠れ層に挿入し訓練することで、高密度なモデル表現を**高度に解耦・低冗長・解釈可能な特徴**に分解する。

**コア仕様**:
- **7モデル対応**: Qwen3シリーズ・Qwen3.5シリーズの密型モデルとMoEモデルをカバー
- **14組のSAE重み**: 各モデルに対応する稀疏自己符号化器の学習済み重みを公開
- **3300万以上の特徴**: 0.5Bトークンの事前学習データから抽出された高品質特徴
- **HuggingFace / ModelScope**で利用可能

**4つの応用シナリオ**:
1. **推論結果の定向制御**: 特徴アクティベーションを直接制御し、言語・エンティティ・スタイルの定向変更をプロンプトなしで実現（Anthropicのモデルステアリング研究をオープンソースで実装）
2. **データの分類と合成**: 毒性データ分類では少量シードデータでSAE特徴パターンを解析し、追加分類器の訓練なしで高精度分類。データ合成では未活性化の特徴を特定し、ロングテール能力を補うサンプルを定向生成（従来の15倍のデータ効率）
3. **モデル訓練の定向最適化**: 言語混用や反復生成などの低頻度badcaseをSAE特徴で定位し、SFT段階で損失関数を設計。RL段階でのサンプリング密度を高め、異常パターンを効率的に修正
4. **評価サンプルの冗長性分析**: 異なるベンチマーク間のSAE特徴被覆度を計算し、重複評価を排除。より高カバレッジ・低コストのテストセット選定を支援

> 従来のPrompt Engineeringに代わり、モデル内部のアクティベーションに直接介入する**Model Steering**の新時代を開く。AnthropicのSAE研究（2024年）がプロプライエタリモデル中心だったのに対し、Qwen-Scopeはオープンソースコミュニティに同レベルの透明性ツールを提供した点に意義がある。

> **出典**: [Alibaba Cloud Community — Qwen-Scope Technical Blog](https://www.alibabacloud.com/blog/qwen-scope-decoding-intelligence-unleashing-potential_603083) (2026-05-06), [PANews — Qwen-Scope开源](https://www.panewslab.com/zh/articles/019dddaf-4a84-71de-99d9-098f42a57ef2) (2026-04-30), [HowAIWorks — Qwen-Scope Interpretability](https://howaiworks.ai/blog/alibaba-qwen-scope-interpretability-sae) (2026-05-01) [T1]

### QwenPaw（旧CoPaw）— オープンソース個人AIアシスタント（2026年4月リブランディング）

2026年4月12日、阿里云のデスクトップAgentツール**CoPaw**が**QwenPaw**（Qwen Personal Agent Workstation）へリブランディング。通義千問オープンソースエコシステムへの深度統合を宣言した。

**主要特徴**:
- **GitHub★16.4K**（2026年5月9日時点、Apache 2.0ライセンス）
- **最新バージョン**: v1.1.6（2026年5月9日リリース）
- **マルチチャネル対応**: 钉钉・飛書・微信・QQ・Discord・Telegram・iMessage
- **ローカル/クラウド両対応**: 一键pipインストール・Docker・デスクトップアプリ・魔搭創空間
- **ローカルモデル**: Ollama・llama.cpp・Apple MLX・百炼平台に対応
- **Skills拡張**: PDF処理・Excel分析・ニュースダイジェスト等、カスタムSkills自動ロード
- **マルチAgent協調**: AgentScopeフレームワークによる複数Agent間の通信・協業
- **OpenClaw対抗製品**: デスクトップAgentとしてOpenClawに対抗する位置付け。OpenClawがTypeScript/pi-agent-coreベースなのに対し、QwenPawはPython/AgentScopeベースでマルチAgent協調をネイティブサポート
- **専用軽量モデル**: QwenPaw-Flash-9BをHuggingFace公開（ツール呼び出し最適化）
- **多言語ドキュメント**: 英語・中国語・日本語・ロシア語

**v1.1.4→v1.1.5の新機能（2026年4月）**:
- 記憶検索最適化、コンテキスト圧縮のデグレードメカニズム
- ACP Agentの重命名・削除機能
- QQ音声・ASRサポート
- コンフィグファイルとSkillsリストのキャッシュ化
- 内蔵DeepSeek V4モデル
- 計画実行モード、Shell迂回検出の構成可能化

**開発者数**: 160名のコントリビューター、10万名以上の開発者が利用（2026年4月時点）、2000以上のシーンカバー。

> **出典**: [GitHub — agentscope-ai/QwenPaw](https://github.com/agentscope-ai/QwenPaw), [IT之家 — CoPaw更名QwenPaw](https://finance.sina.com.cn/tech/digi/2026-04-12/doc-inhufzfw3074234.shtml) (2026-04-12) [T1]

### Qwen Code v0.15.0 — 自律記憶・バッチ処理・Hook拡張（2026年4月23日）

2026年4月23日、Qwen Code v0.15.0がリリースされ、v0.14.xシリーズの「自律エージェント化」をさらに推し進めた:

**AI 跨会話主動記憶（Auto-Memory + Auto-Dream）**:
- AIが会話中に自動的に重要な情報を記憶に抽出。次回セッションでも前回の情報を保持
- 定期的な自動整理（重複マージ、旧情報更新、インデックス保守）— 「本棚整理のように」
- QWEN.mdや設定ファイルへの手動書き込みが不要に

**/batch 批量処理**:
- 1つのコマンドで複数ファイルの並行修正が可能
- ユースケース: 同種lintエラーの一括修正、複数ドキュメントへの同じセクション追加、一括リファクタリング

**Hook拡張（HTTP/Function/Async Hook）**:
- **HTTP Hook**: AIの変更を飛書・钉钉・Slack等に自動通知
- **Function Hook**: AI完了時に任意のコードを自動実行
- **Async Hook**: 長時間処理をバックグラウンド実行（会話をブロックしない）
- コンプライアンス監査・CI/CD自動化・チームコラボレーション向け

**SubAgent バックグラウンド実行**:
- SubAgentがヘッドレス（非表示）モードで動作可能
- SDK経由でCI/CDパイプラインに組み込み可能
- PR自動レビュー・コード品質チェック等の自動化ワークフローに最適

**その他v0.15.0改善**:
- `/doctor`: 環境・設定・ネットワーク接続を一括診断
- PDF直接読取 + Jupyter Notebook構造化表示
- ディレクトリ別ルール自動適用（`.qwen/rules/`）
- リアルタイムToken消費表示
- `/recap`: 会話履歴の自動要約
- Bare startup mode（軽量起動）
- ループ検出強化（ツール呼び出し無限ループ防止）

> **出典**: [Qwen Code 週報 (2026-04-23)](https://qwenlm.github.io/qwen-code-docs/zh/blog/weekly-update-2026-04-23/) [T1]

## Qwenの中国AIエコシステムでの位置づけ

|| 次元 | Qwen | 競合 ||------|------|------|| 開発元 | 阿里巴巴 | 智谱AI（[[glm-zhipu]]）、月之暗面（[[kimi-moonshot]]） || OSS方針 | 全面オープンソース（Apache 2.0） | GLM一部OSS、Kimiクローズド || 企業級呼び出しシェア | **第1位（32.1%）** | 第2位以下 || エンタープライズ統合 | 阿里云Model Studio・钉钉・ERP | 他社は提携関係 || コーディング | Qwen3-Coder（480B MoE） | Kimi K2.6、GLM-5.1 || 価格競争 | Qwen3-Max 50%値下げ | 各社価格破壊競争 |

## AIスーパーアプリ競争 (ChinAI #345)

AlibabaはQwenを中核とした**フルスタックAI戦略**を展開：

- **モデル**: Qwenシリーズ（オープンソース最強力）
- **インフラ**: Alibaba Cloud（中国クラウドシェア1位）+ Zhenwu AIチップ
- **エコシステム**: Taobao/Tmall（EC）、Alipay（決済）、Ele.me（配達）、钉钉（エンタープライズ）
- **戦略**: モデル→クラウド→アプリケーションの垂直統合
- **優位性**: 自社モデル＋自社クラウド＋巨大エコシステム＋自社シリコン
- **課題**: ユーザーエンゲージメントでByteDanceに劣る

### 3Way競争

|| 企業 | AIモデル | エコシステム | 課題 ||------|---------|-------------|------|| Alibaba/Qwen | 自社開発（最強） | EC+クラウド+決済+チップ | ユーザー時間 || ByteDance/Doubao | 移行中 | コンテンツ+推薦 | モデル技術 || Tencent | 追従中 | WeChat（最大） | AI人材・技術 |

## 具身ロボティクスへの進出（2026年4月19日）

阿里巴巴のAmap（高德地图）が北京Humanoid Robot Half Marathonで**初の人型ロボット**をデビュー。四足ロボットはAmapの新embodied-intelligence部門が開発し、Alibabaの**ABot-Worldモデル**（AGIbot World ChallengeおよびWorld Arenaベンチマーク首位）で駆動。これによりQwenは基盤モデルから**自法人型ロボット**への拡張を示した。

## 中国開発者コミュニティでの議論

### V2EX
- 「阿里云的Qwen生态，到底能不能打？」— Qwenエコシステムの実力評価
- Qwen3.6-Max-Previewのpreserve_thinking機能に関する議論
- Qwen3.6-35B-A3Bのローカルデプロイ体験（Ollama・vLLM）
- Zhenwuチップ実装と中国AI自立戦略に関する議論

### 掘金
- Qwen3-Coder vs Claude Codeのコーディング比較
- Qwen3.6 Plusのagentic coding実装ガイド
- Qwen3.6-27Bのベンチマーク分析（dense vs MoE）

### 36kr
- Qwenが企業級大モデル呼び出し量第1位獲得の分析
- 50%値下げが中国AI価格戦争に与える影響
- Qwen3.6-Max-Previewの五大核心 upgrades解説
- Alibabaの$69B AI投資戦略分析

### WeChat機器之心
- Qwen3.6 Plusのアーキテクチャ解説（線形注意＋MoEハイブリッド）
- Qwen3.6-27BのGated DeltaNet技術分析
- ABot-Worldロボティクスモデルの展望
- Zhenwuチップと中国电信のデータセンター連携

## 関連リンク

### 内部リンク

- [[claude-code]] — コーディングエージェントとしての競合
- [[coding-plan]] — Qwenがバンドルされるサブスクリプション
- [[glm-zhipu]] — 中国OSS LLM競合
- [[kimi-moonshot]] — 中国代替モデル
- [[openclaw]] — 阿里云統合パートナー
- [[china-ai-agent-ecosystem]] — 中国AI Agentエコシステム全体
- [[vibe-coding-china]] — Vibe CodingとQwenのコーディング競争
- [[alibaba-cloud]] — Alibaba Cloudインフラの詳細

### 外部ソース

|| ソース | URL | ティア | 概要 ||---|---|---|---|| 新浪 — Qwen3.6-Max-Preview | [sina.cn/news/5289894780869670](https://www.sina.cn/news/detail/5289894780869670.html) | T1 | 五大核心升级 || MarkTechPost — Qwen3.6-27B | [marktechpost.com/...](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/) | T1 | 密型Agentic Codingモデル || Aipedia — Qwenレビュー | [aipedia.wiki/tools/qwen](https://aipedia.wiki/tools/qwen/) | T2 | 2026年4月時点完全レビュー || Yahoo Finance — 企業戦略 | [finance.yahoo.com/...](https://finance.yahoo.com/markets/stocks/articles/alibaba-qwen3-6-plus-targets-070714378.html) | T2 | エンタープライズ向け戦略分析 || Bitget — AIインフラ戦略 | [bitget.com/news/...](https://www.bitget.com/news/detail/12560605360273) | T2 | S字カーブ投資分析 || Simply Wall St — Zhenwuクラスター | [simplywall.st/...](https://simplywall.st/stocks/us/retail/nyse-baba/alibaba-group-holding/news/will-alibabas-new-zhenwu-powered-qwen36-plus-ai-cluster-chan) | T2 | 3800億元投資計画 || Silicon Report — Zhenwuデプロイ | [siliconreport.com/...](https://www.siliconreport.com/alibaba-and-china-telecom-put-zhenwu-into-production-with-a-10-000-chip-ai-data-center-in--bee7425e2315a778) | T2 | 10,000チップ実装 |
