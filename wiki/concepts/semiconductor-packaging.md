---
title: "半導体先進パッケージング — EMIB vs CoWoS、Google TPU第9世代の製造戦略"
created: 2026-06-13
updated: 2026-09-19
tags: [semiconductor, packaging, tpu, intel, tsmc, google, mediatek, broadcom, ai-hardware]
aliases: ["semiconductor-packaging", "先進パッケージング", "EMIB", "CoWoS", "TPU製造"]
source_lang: zh-CN
---

# 半導体先進パッケージング — EMIB vs CoWoS、Google TPU第9世代の製造戦略

> **重要度**: **高** — AIアクセラレータの製造競争における核心的技術
> **関連技術**: 2.5D/3Dパッケージング、Chiplet、ガラス基板（T-Glass）
> **主要プレイヤー**: Intel（EMIB）、TSMC（CoWoS）、Google（TPU設計）、MediaTek、Broadcom

## 概要

2026年6月、Computex 2026での発表を契機に、半導体先進パッケージングをめぐる競争が新たな局面に入った。特に注目されるのは**Google第9世代TPUの製造戦略シフト**と、**Intel EMIB vs TSMC CoWoSの2.5Dパッケージング競争**である。

本概念ページは、AIアクセラレータ製造におけるパッケージング工程の戦略的重要性、主要プレイヤーの動向、供給链構造の変化を追跡する。

## Google TPU第9世代 — 製造戦略の構造変化

### MediaTekが主力、Broadcomはコンティンジェンシーに格下げ

2026年4-5月、MediaTekはGoogleのTPUビジネスで重要なブレイクスルーを達成。Tech Taiwan（胡說科技）の独占報道によれば：

- **第8世代TPU**: BroadcomとMediaTekが対等のパートナーシップで受託
- **第9世代TPU**: MediaTekが共同開発版を**主力パス**に、Broadcom版を**コンティンジェンシー（代替手段）**に格下げする可能性
- **背景**: TSMCのCoWoSパッケージング工程で培ったベテラン技術者のMediaTekへの移籍が士気向上と技術力強化に貢献

Broadcom CEO Hock Tan（陳福陽）はBloombergインタビューで初めてMediaTekを言及し、「ankle-biter（足首に噛み付く小敵）」と揶揄。しかしこの発言は、MediaTekの脅威を公然と認めたものと解釈できる。

### Intel EMIB — Googleの大胆な選択とリスク

Googleは第9世代TPUで**IntelのEMIB-T**（Embedded Multi-die Interconnect Bridge）2.5Dパッケージングプラットフォームを大胆に採用した。

| 技術 | 企業 | 特徴 | 状況 |
|------|------|------|------|
| **EMIB-T** | Intel | シリコンブリッジ方式。有機基板内にシリコンブリッジを埋め込む | Google TPU第9世代で採用。量産能力が焦点 |
| **CoWoS** | TSMC | シリコンインターポーザ方式。高コストだが実績十分 | 業界標準。MediaTek人材の源泉 |
| **SoIC** | TSMC | 3D積層方式（次世代） | 研究開発段階 |

**核心的な質問**: Intel EMIB-Tは大規模量産に対応できるか、それとも第9世代TPUのAchilles' heel（アキレス腱）となるか？

## 先進パッケージングの戦略的重要性

### なぜパッケージングが注目されるのか

1. **ムーアの法則の鈍化**: 微細化（3nm→2nm→1.4nm）のコストが指数関数的に増加
2. **Chipletアーキテクチャの台頭**: 複数ダイをパッケージ内で統合する設計パラダイム
3. **AIアクセラレータの特殊化**: 汎用GPUからTPU/ASICへ。パッケージング工程が性能を左右
4. **サプライチェーンの多極化**: TSMC一強からIntel・Samsung・中国勢の追撃

### T-Glass（ガラス基板）— 次のフロンティア

Agentic AIの台頭により業界全体の出荷予測が急上昇する中、**次のボトルネックは最先端チップやHBMではなく、それらをパッケージングする基板**になると予測されている。

- **MediaTek**: BroadcomやNvidiaに先んじてT-Glass供給の囲い込みに積極的
- **Google**: 追加評価を獲得し、将来的なAI ASIC受注を確保
- **業界**: ガラス基板は次世代パッケージング技術として注目

## Nvidia×Unitree Robotics — 人型ロボット供給链の地政学

### Computex 2026での発表

Nvidia CEO Jensen Huang（黃仁勳）はUnitree Robotics（宇树科技）との人型ロボットリファレンスプラットフォームを発表：

- **Unitree H2**: 身長180cm、重量68kgの人型ロボット
- **Nvidia Jetson Thor**: BlackwellベースのAIコンピュータ
- **Sharpa**: シンガポール製の巧手（dexterous robotic hands）

### 米国シンクタンクの懸念

SCSP（Special Competitive Studies Project）のMartijn Rasser氏はDSETフォーラムで、「中国製ロボットがグローバルスタンダードになる可能性」を公然と警告。

一方、Boston DynamicsのCLO Jason Fiorilloは「NvidiaのUnitree提携は排他的ではない」と冷静な見方を示し、その後Huangが韓国でHyundai Motor Group（Boston Dynamicsの親会社）とのロボット協力深化を発表した事実を指摘。

### 中国国内の反応

皮肉なことに、Nvidia×Unitree提携は中国国内でも批判を浴びた。一部のネットユーザーが「UnitreeがHuaweiではなくNvidia GPUを選択したのは愛国心がない」と非難。

Chris Miller（『Chip War』著者）は、米中サプライチェーン戦争が**Physical AI（ロボット・ドローン）**分野に波及すると警告。EV産業でCATLが直面した「中国依存ジレンマ」をロボット時代で繰り返してはならないと指摘。

## 市場構造図

### AI半導体サプライチェーンの多極化

```
Google TPU第9世代
├── 設計: Google
├── 製造受託（主力）: MediaTek
├── 製造受託（コンティンジェンシー）: Broadcom
└── パッケージング: Intel EMIB-T

Nvidia AIプラットフォーム
├── GPU: Blackwell/Rubin（TSMC製造）
├── ロボット: Unitree H2 + Jetson Thor
└── 提携: Hyundai/Boston Dynamics
```

### 主要プレイヤーのパッケージング戦略

| 企業 | パッケージング技術 | 顧客/パートナー | 状況 |
|------|-------------------|-----------------|------|
| **Intel** | EMIB-T | Google（TPU第9世代） | 量産能力が検証段階 |
| **TSMC** | CoWoS | NVIDIA、MediaTek他 | 業界標準。拡張継続 |
| **Samsung** | I-Cube | 自社Exynos、外部顧客 | CoWoSに対抗 |
| **ASE/SPIL** | OSAT | 汎用 | アセンター |

## 最新動向（2026年6月）

- **MediaTek**: 株価過去1ヶ月で86%急騰。リミットアップ4回。Google TPU受託が主要要因
- **Broadcom**: CEOがMediaTekを公然言及。「ankle-biter」と揶揄も、脅威認識の表れ
- **Intel**: EMIB-T採用がGoogle第9世代TPUで決定。量産能力の成否が焦点
- **TSMC**: CoWoS人材がMediaTekへ流出。アリゾナ新工場と台湾本国の両方で拡張
- **Unitree Robotics**: Nvidia提携でグローバル注目。中国国内で「愛国心」批判も

## TSMC白埔（白埔）CoWoS検証ライン計画（2026-09-19 受信・予告パートのみ）

Tech Taiwan（陈良玲/胡說科技）Semicon Series 3「Inside TSMC's "Baipu Plan"」（2026-09-18号、**本編は会員限定・予告パートのみの受領**）より。Semicon Taiwan 2026 で TSMC 共同COO 秦永沛（Y.P. Chin）が言及した、高雄北部への先端パッケージング検証ライン新設計画：

- **立地**: 白埔（旧糖業「白埔農場」、国有地）。高雄市政府が工業団地に開発し、南仔（Nanzih）方式に倣い TSMC 進出後に国家科学技術委員会へ移管、高雄第4の科学园区になる見通し。供給链各社が「白埔到底在哪」を最初に問うたという。
- **中核**: そこに建てる2つの設備のうち、目玉は**商用品を生産しない CoWoS 生産ライン**。装置サプライヤーを入居させて共同開発・製品検証を行うもので、「台湾で前例のない R&D モデル」と位置づけられる。動機の解説は Semicon Taiwan 2026 の「议程外会合」に始まるとされるが、その本編は未受領。
- **含意（当ウィキ側の評価）**: CoWoS 供給链の検証能力を TSMC が垂直統合から「サプライヤー同址共同検証」へ開く転換点の可能性。後編受領後に本節を改訂すること。

## 関連

- [[mediatek]] — Google TPU受託で台頭。T-Glass供給囲い込み戦略
- [[unitree-robotics]] — Nvidia提携人型ロボット。地政学的懸念の的
- [[chris-miller]] — 半導体地政学分析。Physical AI供給链戦争を警告
- [[gpu-sanctions-china]] — 米中半導体戦争。制裁と国産化の構造
- [[ai-infrastructure]] — Copper-to-Optics移行、Marvell/Inphi、Nvidia-Broadcom-Marvell三極構造
- [[nvidia]] — GPU覇者。Blackwell/Jetson Thorロボットプラットフォーム

## Sources

- Tech Taiwan（胡說科技）, "Could Google's Next TPU Shift Back to TSMC? Inside the EMIB vs. CoWoS Battle" (2026-06-12) — [Substack](https://substack.com/@techtaiwan)
- Tech Taiwan（胡說科技）, "Chris Miller：The AI Supply Chain, Huawei's 'Tao Law,' and the Next Wave of the China Model" (2026-06-12) — ポッドキャスト
- Chris Miller, 『Chip War』（《晶片戰爭》）— 半導体地政学
- Bloomberg — Hock Tan（Broadcom CEO）インタビュー
- Reuters — 米当局のDeepSeek/Blackwell GPU指摘
- SCSP（Special Competitive Studies Project）— Martijn Rassor氏発言
- Tech Taiwan（胡說科技）, "Semicon Series 3 | Inside TSMC's 'Baipu Plan' and the Hidden Agenda That Revealed It" (2026-09-18) — 予告パートのみ受領（会員限定本編未受領）
