---
title: "ChinAI #368: The Affordable Luxury of Kimi K3"
url: "https://substack.com/app-link/post?publication_id=2660&post_id=208550714&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDg1NTA3MTQsImlhdCI6MTc4NTE1MDg1NSwiZXhwIjoxNzg3NzQyODU1LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.ijYXplexexsQd1_QEruDjumYNUMpf_nvSAmHF3iwxAk"
fetched_at: 2026-07-28T04:00:29.237517+00:00
source_date: 2026-07-27
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# ChinAI #368: The Affordable Luxury of Kimi K3

Source: https://substack.com/app-link/post?publication_id=2660&post_id=208550714&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDg1NTA3MTQsImlhdCI6MTc4NTE1MDg1NSwiZXhwIjoxNzg3NzQyODU1LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.ijYXplexexsQd1_QEruDjumYNUMpf_nvSAmHF3iwxAk

Greetings from a world where…
I feel vindicated for liking Interstellar when it came out
…As always, the searchable archive of all past issues is
here
. Please please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).
Context:
Last week, Moonshot AI’s release of Kimi K3 rattled Silicon Valley, Wall Street, and the White House. With 2.8 trillion parameters, K3 marked a big jump in open frontier model size (see image below).
Notably, it ranked third on the Artificial Analysis Intelligence Index, behind only Anthropic’s Claude Fable 5 and OpenAI’s GPT-5.6 Sol. Apart from performance, K3’s price was also shocking: by some metrics, it is 13 times more expensive than DeepSeek’s V4. Based on this week’s feature translation (link to
original
diyi xinsheng
article
), let’s dig into Kimi K3’s pricing strategy.
Key Takeaways:
By now, the U.S. reaction to each new Chinese frontier model release is almost rehearsed — “let’s just ban it”, “this is only because they distilled American models” — but this week’s feature translation referenced
some interesting trends in Chinese reactions to Kimi K3.
Of course, some hailed it as an “honor for Chinese technology.” An intriguing twist: when previous open-source models made waves, Chinese critics would simply attribute it to stealing technology via distillation. Yet, this time, in Chinese public discourse, skepticism about distillation vanished. From the article: “
This time, however, K3’s self-developed architecture—boasting 2.8 trillion parameters—and its top ranking in Code Arena rendered that catch-all explanation completely invalid
.”
Some Chinese social media posts did gasp at the high prices, which rival some of the closed-source models. And, of course, this article cites the one-word “Impressive” comment from Elon Musk, who is consistently referenced in Chinese tech media.
Let’s examine Kimi K3’s pricing structure more closely, to understand the “affordable luxury” tag.
Compare K3’s API pricing to its Chinese competitors. Using the blended rate (essentially, a typical usage scenario),
K3 costs $2.30 per million tokens. By comparison: Alibaba’s Qwen3.7 Max ($1.40), Zhipu’s GLM-5.2 ($0.90), MiniMax’s M3 ($0.22), and DeepSeek’s V4 Pro ($0.18). Compared to its predecessor (Moonshot AI’s K2.6), K3’s output price increased by over 3.5 times.
The blended rate represents average usage scenarios, which may include a significant portion of requests that are “cache misses”: when Moonshot’s system has to process your full prompt request rather than routing it to a server that recently processed the same request. According to the article, Moonshot has adopted techniques that increase the cache hit rate in programming scenarios, which reduces input costs. Concretely, a cache miss costs 20 RMB per million tokens; a cache hit costs 2 RMB per million tokens.
Here’s how the article summarizes K3’s pricing strategy: “
By matching the performance of flagship overseas models while anchoring prices to the ceiling for domestic models, [K3] drives China’s large models to move beyond ‘cutthroat price competition’ toward ‘value monetization
.’
”
Let’s not overreact to K3 either. Moonshot AI has to address a lot of challenges, including: 1) compute constraints, 2) technical limitations, and 3) price-market fit.
Two days after launch, Kimi attracted a surge of new users, but it also had to suspend subscriptions and implement usage limits due to a shortage of computing power.
The Kimi blog also notes some technical limitations, including sensitivity to thinking history and a tendency for
excessive proactivity
. The latter stood out as something to track closely, as it may have safety implications: “
K3's training places particular emphasis on long-horizon, challenging tasks. As a result, when it encounters minor issues or ambiguous user intent during task execution, it may make unexpected decisions on the user's behalf. If your application requires the agent to operate within well-defined boundaries and refrain from excessive improvisation, please impose more explicit behavioral constraints on K3 in the system prompt or in AGENTS.md
.”
Just as with fashion or cars, it may be difficult for affordable luxury to hit the sweet spot of price-to-performance. “
It remains to be seen whether the high price point will be accepted by ordinary consumers and whether enterprise clients are willing to pay for the long-term stability and security of an open-source model’
,” the article concludes.
FULL TRANSLATION:
100 RMB per Million Tokens: With Kimi Adopting “Affordable Luxury” Pricing, Will You Still Pay for K3
This is Concordia’s fourth annual report on AI safety in China. Their headline takeaway: China’s approach to AI safety and governance has evolved beyond content control. It’s packed with good details, including an in-depth analysis of Chinese technical standards. I also learned some updates on gaps in terms of industry commitments: 1) “
Although Z.AI prominently cites its signing of the Seoul Frontier AI Safety Commitments in its IPO documents, it has not followed through on the requirement to publish a frontier AI safety policy
;” 2) “
DeepSeek, MoonShot, and MiniMax have no safety papers in our dataset since January 2025 at all
.”
Benita Zhang (Zhang Xiaojun) is a Chinese business reporter who has worked for Caijing and Tencent News. She’s done these great in-depth interviews with Chinese frontier AI lab leaders:
Two interviews
with Moonshot AI’s Yang Zhilin
An interview
with Zhipu AI (Z.AI)’s CEO Zhang Peng
This exchange on open source vs. closed source, from her
second interview
with Yang Zhilin, was very revealing:
Zhang Xiaojun:
Last year you said that open source would lag behind closed source…You said at the time: “The leader won’t open-source; only the laggards will.”
But today, you open-sourced.
Yang Zhilin:
Because right now, globally, we’re not fully in the lead yet (laughs).
Some of those judgments still hold in their broad direction: when you release a model, the community can contribute certain things. For example, you can do a lot on the inference side; you can let more people use the model for free.
But when it comes to contributing to the model itself — making the model stronger — currently only the original developer can do that.
Of course, if you look at the base model, that’s indeed the case. But doing extensive post-training on top of an open-source model — especially agentic post-training — may give rise to new opportunities.
Suppose you really want to build a law-related agent, and you’re a startup. You can absolutely train a specialized agent on top of K2, with your own specific set of tools, and it can perform extremely well in the scenarios you care about. That kind of opportunity exists.
It’s more about empowering downstream applications than feeding back into the improvement of the base model. Of course, this question needs to be observed dynamically.
Zhang Xiaojun:
Will you choose open source for the long term?
Yang Zhilin:
That’s what we hope to do for the long term, but it doesn’t have to be open source only. We want to share technical know-how with the community — that’s an important way to accelerate technological progress…But not everything has to be open-sourced either. For example, in collaborations with certain companies, not everything will be opened up.
Zhang Xiaojun:
All in all, is open source a belief in a technical system, or a strategy of market maneuvering?
Yang Zhilin:
Objectively speaking, it’s both, and both bring benefits. But ultimately, we hope that through this, the technology becomes safer and reaches a better level faster.
Zhang Xiaojun:
How will the open- and closed-source ecosystems evolve? In your view, how many players will ultimately remain globally, open and closed combined?
Yang Zhilin:
Not many — but there will still be a few. If you look at the past two years, the trend is fairly clear: the market is gradually becoming more concentrated, more convergent, more focused. Maybe it started with several hundred players, then went to several dozen, then to a few.
A few — that’s probably the final stable number. As it looks now, that’s highly likely.
Zhang Xiaojun:
Which side do you belong to — open source or closed source?
Yang Zhilin:
That has to be observed dynamically. We hope to share more technology over the long term.
Zhang Xiaojun:
Why have most Chinese companies gone open source?
Yang Zhilin:
Objectively speaking, there’s an element of market maneuvering. But it’s a good thing for the community.
GovAI, my old home base, is hiring across multiple roles in DC. The Head of US Policy will direct GovAI’s federal policy research and drive its buildup in DC; the DC Chief of Staff will help shape and execute the buildout in Washington; and Research Fellows and Research Scholars will do research on their own topics of interest, including China. Check out the
GovAI Opportunities page
for more information and to learn how to apply.
These are Jeff Ding’s (sometimes) weekly translations of Chinese-language musings on AI and related topics. Jeff is an Assistant Professor of Political Science at George Washington University.
Check out the archive of all past issues
here
& please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay for a subscription will support access for all).
Any suggestions or feedback? Let me know at chinainewsletter@gmail.com or on Twitter at
@jjding99
