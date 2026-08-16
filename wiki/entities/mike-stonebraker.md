---
title: Mike Stonebraker — データベースの父、AI Agentへの警鐘
created: 2026-05-02
updated: 2026-05-02
tags: [person, database, turing-award, ai-agents, postgres, dbos, stonebraker]
aliases: ["Mike Stonebraker", "Michael Stonebraker", "石破天", "マイク・ストーンブレーカー"]
source_lang: zh-CN
---

# Mike Stonebraker — データベースの父、AI Agentへの警鐘

> **トレンド順位**: 2026年4月-5月、AI Agentとデータベースの交差点で急上昇
> **ソース**: 36kr, Vonng Blog, Heavybit Podcast, ACM [T1]
> **重要度**: 高 — 図灵奖得主がAI Agent業界に直言、データベース技術の再評価

## 概要

Mike Stonebraker（マイク・ストーンブレーカー、1943年生まれ）は、アメリカの計算機科学者。MIT CSAIL上席研究員、2014年ACMチューリング賞受賞。**Ingres**と**PostgreSQL**の生みの親として知られ、データベース分野で50年以上にわたり業界をリード。Vertica、StreamBase、VoltDB、DBOSなど多数のデータベース企業を共同設立。2026年春、AI Agent業界に対して「Agentic AIの根本問題はデータベース問題である」と直言し、大きな反響を呼んだ。

## 2026年AI Agent論 — 「Agent最後全是数据库问题」

### 核心主張

Stonebrakerは2026年初頭のインタビューで、現在のAI Agent業界に対して以下の警鐘を鳴らした:

1. **Agentic AIの本質は「LLM + システム包装」**: 現在のAgentはほとんどが「読み取り専用」段階に留まっている
2. **「読み書き」世界ではデータベース問題に帰着**: 振込、在庫更新など実際のwrite操作に入ると、問題は即座に**トランザクション、一貫性、アトミック性**のデータベース古典問題に戻る
3. **耐久性コンピューティング = ACIDのD**: Agentの失敗回復メカニズム（ログ→リワインド→再生）は、まさにデータベースのトランザクションセマンティクスそのもの
4. **1-2年以内にデータベース技術がAgentインフラの中核に**: Sagaパターン、ワークフロートランザクションなどがAgentエコシステムの基盤になる

> 「現在のAgentic AIは largely read-only。writeの世界に入れば、問題は即座にデータベースの旧問題——トランザクション、一貫性、アトミック性——に戻る。これはAI問題ではなく、分散データベース問題である。」

### DBOS（Database-Oriented Operating System）

Stonebrakerの最新プロジェクト。**LinuxとKubernetesをデータベースに置き換える**という逆転の発想:

- オペレーティングシステムの全状態をデータベーステーブルとして表現
- 状態操作はステートレスタスクからのクエリで実行
- プロトタイプはマルチノード・マルチコア・トランザショナルな**VoltDB**
- DatabricksのMatei Zahariaとの共同研究から着想（Databricksが100万SparkサブタスクのスケジューリングをPostgreSQLで管理していた事実から）

> 「OSがデータベースの上で動くアプリケーションになる——その逆ではない。」

## LLMによるText-to-SQLへの厳しい評価

StonebrakerはLLMのSQL生成能力について実データを基に直言:

| 評価軸 | 公開ベンチマーク | 実データウェアハウス |
|--------|-----------------|-------------------|
| 正確率 | 80%+ | **0%**（そのまま） |
| FROM句+結合条件を与えた場合 | - | **35%** |
| 熟練人类エンジニア | - | **90%+** |

**MITデータウェアハウス（1,400テーブル）でのテスト結果**:
- LLM単体: 約10%の正確率
- 結合条件+FROM句提供: 約35%に向上するも、依然として50%以上のギャップ
- 理由: 実データは「the pile」に存在せず、LLMは学習済みデータでない限り正確な取得ができない

> 「実ウェアハウスでは、LLMもAgentic AIも使い物にならない。LLMを全体オーケストレーターとして賭けるのではなく、SQLに賭ける——これが私たちのコントラリアンな視点だ。」

## データベース業界への批評

### Oracleへの直言

Larry Ellison（Oracle創設者）について:
> 「彼は顧客に嘘をつくのが上手だった。未実装の機能を『現在利用可能』として売り、最初の顧客にデバッグさせた。」

具体例: 引用整合性（Referential Integrity）機能——Oracleはマニュアルに2ページの説明を書いたが、ページ下部に「未実装」と記載。Ingresは既に実装済みだった。

### Googleへの批評

MapReduceと結果整合性（Eventual Consistency）について:
> 「Googleは頭が良いから、皆が盲目的に信じた。でもHadoopは信じられないほど非効率で、結果整合性はごく限られた场景にしか適さない。Spannerが登場した時点で、Google自身もトランザクションと一貫性というデータベースの旧問題は回避できないと認めたようなものだ。」

### AWSへの批評

> 「Amazonは約15種類のデータベースを同時に維持している。実際に必要なのは3種類だろう。グラフデータベースや重複機能を持つ多くのデータベースは、性能面でも市場面でも存在理由が疑わしい。」

## 「One Size Fits None」理論

Stonebrakerの代表的なデータベース理論（2004年提唱）:

- **汎用データベースは誰にも最適でない**: 「one size fits all」は実質「誰にもfitしない」
- **専用システムの優位性**: ストリーム処理（StreamBase）、列指向存储（Vertica）、メモリトランザクション（VoltDB）は、それぞれ汎用システムより1桁高性能
- **現代における妥当性**: ClickHouse（列指向）、Pinecone（ベクトル検索）など、専用データベースの成功が理論を裏付け
- **Postgresの位置づけ**: 「最低限の共通ニーズを満たす選択肢としては最高。PB級データウェアハウスや毎秒100万トランザクションには不向きだが、それ以下なら十分」

## Ingres → Postgresの歴史

### Ingres（1972年-1980年）

- UC BerkeleyでGene Wongと共に開発
- Coddの関係モデルに基づいた実装
- 100以上の大学で採用されたが、COBOL非対応など商用面で課題
- 1980年にIngres Corp.設立、商用化へ

### Postgres（1986年-）

Ingresの限界を乗り越えるため設計:

1. **拡張可能型システム**: GIS（点、線、多边形）、債券業務の「30日計算」など、カスタムデータタイプと演算をサポート
2. **継承**: AI研究者のニーズに応えたオブジェクト指向機能
3. **タイムトラベル**: 歴史データクエリ機能（後に削除）

> 「Postgresの核心思想——任意のデータタイプを定義でき、高い実行効率を保つ。」

## 人材評価哲学

Stonebrakerの「優秀な人材」を見分ける方法:
> 「技術的な詳細を掘り下げればすぐ分かる。修士論文は何をしたか、どのように実装したか、エラー処理はどうか、何プロセス使ったか、なぜスレッドを使わなかったか——こうした深い質問をすれば、すぐに判別できる。」

そして有名な一言:
> 「十分に賢くない人々とは交流するのが難しい。」

## 経歴

| 年 | 出来事 |
|----|--------|
| 1943 | 米国マサチューセッツ州生まれ |
| 1971 | UC Berkeley着任、データベース研究開始 |
| 1972 | Ingresプロジェクト開始（助理教授時代） |
| 1976 | UC Berkeley終身在職権取得 |
| 1980 | Ingres Corp.設立 |
| 1986 | Postgresプロジェクト開始 |
| 1994 | UC Berkeley退職、MITに移籍 |
| 1994 | ACMチューリング賞受賞 |
| 2004 | Vertica設立（列指向データベース） |
| 2005 | IEEEジョン・フォン・ノイマンメダル受賞 |
| 2014 | ACMチューリング賞受賞 |
| 2023 | DBOS（Database-Oriented OS）プロジェクト開始 |
| 2026 | AI Agentとデータベースの関係を論じたインタビューで大きな反響 |

## 関連リンク

### 内部リンク

- [[deepseek]] — LLMのSQL生成能力への評価で言及
- [[dbos]] — Stonebrakerの最新プロジェクト
- [[postgres]] — 直接の起源となったプロジェクト

### 外部ソース

| ソース | URL | ティア | 概要 |
|--------|-----|--------|------|
| 36kr — 图灵奖得主炮轰半个行业 | https://36kr.com/p/3788895533095937 | T1 | AI Agentは最終的にデータベース問題になる |
| Vonng Blog — Data 2025 Year in Review | https://vonng.com/en/db/db-year-review-2025 | T1 | Stonebraker×Pavlo対談の詳解 |
| Heavybit Podcast — Ep.11 | https://www.heavybit.com/library/podcasts/data-renegades/ep-11 | T2 | Text-to-SQL評価とDBOSのビジョン |
| ACM Turing Award | https://amturing.acm.org/award_winners/stonebraker_1172121.cfm | T1 | チューリング賞受賞業績 |
| The Register — Stonebraker 80th | https://theregister.com/2023/12/26/michael_stonebraker_feature | T2 | DBOSとOS-as-a-databaseの構想 |
