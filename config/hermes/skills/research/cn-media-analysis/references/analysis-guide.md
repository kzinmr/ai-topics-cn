# Chinese AI Media Analysis Reference

Load this reference only for ad hoc long-form reports. Cron jobs should normally rely on the compact `SKILL.md` checklist.

## Cross-Source Comparison

When several sources cover the same durable topic, compare them by:

- developer practicality: cost, API stability, deployment friction, integration effort
- implementation evidence: code examples, benchmarks, reproducibility, failure modes
- business context: product positioning, financing, partnerships, market structure
- technical argument: model behavior, architecture, evaluation method, research lineage
- policy and ecosystem context: compliance, domestic substitution, hardware/software ecosystem changes

Avoid claiming a propagation path unless timestamps and sources support it.

## Stable Trend Signals

Prefer signals that remain useful after the current news cycle:

- a new or materially changed model, product, dataset, framework, protocol, or developer tool
- adoption by a significant company, platform, research group, or open-source project
- a pricing, licensing, compliance, or deployment change with durable impact
- repeated developer reports that point to a persistent capability or reliability issue
- source disagreement that reveals a meaningful gap between marketing, implementation, and user experience

Treat leaderboard movement, launch-day reactions, social chatter, and unsourced predictions as low-durability unless the task explicitly asks for them.

## Source Handling

- V2EX: useful for practitioner sentiment and concrete complaints; summarize the pattern rather than overquoting individual comments.
- Juejin: useful for implementation detail; verify article date and avoid treating resurfaced old posts as new.
- 36kr: useful for business context; name the specific media or author when available.
- Zhihu: useful when the answer has clear expertise or evidence; separate expert explanations from generic answers.
- WeChat public accounts: useful for long-form reporting; always name the account because quality varies.
- Newsletters: useful for discovery and deduplication; verify important claims against stronger sources when possible.

## Wiki Action Heuristics

Recommend a wiki update when an item:

- introduces a new durable entity or materially changes a known entity
- adds a stable relationship between companies, models, products, papers, or regulations
- clarifies capability, limitation, pricing/licensing, availability, or deployment status
- provides source-backed context that helps future readers interpret the topic

Skip or park items that are only promotional, speculative, duplicate, too thinly sourced, or tied to short-lived chatter.
