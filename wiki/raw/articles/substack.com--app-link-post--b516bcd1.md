---
title: "ChinAI #356: DeepSeek as Road Builder [修路人]"
url: "https://substack.com/app-link/post?publication_id=2660&post_id=195527792&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTU1Mjc3OTIsImlhdCI6MTc3NzI5MDg0NSwiZXhwIjoxNzc5ODgyODQ1LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.IubNjfEk45WoRCaX7sB9JYVYLach48inabXvgdsNWHg"
fetched_at: 2026-04-28T04:00:15.415733+00:00
source_date: 2026-04-27
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# ChinAI #356: DeepSeek as Road Builder [修路人]

Source: https://substack.com/app-link/post?publication_id=2660&post_id=195527792&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTU1Mjc3OTIsImlhdCI6MTc3NzI5MDg0NSwiZXhwIjoxNzc5ODgyODQ1LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.IubNjfEk45WoRCaX7sB9JYVYLach48inabXvgdsNWHg

Greetings from a world where…
Jeopardy is still appointment viewing during this streak
…As always, the searchable archive of all past issues is
here
. Please please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).
Context:
On April 24, DeepSeek released its long-awaited V4  model (including a 1.6 trillion-parameter Pro version). Let’s break down this release’s technical intricacies plus the broader implications for China’s AI ecosystem, with the help of two Huxiu translations.
Key Takeaways: DeepSeek’s V4 demonstrates near-frontier capabilities, but the main breakthroughs are in compute efficiency.
Based on the
technical report
, DeepSeek V4-Pro “
requires only 27% of single-token inference FLOPs and 10% of KV cache compared with DeepSeek-V3.2
.” In her “DeepSeek Overly Understated” piece
, Sihang Song deems DeepSeek a road builder [修路人].
The top models can support 1 million token context windows, which means they can process more information at once, akin to
50,000 lines of code
. The V4 supports this long context window at a fraction of the computational costs. Interestingly, Song notes that DeepSeek surpasses other highly capable, cost-effective Chinese models on this metric: Compared to DeepSeek, “
when confronted with the same complex task, (Moonshot AI’s) Kimi will typically consume a higher volume of tokens
.”
From Song’s article: “
It remains a company focused on building models centered around the core principle of ‘efficiency.’ Features such as its hybrid attention architecture, KV Cache compression, reduced inference costs for million-token context windows, expert parallelism optimizations, and cross-platform kernel designs may not be particularly ‘sexy,’ but they are undeniably critical
.”
What separates DeepSeek from other Chinese AI models?
In terms of technical roadmap (see image below), Huxiu regards Moonshot AI as the company most similar to DeepSeek.
Table of companies, model release dates, and innovations related to “attention mechanisms” (how to make compute and memory usage more efficient as context windows increase)
In part because it is not a traditional startup (given its backing by a quantitative hedge fund), it can undertake long time-horizon investments. By comparison, Moonshot AI operates more like a quintessential AI startup, facing the pragmatic demands of commercialization and fundraising.
It should be emphasized that compute efficiency is not the only thing that matters. Kimi, for instance, is optimized to be a productivity tool. I thought this point from Song’s article was helpful: “
If a model consumes a few extra tokens but saves a user three hours of work time, that trade-off may very well be a worthwhile one
.”
What does DeepSeek V4 mean for Chinese chips? In contrast to some
hasty analysis
, it is very likely that DeepSeek is still dependent on Nvidia chips for
training;
however, some of V4’s toolchain advances suggest gradual progress toward domestic substitution, especially on the inference side.
DeepSeek does not make any claims about using Huawei Ascend chips for training V4. Instead, it is very likely that the V4 was trained on Nvidia chips. As industry insiders told Song: “
If they had truly and completely switched to domestic chips, the V4 model likely wouldn't have arrived this quickly.
”
One fascinating tidbit from DeepSeek’s technical report is their use of the TileLang domain-specific language, which is less tied to the Nvidia ecosystem and can be adapted across many different chip platforms.
Another Huxiu piece, by Bizheng Dong, delves into DeepSeek V4’s implications for inference. DeepSeek has been experimenting with a unique “Engram” architecture, designed to address memory capacity constraints. Memory capacity is one reason why Nvidia is so strong for both training and inference: its latest Rubin GPU has 288GB in total memory capacity (the Ascend 910B, by comparison, has a memory capacity of 64B). DeepSeek is trying to do more with less memory capacity. From the article: “
a long-context inference task that typically requires 80GB of VRAM (video random access memory) to execute might, under the Engram architecture, require only 8GB
.”
Dong shares another detail about adapting DeepSeek-V4 with Chinese chips: “
Breaking with industry convention, the developers did not give Nvidia early testing access; instead, they reserved all opportunities for early adaptation exclusively for Huawei and Cambricon. The explicit objective is to execute a comprehensive migration from the CUDA ecosystem to Huawei’s CANN framework.
”
Dong’s piece contains some more stats and industry reports that hype up what DeepSeek means for China’s domestic chip ambitions. I’m a bit more skeptical (at least in the near-term), but the things that stand out to me about V4 are the Engram architecture and TileLang improvements, which seem like they will have staying power.
FULL TRANSLATIONS: 1)
DeepSeek Overly Understated
; 2)
Don’t Overestimate Nvidia; Don’t Underestimate DeepSeek
*We’ll catch up on reading recommendations next week!
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
