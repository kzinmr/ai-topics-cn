# Wiki Schema — 中国語圏 AI Topics Knowledge Base

## Domain
中国語圏のLLM/AI Agent技術議論 — 大規模言語モデル、AIエージェント、コーディングエージェント、開発ツール、推論/訓練インフラ、プロンプトエンジニアリング、AI安全性、オープンソースAI、中国特有の規制・エコシステム動向。

## 言語規則
- **Wikiページ**: 日本語で記述
- **原文引用**: 中国語原文を保持、日本語訳を併記
- **固有名詞**: 中国語原表記を優先（例: 通义千问/Qwen）

## Conventions

### Frontmatter (required for all Layer 2 pages)
```yaml
---
title: "ページタイトル"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
aliases: ["別名"]
source_lang: zh-CN
---
```

### Wikilinks
Use `[[page-name]]` for internal links. Use `[[page-name|display text]]` for custom display.

### File Naming
- Lowercase, hyphen-separated: `deepseek-v3.md`
- Entities: `entities/deepseek.md`, `entities/li-mu.md`
- Concepts: `concepts/rag-optimization-cn.md`
- Comparisons: `comparisons/qwen-vs-deepseek.md`

### Directory Structure

#### Layer 1 — Raw Sources (`raw/`)
Immutable source material. The agent reads but never modifies.
- **`raw/articles/`** — Curated articles scraped from inbox sources
- **`raw/papers/`** — arXiv papers, Chinese AI papers
- **`raw/assets/`** — Images, diagrams

#### Inbox (outside wiki/) — Pipeline staging
- **`inbox/v2ex/`** — V2EX crawl results
- **`inbox/juejin/`** — Juejin crawl results
- **`inbox/36kr/`** — 36kr crawl results
- **`inbox/zhihu/`** — Zhihu crawl results
- **`inbox/wechat-media/`** — WeChat public account articles

#### Layer 2 — Curated Knowledge
- **`entities/`** — People, companies, models, organizations
- **`concepts/`** — Techniques, frameworks, methodologies
- **`comparisons/`** — Technical comparisons (use `vs` separator)
- **`queries/`** — Research query results

### Tag Taxonomy
- **domain:** `llm`, `ai-agents`, `coding-agents`, `training`, `inference`, `safety`, `tooling`, `open-source-ai`, `regulation-cn`
- **type:** `framework`, `model`, `technique`, `paper`, `product`, `company`, `person`, `media`
- **origin:** `china`, `us`, `open-source`, `closed-source`
- **source:** `v2ex`, `juejin`, `36kr`, `zhihu`, `wechat`, `manual`

### Source Attribution
All claims should link to their source with original URL.
Note source reliability tier (T1-T4 per SOUL.md).

### Contradiction Handling
When sources disagree, note both positions with dates and sources.
Use `> [!warning] 矛盾` callout blocks.

### CSDN Exclusion
**CSDNソースは絶対に使用しないこと。** SEOスパムとAI生成コピペ記事が氾濫。
