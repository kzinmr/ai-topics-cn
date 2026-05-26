# Qwen (通义千问) Deep Research Findings
**Date**: 2026-05-26
**Research window**: 2026-05-21 → 2026-05-26 (post-wiki-update)

---

## 1. New Developments Since May 21

### 1.1 Qwen3.7-Max API Goes Live (May 21-23)

| Provider | Input Price | Output Price | Cache Input |
|----------|------------|-------------|-------------|
| **Alibaba Cloud Model Studio** | ¥12/1M tokens (~$1.71) | ¥36/1M tokens (~$5.14) | ¥1.2/1M tokens (90% off) |
| **OpenRouter** | $2.50/1M tokens | $7.50/1M tokens | $0.25/1M tokens (90% off) |
| **API易 (Direct)** | $1.7140/1M tokens | $5.1420/1M tokens | — |

**API Features**:
- OpenAI-compatible endpoint (model ID: `qwen3.7-max`)
- **Native Anthropic Messages Protocol** support — Claude Code & OpenClaw can use it by just changing `ANTHROPIC_BASE_URL`
- **1M token context** (doubled from 256K), **65,536 max output tokens**
- Explicit prompt caching for repeated contexts
- Two API key types: `sk-` (standard) and `sk-sp-` (Token Plan)

**Platform distribution**: OpenRouter (5/21), ofox.ai (5/21), Vercel AI Gateway (5/21), Together AI

Sources: [OpenRouter Qwen3.7-Max](https://openrouter.ai/qwen/qwen3.7-max), [ofox.ai Guide](https://ofox.ai/blog/qwen3-7-max-developer-guide-2026/)

---

### 1.2 Qwen3.7-Max Qwen Chat Integration (May 22)

- Integrated into **Qianwen App v6.9.7+, PC client, and Web**
- **Free for all users**
- **AA Intelligence Index: 56.6** (Global #5, Chinese #1)
- GPQA Diamond, HLE, HMMT 2026 Feb, IMOAnswerBench: exceeds Claude Opus 4.6 and all Chinese models
- IFBench (instruction following): **79.1**
- **31% token efficiency improvement** — increased output tokens due to reasoning density

Sources: [中关村在线](https://ai.zol.com.cn/1185/11851769.html), [新浪新闻](https://www.sina.cn/news/detail/5301737230701416.html)

---

### 1.3 Qwen3.7-Max Detailed Benchmark Breakdown

| Benchmark | Score | Comparison |
|-----------|-------|-----------|
| AA Intelligence Index | **56.6** | Global #5, #1 in China. Exceeds Gemini 3.5 Flash (55.3) |
| Terminal-Bench 2.0 Hard | **50.8% (+6.9)** | Exceeds DeepSeek-V4-Pro-Max, Claude Opus 4.6 |
| MCP-Atlas | **76.4** | Exceeds Opus-4.6 (75.8) |
| Skillsbench | **59.2** | Exceeds Kimi K2.6 (56.2) |
| MCP-Mark | **60.8** | Exceeds GLM-5.1 (57.5) |
| BFCL-V4 | **75.0** | Function calling leader |
| SpreadSheetBench-v1 | **87** | Office automation top |
| Kernel Bench L3 | **1.98x median speedup (96% win rate)** | GPU kernel optimization |

**35-hour autonomous run details**: Optimized Extend Attention kernel on Zhenwu M890 PPU. 1,158 tool calls, 432 kernel evaluations, 5 architecture candidates iteratively generated. **10x geometric mean speedup** vs Triton reference. Firethering analysis (5/25): GLM 5.1 (7.3x), Kimi K2.6 (5x), DeepSeek V4 Pro (3.3x) all surpassed.

Source: [Alibaba Cloud Blog](https://www.alibabacloud.com/blog/qwen3-7-the-agent-frontier_603154)

---

### 1.4 Qwen Code v0.16.0 (May 21) / v0.16.1 (May 23)

**v0.16.0** (80+ PRs, 25K GitHub stars):
- OSC 8 clickable hyperlinks in terminal
- Worktree isolation (EnterWorktree/ExitWorktree)
- `qwen serve` daemon (Stage 1) with `/demo` debug page
- `/goal` command with judge-driven turn continuation
- `/diff` per-turn interactive dialog
- `/stuck` diagnostic skill for frozen sessions
- `/rewind` file restoration support
- Auto approval mode (LLM classifier)
- NotebookEdit tool for Jupyter notebooks
- Status line presets with interactive dialog
- **ModelScope** built-in as third-party API provider
- Progressive MCP (no longer blocks first input)
- Batch session deletion
- Ink 6 → 7.0.3 upgrade
- Qwen3.6-35B-A3B quant variants: image+video support
- Telemetry Phase 2-4a (TTFT capture, trace tree, custom resource attributes)

**v0.16.1 hotfix**:
- Windows Git Bash (MinTTY) rendering fix — OSC 8 gated on mintty ≥ 3.3
- tool_use↔tool_result invariant across all failure paths
- Tab-indented notebook formatting preserved
- React reconciler PerformanceMeasure leak fix
- Express 4.21.2 → 5.2.1

Issue: [#4420](https://github.com/QwenLM/qwen-code/issues/4420) — UI regression on Windows Git Bash (v0.16.0), fixed in v0.16.1 via PR [#4451](https://github.com/QwenLM/qwen-code/pull/4451).

Sources: [GitHub v0.16.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.0), [v0.16.1](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.1)

---

### 1.5 千问云 (Qianwen Cloud) — Agent-Native AI Platform (May 20, reported May 21-22)

**URL**: [www.qianwenai.com](https://www.qianwenai.com)
**Concept**: Alibaba's first independent product website in 17 years outside the main Alibaba Cloud site. The homepage shows one line instead of product listings:

```
npx skills add QianWen-AI/qianwen-ai
```

This is an **Agent-readable prompt instruction** — agents can parse and autonomously learn all platform capabilities.

**Architecture**:
- **Skills** (9 modules): Text gen/chat, image/video understanding, image/video gen, TTS, model selector, auth, usage, update check
- **CLI**: Login, status, diagnostics, model search, API calls, usage stats
- **MCP**: All model services exposed via Model Context Protocol

**Scale**: 150+ model series, 480+ models (Qwen, GLM, Kimi, DeepSeek, Wan, HappyHorse)

**Supported agent frameworks**: OpenClaw, Hermes Agent, Claude Code, Qoder

**Strategic significance**: First major cloud vendor to redesign a product website with agents as primary users rather than humans. "The consumer of the cloud is changing from humans to agents" — Alibaba Cloud CTO Li Feifei.

Sources: [TestingCatalog](https://testingcatalog.net/alibaba-launches-qianwen-cloud-a-website-designed-for-ai-agents/), [品玩](https://www.pingwest.com/a/313885), [中关村在线](https://ai.zol.com.cn/1184/11843997.html)

---

### 1.6 Token Plan Subscription (May 22)

| Plan | Monthly | Credits | 
|------|---------|---------|
| Standard | ¥198/month | 25,000 Credits |
| Advanced | ¥698/month | 100,000 Credits (4x) |
| Premium | ¥1,398/month | 250,000 Credits (10x) |

**Features**: Team-shareable credits, dedicated API key (`sk-sp-`), built-in tools (search, code interpreter) no extra charge, multi-model support including Qwen3.7-Max, Qwen3.6 Plus, GLM-5.1.

Source: [阿里云开发者社区](https://developer.aliyun.com/article/1736226), [网经社](https://100ec.cn/detail--6659499.html)

---

### 1.7 Alibaba Cloud Bailian Platform Stats (May 20-22)

- **ARR ¥80亿** → expected **¥100亿 this quarter** → **¥300亿 year-end**
- Third-party models now on Bailian: GLM-5.1, MiniMax M2.7, Kimi K2.6
- Token Plan subscriptions launched

Source: [品玩](https://www.pingwest.com/a/313885)

---

## 2. What Needs Updating in the Wiki Page

The wiki page has already been updated to include all findings above. Specifically:

1. ✅ **Metadata**: `updated: 2026-05-26`, added tags `qwen3.7`, `agent-era`; added aliases `Qwen3.7-Max`, `Qwen3.7-Plus`, `千问云`, `Qianwen Cloud`
2. ✅ **Qwen Code v0.16.0/v0.16.1**: Added full section with 17 major features and hotfix details
3. ✅ **Qwen3.7-Max API**: Added pricing table, Anthropic protocol support, platform distribution
4. ✅ **Qwen3.7-Max Qwen Chat**: Added AA Index 56.6 ranking, app integration details
5. ✅ **Detailed benchmarks**: Added 9-benchmark breakdown table, 35-hour autonomous run analysis
6. ✅ **千问云 (Qianwen Cloud)**: Added full section with architecture details, Skills/CLI descriptions
7. ✅ **Token Plan**: Added ¥198/698/1,398 tiered pricing table
8. ✅ **External sources**: Added 10 new T1/T2 references

---

## 3. New search_hints to Add

```
- Qwen3.7 API Anthropic Messages protocol Claude Code
- 千问云 qianwenai.com Skills CLI open source agent platform
- Qwen3.7-Max AA Intelligence Index 56.6 global rank 5 Chinese rank 1
- Qwen Code v0.16.0 worktree isolation auto approval LLM classifier
- Qwen Code v0.16.1 Windows Git Bash MinTTY OSC 8 fix
- Qwen3.7-Max Token Plan ¥198 698 1398 subscription
- 百炼 Bailian ARR ¥100亿 Q2 2026 third-party model hosting
- Qwen3.7-Max 35 hour autonomous kernel optimization 10x Zhenwu M890
- Qwen3.7-Max OpenRouter $2.50 $7.50 pricing comparison
- Firethering Qwen3.7-Max GLM Kimi DeepSeek kernel benchmark comparison
```

---

## 4. Key Findings in Japanese (日本語サマリー)

### 5月21日〜26日 主要動向

**1. Qwen3.7-Max API正式公開（5/21〜23）**
- Alibaba Cloud Model Studio: ¥12/百万トークン（入力）、¥36/百万トークン（出力）
- OpenRouter: $2.50/$7.50（入力/出力）
- Anthropic Messages Protocolネイティブ対応 — Claude CodeがANTHROPIC_BASE_URL変更のみで利用可能
- 1Mコンテキスト、65,536最大出力トークン
- OpenAI互換とAnthropic互換の両APIを同一モデルで提供

**2. Qwen3.7-Max Qwen Chat統合（5/22）**
- 千問App v6.9.7+、PC、Web版に正式統合。全ユーザー無料
- AA Intelligence Index 56.6点（全球5位、国産1位）
- GPQA Diamond・HMMT 2026 Feb・IMOAnswerBenchでClaude Opus 4.6超越
- IFBench 79.1点（指令遵循で新記録）

**3. Qwen Code v0.16.0/v0.16.1（5/21, 5/23）**
- 80以上のPRを含む大規模アップデート。25K GitHub Stars
- Worktree隔離、Auto承認（LLM分類器）、qwen serveデーモン、/goal、/diff、/stuck診断
- v0.16.1: Windows Git Bashのレンダリング不具合修正、tool_result不変条件修正

**4. 千問云（Qianwen Cloud）正式ローンチ（5/20、5/21〜22に詳細判明）**
- 阿里云17年目で初の独立AI製品サイト「www.qianwenai.com」
- ホームページに製品リストではなく**一行のAgent命令**を表示
- 150モデルシリーズ・480モデルをSkills/CLI/MCPとしてAgent向けに再設計
- OpenClaw、Hermes Agent、Claude Code、Qoderが初日対応
- SkillsとCLIはGitHubでオープンソース公開

**5. Token Planサブスクリプション（5/22）**
- 月額¥198/¥698/¥1,398の3段階
- チーム共有クレジット制、専用API Key（sk-sp-）
- Qwen3.7-Max、Qwen3.6 Plus、GLM-5.1等マルチモデル対応

**6. 35時間自律実行の詳細分析（5/25 Firethering）**
- GLM 5.1（7.3倍）、Kimi K2.6（5倍）、DeepSeek V4 Pro（3.3倍）に対し
- Qwen3.7-Maxは10倍（幾何平均高速化）で競合を大幅にリード
