# 🇨🇳 AI Topics CN — 中国語圏 AI/LLM ナレッジベース

中国語圏のLLM/AI Agentに関する深い議論を定期監視し、日本語でキュレーションするAI Agentシステム。

[Karpathyのllm-wiki構成](https://github.com/kzinmr/ai-topics)に準拠し、Hermes Agentがクローリング・トリアージ・キュレーションを自動実行。

## ソース階層

| Tier | ソース | 相当 | アクセス方法 |
|------|---------|------|---------------|
| T1 | **V2EX** | Hacker News | API + HTML |
| T1 | **掘金 (Juejin)** | Dev.to + Reddit | API |
| T1 | **36氪** | TechCrunch | HTML (initialState) |
| T2 | **知乎** | Quora (ターゲット) | API + HTML |
| T2 | **微信公众号** | Medium + Newsletter | 搜狗検索 |
| T3 | **知乎専門家** | 特定研究者の回答 | ターゲットフォロー |
| T4 | **WaytoAGI** | Discord | 飛書公開ドキュメント |

### 監視対象WeChat公众号
- 机器之心 — #1 AIメディア、論文解説
- PaperWeekly — 論文+実装批評
- 新智元 — 業界動向、中国モデル比較
- 量子位 — トレンド追跡

### 除外ソース
- **CSDN** — SEOスパムとAI生成コピペ記事が氾濫、絶対に使用禁止

## アーキテクチャ

```
Layer 1: Raw Sources (inbox/)
  クローラー → inbox/{v2ex,juejin,36kr,zhihu,wechat-media}/
  6時間ごとに自動実行 (systemd timer)

Layer 2: Curated Wiki (wiki/)
  Hermes Agent → entities/, concepts/, comparisons/
  12時間ごとにトリアージ (shelley timer)

Layer 3: Dashboard
  Go web server → https://hermes-china-digest.exe.xyz:8000/
```

## コマンド

```bash
# 全ソースクロール
python3 scripts/crawl_all.py

# 特定ソースのみ
python3 scripts/crawl_all.py --source v2ex --limit 20
python3 scripts/crawl_all.py --source juejin --limit 20
python3 scripts/crawl_all.py --source 36kr --limit 20

# Tier 1のみ
python3 scripts/crawl_all.py --tier 1 --limit 15

# トレンディング分析
python3 scripts/trending_topics.py --days 3

# 個別クローラー
python3 scripts/crawl_v2ex.py --limit 30
python3 scripts/crawl_juejin.py --limit 30
python3 scripts/crawl_36kr.py --limit 30 --no-detail
python3 scripts/crawl_zhihu.py --limit 20
python3 scripts/crawl_wechat_media.py --account "机器之心"
```

## ディレクトリ構成

```
ai-topics-cn/
├── wiki/                    # Layer 2: キュレート済みナレッジ
│   ├── entities/            # 人物・企業・モデル
│   ├── concepts/            # 技術・手法
│   ├── comparisons/         # 比較分析
│   ├── raw/articles/        # キュレート済み原文
│   ├── index.md             # Wikiインデックス
│   ├── log.md               # 操作ログ
│   └── SCHEMA.md            # Wikiスキーマ定義
├── inbox/                   # Layer 1: クロール結果
│   ├── v2ex/
│   ├── juejin/
│   ├── 36kr/
│   ├── zhihu/
│   └── wechat-media/
├── config/hermes/           # Agent設定
│   ├── SOUL.md              # Agentペルソナ
│   └── skills/              # Agentスキル
├── scripts/                 # クローラー・分析ツール
├── srv/                     # Go Webダッシュボード
└── bin/                     # ビルド済みバイナリ
```

## 中国語圏の特徴

1. **中国産モデルが議論の中心**: Qwen, DeepSeek, ChatGLM, Yi, Kimi, 豆包
2. **ローカルデプロイ重視**: VRAM最適化、量子化、検閲回避
3. **規制コンテキスト**: コンテンツモデレーション、データローカリゼーション
4. **WeChatエコシステム**: 最も深い議論は非公開WeChatグループ内
5. **スピード**: 中国メディアは英語論文を数時間以内に翻訳・解説
