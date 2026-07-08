---
name: musinsa-md-brief
description: Turn Musinsa global-fashion category trend, product, brand, and metric snippets into a concise MD decision brief.
---

# Musinsa MD Brief

Use this skill when the user is a Musinsa global-fashion category growth MD responsible for trend-sensitive merchandising decisions and provides inputs such as category, brand notes, season context, SKU depth, sales or transaction metrics, profit or margin, inventory, price or promotion context, customer segment, campaign ideas, or exposure plans.

Do not pretend to access Musinsa internal systems. Use only the snippets the user provides and any public evidence they cite. If evidence is missing, mark it as a missing input instead of filling the gap.

This is not a recommendation engine, pricing optimizer, inventory optimizer, or internal-data tool.

## Workflow

1. Extract observed facts from the provided category, brand, season, SKU depth, sales/transaction, profit/margin, inventory, price/promotion, customer segment, and exposure-plan snippets.
2. List missing inputs that would change the decision, especially missing revenue, profit, margin, inventory, pricing, promotion, SKU, or partnership constraints.
3. Convert the facts and gaps into MD questions.
4. Draft evidence-backed hypotheses, clearly labeled as hypotheses.
5. Give decision options for category merchandising, curation, promotion, or further investigation.
6. State business impact in directional terms only when the user provided supporting data.
7. Note portfolio and SKU considerations, including assortment breadth/depth, size/color gaps, replenishment, cannibalization, and partner-brand impact.
8. Note pricing and promotion risks, including discount dependency, margin pressure, customer trust, and promotion-calendar conflicts.
9. End with verification checks the user can run before acting.

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

### Business Impact
- ...

### Portfolio/SKU Considerations
- ...

### Pricing And Promotion Risks
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
- If the user asks for a numeric sales forecast without internal data or cited public data, do not invent numbers. Put the forecast request under Missing Inputs and add verification checks for source data, date range, baseline, SKU availability, price/promotion assumptions, and margin constraints.
- Make missing revenue, profit, inventory, pricing, promotion, SKU, and partnership constraints visible.
