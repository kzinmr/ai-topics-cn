---
title: "Can Huawei Take On Nvidia's CUDA?"
url: "https://substack.com/redirect/4dfb83d4-71fe-41f5-a1e8-54c1d8de8071?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-06-02T04:00:23.606034+00:00
source_date: 2026-06-01
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Can Huawei Take On Nvidia's CUDA?

Source: https://substack.com/redirect/4dfb83d4-71fe-41f5-a1e8-54c1d8de8071?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Mary Clare McMahon
is an incoming Schwarzman Scholar (‘26) and former Winter Fellow at the Centre for the Governance of AI, where she researched compute governance and U.S.-China AI competition. Previously, she worked in the National Security and Cybercrime Section of the U.S. Attorney’s Office for the Eastern District of New York.
Last month,
reports
emerged that DeepSeek was running a distilled version of its R1 reasoning model on Huawei’s Ascend chips. While DeepSeek trained its model on Nvidia Hopper series chips, Huawei’s deployment of Deepseek R1 underscores a broader strategic question: to what extent can Huawei erode Nvidia’s dominance in the global AI chip market?
Nvidia’s position rests on what
Doug O'Laughlin
has
called
a “three-headed hydra” of
leading hardware
,
networking capabilities
, and, most importantly for this piece,
a deeply entrenched software ecosystem
. At the center of that ecosystem is CUDA, a proprietary programming framework that allows developers to efficiently map computations onto Nvidia’s GPUs. CUDA’s value lies not only in its performance but in its reach: an expansive set of libraries, optimized workflows, and tight integration with widely-used machine learning frameworks make it the industry standard. And, crucially, CUDA can only be used with Nvidia GPUs. That makes CUDA a core component of Nvidia’s competitive advantage, otherwise known as
Nvidia’s moat
.
This article explains Huawei’s attempt to replicate and bypass that moat. For now, Huawei appears to be advancing the following three-pronged strategy:
Building out its own software stack, including a proprietary parallel programming model and surrounding tools that developers rely on to write, optimize, and deploy code efficiently.
Deepening integration with PyTorch, the most widely adopted open-source machine learning framework for model training.
Investing engineering resources in developing the Open Neural Network Exchange (ONNX), an open standard for machine learning models that enables portability across hardware platforms, to support the deployment of non-Ascend-trained models on Ascend chips.
Huawei is not the only actor seeking to erode Nvidia’s software lock-in — AMD has made
similar efforts
with ROCm, and Google has a software stack fitted to run Google TPUs. However, Huawei remains the most significant challenger in the Chinese market.
The core question is not whether Nvidia’s dominance is being contested, but whether Huawei’s software strategy can mature enough for a full-stack transition away from U.S. hardware.
This article proceeds in two parts: part one provides background on Nvidia’s software moat and how it was constructed; part two analyzes Huawei’s evolving response.
The roots of Nvidia’s software moat can be traced back to the late 2000s, when CEO Jensen Huang made a long-term bet on CUDA, Nvidia’s proprietary parallel computing platform. In
2007
, Nvidia released CUDA as a programming model for scientific computing. At the time, the dominant paradigm for scientific research (and most other computing applications) was CPU-based computation; GPUs were considered niche accelerators, primarily designed for graphics rendering in video games. CUDA’s launch was an explicit attempt to invert that paradigm by positioning the GPU as a general-purpose compute platform.
CUDA allowed developers to write code in familiar C/C++ syntax that executed directly on Nvidia GPUs, thereby accessing the highly optimized functionality of these GPUs. But creating a new computing model meant overcoming a classic chicken-and-egg problem: developers needed hardware to test their software on, and customers needed software to run on their hardware — neither would commit without the other. Nvidia addressed this by seeding the market for CUDA with its consumer gaming cards, which already had a broad base of installation. It made CUDA freely available (without open sourcing the code), created a global developer conference, and worked directly with scientists and researchers to port algorithms to the GPU. As Huang later
recalled
in a speech at National Taiwan University, “We worked with each developer to write their algorithms and achieved incredible speedups.” This engagement strategy eventually paid off; in 2012,
AlexNet
was trained on CUDA and Nvidia GPUs.
As Nvidia’s software and hardware stacks became popular with deep learning researchers, Nvidia continued to invest in — and improve — CUDA.
Nvidia created an extensive suite of libraries, such as cuDNN for deep learning, which dramatically lowered the time and expertise required to deploy high-performance models. In short,
CUDA became more than just a programming model — it became the foundation of a full-stack software ecosystem.
For the next decade, CUDA continued to improve and attract more developers. And it is still improving to this day — though CUDA is closed source, Nvidia
welcomes
and often incorporates developers’ feedback. Nvidia also maintains
online forums
for developers to answer and ask questions about CUDA.
Thus, the CUDA ecosystem embeds substantial switching costs. Developers who migrate away from CUDA usually must rewrite large portions of code — by forgoing access to Nvidia’s finely tuned libraries, developers are forced to substitute with less mature equivalents, if any replacements exist at all. Further, developers also lose support from the large troubleshooting community that has grown up around CUDA.
Today, many machine learning developers do not code directly in CUDA. Instead, they write code in Python, a higher-level and more user-friendly language, using frameworks such as PyTorch and JAX. But even here,
CUDA remains central: it acts as the backend bridge between PyTorch and Nvidia’s GPU architecture
.
We will discuss PyTorch in greater detail in a later section. For now, it is enough to note that CUDA’s value lies not only in its impressive performance (which has improved continuously for nearly two decades), but also in the ecosystem that has formed around it. That is the essence of Nvidia’s moat — challengers with competitive hardware must also replicate an entire software environment if they want to compete.
Undermining Nvidia’s software moat requires more than performance parity with Nvidia GPUs — it demands a credible alternative to the tightly integrated CUDA ecosystem. Huawei appears to be pursuing such an alternative. Its strategy consists of three interrelated prongs, each aimed at reducing the friction of switching away from Nvidia.
First, it is expanding its native software stack alongside a growing suite of tools designed to mirror the utility of CUDA’s broader ecosystem. Second, Huawei is deepening integration with PyTorch, the most widely adopted machine learning framework and one that, by default, pairs seamlessly with CUDA. By building backend support through adapters like torch_npu, Huawei is attempting to position Ascend as a drop-in hardware alternative. Third, Huawei is investing in ONNX (Open Neural Network Exchange), an open standard for cross-platform model representation, to allow models trained on non-Huawei hardware to run inference efficiently on Huawei chips. Together, these efforts seek to replicate the full-stack developer experience that has made CUDA so difficult to displace.
Huawei’s Software Alternatives
Huawei’s most direct challenge to CUDA comes in the form of CANN (Compute Architecture for Neural Networks), its proprietary programming environment for Ascend NPUs. CANN sits at the same level of the software stack as CUDA, providing the tools needed to execute high-performance machine learning models on Huawei hardware. Paired with CANN is MindSpore, Huawei’s high-level deep learning framework, conceptually analogous to PyTorch. Together, these tools form Huawei’s native alternative to the Nvidia-centric PyTorch + CUDA stack.
​​CANN has been in development since
at least 2019
, the year Huawei was added to the US entity list. Huawei’s 2024
Annual Report
highlighted (on four occasions) the release of CANN 8.0 in
September of 2024
, promoting this development as a significant step in advancing AI computing capabilities.
However, developers cite serious usability issues with CANN.
According to the
Financial Times
, one Huawei researcher complained that CANN made the Ascend chips “difficult and unstable to use.” One developer described the process of using the Ascend 910B as “a road full of pitfalls” (踩坑之路), sharing the following
reflections
on Zhihu
, a Quora-like Chinese website for academic discussion, in February 2025:
“I have been interning in the company for the past six months. Due to the shortage of computing resources, interns can only use Ascend 910B for training and development… Looking back, every time I encountered various problems and bugs, it was difficult to find the corresponding solutions on the Internet. Some problems were finally solved with the help of Huawei's operation and maintenance engineers. Therefore, I hope that this article, in addition to summarizing my own staged engineering experience, can help more Ascend NPU developers and help the development and progress of the domestic computing ecosystem.”
426 other users upvoted the post. One commenter responded, “It seems that it will take until 2027 for CANN to be truly mature, stable, and easy to use.”
The absence of a robust developer community for CANN further increases the onboarding burden for new developers. Unlike Nvidia’s developer forums, which benefit from community-maintained documentation and rapid peer troubleshooting, Huawei’s Ascend developer portals — both in English and Chinese — exhibit low engagement, with sporadic posts and limited public debugging activity. According to another
Zhihu
article
posted in June of 2024, “When I first started exploring Ascend, I felt quite overwhelmed.
Although there is a lot of documentation available, it feels quite disorganized. When encountering problems, the limited user community means you probably won’t find a corresponding solution,
which leads to frequent frustration.”
While the Nvidia
CUDA Programming and Performance Developer page
had multiple live threads posted just days before the screen capture above, the most recent posts on the Huawei CANN developer pages were from January 2025.
Adapting models to run on Huawei’s platform is also onerous. According to that same Zhihu article from June 2024, “Any public model must undergo deep optimization by Huawei before it can run on Huawei's platform. This optimization process is heavily dependent on Huawei and progresses slowly.” By contrast, after testing the Nvidia H100 and H200 for model training applications, Semianalysis
reported
, “Nvidia’s Out of the Box Performance & Experience is amazing, and we did not run into any Nvidia specific bugs during our benchmarks.
Nvidia tasked a single engineer to us for technical support,
but we didn’t run into any Nvidia software bugs as such we didn’t need much support.”
To try to increase adoption, Huawei has adopted a strategy reminiscent of Nvidia’s own CUDA rollout in the 2000s: embedding engineers directly into customer sites to assist with code migration. According to reporting from the
Financial Times
, Huawei has deployed engineering teams to Baidu, iFlytek, and Tencent to help reimplement and optimize existing CUDA-based training code within the CANN environment​. This mirrors the anecdote recounted
above
, where Jensen Huang described how Nvidia “worked with each developer to write their algorithms and achieved incredible speedups” during CUDA’s early years. Huawei is now attempting to replicate that strategy, pairing onboarding with high-touch technical support in the hope of accelerating ecosystem uptake.
In parallel, Huawei is also trying to improve its native software stack. DeepSeek engineers have reportedly said that the Ascend 910C can achieve
up to 60% of the inference performance
of the H100, and potentially more with CANN optimizations. As
Kevin Xu
noted on a prior episode of
ChinaTalk
, DeepSeek engineers have proven adept at “work[ing] below CUDA to maximize their Nvidia GPU.” If similar techniques were applied within the Huawei ecosystem, they could help close the performance gap between Ascend and NVIDIA hardware.
One particularly intriguing way to close that gap involves using AI to accelerate software optimization. If AI systems themselves can be leveraged to improve kernel optimization, develop the CANN and MindSpore stack, and reduce performance inefficiencies, it could meaningfully shift the competitive landscape. Sakana AI has already demonstrated a version of this approach with its “
AI CUDA Engineer
,” an agentic framework that translates standard PyTorch code into highly optimized CUDA kernels. According to Sakana, the system achieves 10—100x speedups for AI model training. If comparable AI-driven optimization techniques could be adapted for Huawei software, it would represent a significant step toward enhancing performance within the CANN ecosystem. Developer loyalty might follow.
Despite its investment in a native software stack, though, Huawei appears to recognize that displacing CUDA with CANN is not feasible in the near term. As a result, it has shifted part of its strategy toward interoperability rather than replacement. Nowhere is this more evident than in Huawei’s growing involvement with the PyTorch ecosystem.
Huawei and PyTorch
As part of its strategy to reduce friction in migrating away from Nvidia, Huawei has prioritized compatibility with PyTorch, the dominant open-source machine learning framework used across academia and industry. Originally developed by Meta’s AI research lab in 2016, PyTorch was released publicly in 2017, then transitioned to being governed by a wider network of companies under the Linux Foundation in 2022. The resulting PyTorch Foundation is governed by a consortium of premier members, including Meta, Microsoft, Google, Amazon, AMD, Intel, Nvidia, and, as of October 2023, Huawei.
PyTorch enables developers to define, train, and deploy machine learning models using concise and intuitive Python code. The framework's popularity stems from its "eager execution" model, which allows each operation to run immediately, making it easier to debug, prototype, and iterate than other alternative frameworks (like Google’s TensorFlow).
From the outset, PyTorch was optimized for Nvidia GPUs. New operators and features are still tested and tuned against CUDA first, and performance benchmarks are routinely conducted on Nvidia’s hardware. Installing PyTorch via Python’s package manager automatically sets it up to run on Nvidia GPUs. This makes the framework effectively Nvidia-native, and any effort to use it on non-Nvidia hardware requires not just backend substitution, but complete ecosystem engineering.
Huawei’s primary technical achievement has been enabling the execution of PyTorch models on its Ascend NPUs through an adapter called torch_npu. Torch_npu bridges PyTorch with Huawei’s low-level NPU drivers and CANN backend. Huawei developers publicized this development at the
2024 PyTorch Shanghai Meetup
, pictured below.
Huawei’s torch_npu adapter allows Huawei's AI accelerators to interface with PyTorch, though it exists
separately
from
PyTorch’s main codebase
. (The torch_npu adapter uses PyTorch’s PrivateUse1 mechanism, an interface that lets hardware makers test new accelerators without immediately merging their code into PyTorch.) At the 2024 PyTorch meetup in Shanghai, a Huawei engineer
noted
that devices maintained outside PyTorch’s core, like Huawei’s, often face stability issues because changes in PyTorch's main code aren't automatically tested for compatibility. This challenge is widely recognized by the community.
For this reason,
Huawei’s forked version of PyTorch is still less effective than Nvidia’s CUDA-native implementation, and developer feedback points to persistent challenges in runtime reliability and documentation.
In a
Zhihu
thread with more than 700,000 views, senior software engineer “Mingfei” wrote that, “It’s worth emphasizing that plugins [referring to the forked version of PyTorch] are not native” and “several unavoidable issues arise,” including version compatibility; third-party extension support; and test coverage challenges. Another
Zhihu contributor
noted, “Ascend chips provide poor support for third-party frameworks like PyTorch and TensorFlow, making it extremely challenging to adapt to the latest large-scale models and use them effectively.” Note that the developer seems to be referring to the challenges of deploying models on Ascend chips, not training new models.
While Huawei’s patches have not yet been fully integrated upstream,
there are reasons to believe that Huawei might be able to garner political support within the PyTorch Foundation to formalize its contributions.
The PyTorch Foundation’s
official announcement
of Huawei’s status as a premier member noted that Huawei “provides easier access to the PyTorch ecosystem for more hardware vendors… [which] aligns with the PyTorch Foundation’s mission to develop AI as part of a sustainable open source ecosystem and produce inclusive technological feats.” This quote seems to suggest that PyTorch wants to support other hardware options besides Nvidia’s. Further, Huawei’s status as a premier member of the PyTorch Foundation grants it a seat on the Governing Board, as well as a formal role in setting foundation-wide policies and technical priorities. This membership was unanimously approved by existing premier members, signaling at least tacit acceptance of Huawei’s contributions by Meta, Nvidia, AMD, and Google. Finally, Huawei appears to be strongly committed to contributing to open source projects. The company’s
2024 Annual Report
highlighted that Huawei is “a firm supporter and major contributor to open source communities” and explicitly mentioned its membership in the PyTorch Foundation.
In sum, Huawei is executing a long-term strategy to allow developers to use PyTorch with its Ascend series of chips. Its success will depend on the company’s continued technical contributions, the size of its developer community, and whether the PyTorch Foundation will incorporate the torch_npu and other Huawei contributions into its main code base.
Huawei and OXXN
While Huawei’s PyTorch integration aims to reduce friction in model development, it does little to solve the harder problem of model portability — that is, how to take a model trained on Nvidia hardware and deploy it on Huawei’s Ascend chips. To address this, Huawei has turned to a complementary approach, optimizing the Open Neural Network Exchange (ONNX) format to serve as a bridge between software ecosystems.
ONNX (Open Neural Network Exchange) is an open-source format originally developed by Meta and Microsoft in 2017 to enable model interoperability across deep learning frameworks. It allows developers to export a model trained in one framework, such as PyTorch with CUDA, and run inference in another runtime environment — or on different hardware entirely. It also helps optimize models, allowing them to run
faster
than they would if they were directly deployed from PyTorch. ONNX operates under the umbrella of the
Linux Foundation AI & Data
, of which Huawei is a premier member.
Put simply, ONNX is like the PDF of AI models. Just as documents created in Microsoft Word or Google Docs to be exported into a portable, fixed-format PDF file that can be opened and viewed across operating systems, ONNX allows models trained in PyTorch or other machine learning libraries to be exported into a standardized format that can then be run on different hardware platforms.
Huawei has embraced ONNX Runtime, the engine that executes ONNX models. The company maintains a public Ascend ONNX Runtime, available on GitHub, which includes optimized kernels and execution instructions tailored to CANN and Ascend chips. According to the
ONNX Runtime documentation
, Huawei’s ONNX Runtime page is “community-maintained,” meaning that it is maintained by Huawei rather than by the core ONNX Runtime team, and that it is Huawei’s responsibility to ensure ongoing support for the library.
Huawei’s goal here is straightforward: to enable developers to train models on non-Huawei hardware, export the files to ONNX, and deploy the models on Ascend chips, all without rewriting core logic. This workflow has clear appeal in the Chinese market. Model developers could still train on Nvidia Hopper chips or train models through the cloud, then shift deployment or inference workloads to Huawei hardware.
It’s important to note that running a model on hardware, even if using an ONNX file, can introduce bugs or compatibility issues.
Some PyTorch operations don’t export cleanly to ONNX, while others need rewriting
. ONNX models may also need custom operations that the hardware backend has to support. That said, Huawei’s investment in ONNX offers a practical path to inference decoupling. In contrast to the CUDA-first development loop, which binds training and deployment to Nvidia hardware, ONNX gives Huawei a way to insert itself at the deployment stage, even if training remains CUDA-bound.
Nvidia’s enduring dominance in the AI chip market is not due to superior hardware or networking architecture alone — it’s also a function of Nvidia’s deeply integrated software ecosystem. This ecosystem — anchored by CUDA, high-performance libraries, and seamless compatibility with PyTorch — offers a robust developer experience and an active community that reinforce Nvidia’s lead. Huawei’s strategy is to build a competitive stack of its own.
Model deployment may be Huawei’s most immediate opening. Already, it has demonstrated that models trained on Nvidia hardware, like DeepSeek’s R1, can be run in distilled form on Ascend chips. If the US were to
ban the export of Nvidia H20s
to China, this workaround could become standard. In that scenario, indicators of improvement in the Huawei software stack would manifest not as headlines, but as reduced developer complaints, more seamless deployments, and fewer distinctions between fallback option and first choice.
Huawei isn’t there yet, though. As noted by the exasperated programmers quoted above, working with Ascend 910B chips still requires debugging without community support. But Zhihu threads where developers vent frustrations can eventually become a troubleshooting resource that contributes back to the Huawei ecosystem. With enough developers dedicated to advancing that new ecosystem, the result could be a slow, durable shift away from CUDA. That shift won’t happen overnight — remember, it took Nvidia 18 years to build the CUDA ecosystem of today; building a competitive software ecosystem is a multi-year effort even under pressure. But what started as necessity may, over time, harden into habit — and eventually, into infrastructure that can compete with Nvidia’s software stack.
Special thanks to Jeff Ding and Kevin Xu for thoughtful feedback on prior drafts.
