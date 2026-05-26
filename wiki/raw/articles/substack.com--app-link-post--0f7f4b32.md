---
title: "Zhihu Frontier Weekly｜OpenAI, DeepSeek, Anthropic & Google: AI Reasoning, Agents, and the New Infrastructure Race"
url: "https://substack.com/app-link/post?publication_id=6222474&post_id=199193430&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTkxOTM0MzAsImlhdCI6MTc3OTcxOTc3NiwiZXhwIjoxNzgyMzExNzc2LCJpc3MiOiJwdWItNjIyMjQ3NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.Hc_94Dizk08idM1k-12n9NTQ3Vfhv3x5z6Yz2E3znsM&r=2flx6&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email"
fetched_at: 2026-05-26T04:00:43.748013+00:00
source_date: 2026-05-25
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Zhihu Frontier Weekly｜OpenAI, DeepSeek, Anthropic & Google: AI Reasoning, Agents, and the New Infrastructure Race

Source: https://substack.com/app-link/post?publication_id=6222474&post_id=199193430&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoxOTkxOTM0MzAsImlhdCI6MTc3OTcxOTc3NiwiZXhwIjoxNzgyMzExNzc2LCJpc3MiOiJwdWItNjIyMjQ3NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.Hc_94Dizk08idM1k-12n9NTQ3Vfhv3x5z6Yz2E3znsM&r=2flx6&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email

Welcome to
Zhihu Frontier
,
your window into the hottest AI convos from China’s knowledge platform.
Over the past week, some of the most interesting conversations in AI weren’t just about benchmark scores or new releases.
OpenAI’s reasoning model
reportedly cracked a long-standing geometry conjecture, reigniting debates around AI-assisted scientific discovery.
DeepSeek’s new Harness team
hinted at a future where models and engineering systems become tightly integrated. Meanwhile, researchers behind diffusion language models are beginning to question one of the field’s deepest assumptions:
does language intelligence even need discrete tokens?
At the same time, the industry’s competitive dynamics are evolving rapidly. Karpathy’s return to pretraining at Anthropic challenges the idea that scaling laws are “over,” while GPT-5.5 pricing and DeepSeek price cuts show how different model ecosystems are diverging economically.
Here are the biggest discussions from Zhihu this week👇
The result sparked widespread discussion across both mathematics and AI communities. Beyond the proof itself, researchers are debating what this means for the future role of mathematicians in the age of AI-assisted discovery.
🔗 Discussion:
https://www.zhihu.com/question/2040738759281473391
Zhihu contributor @Fyx1123581347:
OpenAI’s original release included three files:
unit-distance-proof.pdf
— the AI-generated proof and a faithful human-readable explanation.
unit-distance-remarks.pdf
— commentary and improvements from human mathematicians.
unit-distance-cot.pdf
— the model’s chain-of-thought.
One important detail: aside from Will Sawin’s section, most of the mathematicians’ commentary is non-technical. Even readers without a math background can understand how experts are evaluating this event.
The AI solution fixed lattice lengths while varying the number field to construct the required point set. The influence of Erdős’ original proof is visible, but as Will Sawin noted, moving from “changing lengths” to “changing number fields” is far from an obvious step.
Interestingly, Jacob Tsimerman said he had explored similar ideas before, but abandoned them because increasing field degree indefinitely didn’t seem reliable. Humans often stop when intuition becomes uncertain. AI doesn’t.
Daniel Litt described the problem as a “low-hanging fruit” — not dismissively, but because it was solved through a concise and elegant construction rather than a massive new theoretical framework.
Many researchers now believe the bigger disruption is not the proof, but the coming transition from “proof scarcity” to “proof abundance.”
🔗 Discussion:
https://www.zhihu.com/question/2040751125725278389
Zhihu contributor @Yves S:
We are entering an era where proofs may become abundant — even overloaded.
Human mathematicians won’t disappear, but their role will fundamentally change. Traditionally, mathematical training emphasized derivation ability. In the future, machines may handle most derivation work.
Human researchers will increasingly
focus on asking meaningful questions and understanding AI-generated results.
Formal verification systems like Lean already exist. What’s missing is a bridge that reliably converts LLM-generated proofs into machine-verifiable steps.
That bridge is likely inevitable. AI could eventually generate Lean-native proofs directly, enabling end-to-end automated proof verification.
If that happens, not only mathematics itself, but journals, peer review, and academic evaluation systems may all need to adapt.
The bigger story may not be another coding assistant, but the rise of “Harness Engineering” as a new AI infrastructure layer.
🔗 Discussion:
https://www.zhihu.com/question/2040450519303288568
Zhihu contributor @刘杨:
Many people think this is simply another Claude Code competitor. But DeepSeek’s ambition is much deeper.
The key word is
Harness
.
In engineering, a harness is fundamentally a control system. The foundation model handles open-ended generation, while the harness layer constrains, validates, corrects, and converges outputs.
These two layers need to be developed together.
Third-party wrappers struggle because the model and engineering environment are disconnected. When an IDE throws a compile error, the model often lacks runtime context and can only guess.
DeepSeek’s approach is to close that loop themselves. Compiler logs, lint feedback, test results, and runtime signals all feed directly back into model optimization.
That’s the real meaning behind:
Model + Harness = Agent
New projects like ELF and Cola DLM are exploring whether language intelligence must rely on discrete tokens at all.
🔗 Discussion:
https://www.zhihu.com/question/2038213982293579409/answer/2039012493549426216
Zhihu contributor & Cola DLM writer @huMAnG0d:
The deeper question is not whether “language models can use diffusion.”
The real question is:
Must textual intelligence be tied to discrete tokens?
If not, what kind of continuous representation would better serve as a semantic carrier?
That’s the core motivation behind Cola DLM. Diffusion itself is not the goal —
it’s simply a solver for modeling continuous latent priors.
The important question is whether language has a more stable, abstract, and compressible semantic state space beyond tokens.
While most of the industry focuses on agents and post-training, Karpathy’s move suggests pretraining may still have untapped potential.
🔗 Discussion:
https://www.zhihu.com/question/2040212835037401530
Zhihu contributor @知乎用户tly:
Everyone focused on which company Karpathy joined. Almost nobody paid attention to which division he chose: pretraining.
The dominant narrative today is that scaling laws are slowing down, and future breakthroughs will come from post-training and agents.
Then Karpathy — arguably one of the industry’s best “direction pickers” —
goes back to pretraining.
His recent “auto research” work already hinted at this. The bottleneck wasn’t orchestration. It was the base model’s shallow scientific understanding.
Agents can coordinate tools and workflows, but if the underlying model lacks deep domain understanding, they can only stitch together superficial knowledge.
The answer may simply be that the two models are competing in entirely different markets.
🔗 Discussion:
https://www.zhihu.com/question/2037925163765691524
Zhihu contributor chenqin:
GPT-5.5 and DeepSeek are
not in the same competitive category at all.
GPT-5.5’s price increase reflects the fact that its capability is significantly ahead of Claude Opus 4.6 and 4.7. Users will still pay for it.
DeepSeek’s price reduction is a tactical move within its own tier,
competing more directly against models like Doubao.
For users spending tens of thousands of dollars monthly on APIs, subtle capability differences matter a lot — and they switch models quickly when incentives shift.
Developers were particularly disappointed by the lack of updates around coding capabilities and token efficiency.
🔗 Discussion:
https://www.zhihu.com/question/2040145697911956151
Zhihu contributor @drixs2050:
From an LLM perspective, the event felt underwhelming.
Gemini 3.5 Flash is now priced surprisingly close to 3.1 Pro, while often consuming more tokens per task in practice.
More importantly, Google barely discussed coding capabilities — currently one of the most important LLM battlegrounds.
Aside from vague mentions of speed improvements, there was little technical detail, which likely means coding performance still isn’t competitive.
📬
That’s all for this week’s AI round-up from Zhihu Frontier.
👉 Subscribe to never miss an update:
zhihufrontier.substack.com
