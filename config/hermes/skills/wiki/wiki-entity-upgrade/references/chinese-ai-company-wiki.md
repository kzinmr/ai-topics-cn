---
name: chinese-ai-company-wiki
description: Create and register Chinese AI company entity pages in the ai-topics-cn wiki from ranking lists and news sources.
category: wiki
---

# Chinese AI Company Wiki Entry Creation

## When to Use
- User asks to register Chinese AI companies from a ranking list (e.g., Hurun, 36kr awards)
- User asks to add company entities to the wiki from a specific URL or topic
- User provides a brief description of companies (e.g., robotics firms, EV companies) and asks to create wiki pages
- Discovering notable Chinese AI companies worth tracking in the wiki

## Workflow

### 1. Research & Data Gathering

**Two approaches depending on prompt type:**

#### A. Ranking-list approach (existing)
Use multiple sources to cross-reference company information:

```
# Primary source: Yahoo Search (avoids CAPTCHA issues that Bing/Google have)
browser_navigate: https://search.yahoo.com/search?p=2025+top+AI+companies+China+ranking+list

# Key sources for Hurun/ranking data:
- hurun.cn (official Hurun rankings)
- 199it.com (data summary articles)
- sohu.com (detailed news articles — may require clicking "展开全文" to expand)
- baike.baidu.com (encyclopedia-style entries with company details)
- enkiai.com (market analysis with company profiles)
```

#### B. Prompt-driven approach (new — robotics, EV, hardware companies)
Use web_search with targeted queries in Chinese AND English. Gather:
- Shipment/sales numbers (出货量, 交付量, 年销量)
- Product models and specs (产品型号, 规格参数)
- Pricing (价格, 售价)
- Founders and company background (创始人, 成立)
- Market share and rankings (市场份额, 排名)
- Recent news/developments (最新消息, 动态)
- Funding rounds (融资轮次, 估值)
- Key technical breakthroughs (技术突破)

Example queries:
```
web_search: "Company中文 2025 2026 出货量 产品 创始人"
web_search: "Company English robotics humanoid 2025 2026"
web_search: "Company中文 融资 估值 供应链"
```

**Priority data points for robotics/hardware companies:**
1. 2025 actual shipment numbers (出货台数) — most important metric
2. 2026 targets/projections (2026年目标)
3. Product lineup with pricing (产品线+价格)
4. Market share in specific segments (细分市场占比)
5. Key partnerships (合作企业)
6. IPO status (上場状況)
7. Major competitors in the same category

### 2. Compile Company Data
For each company, gather:
- Chinese name (中文名)
- English name (if available)
- Founders, headquarters, founding year
- Company valuation/market cap
- Primary AI category (chip, LLM, CV, voice, autonomous driving, humanoid robot, drone, EV, etc.)
- Headquarters city
- Key products/technologies
- 2025/2026 shipment numbers and targets
- Market position and share
- Recent developments (IPO, funding, partnerships, new products)

### 3. Create Entity Pages

**A. Simple format** (from ranking lists — brief entries):

```markdown
---
title: CompanyName (中文名) — Brief Japanese description
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [company, category, china, subcategory]
aliases: ["EnglishName", "中文名", "AlternativeName"]
source_lang: zh-CN
---

# CompanyName (中文名) — Brief Japanese description

> **Hurun Rank**: #N (year)
> **Valuation**: XXXX亿元
> **Source**: 胡润研究院《2025胡润中国人工智能企业50强》
> **Important**: High/Medium — brief reason

## Overview

Brief description in Japanese of what the company does and its significance.

## Key Features

- **Feature 1**: Description
- **Feature 2**: Description
- **Feature 3**: Description

## Market Position

Description of the company's position in the Chinese AI landscape.

## Related Companies

- **Company A**: relationship
- **Company B**: relationship
```

**B. Detailed format** (from prompt-driven research — robotics, EV, hardware companies):

```markdown
---
title: CompanyName (中文名) — Brief Japanese description
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [company, category, china, subcategory]
aliases: ["EnglishName", "中文名", "AlternativeName"]
source_lang: zh-CN
---

# CompanyName (中文名) — Brief Japanese description

> **Founder**: 创始人
> **Founded**: YYYY年、所在地
> **Employees**: 従業員数
> **2025 Shipments**: 出货数 (world share X%)
> **2026 Target**: 目标数
> **IPO**: status
> **Importance**: High/Medium — brief reason

## Overview (概要)

Brief description in Japanese of what the company does, its significance, and key achievements (2-3 paragraphs).

## Product Lineup (主力製品)

| Model | Price | Features | Target |
|-------|-------|----------|--------|

Or if no table fits:
- **Product 1**: description
- **Product 2**: description

## Technical Features (技術特長)

- **Tech 1**: description
- **Tech 2**: description
- **Tech 3**: description

## Market Position (市場ポジション)

- 2025 shipment/shares
- 2026 targets
- Overseas sales ratio
- Key competitors and comparison
- Strategic challenges

## Business Developments (企業動向)

- IPO/funding status
- Key partnerships
- New product launches
- Strategic direction

## Related Companies (関連企業)

- **Company A**: competitive/complementary relationship
- **Company B**: relationship

## Sources (ソース)

- URL 1 — brief description
- URL 2 — brief description
```

**For index.md registration** (add to Entity section, sorted alphabetically):

```
|- [[company-slug|CompanyDisplay — Brief Japanese description]]
```

**Update statistics line** in index.md header:
```
エンティティ: N, コンセプト: N, ダイジェスト: N, ページ: N
```

### 4. Update index.md
Add entries to the Entity section in `~/wiki/index.md`. Keep alphabetical order. Use pipe syntax for descriptive display names:
```
|- [[company-slug|CompanyDisplay — Brief description]]
```

### 5. Commit
```bash
cd /opt/data/ai-topics-cn && git add wiki/ && git commit -m "feat: add N Chinese AI company wiki pages (names)" && git push
```

## Product-Level Entity Pages (Split-Out Pattern)

When a company's product or model has enough substance to warrant its own page:

### When to Create Separate Product Pages
- Product has **specific technical specs** that exceed what fits in a company page portfolio section (e.g., model architecture, benchmark scores, pricing)
- Product has **independent market traction** (user numbers, adoption metrics, separate brand identity)
- Product is a **major strategic bet** for the company (e.g., Tencent's Hy3 MoE, Baidu's ERNIE-Image 8B DiT)

### Product Page Format
```markdown
---
title: "Product Name (中文名) — Brief Japanese description"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [model, product, category, china]
aliases: ["ProductName", "中文名", "AlternativeName"]
source_lang: zh-CN
---

# Product Name (中文名) — Brief Japanese description

> **Parent Company**: [[company-slug|Company Name]]
> **Released**: YYYY-MM-DD
> **Type**: model-type (e.g., MoE LLM, DiT image model, Agent platform)
> **Parameters**: XXX (total/active if MoE)
> **Importance**: High/Medium — brief reason

## Overview
Brief description of the product's role and significance.

## Technical Specifications
| Spec | Value |
|------|-------|

## Architecture
- Key architectural decisions
- Training approach
- Differentiators from competitors

## Performance Benchmarks
| Benchmark | Score | Competitor Comparison |
|-----------|-------|----------------------|

## Ecosystem & Integrations
- Where is this product used?
- API/developer access
- Partner adoption

## Versions & Release History
| Version | Date | Changes |
|---------|------|---------|

## Related
- [[company-slug]] — Parent company
- [[competing-product]] — Competitor product
- [[concept]] — Related technology concept

## Sources
- URL 1 — brief description
```

### Linking from Company Page
Add a **product portfolio** section to the parent company page:
```markdown
### Product: Name
- Brief summary (2-3 lines)
- Key metrics
- **詳細**: [[product-slug]]
```
Then add to the company page's "関連" section:
```
- [[product-slug]] — Product description
```

## Pitfalls

- **Sohu articles** often hide full content behind "展开全文" (expand all) — click the link first, then use browser_console or curl to extract content
- **Baike pages** have lots of navigation chrome — focus on the article content after the heading
- **Hurun official site** may have JS-rendered content that doesn't appear in snapshots — try alternative news sources
- **Company name variations**: Chinese companies often have multiple romanizations (pinyin, English brand name, literal translation)
- **Tags consistency**: Use existing tags from other entity pages when possible (company, ai-chip, gpu, llm, china, startup, etc.)
- **Avoid duplication**: Check existing entities in `~/wiki/entities/` before creating new pages
- **Language**: Entity pages should be written in Japanese (matching the wiki's language)
- **Prioritize data from company official channels** (company website, official social media) over secondary sources for shipment numbers and product specs
- **Cross-reference with English sources** when Chinese sources are thin — IDC, Omdia, Reuters, Bloomberg often have good hardware company data
- **Shipment numbers are the #1 metric** for robotics companies — always include 2025 actuals + 2026 targets
- **Index.md alphabetical sorting** — maintain order when adding new entries, don't just append at the end
- **Page length**: aim for 1,500-5,000 characters per page. Too short (<1,000b) means insufficient research. Too long (>10KB) means include too much filler. **Exception**: product-level pages with detailed benchmarks/specs can exceed this if the data justifies it.
- **Source attribution**: always include URLs in a Sources section so readers can verify claims
- **Reference existing page format** (e.g., horizon-robotics.md) before creating new pages to ensure consistency
- **Product split-out**: when creating separate product pages, ALWAYS update the parent company page with a portfolio summary and cross-link. Don't orphan product pages.

## Priority Companies to Track
From Hurun 2025 AI Top 50, the most notable categories:

### AI Chip (7 of top 10)
- 寒武纪 (Cambricon) - #1
- 摩尔线程 (Moore Threads) - #2
- 沐曦 (MetaX) - #3
- 地平线 (Horizon Robotics) - auto AI chips
- 壁仞科技 (Biren Technology) - GPU
- 芯原股份 (VeriSilicon) - semiconductor IP
- 瑞芯微 (Rockchip) - AIoT SoC

### LLM/AIGC
- 月之暗面 (Moonshot AI / Kimi)
- 百川智能 (Baichuan AI)
- 阶跃星辰 (StepFun)
- MiniMax (稀宇科技)

### Computer Vision
- 商汤 (SenseTime)
- 云天励飞 (Intellifusion)
- 奥比中光 (Orbbec)

### Voice AI
- 科大讯飞 (iFlytek)
- 云知声 (Unisound)

### Other
- 晶泰科技 (XtalPi) - AI drug discovery
- 元戎启行 (DeepRoute.ai) - autonomous driving
- 燧原科技 (Enflame Technology) - AI accelerators
- 海光信息 (Hygon) - CPU/DCU
- 万兴科技 (Wanxing) - AIGC software
