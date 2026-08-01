---
title: Qwen（通义千问）— 阿里云大模型旗舰
created: 2026-04-17
updated: 2026-08-01
tags: [llm, model, china, open-source-ai, alibaba, qwen, agentic-coding, ai-infrastructure, qwen3.7, qwen3.8, agent-era, qwen-image-3, tts]
aliases: ["Qwen", "通义千问", "qwen", "Qwen3.5", "Qwen3-Coder", "Qwen3.6", "Qwen3.6-Plus", "Qwen3.6-27B", "Qwen3.6-35B-A3B", "Qwen3.7-Max", "Qwen3.7-Plus", "Qwen3.8-Max", "千问云", "Qianwen Cloud", "千問办公"]
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

## 2026年5月中旬の動向

### 千问×淘宝全面打通 — AI Shopping（2026年5月11日）

2026年5月11日、AlibabaはQwenと淘宝（Taobao）の深層統合を完了。**世界初のトップAIアプリと超規模ECプラットフォームの深層統合**として報じられた。

| 連携範囲 | 内容 |
|---------|------|
| **事前購買** | ニーズ明確化・条件フィルタリング・あいまい記述マッチング・シーンプランニング |
| **購買実行** | AIアシスタント内でワンクリック注文 |
| **事後** | 注文追跡・アフターサービス連携 |

これによりQwenはフライ帰り・AutoNavi・Alipayに続く「消費エコシステムの最後のピース」を獲得。フルスタックAI戦略のEC応用として重要なマイルストーンとなった。

> **出典**: 海克财经 via Sina Finance 2026.05.15 [Tier-1]

### Qwen Code v0.15.10–v0.15.11（2026年5月10–13日）

Qwen Code CLIが継続的にアップデートを実施：

| 日付 | 主要アップデート |
|------|----------------|
| **5月10日** | セッションリストメタデータ最適化、バッファプーリング、CLI i18nカバレッジ、telemetry tracing |
| **5月11日** | `--json-schema`構造化出力、codegraph skill（PRレビューリスク分析）、Ink 7.0.2アップグレード、Anthropicプロキシ互換 |
| **5月12日** | Tool Searchプレフィックスキャッシング、DASHSCOPE_PROXY_BASE_URLサポート、GitHub Actions Node 24アップグレード |
| **5月13日** | v0.15.11正式タグリリース |
|
|> **出典**: [GitHub QwenLM/qwen-code v0.15.10…v0.15.11](https://github.com/QwenLM/qwen-code/compare/v0.15.10...v0.15.11) [T1]
|
|### Qwen Code v0.16.0 — OSC 8リンク・Worktree隔離・qwen serveデーモン（2026年5月21日）
|
|2026年5月21日、Qwen Code v0.16.0がリリース。v0.15.xシリーズからの大規模アップデートで**80+のPR**を含む。GitHub Starsは25Kに到達。
|
|**主な新機能（v0.16.0, 2026年5月21日）**:
|
|1. **OSC 8ハイパーリンク**: マークダウンリンクがターミナルでクリック可能に
|2. **Worktree隔離（EnterWorktree/ExitWorktree）**: Agent作業を分離された独立ワークツリーで実行、Agent間の干渉防止
|3. **qwen serveデーモン（Stage 1）**: バックグラウンドサーバーモード、`/demo`デバッグページ付き
|4. **/goalコマンド**: セッションスコープの目標設定とjudge駆動の継続実行
|5. **/diff per-turn**: 各ターンの変更差分を対話的に確認
|6. **/stuck診断スキル**: フリーズしたセッションを診断・回復
|7. **/rewindファイル復元**: ファイル単位の巻き戻しサポート
|8. **Auto承認モード（LLM分類器）**: 低リスク操作をAIが自動承認
|9. **NotebookEditツール**: Jupyterノートブックの直接編集
|10. **ステータスラインプリセット**: 対話式のUI設定ダイアログ
|11. **ModelScope内蔵サードパーティAPIプロバイダー**: DashScopeに加えてModelScopeも選択可能に
|12. **プログレッシブMCP**: MCP初期化が初回入力をブロックしなくなった
|13. **バッチセッション削除**: `/delete`で複数セッションを一括削除
|14. **フォークセッション再開フラグ**: Forkしたセッションを`--resume`で再開可能
|15. **Ink 6→7.0.3アップグレード**: レンダリングパイプライン刷新
|16. **Qwen3.6-35B-A3B量子化版の画像+動画サポート**
|17. **Anthropic cache_control on tool_result blocks**
|
|**Telemetry Phase 2-4a**: TTFT（Time To First Token）取得、トレースツリー階層化、カスタムリソース属性、メトリックカーディナリティ制御。
|
**v0.16.1 ホットフィックス（2026年5月23日）**:
- Windows Git Bash（MinTTY）のUIレンダリング問題を修正 — OSC 8検出をmintty v3.3以上にゲート
- tool_use↔tool_result不変条件の全障害パスでの修正
- タブインデントされたノートブック書式を保持
- React reconciler dev buildのPerformanceMeasureリークを防止
- Express 4.21.2→5.2.1に依存関係更新

**v0.16.2 リリース（2026年5月27日）**:
- `fix(build)`: ビルド前の古い出力をクリーンしてTS5055エラーを防止
- `fix(cli)`: ディレクトリ補完時に末尾スペースを追加しないよう修正（#4092/#4288）
- Nightlyビルド v0.16.1-nightly.20260527.641a1a739（5/27）→ v0.16.1-nightly.20260528.34b7d472e（5/28）が継続配信
- GitHub Stars: **~25K**、コントリビューター: 410名

**Qwen Code v0.17.0-preview.0（2026年5月29日）**:
- プレビューリリースとして公開。次期メジャーバージョンに向けた基盤整備。

**Qwen Code 週報 5/28（2026年5月28日）**:
- `/goal`コマンドによるエージェント完了維持戦略
- `/branch`並列探索機能
- Tool Search prefixキャッシングの最適化
- 背景タスクパネル、会話巻き戻し、コスト見積もり機能の強化

> **出典**: [GitHub QwenLM/qwen-code v0.16.2](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.2), [GitHub QwenLM/qwen-code v0.16.1-preview.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.1-preview.0), [Qwen Code Blog 5/28](https://qwenlm.github.io/qwen-code-docs/en/blog/), [Qwen Code Blog 5/14](https://qwenlm.github.io/qwen-code-docs/en/blog/) [T1]

### Qwen Deep Research 正式稼働中

QwenChat上で「Deep Research（深入研究）」機能が稼働中。複数ステップのWeb検索・分析計画・包括レポート生成を自動実行。Qwenの推論・Agent・長コンテキスト・RL能力を統合し、**全ユーザーに無料提供**。

> **出典**: 腾讯云开发者社区 2026.05.14 [Tier-2]

### Qwen「考えすぎ」バグ報告（2026年5月12日）

コミュニティテストにより、QWQ・Qwen3.6推論モデルが無限思考ループに陥る「overthinking（過剰思考）」バグが報告された。GSM8K・HotpotQAで特に顕著。Llama 3.3-70Bでは同症状が確認されず、Qwenの推論チェーン設計に固有の問題とみられる。

> **出典**: 80aj.com 2026.05.12 [Tier-3]

### ベンチマーク最新動向

| 指標 | スコア | 順位 |
|------|--------|------|
| AA Intelligence Index v4.0 | **52点** | 203モデル中**3位**（GPT-5.4 58点, Claude Opus 4.7 56点） |
| Qwen3.6-Max SWE-bench Pro | — | 4月下旬首位 → Claude Mythos(77.8%)に抜かれる |
| Qwen3.6-Max Terminal-Bench 2.0 | 65.4% | Claude Opus 4.7と**同位** |
| QwenWebBench ELO | **1,558** | Claude Opus 4.5(1,182)を大きくリード — Alibabaが正当に首位を主張できる領域 |

## 2026年5月下旬の動向

### Qwen3.7-Max — Agent-firstフラッグシップ正式発表（2026年5月20日）

2026年5月20日、Alibaba Cloud Summit（杭州）で**Qwen3.7-Max**が正式発表された。同日、Qwen3.7-Plus-Previewも同時発表。

| 項目 | Qwen3.7-Max | Qwen3.7-Plus-Preview |
|------|------------|---------------------|
| **発表日** | 2026-05-20（Alibaba Cloud Summit） | 2026-05-20 |
| **プレビュー先行公開** | 5月18〜19日（Qwen Chat / Arena AI） | 同時 |
| **設計思想** | **Agent-first** — 継続的・多段階自律エージェント向け | 均衡型（推論＋マルチモーダル） |
| **コンテキスト** | 256K | 1M tokens |
| **ライセンス** | クローズドウェイト（API専用） | Plus版は後日Apache 2.0 OSS予定 |
| **価格** | — | ¥2/100万トークン〜 |

**衝撃の自律実行デモ**:
- 未学習の**平頭哥真武M890チップ**上で35時間連続稼働
- **1,158回**のツールコール、**432回**のカーネル評価
- 公式SGLang Triton実装比**10倍の推論速度向上**

**ベンチマーク成績**:
| ベンチマーク | スコア | 評価 |
|-------------|--------|------|
| Arena総合テキスト | **#13位** | 国内モデル最高位 |
| Terminal-Bench 2.0-Terminus | **69.7点** | DeepSeek-V4-Pro-Max、Claude Opus 4.6超え |
| MCP-Atlas / MCP-Mark / Skillbench | **首位** | GLM-5.1、Kimi-K2.6超え |
| GPQA Diamond / HLE / HMMT 2026 Feb | **Opus 4.6超え** | 科学的推論でリード |
| IFBench | **79.1点** | 新記録 |

| **対応エージェントハーネス**: OpenClaw、Hermes Agent、Claude Code、Qwen Paw、Qoder最適化。
|
|| ベンチマーク | スコア | 評価 |
||-------------|--------|------|
|| AA Intelligence Index | **56.6**（全球5位/国産1位） | Gemini 3.5 Flash(55.3)を超越 |
|| Terminal-Bench 2.0 Hard | **50.8%（+6.9）** | DeepSeek-V4-Pro-Max、Claude Opus 4.6超え |
|| MCP-Atlas | **76.4** | Opus-4.6(75.8)超え |
|| Skillsbench | **59.2** | Kimi K2.6(56.2)超え |
|| MCP-Mark | **60.8** | GLM-5.1(57.5)超え |
|| BFCL-V4 | **75.0** | 関数呼び出しでリード |
|| SpreadSheetBench-v1 | **87** | オフィス自動化トップ |
|| Kernel Bench L3 | **1.98x 中央値** | 96%勝率、GPUカーネル最適化 |
|
|**35時間自律実行の詳細**: 平頭哥真武M890 PPU上のExtend Attentionカーネルを自動最適化。1,158回ツールコール、432回カーネル評価、5種アーキテクチャ案を反復生成。Triton参照実装比**10倍の幾何平均高速化**。Firetheringの分析（5/25）では、GLM 5.1（7.3x）、Kimi K2.6（5x）、DeepSeek V4 Pro（3.3x）を上回ったと報告。
|
|### Qwen3.7-Max API正式公開（2026年5月21日〜23日）
|
|2026年5月21日より、Qwen3.7-MaxのAPIが順次公開開始された。
|
|| プロバイダー | 入力価格 | 出力価格 | キャッシュ入力 |
||------------|---------|---------|-------------|
|| **Alibaba Cloud Model Studio** | ¥12/百万 tokens（~$1.71） | ¥36/百万 tokens（~$5.14） | ¥1.2/百万 tokens（90%割引） |
|| **OpenRouter** | $2.50/百万 tokens | $7.50/百万 tokens | $0.25/百万 tokens（90%割引） |
|| **API易 (官転直連)** | $1.7140/百万 tokens | $5.1420/百万 tokens | — |
|
|**API仕様の特徴**:
|- **OpenAI互換**: `openai`ライブラリで呼び出し可能（model ID: `qwen3.7-max`）
|- **Anthropic Messages Protocol対応**: ネイティブサポート — Claude Code・OpenClawがそのまま動作。`ANTHROPIC_BASE_URL`を切り替えるだけでQwen3.7-Maxをバックエンドに指定可能
|- **1Mトークンコンテキスト**（256K→1Mに倍増）、**65,536最大出力トークン**
|- **明示的プロンプトキャッシング**: 繰り返しコンテキストで効率的なキャッシュ利用
|- **2種類のAPI Key**: `sk-`（標準API）と`sk-sp-`（Token Plan専用）。別のBase URLを使用
|
|**主要連携**:
|OpenRouter（5/21）、ofox.ai（5/21）、Vercel AI Gateway（5/21）、Together AI — 各社がQwen3.7-Maxのルーティングを開始。ofox.aiでは`bailian/qwen3.7-max`として提供。
|
|> **出典**: OpenRouter Qwen3.7-Max ページ [(link)](https://openrouter.ai/qwen/qwen3.7-max), ofox.ai Developer Guide [(link)](https://ofox.ai/blog/qwen3-7-max-developer-guide-2026/) [T1]
|
### Qwen3.7-Max Qwen Chat統合（2026年5月22日）

2026年5月22日、Qwen3.7-Maxが**千問App v6.9.7+、PCクライアント、Web版**に正式統合された。全ユーザーに無料開放。

- Artificial Analysis Intelligence Index：**56.6点**（全球5位、国産1位）を正式発表
- GPQA Diamond・HLE・HMMT 2026 Feb・IMOAnswerBenchでClaude Opus 4.6および全中国モデルを超過
- IFBench指令遵循：**79.1点**
- **Token効率31%改善**: 同一問題に対する出力トークン増加は推論密度向上によるもの

> **出典**: [中关村在线](https://ai.zol.com.cn/1185/11851769.html) [T1], [新浪新闻](https://www.sina.cn/news/detail/5301737230701416.html) [T2]

### Qwen3.7-Max — 35時間自律カーネル最適化実験の詳細（Firethering分析）

Firethering（5/25）および複数の海外メディアがQwen3.7-Maxの**35時間自律実行実験**を詳細に分析：

- **タスク**: T-Head ZW-M890 PPU（平頭哥真武M890）上のExtend Attentionカーネルの最適化
- **前提条件**: モデルはこのハードウェアを訓練中に**一度も見ていない**。ドキュメント・プロファイリングデータ・サンプルカーネル一切なし。タスク説明・既存SGLang実装・評価スクリプトのみ提供
- **実行内容**: 35時間連続、1,158回ツールコール、432回カーネル評価
- **5段階の最適化プロセス**:
  1. Split-K partitioningでprefix KV-cacheをトークン次元に分割し、36個SMコアを全て活用
  2. 同期`cudaMalloc`を事前割り当てPyTorch変数に置換
  3. プレフィックス長照会用の同期`cudaMemcpy`をtensor metadata使用で除去
  4. ホスト-デバイス通信オーバーヘッドを完全排除
  5. 演算子を再構築し、4つのクエリトークンを1つのスレッドブロックで処理（メモリアクセスオーバーヘッド分散）
- **結果**: Triton参照実装比**10.0x幾何平均高速化**
- **他モデルとの比較**:
  | モデル | 高速化倍率 | 備考 |
  |--------|-----------|------|
  | **Qwen3.7-Max** | **10.0x** | 35時間完遂 |
  | GLM 5.1 | 7.3x | — |
  | Kimi K2.6 | 5.0x | — |
  | DeepSeek V4 Pro | 3.3x | 早期終了 |
  | Qwen3.6-Plus | 1.1x | 早期終了 |

- **KernelBench L3**: 96%のシナリオで加速カーネル生成（Opus 4.6: 98%、GLM 5.1: 78%、Kimi K2.6: 80%、DeepSeek V4 Pro: 54%）

> **出典**: [Firethering — Qwen3.7-Max 35-Hour Autonomous Run](https://firethering.com/alibaba-qwen3-7-max-autonomous-agent/) [T1], [TestingCatalog — Qwen3.7-Max Autonomously Wrote 1,158 Lines of Code](https://testingcatalog.net/qwen3-7-max-autonomously-wrote-1158-lines-of-code-to-10x-chinese-chip-performance/) [T2], [TheDecoder](https://the-decoder.com/alibabas-latest-ai-model-ran-autonomously-for-35-hours-to-optimize-code-for-its-own-custom-chip/) [T2], [VentureBeat](https://venturebeat.com/technology/alibabas-proprietary-qwen3-7-max-can-run-for-35-hours-autonomously-and-supports-external-harnesses-like-anthropics-claude-code) [T1]

### Qwen3.7-Max — OpenRouter API使用量とベンチマーク詳細

OpenRouter上でのQwen3.7-Max API使用動向（5/21〜5/29）:

- **日次トークン使用量**: 5/21の10.3B（103億）トークンから始まり、5/29時点で累計**226M+ prompt tokens**、**91.9M+ reasoning tokens**を記録
- **利用傾向**: 日々増加傾向 — Agent開発者・コスト重視のAPIユーザーからの採用が拡大
- **価格比較（$/1M tokens）**:
  | モデル | 入力 | 出力 | コンテキスト |
  |--------|------|------|------------|
  | **Qwen3.7-Max** | **$2.50** | **$7.50** | **1M** |
  | GPT-5.5 | $5.00 | $30.00 | 1M |
  | Claude Opus 4.7 | $5.00 | $25.00 | 1M |
  | Gemini 3.5 Flash | $1.50 | $9.00 | 1M |
  | DeepSeek V4 Pro | $1.74 | $3.48 | 1M |

- **キャッシュ90%割引**: $0.25/M入力（エージェントの繰り返しコンテキスト読み取りに最適）
- **BenchLM.ai暫定リーダーボード**: 92/100で**117モデル中#3**、検証済みリーダーボードで**25モデル中#2**
- **カテゴリ別ランク**: Coding **#4**、Reasoning 96.4、Agentic 87.7、Knowledge 86.8、Multilingual #10
- **LMSYS Chatbot Arena**: Text Overall 1475（±10.0）、3,741 votes; Coding 1525（±18.4）、1,135 votes

- **留意点（Hallucination/Abstention）**: OfficeChaiの分析によると、Qwen3.7-Maxの回答試行率は**48.0%**と類似frontierモデル中最低。高い棄却率によりhallucinationスコアが改善している側面あり。Agentが曖昧なケースをpush throughする必要があるワークロードでは注意が必要。

> **出典**: [OpenRouter — Qwen3.7-Max](https://openrouter.ai/qwen/qwen3.7-max) [T1], [BenchLM.ai](https://benchlm.ai/models/qwen3-7-max) [T2], [Fello AI — Qwen3.7-Max Review](https://felloai.com/cs/qwen-3-7-max-review/) [T2], [DataCamp — Qwen3.7-Max Features, Benchmarks](https://www.datacamp.com/blog/qwen3-7-max) [T2], [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/05/qwen3-7-max/) [T2]

> **出典**: [Alibaba Cloud Blog — Alibaba Unveils New AI Chip](https://www.alibabacloud.com/blog/alibaba-unveils-new-ai-chip-flagship-model-and-rebuilt-cloud-stack-ai-for-agentic-era_603151), [新浪科技](https://finance.sina.com.cn/tech/roll/2026-05-20/doc-inhyphnp1790590.shtml), [CnTechPost](https://cntechpost.com/2026/05/19/alibaba-hints-qwen3-7-ai-model-launch-step-up-ai-race/)

### Qwen3.7-Max 無料化 — Qwen Chatでの完全無料提供開始（2026年6月1日）

2026年6月1日、Qwen3.7-Maxが**Qwen Chat（千问App）**で完全無料化された。5月下旬の公開当初、API・サブスクリプションともに高額（¥198〜/月のToken Plan、API $2.50/M入力）で「Qwen3.7Max 测了一波有点用不起啊」（5月29日、甲维斯）とコミュニティでコスト批判が相次いだことを受け、Alibabaは無料提供に舵を切った。

- **背景**: 5月29日〜31日にかけて掘金で「Qwen3.7Max 测了一波有点用不起啊」が話題に。「能力向上は明らかだが、高すぎる」との批判が多数
- **6月1日発表**: 甲维斯が掘金で「免费的Qwen3.7max终于来了！」を公開 — スコア16、⭐20と高いエンゲージメントを記録
- **影響範囲**: Qwen Chat（千问App v6.9.7+、PCクライアント、Web版）で全ユーザーが無料利用可能。API・Token Planは従来通り有料
- **コミュニティ反響**: 6月2日〜4日まで継続的に掘金で同記事が再掲載され、継続的な話題に

> **出典**: [掘金 — 免费的Qwen3.7max终于来了！(6/1)](https://juejin.cn/post/7646234722919170088) [T1], [掘金 — Qwen3.7Max 测了一波有点用不起啊(5/29)](https://juejin.cn/post/7644794219849744394) [T1]

### QwenPaw — オープンソース個人AIアシスタント（2026年5月30日）

2026年5月30日、掘金で**QwenPaw（Qwen Personal Agent Workstation）**のソースコード学習ガイドが公開された。AgentScopeチームが開発・メンテナンスするオープンソース個人AIアシスタントプラットフォーム。

- **旧称**: CoPaw
- **開発元**: AgentScopeチーム
- **機能**: 個人AIアシスタント（エージェント基盤）

> **出典**: [掘金 — QwenPaw 源码学习指南(5/30)](https://juejin.cn/post/7645237921839874098) [T1]

### オープンソースエコシステムの拡大（2026年6月2日）

#### funyi — Qwen3-ASRベースのリアルタイム字幕ツール

2026年6月2日、V2EXユーザーkvlが**funyi**をオープンソース公開。Qwen3-ASR-1.7Bを音声認識エンジンとして使用するローカルリアルタイム字幕ツール。

- **ASRエンジン**: Qwen3-ASR-1.7B（完全ローカル推論、オフライン可）
- **翻訳**: Hy-MT2-1.8B
- **クライアント**: Tauri製デスクトップアプリ（Windows/macOS）
- **サーバー**: Linux/WSL + NVIDIA CUDA GPU
- **パフォーマンス**: RTX 4090上で**500ms**の低遅延リアルタイム表示
- **GitHub**: [github.com/vauxe/funyi](https://github.com/vauxe/funyi)
- **用途**: ライブ配信、動画視聴、会議のリアルタイム字幕

> **出典**: [V2EX — 写了一个本地模型的实时字幕工具(6/2)](https://www.v2ex.com/t/1217448) [T1]

#### DocPilot Qwen — Android向けドキュメントAIアシスタント

同日、掘金で**DocPilot Qwen**がオープンソース公開された。Qwenをバックエンドに使用したAndroid向けドキュメントAIアシスタント。

- **機能**: ドキュメント取込・解析・AI質問応答・要約生成・テンプレート抽出・ローカル記録管理
- **用途**: スマートフォンでの学習資料整理、論文読解
- **ターゲット**: Androidモバイルユーザー

> **出典**: [掘金 — DocPilot Qwen正式开源(6/2)](https://juejin.cn/post/7646593427816693770) [T1]

### Qwen3.7-Max エコシステム展開まとめ（2026年5月下旬〜6月）

| 日付 | 出来事 | ソース |
|------|--------|--------|
| 5/29 | Qwen3.7Max高コスト批判が掘金で話題に | 掘金 |
| 5/30 | QwenPaw学習ガイド公開 | 掘金 |
| 6/1 | Qwen3.7-Max Qwen Chatで無料化 | 掘金 |
| 6/2 | funyi字幕ツール（Qwen3-ASR）公開 | V2EX |
| 6/2 | DocPilot QwenドキュメントAI公開 | 掘金 |

## 2026年6月6日〜11日の動向

### Meta VLM³ — Qwen3-VL-4Bを基盤とした3D視覚研究（2026年6月8日）

2026年6月8日、Metaが発表した研究論文 **VLM³（Visual Language Model 3D）** が36krで報じられた。Qwen3-VL-4Bをベースモデルとして採用し、視覚モデルが本来3Dを学習する能力を持つことを実証。深度推定精度が**0.9**に到達した。

- **基盤モデル**: Qwen3-VL-4B（4BパラメータVision-Language Model）
- **手法**: マルチタスク統一モデリング — 同一アーキテクチャで深度推定・三次元再構成・視覚エンティティ認識を統合
- **成果**: 深度推定（depth estimation）で90%精度を達成
- **意義**: Meta（米国大手テック）がQwenモデルを研究基盤として採用した珍しい事例。Qwen3-VLの性能が国際的にも認知されていることを示す

> **出典**: [36kr — Meta VLM³](https://36kr.com/p/3844230320933378) [T1]

### QwenPaw 記憶対話管理アーキテクチャ解説（2026年6月7日）

2026年6月7日、掘金で「QwenPaw 记忆与对话管理架构」と題する技術解説記事が公開された。AgentScopeチームが開発するQwenPawの内部アーキテクチャを詳細に分析。

- **テーマ**: QwenPawの記憶管理・会話管理・エージェント間通信の設計
- **コミュニティ反響**: QwenPawが単なるツールではなく、Agent開発基盤としての関心が高まっている

> **出典**: [掘金 — QwenPaw记忆与对话管理架构](https://juejin.cn/post/7647882996956823606) [T1]

### 千問3.6の0コスト活用チュートリアル（2026年6月7日・9日）

掘金で「保姆级教程：如何0成本调用千问3.6大模型？讯飞星辰MaaS平台上手指南」が公開され、連続的に拡散（6月7日・9日）。讯飞星辰MaaSプラットフォーム上でQwen3.6を無料で呼び出す方法を解説。Qwenモデルの中国開発者コミュニティでの普及が継続。

> **出典**: [掘金 — 0成本调用千问3.6](https://juejin.cn/post/7648157267778486287) [T1]

### Qwen3.6-27B vs DeepSeek V4 Flash比較議論（2026年6月7日）

V2EXで「deepseek v4 flash 和本地部署 Qwen3.6-27B-MTP-GGUF Q4_K_M 哪个更强？」とのスレッドが投稿。ローカルデプロイ環境での実用的なモデル選択の観点から両モデルを比較。コミュニティの関心がハイエンドモデルから実用・ローカル実行可能な中小規模モデルへシフトしている傾向を示す。

> **出典**: [V2EX — Qwen3.6-27B vs DeepSeek V4 Flash](https://www.v2ex.com/t/1218583) [T1]

### Qwen Code v0.17.x — プレビュー以降の動向

Qwen Code v0.17.0-preview.0（2026年5月29日）以降、**6月11日時点で新たな正式リリースは確認されていない**。v0.17.x系統は現在プレビュー段階で、次期メジャーバージョン（v0.17.0正式版 or v0.18.0）に向けた開発が継続中と推定される。

### Qwen3.7-Max — 無料化後のコミュニティ反響

Qwen3.7-Maxが6月1日にQwen Chatで無料化されて以降、コミュニティでの話題は以下の傾向：
- **ポジティブ**: 無料で利用可能な高品質モデルとして評価
- **API課金は依然高額**: Token Plan（¥198/月〜）やAPI従量課金のコスト懸念は継続
- **競合製品の台頭**: Claude Fable 5 / Mythos 5（6月9-10日発表）やGPT-5.6の登場により、ベンチマーク競争が再激化

### 総評：2026年6月上旬のQwenエコシステム

| 領域 | 評価 |
|------|------|
| **モデル** | Qwen3.7-Max無料化によりユーザー基盤拡大。Meta VLM³での採用が国際的認知を示す |
| **Qwen Code** | v0.17.0-preview.0以降、6月前半は安定開発期。新リリースなし |
| **千問云** | シンガポール公開後、海外展開の初期フェーズ。新たな導入事例は6月前半には確認されず |
| **Qoder CN** | ブランド変更完了後、価格体系・機能面での大きな動きなし |
| **コミュニティ** | 実用・ローカルデプロイ関心が高まる（Qwen3.6-27B、Xunfei連携）|



- **公式モデルID**: `qwen3.5-livetranslate-flash-realtime-2026-05-19`
- **基盤**: Qwen3.5-Omniベース
- **対応言語**: **60入力言語**（うち29言語で音声出力対応）
- **遅延**: **2.8秒**（Qwen3版の3秒から改善）
- **ビジョン強化**: 口の動き・ジェスチャー・画面テキスト読み取りで翻訳精度向上
- **リアルタイム声クローン**: 1文の発話で話者の声プロファイルを再現
- **セマンティック単位予測**（Reading Units）による連続ストリーミング出力
- **動的キーワード設定**: ドメイン固有辞書をランタイム注入可能
- **API専用**（WebSocketベース、DashScope API経由）

> **出典**: [Qwen Changelog](https://docs.qwencloud.com/changelog/models), [MarkTechPost](https://www.marktechpost.com/2026/05/20/alibaba-qwen-team-introduces-qwen3-5-livetranslate-flash-real-time-multimodal-interpretation-across-60-languages-at-2-8-second-latency/)

### Qoder 1.0 — 自律開発デスクトップへ進化（2026年5月15日）

AlibabaのAI IDE「Qoder」がv1.0に到達し、**自律開発デスクトップ（Autonomous Development Desktop）**へ進化：

| 新機能 | 説明 |
|--------|------|
| **チーム知識共有エンジン**（世界初） | 分散メモリ・Wiki・知識カードを統合。コード保持率+11%、入力Token消費-40%、対話数-33% |
| **Expertsモード** | カスタマイズ可能なエージェントチーム作成（ドメイン知識・タスクスキル・外部ツール設定） |
| **クロスプロジェクトマルチタスク** | 複数プロジェクトのエージェントタスクを統合パネルから同時実行 |
| **Quest機能進化** | 単一モードから独立ウィンドウシステムへ。タスク管理・ステータス追跡・成果レビュー・知識検索を統合 |

- **グローバルユーザー**: 500万人超（2025年8月ローンチ以来）
- **位置づけ**: Qwen-Coder-Qoderモデル（強化学習特化）搭載、Cursor Composer対抗

> **出典**: [CnTechPost](https://cntechpost.com/2026/05/15/alibaba-launches-qoder-1-0-to-automate-software-development-ai-agents/), [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/16/3296208/0/en/Qoder-Version-1-0-Released-Full-Automation-of-Code-Generation-Verification-Delivery.html)

### 通义灵码→Qoder CN 正式更名（2026年5月20日）

2026年5月20日23時（北京時間）、阿里云旗下智能编码助手**「通义灵码」**が**「Qoder CN」**に正式更名。同時に**Lingma**から**Qoder CN**へ英語名称も変更。これにより、Qoder CNはQoderグローバル製品の中国版シリーズに正式に統合された。

**更名の詳細**:
- **旧名称**: 智能编码助手通义灵码（Lingma）
- **新名称**: Qoder CN（Qoder CNシリーズ中面向软件开发场景的核心子产品）
- **运营主体**: 浙江阿里巴巴云计算有限公司（グローバル版Qoderの运营主体はシンガポールのBright Zenith Private Limited）
- **製品形態**: IDE、JetBrainsプラグイン、VS Codeプラグイン、QoderWork CN（デスクトップ）、Qoder CLI CN（ターミナル）

**価格改定（2026年5月20日23時以降の新規契約）**:

| バージョン | 旧価格 | 新価格 | Credits/月 | 変更率 |
|-----------|--------|--------|-----------|--------|
| 個人基礎版 | 無料 | 無料 | 限定 | — |
| 個人専門版 | 無料（限時）→59元/月 | 59元/月 | 2,000 | 新規有償化 |
| 企業標準版 | 79元/席/月 | 99元/席/月 | 3,000 | +25.3% |
| 企業専属版(VPC) | 159元/席/月 | 199元/席/月 | 3,000 | +25.2% |

**Creditsメカニズム**:
- 2026年5月20日よりサブスクリプション席位にCredits制を導入
- 超额时可增购リソース包
- 存続契約は契約満了まで旧価格適用
- 個人専門版の限時無料活動は5月20日18時に終了
- 2026年7月にQoder CNとQoderWork CNのCredits共有を予定

**モデル対応の拡大**:
- 旧来: Qwenモデル中心
- 新規: GLM、DeepSeek、Kimi、MiniMax等多モデル対応
- Qwen-Coder-Qoderモデル搭載（Qwen-Coderベースの強化学習特化モデル）

> **出典**: [163新闻 — 通义灵码更名Qoder CN](https://www.163.com/dy/article/KTHN7OVM05118UGR.html) [T1], [阿里云帮助文档 — Qoder CN产品概述](https://help.aliyun.com/zh/lingma/qoder-cn/product-overview/what-is-xx) [T1], [阿里云帮助文档 — 计费说明](https://help.aliyun.com/zh/lingma/product-overview/billing-description) [T1], [AtomGit — Qoder CN更名分析](https://gitcode.csdn.net/6a0da7ba662f9a54cb75e79e.html) [T2]

### Qwen Cloud 新加坡海外版公開（2026年5月26日）

2026年5月26日、阿里云は新加坡で**Qwen Cloud**（千问云の海外版）を正式に公開。海外市場向けにAgent時代のクラウド製品新入口を展開。

**海外版の特徴**:
- **三入口設計**:
  1. **Website**: 開発者がモデルを閲覧・試用・比較し、OpenAI互換APIに接続
  2. **Skills**: プラットフォーム能力をAgent可読な標準化指令にカプセル化
  3. **CLI**: 開発者と智能体向けの安定したコマンドライン操作層
- **Token Plan**: 月額定額制。マルチモーダル（テキスト・画像・音声）対応。超過時は従量課金に自動切り替え
- **エンタープライズ機能**: ワークスペース分離、細粒度権限管理、レート制限、APIキー管理、透明な請求
- **マルチモデル**: Qwen、GLM、Kimi、DeepSeek等150+モデルシリーズ、480+モデル

**阿里云CTO李飛飛の発言**:
> 「海外市場のAI需要は持続的に旺盛。特にAgentの爆発によりモデル呼び出し量とクラウドリソース消費が指数級的に増加。阿里云は海外向けに全スタックアップグレードを展開中 — モデル、入口、Agent製品、クラウドインフラをカバー」

**戦略的意義**:
- 「未来にモデルを使用する主力はAgentになる」という判断のもと、従来の人間向けUI・プロセス・インタラクションロジックを全面的に書き換え
- Agentワークロードは「無規律弾性、短ライフサイクル、瞬時起動即終了」— 従来クラウドの定常負荷と根本的に異なる
- 全スタック統合能力（インフラ・モデル・実行環境）を持つクラウドベンダーがAgentロードにおいて価値コアを占める

> **出典**: [新浪财经 — 阿里云面向海外发布Qwen Cloud](https://finance.sina.com.cn/jjxw/2026-05-26/doc-inhzfmym2236354.shtml) [T1], [Alibaba Cloud Community — Qwen Cloud Global Launch](https://www.alibabacloud.com/blog/alibaba-cloud-launches-qwen-cloud-for-global-markets_603191) [T1], [新加坡眼 — 阿里云千问大会在新加坡](https://www.yan.sg/20260527-the-alibaba-cloud-qwen-conference-was-held-in-singapore/) [T2]

### 千问云 企業採用事例 — 易点天下（2026年5月26日）

新加坡での阿里云千问大会（Qwen Conference 2026）において、**易点天下（eclicktech、股票代码: 301171）**が自社の統一Agent調度体系を出展。阿里千问大模型と百煉プラットフォームを基盤に構築。

**実装内容**:
- データ中台の分析能力と主要メディアアカウント管理、マーケティング洞察、予算配分、素材管理、プログラム広告投放を全面統合
- AI Agentを「補助ツール」から「業務参加者」へアップグレード — 分析・戦略生成・操作実行を自律的に完遂
- **Token予算ガバナンスとToken消耗効率**の最適化に注力
- 出海企業向けの業界ソリューションとして展開予定

**意義**: 易点天下はAIインフラの使用者からAI運営能力の輸出者へ転身 — AI化改造を自身で完了し、実戦検証済みの方法論をAI転換途上の出海企業へ輸出。

> **出典**: [新加坡眼 — 易点天下携统一Agent调度体系](https://www.yan.sg/20260527-the-alibaba-cloud-qwen-conference-was-held-in-singapore/) [T2], [亿邦动力 — 阿里云发布千问云](https://m.ebrun.com/669121.html) [T2], [中证网 — 千问云上线](https://www.cs.com.cn/ssgs/01/2026/05/20/detail_2026052010013156.html) [T1]

### 百煉プラットフォーム — 他社モデル全面開放（2026年5月20日）

阿里云百煉プラットフォームが全面開放され、月之暗面、Minimax、智譜、階躍星辰、愛詩科技、生数科技等と提携。以下のモデルが百煉経由および千问云官網で販売開始：

- **GLM-5.1**（智譜）
- **MiniMax M2.7**
- **Kimi K2.6**（月之暗面）
- **Pixverse-v6-it2v**（愛詩科技）
- **Kling-v3-omni-video-generation**（快手可霊）
- **Vidu Q3-Pro**（生数科技）
- **Tripo-H3.1**
- **mimo-v2.5-pro**

**计费模式**: 按需・按時間の柔軟计费。統一SDKインターフェースで異モデル切替が可能。

**百煉プラットフォームの成長指標**:
- 截至2026年3月、客户数量**同比8倍増**
- モデルサービスのToken消耗規模大幅上昇
- AI関連製品収益: **2026财年Q4 ¥89.71億**（連続11四半期三桁成長）、云外部収入占比**30%突破**

> **出典**: [新浪科技 — 阿里云百煉平台上架顶尖模型](https://finance.sina.com.cn/tech/roll/2026-05-20/doc-inhypnuh2623495.shtml) [T1]

### Qoder CN IDE 更新ログ（2026年5月）

Qoder CN（旧Lingma）IDEの最新アップデート：

| バージョン | 日付 | 主要内容 |
|-----------|------|---------|
| **v0.11.0** | 2026-04-28 | Code Review、ブラウザAgent、Hookメカニズム、DevContainerサポート、サンドボックス化ターミナル実行 |
| **v0.10.0** | 2026-04-14 | — |
| **v0.9.0** | 2026-04-09 | — |
| **v0.6.0** | 2026-03-18 | カスタムモデル対応（阿里云百煉、智譜、Kimi、MiniMax）、Qwen-Coder-Qoderモデルアップグレード |

**注**: 2026年2月以降、Qoder CNのVS Codeプラグインはメンテナンス停止。Qoder CN IDEへの移行を推奨。

> **出典**: [阿里云帮助文档 — Qoder CN更新日志](https://www.alibabacloud.com/help/en/lingma/product-overview/qoder-cn-update-log) [T1]

### Alibaba Cloud Summit — ハードウェアスタック刷新（2026年5月20日）

Alibaba Cloud Summitで発表された新ハードウェア群：

| 製品 | スペック |
|------|---------|
| **真武M890チップ** | 前世代(真武810E)比**3倍性能**、144GBオンチップメモリ、800GB/sチップ間帯域幅、FP32〜FP4対応 |
| **ICN Switch 1.0** | 25.6Tbps集約帯域幅、64アクセラレータ間輻輳フリー通信 |
| **Panjiu AL128スーパーノードサーバー** | 128アクセラレータ、PB/s内部帯域幅 |
| **T-Head SAILソフトウェアスタック** | 独自ハードウェア性能最大化 |

**Agentic RL**（百煉プラットフォーム）: 実際のエージェントタスク結果に基づく継続的モデル改善を実現。

**ARR予測**: 6月四半期に**¥100億（約$14億）**、年末までに**¥300億（約$41億）**。AI関連製品収益は約1年以内に従来のクラウドコンピュート売上を超える見込み。

> **出典**: Alibaba Cloud Blog (同上)

### 千问云（Qianwen Cloud）— Agent向けAI製品プラットフォーム（2026年5月20日）

2026年5月20日、阿里云は**千问云（Qianwen Cloud, www.qianwenai.com）**を発表。17年目で初めて阿里云公式サイト外に独立したAI製品サイトとして開設。ホームページに製品リストやコンソールボタンはなく、**一行のコード**のみが表示される：

```
npx skills add QianWen-AI/qianwen-ai
```

これは**Agent可読なプロンプト命令**。Agent（OpenClaw、Hermes Agent、Claude Code等）がこの命令を解釈し、全機能を自律的に「学習」する。

**核心アーキテクチャ**:

| 構成要素 | 説明 |
|---------|------|
| **Skills（標準化技能）** | モデル選定・呼び出し・認証・使用量照会を構造化ファイルにカプセル化。AgentがAPIドキュメント不要でモデルを呼び出せる。9モジュール: テキスト生成/チャット、画像理解、動画理解、画像生成、動画生成、TTS、モデルセレクター、認証、使用量照会 |
| **CLI（コマンドラインツール）** | ログイン・ステータス照会・環境診断・モデル検索・API呼び出し・使用量統計をコマンドラインで完結。スクリプトやバックグラウンドプロセスから操作可能 |
| **MCP（Model Context Protocol）** | 全モデルサービスをMCPプロトコルで公開 |

**規模**: 
- **150+モデルシリーズ、480+モデル**：Qwen、GLM、Kimi、DeepSeek、Wan、HappyHorse等
- **対応Agentフレームワーク**: OpenClaw、Hermes Agent、Claude Code、Qoder — 初日から対応
- SkillsとCLIは**GitHubでオープンソース**公開

**戦略的意義**:
- 「クラウドの消費者が人間からAgentに変わる」というパラダイムシフトに対応
- 阿里云CTO李飛飛: 「Agentワークロードは無規律弾性、短ライフサイクル、瞬時起動即終了 — 従来クラウドの定常負荷とは根本的に異なる」
- 全球の主要クラウドベンダーで初めて、Webサイトの第一言語を**人間からAgentに変更**した事例

> **出典**: [TestingCatalog](https://testingcatalog.net/alibaba-launches-qianwen-cloud-a-website-designed-for-ai-agents/) [T1], [品玩](https://www.pingwest.com/a/313885) [T1], [中关村在线](https://ai.zol.com.cn/1184/11843997.html) [T1]

### Token Plan サブスクリプション — 月額定額モデル（2026年5月22日）

千问雲と同時に、**Token Plan**サブスクリプションサービスが発表された。高頻度AIプログラミングおよびAgentツール向けに設計。

| プラン | 月額料金 | Credits | 月換算トークン相当 |
|-------|---------|---------|----------------|
| **標準版** | ¥198/月 | 25,000 Credits | — |
| **上級版** | ¥698/月 | 100,000 Credits（標準の4倍） | — |
| **尊享版** | ¥1,398/月 | 250,000 Credits（標準の10倍） | — |

**特徴**:
- チーム共有可能なクレジット制
- 専用API Key（`sk-sp-`接頭辞）と専用Base URL — 標準API（`sk-`）と完全隔離
- Hermes Agent、OpenClaw、Qwen Code等のツール間でクレジット共有
- 内蔵ツール（検索・コードインタープリター）は追加課金なし
- 利用量しきい値アラート設定可能
- マルチモデル対応：Qwen3.7-Max、Qwen3.6 Plus、GLM-5.1等

> **出典**: [阿里云开发者社区](https://developer.aliyun.com/article/1736226) [T1], [网经社](https://100ec.cn/detail--6659499.html) [T2]

### Qwen3.5-Plus 2026-04-20 スナップショット

4月20日付スナップショットでAgentic Coding能力が大幅改善。1Mトークンコンテキスト対応。4月27日より一般公開。

### ビジネス指標（QuestMobile Q1 2026）

- **2026年3月MAU**: **1.66億**（中国AIアプリ2位、Doubao 3.45億に次ぐ）
- **前年同期比成長率**: **+4,241%** — 中国最速成長AIアプリ
- **Q1純増MAU**: +1.26億
- **フルスタックMAU（App+Web+PC）**: 3億超
- **成長ドライバー**: 春節キャンペーン + 阿里ECエコシステム深層統合
- **2026年2月グローバルMAU**: 2.03億、世界3位（ChatGPT/Doubaoに次ぐ）、**成長率552%で世界1位**

> **出典**: QuestMobile/AI Product榜 2026.04–05 [Tier-1]

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
- **Qwen3.7-Max無料API体験共有（5/29）** — 芒果灵创の無料API期間をV2EXユーザーが共有
- **funyiリアルタイム字幕ツール（6/2）** — Qwen3-ASR-1.7BベースのOSS字幕ツールが話題に
- **Qwen3.7-Maxコード能力評価（5/23〜）** — 「qwen3.7-max 的代码能力提升非常大」との報告

### 掘金
- Qwen3-Coder vs Claude Codeのコーディング比較
- Qwen3.6 Plusのagentic coding実装ガイド
- Qwen3.6-27Bのベンチマーク分析（dense vs MoE）
- **Qwen3.7Max高コスト批判→無料化（5/29〜6/1）** — 甲维斯による一連の記事が大きな反響
- **QwenPawソースコード学習ガイド（5/30）** — AgentScopeチームのOSS個人AIアシスタント
- **DocPilot Qwenオープンソース公開（6/2）** — Android向けドキュメントAIアシスタント

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

### 2026年7月の新規動向

#### Qwen Image 3 — 画像生成モデル（2026年7月）
- 新世代画像生成モデル「Qwen Image 3」リリース。V2EX上で7月17日・21日にコミュニティ評価
- 開発者により専用ツールサイト（qwenimage3.co）が構築されるなど、実用浸透が進む

#### Qwen3-TTS — テキスト読み上げモデル（2026年7月15日）
- Qwen3-TTSがMacアプリケーションで活用開始。V2EXユーザーがQwen3-TTSを用いた無料TTSアプリを公開

#### Alibaba Cloud — Agent Native Cloud戦略（2026年7月20日）
- 阿里云が掘金で「Agent Native Cloud」記事を公開。AI智能体を企業のネイティブ能力として位置づける戦略宣言

#### Qwen Code v0.17.x — 未リリース継続
- v0.17.0-preview.0（5/29〜）が最新のまま、安定版リリースなし

### 2026年7月下旬の新規動向

#### Qwen 3.8 Maxプレビュー（2026年7月下旬）⭐
- **2.4兆（2.4T）パラメータ** — 中国2番目の大型フラッグシップモデル
- **ネイティブマルチモーダル対応** — 動画理解を含む
- **オープンウェイト化の意向** — フロントスケールパラメータ+OSSの初の中国モデルの可能性
- Zhihuコミュニティ反応: 「本质上是GLM-5.2的多模态版」「Kimi K3より速いが安価」「K3への対抗措置」
- 価格: **$1.40/MTok** 混合レート（ChinAI #368確認、従来$2.50から引下げ）
- 出典: Zhihu Frontier Weekly 7/27、ChinAI #368

#### 千問办公（Qwen Office）— AI辦公参入（2026年7月24日）
- 36kr報道: Alibaba AI辦公戦略が「智能体竞速」時代に突入
- DingTalk・千問雲・Qwen Appを統合したAIオフィスエコシステム構築
- wiki未記載の新規プロダクトカテゴリ

#### Qwen3-Coder-30B-A3B-Instruct-AWQ（2026年7月25日）
- V2EX: 無料提供される量子化モデルバリアント。Cursor autoモードとの比較報告

#### QwenPaw公式ガイド（2026年7月27日）
- Juejin: 「部署在你本地的专属数字员工」— 公式デプロイメントチュートリアル公開

#### 注目すべきAbsent
- Qwen4.0等の次世代モデルリリースなし
- WAIC 2026では目立ったQwen発表なし

### 外部ソース

|| ソース | URL | ティア | 概要 ||---|---|---|---|| 新浪 — Qwen3.6-Max-Preview | [sina.cn/news/5289894780869670](https://www.sina.cn/news/detail/5289894780869670.html) | T1 | 五大核心升级 || MarkTechPost — Qwen3.6-27B | [marktechpost.com/...](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/) | T1 | 密型Agentic Codingモデル || MarkTechPost — Qwen3.7-Max | [marktechpost.com/...](https://www.marktechpost.com/2026/05/21/qwen-introduces-qwen3-7-max-a-reasoning-agent-model-with-a-1m-token-context-window/) | T1 | 1Mコンテキスト・Agent永続実行 || Alibaba Cloud Blog — Qwen3.7 | [alibabacloud.com/blog/...](https://www.alibabacloud.com/blog/qwen3-7-the-agent-frontier_603154) | T1 | Qwen3.7公式Blog (5/21) || TestingCatalog — 千问云 | [testingcatalog.net/...](https://testingcatalog.net/alibaba-launches-qianwen-cloud-a-website-designed-for-ai-agents/) | T1 | Agent向け再設計詳細 || 品玩 — Agent時代インフラ | [pingwest.com/a/313885](https://www.pingwest.com/a/313885) | T1 | 芯片〜MaaS入口全層分析 || OpenRouter — Qwen3.7-Max | [openrouter.ai/qwen/qwen3.7-max](https://openrouter.ai/qwen/qwen3.7-max) | T1 | API価格・仕様 || GitHub — Qwen Code v0.16.0 | [github.com/...](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.0) | T1 | v0.16.0リリースノート || GitHub — Qwen Code v0.16.1 | [github.com/...](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.1) | T1 | v0.16.1ホットフィックス || GitHub — Qwen Code v0.16.2 | [github.com/...](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.2) | T1 | v0.16.2リリース || GitHub — 千问云 Skills/CLI | [github.com/QianWen-AI/...](https://github.com/QianWen-AI/qianwen-ai) | T1 | オープンソースSkills+CLI || 阿里云开发者社区 — Token Plan | [developer.aliyun.com/...](https://developer.aliyun.com/article/1736226) | T1 | Token Plan詳細 || Firethering — Qwen3.7-Max 35h autonomous | [firethering.com/...](https://firethering.com/alibaba-qwen3-7-max-autonomous-agent/) | T1 | 35時間自律カーネル最適化 || BenchLM.ai — Qwen3.7-Max | [benchlm.ai/...](https://benchlm.ai/models/qwen3-7-max) | T2 | リーダーボード || DataCamp — Qwen3.7-Max | [datacamp.com/...](https://www.datacamp.com/blog/qwen3-7-max) | T2 | Features & Benchmarks || 阿里云Qoder CN产品概述 | [help.aliyun.com/...](https://help.aliyun.com/zh/lingma/qoder-cn/product-overview/what-is-xx) | T1 | Qoder CN公式ドキュメント || 阿里云Qoder CN计费说明 | [help.aliyun.com/...](https://help.aliyun.com/zh/lingma/product-overview/billing-description) | T1 | Credits価格体系 || 阿里云Qoder CN更新日志 | [help.aliyun.com/...](https://help.aliyun.com/zh/lingma/product-overview/qoder-cn-update-log) | T1 | IDE更新履歴 || 163新闻 — 通义灵码更名Qoder CN | [163.com/...](https://www.163.com/dy/article/KTHN7OVM05118UGR.html) | T1 | 更名詳細・価格改定 || 新浪 — 阿里云面向海外发布Qwen Cloud | [sina.com.cn/...](https://finance.sina.com.cn/jjxw/2026-05-26/doc-inhzfmym2236354.shtml) | T1 | Qwen Cloud海外版公開 || Alibaba Cloud Blog — Qwen Cloud Global | [alibabacloud.com/...](https://www.alibabacloud.com/blog/alibaba-cloud-launches-qwen-cloud-for-global-markets_603191) | T1 | Token Plan・Enterprise機能 || 新加坡眼 — 阿里云千问大会 | [yan.sg/...](https://www.yan.sg/20260527-the-alibaba-cloud-qwen-conference-was-held-in-singapore/) | T2 | 易点天下Agent事例 || 亿邦动力 — 阿里云发布千问云 | [ebrun.com/...](https://m.ebrun.com/669121.html) | T2 | Skills/CLI解説 || 中证网 — 千问云上线 | [cs.com.cn/...](https://www.cs.com.cn/ssgs/01/2026/05/20/detail_2026052010013156.html) | T1 | 千问云概要 || 新浪 — 百煉平台上架顶尖模型 | [sina.com.cn/...](https://finance.sina.com.cn/tech/roll/2026-05-20/doc-inhypnuh2623495.shtml) | T1 | 他社モデル開放 || AI Models Navi — Qwen3.7完全ガイド | [aimodelsnavi.com/...](https://aimodelsnavi.com/en/blog/qwen3-7-max-deep-dive) | T2 | リリースタイムライン・ベンチマーク || Aipedia — Qwenレビュー | [aipedia.wiki/tools/qwen](https://aipedia.wiki/tools/qwen/) | T2 | 2026年4月時点完全レビュー || Yahoo Finance — 企業戦略 | [finance.yahoo.com/...](https://finance.yahoo.com/markets/sto...|| 掘金 — Qwen3.7-Max無料化 | [juejin.cn/post/7646234722919170088](https://juejin.cn/post/7646234722919170088) | T1 | 6/1 Qwen3.7-Max無料化発表 || 掘金 — Qwen3.7Max高コスト批判 | [juejin.cn/post/7644794219849744394](https://juejin.cn/post/7644794219849744394) | T1 | 5/29 コスト批判記事 || 掘金 — QwenPaw学習ガイド | [juejin.cn/post/7645237921839874098](https://juejin.cn/post/7645237921839874098) | T1 | 5/30 QwenPaw OSS解説 || 掘金 — DocPilot Qwen | [juejin.cn/post/7646593427816693770](https://juejin.cn/post/7646593427816693770) | T1 | 6/2 DocPilot OSS公開 || V2EX — funyi字幕ツール | [v2ex.com/t/1217448](https://www.v2ex.com/t/1217448) | T1 | 6/2 Qwen3-ASR字幕ツール || V2EX — Qwen3.7-Max無料API共有 | [v2ex.com/t/1216566](https://www.v2ex.com/t/1216566) | T1 | 5/29 無料API期間共有|


