---
title: Qwen（通义千问）— 阿里云大模型旗舰
created: 2026-04-17
updated: 2026-04-26
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

> **出典**: [MarkTechPost — Qwen3.6-27B Release](https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/), [Qwen Blog — Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b), [TokenMix Review](https://tokenmix.ai/blog/qwen-3-6-27b-review-dense-beats-moe-2026)

### Qwen3-Coder — コーディング特化（480B MoE / 35B active）

コード生成・理解に特化したバージョン。Claude Code、Cursorと比較する記事が掘金・V2EXで多数投稿。CodingPlan（[[coding-plan]]）においてKimi K2.6およびGLM-4.7と並んでバンドル提供。

### 価格競争 — Qwen3-Max 50%値下げ

2026年の中国AI価格戦争でQwen3-Maxの料金が最大50%引き下げ。trillion-parameter閉鎖モデルながら、競争激化により価格破壊を起こしている。

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
