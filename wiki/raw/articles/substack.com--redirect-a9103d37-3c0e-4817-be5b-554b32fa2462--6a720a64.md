---
title: "China AI Bulletin 9"
url: "https://substack.com/redirect/a9103d37-3c0e-4817-be5b-554b32fa2462?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-08-25T07:00:16.811865+00:00
source_date: 2026-08-24
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# China AI Bulletin 9

Source: https://substack.com/redirect/a9103d37-3c0e-4817-be5b-554b32fa2462?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Welcome to Issue 9 of the China AI Bulletin, the latest on AI governance, development, and safety in China. Today’s highlights: a
Qiushi
essay amplifies an AI-hegemony argument against possible US model controls, the Ministry of State Security and state media caution against foreign models, and Chinese labs published two biosecurity benchmarks.
Number(s) of the week:
116,000 & 55,000
—the numbers of new “humanoid-robot-related” and “generative-AI-related” enterprises, respectively, that the State Administration for Market Regulation (SAMR)
says were registered
in the first half of 2026.
This implies more than twice as many new humanoid-robot businesses as generative-AI businesses. SAMR  places both within its broad “eight emerging industries plus nine future industries” dataset but does not explain its classification method. The figures are registrations only, not an indicator of how many businesses are operating or profitable, so it remains to be seen what impact it has on the industry.
Domestic AI Governance:
The
Ministry of State Security
issued its second warning in two months about the risks of accessing foreign AI services. Though it was framed as an advisory about model autonomy and loss of control, it used the OpenAI–Hugging Face incident to tell users to avoid AI tools from unknown overseas sources and not to upload sensitive information to AI services. Its advisory appeared between
Economic Daily
and
People’s Daily
commentaries calling for more preventive, tiered model oversight.
Standards
: China released a mandatory L3/L4 automated-driving safety standard, five AI guiding technical documents, and a large batch of communications industry standards.
Note: there was a lot of standards activity this week; you’ll find an extensive discussion at the end of the Bulletin.
International AI Governance:
An essay in the CCP’s premier theoretical journal,
Qiushi
, by think tank director
Li Yan
presents US scrutiny of distillation and possible open-weight controls as part of a broader strategy of “AI hegemony.”
Eight more countries signed the agreement establishing the
World AI Cooperation Organization
, bringing the total to 37.
Export Controls & Economic Policy:
China answered recent US drone and forced-labor restrictions with controls on UAV exports to the US and a wider package affecting testing, certification, office equipment, and sanctioned US entities.
New exit-and-entry regulations also allow authorities to stop people implicated in export-control or technology-transfer violations from leaving China.
Beijing’s “token economy” policy connects subsidized AI inference to the emerging national compute network.
Models and Lab Publications:
Chinese labs released 202 papers on arXiv this fortnight.
DeepSeek-V4-Flash-0731
converts DeepSeek’s earlier preview into a 304-billion-parameter mixture-of-experts, MIT-licensed open-weight release and sharply improves the company’s reported agentic benchmark results.
MiniMax H3
opens the 768p core of its audio-video system while retaining hosted components for prompt interpretation and 2K output;
Alibaba’s Qwen3.8-Max
is now generally available.
Lab publications this cycle include papers on Alibaba’s
Qwen-CUA
computer-use agent and Tencent’s research on persistent backdoors in self-evolving agent skills.
Technical AI Safety Publications:
Chinese institutional authors released 93 safety-related papers on arXiv this fortnight.
The spotlight pairs two biosecurity benchmarks that look beyond model refusal.
BioDisclose
grades how much operational biomedical detail a response reveals, while
SPIKE-Bench
screens generated protein sequences for plausibility and predicted toxicity; both expose gaps in refusal-only evaluation, but neither demonstrates that a model output would work in a laboratory or cause biological harm.
China’s Ministry of State Security (MSS)
has used the
OpenAI–Hugging Face security incident
to caution the public about loss of control and the use of foreign models. In its August 5 advisory,
“Beware AI ‘Acting on Its Own’!”
,
the ministry says OpenAI’s models “went out of control and broke free” (失控出逃). The piece goes on to make security recommendations that are primarily concerned with security and privacy. The “AI Safety Usage Guide”
tells users not to use AI tools from “unknown overseas sources,”
enter personal data into AI systems, or spread deceptive AI-generated content. It separately told government and research personnel never to upload classified files, work information, or other sensitive material to Internet-connected AI services.
Chinese commentary
used the incident
to draw a contrast between foreign closed models and Chinese open-weight models after Hugging Face
said
it used a locally deployed version of Zhipu AI’s GLM-5.2 for forensic analysis after tripping commercial models’ safeguards. The MSS announcement also references this and criticizes closed “black-box” models for being less secure.
This is MSS’s second public warning about AI access in two months. Its June advisory,
“AI Relay Stations: Risks Require Precautions,”
cautioned against using the third-party gateways
many people have used to access Claude in China
. Together, the two advisories push against both untrusted routes to foreign AI services and the models themselves in the name of national security.
The MSS advisory came out in between two central state-media commentaries on model security. On August 4,
Economic Daily
argued
China’s existing model governance remains too focused on assigning responsibility after an incident.
It called for risk forecasting, dynamic monitoring, safety testing, and rules embedded throughout the model lifecycle. More concretely, it proposed classifying risk based on model capability, data sources, application, and user scale: low-risk models would require filing and routine monitoring, while high-risk models in public decision-making, finance, healthcare, and public-opinion contexts would face stricter admission reviews, algorithm certification, and real-time oversight.
On August 6,
People’s Daily
used
the same OpenAI incident to make the case for coordinating laws, technical standards, and risk monitoring.
It presented China’s content-labeling measures,
planned mandatory agent-safety standard
, and domestic lab safeguards as parts of that approach, then cited GLM-5.2’s role in the forensic investigation to argue that open models can strengthen safety. Xinhua republished both commentaries.
The August 4–6 sequence marks a step up from abstract calls for AI governance to more specific discussion of preventive, tiered model oversight.
Economic Daily
supplies a domestic regulatory blueprint; MSS treats access to foreign models as a national security question; and
People’s Daily
links safety governance to Chinese open source and international cooperation. While signed media commentaries and MSS guidance do not mean policy is changing, their convergence can signal governance priorities.
Politburo meeting discussed AI+ and AI governance.
At its
July 30 economic work meeting
, the Politburo called for deeper implementation of the “AI+” action, development of the
“intelligent economy” (智能经济)
—a policy term covering both the AI industry and AI-led transformation across existing sectors—and improvement of the AI governance system. This reiterates the
2026 Government Work Report’s
macroeconomic framing.
The National Development and Reform Commission (NDRC) reiterated plans for AI legislation.
At its
July 31 press conference
, NDRC Spokesperson Jiang Yi said China would accelerate the AI Law
legislative process and strengthen monitoring, early-warning, and emergency-response systems (which is becoming an increasingly common grouping of priorities). The announcement included no timetable.
AI entered two intellectual property workstreams.
At a
July 29 policy briefing
, the China National Intellectual Property Administration said it plans to revise the
Guidelines for AI-Related Invention Patent Applications (Trial)
and continue updating patent standards for areas, including embodied intelligence and brain-computer interfaces. Separately, the State Council’s
Fifteenth Five-Year Plan for Intellectual Property Protection and Utilization
names an “IP and AI mutual empowerment project”
among 12 special projects. Neither announcement supplied an AI-specific draft or implementation schedule.
Heilongjiang launched an AI+ agricultural pilot.
The
national application pilot base for crop cultivation
will provide testing and other services to producers, agricultural service companies, research institutions, and regulators.
Eight countries signed the
Agreement on Establishing the World AI Cooperation Organization
(WAICO) after the organization’s July 16 founding ceremony. Brunei, Togo, Iran, Sudan, and Vietnam signed on July 31 in a ceremony with Assistant Foreign Minister Liu Bin; Georgia and Tanzania signed separately that day, and Dominica signed on July 30. The later signatures expand WAICO beyond its
29 founding signatories
. It’s still unclear what concrete programs WAICO will implement to achieve its
stated goals
of promoting international cooperation and  global AI governance.
Li Yan, director of the Institute of Science, Technology, and Cybersecurity at the China Institutes of Contemporary International Relations, published a
Qiushi
essay
on August 1 titled “Working Together to Oppose Hegemonic Behavior in AI.”
He argues that US companies and policymakers are reframing model distillation from a common training technique into a national security and intellectual property issue to justify controls extending from chips to models and algorithms. Li rejects Anthropic’s allegation that DeepSeek, Moonshot, and MiniMax conducted industrial-scale distillation and dismisses the distinction between “normal” and “adversarial” distillation as technically unsound. The essay draws parallels to Anthropic’s settlement over allegations it downloaded seven million pirated books for training and quotes Elon Musk’s
response
to the distillation accusation. The quote seems from the tweet below, but the Chinese rendering
is closer to “How could someone steal something that Anthropic stole from human coders?” than “How dare they steal the stuff Anthropic stole from human coders??”
Li places the dispute in a broader historical claim: the US first establishes technological dominance, then portrays challengers as security threats and uses sanctions to preserve its position. Arguing US restrictions also face domestic opposition, the essay cites a
July 22 letter
signed by 179 Little Tech Association founders and member companies calling for continued US access to open models available worldwide and a
July 24 industry letter
from Nvidia, Microsoft, Meta, and others opposing premature restrictions on downloadable model weights. It then connects open weight access to WAICO and UN-centered governance, and closes with a line from President
Xi Jinping’s July 17 World AI Conference speech
: “AI development should not be a solo performance by one country, but a symphony of global cooperation.”
Publication in
Qiushi
does not mean Li’s stance is now official policy.
Still, it matters as signaling. The essay extends a framing the journal featured in
a July 1 article on “US digital hegemony,”
which described US control over chips, platforms, data, and technical standards as mutually reinforcing. Overall, it seems that
Qiushi
is being used to amplify this argument, which may filter into more of China’s global AI governance efforts.
An August 10
China-US Focus essay
by Fan Gaoyue, a former chief specialist at the People’s Liberation Army Academy of Military Science, extends the same securitization discussion  beyond distillation. Fan describes the US Gold Eagle cybersecurity initiative—
described by the White House
as
a voluntary public-private clearinghouse for finding and patching software vulnerabilities—as an instrument of technological dominance fragmenting the global AI ecosystem and presents open source and UN-centered governance as the better alternative. The essay shows that the “AI securitization” argument is spreading into military-affiliated expert commentary
.
Ministry of National Defense Spokesperson Jiang Bin
said at a July 30 briefing
that China “firmly opposes” broadening the concept of national security (
a jab at the US also seen in Xi’s WAIC speech
), politicizing or weaponizing AI, and starting a new AI arms race.
He also repeated the World AI Conference position that China would provide international public goods and support a “just and reasonable” global AI governance system. Back in March, the ministry had already
called for human primacy and safeguards against loss of control
in military AI.
Editor’s note: DeepSeek V4-Pro dropped right at press time. We’ll be covering it in the next issue!
DeepSeek
released
DeepSeek-V4-Flash-0731
on July 31, replacing its earlier V4-Flash preview with an official
304-billion-parameter, MIT-licensed open-weight model
, a mixture-of-experts design in which only a fraction of parameters activate per token, and a public-beta application programming interface (API). The architecture is unchanged from the preview and retains DeepSeek’s DSpark speculative-decoding module, but DeepSeek says further post-training substantially improved agentic performance. DeepSeek reports
82.7 on Terminal-Bench 2.1
, a benchmark of terminal-based agent tasks, compared with 61.8 for the Flash preview, 72.1 for the larger V4-Pro preview, and 85.0 for Claude Opus 4.8. The API update applies only to V4-Flash; DeepSeek did not update V4-Pro or the models in its web and mobile apps.
MiniMax
released
MiniMax H3
, a
33-billion-parameter dense video model
that processes text, images, video, and audio in one stream and generates four- to 15-second clips with native 32 kHz stereo audio, accepting up to nine reference images or three video clips. The open release is partial. MiniMax posted two downloadable checkpoints under its Community License: one generates a clip from its first and last frames, the other from multimodal references. Both run locally but top out at 768p (roughly standard-definition) video. Its advertised, higher-resolution 2K output needs two services that MiniMax runs only on its own servers: one rewrites a complex prompt into a form the model handles, and the other re-renders the 768p clip at 2K. MiniMax has therefore open-sourced the base generator, not the higher-resolution system it markets.
ByteDance
launched
Seedance 2.5
, a closed audio-video generation model that doubles single-pass output from
15 to
30 seconds
and supports multi-round extension. Users can provide up to 30 images, 10 videos, and 10 audio clips as references, then edit characters, actions, camera movements, or plot elements at specified timestamps. ByteDance is rolling it out through Jimeng AI and Doubao Pro and says API access will follow through BytePlus ModelArk. Unlike MiniMax H3, Seedance 2.5 has no downloadable weights.
Alibaba
made
Qwen3.8-Max
generally available through its API and Qwen products on August 3, replacing the July preview. Alibaba reports
2.4 trillion total parameters
and positions the model around autonomous coding and computer-based office work, including integration into QwenWork. The model is
available through Alibaba Cloud Model Studio
at 2 USD per million input tokens and 6 USD per million output tokens. On August 12, it ranked sixth on the
Artificial Analysis Intelligence Index
.
Alibaba said on August 3
that weights would follow the next week. On August 9, it published weights for
Qwen3.8-2.4T-A95B
, which it says Qwen3.8-Max was based on, but lacks many of its core features. Users on Hugging Face expressed
disappointment
, but it’s possible additional weights are forthcoming.
More releases this cycle:
ByteDance
released
SeedRealtime
, a closed full-duplex model that processes continuous audio, video, and text and decides when to respond without relying on a separate voice-activity-detection system. ByteDance has deployed it into its products but has not published weights or a model repository.
Shanghai AI Lab’s InternLM team
released
Intern-MemDec-4B
, a 4-billion-parameter biological-domain memory for the 397-billion-parameter Intern-S2-Preview backbone model. A token-level router combines the frozen backbone model’s predictions with the memory module each generation step. InternLM reports the module raises the backbone’s average score across 21 biology tasks from 56.92 to 60.32 while preserving a similar general-capability profile. It is an auxiliary component that currently works only with Intern-S2-Preview-397B, not a standalone chat model.
Frontier lab-affiliated authors released 202 papers on arXiv this fortnight. Highlights are below; a full list with summaries can be found
here
.
Labs include China’s BATX and “Six Little Tigers,” plus labs actively or recently releasing frontier-level models. Only papers where the first author or corresponding author has frontier lab affiliation are included.
Can Released LLM Vocabularies Support Token-Level Estimation of Hidden Corpora?
Released tokenizer vocabularies can reveal the composition of hidden pretraining corpora. The paper’s distribution-transfer method,
QGDE
, estimates token and corpus-category ratios with 3 percent relative error.
Qwen-CUA: Native Computer Use for (almost) Everything
Qwen-CUA
is a 397-billion-parameter agent that operates software through screenshots, keyboard inputs, and mouse controls. Alibaba trained it on 40,000 verifiable tasks using 100,000 virtual central processing units (vCPUs). The paper reports 86.2 percent on OSWorld-Verified and completion scores of 18.5/48.4 on OSWorld 2.0. A scaled 1-trillion-parameter variant raises those results to 87.6 percent and 21.2/53.3 and reduces adversarial attack success from 36.6 to 16.4 percent.
Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents
Qwen-UI-Agent
operates across mobile, desktop, web, and search environments. It combines graphical user interface (GUI) and command-line interface (CLI) actions, online reinforcement learning on trajectories longer than 100 turns, and an automated data flywheel. Alibaba reports 97.5 percent on AndroidDaily and 92.2 percent on MobileWorld-Real, alongside results competitive with frontier models on desktop and web tasks.
Right Answer, Wrong Method: Shortcut Hacking Misleads the Evaluation of LLM Reasoning on Frontier Science Benchmarks
The paper finds that models often reach correct answers on science benchmarks through invalid shortcuts, including numerical guessing.
Solution hacking
accounts for 8.2–44.1 percent of credited answers across the tested models. The rate rises from 2.2 to 37.4 percent on harder problems, indicating that answer-only evaluation can overestimate reasoning ability.
When Experience Becomes Instruction: Trajectory Poisoning in Self-Evolving Agent Skill Systems
A Multimodal Automatic Redteaming Evaluation Based on Atomic Jailbreak Strategy Decoupling and Combination
SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation
SkillLens
represents visual workflows as
Visual Skill Cards
, which contain applicability cues and verification signals. Retrieving these cards improves GUI action prediction by 11.6 percentage points on Multimodal-Mind2Web. The same representation supports
CardDistill
, which raises smaller-model performance by 12 percentage points without runtime retrieval.
Benchmarking the Residual: What Long-Horizon Evaluations Add Beyond Matched Short-Task Performance
The paper proposes the
horizon residual
, which compares actual long-task success with predictions based on matched short-stage performance. This separates ordinary error compounding from degradation that emerges over a trajectory, including context rot. The authors stress that meaningful comparisons require matched agent configurations and prespecified experimental choices.
SkillJack: Persistent Skill Backdoors in Self-Evolving Agents
SkillJack
turns malicious experiences into persistent agent skills. Safety detection falls from 98.5 percent for poisoned trajectories to 11.4 percent for the resulting skills, and the backdoor can survive deletion of the source records. The attack targets the agent’s learning pipeline rather than relying only on poisoned retrieval context.
When Self-Evolution Backfires: Pre-Commit Gating Against Skill Contamination in LLM Agents
The paper finds that a flawed skill can contaminate descendant skills after entering an agent’s context, making later removal insufficient.
Verifier-as-Gatekeeper
uses three specialized critics to screen skills before admission. The authors report 72 percent pass@1 with a skill pool one-fifth the size of the baseline and positive transfer across models and benchmarks.
There were
93 AI-safety-related papers published by Chinese researchers
this fortnight. Highlights are below; a full list with summaries is available
here
.
A safety evaluation usually records only whether a model refused a request or complied with it. These two Chinese benchmarks look at what the model actually discloses or generates when it responds.
BioDisclose
grades the operational detail in biomedical answers, including responses that refuse before leaking useful information.
SPIKE-Bench
goes a step further for protein-sequence requests, passing model outputs through computational tests of whether they resemble plausible, toxic proteins. Both find that a binary refusal score leaves out important information about the output—but neither establishes that an output could cause biological harm in practice.
BioDisclose
examines whether a deployed system releases biomedical information that could make a harmful task easier. The benchmark expands 24 expert-authored scenarios across six risk domains into 480 English, single-turn prompts using academic, historical, role-playing, and step-by-step framings. The risk domains are “Pathogen Biology, Human Gene Editing, Synthetic Biology, Animal Research, Human Biospecimens, and Safety.” “Safety” includes “unsafe laboratory practice and attempts to circumvent containment, decontamination, waste-handling, or institutional controls.” It grades responses from refusal (
L0
) through conceptual discussion (
L1
) and detailed, scenario-relevant information (
L2
) to a coherent end-to-end procedure (
L3
). Across five deployed systems, the authors report L2-or-higher rates from 9.2 percent to 64.0 percent. Framing requests as academic produces the highest average rate, at 43.2 percent. But complete L3 responses remain below 6 percent for every system, so the most common failure mode is partial operational detail rather than a ready-to-run protocol.
That distinction also limits what BioDisclose proves. Its score does not test whether the information is correct, experimentally feasible, sufficient for execution, or an uplift over what a user could find elsewhere.
Each of the five systems was tested as a live product: a model wrapped in the provider’s own safety filters and scaffolding, which providers keep updating. The scores therefore reflect those deployed products, not the underlying models in isolation.
The deterministic evaluator performs well against 250 human-labeled responses at the paper’s L2 threshold, but errors cluster around the line between sophisticated background information and details that materially advance a restricted objective.
SPIKE-Bench
uses 631 toxin-design prompts across seven functional categories to evaluate 32 language models. An individual response contributes to the paper’s
Functional Harmfulness Rate (FHR)
only if the model complies, produces a valid amino acid sequence, passes two protein-plausibility thresholds, and is classified as toxic by ToxinPred2. FHR ranges from 0 to 50.7 percent across models, with a median of 11.4 percent. The strongest predictor is the model’s ability to generate valid protein sequences, not its refusal rate. That does not mean refusal is useless: all five models that refused more than 90 percent of the original prompts had FHR at or below 1.1 percent. The narrower conclusion is that partial or inconsistent refusal does not distinguish models that lack biological capability from models that comply less often but generate stronger sequences when they do.
The authors stress that FHR is a
computational screening signal
, not a wet-lab success rate. Their filters ask whether a sequence falls within the statistical envelope of known toxins and receives a toxicity prediction; they do not establish that it could be synthesized, expressed, folded in a living system, bound to a target, delivered, or would actually be potent. To rule out that FHR merely reflects an over-eager toxicity classifier, the authors ran a control using random amino-acid sequences built to look like real toxins (same length and composition) but otherwise meaningless. The full FHR pipeline scored junk sequences at zero, even though the classifier alone labeled about 57 percent of it toxic—so FHR’s plausibility filters, not the classifier, are determining the score.
Its proposed input filter, BioSafe-Guard, detected 98.9 percent of the original prompts. But on a 50-prompt stress test in which another model preserved the requested biological function while removing conspicuous terms such as “toxin,” detection fell to 80 percent. This suggests the filter learns more than a simple keyword list but remains vulnerable to indirect descriptions of the same task. The test is small and uses machine-generated rewrites rather than prompts developed by human biosecurity experts, so it is only an initial robustness check.
Taken together with
last issue’s Intern-BioBreaker spotlight
, these papers cover three different layers of biosecurity evidence. BioDisclose measures the specificity of information a model releases; SPIKE-Bench adds domain tools to screen generated sequences; Intern-BioBreaker takes selected outputs into controlled wet-lab validation. They’re also a signal that more Chinese research organizations seem to be focusing more on bio-risk.
A²E: An End-to-End Agent Auditing Engine
A²E
pairs nine agent harnesses with 23 benchmarks through a common task protocol and records standardized execution traces. It evaluates efficiency, tool use, planning, and error recovery rather than measuring only whether an agent reaches the correct answer. No model-harness combination performs best across every task, so the paper is principally a capability-evaluation contribution rather than evidence that the audited systems are safer.
Institutional affiliations:
Shanghai Artificial Intelligence Laboratory.
SkillJack: Persistent Skill Backdoors in Self-Evolving Agents
SkillJack
exploits the conversion of past interactions into reusable skills. Malicious behavior persists after the source data is deleted because skill extraction obscures malicious intent, promotes a temporary experience into a durable capability, and separates the backdoor from its source record. Across two systems, safety detection falls from 98.5 percent for poisoned trajectories to 11.4 percent for extracted skills; attack-success rates reach 56–89 percent, and 80 percent of attacks persist after source deletion.
Institutional affiliations:
Tencent Zhuque Lab.
Breadcrumbing Search Agents
Authority-Chain Hijack
coordinates prompt injections across successive searches and sources, allowing an attacker to build a false but internally corroborating evidence chain. The attack reaches 55.9 percent success on SafeSearch. The paper’s trace-guided strategy evolution raises success to 71.4 percent on held-out evaluations.
Institutional affiliations:
University of Science and Technology of China and Nanyang Technological University.
REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems
REDAgentBench
derives attacks from explicit safety constraints, runs them in sandboxed environments, and verifies harmful outcomes from service logs and state changes. Across 1,661 cases, agents sometimes acknowledge a safety constraint and violate it during execution. A policy reminder reduces confirmed violations by more than 70 percentage points in matched replay.
Institutional affiliations:
Fudan University, Hong Kong University of Science and Technology, Qwen DianJin Team at Alibaba Cloud Computing, and Soochow University.
COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution
Institutional affiliations:
Ant Group.
AgentS4D: Benchmarking Runtime Risks Across the Execution Lifecycle of LLM-Based Workspace Agents
AgentS4D
evaluates workspace agents across six risk-entry sources, six induction strategies, nine target harms, and seven execution checkpoints. In 6,560 runs covering 20 agent configurations, 68 percent trigger unsafe behavior and 66.22 percent are both unsafe and task-complete. Task completion therefore cannot establish runtime safety.
Institutional affiliations:
Institute of Cyberspace Security, Binjiang Institute of Artificial Intelligence, and College of Information Engineering at Zhejiang University of Technology.
ProbGuard: Calibrated Safety Risk Estimation from LLM Output Distributions
ProbGuard
estimates the probability of an unsafe completion from the model’s output distribution after the first ten decoding steps. The paper reports reductions of 79.6 percent in average Brier score and 71.9 percent in expected calibration error relative to the strongest baseline, while limiting attack success to at most 1 percent across six jailbreak attacks.
Institutional affiliations:
Zhejiang University, Hangzhou High-Tech Zone (Binjiang) Institute of Blockchain and Data Security, University of Electronic Science and Technology of China, Anhui University, King Abdullah University of Science and Technology, and Sun Yat-sen University.
SHE: Trajectory-Driven Safety Harness Evolution for LLM Agents
Safety Harness Evolution (SHE)
treats prompts, rules, safety memory, and tool permissions as components that can be updated from failure trajectories. On Agent-SafetyBench, SHE reduces unsafe-action rates 3.1 times more than static baselines while maintaining utility. The updated harness also transfers across agent models without retraining them.
Institutional affiliations:
Shanghai Artificial Intelligence Laboratory, Fudan University, Shanghai Jiao Tong University, and Hong Kong University of Science and Technology.
Once Poisoned, Arbitrarily Controlled: A Programmable Backdoor in VLMs
The paper’s
programmable backdoor
separates target selection from the poisoning phase. After one poisoning phase, an attacker can generate a visual trigger for a previously unseen target caption and steer the model toward it at inference time. The method preserves clean-model utility in the authors’ tests and remains effective against several established defenses.
Institutional affiliations:
Key Laboratory of System Software at the Chinese Academy of Sciences, Institute of Software at the Chinese Academy of Sciences, University of Chinese Academy of Sciences, University of Macau, and Institute of AI for Industries at the Chinese Academy of Sciences.
Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs
The paper derives an exact lower bound on attacker assistance when safeguards rely on information that an attacker can copy, such as a request or conversation history. Under this setup, useful capability, reliable safety, and open access cannot all coexist. Hard-to-copy credentials can lower the bound, shifting part of the safety problem from prompt filtering to verification of users and downstream use.
Institutional affiliations:
University of Science and Technology of China, Hefei AiDA Lab, and Zhejiang Wanli University.
On August 5, the Ministry of Commerce (MOFCOM) placed exports of controlled unmanned aerial vehicles (UAVs), critical components, and related technology to the US under
strict case-by-case review
.
The Associated Press reported
that MOFCOM presented this package of measures as a necessary response to recent US restrictions, including the Federal Communications Commission (FCC)’s restrictions on foreign-made drones and the Department of Homeland Security’s addition of 43 Chinese companies to its forced-labor entity list. The individual notices show how those triggers map onto the package: the action against Compliance Testing LLC explicitly cites FCC measures,
while the action against six US entities explicitly cites US forced-labor sanctions.
The UAV measure is the clearest direct response, although the two measures largely overlap. Trivium notes that it’s unusual for China to directly name the measures it’s responding to and interprets it as a warning calibrated to preserve the Busan trade deal.
China announced several other tech-trade measures the same day, but their legal bases and stated targets differ. MOFCOM
barred Chinese organizations and individuals from transactions or cooperation with Compliance Testing LLC
, saying the company had supported FCC measures against China, and
opened a national security investigation
into imported printers, copiers, and related office equipment that use foreign-developed or maintained driver and embedded software.
SAMR also said US-based organizations could
no longer conduct follow-up factory inspections
on behalf of Chinese bodies for China Compulsory Certification. US manufacturers can still use inspectors based elsewhere, but the measure adds friction to the product-certification infrastructure around electronics trade. Separately, MOFCOM
prohibited transactions and cooperation with six US entities
over their support for US Xinjiang forced-labor sanctions.
Overall, these measures are an expansion of the export control contest beyond chips and models into autonomous hardware and the systems that certify and operate it.
Another security action seems to be part of this response; on August 6, China’s Cybersecurity Review Office
opened a review of cybersecurity company Palo Alto Networks products sold in China
.
Geopolitechs
interprets it
as part of the same cross-departmental, “portfolio-style” response as the August 5 measures, but the official review notice does not itself make that connection. The action also follows
January reporting that Chinese authorities had told domestic companies to stop using cybersecurity software from several US and Israeli suppliers
, including Palo Alto Networks, suggesting it formalizes a longer-running security concern.
An August 9
State Council retrospective on the national computing-power network
says more than 60 percent of China’s compute resources are now under unified monitoring through the National Integrated Computing-Power Network Monitoring, Dispatching, Testing, and Validation Platform,
a
National Data Administration (NDA) system built by the Chinese Academy of Sciences' Institute of Computing Technology
. It also says China has built its first domestic cluster with 100,000 accelerators and repeats MIIT’s end-of-June estimate that China has 2,185 EFLOPS of intelligent compute capacity, up 177 percent year-over-year. The 60 percent figure measures monitoring coverage; it does not mean the central government owns that capacity or can freely allocate all of it. The figures mark progress in the effort to consolidate provincial infrastructure into a national network.
A second national platform runs alongside it. The NDA’s platform seems to be for monitoring and dispatch; it centrally tracks and schedules compute across the integrated national network. The
China Computing Power Platform
, run by MIIT and the China Academy of Information and Communications Technology (CAICT), is more market-facing. It matches compute buyers with sellers and lets users aggregate, purchase, and instantly provision capacity, alongside industry-ecosystem services like an alliance of compute firms and zones for smaller enterprises;
its Guizhou branch
, for example, collects standardized data from telecom operators, Huawei Cloud, and other data centers. Both have the same “single ledger” ambition and both do some monitoring, but they seem to be complementary rather than competing. The NDA runs the centralized monitoring/dispatch based on its data-infrastructure and East-Data-West-Compute (东数西算) remit, while MIIT and CAICT run what is effectively a compute marketplace out of MIIT’s telecom-and-industry remit.
Two days earlier, Beijing Economic-Technological Development Area published what
Science and Technology Daily
called
Beijing’s first special policy for the “token economy.”
In May, the National Data Administration
said it would develop the token economy
around high-quality industry datasets and the national integrated computing-power network.
In the framework, the network supplies and routes the underlying compute, while the “token economy” is the measurement and commercial layer that turns model inference into a metered, distributable, and billable service.
The Beijing policy applies that idea locally through “token factories,” unified model access and settlement, token vouchers, and consumption subsidies. A
“token factory”
is Beijing’s term for an industrial-scale AI-serving facility that combines compute, models, data, and software services and measures its output in tokens, rather than merely renting access to accelerator cards.
The district was already spending
100 million RMB/14 million USD a year on each of three voucher programs
for compute, models, and data. The new policy seemingly brings those existing subsidies together under a broader plan for producing, distributing, and consuming tokens.
China’s new
exit-and-entry regulations
, which take effect September 15, allow MOFCOM and other competent authorities to stop a Chinese citizen from leaving the country if the person has “violated regulations concerning export controls or technology import and export management, potentially endangering national industrial or technological security.”
A
Ministry of Justice explainer
says the rule is a response to increased incidence of Chinese citizens being “deceived” into leaving the country or illegally departing to transfer technology to foreign actors. It’s unclear what these restrictions will look like in practice or how broadly they’ll be interpreted.
The Ministry of Industry and Information Technology (MIIT)
published GB 44721—2026
, 《智能网联汽车 自动驾驶系统安全要求》 (
Intelligent Connected Vehicles—Safety Requirements for Automated Driving Systems
), on July 30. The mandatory national standard covers Level 3 and Level 4 systems in passenger and commercial vehicles, excluding automated parking. It sets requirements for lifecycle management, system safety, driver takeover, and confirmation testing, which will take effect on July 1, 2027.
This creates binding safety requirements and pairs with a lower-tier mandatory standard issued weeks earlier. In early July, SAMR and SAC published
GB 47955—2026
, 《智能网联汽车 组合驾驶辅助系统安全要求》 (
Safety Requirements for Combination Driving Assistance Systems
), which covers L2-and-below combination driving assistance and takes effect January 1, 2027. Together the two set mandatory safety requirements spanning assisted driving through high automation. Mandatory standards are
more common
for vehicle safety than for AI itself; China’s model, agent, and platform standards are almost all recommended (GB/T) or guiding (GB/Z). (Exceptions include the 2025 generated content labeling standard
GB 45438—2025
and the
forthcoming mandatory AI agent safety standard
.)
The Standardization Administration of China (SAC)
published GB/T 47941.1—2026
, 《人工智能医疗器械 质量要求和评价 第1部分：术语》 (
Artificial Intelligence Medical Devices—Quality Requirements and Evaluation—Part 1: Terminology
), on July 30. The recommended national standard defines the vocabulary for evaluating the quality of AI medical devices and will take effect on August 1, 2027. This is the first part of a planned series.
The SAC
published five AI guiding technical documents
on July 30. The batch covers industrial agents, large-model procurement and deployment, industrial large-model requirements, and AI-assisted legal work
(see footnote for links).
These are
GB/Z guiding technical documents
, which offer state-issued reference architectures and implementation guidance but do not create mandatory requirements. GB/Z 195 extends China’s agent-standardization work from the
seven-part agent-interconnection series
published in May into the architecture of industrial-agent systems.
The Ministry of Industry and Information Technology (MIIT)
publicized
eight recommended communications-industry standards on August 3; they were originally approved July 24.
The batch standardizes the data and compute infrastructure around large models and also defines who counts as an AI enterprise. YD/T standards are recommended industry standards, not mandatory national standards.
The SAMR’s
July industry-standard filing report
, posted August 1, lists 674 standards, including
22 directly or closely related to AI and intelligent computing
. They cover model management and enterprise AI maturity, large-model benchmarking and operations, model-as-a-service platforms, agents, edge AI, generated image detection, multimodal models, and intelligent compute clusters. The group also includes YD/T 7073, which defines AI safety-governance terminology.
From July 30 through August 11, the National Technical Committee on Cybersecurity Standardization (TC260) issued
16 calls for drafters
covering model testing, AI safety guardrails, agent data processing, personal-information protection, generated-content detection, open-source models, embodied AI, edge models, training and inference frameworks, and intelligent-compute cloud services.
See footnote for links.
Fourteen of the 16 subjects also appear in a
SAC consultation
on whether to establish them as recommended national-standard projects, with comments due September 3. The anthropomorphic-interaction and embodied-AI projects remain at the drafter-recruitment stage.
TC260’s
July monthly report
, published August 12, identifies two AI-relevant July milestones we haven’t previously covered. On July 15, TC260 opened public comment on
《网络安全技术 人工智能应用安全分类分级方法》
(
Cybersecurity Technology—Methods for Classifying and Grading AI Application Security
), with comments due September 13. On July 16, experts reviewed
《网络安全技术 人工智能安全能力成熟度评估方法》
(
Cybersecurity Technology—AI Security Capability Maturity Assessment Methods
). The first is a public draft; the second remains at expert review. The report’s other major AI items were covered in
Issue 8
.
Five recommended national standards advanced in SAC’s pipeline. None have been published yet
(see footnote for links)
.
Drafters of the two large-model standards include the China Electronics Standardization Institute, Huawei Cloud, Zhejiang University, Beijing Academy of Artificial Intelligence, Shanghai AI Lab, Ant Group, Zhipu AI, SenseTime, Alibaba Cloud, and Baidu.
The SAC’s
seventh recommended national-standard project plan for 2026
, dated July 30 and posted August 4, includes two AI projects among 397 total—a
specification for intelligent compute data processing units
, and a
safety classification system for AI-generated content
.
These will be drafted over the next 15 months.
The SAC also registered 12 early-stage guiding technical-document projects. All remain at the drafting stage
(see footnote for links)
.
These registrations identify future work but contain no adopted requirements. The
“-Z-469” identifiers are project registration numbers, not published GB/Z standard numbers.
DeepSeek V4-Pro dropped right at press time. We’ll be covering it in the next issue!
For more on how we select and track content, see our methodology
here
.
The China AI Bulletin is maintained by the Safe AI Forum (SAIF), a US 501(c)3 facilitating international cooperation on extreme AI risks. Views expressed represent individual authors’ perspectives, not official SAIF positions.
The China AI Bulletin is copy-edited and fact-checked by Kacie Yearout, Pivotal fellow and former diplomat.
