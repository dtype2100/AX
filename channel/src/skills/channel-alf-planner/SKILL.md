---
name: channel-alf-planner
description: Use when planning Channel Talk ALF setup for an e-commerce support team from pasted FAQ pages, policy text, support macros, product notes, and optional anonymized customer inquiries. Produces inquiry taxonomy, FAQ gaps, ALF Rule candidates, ALF Task candidates, answer-quality risks, escalation triggers, and next Channel Talk setup actions.
---

# Channel ALF Planner

## Inputs

Ask for pasted source text when it is missing. Accept any mix of:

- FAQ, policy, shipping, return, refund, product, membership, or payment notes.
- Support macros or agent notes.
- Optional anonymized customer inquiries or chat snippets.

Do not use private customer data. If personal data appears, tell the user to remove it before continuing.

## Workflow

1. Separate source material into facts, policies, process steps, unresolved claims, and inquiry samples.
2. Rewrite messy inquiry samples as short canonical customer questions.
3. Group questions and source facts into a compact inquiry taxonomy.
4. Identify FAQ gaps where repeated questions lack a clear, customer-safe answer.
5. Propose ALF Rule candidates for repeated answer patterns, routing, tagging, or scenario-specific handling.
6. Propose ALF Task candidates only when the inquiry requires an action or system check, such as cancellation, address change, exchange, return, refund, stock check, order lookup, or delivery status.
7. List answer-quality risks: missing policy detail, stale source text, contradictory instructions, jurisdiction/payment constraints, inventory dependency, or claims needing human review.
8. List escalation triggers for sensitive, high-value, ambiguous, angry, legal, payment, damaged-item, or exception cases.
9. End with the next Channel Talk setup actions in order: knowledge cleanup, FAQ additions, tags/rules, task candidates, review metrics, and human QA.

## Output Format

Use this exact structure:

```markdown
## Inquiry Taxonomy
| Category | Canonical questions | Source basis | Automation fit |
| --- | --- | --- | --- |

## FAQ Gaps
| Gap | Why it matters | Suggested FAQ question | Needed source |
| --- | --- | --- | --- |

## ALF Rule Candidates
| Rule | Trigger | Draft behavior | Tags or routing | Escalate when |
| --- | --- | --- | --- | --- |

## ALF Task Candidates
| Task | Customer goal | Required system/source check | Human fallback |
| --- | --- | --- | --- |

## Answer-Quality Risks
-

## Escalation Triggers
-

## Next Channel Talk Setup Actions
1.
```

Keep recommendations tied to the pasted text. Say "not enough evidence" instead of inventing policies, metrics, integrations, or API behavior.
