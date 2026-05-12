---
title: "ChinAI #350: Around the Horn (24th episode)"
url: "https://substack.com/redirect/10a15a5c-009f-423b-a4bd-e1defd3c94b1?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-05-12T04:01:11.217040+00:00
source_date: 2026-05-11
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# ChinAI #350: Around the Horn (24th episode)

Source: https://substack.com/redirect/10a15a5c-009f-423b-a4bd-e1defd3c94b1?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Greetings from a world where…
over 30,000 of y’all now subscribe to this little rag
…As always, the searchable archive of all past issues is
here
. Please please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).
That weekday 4PM central time slot beckons: let’s go back Around the Horn!
Welcome to episode 24. For new readers, here’s how it works (see
ChinAI #342
for the previous edition):
I give short previews of ten articles that caught my eye during a scan through my usual sources (all published within the past week or so). The title for each preview links to the original article in Chinese.
Readers vote on next week’s feature translation by replying to the email and/or commenting on the post with the number of your preferred article.
*As a show of appreciation to readers who support ChinAI through a paid subscription, I’ll give some added weight to those votes.
The main idea is that any of these 10 links would have made for a great feature translation this week — like season 4 of Industry, there are no skips!
Summary:
Last week, I noted how OpenClaw enthusiasts factor into MiniMax’s popularity on OpenRouter. This article reports on OpenClaw’s China community, including Tencent and other big cloud providers setting up offline “booths” to help people deploy open-source agents.
Source: All Weather TMT [全天候科技]
- article recommended by Huxiu platform
Summary:
By March 3rd, MiniMax ranked as the fifth largest technology stock on Hong Kong’s stock exchange, nearing Baidu and JD.com’s value. Is this real? What do the R&D efficiency numbers show? How will geopolitics and international regulations affect its rise?
Source: 虎嗅 (
Huxiu) — well-known platform that shares user-generated content but also publishes their own pieces on China’s science and technology ecosystem.
Summary:
Only .5% of Chinese college graduates will land a position at a top tech firm. What’s the waiting game like for those who hope to convert summer internships into full-time offers? One aspect: knowing how to properly light a superior’s cigarette.
Source: 极昼工作室 (
Perpetual Light Studio
)
, a reporting unit under Sohu that does longform human-interest stories.
Summary:
We really need more sober takes on China’s robotics industry. Please send recommendations my way if you have them (bonus points if they are at least the level of detail as pg. 193 of my book). This piece points out many Chinese humanoid robots use pre-programmed movements.
Source: 快刀财经
via
IT桔子 (IT Juzi) —
good source on financing and venture capital in technology fields.
Summary:
In this northern
small town
of just under 500,000 people, AI signboards litter the storefronts: “AI Deep Skin Analyais”; AI Smart Study Room, etc.” This reporter scrutinizes the actual AI content in these small-town stores.
Source: 脑极体
(Naojiti
)
, a tech media platform based in Tianjin. Previous issues have translated their analysis of liquid cooling in data centers.
Summary:
As the technical lead of Alibaba’s Tongyi Qianwen LLM series since 2022, Lin had fostered a successful ecosystem. He had also risen the ranks very quickly. Before all the speculation about why he left, this piece provides a good profile of his background.
Source: 机器之心 (
jiqizhixin) — media portal similar to Leiphone in coverage.
Summary:
This is one of the Chinese AI safety benchmarks that I’ve been following over the past year or so. This announcement describes the types of evaluations that CAICT will conduct when it comes to AI safety and security.
Source: CAICT AI Safety/Security Governance”[CAICT AI安全治理]
- AI governance portal of gov-affiliated think tank under China’s Ministry of Industry and Information Technology.
Summary:
I’ve been keeping up with this SuperCLUE benchmark since March 2023. Now, their 2025 annual report is out, with three U.S. models at the top. See our coverage of their 2025 mid-year report in a previous issue (
ChinAI #324
).
Source: CLUE中文语言理解测评基准
(SuperCLUE) — organization that tests the capabilities of large language models from Chinese and international labs.
Summary:
AI was a hot topic at the beginning of China’s Two Sessions (annual legislative sessions). This post discusses the Zhihu founder’s proposal to enhance copyright protections in response to a flurry of AI-generated comics.
Source: Zhihu
discussion: a Quora-like Q&A forum
Summary:
Last week, three Chinese chip companies released their earnings reports on the same day. What can we learn from their reported indicators? How are they seeking to differentiate themselves?
Source: 雷峰网 (
Leiphone) — media portal that covers China’s science and tech landscape, with a focus on AI-related happenings.
Yorwba added an important content on last week’s
ChinAI
, questioning the article’s depiction of the geographical pathway for American developers integrating Chinese open-source models like MiniMax M2.5.
Last week’s TechFlow article claimed:
An American developer in San Francisco sends an API request. Data travels from California, via an undersea fiber optic cable in the Pacific, to a data center somewhere in China. The GPU cluster starts working, electricity flows from China’s power grid to the chips, inference is completed, and the results are sent back. The entire process may only take a second or two.
But Yorwba’s comment pointed out that, when you look at the OpenRouter profiles for MiniMax 2.5 or Zhipu’s GLM 5 or DeepSeek V3.2, the most popular providers are U.S.-based inference providers such as DeepInfra or Atlas Cloud. One exception might be Siliconflow, which is a Chinese inference engine company, but it lists its headquarters as Singapore on OpenRouter (which means, possibly, its data centers are based in Singapore, not China). Put simply, Yorwba is right to correct me: “
Most of the tokens OpenRouter attributes to Chinese models likely never pass through a data center in China at all
.”
This means this passage from last week’s issue should also be scratched:
U.S. companies will likely be hesitant to use platforms like OpenRouter to leverage Chinese models: “
An API request from an American developer is processed through a Chinese data center, physically passing through China. This isn’t a problem for individual developers and small applications, but it’s a fatal flaw in scenarios involving sensitive corporate data, financial information, and government compliance. This is why the Chinese model has the highest penetration rate in development tools and personal applications, but almost no presence in core enterprise systems.
”
Yorwba’s comment led me to a fascinating
Substack post
titled “Flooding the AI Frontier”, by Ben Turtel, a former Google software engineer. On the process by which developers adopt Chinese open-weight models, he points out:
Top open-weight models are hosted by a multitude of
US-based
providers (like
DeepInfra
and
Cerebras
) who process queries in
US-based
data centers. Chinese companies have no visibility into, and generate no revenue from, this usage of their models.
Why would Chinese companies do this? Ben goes on to parse through the point made in last week’s issue: the notion that usage of Chinese open-source models will enable them to become a the sticky, default infrastructure option for global developers. Ben disputes this:
One prominent hypothesis is that if global developers adopt Chinese AI models, China could set standards that steer AI development worldwide. I’m skeptical. In the past, choosing open alternatives like Android over iOS or Linux over Windows meant rewriting nearly everything from scratch. But LLMs are different: they process and generate natural language, making them perhaps the most natively interoperable technology ever invented. With tools like
OpenRouter
, swapping models is often as simple as changing a single parameter in your code. The same prompt can be processed by different LLMs. Lock-in doesn’t exist here.
The
whole post
is worth reading, as he goes on to ponder whether the rise of Chinese open-weight models “makes it harder for US companies developing
foundational AI
, just like cheap subsidized manufacturing undercut US
factories
.”
*
These are Jeff Ding’s (sometimes) weekly translations of Chinese-language musings on AI and related topics. Jeff is an Assistant Professor of Political Science at George Washington University.
Check out the archive of all past issues
here
& please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay for a subscription will support access for all).
Also! Listen to narrations of the ChinAI Newsletter in podcast format
here
.
Any suggestions or feedback? Let me know at chinainewsletter@gmail.com or on Twitter at
@jjding99
