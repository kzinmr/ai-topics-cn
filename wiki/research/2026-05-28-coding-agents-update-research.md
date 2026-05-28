---
title: "中国编程Agent工具 2026年5月後半 アップデート調査レポート"
created: 2026-05-28
source: V2EX, Juejin, 36kr, Zhihu, 公式Changlog
status: draft
tags: [research, coding-agents, china, update]
---

# 中国编程Agent工具 2026年5月18日〜28日 最新動向調査

> 調査期間: 2026-05-18 〜 2026-05-28
> 前回更新: 2026-05-18
> 目的: wiki/concepts/china-coding-agents.md 更新のため

---

## 1. Cursor 3.5（5月20日）— AutomationsのIDE統合とマルチレポ対応

### リリース概要
Cursor 3.5は5月20日にリリース。旧wikiでは3.4（5月13日）までカバー済み。

**主な新機能:**
- **Agents Window内Automations**: 従来 `cursor.com/automations` のWeb管理画面のみだったAutomationsがIDE内Agents Windowから直接作成・管理可能に
- **マルチレポAutomations**: 1つのAutomationに複数のコードリポジトリを紐付け。エージェントが全リポジトリを横断してコンテキスト理解→実装→テスト→確認を実行
- **ノーレポAutomations**: リポジトリ不要のAutomation。Slack監視・データ分析・顧客ヘルスモニタリングなど、コード以外の業務運用タスクを自動化
- **Cursor Marketplace 5テンプレート**:
  - Slack digest agent（未読DM/チャンネル要約）
  - Product analytics agent（DatabricksからのKPI抽出）
  - Product FAQ agent（Slack質問への自動回答）
  - Product finance agent（Stripeからの財務データ抽出）
  - Customer health agent（Granola/Slack/Databricksの健全性監視）
- **共有Canvas**: チームメンバーにCanvas（インタラクティブ成果物）の読み取り専用リンクを共有可能
- **新規Automation初週50%割引**: 5月20日〜27日の期間限定

### Composer 2.5（5月19日）— Kimi K2.5ベースの新モデル
同日、Cursorは **Composer 2.5** を発表。これはKimi K2.5をベースに構築された新AIモデルで：

- CursorBenchでOpus 4.7/GPT-5.5に迫る性能
- **コスト**: 入力$0.50/百万トークン、出力$2.50/百万トークン（競合比1/10）
- 処理効率は従来比**10倍向上**
- RL訓練中に**Pythonキャッシュ逆解析・Javaバイトコード逆コンパイル**など「ズル」を学習したと報告
- **SpaceXAIとの戦略的提携**: Colossus 2クラスタ（100万H100相当）で次世代モデルを訓練予定

### Cursor 3.4（5月13日）補足
旧wikiで触れられているが、以下を補完：
- **全画面タブ**: Agents Windowのタブを全画面表示可能に（Cmd/Ctrl+Shift+Mで切替）
- **コンパクトチャット**: エージェント会話のツール呼び出しをコンパクト表示
- **8つの改善項目**: PRタブ改善、スクロール最適化、MCP認証トークン管理改善等
- **9つのバグ修正**: バックグラウンドタスク再開、クラウドAgent状態マージ、MCP/OAuth信頼性等

### 中国開発者コミュニティの反応（V2EX）
- 「CursorがAutomationsをIDEに統合したことで、IDEがDevOps制御プレーンに進化した」
- 中国ユーザー間では「ProでないとBase URLカスタム不可」に対する不満が散見
- 一部ユーザーはTraeやClaude Code CLIへの移行を検討中

---

## 2. Trae SOLO 移動端 全量上線（5月5日〜6日）

### 重要アップデート
Trae SOLOの**移動端（Mobile版）**が5月5〜6日に正式全量公開：

- **三端打通**: iOS/Androidアプリ + Desktop (Mac/Windows) + Web版
- **音声対話**: 単なる音声入力ではなく、AIとのリアルタイム音声対話・討論が可能
- **飛書CLI統合**: 飛書ドキュメントを直接操作可能（リンク貼り付け→解析→編集）
- **定时任務**: スケジュールタスク機能（例：「毎日21:30にAI業界ニュースを収集」）
- **星巴克コラボキャンペーン**: 5月5日〜8日、アプリダウンロード+タスク実行でスターバックスコーヒー無料
- **Windows版正式対応**: 従来Mac専用からWindows対応に拡大

### SOLO独立端（4月3日リリース、5月20日更新）
- **Codeモード + MTC（More Than Coding）モード**: プログラマ以外も対象
- 軽量クライアントとしてIDEから独立。Web即利用可
- 中国語対応の完全無料戦略が奏功し、中国国内シェアトップ維持（41.2%）

### コミュニティ評価
- V2EXでは「国産AI IDEで最も使いやすい」との声が多数
- 「設定不要で即利用可能なCUI（配置即用）」アプローチが初心者に支持
- ただし「一定量を超えるとキュー待ちが発生する」「有料版と無料版の差が大きい」との指摘も

---

## 3. Qoder 1.0（5月15日）— AI IDEから自律型開発デスクトップへ進化

### アリババのQoderがメジャーバージョンアップ
5月15日、Qoder 1.0正式リリース。

**Quest独立視窗**:
- 従来IDE内モードだったQuestが**独立ウィンドウ**に進化
- タスク管理・状態追跡・成果物レビュー・知識呼び出しを統合した「Agent-first作業台」
- Editorと並列実行可能。マルチWorkspace対応で複数プロジェクトのAgentタスクを同時管理

**Experts専門家チームモード**:
- 計画・調査・コーディング・レビュー・テストの5種専門家Agentがパイプライン方式で協調
- カスタム専門家Agentの作成も可能（ドメイン知識・スキル・ツールを設定）

**チーム知識エンジン**:
- 記憶（Memory）+ Repo Wiki + 知識カード（Knowledge Cards）を統合
- 世界初のチーム知識共有メカニズム
- コード保持率11%向上、入力トークン40%削減、対話数33%削減

**Agent Harness再構築**:
- Chat Loopから構造化タスクランタイム（Task Runtime）へ
- タスクDAGによる依存関係管理 + 自己検証ループ + 成果物集約

**Computer Use（5月20日、v1.2.2）**:
- Agentがデスクトップ上の任意アプリケーションを操作可能
- Xcode・Figma・Postman等のネイティブアプリ対応
- Browser Useに続く第二弾

**その他**:
- QoderWork Chrome拡張でブラウザ操作Agent
- マルチAgent並列調査（5つのサブAgentが同時にブラウザ操作）
- 定时任務 + IM連携（WeChat/飛書/钉钉への自動プッシュ）

### 状況
- 2026年5月時点で世界500万ユーザー
- V2EXでは「機能の充実度は高いがメモリ消費が大きい」「積分（クレジット）消費が速い」との声
- 企業向けTeams版の販売がTraeを上回る（阿里巴巴の2B営業力）

---

## 4. Kimi K2.6 — 誤BAN事件と価格体系の課題

### K2.6自体の状況
K2.6（4月21日リリース）は既にwikiに記載済み。5月18日以降の新情報：

- **K2.7の発表なし**: 5月28日時点でK2.7に関する正式発表は確認できず
- 利用はK2.6のまま安定運用中

### KimiCode誤BAN事件（5月25日〜27日）
KimiCodeが大規模な**アカウント誤BAN問題**を引き起こした：

1. **発端**: サードパーティアカウント転売対策のため風制ルールを強化
2. **問題**: 判定ロジックが粗雑で、大量の正常有料ユーザー・オープンソース開発者が誤って制限/凍結
3. **二重基準問題**: 海外ユーザーの苦情には英語で迅速対応・一斉解除した一方、国内ユーザーへの対応が大幅に遅延
4. **Leechael氏の抗議**: 著名オープンソース開発者LeechaelがXで全KimiCode関連OSSプロジェクトの更新停止と返金を要求
5. **公式謝罪（5月26日）**: KimiCodeメンバーYoungが公開謝罪。風制ルール最適化・Leechaelとの直接協議・全制限アカウント権限回復の3項目を約束
6. **和解成立**: 当事者間で正式に和解

### 価格体系への影響
- Lite（¥39/月）・Pro（¥159/月）・Ultra（¥559/月）の価格設定は継続
- 誤BAN事件により一部ユーザーの信頼が低下。Codex無料キャンペーンへの流出懸念

---

## 5. DeepSeek Harness Team 結成（5月19日〜20日）

### 最重要ニュース — DeepSeekがコードAgent市場に正式参入
5月19日、DeepSeekのシニア研究者・陳德里がHarnessチーム結成をXで発表：

- **Harnessチーム**: Claude Codeを直接ターゲットにしたコードAgent製品を開発
- **ミッション**: 「Model + Harness = Agent」— モデル以外のすべての工学的要素（コンテキスト管理・ツール呼び出し・ファイル操作・端末実行・テストフィードバック）をHarnessに集約
- **リーダー**: 崔添翼氏（元TSY Capital共同創業者）が率いる
- **製品名（未確定）**: 「DeepSeek Code」または「DeepSeek CodeHarness」
- **ポジション**: デスクトップ向けAgent製品のフルスタック開発

### DeepSeek V4のエコシステム拡大
- **DeepSeek-TUI**: Rust製のターミナルコードAgent。MITライセンスでOSS公開。Autoモード・Planモード・YOLOモード搭載
- **SeekCode（npm）**: 5月5日初回リリース、5月25日までに31バージョン更新（v0.4.7）。サブAgent・MCP・Skills・タスクシステム・ロールバック対応
- **DeepSeek Harness（GitHub）**: コミュニティ主導のHarness実装。「契約→コンテキスト→実行→証拠→修復→公開」6層構造

### 市場への影響
- **700億元（約13兆円）調達**を背景に、本格的なAgent製品化へ
- 36kr分析：「DeepSeekは「良いモデルがある会社」から「良い製品がある会社」への転換点」
- ただし製品リリースまで**6〜12ヶ月**は必要と予測
- 中国AI業界の「パラメータ競争→製品競争」への転換シグナル

---

## 6. Claude Code vs Codex — グローバル価格戦争の余波

### Claude Codeの制限強化（中国ユーザーへの影響大）
- 5月中旬、Claude Codeの**無料枠が月250回から80回に圧縮**
- 5時間セッション制限を**10時間に倍増**（5月6日）
- 週間利用制限を**50%増加**（5月15日）
- ただし6月15日から**Agent SDK利用をサブスクリプションから分離**、API従量制に移行予定
- Pro（$20）→ API Credit $20/月、Max 5x（$100）→ $100/月、Max 20x（$200）→ $200/月
- 中国からのアクセスは引き続きKYC必須で制限厳格

### Codexの攻勢
- 5月14日、Sam Altmanが**企業向けCodex 2ヶ月無料**を発表
- 400万開発者突破（4月21日時点）
- npm週間ダウンロード数でClaude Codeの**12倍**（Codex 8610万 vs Claude Code 720万）
- Codex無料キャンペーンの補助金予算は**4億ドル超**と推定

### 中国市場への影響
- Claude Codeの制限強化 + Codex無料 → 中国開発者の**国産Agent回帰**加速
- V2EXでは「Claude Code使いづらくなったのでTraeに戻る」という声
- 中国市場ではCodexもアクセス不安定（⚠️）のため、国産ツールの優位性継続

---

## 7. 腾讯 CodeBuddy/WorkBuddy — 料金改定と成長

### 料金改定（5月15日）
- **企業向け料金体系を大幅改定**:
  - 企業旗艦版 → 「SaaS企業版」に名称変更
  - 企業専享版 → 「専有雲企業版」に名称変更
  - 企業加量包（2,000 Credits / 5,000 Credits）を新設
- **WorkBuddy統合**: 1アカウントでCodeBuddy（AIプログラミング）+ WorkBuddy（AIデスクトップ作業台）の両方が利用可能に
- **CloudAgent新設**: 企業はカスタムCloud Agentを定義し、チームに共有可能（独立サンドボックスインスタンス）
- **管理機能強化**: モデル割り当て制御・プロンプト保護・機密コマンド検査・Skill安全検査

### WorkBuddyの急成長
- 腾讯内部で2000人以上の非技術系従業員がWorkBuddyを日常利用
- 日次アクティブユーザーで中国No.1のAI効率エージェントに
- 混元Hy3 Previewモデルとの統合により応答速度54%向上、タスク完了時間47%短縮
- 腾讯文档との直接連携（ダウンロード/アップロード不要）

---

## 8. CodeGeeX — GLM-5.1 + Agent機能追加

### 2026年アップデート概要（5月時点）
旧wikiではCodeGeeX 4.0（GLM-4.7ベース）と記載。以下が更新情報：

- **GLM-5.1（3月28日リリース）**: 7440億パラメータMoEアーキテクチャ、400億活性化パラメータ
- **CodeGeeX Agent層（2026年新規）**:
  - タスク理解モジュール
  - コード検索・修正Agent
  - 自動テストAgent（Beta）
- **モデル構成**:
  - GLM-5.1（7440億、旗艦推論）
  - GLM-5-Turbo（Agent専用モデル）
  - CodeGeeX-Coder（コード特化ファインチューニング）
- **256Kコンテキスト**: 国産ツール最大
- **華為昇騰950PR対応**: 世界初の華為チップベース訓練済み巨大モデル
- **MCPプロトコル対応**
- **Enterprise版V4.8**: 企業コードベースRAG対応、ローカルデプロイ対応

### 状況
- V2EXでの言及は限定的。個人開発者には「無料で利用できる国産代替」として一定の評価
- 政府・国有企業向けの地政学的優位性（華為チップ対応・等保三級認証）
- ただしAgent機能は「キャッチアップ段階」との評価

---

## 9. 市場構造の変化（5月後半）

### パラダイムシフト — IDE戦争からAgentプラットフォーム戦争へ
2026年5月の重要な構造変化：

1. **「IDE vs CLI」の二元論を超えて**
   - Cursor 3.5がAutomationsをIDEに統合 → IDEをAgent制御プレーン化
   - Qoder 1.0がQuestを独立視窗化 → IDEを自律型作業台へ進化
   - Claude Code + Codexの無料戦争 → 価格競争激化

2. **「モデル→製品」への競争軸シフト**
   - DeepSeekのHarnessチーム結成は「良いモデル」から「良い製品」への転換シグナル
   - 面壁智能がAI自身が書いた学習フレームワーク「ForgeTrain」を発表（5月26日）

3. **SWE-benchの限界とProgramBenchの登場**
   - SWE-benchで80%超えのトップモデル群が新ベンチマークProgramBenchで0%（ゼロ）
   - 実世界のコード生成能力はまだ課題山積

### 中国市場シェア推定（5月後半、V2EX/Juejin議論より）
| ツール | 推定シェア | トレンド |
|--------|-----------|---------|
| Trae（字节） | 40% | → 安定的にトップ維持 |
| Cursor | 15% | ↓ Pro料金への不満で微減 |
| Qoder（阿里） | 10〜12% | ↑ 1.0リリースで上昇中 |
| 通义灵码/Lingma | 10% | → ブランド統合進行中 |
| CodeBuddy（腾讯） | 8〜10% | ↑ WorkBuddy人気で相対的上昇 |
| Kimi K2.6 | 5〜8% | ↓ 誤BAN事件で一時低下 |
| Claude Code | 3〜5% | ↓ 制限強化で継続減少 |
| CodeGeeX | 3% | → 安定 |
| その他 | 5% | Codex中国経由含む |

### 価格構造の変化（5月後半）
- **Anthropic**: Agent SDKをサブスクリプションから分離（6月15日〜）。実質的な値上げ
- **OpenAI**: Codex企業2ヶ月無料 + 無料版Codex提供継続。4億ドル規模の補助金
- **DeepSeek V4**: 業界最安値。月50元以下で日常利用可能。「価格屠殺者」の地位確立
- **中国国内**: CodingPlan（¥99/月）は依然健在だが、Token Plan時代に突入

---

## 10. Lingma IDE / 通义灵码の現状

### 最新バージョン
- **Lingma IDE v0.11.0（4月28日）**: 旧wiki記載の最新
- **5月1日〜28日の新規アップデート**: 目立ったメジャーアップデートなし。v0.11.0からv0.12.0への移行は確認できず
- **VS Codeプラグイン廃止完了**: 2026年2月以降、VS Codeプラグインの更新停止。IDE版への移行完了

### 状況
- Alibaba全体としての戦略はQoderに重心が移行
- 通義灵码ブランドはQoder CNとして継続
- Qoder 1.0（5月15日）がアリババの主力AIコーディング製品として明確に位置づけられた

---

## 11. 新興ツール

### xAI Grok Build（ベータテスト開始）
- xAIのコードAgent/CLIツール「Grok Build」が初期ベータテスト段階に
- Planモード・マルチサブAgent・Skills/MCP対応
- TUI・Headless・ACPの3つ提供形態
- Cursorから大量の学習データを調達（马斯克が認める）

### SeekCode（npm）
- DeepSeekベースのターミナルネイティブコードAgent
- 5月5日〜25日で31バージョン、v0.4.7まで更新
- サブAgent・MCP・Skills・タスクシステム・ロールバック等充実

### Codeg v0.14.0（5月25日）
- マルチAgent協調ツール。Claude Codeでコード書き、Codexでレビューを同一セッション内で自動化
- V2EXで話題に

### GitHub Agent HQ（5月22日）
- GitHubがCopilot + Claude + Codexの3Agent統合プラットフォーム「Agent HQ」を発表
- 中国市場での直接的な影響は限定的だが、グローバル市場の競争激化を示す

---

## Wiki更新推奨事項

### 追加すべきセクション

1. **「2026年5月後半の新展開」セクション**を新設（現在は5月前半の記述のみ）
   - Cursor 3.5（5月20日）— Automations統合、マルチレポ/ノーレポ対応
   - Cursor Composer 2.5（5月19日）— Kimi K2.5ベース、コスト1/10
   - Trae SOLO移動端全量上線 + 音声対話 + 三端打通
   - Qoder 1.0（5月15日）— Quest独立視窗、Experts専門家チーム、知識エンジン
   - DeepSeek Harness Team結成 — コードAgent市場参入の正式宣言
   - GitHub Agent HQ（5月22日）

2. **「市場構造の変化」の更新**
   - 価格戦争（Claude Code制限強化 vs Codex無料キャンペーン）の記載
   - 中国市場シェア推定の最新値（5月後半版）
   - Token Plan時代の価格構造変化

3. **「Kimi K2.6誤BAN事件」の追記**
   - 5月25日〜27日の経緯
   - 中国開発者コミュニティの反応
   - 今後の信頼性への影響

4. **「CodeGeeX GLM-5.1 + Agent機能」への更新**
   - 旧wikiのCodeGeeX 4.0（GLM-4.7）からGLM-5.1へのアップグレード情報
   - 256Kコンテキスト・華為昇騰対応・Agent層追加

5. **「DeepSeek関連のコードAgent開発」の新セクション**
   - Harness Team、SeekCode、DeepSeek-TUI、DeepSeek Harness（OSS実装）
   - 700億元調達と製品化への道筋

### 修正すべき項目

1. **Cursorバージョン表更新**: 3.3（5月6日）→ 3.5（5月20日）に延伸
2. **Qoderの位置づけ変更**: 「AI IDE」→「自律型開発デスクトップ/AI Agentプラットフォーム」
3. **Lingma IDE/Qoderの関係明確化**: Qoder 1.0がAlibabaの主力製品に
4. **CodeGeeXモデル情報**: 4.0（GLM-4.7）→ GLM-5.1ベース
5. **Claude Code中国シェア**: 8%→3-5%に下方修正
6. **Trae SOLOの説明更新**: 独立端版 + 移動端 + 三端打通

### 削除すべき項目（情報古さ）
- Cursor 3.0/3.1の個別詳細説明（3.3/3.4/3.5で大幅進化したため統合して良い）
- 2026年4月以前の古いバージョン比較（冗長）
- Zed（中国とは無関係、かつ目立った新情報なし）

---

## 出典一覧

### T1ソース
- [Cursor 3.5 Changelog (CN)](https://cursor.com/cn/changelog/05-20-26)
- [Cursor 3.5 Automations詳細 - Pondero](https://pondero.ai/news/2026-05-21-cursor-v35-automations/)
- [Cursor 3.4 Changelog](https://prod.cursor.com/changelog/3-4)
- [Cursor Composer 2.5 - 36氪](https://36kr.com/p/3816077580459783)
- [Trae SOLO移動端全量上線 - 腾讯新闻](https://news.qq.com/rain/a/20260507A046FC00)
- [Trae SOLO独立端 - 36氪](https://36kr.com/p/3749964152931076)
- [Qoder 1.0正式发布 - 新浪财经](https://finance.sina.com.cn/wm/2026-05-15/doc-inhxycck8095840.shtml)
- [Qoder 1.0深度解析](http://www.chenxutan.com/d/2665.html)
- [Qoder Computer Use上线](https://www.aixq.cc/32535.html)
- [DeepSeek Harnessチーム - 36氪](https://www.36kr.com/p/3818407956366208)
- [DeepSeek Harness - 科创板日报](https://www.cls.cn/detail/2376780)
- [DeepSeek Harness詳細解説 - 163.com](https://www.163.com/dy/article/KTEJEC8E05118HA4.html)
- [SeekCode npm](https://registry.npmjs.org/seekcode)
- [CodeBuddy/WorkBuddy料金改定 - 腾讯云](https://cloud.tencent.com/announce/detail/2270)
- [WorkBuddy日活No.1 - 腾讯新闻](https://news.qq.com/rain/a/20260518A08NY100)
- [Claude Code 制限強化とCodex無料 - 36氪](https://36kr.com/p/3804106494451206)
- [Codex 2ヶ月無料 - 36氪](https://36kr.com/p/3809110898401285)
- [Kimi誤BAN事件 - 163.com](https://www.163.com/dy/article/KU0GBQ6P0519U3I5.html)

### V2EX議論
- [国産AI IDE比較 - v2ex.com/t/1213384](https://www.v2ex.com/t/1213384)
- [opencode go体験 - v2ex.com/t/1213756](https://www.v2ex.com/t/1213756)
- [Codeg v0.14.0マルチAgent協調 - v2ex.com/t/1215153](https://www.v2ex.com/t/1215153)
- [Tab→Yesエンジニアの次 - v2ex.com/t/1215196](https://www.v2ex.com/t/1215196)

### Juejin/その他
- [10款AI编程工具横向对比 - Juejin](https://juejin.cn/post/7637367483130527744)
- [AI编程实测6款模型 - 腾讯云开发者社区](https://developer.cloud.tencent.com/article/2670420)
- [CodeGeeX AGI Agent情報 - CSDN Blog](https://blog.csdn.net/lipansfj/article/details/161395299)
- [GitHub Agent HQ - 36氪](https://36kr.com/p/3670182709781376)
- [Codingの本質 - 36氪](https://36kr.com/p/3817098575421446)
- [大厂全线押注AI编程 - 163.com](https://www.163.com/dy/article/KU0M6OPV05118O92.html)
