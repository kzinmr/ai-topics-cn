---
name: semantic-article-grouping
description: Group crawled Chinese AI articles from inbox by semantic similarity and assess wiki value
category: research
version: 1.0.0
author: hermes
license: MIT
metadata:
  hermes:
    tags: [Grouping, Triage, Chinese-AI, Semantic-Analysis]
---

# Semantic Article Grouping（中国語ソース版）

## Purpose

inbox/{v2ex,juejin,36kr,zhihu,wechat-media}/ に蓄積されたクロール済み中国語AI記事を意味的類似性に基づいてグループ化し、wiki取り込み優先度を判定する。中国語圏特有のトピック構造（国産モデル競争、規制動向、ローカルデプロイ文化）を考慮したグルーピングを行う。

## Steps

### 1. インボックス記事の探索
```bash
# 全ソースからの記事一覧と件数
for src in v2ex juejin 36kr zhihu wechat-media; do
  count=$(find ~/ai-topics-cn/inbox/$src/ -name '*.md' 2>/dev/null | wc -l)
  echo "$src: $count articles"
done
```

各記事ファイルを読み取り、サイズが1000バイト以上のものを実質的な記事として選別する。

```python
import os
inbox_dir = os.path.expanduser("~/ai-topics-cn/inbox")
sources = ["v2ex", "juejin", "36kr", "zhihu", "wechat-media"]
files = []
for src in sources:
    src_dir = os.path.join(inbox_dir, src)
    if not os.path.isdir(src_dir): continue
    for f in os.listdir(src_dir):
        if not f.endswith('.md'): continue
        path = os.path.join(src_dir, f)
        size = os.path.getsize(path)
        if size > 1000:
            files.append((src, f, size))
files.sort(key=lambda x: -x[2])
print(f"Total substantive articles: {len(files)}")
```

### 2. コンテンツメタデータ抽出

各記事から以下を抽出する：
- **タイトル**（中国語原文）
- **URL**（元ソース）
- **キーフレーズ**（中国語のまま保持）
- **言及エンティティ**: モデル名（DeepSeek, Qwen, GLM, Kimi, Doubao等）、企業名、人名
- **ソースカテゴリ**: V2EX=開発者議論, Juejin=実践技術, 36kr=ビジネス/産業, Zhihu=学術的分析, WeChat=深層分析
- **既存wikiトピックとのマッチ**: `wiki/entities/`, `wiki/concepts/` 内の既存ページとの照合

### 3. セマンティックグルーピング基準

以下の軸で記事をグループ化する：

- **共有エンティティ**: 同一モデル/企業/人物への言及
  - 例: DeepSeek関連記事群、Qwen関連記事群
- **関連コンセプト**: 技術的な関連性
  - 例: RAG最適化 ↔ ベクトルDB ↔ 長文脈処理
- **イベントクラスタ**: モデルリリース、規制発表、価格戦争
  - 例: GLM-5オープンソース化に関する複数ソース記事
- **ソース横断テーマ**: 同一トピックの多角的報道
  - 例: 同じモデルについてV2EX（開発者評価）+ 36kr（ビジネス分析）+ Juejin（実装ガイド）

#### 中国語圏特有のグルーピングパターン

| パターン | キーワード例 | グループ化方法 |
|----------|-------------|---------------|
| 国産モデル競争 | 国产大模型, 降价, 价格战, 开源 | 企業/モデル別にグループ |
| ローカルデプロイ | 本地部署, 量化, VRAM, ollama | 技術テーマ別にグループ |
| 規制動向 | 监管, 合规, 内容审核, 备案 | 政策テーマ別にグループ |
| コーディングエージェント | Claude Code, Cursor, Coding Plan, 编程 | ツール別にグループ |
| AI安全性 | 对齐, alignment, 安全, 越狱 | コンセプト別にグループ |

### 4. 価値評価マトリクス

各グループのwiki取り込み価値を5段階で評価する：

- ★★★★★ = 新規コンセプトページまたはエンティティページの作成が必要
- ★★★★☆ = 既存ページの重要な更新が必要
- ★★★☆☆ = 既存エンティティページで言及すべき内容
- ★★☆☆☆ = 軽微な言及のみ（ログ記録で十分）
- ★☆☆☆☆ = wiki価値なし（宣伝記事、重複、表層的報道）

#### ソース信頼度によるバイアス補正

| ソース | 信頼度 | 備考 |
|--------|--------|------|
| V2EX | Tier-1 | 開発者の生の声、具体的な経験談に価値 |
| 掘金 (Juejin) | Tier-1 | コードレベルの実践知に価値 |
| 36kr | Tier-1 | 産業分析・ビジネス動向に価値 |
| 知乎 (Zhihu) | Tier-3 | 専門家回答のみ高価値、一般回答は低品質 |
| WeChat公众号 | Tier-2 | 機器之心・PaperWeekly等は高品質、それ以外は要注意 |
| CSDN | 除外 | **絶対に使用しない** — SEOスパム、AI生成コピペ |

### 5. 出力フォーマット

```markdown
### 📊 グループ N: [トピック名]
**代表トピック:** `[canonical-name]`
**ソース横断度:** [何ソースから言及があるか]

| ソース | 記事 | 内容 |
|--------|------|------|
| V2EX | [title] ([size]) | [1文要約・日本語] |
| Juejin | [title] ([size]) | [1文要約・日本語] |
| 36kr | [title] ([size]) | [1文要約・日本語] |

**Wiki追加価値:** [★評価] - [推奨アクション]
**関連既存ページ:** [[existing-page]] （あれば）
```

### 6. 推奨アクション

- **Create（新規作成）**: ★★★★★グループ → 新規エンティティ/コンセプトページ
- **Update（更新）**: ★★★★☆グループ → 既存ページに新セクション追加
- **Mention（言及追加）**: ★★★☆☆グループ → 既存ページ内で言及
- **Log（記録のみ）**: ★★☆☆☆グループ → wiki/log.md に記録
- **Skip（スキップ）**: ★☆☆☆☆グループ → 処理不要

### 7. 処理後のクリーンアップ

```bash
# 処理済み記事をraw/articles/に移動（wiki価値ありの場合）
mv inbox/{source}/{article}.md wiki/raw/articles/

# index.mdとlog.mdを更新
# git commit & push
cd ~/ai-topics-cn && git add wiki/ inbox/ && git commit -m "wiki: semantic grouping batch N" && git push
```

## Output

- グルーピング結果レポート（日本語）: 全グループの一覧、価値評価、推奨アクション
- 各グループの代表記事と要約（中国語原文タイトル + 日本語要約）
- wiki/log.md への作業記録追記
- 後続スキル（`cn-source-triage`, `wiki-entity-upgrade`）への入力データ
