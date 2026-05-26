# Deep Research: Vibe Coding in China — Latest Developments (2026-05-26)

## Task
Deep research on Vibe Coding (中国氛围编程) latest developments since last wiki update (2026-05-20).

---

## 1. New Developments Since 2026-05-20

### A. Google I/O 2026: Antigravity 2.0 — "Vibe Coding as Default" (May 19-20)

| Event | Detail |
|-------|--------|
| **Antigravity 2.0** | Standalone desktop app, CLI, SDK, Managed Agents in Gemini API |
| **Gemini 3.5 Flash** | Co-developed with Antigravity 2.0, 4x faster than competing frontier models |
| **Google AI Studio** | Native Android vibe coding (Kotlin support), one-click Cloud Run deploy, Workspace integration |
| **OS-in-12-hours demo** | 93 sub-agents, billions of tokens, built an OS for under $1,000 |
| **AI Ultra plan** | $100/month, 5x higher Antigravity limits than Pro |
| **Key framing** | "From AI that assists, to agents that independently navigate complex tasks" |

**Sources:**
- https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- https://thenewstack.io/google-io-antigravity-codemender-ai-agentic/
- https://www.digit.in/news/general/google-io-2026-google-claims-antigravity-20-created-an-operating-system-in-12-hours-brings-vibe-coding-to-android.html
- https://ppc.land/gemini-3-5-and-antigravity-2-0-headline-google-i-o-2026-reveal/
- https://cloud.google.com/blog/products/databases/vibe-coded-ai-studio-apps-with-firestore-firebase-cloud-sql

### B. Anthropic Mythos & Project Glasswing Update (May 22)

| Event | Detail |
|-------|--------|
| **SWE-bench 93.9%** | Mythos Preview at 93.9% — first model over 90%, +13.1pp over Opus 4.6 |
| **Glasswing results** | 10,000+ high/critical vulnerabilities found across 50+ partners in one month |
| **Mythos 1 "preview"** | Appearing in Claude UI on Google Cloud Vertex AI (May 16-23) |
| **Claude Security** | Public beta for Enterprise; 2,100+ vulnerabilities patched in 3 weeks |
| **Recursive Self-Improvement** | Karpathy's team at Anthropic focused on using Claude to accelerate pre-training research |
| **Jack Clark prediction** | 60% probability of full autonomous AI R&D by end of 2028 |

**Sources:**
- https://www.anthropic.com/research/glasswing-initial-update
- https://www.engadget.com/2180028/anthropic-claude-mythos-preview-project-glasswing-update/
- https://www.testingcatalog.com/anthropic-prepares-mythos-1-for-claude-code-and-claude-security/
- https://cybersecuritynews.com/claude-mythos-moves-toward-public/
- https://36kr.com/p/3817196535071624
- https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/

### C. ProgramBench: New地狱级 Coding Benchmark (May 5-11, breakthrough May 23-25)

| Metric | Data |
|--------|------|
| **Fully resolved (all models)** | 0% initially — all 9 top models (Claude, GPT, Gemini) |
| **Tasks** | 200 tasks: jq, ripgrep, FFmpeg, SQLite, PHP compiler, DuckDB |
| **Tests** | 248,000+ behavioral tests, agent-driven fuzzing |
| **GPT-5.5 xhigh** | First model to fully resolve a task (0.5%) — cmatrix by C and Python |
| **Claude Opus 4.7** | Best "almost resolved" at 3.0% |
| **Key insight** | ProgramBench tests system-level engineering, not patch-level coding |
| **Implication** | "SWE-bench at 80%+ = ProgramBench at 0%". Gap measured precisely. |

**Sources:**
- https://36kr.com/p/3798593895930888
- https://36kr.com/p/3807610197384968
- https://programbench.com/
- https://arxiv.org/abs/2605.03546
- https://github.com/facebookresearch/ProgramBench

### D. Cursor $50B Valuation & SpaceX Option (April-May 2026)

| Metric | Data |
|--------|------|
| **Valuation** | $50B pre-money (raising $2B+) |
| **ARR** | $2B (Feb 2026), projected $6B by year-end |
| **Enterprise** | 70% Fortune 1000, 30,000+ enterprise customers |
| **SpaceX option** | $60B acquisition option, $10B breakup fee, xAI's Colossus compute |
| **Investors** | A16z, Thrive, Nvidia, Battery Ventures; round oversubscribed |
| **Employees** | ~600 (!!) — generating $3.3M ARR per employee |

**Sources:**
- https://startupsworld.news/market-movers/cursor-50b-saas-playbook-dead/
- https://www.todaysstartupnews.com/startups/cursor-is-raising-2-billion-at-a-50-billion-valuation-three-years-ago-it-did-not-exist
- https://finimize.com/content/cursors-revenue-run-rate-hit-3-billion-as-spacex-deal-waits
- https://sacra.com/c/cursor/

### E. 36kr Major Coverage — "Coding的中场战事" & Critical Analysis (May 2026)

Several major articles from 36kr covering the AI programming landscape:

1. **"Coding的中场战事" (Mid-Battle of Coding)** — Comprehensive analysis of AI coding agent wars: Claude Code vs Codex vs Gemini, price wars, compute wars, ProgramBench shock
2. **"Claude吞噬整个AI编程栈"** — Claude Code source code leak (1900 TypeScript files, 510K+ lines), Anthropic building full-stack from model→CLI→GUI→OS-level
3. **"如何正确Vibe Coding"** — Anthropic's Erik Schluntz masterclass: 15-20 min pre-planning, 22,000-line production merge, TDD essential
4. **"氛围编程行不通，CTO们集体炮轰"** — CTOs criticize Vibe Coding for production: "not unemployment, but loss of control"
5. **"外行式Vibe Coding正跟专业的Agent工程走向融合"** — Simon Willison: Vibe Coding + Agentic Engineering converging, "semi-blackbox" trust emerging

**Sources:**
- https://36kr.com/p/3815446937820932
- https://36kr.com/p/3764989164307202
- https://36kr.com/p/3774648797659657
- https://36kr.com/p/3436216442424713
- https://www.infoq.cn/article/uLLYdtZdZu9sCQSyUcst

### F. Claude Code Pricing Shock & Codex Advantage (mid-May 2026)

| Event | Detail |
|-------|--------|
| **Claude Code** | Free tier cut from 250→80 calls/month, Friday evening announcement |
| **Community reaction** | "We just put our entire CI/CD pipeline on Claude Code... what about Monday's deployment?" |
| **OpenAI response** | Sam Altman: "No quotas" — Codex free for 2 months, ~$400M subsidy |
| **Developer migration** | "Claude Code you're done, I'm switching to Codex" — trending on 36kr |
| **Token pricing changes** | Opus 4.7 tokenizer change = 40% more tokens for same content (de facto price hike) |

**Sources:**
- https://36kr.com/p/3815446937820932
- https://36kr.com/p/3348336694778760

### G. Trae (ByteDance) May 2026 Updates

| Event | Detail |
|-------|--------|
| **Trae SOLO mobile** | Launched May 5 — mobile AI development assistant |
| **Trae Skills** | MCP-based skill system, Spec Coding workflows, Feishu integration |
| **Free strategy** | 14-day Pro trial, $3/mo Lite, $10/mo Pro — most generous in market |
| **Users** | 600万+ registered, daily 150万+ queries, 60亿+ lines of code accepted |
| **Multi-model** | Claude 4.6 Sonnet, GPT-4o, Gemini 2.5 Pro, DeepSeek R1 all built-in |

**Sources:**
- https://developer.volcengine.com/articles/7636955544025464841
- https://forum.trae.cn/t/topic/17840
- https://weavai.app/blog/zh-cn/2026/05/08/2026-trae-ai-评测/
- https://tianqi.csdn.net/6a0bffa0662f9a54cb759e8f.html

### H. 腾讯吐司 (Toast) Post-Launch Analysis (May 18+)

| Metric | Detail |
|--------|--------|
| **Platform** | APK-native app generation, vs Ant Lingguang's HTML-based "flash apps" |
| **Core loop** | Idea → AI decompose → Preview → Multi-turn revision → APK → Install |
| **Limitations** | 5 free attempts, ~20-30 min per app (preview+packaging), Android-only |
| **Differentiation** | Real APK app with offline capability, home screen icon, shareable |
| **Ecosystem** | "Inspiration Square" for sharing/remixing, future App Store ambitions |
| **Versus Lingguang** | Lingguang: 30秒, HTML, 3000万 apps generated. Toast: real APK, slower, more permanent |

**Sources:**
- https://cloud.tencent.com.cn/developer/news/3918372
- https://www.163.com/dy/article/KT7F31Q0519CUHG.html
- https://www.163.com/dy/article/KT88NJLV051100B9.html
- https://www.faxai.cn/archives/8059

### I. Karpathy at Anthropic — Deep Analysis (May 19+)

| Aspect | Detail |
|--------|--------|
| **Role** | Pre-training team under Nick Joseph, leading new team focused on using Claude to accelerate pre-training research |
| **RSI focus** | Recursive Self-Improvement — AI improving its own training process |
| **Significance** | "You can't be at the frontier if you go solo" — Karpathy chose Anthropic over OpenAI |
| **Mythos capabilities** | Model autonomously found zero-days in FreeBSD (17yr), OpenBSD (27yr), FFmpeg (16yr) |
| **Industry reaction** | Third OpenAI founder to join Anthropic (after Jan Leike, John Schulman) |
| **36kr analysis** | "Karpathy's position: not VP but pre-training team member — bet on pre-training, not agent layer" |

**Sources:**
- https://www.163.com/tech/article/KTCBDJUK00097U7T.html
- https://www.36kr.com/p/3816490198475011
- https://www.odaily.news/zh-CN/post/5210873
- https://perplexityaimagazine.com/ai-news/andrej-karpathy-joins-anthropic-pretraining-team-2026/

---

## 2. What Needs Updating in the Wiki Page

### Sections requiring major additions:

1. **「2026-05-20 〜 2026-05-26 最新動向」— New section needed** (currently only has up to 5/20)
   - Google I/O 2026 Antigravity 2.0
   - ProgramBench + GPT-5.5 breakthrough
   - Mythos Glasswing update + Claude Security
   - Cursor $50B / SpaceX deal
   - Claude Code pricing shock
   - 36kr "Coding的中场战事" analysis

2. **Section 11 (Anthropic Code w/ Claude 2026) — Update market share data**
   - Mythos at 93.9% SWE-bench changes everything
   - Claude Code pricing changes
   - Need updated market share numbers

3. **Section 8 (Karpathy @ Sequoia AI Ascent) — Add post-Anthropic context**
   - Karpathy's actual role at Anthropic
   - RSI (Recursive Self-Improvement) implications

4. **Section 1 (Vibe Coding定义) — Update timeline**
   - May 19: Karpathy joins Anthropic
   - May 19-20: Google I/O / Antigravity 2.0
   - May 22: Glasswing report (10,000+ vulns)
   - May 23: GPT-5.5 breaks ProgramBench
   - May 15: Claude Code pricing cut

5. **Section 5 (中国AI编程ツール市場) — Add Antigravity as global competitor**
   - Google Antigravity 2.0 directly competes with both Cursor and Chinese tools

6. **Section about Project Glasswing/Mythos** — New section needed
   - Mythos represents "next generation" beyond Agentic Engineering
   - SWE-bench 93.9% ceiling
   - Security implications for enterprise adoption

### New sections to add:

- **「ProgramBench — AIプログラミングの新たな壁」** (New benchmark section)
- **「Google Antigravity 2.0 — Vibe Codingのプラットフォーム化」** (Google entering the fray)
- **「Cursor $50B — AIコーディングツールの経済学」** (Market economics)
- **「Claude Mythos — Agentic Engineeringの次へ」** (Mythos as step beyond)
- **「Claude Code価格改定とCodexの応酬」** (Pricing wars)

---

## 3. New Search Hints to Add

```yaml
search_hints:
  - "ProgramBench AI coding 0% 2026 5月"
  - "Google Antigravity 2.0 vibe coding 2026 5月"
  - "Anthropic Mythos 93.9% SWE-bench 2026"
  - "Claude Code pricing cut 80 calls 2026 5月"
  - "Cursor $50B valuation SpaceX 2026"
  - "GPT-5.5 ProgramBench breakthrough 2026"
  - "Project Glasswing 10000 vulnerabilities 2026"
  - "36氪 coding中场战事 2026 5月"
  - "Karpathy Anthropic Claude pre-training RSI 2026"
  - "Claude Code 源码泄露 51万行 TypeScript 2026"
  - "Trae SOLO mobile 字节跳动 2026 5月"
  - "腾讯吐司 应用宝 灵感广场 共创 2026"
```

---

## 4. Key Findings in Japanese (日本語サマリー)

### 2026年5月20日〜26日：中国Vibe Coding / Agentic Engineering最新動向

**最重要トピックス：**

1. **Google I/O 2026 (5/19-20)**: Antigravity 2.0発表。Vibe Codingを「デフォルト」に。Androidアプリを自然言語で生成、OSを12時間でビルド（93サブエージェント、$1,000以下）。AI Studio + Antigravity + Cloud Runのフルスタック展開。

2. **Karpathy、Anthropic入社 (5/19)**: プリトレーニングチームに所属、Claudeを使ってプリトレーニング研究を加速する新チームを指揮。「RSI（再帰的自己改善）」にコミット。2年以内にOpenAIからAnthropicに移った3人目の核心的人物。

3. **ProgramBench — 全モデル0%の衝撃 (5/5〜11、5/23〜25)** : SWE-Bench作者による新ベンチマーク。FFmpeg・SQLite等200タスク、全モデル0%完全解決。5/23 GPT-5.5 xhighが初のタスク解決（0.5%）。「コード修正≠ソフトウェア設計」。中国では36氪が大々的に報道。

4. **Anthropic Mythos & Glasswing (5/22)**: SWE-bench 93.9%(初の90%超)。1ヶ月で10,000以上の脆弱性を発見。Mythos 1がClaude Code + Claude Securityへの統合準備中。一般公開への布石か。

5. **Cursor $50B評価額 (4〜5月)**: ARR $2B(2月)→$6B(年末予測)。SpaceXが$60Bの買収オプション。70% Fortune 1000採用。Nvidia・a16z主導。

6. **Claude Code価格ショック**: 無料枠を250→80コール/月に突然削減。OpenAI Codexが「No quotas」で対抗。開発者がClaude CodeからCodexへ移行。

7. **36氪「Codingの中場戦事」(5月)**: AIプログラミング戦争の包括的分析。ProgramBench 0%、Claude Code vs Codex価格戦争、Anthropicがスタック全体を飲み込む戦略。Vibe CodingとAgentic Engineeringの融合が進行中。

8. **中国プラットフォーム競争**: 腾讯「吐司」(APK生成、リアルアプリ) vs 蚂蚁「灵光」(30秒HTML、3000万アプリ) vs 字节「Trae」(600万ユーザー、無料戦略)。3極化。

**総評**: 
- Vibe CodingからAgentic Engineeringへの移行は不可逆的
- ProgramBenchは「次のフロンティア」を正確にマッピング
- Mythosクラスモデルが「Agentic Engineeringの次」を示唆
- 中国市場では「誰でもアプリを作れる」C端プラットフォーム戦争が激化
- $50B評価額のCursorが示す：AIコーディング市場は異常な速度で拡大中
- Google I/Oが示した：Vibe Codingは「検索のデフォルト結果」になりつつある
