---
name: wiki-entity-upgrade
description: Upgrade skeleton wiki entity pages to full-depth analysis with Chinese AI source cross-referencing
category: wiki
version: 1.0.0
author: hermes
license: MIT
metadata:
  hermes:
    tags: [Wiki, Entity, Upgrade, Chinese-AI, Deep-Analysis]
---

# Wiki Entity Page Upgrade（中国語圏AI版）

## Purpose

`wiki/entities/` 内のスケルトンまたは浅いエンティティページを、中国語圏AIソースとの相互参照を含む完全な深層分析ページにアップグレードする。品質ターゲットは既存の `glm-zhipu.md`（9.9KB）および `claude-code.md`（10.3KB）レベル。対象はモデル、企業、人物、組織など全エンティティタイプ。出力は日本語。

## Steps

### 1. 現状監査

```python
import os
target = os.path.expanduser("~/ai-topics-cn/wiki/entities/")
skeletons, upgraded = [], []
for f in sorted(os.listdir(target)):
    if not f.endswith('.md'): continue
    with open(os.path.join(target, f)) as fh:
        content = fh.read()
    size = len(content)
    has_depth = any(s in content for s in [
        "## 核心的な主張", "## Core Ideas", "## モデルラインナップ",
        "## 実戦での評価", "## エコシステム連携", "## 中国語圏での"
    ])
    if has_depth and size > 5000:
        upgraded.append((f, size))
    else:
        skeletons.append((f, size))
print(f"✅ 完了: {len(upgraded)}, 📋 要アップグレード: {len(skeletons)}")
for name, size in skeletons:
    print(f"  - {name} ({size}B)")
```

### 2. 品質ターゲットページの確認

以下の既存ページが品質基準を示す参照ページである:

| ページ | サイズ | 特徴 |
|--------|--------|------|
| `glm-zhipu.md` | ~10KB | モデルラインナップ、ソース引用付き評価、比較、エコシステム連携 |
| `claude-code.md` | ~10KB | 中国語圏での利用状況、コミュニティ反応、代替ツールとの比較 |
| `kimi-moonshot.md` | ~7.5KB | 企業概要、中国市場でのポジション、開発者コミュニティでの評判 |

**共通する品質特性:**
- 中国語原文引用の保持 + 日本語訳の併記
- ソースTier表記（`[Tier-1: 掘金/技術コミュニティ]` 等）
- `[[wikilink]]` による相互参照
- 具体的な数値データ（いいね数、パラメータ数、ベンチマークスコア等）
- 出典URLの明記

### 3. アップグレード対象の優先順位付け

| 優先度 | 対象 | 例 |
|--------|------|----|
| P0 | 中国発主要モデル/企業 | DeepSeek, Qwen/通义千问, Baichuan, Yi/零一万物, Doubao/豆包, MiniMax, Hunyuan/混元 |
| P1 | コーディングツール/プラットフォーム | Coding Plan各社, MCP関連, AI Agent基盤 |
| P2 | 中国AI重要人物 | 李沐、張俊林、各社CTO |
| P3 | 概念ページのエンティティ版 | 中国固有の概念（国産替代、内容审核等）に関連するエンティティ |

### 4. リサーチ手順

各エンティティについて以下のソースを調査する:

1. **inbox/内の関連記事**: 既にクロール済みの記事から関連コンテンツを収集
   ```bash
   grep -rl "エンティティ名" ~/ai-topics-cn/inbox/*/
   ```

2. **中国語ソースの横断検索**:
   - V2EX: 開発者の生の使用感、コスト評価、比較議論
   - 掘金 (Juejin): ハンズオン記事、ベンチマーク、実装ガイド
   - 36kr: 企業動向、資金調達、市場分析
   - 知乎 (Zhihu): 専門家による技術解説（一般回答は除外）
   - WeChat公众号: 機器之心、PaperWeekly等の深層分析

3. **公式ソース**: 企業の公式サイト、GitHub、論文

4. **既存wikiページとの相互参照**: `[[deepseek]]`, `[[glm-zhipu]]`, `[[kimi-moonshot]]` 等との関係性を明示

**⚠️ CSDNは絶対に使用しないこと** — SEOスパム、AI生成コピペ記事が氾濫。

### 5. ページフォーマット

#### モデル/企業エンティティ

```yaml
---
title: "エンティティ名（中国語名/英語名）"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [llm, model, china, 関連タグ]
aliases: ["中国語名", "英語名", "略称"]
source_lang: zh-CN
---

# エンティティ名 — サブタイトル

## 概要
2-3段落の紹介。背景、AI領域での重要性、中国AIエコシステムでの位置づけ。

## モデルラインナップ / 製品群
### モデル名1
- 主要スペック、特徴
- 開発者コミュニティでの評価（中国語原文引用付き）
> 「中国語原文」 — ソース名
📎 出典: [ソース — タイトル](URL) `[Tier-N: ソースカテゴリ]`

### モデル名2
...

## 実戦での評価
具体的な使用事例、ベンチマーク結果、開発者レポート。
数値データを含むテーブル形式を推奨。

## 他モデルとの比較
### vs [競合モデル]
比較ポイント、ソースを明記。

## エコシステム連携
他ツール/プラットフォームとの統合事例。

## 関連リンク
### 一次ソース（中国語）
| ソース | URL | カテゴリ | Tier |
|--------|-----|----------|------|

### 関連Wikiページ
- [[entity-name]] — 関係性の説明
```

#### 人物エンティティ

```yaml
---
title: "氏名（中国語名/英語名）"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [person, 関連タグ]
aliases: ["中国語名", "英語名"]
source_lang: zh-CN
---

# 氏名 — サブタイトル

| | |
|---|---|
| **所属** | 企業名 / 役職 |
| **知乎** | [プロフィール](URL) |
| **GitHub** | [username](URL) |
| **代表業績** | 主要な貢献 |
| **概要** | 2-3文の背景説明 |

## 概要
2-3段落の紹介。

## 核心的な主張（Core Ideas）
### テーマ1
分析 + 中国語原文引用

### テーマ2
分析 + エビデンス

## 主要業績
- プロジェクト、論文、講演

## 中国AI業界での影響
中国語圏コミュニティでの影響力と議論。

## 関連人物
- [[entity-name]] — 関係性の説明

## ソース
- URL 1
- URL 2
```

### 6. バッチ処理

- サブエージェントあたり2-3エンティティ（並列最大4）
- 類似ドメインでグループ化（中国LLM企業群、コーディングツール群、人物群など）
- 各バッチ後: 監査 → コミット → プッシュ → 次バッチ
- 絶対パス `/home/exedev/ai-topics-cn/wiki/entities/` を常に指定

### 7. 検証とコミット

```bash
# ファイルサイズ確認
ls -la ~/ai-topics-cn/wiki/entities/*.md | sort -k5 -n -r | head -20

# スケルトン残存チェック
grep -l 'status: skeleton' ~/ai-topics-cn/wiki/entities/*.md

# index.mdとlog.mdを更新後、コミット
cd ~/ai-topics-cn && git add wiki/ && git commit -m "wiki: upgrade entities (batch N)" && git push
```

## Output

- アップグレード済みエンティティページ（8-15KB目標）
- 中国語原文引用 + 日本語訳の併記
- ソースTier表記付きの出典リンク
- `[[wikilink]]` による相互参照ネットワーク
- wiki/index.md と wiki/log.md の更新
- git commit & push

## 注意事項

- **CSDNソースは絶対に使用しないこと** — SCHEMA.md、SOUL.md双方で明示的に禁止
- 知乎は「専門家回答」のみ採用。フォロワー数・回答の専門性で判断
- 中国語原文引用は原文のまま保持し、日本語訳を併記する（SCHEMA.md準拠）
- 固有名詞は中国語原表記を優先（例: 通义千问/Qwen、智谱/Zhipu）
- 矛盾する情報がある場合は `> [!warning] 矛盾` コールアウトブロックを使用
- ソース信頼度Tier（SOUL.md準拠）を常に明記する

## 既知の注意点

1. **サブエージェントのパス問題**: サブエージェントが `~/.hermes/hermes-agent/wiki/entities/` に書き込むことがある。常に完了後に確認し、必要に応じてコピー:
   ```bash
   cp ~/.hermes/hermes-agent/wiki/entities/*.md ~/ai-topics-cn/wiki/entities/
   ```

2. **ファイル名エイリアス**: サブエージェントが指定と異なる名前でファイルを作成する場合がある。バッチ後に `ls -lat` で新規ファイルを確認し、重複を整理。

3. **バジェット枯渇**: delegate_taskの50イテレーション制限。3エンティティ以上のバッチでは `exit_reason: max_iterations` が発生しうる。バッチ後に必ず監査スクリプトを実行。

4. **エンティティタイプの混同**: モデル、企業、人物で異なるフォーマットを使う。スキップすべき非エンティティページ（概念ページ等）に注意。
