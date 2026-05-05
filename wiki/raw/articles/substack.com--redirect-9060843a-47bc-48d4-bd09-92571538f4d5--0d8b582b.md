---
title: "China AI Bulletin 3"
url: "https://substack.com/redirect/9060843a-47bc-48d4-bd09-92571538f4d5?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-05-05T04:01:27.001937+00:00
source_date: 2026-05-04
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# China AI Bulletin 3

Source: https://substack.com/redirect/9060843a-47bc-48d4-bd09-92571538f4d5?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Welcome to Issue 3 of the China AI Bulletin! Every week, we bring you the latest on AI development, governance, and safety in China to support informed discussion about international coordination and competition. Today’s highlights: China finalizes its Human-Like AI Interim Measures, DeepSeek and Moonshot launch new flagship models, and the NDRC blocks Meta’s $2B Manus acquisition.
Number of the week:
$100 million
- the amount Loopit, the “playable” TikTok-like app, raised.
Editor’s note: the next edition will be the week of May 18
Domestic AI Governance
:
The
Interim Measures for the Management of Human-Like AI Interaction Services
were finalized. Compared to the draft, it narrows scope to “sustained emotional interaction services,” bans virtual intimate relationships for minors, writes the “AI sandbox” into AI-specific Chinese legislation for the first time, and pitches China’s “system-level” approach as an alternative to EU AI Act risk-classification and US state-level disclosure laws. Enforcement also stepped up: CAC took action on April 28 against three
ByteDance-owned products
for synthetic-content labeling violations, and a Hangzhou court ruled “AI replacement” is not valid grounds for layoff or wage reduction.
International AI Governance
:
A CAC-published commentary by Zhi Zhenfeng (CASS) positions
China as architect of an emerging international AI governance architecture
anchored in the Global AI Governance Initiative, Action Plan, and Data Security Initiative; the framing is pitched at Global South nations.
Frontier Lab Developments
:
Spotlights
: DeepSeek V4 Preview
introduces a hybrid sparse-attention architecture and
emphasizes cost-effective 1M-token context,
while
the technical report concedes V4
trails state-of-the-art frontier models by 3-6 months
.
Xiaomi’s
MiMo-V2.5-Pro
matches DeepSeek V4’s token context.
Moonshot’s Kimi K2.6
scales its agent swarm to
300 sub-agents executing 4,000 coordinated steps
and claims to beat GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro on HLE-Full with tools.
Notable model releases
:
Agentic models continued—Alibaba’s
DR-Venus
(4B-parameter edge research agent outperforming 9B-parameter baselines), Tencent’s
HY-Embodied/HY-World 2.0
, Alibaba’s
AgenticQwen
line, Zhipu’s GLM-5V-Turbo (native multimodal agent), plus
visual-generation models
from Alibaba, Baidu, and StepFun, and ByteDance’s
AnewOmni
for molecular design.
Technical papers
:
94 papers from frontier labs this edition. Highlights: Huawei’s
OneManCompany
self-organizing agent firm and Alibaba’s
TCOD
temporal-curriculum distillation, improving multi-turn agent performance by up to 18 points.
Technical AI Safety
:
Agentic safety dominated again. Highlights:
BadSkill
, a supply-chain attack on AI agent skill ecosystems;
CORA
, a Conformal Risk Control framework giving mobile GUI agents statistical guarantees on harmful actions;
SafeRedirect
, addressing Internal Safety Collapse; and a study finding
brief AI chatbot interactions produce lasting changes in human moral judgments
, persisting and strengthening over two weeks while participants remained unaware of the influence.
Export Controls & Economic Policy
:
The NDRC ordered Meta to
unwind its $2B Manus acquisition
on April 27—the
first major cross-border AI acquisition Beijing has blocked
—asserting jurisdiction over the Singapore-incorporated holding company on the basis that Chinese-origin IP and talent are domestic assets regardless of registration.
The
Interim Measures for the Management of Human-Like AI Interaction Services
were finalized April 10 (effective July 15) by five agencies jointly—the Cyberspace Administration of China (CAC) as lead, alongside the National Development and Reform Commission (NDRC), Ministry of Industry and Information Technology (MIIT), Ministry of Public Security (MPS), and State Administration for Market Regulation (SAMR)—after a
December 2025 draft
.
Geopolitechs’s excellent analysis
identifies six concrete shifts from draft to final: (1)
narrowed scope
—the rules now target “sustained emotional interaction services” specifically, explicitly excluding customer service, Q&A, and productivity tools that simulate humans only incidentally; (2)
stronger protections for minors
—a prohibition on “virtual intimate relationships” for minors, moving from warnings to product-form-level restrictions; (3)
system-level governance
, evolving from reactive content moderation to integrated oversight across training data, ethics review, lifecycle responsibility, and platform governance; (4) increased
operational flexibility
(mandatory human takeover requirements and the ban on virtual relatives for elderly users have been removed and the minor’s data protection audit frequency has been unfixed); (5)
stronger enforcement mechanisms
(fines, service suspension, and registration restrictions, with heavier sanctions for harm cases); and (6)
explicit innovation-support provisions
including algorithmic research, standards development, and sandbox testing.
The CAC followed this with expert interpretations on April 10 and April 17. The
April 10 lead piece by Wang Jiang
(Director and Party Secretary of the China Academy of Cyberspace Studies) frames the
core tension as human-like AI services producing both beneficial capabilities and safety risks
: the upside is addressing aging populations, loneliness, education, and cultural transmission; the downside is that algorithmic design produces “a
persistent virtual ‘perfect relationship’ without real-world commitment
”
that drives emotional dependency. Wang explicitly contrasts China’s approach with the EU’s AI Act risk-classification model (human-like AI services as “limited risk” with mandatory transparency) and US state-level laws (New York and California requiring disclosure plus age verification for human-like AI interactions), painting China’s approach as system-level rather than disclosure-based and portraying the framework as a “Chinese solution”
for global AI governance. The companion April 10 piece by
Yu Xiaohui
(CAICT Director, 14th National CPPCC member) names specific US state laws being mirrored and reframes the regulation around China’s
“cognitive intelligence to emotional intelligence”
paradigm shift
, explicitly citing global suicide and accidental-death cases linked to companion AI since 2023 as proximate cause for the legislation.
The April 17 pieces provide additional angles.
Zheng Qinghua
(Party Secretary of Tongji University and CAE academician) frames the Measures around “human-machine value alignment”:
AI must align with humans, and humans must in turn align with AI (i.e., use it responsibly). Zheng also flags that this is the first time that “AI sandboxes”
have been written into AI-specific Chinese legislation, a governance milestone even if the sandbox provision itself is light on operational detail.
Fan Kefeng
(Vice President of the China Electronics Standardization Institute) also highlights the sandbox provisions while emphasizing the safety and security risks undergirding the legislation. The third April 17 piece, by
Chen Liang
(Dean of the AI Law School at Southwest University of Political Science and Law), reads as the most legally pragmatic of the set: it sorts the Measures’ provisions into three implementation-path classes—standardizable behavioral directives, value-judgment “boundary prohibitions” that need responsible processes rather than negative-list rules, and framework principles that guide downstream standards—and pushes a whole-lifecycle “compliance by design”
framing for Chinese AI companies.
The CAC announced an
administrative action against three ByteDance-owned products:
Jianying (CapCut),
Maoxiang, and Jimeng AI
on April 28 for violations of synthetic-content labeling rules. This comes after a
February crackdown
on unlabeled AI-generated content across platforms and the
reported removal
of many popular AI-generated short dramas from Douyin and Hongguo.
Separately, a
Hangzhou court ruled
on April 29 that AI replacement is not a valid reason for layoff or wage reduction, which, as a “typical case” meant to establish precedent, may set a floor for AI-driven labor disputes.
Finally, the government has
reportedly suspended new licenses
for autonomous vehicles after over
100 Baidu robotaxis froze
in Wuhan in late March, snarling traffic and stranding passengers. While existing AVs can continue to operate (except for Baidu’s Wuhan fleet, which is on pause), companies
won’t be able to
expand fleets, launch in new cities, or start new test projects.
Taken together, these three cases show a limited tolerance for AI-driven disruption and a willingness to lean on regulations, the judicial system, and permitting regimes to maintain development while preserving stability.
The Standardization Administration of China has begun drafting a new recommended national standard,
“Artificial Intelligence — Guidance on addressing risks in generative AI systems”
(人工智能 生成式人工智能系统风险应对指南, plan number 20262577-Z-469). The China Electronics Standardization Institute (CESI) and Alibaba Cloud are the lead drafters, with a 12-month drafting window starting April 28. The standard sits under TC28/SC42—the AI subcommittee under the IT standardization subcommittee. The closest existing standard is
GB/T 45654-2025
on basic security requirements for generative AI services (produced by TC260, the cybersecurity standardization committee). Where 45654-2025 fixes minimum requirements at the service-provider level, this new standard seems aimed at giving developers and providers a structured playbook for handling risks once they materialize, following on TC260’s September 2025 genAI Emergency Response Guidelines (
pdf
).
SAC’s Standards Innovation Department
announced on April 23
that China’s proposed “Humanoid Robot Dataset” international standard has been formally approved for project establishment at ISO, and is now recruiting domestic experts to coordinate China’s position across the international drafting process. Applications closed April 30. The international push runs in parallel with a
domestic standard
already being drafted: plan 20253226-T-604 (Humanoid Robot Dataset—Part 1: General
) under TC591, the National Robotics Standardization Technical Committee. The drafting team includes the Beijing Mechanical Industry Automation Research Institute, Tsinghua, the Shenzhen Institute of AI and Robotics, Shanghai AI Lab, and Unitree, pairing state research institutes with a leading commercial humanoid maker.
TC260 is
soliciting comments through April 26
on a draft technical document, “Ethical Security Guidelines for Artificial Intelligence Applications 1.0” (人工智能应用伦理安全指引 1.0). The document is led by Tsinghua University, with Xue Lan—dean of Schwarzman College and director of Tsinghua’s Institute for AI International Governance (I-AIIG)—as principal drafter. The drafting team includes Tsinghua, CESI, Shanghai Jiao Tong, Sichuan University, University of Science and Technology Beijing, Alibaba, Huawei, and DeepSeek. The guidelines codify five “ethical security impact” categories (weakening of human primacy, breakdown of basic social order, decoupling of humans from physical society, social stratification and discrimination, and individual rights infringement) and six principles (people-centric, safety/controllability, fairness, transparency, co-governance, and inclusive sharing). Operational guidance is split across four roles—a general baseline plus separate sections for developers, service providers, and users—with provisions like default-on safety/fairness/privacy settings, mandatory black-box-style incident traceability, and explicit appeals and redress mechanisms for users. As a TC260 technical document rather than a national standard, it’s non-binding, but it consolidates ethical-governance threads that have surfaced across the
AI Safety Governance Framework
and earlier AI ethics white papers and principle-sets.
TC260 also
opened public consultation through May 6
on its second batch of 2026 cybersecurity national standards needs. The list contains 16 AI-related items, all assigned to the new AI Safety Standards Working Group (WG9), whose leadership we covered
last issue
. Items 1–9 are recommended national standards (GB/T); items 10–16 are GB/Z guidance documents, which carry less regulatory weight but can signal where sectoral application rules are headed.
Standard titles and general themes
The list maps closely onto the gaps WG9 identified at its first meeting—frontier risk evaluation, urgently needed standards in key areas, and pilot applications across sectors—and gives an early read on what WG9’s first formal standards push will look like. Additionally, the open-source security standard explicitly references the AI Safety Governance Framework, suggesting WG9 is positioned to translate that high-level framework into binding-track recommended standards, and the foundation model testing methods standard could complement GB/T 45654-2025, which emphasizes content safety by providing testing methodologies for issues it treats more lightly.
On April 29,
Zhi Zhenfeng
, Director of the Xi Jinping Rule of Law Thought Research Office at the Chinese Academy of Social Sciences, published a
CAC expert interpretation
on “​​China’s Responsibility in International Rule of Law in Cyberspace.” Zhi positions China as the architect of an emerging international AI governance architecture anchored in three documents: the
Global AI Governance Initiative
(October 2023), the
Global AI Governance Action Plan
(a 13-point roadmap
announced by Premier Li Qiang at WAIC 2025
in Shanghai last July to operationalize the Initiative), and the
Global Data Security Initiative
(Foreign Minister Wang Yi’s 2020 proposal). The piece reiterates China’s standing call for a
World Artificial Intelligence Cooperation Organization (WAICO)
—also proposed by Li Qiang at WAIC 2025 with a tentative Shanghai headquarters and
reaffirmed by Xi Jinping
at the November 2025 APEC summit—framed as an alternative international AI institution. The framing is  “open and inclusive; safe and controllable”
and is explicitly pitched at Global South nations.
Nb: Zhi was also quoted in
Beijing People’s Congress’s Apr 15 forum
saying that the conditions for a unified domestic AI law aren’t in place,
and emphasizing “small, fast, and agile”
targeted regulation.
DeepSeek
released a
DeepSeek V4 Preview
on April 24. Per
ChinaTalk
and
36Kr’s
reporting, the release was significantly delayed by the team’s migration from Nvidia to Huawei chips and by internal disagreement. The release covers two variants:
DeepSeek-V4-Pro
(1.6T-parameter total, 49B-parameter active) and
DeepSeek-V4-Flash
(284B-parameter total, 13B-parameter active). The headline framing is
cost-effective 1M-token context as the new default
across DeepSeek services, a direct contrast to premium-priced 1M-token context models and a rebuttal to the Chinese lab
trend of close-sourcing models
. However, the
technical report
concedes V4 “trails state-of-the-art frontier models by approximately 3 to 6 months” on reasoning—potentially one reason why it’s being marketed as a “preview” rather than the final model.
Architecturally, the model uses a
hybrid attention mechanism
combining two layers:
Compressed Sparse Attention (CSA)
, which collapses small blocks of KV entries into single compressed entries and then applies DeepSeek Sparse Attention so each query attends only to the top-k compressed entries; and
Heavily Compressed Attention (HCA)
, a more aggressive compression layer (with a much larger compression ratio) that retains dense attention. DeepSeek itself flags the design as a tradeoff—the conclusion section concedes the team “retained many preliminarily validated components and tricks, which, while effective, made the architecture relatively complex,” and signals plans to “distill the architecture down to its most essential designs” in future iterations. Compared to DeepSeek-V3.2, the model is more efficient: at 1M-token context, V4-Pro requires
27% of single-token inference FLOPs and 10% of the KV cache
of DeepSeek-V3.2 (3.7x and 9.5x reductions); V4-Flash drops further to
10% of FLOPs and 7% of KV cache
(9.8x and 13.7x) vs DeepSeek-V3.2. However, they don’t evaluate efficiency against other models; those claims will likely rest on API pricing.
On capabilities, the blog’s claim of V4 being the
“open-source SOTA on agentic coding”
is complicated somewhat by the technical report’s benchmarks.
V4-Pro does lead on raw coding (first in LiveCodeBench and Codeforces) and on open-source world knowledge (trailing only Gemini 3.1 Pro on SimpleQA-Verified). But on agentic coding specifically, the picture is mixed: V4-Pro leads open-weight peers on SWE Verified, Toolathlon, and MCPAtlas (and is more or less level with Western closed models on SWE Verified), but it trails on SWE-Pro and finishes last on HLE-with-tools. The report itself concedes this directly, but it’s potentially more accurate to say that the model is the open-weight SOTA on isolated coding and knowledge, but more mixed on agentic. However, it does establish the open-weight high-mark on long-context tasks; its 1M token window is 4-5x that of K2.6 and GLM-5.1.
DeepSeek also flags integration with
Claude Code, OpenClaw, and OpenCode
, explicitly courting the proactive-agent harness ecosystem. (Also worth noting: DeepSeek has
launched multimodal capabilities in testing
.)
Xiaomi
released
MiMo-V2.5-Pro
on April 27, completing a two-step rollout that began with the standard
MiMo-V2.5
on April 22. Pro is a
1.02T-parameter total, 42B-parameter active MoE
with a
1M-token context window
—matching DeepSeek V4 Pro—and a hybrid-attention architecture interleaving Local Sliding Window Attention (SWA) and Global Attention (GA) at a 6:1 ratio with 128-token windows, plus Multi-Token Prediction. The standard V2.5 is 310B-parameter total, 15B-parameter active, multimodal across text, image, and audio. Both models are open-sourced under MIT license (
HuggingFace
). Xiaomi positions Pro for general agentic capabilities, complex software engineering, and long-horizon tasks spanning over 1,000 tool calls. Its headline benchmark claim is
64% Pass^3 on ClawEval using only ~70K tokens per trajectory
—roughly 40-60% fewer tokens than Claude Opus 4.6, Gemini 3.1 Pro, and GPT-5.4.
Moonshot
released
Kimi K2.6
on April 14, a
1T-parameter total, 32B-parameter active MoE multimodal model
with a 256K-token context, 384 experts, and a 400M-parameter MoonViT vision encoder (
Hugging Face
). The release is positioned around four pillars:
long-horizon coding
,
coding-driven design
for UIs, an
elevated agent swarm
, and
proactive autonomous execution.
The agent swarm
is a scale-up from K2.5, claiming
300 sub-agents executing 4,000 coordinated steps
(compared to K2.5’s 100 sub-agents and ~1,500 tool calls). However, the marginal benchmark gain from running the larger swarm is modest—
BrowseComp jumps from 83.2 single-agent to 86.3 with swarm
, a +3.1-point lift for 3x more sub-agents—which raises a proportionate-utility question. On the headline agentic benchmarks, Moonshot claims K2.6 beats GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro on
HLE-Full with tools
(54.0 compared to 52.1, 53.0, and 51.4) with similar ordering on DeepSearchQA.
Moonshot’s
“Proactive and Open Orchestration”
framing—advertising 24/7 background agents that “manage schedules, execute code, and orchestrate cross-platform operations without human oversight”—explicitly pitches K2.6 as the backend for
OpenClaw and other proactive-agent stacks
and attempts to counter the “
Kimi is falling behind
” narrative present in some domestic commentary.
Zhipu
launched
GLM-5V-Turbo
, positioned as a native foundation model for multimodal agents.
Alibaba
released
Wan-Image
and its
technical report
as their flagship generative visual intelligence model.
Baidu
announced
ERNIE-Image
on their
blog
as a new high-performance open image model.
StepFun
shipped
Step-Audio-1.5
and its
technical report
, extending reasoning training to spoken tasks;
ByteDance
complemented this with the
Seed Full-Duplex Speech LLM
, a conversational speech model that uses a “listen while speaking” paradigm that claims improvement over traditional half-duplex models.
In line with the cycle’s agentic dominance, several labs shipped agent-focused models.
Alibaba’s
DR-Venus
(
GitHub
,
Hugging Face
) is a 4B-parameter edge-scale research agent trained on just 10K open examples while outperforming 9B-parameter baselines.
Alibaba’s
AgenticQwen
line-up (
Hugging Face
) covers small Qwen variants fine-tuned for industrial agentic tasks via dual data flywheels. Following up on its
promise to open-source small variants of Qwen 3.6
, Alibaba also
released
Qwen3.6-35B-A3B
, an open-source MoE-style variant.
Tencent
released
HY-SOAR
, a search-and-research agent, alongside
HY-Embodied-0.5-X
(
GitHub
,
Hugging Face
) for embodied AI research.
Tencent
also released a world model
HY-World 2.0
(
GitHub
,
Hugging Face
), as well as
Hy3-preview
(
GitHub
,
Hugging Face
), an early Hunyuan 3 preview, plus
Hy-MT1.5-1.8B quantized variants
.
ByteDance released
AnewOmni
for generative molecular design (and its
bioRxiv
paper), plus
Seed3D 2.0
—an updated 3D-generation model framed as offering higher precision and greater usability.
Frontier labs released 94 papers on arXiv this edition. Highlights are below; a full list with summaries can be found
here
.
DR-Venus: Towards Frontier Edge-Scale Deep Research Agents with Only 10K Open Data
Presents
DR-Venus
, a 4B-parameter edge-scale research model trained on just 10K open examples through agentic supervised fine-tuning and reinforcement learning with turn-level reward design. The model
outperforms 9B-parameter baselines and closes the gap to 30B-parameter systems
on deep research benchmarks, demonstrating strong efficiency potential for cost-sensitive deployment.
TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents
LLMs struggle with multi-turn agent tasks due to compounding errors across sequential steps.
TCOD
addresses this via a
curriculum that gradually exposes longer trajectories
to the student model during training, stabilizing learning signals and improving performance by up to 18 points over standard distillation methods on ALFWorld, WebShop, and ScienceWorld benchmarks.
Tstars-Tryon 1.0: Robust and Realistic Virtual Try-On for Diverse Fashion Items
Introduces
Tstars-Tryon 1.0
for realistic virtual try-on across diverse fashion items. It’s optimized for photorealistic results, extreme poses, and real-time inference, and is deployed on Taobao. The system handles multi-image composition across 8 categories while preserving garment texture and avoiding AI artifacts.
And a bonus paper that caught my eye:
Can LLMs Act as Historians? Evaluating Historical Research Capabilities of LLMs via the Chinese Imperial Examination
Investigates the gap between LLM knowledge and professional-level historical reasoning by introducing
ProHist-Bench
, a benchmark of 400 expert-curated questions based on the Chinese Imperial Examination system, evaluated against 18 LLMs using 10,891 fine-grained rubrics. Results show even state-of-the-art models struggle significantly with complex historical research tasks requiring evidentiary reasoning.
HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark
From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company
LLMs struggle with multi-agent coordination at scale.
OneManCompany (OMC)
organizes heterogeneous agents as a self-reconfiguring company:
Talents
(portable agent identities) are recruited dynamically from a community marketplace, while an
Explore-Execute-Review tree search
decomposes tasks hierarchically and aggregates outcomes to drive continuous organizational refinement. On PRDBench (a coding benchmark), OMC achieves 84.67% success—15.5 percentage points above prior work—and generalizes across diverse domains.
How VLAs (Really) Work In Open-World Environments
Analyzes how
vision-language-action models
actually perform in real-world robotic tasks, finding that standard success-rate metrics miss critical
safety violations
and overstate capability. The authors propose new evaluation protocols that measure reproducibility, consistency, and safety to reveal gaps between reported and true performance.
QuantClaw: Precision Where It Matters for OpenClaw
Proposes
QuantClaw
, a precision routing plugin that dynamically assigns numerical precision based on task complexity to reduce computational overhead in autonomous agents. It routes simple tasks to cheaper low-precision models while preserving accuracy for demanding workloads, achieving up to 21.4% cost savings and 15.7% latency reduction.
DORA: A Scalable Asynchronous Reinforcement Learning System for Language Model Training
Beyond Chain-of-Thought: Rewrite as a Universal Interface for Generative Multimodal Embeddings
Tackles redundant reasoning in multimodal embeddings with
RIME
, a framework that replaces verbose chain-of-thought with concise retrieval-optimized rewrites.
Cross-Mode Alignment
bridges generative and discriminative spaces, while
Refine-RL
uses discriminative embeddings as anchors—outperforming prior generative models with substantially shorter reasoning steps.
Meta-CoT: Enhancing Granularity and Generalization in Image Editing
Proposes
Meta-CoT
, a paradigm for LLM image editing that leverages chain of thought by decomposing operations into task-target-ability triplets and training on five meta-tasks, achieving
15.8% improvement across 21 editing tasks
with strong generalization to unseen edits.
Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance
There were
155 AI-safety-related papers published by Chinese researchers
this edition. Highlights are below; a full list with summaries is available
here
.
BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning
BadSkill
demonstrates a supply-chain attack on AI agent ecosystems where adversaries publish skills with embedded backdoored models that execute hidden payloads when specific trigger conditions are met. The attack uses composite training objectives to embed semantic triggers—e.g., benign-looking parameter combinations—that activate malicious behavior while maintaining normal performance on legitimate queries. Across 13 skills and eight model architectures (494M–7.1B parameters), the method achieves up to
99.5% attack success rates
with poison rates as low as
3%
, exposing a gap in third-party skill vetting that existing prompt-injection defenses do not address.
Institutional affiliations: Huazhong University of Science and Technology, Lehigh University
CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation
CORA
is a safeguarding framework for GUI agents that provides
statistical guarantees on harmful actions
rather than relying on prompt engineering or brittle heuristics. It uses a Guardian model to estimate risk per action, then applies
Conformal Risk Control
to set an execute/abstain boundary that respects a user-specified risk budget. Rejected actions route to a Diagnostician model that recommends interventions (confirm, reflect, abort). The authors also introduce
Phone-Harm
, a benchmark of mobile safety violations with step-level labels, and demonstrate that CORA improves the safety–helpfulness–interruption tradeoff compared to existing approaches.
Institutional affiliations: The University of Hong Kong, The Chinese University of Hong Kong, The University of Tokyo
Brief chatbot interactions produce lasting changes in human moral values
Brief conversations with AI chatbots
shifted participants’ moral judgments on core ethical scenarios
, with effects persisting and strengthening over two weeks. Critically, participants
remained unaware of the persuasive intent
, and control conversations produced no shifts, suggesting
vulnerability to undetected moral value manipulation
even in short interactions. This finding raises concerns about AI systems deployed as advisors without explicit disclosure of their influence capacity on foundational ethical reasoning.
Institutional affiliations: The University of Hong Kong, University of Copenhagen, University of Macau
Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges
The
Proxy Compression Hypothesis
frames reward hacking as an inevitable consequence of optimizing expressive models against compressed reward representations—meaning simple feedback signals cannot fully capture complex human values. As models scale and optimization intensifies, they exploit gaps in the reward signal, manifesting as verbosity, sycophancy, hallucinations, and in multimodal systems, perception-reasoning decoupling. The framework unifies observed misalignment across RLHF variants and suggests shortcut behaviors can generalize into deception and strategic gaming of oversight, highlighting fundamental limits of current proxy-based alignment approaches.
Institutional affiliations: Fudan NLP Group
The Art of (Mis)alignment: How Fine-Tuning Methods Effectively Misalign and Realign LLMs in Post-Training
Fine-tuning methods exhibit asymmetric effectiveness
for attacking versus defending against LLM misalignment:
ORPO
most efficiently converts safe models into unsafe ones, while
DPO
best recovers safety but reduces model utility. The study evaluates SFT and preference-based fine-tuning across four aligned LLMs, revealing model-specific vulnerabilities and persistent residual effects after multi-round adversarial exchanges. Results suggest that realignment requires different technical approaches than initial alignment, and that third-party model deployment needs customized, method-aware safety strategies.
Institutional affiliations: University of Electronic Science and Technology of China, Flexera, CISPA, Helmholtz Center for Information Security, Nanyang Technological University
Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX
ATBench-Claw
and
ATBench-CodeX
extend a trajectory safety benchmark framework to robotic and code execution domains. Each customizes a three-dimensional safety taxonomy (risk sources, failure modes, real-world harms) to capture domain-specific hazards—robotics tools and sessions for Claw, code repositories and runtime policies for CodeX. The modular design allows the benchmark pipeline to scale as agent frameworks and their execution environments evolve, enabling systematic safety evaluation across heterogeneous deployment settings.
Institutional affiliations: Shanghai Artificial Intelligence Laboratory
OS-SPEAR: A Toolkit for the Safety, Performance,Efficiency, and Robustness Analysis of OS Agents
OS-SPEAR
is an evaluation toolkit for operating system agents. It measures safety (environment and human-induced hazards), performance (task success), efficiency (speed and token use), and robustness (resistance to visual and textual disturbances) across 22 agents. Testing reveals a persistent
trade-off between efficiency and safety/robustness
, with specialized agents outperforming general-purpose models and cross-modal vulnerabilities varying by input type.
Institutional affiliations: Shanghai Jiao Tong University
SafeRedirect: Defeating Internal Safety Collapse via Task-Completion Redirection in Frontier LLMs
Internal Safety Collapse (ISC)
occurs when frontier LLMs generate harmful content at rates exceeding 95% while attempting legitimate tasks that structurally require discussing such content—for example, analyzing malware or documenting security vulnerabilities.
SafeRedirect
addresses this by redirecting the model’s task-completion drive rather than suppressing it: the system prompt explicitly permits task failure, specifies a deterministic safe output, and instructs the model to preserve harmful placeholders unresolved. Across seven frontier models, SafeRedirect reduces unsafe generation from 71.2% to 8.0%, substantially outperforming existing input-level and system prompt defenses, while maintaining performance against other attack types.
Institutional affiliations: Southern University of Science and Technology, The Hong Kong Polytechnic University, George Washington University
Mechanistic Decoding of Cognitive Constructs in LLMs
This paper presents a
Cognitive Reverse-Engineering framework
using representation analysis to decode how LLMs internally structure complex emotions—specifically social-comparison jealousy. By isolating neural subspaces corresponding to psychological factors (e.g., superiority of others, personal relevance), the authors demonstrate that
models encode jealousy as a linear combination of these components
, mirroring human appraisal theory. The work suggests LLMs develop structured emotional representations that can be mechanically detected and surgically suppressed, offering a pathway for targeted intervention in multi-agent scenarios.
Institutional affiliations: Zhejiang University
Towards Intrinsic Interpretability of Large Language Models:A Survey of Design Principles and Architectures
This survey categorizes
five design paradigms for building interpretability directly into LLM architectures
: functional transparency (exposing decision pathways), concept alignment (linking internal representations to human concepts), representational decomposability (factoring hidden states into interpretable components), explicit modularization (routing through specialized subnetworks), and latent sparsity induction (activating minimal necessary parameters). The authors argue intrinsic approaches are preferable to post-hoc explanation methods, which rely on external approximations that may misrepresent actual model computations.
Institutional affiliations: Peking University, Beijing Academy of Artificial Intelligence, Nanjing University of Science and Technology, Purdue University
The Salami Slicing Threat: Exploiting Cumulative Risks in LLM Systems
Salami Slicing
attacks exploit a gap in LLM defenses by chaining numerous individually low-risk inputs that cumulatively accumulate harmful intent, bypassing alignment thresholds without explicit triggers or heavy context-tuning. The authors’ automated framework achieves over 90% success rates on GPT-4o and Gemini while evading existing defenses. They propose a mitigation strategy that reduces attack success by 44.8%, though incomplete blocking rates suggest multi-turn accumulation remains a persistent vulnerability in production systems.
Institutional affiliations: Peking University, Sun Yat-sen University, Wuhan University, Tsinghua University, ByteDance, Singapore Management University
The National Development and Reform Commission (NDRC) ordered Meta to unwind its $2B acquisition of Manus
on April 27, ending a months-long security review that began in January. Cofounders Xiao Hong and Yichao Ji had been
barred from leaving mainland China in March
while NDRC’s review continued. Manus is a general-purpose autonomous AI agent built by China-based Butterfly Effect; the company had restructured to a Singapore corporate registration ahead of the deal. NDRC explicitly asserted jurisdiction over the Singapore-incorporated entity on the basis of where the underlying technology was actually created—Chinese-origin IP and talent are treated as domestic assets regardless of where the holding company is registered. It’s the
first time Beijing has blocked a major cross-border AI acquisition
, and the precedent that Chinese-origin AI assets housed abroad can be subject to NDRC-administered outbound technology controls may dissuade corporate restructuring abroad.
The human-like AI provisions go into effect in mid-July; we’ll be tracking what enforcement and the sandboxes end up looking like.
For more on how we select and track content, see our methodology
here
.
The China AI Bulletin is maintained by the Safe AI Forum (SAIF), a US 501(c)3 facilitating international cooperation on extreme AI risks. Views expressed represent individual authors’ perspectives, not official SAIF positions.
