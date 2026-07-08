# Channel ALF Planner

## 심사용 빠른 요약

ALF 자동화 전에, 자동화해도 되는 것과 사람에게 남겨야 하는 것을 가르는 AX 설계 플러그인.

| 항목 | 내용 |
| --- | --- |
| Target user | Channel Talk AX Consultant |
| Situation | 고객사의 ALF 도입 전, FAQ/정책/운영 메모를 자동화 설계안으로 정리해야 할 때 |
| Input | 공개 FAQ, 배송/교환/환불 정책, 상담 매크로, 제품 메모, 익명화된 문의 예시 |
| Output | 지식 준비도, 자동화 후보, 워크플로/API 핸드오프 후보, 상담원 핸드오프 노트, 출시 후 점검 항목 |
| Public evidence | Channel Talk ALF, FAQ, Rule, Knowledge, Task 공식 문서와 Channel Talk AX Consultant 공개 채용 공고 |
| Verification | 설치 구조, 성공 샘플, 실패 샘플, 로그 보존, 제출 zip 구조를 확인 |

### 실제 입력 / 출력 스냅샷

Sample Input:

```text
Shipping: Orders ship in 1-2 business days. Tracking is sent after dispatch.
Returns: Customers may request return within 7 days if the item is unused.
Refunds: Refund timing depends on payment provider confirmation.
Damaged item: Ask the customer for order number and photo, then escalate to an operator.
```

Output Snapshot:

| Section | Key output |
| --- | --- |
| Implementation Context | E-commerce support rollout before ALF setup; source is policy text only, with no internal system access assumed. |
| Knowledge Readiness | Shipping and return basics are usable; refund timing needs safer wording because provider timing is not fixed. |
| Response Scenario Candidates | Shipping status and basic return eligibility can be drafted from evidence; damaged-item handling needs escalation. |
| Workflow/API Handoff Candidates | Tracking lookup and refund-status checks are planning candidates only if later connected to approved systems. |
| Operator Handoff Notes | Escalate damaged-item claims, missing order numbers, payment-provider disputes, and unsupported exceptions. |
| Post-Launch Review | Review unresolved refund questions, escalation rate, missing FAQ candidates, and repeated operator corrections. |

### 검증 요약

| Check | Result |
| --- | --- |
| Install | PASS |
| Success sample | PASS |
| Failure sample | PASS |
| Logs | PASS |
| Zip | PASS |

Channel ALF Planner is a skill-only Codex plugin for a Channel Talk AX Consultant who is preparing a customer's ALF rollout. The customer-side stakeholder is typically an e-commerce CX operations manager who owns the source material and approves policy decisions.

Situation: before ALF setup, the consultant has to turn scattered FAQ pages, shipping/return/refund policies, support macros, product notes, and optional anonymized inquiry samples into a rollout-ready planning brief.

Inputs: pasted public-facing support materials and optional anonymized inquiry examples. The plugin does not connect to Channel Talk, customer systems, internal dashboards, or private data sources.

Outputs: `Implementation Context`, `Knowledge Readiness`, `Inquiry Taxonomy`, `FAQ Gaps`, `Response Scenario Candidates`, `Workflow/API Handoff Candidates`, `Operator Handoff Notes`, and `Post-Launch Review`.

## 1. What is the plugin, who uses it, and in what situation?

The plugin is a planning assistant for Channel Talk ALF onboarding. Its primary user is a Channel Talk AX Consultant who is preparing a customer rollout and needs a structured way to decide:

- what knowledge is ready for ALF
- which scenarios are safe to automate
- which workflows may need task or API handoff later
- which cases must stay with a human operator

The e-commerce CX operations manager remains the customer-side stakeholder. They provide policy text, review missing evidence, and approve exceptions, but the plugin itself is framed around the consultant's rollout work rather than the customer's day-to-day queue handling.

## 2. Why was this problem selected?

This plugin is aimed at a public, verifiable Channel Talk problem: ALF works best when rules, structured knowledge, and executable tasks are prepared before launch.

Official product evidence:

- Channel Talk positions ALF as an AI support agent that resolves repetitive customer conversations so teams can focus on higher-value work: <https://docs.channel.io/help/en/categories/AI-d5340000>
- The FAQ guide says ALF can answer from registered FAQ content and Channel Talk can recommend FAQ candidates from ongoing conversations: <https://docs.channel.io/help/en/articles/FAQ--db21218c>
- The Rule guide shows scenario-based prompting, routing, and tagging for cases such as delivery delays and damaged items: <https://docs.channel.io/help/en/articles/Rule-b43e19a1>
- The Knowledge guide says ALF can rely on structured sources such as documents, websites, Excel, and PDFs, with scoped references and filters: <https://docs.channel.io/help/en/articles/Knowledge--803f6ac9>
- The Task guide says ALF can handle operational tasks such as cancellation, address change, exchange, return, refund, stock check, and order lookup: <https://docs.channel.io/help/en/articles/Task--2a16be8b>
- The Channel Talk homepage says accurate AI support comes from the combination of trusted rules, structured knowledge, and actionable support: <https://channel.io/us>

Supporting context only, not sole proof:

- The AX video context reinforces the framing that strong AI work starts from a real business problem, uses AI agents to solve essential work, and values talent density over collecting tools: <https://www.youtube.com/watch?v=5iRf37Z8Wd4>

Why AX Consultant is the best fit:

- Channel Talk AX Consultant is supported by a public Korean careers posting checked on 2026-07-08: <https://channel.io/kr/careers/e588e8b8-c1d1-43d7-b8b0-3ae9cb639d74>
- The posting duties align with turning FAQ, product, and operation-policy data into Knowledge, building response scenarios, onboarding customers, designing workflow/API handoffs, surfacing CX insights, and collaborating with engineering.
- The job to be done is rollout design: interpret customer policy material, shape ALF knowledge, define response scenarios, flag missing evidence, and prepare human handoff notes.
- That is closer to customer-facing AX implementation work than to PM roadmap prioritization.
- It is also closer to deployment planning than to an Applied AI Engineer workflow, because this plugin does not build models, run evaluations, tune RAG, or implement system integrations.

## 3. How does the plugin work?

The plugin stays intentionally small:

- `src/.codex-plugin/plugin.json` declares the plugin
- `src/skills/channel-alf-planner/SKILL.md` defines the workflow and output contract
- there is no MCP server, Channel Talk API call, model-evaluation harness, roadmap generator, or integration runtime

Execution flow:

1. Ask for pasted source text when it is missing.
2. Refuse to proceed on personal data or unsupported claims.
3. Separate the input into policies, facts, process steps, unresolved claims, and inquiry examples.
4. Assess whether the material is ready enough for ALF knowledge use.
5. Normalize messy inquiry examples into short customer scenarios.
6. Propose automation candidates only when the pasted text supports them.
7. For every automation candidate, explain:
   - why it fits automation
   - what pasted evidence supports it
   - what evidence is still missing
   - when a human should intervene
8. Where execution or system checks may be needed later, suggest workflow/API handoff candidates as planning notes only.
9. End with operator handoff notes and a post-launch review checklist.

If the source does not prove a policy, the plugin must say `not enough evidence` or `human review required`. It must not invent refund approvals, VIP exception rules, delivery-date promises, or internal system capabilities.

## 4. How was AI used?

AI is used as a planning copilot, not as a hidden integration layer. Codex reads the pasted text, normalizes inquiry language, clusters repeated scenarios, surfaces knowledge gaps, and drafts rollout artifacts for a consultant to review.

Method support:

- Human-in-the-loop support research supports uncertainty marking and escalation instead of overconfident automation: <https://arxiv.org/abs/2301.12158>
- Message-to-question reformulation is a good fit for turning messy customer language into canonical support scenarios: <https://arxiv.org/abs/2401.09785>

This is not a RAG benchmark, PM roadmap tool, API integration implementation, or model-evaluation tool.

## 5. How was the plugin verified?

Verification stayed inside `/Users/jinlee/ax_herkerton/channel` and did not edit logs.

Install and structure checks:

```text
$ pwd
/Users/jinlee/ax_herkerton/channel

$ find src -maxdepth 4 -type f | sort
src/.codex-plugin/plugin.json
src/skills/channel-alf-planner/SKILL.md

$ python3 -m json.tool src/.codex-plugin/plugin.json >/dev/null && echo plugin-json-ok
plugin-json-ok
```

Behavior checks used a synthetic e-commerce support pack with shipping, cancellation, exchange/return, refund, stock, payment, damaged-item, and VIP complaint scenarios. The plugin was checked for these outcomes:

- it produces the same rollout sections described in the skill
- it keeps claims tied to pasted evidence
- it separates automation-fit scenarios from human-review scenarios
- it does not claim Channel Talk API access or customer internal data access

Failure tests checked that the plugin refuses to invent policy:

- unsupported refund approval policy -> `not enough evidence` or `human review required`
- VIP exception handling without a written rule -> `human review required`
- unsupported delivery-date promise when tracking or SLA proof is missing -> `not enough evidence`

Logs were left untouched. `logs/codex/*.jsonl` remain the original hook-copied transcripts under the Channel folder.

## Role Fit Matrix

| Role | Fit | Why |
| --- | --- | --- |
| Channel Talk AX Consultant | Primary fit | Owns ALF rollout design, source review, scenario definition, handoff planning, and launch-readiness judgment. |
| Customer-side e-commerce CX operations manager | Secondary stakeholder | Supplies policy/materials and approves decisions, but is not the main operator of this plugin's planning workflow. |
| Product Manager | Weak fit | PM work would focus on roadmap, prioritization, and product decisions rather than customer-specific ALF rollout preparation. |
| Applied AI Engineer | Weak fit | This plugin does not build retrieval, model evaluation, or production integrations; it prepares rollout artifacts from pasted text. |

## Evidence Matrix

| Claim supported by the plugin | Public evidence | Why it matters |
| --- | --- | --- |
| AX Consultant is a public Channel Talk role whose listed duties match this workflow | Channel Talk Korean AX Consultant posting | Grounds the target user in a public role while keeping product docs as the main proof of the ALF problem. |
| ALF depends on clear rules | Channel Talk Rule guide | Justifies scenario rules and exception gates. |
| ALF depends on structured knowledge | Channel Talk Knowledge guide | Justifies knowledge-readiness assessment before automation. |
| ALF can answer from FAQ and recommend FAQ opportunities | Channel Talk FAQ guide | Justifies FAQ gap finding and scenario normalization. |
| ALF can handle operational tasks | Channel Talk Task guide | Justifies workflow/API handoff candidates as planning outputs. |
| AI support should reduce repetitive work while preserving higher-value human attention | Channel Talk AI docs, Channel Talk homepage, human-AI support paper | Justifies automation-fit analysis plus operator handoff notes. |

## Before / After

Before:

- FAQ, policy, macro, and inquiry text are scattered
- automation candidates are mixed together with unsupported edge cases
- launch risk is hidden inside missing refund, VIP, or delivery policies
- the consultant has to infer rollout scope manually

After:

- knowledge readiness is visible
- response scenarios are organized into concrete rollout candidates
- workflow/API handoff candidates are separated from answer-only scenarios
- unsupported cases are explicitly marked for human review
- the consultant has a post-launch review list instead of a vague "set up ALF" task
