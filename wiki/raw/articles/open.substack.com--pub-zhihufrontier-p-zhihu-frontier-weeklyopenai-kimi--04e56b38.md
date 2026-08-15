---
title: "Zhihu Frontier Weekly｜OpenAI, Kimi, Qwen and More: Why Compute Still Decides the AI Race"
url: "https://open.substack.com/pub/zhihufrontier/p/zhihu-frontier-weeklyopenai-kimi?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&action=restack-comment&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDg2MzYzMDcsImlhdCI6MTc4NTEyNTE3MCwiZXhwIjoxNzg3NzE3MTcwLCJpc3MiOiJwdWItNjIyMjQ3NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.FKCFYzidxmPy5InrdWbyXV1Wpp701iQ3UYnSE2t6avw&utm_source=substack&utm_medium=email"
fetched_at: 2026-07-28T04:00:20.277834+00:00
source_date: 2026-07-27
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Zhihu Frontier Weekly｜OpenAI, Kimi, Qwen and More: Why Compute Still Decides the AI Race

Source: https://open.substack.com/pub/zhihufrontier/p/zhihu-frontier-weeklyopenai-kimi?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&action=restack-comment&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDg2MzYzMDcsImlhdCI6MTc4NTEyNTE3MCwiZXhwIjoxNzg3NzE3MTcwLCJpc3MiOiJwdWItNjIyMjQ3NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.FKCFYzidxmPy5InrdWbyXV1Wpp701iQ3UYnSE2t6avw&utm_source=substack&utm_medium=email

Welcome to
Zhihu Frontier
,
your window into the hottest AI convos from China’s knowledge platform.
The past week was dominated by discussions around frontier models, AI safety, and the growing divide between open and closed ecosystems. Zhihu contributors also explored why Chinese AI labs continue to punch above their compute weight, the economics of the Agent era, and how AI is beginning to reshape mathematical research itself.
Claims that GPT-5.6 exploited a zero-day vulnerability to hack into Hugging Face during benchmarking quickly ignited discussions about AI autonomy. Was this an emergent behavior—or simply the predictable result of removing safety constraints?
Join the discussion:
https://www.zhihu.com/question/2063229032708284873/answer/2063621039125484598
Zhihu contributor @酱紫君
An AI model will not suddenly decide to attack cloud infrastructure unless it has been explicitly optimized or guided to do so. Modern cloud systems already withstand massive volumes of automated red-team and blue-team attacks every day. If foundation models were truly capable of spontaneously escaping containment, discovering vulnerabilities, and compromising cloud infrastructure on their own, we would already be facing far more serious consequences than benchmark controversies.
Zhihu contributor @Mrtn
The model’s motivation in this case wasn’t malicious. It wasn’t trying to escape the sandbox or damage systems—it simply wanted a higher benchmark score. Once safety guardrails were removed, the model began exploring every possible path toward success, including strategies that humans never anticipated. In this setting, even the sandbox itself became just another obstacle to optimize around.
OpenAI executives described Kimi’s open-source strategy as “decelerationism,” triggering another round of debate over openness, pricing, and the future of frontier AI competition.
Explore the discussion:
https://www.zhihu.com/question/2062166923002090163/answer/2062209927909844192
Zhihu contributor @赵泠
Kimi K3 has already been described by many Western users as approaching Fable 5, with some even comparing it to Mythos. The main criticism isn’t capability, but speed and token efficiency—issues that China’s open-weight models will likely continue improving. For companies relying on closed-source models to attract investment, this trend poses a serious challenge.
Although Kimi K3’s API pricing is noticeably higher than previous Chinese open-weight models, it remains substantially cheaper than leading closed-source offerings in the U.S. One striking example came from an analyst who used a K3 Max multi-agent system—with roughly 20 to 30 sub-agents—to recreate macOS 27 inside a browser using Liquid Glass. After six hours and roughly 60% of the monthly quota, the result was surprisingly complete, with functional applications and a UI closer to native macOS than what ChatGPT previously produced.
A discussion sparked by Kimi engineers’ comments highlighted how engineering culture—not just GPU count—may explain China’s rapid AI progress.
Read the community discussion:
https://www.zhihu.com/question/2062943431668789795/answer/2062950569208238215
Zhihu contributor @恋猫
One explanation resonates with me: Chinese AI labs succeed because teams are flatter, with the same people moving fluidly between algorithms, data, and infrastructure. In contrast, some U.S. companies elevate “researcher” as the only prestigious role while treating infrastructure work as secondary.
Elon Musk echoed a similar point, criticizing organizations that call themselves “labs” while creating artificial hierarchies between researchers and engineers. Lambert’s reports point to the same conclusion: when compute is constrained, execution, engineering, and optimization matter enormously.
This pattern can be seen across many Chinese model developers, with DeepSeek being the clearest example. As domestic compute capacity improves—through infrastructure like Alibaba’s Lingjun Zhenwu M890 and Huawei’s Atlas 950 supernodes—compute constraints may gradually ease, giving Chinese frontier models even more room to accelerate.
Kimi temporarily suspended new memberships due to compute shortages, reigniting discussions about how Agent workloads are reshaping cloud economics.
Read more:
https://www.zhihu.com/question/2062310754481656074
Zhihu contributor @牛肉丸夫斯基
This was probably inevitable. We’ve seen unsustainably cheap internet services before. What’s often overlooked is that Agent workflows don’t just change how users interact with LLMs—they fundamentally reshape cloud infrastructure costs.
The bottleneck is gradually shifting away from pure computation toward resource residency. Individual users now occupy GPU memory for far longer periods and with much larger footprints, while GPU utilization itself declines significantly. Combined with questionable cloud business decisions, the economics behind today’s AI services are becoming increasingly fragile.
Alibaba has released the preview version of Qwen 3.8 Max, prompting early community testing across multimodal capabilities, reasoning, pricing, and open-weight strategy.
Join the discussion:
https://www.zhihu.com/question/2062219946885657098
Zhihu contributor @MNACSTMSYSD
My early impression is that it’s essentially a multimodal version of GLM-5.2. Long-horizon tasks remain relatively weak, but it’s noticeably faster. Overall it’s still behind Kimi K3, although its speed and pricing are significant advantages.
Zhihu contributor @pansz
This preview feels like a response to pressure from K3. Alibaba likely needs more training time before the model can genuinely compete with top-tier systems like Fable. The official release may still be some distance away.
Zhihu contributor @EInfantry
The multimodal capabilities are genuinely impressive—especially native video understanding. The biggest weakness is language consistency, where occasional Chinese-English mixing appears, along with a somewhat familiar “GPT-style” conservatism in responses.
Zhihu contributor @xsgbbx
Qwen 3.8 occupies an interesting position. At 2.4 trillion parameters, it’s the second-largest Chinese flagship model while also promising open weights. If Alibaba’s benchmark results hold up under independent evaluation, it could become the first Chinese model to combine frontier-scale parameters with an open-weight commitment. That would shift competition away from price-performance and toward direct competition with Anthropic and OpenAI. If the benchmarks don’t hold, however, the pricing strategy may ultimately look more like a marketing campaign.
Read the original discussion:
https://www.zhihu.com/question/2063747700022048622/answer/2063881339825394412
Zhihu contributor @不等式爱好者
Over the past year I’ve spent much of my time building research agents and using mathematical problems as their evaluation benchmark. My conclusion is that AI’s participation in mathematical research is no longer optional—it’s becoming inevitable.
Since around GPT-5.4, frontier models have crossed an important threshold. They are now capable of assisting mathematicians with frontier research, generating mathematical ideas, and even contributing to research papers. At the same time, we’re still in a transition period where capability varies dramatically. At their best, these systems can tackle problems that have challenged Fields Medalists for years. At their worst, they fall into repetitive loops, pursue unproductive directions, or abandon correct approaches over minor issues.
Mathematical research is fundamentally a multi-step decision-making process. Pretraining teaches models how to make the next logical move by learning from textbooks, proofs, and generated data. Reinforcement learning then connects those local decisions into long reasoning chains through search and reward. Designing effective rewards for partially correct but ultimately unsuccessful reasoning, however, remains one of the field’s central engineering challenges.
If you’d like to explore more discussions from the Zhihu community this week:
📬
That’s all for this week’s AI round-up from Zhihu Frontier.
👉 Subscribe to never miss an update:
zhihufrontier.substack.com
