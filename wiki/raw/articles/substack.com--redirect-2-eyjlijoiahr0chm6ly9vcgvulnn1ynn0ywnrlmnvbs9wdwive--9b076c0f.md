---
title: "Zhihu Frontier Weekly｜Huawei’s τ Law, DeepSeek Price Wars, MiMo Discounts, and Microsoft’s AI Cost Reality"
url: "https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvemhpaHVmcm9udGllci9wL3poaWh1LWZyb250aWVyLXdlZWtseWh1YXdlaXMtbGF3P3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0yZmx4NiZ0b2tlbj1leUoxYzJWeVgybGtJam8wTURnM05EZ3lMQ0p3YjNOMFgybGtJam95TURBeU5qWTBNRGNzSW1saGRDSTZNVGM0TURNNU1UQTRNeXdpWlhod0lqb3hOemd5T1Rnek1EZ3pMQ0pwYzNNaU9pSndkV0l0TmpJeU1qUTNOQ0lzSW5OMVlpSTZJbkJ2YzNRdGNtVmhZM1JwYjI0aWZRLi1QalR2SU1yeE1fTVkyS2NrRUMzN3QwZTV0MndDZ0xoOXlIUXktZlVmR1kiLCJwIjoyMDAyNjY0MDcsInMiOjYyMjI0NzQsImYiOnRydWUsInUiOjQwODc0ODIsImlhdCI6MTc4MDM5MTA4MywiZXhwIjoyMDk1OTY3MDgzLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.4FUzwzi_kMFNhVrqGntDgyOr3T_-d199QOMUoDBIG_U?&utm_source=substack&utm_medium=email"
fetched_at: 2026-06-03T04:00:14.827306+00:00
source_date: 2026-06-02
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Zhihu Frontier Weekly｜Huawei’s τ Law, DeepSeek Price Wars, MiMo Discounts, and Microsoft’s AI Cost Reality

Source: https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvemhpaHVmcm9udGllci9wL3poaWh1LWZyb250aWVyLXdlZWtseWh1YXdlaXMtbGF3P3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj0yZmx4NiZ0b2tlbj1leUoxYzJWeVgybGtJam8wTURnM05EZ3lMQ0p3YjNOMFgybGtJam95TURBeU5qWTBNRGNzSW1saGRDSTZNVGM0TURNNU1UQTRNeXdpWlhod0lqb3hOemd5T1Rnek1EZ3pMQ0pwYzNNaU9pSndkV0l0TmpJeU1qUTNOQ0lzSW5OMVlpSTZJbkJ2YzNRdGNtVmhZM1JwYjI0aWZRLi1QalR2SU1yeE1fTVkyS2NrRUMzN3QwZTV0MndDZ0xoOXlIUXktZlVmR1kiLCJwIjoyMDAyNjY0MDcsInMiOjYyMjI0NzQsImYiOnRydWUsInUiOjQwODc0ODIsImlhdCI6MTc4MDM5MTA4MywiZXhwIjoyMDk1OTY3MDgzLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.4FUzwzi_kMFNhVrqGntDgyOr3T_-d199QOMUoDBIG_U?&utm_source=substack&utm_medium=email

Welcome to
Zhihu Frontier
,
your window into the hottest AI convos from China’s knowledge platform.
The past week highlighted a growing shift from
model capability races to infrastructure and economics.
Huawei introduced
τ Law
, proposing a new framework for chip design beyond traditional transistor scaling. Meanwhile,
DeepSeek
continued reshaping the market with another dramatic price cut for V4 Pro and reports of a massive new funding round.
Xiaomi
followed with steep MiMo pricing reductions, while discussions around SSD-based KV cache architectures gained renewed attention. At the same time, reports that Microsoft may reduce its reliance on Claude sparked a broader conversation: as AI workflows become increasingly agentic, model costs—not model quality—may become the industry’s next bottleneck.
Here are the biggest discussions from Zhihu this week👇
Rather than introducing a new manufacturing process, Huawei’s newly proposed
τ (tau) Law
offers a new design philosophy for improving chip performance by reducing propagation delay through parasitic RC optimization.
🔗 Read more:
https://www.zhihu.com/question/2042176040638707165
Zhihu contributor @NavisLee:
The overall logic is sound.
τ = RC
is a fundamental circuit equation: reducing parasitic resistance and capacitance shortens propagation delay, which directly improves performance. The physical mechanism is internally consistent.
The most important part of Huawei’s proposal is
Circuit Folding.
Through its SkyBridge architecture, data routing is transformed from a traditional planar layout into a hybrid horizontal-and-vertical interconnect structure. High-speed signals are moved onto upper metal layers, reducing package area by more than 60%, while relay buffers placed at vertical interconnect points help shorten critical signal paths.
Another key component is
SkyClock.
Instead of distributing clocks from the bottom up, clock signals are delivered from the top down. More importantly, clock skew can potentially be adjusted even after tape-out, providing additional tuning flexibility. Huawei claims this can improve performance by over 5% while increasing tolerance to manufacturing variations and improving yield.
What’s particularly interesting is how SkyBridge differs from approaches pursued by TSMC and Intel. Similar concepts exist in advanced packaging, where vertical integration is used to connect multiple dies. SkyBridge, however, operates within the BEOL routing layers of a single die. It fundamentally reassigns how metal layers are used, leveraging the low-resistance characteristics of upper metal layers for high-speed signal transmission.
A useful analogy is redesigning the hallways inside a building rather than constructing new bridges between buildings. The engineering scale is nearly an order of magnitude different, requiring entirely new EDA workflows and design methodologies.
Zhihu contributor @且听沧海:
τ Law is not a breakthrough technology in itself, but a new design philosophy.
For decades, semiconductor progress has been guided by transistor scaling. Smaller transistors allow more devices to fit on a wafer, improving performance while reducing power consumption. Process nodes such as 14nm, 7nm, equivalent 5nm, as well as technologies like FinFET and GAA, all emerged under this paradigm.
τ Law proposes shifting attention from transistor dimensions to delay optimization across the entire system. In that sense, it may represent a new way of thinking about future semiconductor progress rather than a direct replacement for Moore’s Law.
DeepSeek has permanently reduced V4 Pro pricing once again—reportedly to roughly one-quarter of its previous level—raising new questions about how far model economics can be pushed.
🔗 Discussion:
https://www.zhihu.com/question/2041262830561875450
Zhihu contributor @李明殊:
The reason many users started calling Liang Wenfeng “Saint Liang” wasn’t the initial discount itself. It was what people discovered after using the model: cache hit rates were approaching 99%, effectively making many workloads feel almost free.
A major reason DeepSeek can afford such aggressive pricing is its architecture. The company reportedly
stores KV cache data on SSDs
and reloads it when needed, freeing expensive HBM resources while maintaining high throughput. The technical details have already appeared in published papers.
At its core, this is a trade-off of
storage for computation
. Retrieving data can be far cheaper than recomputing it, creating substantial efficiency gains for long-context workloads.
Reports suggest DeepSeek is pursuing a funding round worth approximately RMB 70 billion, while founder Liang Wenfeng continues emphasizing the company’s commitment to open-source development.
🔗 More details:
https://www.zhihu.com/question/2041154123677126717
Zhihu contributor @AI解码师:
The most unusual detail is that Liang Wenfeng himself is reportedly contributing around RMB 20 billion, nearly 29% of the entire round.
In most startup financings, founders are diluted while outside investors provide capital. Here, the founder appears to be the largest single participant.
Combined with a recent corporate restructuring that significantly increased Liang’s ownership and voting control, the picture is clear: control is being locked in first, with external capital brought in afterward.
Xiaomi has dramatically reduced pricing for the MiMo V2.5 model family, with some cache-hit requests reportedly discounted by nearly two orders of magnitude.
🔗 Read the discussion:
https://www.zhihu.com/question/2042778573321266131
Zhihu contributor @pansz:
The scale of this price reduction is astonishing. Bringing cache-hit pricing down to roughly 1% of standard rates may become one of the most significant discounts in AI API history.
One possible explanation is that Xiaomi has adopted techniques similar to those described in DeepSeek’s public technical papers, particularly
the use of SSDs
as an extension of memory for KV cache storage.
Interestingly, API response speeds appear to have slowed noticeably and now resemble DeepSeek’s latency profile. That trade-off—lower cost at the expense of response speed—could be another signal that similar caching architectures are being used.
Reports suggest Microsoft may be reducing its reliance on Claude, with rising operational costs becoming a key factor in strategic decision-making.
🔗 Read more:
https://www.zhihu.com/question/2042293920017691036
Zhihu contributor @酱紫君:
Microsoft’s leadership may have underestimated both the intensity of the AI boom and the strength of Claude’s moat.
Today, the bills are becoming difficult to ignore. Once skills, sub-agents, and harness-style architectures are layered together, usage can grow exponentially.
And Microsoft is hardly alone. Any company that aggressively adopted AI workflows is now facing the same reality: traditional SaaS assumptions about declining marginal costs no longer hold when every workflow is powered by large-scale inference.
📬
That’s all for this week’s AI round-up from Zhihu Frontier.
👉 Subscribe to never miss an update:
zhihufrontier.substack.com
