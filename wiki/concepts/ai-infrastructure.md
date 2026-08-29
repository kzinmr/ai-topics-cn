---
title: "AIインフラ構造 — AI Rack WarとCopper-to-Optics移行トレンド"
description: "AIサーバー/ラックインフラの技術トレンド：銅配線から光配線への移行、Compute-Memory-Connectivityの三本柱、MediaTek/Marvell/Foxconnの戦略的ポジショニング、TSMC COUPEシリコンフォトニクス光エンジン量産"
created: 2026-06-06
updated: 2026-08-29
tags: [AI-infrastructure, datacenter, copper-to-optics, silicon-photonics, Marvell, MediaTek, Foxconn, Computex, TSMC, COUPE, Nvidia-Spectrum-X]
source_lang: zh-CN
---

# AIインフラ構造（AI Rack Infrastructure）

AIサーバー/データセンターの物理インフラにおける技術トレンドと競争構造。2026年に入り、**Compute→Memory→Connectivity**とボトルネックが移行する中で、銅配線から光配線への「Copper-to-Optics」転換が業界の焦点となっている。

## Compute・Memory・Connectivityの三本柱

Marvell Technology（美満電子/Matt Murphy CEO）はComputex 2026のキーノートで、AIインフラパフォーマンスは以下の3つの柱に依存すると指摘した：

| 柱 | 時期 | 状態 |
|---|---|---|
| **Compute**（演算） | 過去2年 | 主要ボトルネック（GPU不足） |
| **Memory**（メモリ） | 現在 | 主要ボトルネック（HBM容量/帯域） |
| **Connectivity**（接続） | 今後 | 次のボトルネック（「Copper Wall」到達） |

この3段階のボトルネック移行は、AIインフラ投資の重点がチップ単体から**ラック内/ラック間接続**へとシフトしていることを示す。

## Copper Wall（銅の壁）とCopper-to-Optics移行

### 銅配線の物理限界

AIラック内のデータ伝送は従来、銅ケーブル（copper cables）と銅配線（copper traces）に依存してきた。しかしGPU間/ノード間の帯域要件が急増するにつれ、銅媒体の物理的限界（信号減衰、消費電力、発熱）に到達しつつある。これが業界で**「Copper Wall」**と呼ばれている現象。

### 光配線（Silicon Photonics）への移行

Marvellは2021年にInphi社を**100億ドル**で買収し、高速光相互接続と信号処理技術を獲得。これによりシリコンフォトニクス（silicon photonics）分野で即座にリーディングポジションを確立した。

Copper-to-Optics移行は以下の層で進行中：

| 層 | 技術 | 主要プレイヤー |
|---|---|---|
| チップ間接続 | Copper traces → Optical I/O | Marvell, Ayar Labs |
| ラック内接続 | DAC銅ケーブル → 光ケーブル（AOC） | Foxconn, Luxshare |
| ラック間接続 | 光トランシーバー（800G/1.6T） | Innolight, Coherent, Marvell |

#### TSMC COUPE光エンジンの量産開始（2026-08-21）

シリコンフォトニクス商業化の遅延（2〜3世代に及ぶ停滞）の背景で、TSMCが自社のシリコンフォトニクス光エンジン **COUPE** を実用化。Nvidiaは2026年8月、TSMC製COUPE光エンジンとシリコンフォトニクスを組み込んだ**初代Spectrum-Xスイッチ**が量産開始したと発表（Tech Taiwan 胡說科技、2026-08-21号）。

- **意味**: Copper-to-Optics移行のラック間/ラック内接続層で、TSMCが「フォウンドリ+光エンジン」の一体供給で優位性を獲得。NvidiaとBroadcomの既存光配線サプライチェーンをTSMCが取り込む構造。
- **TSMCシリコンフォトニクスR&D**: 10年以上同分野R&Dに携わるTSMC顧客へのインタビュー（Tech Taiwanポッドキャスト連携）。シリコンフォトニクスが2〜3世代を経てようやく商業的実用段階に到達した経緯を独自解説。
- **競合位置づけ**: Marvell（Inphi買収由来のシリコンフォトニクス先行）とTSMC COUPEが、ラック内/チップ間光相互接続で並走する新段階。

## 主要企業の戦略的ポジショニング

### Marvell Technology（美満電子）

- **CEO**: Matt Murphy（フランクリン&マーシャルカレッジ卒、リベラルアーツ出身の異色CEO）
- **変革**: 2016年の会計スキャンダル後、創設者チームが退任。Murphyが緊急CEOとして就任
- **戦略転換**: スマートフォン市場撤退、Wi-Fi/Bluetooth事業売却 → クラウドデータセンター・AIサーバー向け半導体ソリューションへ
- **ノード戦略**: 14/16nm→7nmを**スキップ**して5nmへ直接移行
- **買収戦略**: Avera Semiconductor（旧IBM ASIC設計部門）、Inphi（100億ドル/光相互接続）
- **Nvidiaとの関係**: 2026年3月、NvidiaがMarvellに**20億ドル**出資。「mini-Broadcom」（ネットワーキング+ASIC両輪）として、AIインフラで台頭するBroadcomへの対抗軸に育成する意図
- **Google LPU契約（2026-08-21）**: GoogleとTPU関連商業契約を締結。報道では「Marvell製品はGoogle TPUを支援」と曖昧だが、実態は**LPU（超低遅延推論向けニッチAIプロセッサ）**を受託（TPUではない、MediaTekのTPU注文を奪った形跡なし）。MarvellはGoogleに市場価格割安の株式引受（最大5,897万株、全行使で約122億ドル相当）を許容し、Googleを第5位株主にする構造。台湾規制上、Marvellが差し入れたワラントタイプは許可されないとの指摘
- **時価総額**: MediaTekを明確に上回る

### MediaTek（聯発科技）

- AIラック戦争において、Copper-to-Optics移行の波に乗る戦略
- Computex 2026のブースで、光コネクタ関連の展示が注目
- T-Glass（ガラス基板）供給囲い込み戦略と併せ、AIインフラ層でのプレゼンス強化
- 詳細: [[mediatek]]

### Foxconn（鴻海精密）

- Computex 2026でAIラック内の金属コネクタ展示
- 従来は組立中心だったが、光コネクタ/シリコンフォトニクス領域への参入を示唆
- AIサーバーOEM/ODMとしてのバリューチェーン上流化戦略

## Nvidia vs Broadcom vs Marvell：AIインフラの三極構造

| 企業 | ポジション | AIインフラ戦略 |
|---|---|---|
| **Nvidia** | GPU支配 | CUDAエコシステム+NVLink。Marvellに出資して対Broadcom軸形成 |
| **Broadcom** | カスタムASIC最大手 | Google TPU受託。XPUネットワーク。Nvidiaの最有力競合 |
| **Marvell** | ネットワーキング+ASIC | 「mini-Broadcom」。シリコンフォトニクス強み。Nvidiaと提携 |

この三極構造において、**Connectivity層**が次の競争の焦点となる。NvidiaはGPUのCompute支配を背景に、MarvellをConnectivity/ASIC軸のパートナーとして引き込み、Broadcomの台頭に対抗しようとしている。

## 市場データ

| 指標 | 値 | 出典 |
|---|---|---|
| Marvell Inphi買収額 | $10B（2021年） | Marvell IR |
| Nvidia→Marvell出資 | $2B（2026年3月） | Tech Taiwan |
| Marvell→Google LPUワラント | 最大5,897万株・全行使で約$12.2B相当（Google第5位株主、2026-08-21） | Tech Taiwan |
| TSMC COUPE + Nvidia Spectrum-X | 初代Spectrum-Xスイッチがシリコンフォトニクス+COUPE光エンジンで量産開始（2026-08-21） | Tech Taiwan |
| Silicon Photonics市場予測 | 2030年に$10B超 | 業界レポート |
| 800G光トランシーバー需要 | 2026年急増 | Computex 2026 |

## 技術トレンド

### Copper-to-Opticsのタイムライン

1. **〜2024年**: Copper DAC（Direct Attach Copper）が主流。ラック内1-3m接続
2. **2025-2026年**: Copper Wall到達。800G/1.6Tで銅の信号減衰が限界に
3. **2026-2028年**: AOC（Active Optical Cable）への移行加速。ラック内光配線本格化
4. **2028年〜**: Optical I/O（チップレベル光相互接続）の実用化

### ガラス基板（Glass Substrate）

T-Glassなどガラス基板技術は、パッケージング層での銅代替として注目。MediaTekが供給囲い込みを先行実施（[[mediatek]]参照）。Copper-to-Opticsトレンドと連動する。

### 利益配分の逆転 — 「レール」川湖科技がNvidia超え（2026-08-28）

NvidiaのFY2028（2028年1月末締め）売上成長見通しが**70%**と発表され、アナリスト平均予想45%を大幅に上回った（発表翌日、Nvidia株は一時8.7%急伸）。黄仁勳（Jensen Huang）は「70%はサプライチェーンが支えられる水準に過ぎず、需要ははるかに高い」と説明し、CFOは顧客提示の需要実績値が「倍増」を示唆すると述べた——**需要が供給能力を大幅に超過**している構図が明確になった。

Morgan Stanleyは残るボトルネックを**TSMC 3nm容量**と**ABF基板（T-Glassガラスクロス）**の2点に絞る（HBM要件はNvidia側が既に引き下げ済み）。TSMCの来期値上げ（+5〜10%）を正当化する材料でもある。

利益配分では異例の逆転が起きている：

| 企業 | 品目 | 粗利率 | 出典 |
|---|---|---|---|
| 川湖科技（King Slide Works） | サーバー用レール（slides/rails） | **87.4%**（2026年Q2、台湾製造業記録か） | Tech Taiwan 2026-08-28 |
| Micron（美光） | HBM/メモリ | 86%（2026年Q2） | 同上 |
| Nvidia | GPU | 71〜72%（今後2四半期はさらに低下見通し） | 同上 |
| TSMC | フォウンドリ | 68%（Q2、過去最高） | 同上 |

- 川湖は創業者・林聰吉一族がForbes台湾富豪ランキング首位（純資産207億ドル超、張虔生・陳泰銘らを抜く）に浮上。
- TSMCの魏哲家CEOはMicronの86%粗利率に「うらやましい。うちは68%で十分嬉しい」と発言（7月決算説明会）。
- **論点**: サプライチェーンの利益は最先端チップ設計（Nvidia）から、代替困難な周辺部品・材料（レール、メモリ、T-Glass）へ移転している。「Why is King Slide so profitable? Will major customers simply stand by while a Taiwanese supplier earns higher margins than they do?」——川湖の粗利率の持続可能性と、サーバーレールがなぜ代替困難かの深掘りは同号の後編に委ねられた（後編未受領）。
- 川湖の「87%」がNvidiaとTSMCの間で孤立しないよう、Micron/TSMCの数字を併記する形に修正。

## 関連

- [[mediatek]] — MediaTekのT-Glass戦略とAI半導体ポジショニング
- [[gpu-sanctions-china]] — GPU制裁と中国半導体自立化（AIインフラの地政学）
- [[verisilicon]] — 中国半導体IPプロバイダ
- [[cambricon]] — 中国AIチップ設計（寒武紀）
- [[biren-technology]] — 中国GPUスタートアップ（壁仞科技）

## Sources

- Tech Taiwan（胡說科技）, "Inside the AI Rack War: MediaTek and Foxconn Race Toward the Copper-to-Optics Era" (2026-06-05) — [Substack](https://substack.com/@techtaiwan)
- Tech Taiwan（胡說科技）, "How TSMC Came From Behind in Silicon Photonics and Won Over Nvidia and Broadcom" (2026-08-21) — [Substack](https://substack.com/@techtaiwan)
- Tech Taiwan（胡說科技）, "King Slide's 87% Gross Margin Tops Nvidia's. What Makes Its Server Rails So Hard to Replace?" (2026-08-28) — [Substack](https://substack.com/@techtaiwan)
- Marvell Technology Computex 2026 キーノート（Matt Murphy CEO）
- Nvidia $2B Marvell出資報道（2026年3月）
