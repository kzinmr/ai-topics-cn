# Crawl Pipeline Source Coverage by Topic Domain

Documenting which topic categories the auto-crawl pipeline (V2EX/Juejin/36kr/WeChat) covers well versus its blind spots. Use this when deciding whether local crawl data alone is sufficient, or if web search is essential.

## Well-Covered Topics (crawl data usually sufficient)

| Domain | Example Topics | Typical Volume per Cycle |
|--------|---------------|-------------------------|
| Model releases & pricing | deepseek, qwen, doubao, chatglm, kimi | High (multiple articles per day) |
| Agent frameworks & tools | china-ai-agent-ecosystem, openclaw, coze, dify | High (V2EX/Juejin discourse) |
| Coding tools & IDE plugins | china-ai-coding-assistants, china-coding-agents, coding-plan | Medium-High |
| API pricing & platform changes | Any pricing/Token Plan topic | High (36kr + V2EX) |
| Enterprise adoption cases | Dify at みずほ, Coze enterprise | Medium |
| GPU/local deployment | china-local-deployment, vram-optimization | Medium |
| Vibe Coding trends | vibe-coding-china | Medium (sporadic spikes) |
| MCP ecosystem | mcp-china, mcp-chinese-tools | High (ongoing coverage) |
| OpenClaw ecosystem | openclaw | Very High (weekly releases) |

## Poorly Covered Topics (web search essential)

| Domain | Example Topics | Why Crawl Misses |
|--------|---------------|------------------|
| **Government regulation** | china-ai-regulation, china-ai-model-filing | CAC/MIIT/NDRC announcements don't appear on tech media. 清朗行动 enforcement only surfaces when a company is punished. |
| **Legislation & policy** | AI立法, 伦理指引 | Official gazette publications not crawled. |
| **Academic open-source releases** | china-open-source-ai (new model releases) | 面壁/MiniCPM, LingBot, Ring releases may appear on ModelScope/HuggingFace but not in crawled media. |
| **Hardware/chip developments** | china-gpu-restrictions | Semiconductor supply chain news appears on specialized trade media not in the crawl pipeline. |
| **Financial results (non-listed)** | Private company fundraising | Only covered when 36kr/Jiemian writes a dedicated piece. |
| **Company personnel changes** | Exec departures, team restructuring | Only surface on 36kr/V2EX for notable cases. |

## Fallback Strategy When web_search Is Down

1. **Check crawl digests first**: `~/ai-topics-cn/inbox/daily_digests/daily-digest-YYYY-MM-DD.md` — grep by topic keywords
2. **Cross-source**: If a topic appears in 2+ sources (e.g., both 36kr and Juejin), confidence is higher
3. **Accept gaps for poorly-covered domains**: If the topic is in 'Poorly Covered' and web_search is down, document "新規情報なし" and move on. Do NOT fabricate findings.
4. **Newsletter coverage**: Newsletter digests (`inbox/newsletters/`) may catch topics from ChinAI, 知乎Frontier Weekly, or 机器之心 that the general crawl misses. Check these as a secondary source.
