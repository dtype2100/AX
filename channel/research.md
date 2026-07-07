# Channel Talk Research Phase

Date: 2026-07-08

## Problem Hypothesis

E-commerce CX teams using Channel Talk need a pre-automation planning workflow that turns scattered FAQs, policies, product/support notes, and chat exports into a short automation plan: inquiry taxonomy, candidate ALF rules, candidate ALF tasks, answer-quality risks, and next actions.

The narrow problem is not "build a chatbot." Channel Talk already provides ALF, FAQ, Knowledge, Rules, Tasks, Workflow, Analytics, and integrations. The missing submission workflow should help a CX lead decide what to configure first and what should stay human-reviewed.

## Target User

Primary user: e-commerce CX lead, support operations manager, or Channel Talk implementation owner.

Situation: preparing or improving ALF/FAQ/Workflow setup from public-facing policy pages, support macros, product notes, and a small sample of anonymized inquiry text.

## Video Context

- Title: `"AI 툴을 많이 쓰는 게 중요한 게 아닙니다" 채널톡이 바라보는 AI 시대 인재 | AX 인재전쟁 4화 채널톡`
- URL: https://www.youtube.com/watch?v=5iRf37Z8Wd4
- Source type: public YouTube video requested by the assignment; YouTube oEmbed title verified on 2026-07-08 with author 조코딩 JoCoding and provider YouTube.
- Transcript availability: Korean auto-generated transcript fetched from public YouTube via `youtube_transcript_api` on 2026-07-08. The transcript is not saved or quoted in full.
- Relevant summary: Channel Talk frames its work around the enduring business problem of customer/company communication, including e-commerce customer 상담. The video emphasizes AI agents for commerce support problems, while arguing that AX skill is not about trying many tools; it is about understanding why a problem and tool were chosen, using even one tool well, and increasing talent density so a small team can solve larger company-scale work.

## Evidence Map

| Claim | Source | Reliability | Plugin implication |
| --- | --- | --- | --- |
| Channel Talk positions AI around reducing repetitive inquiries so teams can focus on important work. | Channel Talk User Guide, AI category: https://docs.channel.io/help/en/categories/AI-d5340000 | Official product documentation | The plugin should focus on repeated inquiry triage, not generic CX advice. |
| FAQs can be pre-registered, ALF can answer from FAQ content, and Channel Talk's AI recommendations analyze open chats to suggest frequent FAQ topics. | Channel Talk FAQ guide: https://docs.channel.io/help/en/articles/FAQ--db21218c | Official product documentation | Output should include FAQ gaps and suggested question variants, sorted by likely frequency when input supports it. |
| ALF Rules are pre-written prompts applied by inquiry type, customer info, or scenario, with examples such as delivery delay tags and damaged-product routing. | Channel Talk Rule guide: https://docs.channel.io/help/en/articles/Rule-b43e19a1 | Official product documentation | Output should map inquiry classes to draft rule intent, filters, tags, and escalation conditions. |
| ALF Knowledge can reference articles, FAQs, websites, Excel, and PDFs, with filtering and reference descriptions controlling what ALF uses. | Channel Talk Knowledge guide: https://docs.channel.io/help/en/articles/Knowledge--803f6ac9 | Official product documentation | Output should flag missing, stale, ambiguous, or unstructured source material before recommending automation. |
| ALF Tasks automate common customer work beyond Q&A, including order cancellation, address changes, exchange/return/refund, and stock checks for e-commerce. | Channel Talk Task guide: https://docs.channel.io/help/en/articles/Task--2a16be8b | Official product documentation | Output should separate "answer only" topics from "task workflow" candidates requiring order/status/system checks. |
| Channel Talk Analytics exposes response metrics, inbound distribution, consultation tags, page/referral paths, and downloadable consultation statistics. | Channel Talk Chats analytics guide: https://docs.channel.io/help/en/articles/analytics-chats-10d6b120 | Official product documentation | Verification should use sample inputs and later can compare recommended taxonomy with existing tags/statistics exports. |
| Channel Talk's own homepage emphasizes clear rules, structured knowledge, executable tasks, and continuous improvement as the four ingredients for AI resolving routine inquiries. | Channel Talk homepage: https://channel.io/us | Official marketing/product source | Recommended workflow should mirror those four buckets: rules, knowledge, tasks, improvement checks. |
| Retail/e-commerce support increasingly uses automation for repetitive queries while preserving human attention for higher-value or complex interactions. | Vogue Business, "The tech driving next-gen customer service": https://www.voguebusiness.com/technology/cx-customer-service-ai-zendesk-kustomer-powerfront | Reputable industry source | The plugin should identify automation candidates and human-retained cases instead of recommending automation for every topic. |
| Human-AI collaboration is important because support bots can miss intent or personal context. | Banerjee et al., "A System for Human-AI collaboration for Online Customer Support": https://arxiv.org/abs/2301.12158 | Academic method reference | Output should include uncertainty, escalation triggers, and review notes, not just final answers. |
| E-commerce buyer messages can be reformulated into succinct questions to improve automated answering. | Fetahu et al., "Instant Answering in E-Commerce Buyer-Seller Messaging using Message-to-Question Reformulation": https://arxiv.org/abs/2401.09785 | Academic method reference | The skill can normalize messy inquiry samples into canonical question labels before taxonomy and FAQ recommendations. |

## Method References

- Use message-to-question reformulation as the lightest method for converting messy customer inquiry samples into canonical support questions: https://arxiv.org/abs/2401.09785
- Keep a human-in-the-loop support model with uncertainty and escalation because online support AI may misunderstand intent or lack personal context: https://arxiv.org/abs/2301.12158
- For this first plugin, avoid external automation or API calls. A skill-only workflow can inspect user-provided text and produce planning output.

## Implementation Structure References

- OpenAI Codex manual, Build plugins: a minimal plugin has `.codex-plugin/plugin.json` and can package one skill under `skills/<name>/SKILL.md`. The manual also says to start with a local skill while iterating and build a plugin when sharing the workflow. Local fetched source: `/var/folders/f_/9b1rshqd2qggyy4bf6d_q_x80000gn/T/openai-docs-cache/codex-manual.md`, source page `/codex/plugins/build.md`.
- OpenAI Codex manual, Agent Skills: skills package reusable workflow instructions and use `SKILL.md` with `name` and `description`. Local fetched source: `/var/folders/f_/9b1rshqd2qggyy4bf6d_q_x80000gn/T/openai-docs-cache/codex-manual.md`, source page `/codex/skills.md`.
- GitHub `openai/skills` points current Codex skill and plugin examples back to the OpenAI Plugins repository and the Build plugins guide: https://github.com/openai/skills
- Agent Skills specification defines the minimal `SKILL.md` directory structure and required frontmatter fields: https://agentskills.io/specification

## Open Risks

- Channel Talk official sources support the candidate problem strongly, but they are product docs and marketing pages. Keep industry sources limited to broad context and do not cite them for Channel Talk-specific claims.
- No private Channel Talk customer data should be used. Future tests should use synthetic or anonymized support snippets.
- A skill-only plugin will not prove Channel Talk API integration. That is acceptable for the first submission if the workflow is explicitly an implementation-planning assistant.

## Recommended Next Workflow

1. Define the plugin as `channel-alf-planner`, a skill-only Codex plugin.
2. Input: pasted FAQ/policy/support notes and optional anonymized inquiry samples.
3. Output: inquiry taxonomy, FAQ gaps, ALF Rule candidates, ALF Task candidates, answer-quality risks, escalation triggers, and next Channel Talk setup actions.
4. Verification: run the skill on a small synthetic e-commerce support pack covering shipping, cancellation, exchange/refund, stock, payment, damaged item, and VIP complaint cases.
5. Keep the plugin narrow. No MCP server, no Channel Talk API calls, no zip packaging until the skill works and README evidence matches this research.
