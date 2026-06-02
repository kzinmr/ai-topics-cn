---
title: "ChinAI #361: What can CANN do for China's independent compute capacity?"
url: "https://substack.com/app-link/post?publication_id=2660&post_id=199909074&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTk5MDkwNzQsImlhdCI6MTc4MDMxMzE0NCwiZXhwIjoxNzgyOTA1MTQ0LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.-ddi2vHPiElysvnhojQWZGDhN5t34GbwsOMCXGlP7s8"
fetched_at: 2026-06-02T04:00:18.956314+00:00
source_date: 2026-06-01
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# ChinAI #361: What can CANN do for China's independent compute capacity?

Source: https://substack.com/app-link/post?publication_id=2660&post_id=199909074&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTk5MDkwNzQsImlhdCI6MTc4MDMxMzE0NCwiZXhwIjoxNzgyOTA1MTQ0LCJpc3MiOiJwdWItMjY2MCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.-ddi2vHPiElysvnhojQWZGDhN5t34GbwsOMCXGlP7s8

Greetings from a world where…
welcome new readers: most issues are note-taking exercises on Chinese-language articles that interest me (not lengthy missives)
…As always, the searchable archive of all past issues is
here
. Please please
subscribe here
to support ChinAI under a
Guardian
/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).
Context:
DeepSeek’s V4 made waves for something beyond pure capabilities: the validation of “chip-model synergy” between V4 and Huawei’s Ascend chips on a large scale. Previously, this was something that could only be achieved with Nvidia chips, in part because of the CUDA moat. As Lily Ottinger and Mary Clare McMahon described in a
ChinaTalk article
:
Nvidia’s position rests on what Doug O’Laughlin has called a “three-headed hydra” of leading hardware, networking capabilities, and, most importantly for this piece, a deeply entrenched software ecosystem. At the center of that ecosystem is
CUDA, a proprietary programming framework
that allows developers to efficiently map computations onto Nvidia’s GPUs. CUDA’s value lies not only in its performance but in its reach: an expansive set of libraries, optimized workflows, and tight integration with widely-used machine learning frameworks make it the industry standard. And, crucially, CUDA can only be used with Nvidia GPUs. That makes CUDA a core component of Nvidia’s competitive advantage, otherwise known as Nvidia’s moat.
In this week’s feature translation, QBitAI provides a readout (link to
original Chinese
) on Huawei’s alternative to CUDA, the Compute Architecture for Neural Networks (CANN), based on panels at the Kunpeng Ascend Developer Conference.
Photo of Kunpeng Ascend Developer Conference 2026. Source: KADC and QBitAI.
Key Takeaways: CANN has transitioned from its “infancy” into a “youth” phase, according to Qiuwu Chen, founder of Shanghai-based AI coding start-up AIGCode.
From the article: “
This ‘youth phase’ does not imply that the ecosystem has reached full maturity; rather, it signifies that developers are beginning to move beyond ‘vendor-provided babysitting support.’ Developers are now capable of independently resolving issues, contributing code, and driving the ecosystem's iterative progress
.
Chen recounted his company’s experience with Ascend over the past year or so. They used Ascend out of necessity, due to severe GPU shortages at the beginning of 2024. In early days, when they ran into issues when pre-training of a 7B-scale Mixture-of-Experts model on Ascend chips, they had to submit a support ticket to Huawei, which resulted in a four month wait. The entire ecosystem was “essentially a section of desert,” Chen recalls.
The three dimensions that dictate whether Huawei chips can overcome the Nvidia CUDA moat: adaptation efficiency, performance ceilings, and production-grade reliability.
Regarding adaptation efficiency, as the previously cited Ottinger and McMahon article emphasizes, “
adopting models to run on Huawei’s platform is also onerous
.” If you have to depend on Huawei engineering support to fix issues, then it will take a long time (as the early experience of Chen’s AIGCode reveals). At the developer conference, a University of Science and Technology of China team claimed that it took less than a week for them to migrate a high-performance computing solver to Huawei’s Kunpeng CPU chips.
On performance ceilings, one key indicator is Model Flops Utilization (MFU), or compute utilization rate. How much compute can you squeeze out of the same chip? The article reports, “
On the Ascend accelerator, AIGCode achieved a Model Flops Utilization of 65% during the pre-training of its MoE model. This figure is nearly double the industry average
.” This dimension will also be shaped by the efficiency of scheduling and coordination in massive clusters (for example, a supernode of 384 Ascend chips and 192 Kunpeng chips).
Lastly, the example of production-grade trust comes from a leading joint-stock commercial bank (think: an institution like China Construction Bank). At the developer event, this bank stated that they had directly integrated AI into its core risk management processes. The article implies (though it is not explicitly stated) that the open-sourcing of the CANN framework shaped this financial institution’s decision to entrust a core business operation to AI models that run on Huawei chips.
Could an open-source developer ecosystem drive CANN’s development going forward? This is one of the most interesting questions.
Huawei open-sourced the core code for CANN, including runtime environments and compilers, last December. The article lists a few indicators that may point to a sustainable ecosystem that drives flywheel growth: Over 70 major AI models are now supported immediately upon their release, the Kunpeng and Ascend developer communities both surpass 4 million members, and groups like AIGCode and the aforementioned leading bank are contributing features to various communities.
*Notably, the bank contributed 34 optimizations to vLLM-Ascend, a project to adapt one of the most popular inference engines for Ascend NPU chips.
Back in May 2025, Ottinger and McMahon found that “
Huawei’s Ascend developer portals — both in English and Chinese — exhibit low engagement, with sporadic posts and limited public debugging activity
.” To be honest, it was difficult for me to figure out whether this has meaningfully changed. On the surface level, the
Ascend forums
seem to have more activity. I guess I’m just used to an open-source framework being posted on a Github repository, and then most of the issues being sorted out there, instead of a separate community forum website. And on my quick scan, it seemed like CANN was posted on Gitee (China’s domestic alternative to GitHub) and then switched to Huawei’s own site.
In any case, the key trend to watch is whether CANN can actually benefit from an organic community of implementers and complementary innovators that contribute back into the framework.
FULL TRANSLATION:
Behind DeepSeek V4’s “Chip-Model Synergy”, the domestic computing ecosystem begins flywheel acceleration
Written for ChinaTalk in May 2025, Lily Ottinger and Mary Clare McMahon’s in-depth analysis of CUDA vs. CANN was essential background reading for this post. Definitely read it if you are interested in this topic.
In
NYT
, David Pierson and Berry Wang report on Beijing’s efforts to export its security model to the Solomon Islands, which signed a security pact with China in 2022. The pilot was suspended after local backlash. H/t to
Kirsty Needham
for sharing and who reported on this in a 2024 story.
Good discussion and back-and-forth on this thread about whether some AI-failure stories are overblown. The context behind this is a flurry of reporting about companies saying that they’ve spent too much on AI.
If you’re in the area, I’ll be joining the Wonky China team for a happy hour at Chang Chang on June 10th. Come for the hot takes, stay for the scallion bubble pancakes.
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
