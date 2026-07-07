---
name: musinsa-md-brief
description: Turn Musinsa category trend, product, brand, and metric snippets into a concise MD decision brief.
---

# Musinsa MD Brief

Use this skill when the user is a Musinsa category MD responsible for trend-sensitive merchandising decisions and provides inputs such as brand notes, product attributes, trend signals, search or transaction metrics, season context, campaign ideas, or customer segments.

Do not pretend to access Musinsa internal systems. Use only the snippets the user provides and any public evidence they cite. If evidence is missing, mark it as a missing input instead of filling the gap.

## Workflow

1. Extract observed facts from the provided brand, product, trend, and metric snippets.
2. List missing inputs that would change the decision.
3. Convert the facts and gaps into MD questions.
4. Draft evidence-backed hypotheses, clearly labeled as hypotheses.
5. Give decision options for category merchandising, curation, promotion, or further investigation.
6. Note brand and customer risks, including partner-brand impact, cannibalization, over-curation, fit/compatibility, price, seasonality, and localization risks when relevant.
7. End with verification checks the user can run before acting.

## Output Format

```markdown
## Musinsa MD Brief

### Facts
- ...

### Missing Inputs
- ...

### MD Questions
- ...

### Hypotheses
- ...

### Decision Options
- ...

### Brand And Customer Risks
- ...

### Verification Checks
- ...
```

## Guardrails

- Separate facts from hypotheses.
- Preserve metric units and time windows exactly as supplied.
- Avoid uncited numbers.
- Prefer concise bullets over long narrative.
- If the user asks for a final decision, choose the lowest-risk option and state what evidence would overturn it.
