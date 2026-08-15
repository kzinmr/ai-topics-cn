---
title: "ChinAI #369: My Boss Wants Me to Run Kimi K3, What Should I Do?"
url: "https://substack.com/app-link/post?publication_id=2660&post_id=209422404&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDk0MjI0MDQsImlhdCI6MTc4NTc1NzA2NCwiZXhwIjoxNzg4MzQ5MDY0LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.KK8E3SXxEtE2amr1SiHORPVWouw4IC67n6OROMxbX8w"
fetched_at: 2026-08-04T04:00:26.746698+00:00
source_date: 2026-08-03
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# ChinAI #369: My Boss Wants Me to Run Kimi K3, What Should I Do?

Source: https://substack.com/app-link/post?publication_id=2660&post_id=209422404&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDk0MjI0MDQsImlhdCI6MTc4NTc1NzA2NCwiZXhwIjoxNzg4MzQ5MDY0LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.KK8E3SXxEtE2amr1SiHORPVWouw4IC67n6OROMxbX8w

Greetings from a world where…
cicada killer wasps are back
…As always, the searchable archive of all past issues is
here
. Please please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).
Context:
Less dense than our usual fare, this article (link to
original Chinese
) is a nice explainer of why you can’t run Moonshot AI’s latest model K3 on your own device. A friend asked 快刀青衣 (co-founder of a popular Chinese knowledge-sharing app): “
I heard K3 is an open-source and free model, right? So, can I just download it, deploy it on my own computer, and never have to spend money on it again?
”
Key Takeaways: “Open-source” language models differ from open-source software in that the former only open-sources the weights, not the source code.
Based on hardware costs to just load K3, you need at least 16 H200 GPUs. This is different from Kimi K2, a compressed version of which enthusiasts managed to run on a Mac Studio. Now, however, K3 is a “species that can only run in data centers or within enterprise environments.”
The article explains:
“Let me use an analogy. Imagine a three-star Michelin restaurant releasing the full recipe for its signature dish for free: ingredient quantities, cooking times, and every step is clearly written out. Could you recreate it? It looks like you could.
That is, until you turn to the first page and see the kitchen requirements: you need 64 professional-grade stoves running simultaneously, a power supply capable of supporting a small factory, and an initial investment of 20 million (RMB) just to acquire the equipment. The recipe is truly free, but the kitchen is truly unaffordable.”
We haven’t even mentioned the electricity costs.
Moonshot AI’s official recommendation is to deploy K3 on a super-node of at least 64 accelerator cards (roughly 17 million RMB in total costs). But if you tried to run these cards at full load in your home, it would consume 45 kilowatts, which would far exceed an ordinary household’s electrical meter and wiring.
Some observers have noted that K3 is “
hungry for tokens
.” The article points out, “
The economics of traditional software are such that development is expensive, while replication and operation are virtually free. In contrast, the economics of large models involve extremely high development costs; while replication is free, every single operation burns through real money in the form of electricity and GPU usage
.”
FULL TRANSLATION:
My Boss Asked Me to Deploy the Free K3 Model: I first calculated the “unaffordable” server costs
Here are some notes on things that stood out to me from K3’s technical report:
K3 trails the two strongest proprietary systems (Claude Fable 5 and GPT-5.6 Sol) but sits at the cost-efficiency frontier.
For the post-training and evaluation phase, Moonshot AI used a new sandbox infrastructure called
AgentENV
, which itself is an open-source platform.
This speaks to the close collaboration between the Kimi team and Tsinghua University’s MADSys Lab (machine learning, AI, big data systems group). This lab also developed the Mooncake architecture that helped K3 achieve higher cache hit rates. When I looked at the AgentEnv contributors list, a Tsinghua PhD student ranks as top in commits.
K3’s cybersecurity capabilities were surprisingly weak. It does identify previously unknown vulnerabilities but it was not very strong at converting vulnerabilities into working exploits. Also from the report:
The K3 report disclosed that K3 underwent an independent joint assessment by the UK AI Security Institute and NIST’s Center fro AI Standards and Innovation. From the
assessment
: “
Kimi K3 performs significantly below the most recent frontier cyber-capable models on preliminary cyber evaluations
run by UK AISI / CAISI. Specifically: When tasked to develop exploits, Kimi K3 performs significantly below the most recent frontier cyber-capable models.”
By Lavender Au, for
The Dial
, this longform article explores China’s short dramas (which run just a few minutes per episode). In just the first quarter of this year, 122,000 AI-generated short dramas went online. Au writes:
On any given day in China, roughly 215 million people spend over an hour watching short dramas. These dramas have multiplied on China’s internet, with 33,000 released in 2025. It’s a more than 100-billion-yuan ($13.8 billion) market domestically, double what it was in 2024.
Zvi Mowshowitz rounded up a great array of judgements on K3’s capabilities across many public and private benchmarks. The discussion about whether Moonshot intentionally “nerfed” K3’s cyber capabilities was especially interesting.
This new Department of Homeland Security rule will make it even harder for international students to study in the states. From NAFSA: Association of International Educators CEO Fanta Aw: “
Despite more than 20,000 public comments—including NAFSA’s—that raised serious concerns, DHS has chosen to move forward with a rule that will create more barriers for global talent without making our nation safer or stronger
.”
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
