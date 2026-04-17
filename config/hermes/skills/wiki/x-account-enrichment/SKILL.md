---
name: x-account-enrichment
description: Enrich skeleton X/Twitter entity pages for Chinese AI space accounts from x-accounts.yaml
category: wiki
version: 1.0.0
author: hermes
license: MIT
metadata:
  hermes:
    tags: [Wiki, Enrichment, X-Accounts, Chinese-AI, Entity]
---

# X Account Enrichment（中国語AIスペース版）

## Purpose

`config/feeds/x-accounts.yaml` に登録された中国語AIスペースのX/Twitterアカウントのスケルトンエンティティページを、充実したフルページにエンリッチする。中国のAI研究者、開発者、エンジニア、メディア関係者のX活動、ブログ投稿、プロジェクト、貢献内容を調査し、日本語で記述する。

## Steps

### 1. 現状監査

```bash
# x-accounts.yamlのアカウント一覧とエンティティページの状態確認
python3 -c "
import os, yaml
with open(os.path.expanduser('~/ai-topics-cn/config/feeds/x-accounts.yaml')) as f:
    data = yaml.safe_load(f)
    accounts = data.get('accounts', data) if isinstance(data, dict) else data
entity_dir = os.path.expanduser('~/ai-topics-cn/wiki/entities')
for acct in accounts:
    handle = acct['handle'].lstrip('@')
    name = acct.get('name', handle)
    path = os.path.join(entity_dir, f'{handle}.md')
    if os.path.exists(path):
        with open(path) as f: content = f.read()
        skeleton = 'status: skeleton' in content or len(content) < 2000
        print(f'  {handle} ({name}): skeleton={skeleton}, size={len(content)}B')
    else:
        print(f'  {handle} ({name}): MISSING')
"
```

### 2. 優先度付け

以下のティアで優先順位を決定する：

| ティア | 対象 | 例 |
|------|------|------|
| Tier-1 | 中国AIの重要人物、主要企業のCTO/研究リード | 李沐（Li Mu）、張俊林、DeepSeek/MoonshotのCTO |
| Tier-2 | MLエンジニア、AIコメンテーター、スタートアップ創業者 | 中国AIエコシステムの活発な発信者 |
| Tier-3 | コントリビューター、新興の声 | 中国AIに関するインサイトを提供する新興アカウント |

### 3. リサーチ戦略

各アカウントについて以下を調査：

1. **X/Twitter活動**: 最近のツイート、主要な意見、ディスカッションテーマ
2. **ブログ/個人サイト**: 記事、技術ノート（知乎コラム、WeChat記事含む）
3. **GitHubリポジトリ**: 作成・コントリビュートしたプロジェクト
4. **中国AIコミュニティでの影響力**: V2EX、Juejin、Zhihuでの言及状況
5. **講演、インタビュー、ポッドキャスト**: 公開発言
6. **他wikiエンティティとの接点**: [[deepseek]], [[glm-zhipu]], [[kimi-moonshot]] 等との関係

#### 中国語圏特有の調査ポイント

- 知乎の専門家プロフィール（回答数、フォロワー数、主要回答テーマ）
- WeChat公众号（運営している場合）
- Bilibili/動画プラットフォームでの活動
- 中国国内企業との関係（阿里、バイトダンス、テンセント、バイドゥ、清華大学等）

### 4. エンリッチフォーマット

```yaml
---
title: "氏名（中国語名/英語名）"
handle: "@twitter_handle"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [person, 関連タグ]
aliases: ["中国語名", "英語名", "handle"]
source_lang: zh-CN
---

# 氏名 (@handle)

| | |
|---|---|
| **X** | [@handle](https://x.com/handle) |
| **知乎** | [プロフィール](URL) |
| **GitHub** | [username](https://github.com/username) |
| **所属** | 企業名 / 役職 |
| **代表業績** | 主要な貢献 |
| **概要** | 2〓3文の背景説明 |

## 概要

2〓3段落の紹介。人物背景、AI領域での重要性、中国AIエコシステムでの位置づけ。

## 核心的な主張（Core Ideas）

中国AIに関する主要な見解、理論、意見。サブセクションで各テーマを整理。実際の投稿/記事を可能な限り引用。
中国語原文は原文のまま保持し、日本語訳を併記。

### [テーマ1]
分析 + エビデンス

### [テーマ2]
分析 + エビデンス

## 主要業績（Key Work）

- 作成したプロジェクト/ツール/ライブラリ
- 発表論文
- 著名なブログ記事 / 知乎回答
- 講演・プレゼンテーション

## 最近の活動（Recent Posts）

主要な記事/ツイートを日付付きで記載。

## 関連人物（Related People）

他wikiエンティティとの接点。

## X活動テーマ（X Activity Themes）

最も頻繁にツイートするトピック。
```

### 5. バッチ処理

- サブエージェントあたり2アカウント（並列最大4）
- 絶対パスを指定: `/home/exedev/ai-topics-cn/wiki/entities/{name}.md`
- バッチ後にファイルサイズとスケルトン状態を検証

### 6. コミット

```bash
cd ~/ai-topics-cn && git add wiki/ && git commit -m "wiki: enrich X accounts (batch N)" && git push
```

## Output

- エンリッチ済みエンティティページ（8-15KB目標）
- 実際の引用、具体的な例、実在のリンクを含む
- `[[deepseek]]`, `[[glm-zhipu]]`, `[[kimi-moonshot]]` 等への相互リンク
- wiki/index.md と wiki/log.md の更新

## 品質目標

- **サイズ**: 8-15KB以上（glm-zhipu.mdレベルを参考）
- **内容**: 実際の引用、具体的な例、実在のURL
- **セクション**: 核心的な主張（サブセクション付き）、主要業績、最近の活動、関連人物、X活動テーマ
- **フロントマター**: `source_lang: zh-CN`、`status: skeleton`タグなし
- **相互参照**: `[[entity-name]]` 形式で他エンティティをリンク
- **言語**: 日本語で記述、中国語原文は引用時に保持

## 既知の注意点

1. **ファイル名エイリアス**: サブエージェントが指定と異なるファイル名で作成することがある。バッチ後に必ず重複チェック。
2. **バジェット枚渇**: 50イテレーション制限。バッチ後に全ファイルが書き込まれたか検証。
3. **パス混乱**: サブエージェントが誤ったディレクトリに書き込むことがある。常に絶対パス `/home/exedev/ai-topics-cn/wiki/entities/` を指定すること。
4. **statusクリーンアップ**: エンリッチ後も `status: skeleton` が残ることがある。手動で確認・削除。
