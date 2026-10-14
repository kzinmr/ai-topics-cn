---
title: "Can China close the high-end AI data gap?"
url: "https://substack.com/redirect/46813e09-4292-48bd-a4e7-69d44f5af0d4?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-10-13T07:00:16.020578+00:00
source_date: 2026-10-12
tags: [newsletter, auto-ingested]
source_lang: zh-CN
---

# Can China close the high-end AI data gap?

Source: https://substack.com/redirect/46813e09-4292-48bd-a4e7-69d44f5af0d4?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

American firms are supplying several Chinese AI labs with the high-quality data they need for post-training their models, Forbes
revealed
recently. In the wake of the exposé, several U.S.
industry
and
policy
leaders questioned whether these sales should be happening. Meanwhile, the Chinese government isn’t exactly enthused about domestic companies relying on data from its biggest rival. At a recent press conference, an official from the Internet regulator, the Cyberspace Administration of China, named “technological hegemony” as the fifth major category of AI security risk, and
remarked
that “certain countries” are “taking advantage of their dominance in training-data resources to promote particular values through AI systems…”
So what options do Chinese labs have, if any, to source similar data from domestic providers? And how quickly could domestic supply improve if access to American training data was cut off?
First, let’s clarify the type of data we’re talking about. This post-training data is structured, sophisticated data that helps AI models learn how to perform complex reasoning and long-horizon agentic tasks. It comes in three major forms:
Demonstrations:
Experts produce ideal solutions—a reasoning problem solved step by step, or a complete trajectory showing steps to operate a browser or terminal—which the model learns to imitate through Supervised Fine-Tuning (SFT).
Judgment or preference data:
Experts score or rank the model’s attempts to perform a task. Those judgments are used to train a model to produce outputs more like those preferred by the experts, using methods such as Direct Preference Optimization (DPO) or Reinforcement Learning with Human Feedback (RLHF).
Tasks and verifiers:
The frontier for agentic tasks. The supplier builds a realistic simulated environment—an inbox, a codebase, an enterprise software stack—plus tasks and a verifier that checks whether the agent completed them. The model attempts each task many times, and the verifier’s scores are fed back as rewards, reinforcing whatever worked. When the check is programmatic (such as “Did the code pass the tests?”), this is called reinforcement learning with verifiable rewards (RLVR). For fuzzier tasks, experts write scoring rubrics and an AI judge applies them at scale.
The experts producing this data include programmers, doctors, lawyers, accountants, and cybersecurity specialists. Surge AI, one of the major American vendors reportedly serving Chinese companies, claims access to more than 200,000 PhDs, 500 disciplines and 80 languages. Public sector data and data for training autonomous vehicles and embodied AI, areas in which China is relatively strong, are outside the scope of this piece.
I found three prominent Chinese post-training data providers for which relatively detailed product and financial information is available. The first is ByAI Data (Benyuan Zhishu or 本原智数 in Chinese), founded in Shanghai in 2015. C.banner, a footwear company trying to diversify, acquired a controlling stake in it this year. ByAI’s
offerings
include expert-produced data in maths, coding, law, and other technical fields; agent trajectory data; enterprise workflow data; virtual environment reconstruction data for world models; and suites for evaluating a model’s Skill selection and execution in Claude Code. Customers reportedly include leading Chinese foundation model developers, internet platforms, game publishers and embodied AI companies; Tencent, Ant Group, Baidu, Alibaba Cloud, and Meituan are among the partners listed on the ByAI website. Its Hong Kong Exchange filing claims that it “acts as the sole data supplier to certain customers across multiple high-value data categories”. Its 2025 revenue was ~$21.8 million, up 6.6% from 2024, and its post-tax profit was ~$1.6 million.
Then there’s Speechocean (海天瑞声), founded in Beijing in 2005 and listed on Shanghai’s STAR market. As the name suggests, Speechocean began with speech and multilingual data, and these remain core strengths. But it also
offers
expert data in fields such as law, medicine, coding, and finance, as well as chain-of-thought reasoning and programming data, and human-preference data for RLHF. Its
H1 2026 report
described an under-construction Graphical User Interface agent recording system that would capture screens, user actions, and replayable trajectories across devices. Its 2025 revenue was around $52m, up 59% from 2024, of which around 42% came from overseas. It claims access to 50,000 experts and 1,200 clients;
named customers
include Alibaba, Tencent, and Baidu.
Another publicly traded competitor is Beijing-based Datatang (数据堂), established in 2010. Datatang made ~$50m in revenue in 2025 (up 49% year-on-year) and ~$8m in post-tax profit. The company’s large model service
advertises
RLHF annotation; expert data in medicine, finance, education, law, and creative writing; and red-teaming and safety evaluation, among other post-training and pretraining data services. In August 2025, the COO
said
the company’s work was shifting from labeling outputs to “teaching AI to think,” including producing chain-of-thought and other reasoning data. But I couldn’t find evidence of it offering tool-use trajectories or enterprise software simulations.
In summary, Chinese suppliers already cover much of the standard post-training menu. The largest gaps with leading U.S. competitors are in the production of long-horizon agent trajectories, RL environments and verifiers, and realistic enterprise software tasks. And the difference in product offerings is reflected in the numbers. The combined 2025 revenue of ByAI, Speechocean, and Datatang is around a quarter of the ~$500m that China’s top six AI labs have been paying to American data companies, according to Forbes’ unverified estimate.
Table comparing capabilities of U.S. provider Surge AI with the three Chinese companies studied, based on their websites. “✓” = the company explicitly advertises the service or reports delivery of it (this is not a comment on quality or scale). “△” means partial, under development or weakly documented.
ByAI CTO Lin Zhenya gave
his diagnosis
of a major reason for the capability gap in March 2026. Lin argued that while U.S. labs are willing to outsource a complete data problem to specialist vendors, internal data teams at Chinese labs retain considerable authority, while external suppliers are generally limited to providing labor for data labeling. Because Chinese labs keep the core data expertise, suppliers accumulate less reusable process knowledge. Furthermore, their inability to develop differentiated capabilities has sustained intense price competition and a fragmented market, preventing suppliers from achieving the scale and customer relationships of U.S. leaders such as Scale AI or Surge AI. Lin estimates that China’s three largest suppliers control 20-30% of the market in China, compared to 70-80% for the top three abroad. It seems there’s a chicken-and-egg problem: without empowerment, data suppliers can’t develop vital capabilities, and without those capabilities, they can’t win customer trust or grow their businesses.
Another explanation is that distillation of leading Western models has reduced the incentive for Chinese model developers to invest in domestic data pipelines. Anthropic’s recent
report
details distillation of its models from seven Chinese companies, which in some cases fed prompts from their own users into Claude. The report also notes that Chinese model developers can buy transcripts of user exchanges with Western frontier models from third-party resellers. These resellers include the operators of proxy services, known as transfer stations, allowing Chinese users access to Western models. This kind of data acquisition shortcut may have limited demand for suppliers building their own sources of data. It’s unclear how much longer the distillation route will be available, however. Western providers are strengthening technical measures to identify and prevent it, and the Chinese government will likely crack down on companies feeding sensitive Chinese user data to American model providers in contravention of data privacy and national security laws.
Government sources acknowledge weak market demand as a constraint while also pointing to supply-side issues in the sector. A 2025
commentary
by the head of China Center for Information Industry Development (a research institute subordinate to the Ministry of Industry and IT), published by the National Data Administration (NDA), encouraged companies to outsource more data-labeling work, while simultaneously calling out weak standardization (for example, of annotation procedures and quality assessment), insufficient intelligent labeling technology (which increases reliance on human workers), and shortages of high-quality talent. An
expert commentary
published alongside the NDA’s
high-quality industry dataset plan
in June 2026 further highlighted large quantities of valuable data remaining unused inside institutions and companies.
The government wants to resolve these problems and shift the data industry from low-value to high-value work. The NDA’s aforementioned 2026 plan calls for institutions to build datasets for complex task planning, long-horizon reasoning, and human-computer interaction. Other measures include developing national standards and combining public and industry data, and encouraging local funds to provide capital support. And local governments are indeed trying to incentivize the growth of data enterprises in their areas. Zhongguancun Science City, in Beijing’s Haidian district, issued a policy
offering
up to RMB 100 million—roughly $14 million—for construction of a “high-end AI data labeling demonstration base.”
It seems possible for the Chinese data ecosystem to level up, especially if access to Western data is cut off. China graduated nearly 113,000 PhD students in 2025, so talent won’t be the bottleneck. It’s true this talent needs to be organized effectively. Building and managing a sophisticated production system that can write rubrics and verifiers that correlate with real performance, weed out plagiarism and secret use of models by human workers, and create interactive, realistic reinforcement learning environments is not easy. But organizational problems have not prevented Chinese companies from getting very close to the frontier of LLM development. It seems within reach for them to do the same in the data industry.
One particular indicator to watch is the progress of a new cohort of
young startups
aiming to fill the gaps in Chinese incumbents’ portfolios. Take Beijing-based startup Yuanrang Intelligent Technology (北京原壤智能科技), founded in 2025. Its public face is a set of benchmarks for agentic professional work published under the brand Humanlaya, alongside an “enterprise data partnerships” program inviting companies to turn their anonymized internal workflows into revenue, and an expert recruitment platform called
Talents-AI
. According to a September
post
by an investor at CDH Investments, which led Yuanrang’s Pre-A round, it is already valued in the hundreds of millions of dollars, with over 100,000 registered experts and most major Chinese model developers as clients. The CDH post frames the investment explicitly as a bet that China can produce “its own Surge and Mercor”.
Meanwhile,
Human Intelligence
(智能知识), whose core team came from ByteDance’s Seed (foundation model) division, has raised two rounds from prominent funds including 5Y Capital and MiraclePlus. It advertises agent task data for terminal and tool-calling workflows alongside an expert recruitment network called
Meet Chances
(一面千识). Neither of these companies has public revenue figures yet, so it’s hard to judge how well they’re doing beyond their slick marketing.
Screenshot from the Human Intelligence
homepage
. They state their mission is “to cultivate an AGI with a genuine soul”, and they frame data quality as the key to building “an AGI that benefits the world, cures disease, and pursues truth”, rather than “a utilitarian system chasing vibe revenue, Arena click-throughs and benchmark scores”.
While it’ll be relatively easy for such startups to build data pertaining to universal knowledge (such as maths or science) and Chinese contexts, Western providers are likely to retain an advantage in two main areas. The first is fields that rely on institutional and cultural knowledge, such as U.S. law, management, or healthcare expertise and norms. The second is workflows specific to U.S. workplace software and organizational systems, such as completing tasks across Slack, Jira, Salesforce, and email. It’ll be hard for Chinese companies to gain the necessary trust from Western enterprise partners that would allow them to accumulate exposure to Western companies’ task distributions and internal environments.
Any attempt at export controls on U.S. data would face at least a few challenges. The first is that they would likely spur more investment and progress in indigenization of the supply chain in China; if Chinese customers weren’t willing to trust domestic suppliers with more control over data projects in the past, they might have to if they have nowhere else to get high-quality data from. We’ve seen that the semiconductor export controls have spurred closer collaboration between Chinese AI companies and domestic compute suppliers, and the data industry seems a much easier nut to crack than semiconductors given the lower supply chain complexity involved. The early traction of the new startups discussed above supports that assessment.
The second challenge is scope. Defining high-quality data for the purpose of restrictions might not be easy. Some might propose basing restrictions on customers: if you supply leading U.S. AI labs or the Department of War, then you shouldn’t reuse the know-how built up serving these high-end U.S. customers to sell to Chinese AI labs. But this might create perverse incentives to, for example, avoid DoW contracts and focus on higher-value, quicker-to-secure Chinese ones.
A final, less significant factor is the risk of reciprocal restrictions. U.S. companies use data from Chinese providers: Speechocean lists Meta and Microsoft among its customers and generated RMB 158 million (~$22m) overseas in 2025; Datatang’s disclosed customer materials have included Microsoft and Intel. The scale and scope of these transactions likely don’t match Chinese procurement of U.S. data, but it’s necessary to consider the implications for U.S. customers if these purchases were no longer viable.
In conclusion, I don’t think the U.S. providers possess a permanent, across-the-board moat when it comes to high-quality post-training data. Established Chinese providers and new startups are strengthening their offerings for agent training. Distillation and a reluctance to outsource complete data problems to emerging domestic suppliers may have slowed the growth of the Chinese data ecosystem so far. But the growing controversy around both distillation and U.S. data providers selling to China strengthens incentives to develop domestic alternatives. Restrictions on U.S. data sales would hinder the training of Chinese agents for Western enterprise environments, but are unlikely to create a durable constraint on Chinese AI progress more broadly—and may even prove counterproductive.
Share
