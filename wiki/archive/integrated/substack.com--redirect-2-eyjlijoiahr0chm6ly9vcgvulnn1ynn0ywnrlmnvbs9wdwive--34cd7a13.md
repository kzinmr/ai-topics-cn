---
title: "Zhihu Frontier Weekly｜From DeepSeek V4 to Kimi K2.6 - model race, infra evolution, and the shifting AI stack"
url: "https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvemhpaHVmcm9udGllci9wL3poaWh1LWZyb250aWVyLXdlZWtseWZyb20tZGVlcHNlZWs_dXRtX3NvdXJjZT1zdWJzdGFjayZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1yZXN0YWNrLWNvbW1lbnQmYWN0aW9uPXJlc3RhY2stY29tbWVudCZyPTJmbHg2JnRva2VuPWV5SjFjMlZ5WDJsa0lqbzBNRGczTkRneUxDSndiM04wWDJsa0lqb3hPVFUyTWpVd05UTXNJbWxoZENJNk1UYzNOekk1TnprNU15d2laWGh3SWpveE56YzVPRGc1T1RrekxDSnBjM01pT2lKd2RXSXROakl5TWpRM05DSXNJbk4xWWlJNkluQnZjM1F0Y21WaFkzUnBiMjRpZlEuQjZBbE9VVjF0VW1kMnItanRJUFVobnkwbEZqWGQzdFB5aHdlMzZaNnJVVSIsInAiOjE5NTYyNTA1MywicyI6NjIyMjQ3NCwiZiI6dHJ1ZSwidSI6NDA4NzQ4MiwiaWF0IjoxNzc3Mjk3OTkzLCJleHAiOjIwOTI4NzM5OTMsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.EGGgBuHTTOpdZWb538QvBy90FsOxGpqBQH0GA6lRiec?&utm_source=substack&utm_medium=email"
fetched_at: 2026-04-28T04:00:38.570778+00:00
source_date: 2026-04-27
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Zhihu Frontier Weekly｜From DeepSeek V4 to Kimi K2.6 - model race, infra evolution, and the shifting AI stack

Source: https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvemhpaHVmcm9udGllci9wL3poaWh1LWZyb250aWVyLXdlZWtseWZyb20tZGVlcHNlZWs_dXRtX3NvdXJjZT1zdWJzdGFjayZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1yZXN0YWNrLWNvbW1lbnQmYWN0aW9uPXJlc3RhY2stY29tbWVudCZyPTJmbHg2JnRva2VuPWV5SjFjMlZ5WDJsa0lqbzBNRGczTkRneUxDSndiM04wWDJsa0lqb3hPVFUyTWpVd05UTXNJbWxoZENJNk1UYzNOekk1TnprNU15d2laWGh3SWpveE56YzVPRGc1T1RrekxDSnBjM01pT2lKd2RXSXROakl5TWpRM05DSXNJbk4xWWlJNkluQnZjM1F0Y21WaFkzUnBiMjRpZlEuQjZBbE9VVjF0VW1kMnItanRJUFVobnkwbEZqWGQzdFB5aHdlMzZaNnJVVSIsInAiOjE5NTYyNTA1MywicyI6NjIyMjQ3NCwiZiI6dHJ1ZSwidSI6NDA4NzQ4MiwiaWF0IjoxNzc3Mjk3OTkzLCJleHAiOjIwOTI4NzM5OTMsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.EGGgBuHTTOpdZWb538QvBy90FsOxGpqBQH0GA6lRiec?&utm_source=substack&utm_medium=email

Welcome to
Zhihu Frontier
,
your window into the hottest AI convos from China’s knowledge platform.
This week marks a
dense release cycle across China’s AI ecosystem
, spanning foundation models, agent infrastructure, chips, and multimodal systems.
From DeepSeek V4’s long-awaited debut, to Kimi and Qwen pushing reasoning and tool-use boundaries, and even hardware-level discussions around CUDA replacement — the AI stack is being rebuilt simultaneously at
model, infra, and systems levels
.
Below is a curated breakdown of the most discussed developments on Zhihu.
📎
Full technical breakdown:
https://www.zhihu.com/question/2030963929510310856/answer/2030968025906680230
Zhihu contributor @toyama nao：
Short conclusion: a long-awaited release that delivers outsized value.
The new V4 introduces two model families:
Flash and Pro,
supporting multiple inference tiers. Flash is comparable in size to mainstream small-to-mid models, optimized for speed and low cost, while Pro scales to trillion-level parameters and targets upper-bound intelligence.
V4 Pro effectively reclaims the domestic coding benchmark crown. In coding engineering tests, the max tier consistently outperforms the previous leader GLM-5.1, significantly narrowing the gap with Claude Opus. The high tier can complete four full engineering tasks reliably.
In
coding behavior,
V4 Pro shows several distinctive traits: broad programming knowledge coverage, strong long-context robustness with reduced hallucination, occasional attention drift, and relatively unstructured architecture/UI preferences.
Overall, both max and high tiers
are highly usable.
The model follows a strict execution loop in development tasks: deep reasoning first, single-pass code generation, then self-testing. It avoids iterative mid-writing redesigns, which significantly reduces low-level errors.
The max tier does not significantly increase average token output compared to high, but increases tool-call frequency and file-reading depth by up to ~60%, meaning higher time cost but manageable economic overhead.
Flash performs similarly to high tier on low-to-medium difficulty one-shot tasks, but shows higher variance: performance can range from unusable to perfect depending on prompts. Token consumption is higher than expected, but cost-performance remains strong overall.
📎
Industry transition analysis:
https://www.zhihu.com/question/2028817450829976782/answer/2029662178047731205
Zhihu contributor @尙禾：
NVIDIA’s real advantage lies in long-term compounding effects that are hard to quantify.
“Decoupling from CUDA” should not be interpreted as an immediate break from NVIDIA’s ecosystem.
DeepSeek V4 has been delayed for months without official confirmation, suggesting
this transition is still in early stages.
Reports indicate that training on domestic chips (e.g., Huawei hardware) has encountered stability issues, reinforcing that the transition away from CUDA is still at
an early experimental phase.
Beyond DeepSeek, companies like Alibaba, ByteDance, and Tencent are increasingly adopting domestic chips—not as full decoupling, but as diversification against reliance on NVIDIA.
📎
Performance analysis:
https://www.zhihu.com/question/2029714522651272097/answer/2030049575298389432
Zhihu contributor @toyama nao：
K2.6 behaves more like a human-like agent in
long-context and real-world task scenarios.
Its
reasoning capability
has improved significantly, regaining the top domestic position previously held by Seed models. This also gives Moonshot a modest pricing increase, with per-unit cost rising from 21 to 27.
However, the overall
chain-of-thought
structure remains relatively stable, keeping total cost manageable.
The non-reasoning mode shows more “adaptive but budget-constrained” behavior: simple tasks are solved within a few thousand tokens, while complex tasks can expand to 20K–30K tokens. Given the 15K limit in non-reasoning mode, many outputs exceed constraints and are not fully evaluated.
The reasoning mode is also affected by excessively long reasoning chains, with some outputs exceeding 80K token limits, leading to incomplete evaluation under benchmark rules, which partially explains lower median scores.
📎
Local deployment report & benchmarking thread:
https://www.zhihu.com/question/2028243224301454445
Zhihu contributor @Jon.Xiao：
Successfully deployed on 16GB RAM + 8GB VRAM (RTX 4060).
Performance is particularly
impressive in long-context usage:
with ~23K tokens of context and multiple conversation rounds, the model maintains usable speed (~16 tokens/sec), slightly slower than cloud-based GLM-5.
Overall,
a 3B activated parameter model can match the performance of much larger dense models (~27B scale)
, demonstrating strong efficiency gains.
Zhihu contributor @Lynn：
On a 4090 (48GB), Qwen3.6-35B-A3B-FP8 achieves 69/72 (96%) accuracy in tool-calling benchmarks with ~1024ms latency.
In
structured tool-use evaluation
, it outperforms five major Chinese commercial APIs including GLM, Kimi, DeepSeek, StepStar, and MiniMax.
📎
Pricing model update & ecosystem discussion:
https://www.zhihu.com/question/2030441793607746308/answer/2030449297569870738
Zhihu contributor @从不毒舌可达鸭：
Agent-based workloads consume significantly more tokens than chatbot interactions, making fixed quota systems less efficient under compute constraints.
Xiaomi restructured its Token Plan: early users effectively receive ~50% cost reduction, and pricing is no longer differentiated by context window size. Subscription and annual plans also include meaningful discounts.
Combined with improvements in model efficiency and token utilization, the overall cost-performance ratio has significantly improved.
In general, most vendors eventually return to economic rationality under sustained compute pressure, except a few players with strong ecosystem subsidies.
📎
Ecosystem convergence analysis thread:
https://www.zhihu.com/question/2030703202702549014/answer/2030743512271017421
Zhihu contributor @dreaaim：
Foundation model technology is no longer protected by strong moats. Even Tencent has caught up quickly, raising questions about why some players lag behind.
After DeepSeek’s methodological contributions in early 2025, the ecosystem entered a phase of rapid convergence:
Qwen initially dominated
GLM, MiniMax, and others re-entered competition
ByteDance Seed joined aggressively
Tencent Hunyuan has now caught up
The result is intensified competition, which short-term benefits users through faster iteration and lower prices.
📎
Product capability overview:
https://www.zhihu.com/question/2030082882098680763
Zhihu contributor @云天明的童话：
The model is no longer just text-to-image generation—it behaves like a full-stack creative assistant handling research, layout, and design tasks.
Zhihu contributor @rwfs：
The system demonstrates strong improvements in content richness, error reduction, layout quality, and visual consistency. With prompt robustness improvements, it approaches an ideal generative design workflow tool.
📬
That’s all for this week’s AI round-up from Zhihu Frontier.
👉 Subscribe to never miss an update:
zhihufrontier.substack.com
