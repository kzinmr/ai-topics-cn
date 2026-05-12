---
title: "China's AI Stack Blueprint vs Nvidia's CUDA Moat"
url: "https://substack.com/redirect/a528fadc-71da-45e6-98dc-86da893d4bf0?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-05-05T04:01:26.244630+00:00
source_date: 2026-05-04
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# China's AI Stack Blueprint vs Nvidia's CUDA Moat

Source: https://substack.com/redirect/a528fadc-71da-45e6-98dc-86da893d4bf0?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Editor’s note:
This is
Flashpoint,
Hello China Tech’s premium quick-strike column. In under 600 words, we cut through the noise to unpack one market-moving China tech event and why it matters. Flashpoint drops whenever the story demands it–weekdays or weekends.
Today’s column decodes DeepSeek’s latest move: a 50 per cent price cut that hides the real story in a technical footnote. The launch of TileLang, a Python-like programming language, marks phase two of building a China-controlled AI stack. Same-day support from Huawei, Cambricon, and Hygon signals coordinated standard-setting across hardware and software. But coordination isn’t conquest–Nvidia’s CUDA moat remains deep. For the Flashpoint overview, see our
introduction here
.
A 50 per cent price cut from a top Chinese artificial intelligence lab is enough to command attention. But when DeepSeek
announced
its new, more efficient language model, the real story for investors lay not in the lower API fees,
but in a technical footnote
: the use of a new programming language called TileLang. The coordinated, same-day support from domestic chipmakers confirms this is more than a technical choice. It is the second phase of a deliberate campaign to build a self-sufficient AI stack, free from Nvidia’s influence.
In the process of researching the new model, many new GPU operators need to be designed and implemented. We use the high-level language TileLang for rapid prototyping to support deeper exploration. In the final stage, with TileLang as the accuracy baseline, we gradually implement more efficient versions using low-level languages. Therefore, the main operators released in this open source project include both TileLang and CUDA versions. We recommend that the community use the TileLang-based version for research experiments to facilitate debugging and rapid iteration.
This is not the first time DeepSeek has played this role. Just months ago, its quiet adoption of the
UE8M0 FP8
data format sent shares of local hardware makers soaring. By signalling a preferred standard for data processing, DeepSeek gave a fragmented industry a common target for hardware optimisation. Now, with
TileLang
, it is addressing the other side of the equation: the software that runs on that hardware.
