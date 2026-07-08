# Channel Talk Research Phase

Date: 2026-07-08

## Problem Hypothesis

Channel Talk customers adopting ALF need a pre-launch planning workflow that turns scattered FAQ, policy, macro, and inquiry text into a rollout brief. The real problem is not building a new chatbot. It is deciding what knowledge is rollout-ready, what scenarios are safe to automate, what requires a later workflow or API handoff, and what must remain with a human operator.

## Target User

Primary user: Channel Talk AX Consultant preparing a customer ALF rollout.

Customer-side stakeholder: an e-commerce CX operations manager who provides support-policy material, clarifies missing rules, and approves exception handling.

Why this role fit is stronger:

- the work is rollout design and customer enablement
- the work requires interpreting support policy and structuring ALF-ready knowledge
- the work requires defining response scenarios and human handoff boundaries
- the work does not require product-roadmap ownership or model-building ownership

## Hiring-Site Role-Fit Rationale

Public hiring-site context checked on 2026-07-08:

- Channel Talk AX Consultant is supported by a public Korean careers posting: <https://channel.io/kr/careers/e588e8b8-c1d1-43d7-b8b0-3ae9cb639d74>
- the posting duties align with analyzing customer FAQ, product information, and operation-policy data into ALF Knowledge; building customer response scenarios; customer onboarding and value proof; workflow/API design; CX insight discovery; and engineering collaboration
- this supports `Channel Talk AX Consultant` as the primary public role fit for the workflow

Why the role fit is strong:

- the product docs remain the main proof of the ALF problem: shaping knowledge, rules, task boundaries, and review flows before launch
- the homepage describes AI support in terms of trusted rules, structured knowledge, and actionable support, which matches implementation planning rather than product strategy or model engineering
- the plugin's outputs line up with customer onboarding and rollout preparation, which is a better fit for an AX consultant persona than a PM or Applied AI Engineer persona

Why AX Consultant is stronger than PM:

- PM work would naturally expand into prioritization, roadmap sequencing, feature requirements, and internal product tradeoffs
- this plugin does not choose Channel Talk product direction; it prepares one customer's rollout using public docs plus pasted customer material
- the hiring-site evidence points to customer ALF setup and onboarding rather than internal product-management ownership

Why AX Consultant is stronger than Applied AI Engineer:

- Applied AI Engineer work would naturally move toward retrieval design, evaluation metrics, prompt experiments, model comparisons, or integration implementation
- this plugin does none of that; it stays as a skill-only planning workflow with no RAG benchmark, no model-evaluation harness, and no API implementation
- the hiring-site and product evidence require technical literacy, workflow/API planning, and AI rollout judgment, not model training, RAG architecture, or API coding

## Video Context

- Title: `"AI 툴을 많이 쓰는 게 중요한 게 아닙니다" 채널톡이 바라보는 AI 시대 인재 | AX 인재전쟁 4화 채널톡`
- URL: <https://www.youtube.com/watch?v=5iRf37Z8Wd4>
- Use in this project: supporting context only

Relevant context to reflect, but not use as sole proof:

- AX should start from an essential business problem
- AI agent work should explain why the chosen tool and workflow fit that problem
- talent density matters because a small team should solve larger customer-facing work with better leverage

That framing supports this plugin's posture: explain why a specific ALF rollout plan is the right answer to a real customer support problem.

## Evidence Map

| Claim | Source | Reliability | Plugin implication |
| --- | --- | --- | --- |
| Channel Talk positions AI around reducing repetitive inquiries so teams can focus on important work. | Channel Talk User Guide, AI category: <https://docs.channel.io/help/en/categories/AI-d5340000> | Official product documentation | The plugin should focus on repeated support scenarios and rollout preparation, not generic support advice. |
| FAQs can be registered ahead of time, ALF can answer from FAQ content, and FAQ opportunities can be suggested from conversation patterns. | Channel Talk FAQ guide: <https://docs.channel.io/help/en/articles/FAQ--db21218c> | Official product documentation | The plugin should surface FAQ gaps from repeated scenarios and missing safe answers. |
| ALF Rules are scenario-driven instructions using inquiry context, customer information, tagging, and routing. | Channel Talk Rule guide: <https://docs.channel.io/help/en/articles/Rule-b43e19a1> | Official product documentation | The plugin should translate source text into response scenarios and exception boundaries. |
| ALF Knowledge can rely on websites, FAQs, documents, Excel, and PDFs with scoped references and filters. | Channel Talk Knowledge guide: <https://docs.channel.io/help/en/articles/Knowledge--803f6ac9> | Official product documentation | The plugin should assess knowledge readiness before recommending automation. |
| ALF Tasks can support order cancellation, address changes, exchange, return, refund, stock checks, and other operational flows. | Channel Talk Task guide: <https://docs.channel.io/help/en/articles/Task--2a16be8b> | Official product documentation | The plugin should distinguish answer-only scenarios from workflow or API handoff candidates. |
| Channel Talk presents accurate AI support as the combination of trusted rules, structured knowledge, and actions that let AI get work done. | Channel Talk homepage: <https://channel.io/us> | Official product and marketing source | The plugin should mirror that rollout logic instead of inventing a new framework. |
| Human-AI support systems need uncertainty handling and human collaboration because support AI can miss intent or context. | Banerjee et al., "A System for Human-AI collaboration for Online Customer Support": <https://arxiv.org/abs/2301.12158> | Academic method reference | The plugin should mark missing evidence and human review points explicitly. |
| E-commerce messages can be reformulated into canonical questions to improve downstream answering. | Fetahu et al., "Instant Answering in E-Commerce Buyer-Seller Messaging using Message-to-Question Reformulation": <https://arxiv.org/abs/2401.09785> | Academic method reference | The plugin can normalize messy inquiry samples into response scenarios before planning outputs. |

## Role Fit Matrix

| Candidate role | Fit | Reason |
| --- | --- | --- |
| Channel Talk AX Consultant | Strong | Best match for ALF rollout design, knowledge preparation, scenario definition, and operator handoff planning. |
| Customer-side e-commerce CX operations manager | Medium | Supplies the material and approves policy, but is not the main operator of the planning workflow. |
| Product Manager | Weak | Would push the scope toward roadmap and product strategy, which this plugin should not do. |
| Applied AI Engineer | Weak | Would push the scope toward RAG, evaluation, and system implementation, which this plugin should not do. |

## Scope Boundaries

This plugin should remain:

- a skill-only Codex plugin
- a rollout-planning assistant for pasted text
- explicit about missing evidence and human review

This plugin should not become:

- an Applied AI Engineer RAG benchmark
- a PM roadmap tool
- an API integration implementation
- a model-evaluation tool

## Verification Implications

Verification should prove:

- the user and situation are framed as AX-consultant rollout work
- the output contract matches the skill and README
- unsupported refund approval, VIP exception handling, and delivery-date promises fail safely
- no claim is made about internal Channel Talk data access or customer system access
