---
title: "Zhihu Frontier Weekly｜DeepSeek, Huawei, ByteDance, Xiaomi and More: China’s AI Infrastructure Race Heats Up"
url: "https://substack.com/app-link/post?publication_id=6222474&post_id=204084745&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDQwODQ3NDUsImlhdCI6MTc4MjcyNDk5NSwiZXhwIjoxNzg1MzE2OTk1LCJpc3MiOiJwdWItNjIyMjQ3NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.wuqmrXht9Z9L7rUJfxWaj1k4NAoWmHqqCt4LjTD9lRA"
fetched_at: 2026-07-05T04:01:05.887332+00:00
source_date: 2026-06-29
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Zhihu Frontier Weekly｜DeepSeek, Huawei, ByteDance, Xiaomi and More: China’s AI Infrastructure Race Heats Up

Source: https://substack.com/app-link/post?publication_id=6222474&post_id=204084745&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=2flx6&token=eyJ1c2VyX2lkIjo0MDg3NDgyLCJwb3N0X2lkIjoyMDQwODQ3NDUsImlhdCI6MTc4MjcyNDk5NSwiZXhwIjoxNzg1MzE2OTk1LCJpc3MiOiJwdWItNjIyMjQ3NCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.wuqmrXht9Z9L7rUJfxWaj1k4NAoWmHqqCt4LjTD9lRA

Welcome to
Zhihu Frontier
,
your window into the hottest AI convos from China’s knowledge platform.
The conversation this week extended well beyond model releases. China’s first CPU-only exascale supercomputer topped the TOP500 rankings, Huawei introduced a new chip design philosophy, ByteDance rolled out major upgrades to Seed, and DeepSeek and Zhipu signaled a broader shift toward domestic AI infrastructure.
Here are the stories—and expert perspectives—from the Zhihu community.
China’s new
LineShine
supercomputer has officially claimed the No.1 spot on the TOP500 list. Built with 47,000 Huawei Kunpeng CPUs and exceeding 2 exaFLOPS, it’s also the world’s first officially recognized CPU-only exascale supercomputer.
💬 Explore the community discussion:
https://www.zhihu.com/question/2032659692376343993/answer/2052920072528831413
Zhihu contributor @一根弦
I see three major technical highlights.
First, the efficiency numbers are extraordinary.
While LineShine’s theoretical FP64 performance (2.735 EFLOPS) is slightly below El Capitan’s 2.82 EFLOPS, its measured HPL performance reached
2.198 EFLOPS
, more than 20% higher than El Capitan’s 1.8 EFLOPS. That makes it the world’s first officially recognized supercomputer to surpass the
2-exaFLOPS
HPL milestone.
Looking across the current TOP10 systems, LineShine achieves an
HPL efficiency of 80.3%
, while El Capitan reaches only 64%. Only Japan’s Fugaku (82%) and Germany’s JUPITER Booster currently post slightly higher efficiency numbers.
Second, its architecture is unusually bold.
Unlike nearly every modern flagship system pursuing heterogeneous CPU+GPU designs, LineShine adopts a
homogeneous CPU architecture
. Achieving such high HPL efficiency is considerably easier in homogeneous systems, but choosing this path today required real confidence when everyone else is racing toward heterogeneity.
High efficiency also implies an exceptionally strong interconnect. At this scale, without extremely high bandwidth and network stability, HPL efficiency would collapse long before reaching 80%.
Third, the disclosed hardware hints at several key architectural features.
Based on public information and Torsten’s observations, the LX2 CPU likely includes matrix-computing units similar to Tensor Cores—possibly ARM SME (Scalable Matrix Extension)—along with HBM (High Bandwidth Memory).
Matrix engines provide strong compute capability, while HBM prevents memory bandwidth from becoming the bottleneck. In many ways, the chip resembles a GPU equipped with Tensor Cores and HBM, yet retains the advantages of a general-purpose CPU for instruction processing.
Xiaomi officially launched its first NAS through crowdfunding, starting at RMB 2,299. Rather than targeting enthusiasts, the product focuses on lightweight home storage and media management.
💬 Read the full discussion:
https://www.zhihu.com/question/2053074417689931982
Zhihu contributor @Neko Fox
This is a very typical entry-level NAS configuration. The Realtek RTD1619B is a quad-core ARM processor introduced in 2022 for lightweight NAS products, and it’s already used by numerous devices from Synology, QNAP, TerraMaster, Lenovo, UGREEN, Hikvision and others.
Its core capabilities are exactly what most home users expect: file storage, backup, sharing, photo synchronization, remote downloads and media libraries. Since the chip includes an NPU, AI-powered photo management—such as face recognition—comes essentially as standard.
For most consumers, that’s more than enough. The limitation comes if you’re looking for an all-in-one home server or advanced Docker workloads, which ARM-based entry-level NAS devices generally don’t support. Personally, I also think a
4-bay + 1-drive
entry configuration would have offered better long-term upgrade flexibility than Xiaomi’s current design.
ByteDance has launched
Doubao Pro
, offering three subscription tiers priced up to RMB 6,000 per year. But are users actually getting more value?
💬  See what Zhihu users are discussing:
https://www.zhihu.com/question/2053056486595629534
Zhihu contributor @恋猫
Since both products come from ByteDance, I can’t help comparing it with
Trae Work
, which actually feels like the stronger experience despite Doubao’s broader brand recognition.
The pricing itself follows today’s increasingly common “fuzzy pricing” strategy:
Standard: RMB 68/month (RMB 688/year), with over five times the quota of the free plan.
Plus: RMB 200/month (RMB 2,048/year), offering roughly four times the Standard quota.
Premium: RMB 500/month (RMB 5,088/year), offering ten times the Standard quota.
The real issue is that ByteDance never clearly explains what the free quota actually is. Without concrete token limits or workload estimates, users only get a vague sense of the differences, making it difficult to judge the true value of each tier.
Both DeepSeek and Zhipu have announced plans to deploy Huawei’s new
Ascend 950 Supernode
at scale later this year, highlighting China’s accelerating investment in domestic AI infrastructure.
💬  Join the discussion:
https://www.zhihu.com/question/2050591443664779181
Zhihu contributor @知乎用户
I initially assumed Huawei’s ecosystem would be difficult to use, but after working with it for several days, I was pleasantly surprised.
Triton compatibility is already fairly mature, and Huawei’s Ascend C documentation is detailed enough to make development practical. Performance still trails NVIDIA, but at least you understand where the bottlenecks are instead of being left completely confused. Their developer community is also responsive when technical issues arise.
In some ways, the experience is actually smoother than AMD’s tooling. Huawei provides profiling tools similar to NVIDIA Nsight Systems, and enterprise customers can even receive direct engineering support for drivers and deployment.
The biggest challenge is that Ascend’s programming model is more complicated than CUDA. Developers need to explicitly manage Cube units, Vector units, DMA, Unified Buffer, data movement and several hardware-specific components, making kernel development more complex.
That said, this is becoming much more manageable in 2026 thanks to coding agents and dedicated projects like
Awesome Ascend Skills
. Without modern AI coding tools, writing Ascend kernels manually would still be significantly harder—but fortunately, very few developers work that way anymore.
ByteDance has released
Seed 2.1 Pro
, its latest flagship language model. While the upgrade isn’t revolutionary, early evaluations suggest it reinforces Seed’s traditional strengths—at the cost of significantly higher token usage and pricing.
💬 Read the original discussion:
https://www.zhihu.com/question/2052334882773283806
Zhihu contributor @toyama nao
As the chatbot era winds down and the Agent era continues to take shape, Seed once held the domestic SOTA position for several months thanks to its strong multimodal capabilities and reasoning performance. But while Seed was leading, second-tier competitors rapidly caught up, and even ByteDance’s own
Seedance
continued dominating the video generation space. It’s only natural that the Seed language model team wants to reclaim the top position.
The longer users wait, the higher their expectations become. Four months is enough time for Chinese competitors to iterate twice—and North American leaders three times. While
Seed 2.1 Pro
isn’t a dramatic leap over Seed 2.0 Pro, it’s a solid, disciplined upgrade that strengthens existing advantages while addressing known weaknesses.
One notable change is its willingness to fully utilize its token budget. Under the
High
reasoning mode, the model almost always consumes the maximum allocation available. As a result, average reasoning usage jumps to an unprecedented
65K tokens
, roughly 25% higher than the next closest competitor. Even its non-reasoning mode, once known for efficiency, now averages around
5K tokens
and occasionally behaves much like a reasoning model.
Pricing has also nearly doubled—from
16 to 30 per million tokens
—making it the most expensive domestic model currently available. Only GPT and Claude Opus remain more expensive overall. This likely reflects growing compute pressure rather than a purely commercial decision.
ByteDance has also introduced
Seedance 2.5
, the latest version of its video generation model. While it may not deliver the same “wow” factor as 2.0, creators see meaningful progress in controllability and professional workflows.
💬 Explore the discussion:
https://www.zhihu.com/question/2052734400673190128
Zhihu contributor @贤最
At first glance,
30-second generation
and support for
50 reference images
sound extremely impressive. The showcased long, continuous camera shots are also visually striking.
But those numbers aren’t what matter most to me. Previous versions often struggled with prompt following, camera language, reference consistency and general controllability. Whether 2.5 truly solves those issues still needs real-world testing, so I wouldn’t draw conclusions yet.
What excites me much more is the newly introduced
white-model rendering
workflow. As someone creating science fiction content, AI has long struggled with spatial scale, dynamic storyboarding and cinematic shot planning. Improving professional controllability is exactly the direction AI creative tools should be heading.
Although Seedance 2.5 isn’t as eye-catching as the original 2.0 launch, it’s still a meaningful upgrade. Compared with recent releases like Grok 1.5 and Alibaba’s HappyHorse 1.1, Seedance remains comfortably ahead of competitors in AI video generation.
If you’d like to explore more discussions from the Zhihu community this week:
📬
That’s all for this week’s AI round-up from Zhihu Frontier.
👉 Subscribe to never miss an update:
zhihufrontier.substack.com
