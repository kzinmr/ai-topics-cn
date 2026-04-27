# Claude Code 换成了Kimi K2.5后，再也回不去了

**Source:** 掘金 (宅小年)
**Date:** 2026-04-23
**URL:** https://juejin.cn/post/7611432757572141096
**Categories:** [Claude Code, Kimi K2.5, GLM-4.7, 国内模型, API聚合]

## Summary
Developer guide for switching Claude Code from official Claude models to domestic Chinese models (Kimi K2.5 and GLM-4.7). Solves stability issues (account bans, timeouts) for Chinese developers while maintaining comparable performance. Kimi K2.5 ranks #1 on OpenRouter and OpenClaw leaderboards.

## Configuration
**GLM-4.7:**
```
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
ANTHROPIC_MODEL=GLM-4.7
```

**Kimi K2.5:**
```
ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
ANTHROPIC_MODEL=kimi-k2.5
```

**Router tool:** `claude-code-router` (ccr use kimi / ccr use glm / ccr use claude)

## Key Commands
- `/clear`: Resets conversation, keeps code changes
- `/compact`: Compresses history into summary
- `/init`: Generates CLAUDE.md for project instructions
- Plan Mode: `Shift+Tab` twice — read-only analysis before execution

## Analysis
This reflects the broader trend of Chinese developers diversifying away from single US model dependency. The ability to use Claude Code's UI with domestic model backends creates a hybrid workflow that balances capability with stability.
