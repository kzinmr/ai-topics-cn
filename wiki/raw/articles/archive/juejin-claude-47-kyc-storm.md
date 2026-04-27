# Claude 4.7与KYC风暴 — 中国AI从业者何去何从

**Source:** 掘金
**Date:** 2026-04-23
**URL:** https://juejin.cn/post/7630724767642533922
**Categories:** [Claude Opus 4.7, KYC, 中国AI从业者, 身份验证]

## Summary
Dual analysis: Claude Opus 4.7's performance breakthroughs AND Anthropic's KYC identity verification that effectively blocks Chinese users. Released April 16, 2026 — Opus 4.7 achieves SWE-bench Pro 64.3% and CursorBench 70%, but context memory collapsed from 78.3% to 32.2%. KYC via Persona Identities does not accept Chinese passports; China is "unsupported region."

## Opus 4.7 Performance
- SWE-bench Pro: 64.3% (vs GPT-5.4's 57.7%)
- CursorBench: 70%
- Vision Accuracy: 98.5% (from 54.5%)
- Image resolution: 3.75M pixels (from 1.15M)
- Hidden ~35% price increase via new tokenizer
- Context memory collapse: 78.3% → 32.2%

## KYC Impact
- Requires real-time photo of government ID (no scans)
- Chinese passports NOT accepted
- 18+ only (vs OpenAI/Gemini 13+)
- Persona Identities: 269 checks including watchlists and "negative media"
- Privacy concerns: ID photos used for AI training

## Survival Strategies for Chinese Developers
1. API aggregators (bypass direct KYC)
2. Domestic model combos (Zhipu GLM + Qwen + Kimi + MiniMax)
3. Local open-source deployment

> "You are chasing the world's frontier, but the world keeps closing its doors on you."
