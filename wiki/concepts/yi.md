---
title: "Yi（零一万物）— 01.AI"
type: concept
tags: [LLM, chinese-ai, open-source, MoE, enterprise-ai]
created: 2026-04-23
updated: 2026-04-23
source_lang: zh-CN
---

# Yi（零一万物）— 01.AI

| | |
|---|---|
| **会社** | 北京零一万物情報技術有限公司（01.AI） |
| **創設** | 2023年11月、李開復（Kai-Fu Lee） |
| **代表モデル** | Yi-34B, Yi-1.5, Yi-Coder, Yi-Lightning, Yi-Large |
| **アーキテクチャ** | Dense + MoE（Yi-Lightning） |
| **エンタープライズプラットフォーム** | 万智平台（WorldWise Platform） |
| **Webサイト** | [01.ai](https://www.01.ai/) |

## 概要

01.AI（零一万物）は、Google/Microsoftの元高管である**李開復（Kai-Fu Lee）博士**が率いる中国の生成式AI企業。2023年3月に設立され、同年11月には**Yiシリーズ大モデル**をリリース。わずか8ヶ月で**10億ドル超のユニコーン評価額**を達成し、シリアルAラウンドは**Alibaba Cloud**がリード、**Sequoia China（紅杉中国）**、**ZhenFund（真格基金）**らが参加。

**ビジョン**: "Make AGI Accessible and Beneficial to Everyone"（AGIを誰もがアクセスでき、有益なものにする）。AI 2.0によって技術・プラットフォーム・アプリケーションの各層で革命を起こすと主張。

## Yiモデル系列

### Yi-34B（2023年11月）

- **パラメータ**: 34B
- 初期バージョンで**200Kコンテキスト**をサポート
- HuggingFaceのベンチマークで**MetaのLlama 2を複数項目で上回る**性能を記録
- 中国語・英語のバイリンガルアライメントに優れる
- プライベートデプロイメントや業界別カスタマイズに広く使用

### Yi-1.5シリーズ（2024年）

- **Yi-1.5-6B/9B/34B**: Yi-34Bのアップグレード版
- コーディング・数学・推論能力を大幅に強化
- 多言語コーパスの清洗と配分に独自のデータ护城河を構築

### Yi-Coder-1.5B/9B

- **コード生成特化モデル**。プログラマーのための「オープンソース利器」と称される
- **52言語**に対応
- **128Kコンテキスト**ウィンドウ
- コード補完、デバッグ、クロス言語変換に強い

### Yi-Lightning

- **MoEアーキテクチャ**を採用した軽量・高効率モデル
- **SOTAのコストパフォーマンス**モデルとして位置づけ
- コスパ重視の企業ユースケースに最適

### Yi-Large

- **数百億パラメータの閉源モデル**
- API価格は**$2.5/MTok**（GPT-4 Turboの$10/MTokの**約1/4**）
- クローズドAPI提供でハイエンド計算サービスを提供

### Yi-VL-6B/34B

- **多模态モデル**（テキスト+画像）
- **448×448解像度**の画像理解
- 視覚・言語の統合モデル化に向けた取り組み

## 万智平台（WorldWise Platform）

01.AIのエンタープライズ向けAI Agentプラットフォーム。

### v1.0（2025年3月）

- 企業サービスに完全シフト。「**All in to B**」戦略
- AI Agentのカスタマイズとマルチエージェント協調をサポート

### v2.0（2025年7月）

- **「首席執行官プロジェクト（Chief Executive Project）」**戦略発表
- WorldWise v2.0で企業向けAI Agentに重点

### v2.5（2026年1月）

- **「AI 2.0オペレーティングシステム」**と位置づけ
- **「Super Employee（超级员工）」**: 企業AI Agentの新形態
- 2026年を「マルチエージェントシステムの企業デプロイの重要年」と宣言

### 「All in 万智」戦略

2024年後半、**1兆パラメータモデルの訓練**を中断し、**軽量産業モデルとエンタープライズアプリケーション**への集中へシフト。2025年3月には「All in to B」戦略を正式発表。

## 市場定位と現状

### 「六小虎」から「四小強」への再編

中国AIスタートアップの「**六小虎（六小虎）」**時代から、2024-2025年にかけて**「四小強」**への再編が進行。01.AIはBaichuan Intelligenceとともに「**頭部から脱落**」したと見なされる。

### 「四小強」との比較（2026年初頭）

- **智譜AI（Zhipu AI）**: B側ローカル展開で最強。香港上場済み
- **MiniMax**: C側多模态・海外市場で支配
- **月之暗面（Moonshot/Kimi）**: 長コンテキスト技術のリーダー。100億人民元以上の現金準備
- **阶跃星辰（StepFun）**: DeepSeekのV3/R1で市場を disruption

### 2025年業績

- 2024年比で**数倍の増収**だが、正確な数字は非公表
- 中国企業はAIプロジェクトへの支払いに消極的という課題

### 海外市場が新しい成長エンジン

- **米国、サウジアラビア、香港、シンガポール**に進出
- サウジ・中央アジア（カザフスタン）での政府連携も活発
- 李開復博士の国際的な人脈が海外展開を加速

### 企業向けAI Agent（万智平台）への戦略シフト

FDE（Frontier Deployment Engineer）モデルを採用。「コンパニオン型」のエンタープライズ顧客への手厚い対応を実施。Alibaba Cloudのインフラへの依存が戦略的リスクとも指摘される。

## 関連エンティティ

- [[concepts/qwen]] — Alibabaの対抗モデル
- [[concepts/chatglm]] — 清華大学系Zhipu AIのモデル
- [[concepts/china-local-deployment]] — 国産モデルのローカル展開
- [[concepts/china-ai-agent-ecosystem]] — 中国AI Agent生態系

## 出典

- [Yi 大模型全面解析：零一万物开源编程利器与生态布局 (AI问答站)](https://ai.lansai.wang/103222.html)
- [01.AI / 零一万物 Deep Research Report (Mapping Studio)](https://mappingstudio.ai/companies/01ai/report)
- [01.AI Official Website](https://www.01.ai/)
