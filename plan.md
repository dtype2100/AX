# Final Integrated Improvement Plan

> Root workspace rule: this repository root is for orchestration, review, and Git operations only. Company-specific implementation belongs inside `channel/`, `musinsa/`, and `kakaopay/`.

## Goal

Complete three company-specific Codex plugin submissions so each one aligns its hiring-site role fit, video context, public evidence, five required answers, plugin behavior, logs, and verification results.

The current plugin directions remain valid. This plan sharpens the target user and deliverable for each project instead of pivoting to unrelated domains.

| Company | Final positioning | Decision |
| --- | --- | --- |
| Channel Talk | A plugin that helps Channel Talk AX Consultants turn customer ALF onboarding material into an automation design brief. | Keep direction, refine target user. |
| Musinsa | A plugin that helps global-fashion category growth MDs turn fragmented trend, brand, inventory, price, and campaign signals into an execution brief. | Keep direction, make MD workflow more specific. |
| Kakao Pay Securities | A plugin that helps customer-support knowledge / investor-education content operators turn public investment material into safe beginner explanations. | Keep direction, strengthen safety boundaries. |

## Evidence And Context Rules

- Hiring-site evidence defines the target user and job-fit logic.
- Official company/service sources prove the public problem.
- Video summaries are supporting context only, not standalone proof.
- Academic, GitHub, Codex, and plugin references support implementation method, not company problem claims.
- Each folder must keep README, skill behavior, research notes, logs, and test summaries consistent with one another.

## Required README Tables

Each company README must include or clearly cover:

- `Role Fit Matrix`: why the selected user is the best fit, and why close alternatives are weaker.
- `Evidence Matrix`: problem claim -> public evidence -> plugin feature -> verification result.
- `Before / After`: messy source input -> usable work artifact.

## Five Required Answers

Each company README must directly answer:

1. What is the plugin, who uses it, and in what situation?
2. Why was this problem selected?
3. How does the plugin work?
4. How was AI used?
5. How was the plugin verified?

The answers must be reflected in the corresponding `src/skills/<name>/SKILL.md` behavior and verification results.

## Company Work Plans

### Channel Talk

Final target user: Channel Talk AX Consultant preparing customer ALF rollout.

Reasoning:
- The AX Consultant role analyzes customer FAQ, product information, and operation-policy data into ALF Knowledge.
- It also builds response scenarios, designs workflow/API handoff candidates, supports onboarding, and derives post-launch CX insights.
- The current ALF planner is closer to AX implementation work than to PM product strategy or Applied AI Engineer model work.

Required changes:
- Reframe the README and skill from `e-commerce CX operations manager` to `Channel Talk AX Consultant`; keep the CX operations manager as the customer-side stakeholder.
- Add or strengthen outputs for `Implementation Context`, `Knowledge Readiness`, `Response Scenario Candidates`, `Workflow/API Handoff Candidates`, `Operator Handoff Notes`, and `Post-Launch Review`.
- Make every automation candidate explain why it fits automation, what evidence is missing, and when a human should intervene.
- Add a failure test for unsupported refund approval, VIP exception handling, or unsupported delivery-date promises.
- Do not turn this into a RAG benchmark, model evaluation tool, or PM roadmap tool.

Video context to reflect:
- AX, AI agent, essential problem solving, and talent-density thinking.
- Position the plugin as a way to explain why a specific ALF setup is the right answer to a real customer support problem.

### Musinsa

Final target user: Musinsa global-fashion category growth MD.

Reasoning:
- The global-fashion MD role covers brand portfolio strategy, category growth, revenue/profit/inventory metrics, pricing/promotion, SKU/season operations, partnerships, and end-to-end execution.
- The current MD brief already separates facts, missing inputs, hypotheses, options, risks, and verification checks.

Required changes:
- Reframe the README and skill from broad `Musinsa category MD` to `global-fashion category growth MD`.
- Add input expectations for `category`, `brand`, `season`, `SKU depth`, `sales/transaction`, `profit or margin`, `inventory`, `price/promotion`, `customer segment`, and `exposure plan`.
- Add or strengthen outputs for `Business Impact`, `Portfolio/SKU Considerations`, and `Pricing And Promotion Risks`.
- Make missing revenue, profit, inventory, pricing, promotion, SKU, and partnership constraints visible.
- Add a failure test for unsupported numeric sales prediction without internal or cited data.
- Do not claim to be a recommendation engine, pricing optimizer, inventory optimizer, or internal-data tool.

Video context to reflect:
- Data fragmentation, one-core multi-platform, and connecting deep thinking to business impact.
- Position the plugin as a way to turn scattered signals into a narrow, verifiable MD decision brief.

### Kakao Pay Securities

Final target user: customer-support knowledge / investor-education content operator.

Reasoning:
- The public hiring page gives process and culture context, not a precise matching open-role description.
- The culture page emphasizes customer-centered work, fact-based communication, principles/manuals, and AI-native work.
- The official service site emphasizes easy access for inexperienced investors while also warning about explanation rights, product documents, and principal-loss risk.
- The safe fit is educational explanation support, not investment advice.

Required changes:
- State that the target user is an inferred function, not a claimed official job title.
- Keep the plugin focused on understanding public source material before a decision, never on buy/sell/hold decisions.
- Add or strengthen outputs for `Fact vs Opinion`, `Risk Checklist`, `Uncertainty Notes`, `Human Review Required`, `Compliance Review Needed`, and `Notice`.
- Add a privacy intake guard for personal information, account data, resident-registration numbers, salary, tokens, and other secrets.
- Add refusal tests for buy/sell/hold, target price, timing, subscription/redemption, tax/legal, account-specific judgment, and personalized allocation requests.

Video context to reflect:
- Solver, logical proof, and helping users understand.
- Position the plugin as a source-grounded explanation assistant that helps operators make reasoning inspectable without crossing into advice.

## Verification Plan

Run the following inside each company folder after edits.

### Structure

```bash
find src -maxdepth 4 -type f | sort
python3 -m json.tool src/.codex-plugin/plugin.json
test -f README.md
test -d logs
```

Pass criteria:
- `src/.codex-plugin/plugin.json` exists.
- `src/skills/<name>/SKILL.md` exists.
- `README.md` exists.
- `logs/` exists.
- `plugin.json` parses.

### Installation

```bash
codex plugin list | rg "<plugin-name>"
```

Pass criteria:
- Plugin appears as installed and enabled.
- Plugin path points to that company's `src`.

### Functional Samples

- Channel Talk: FAQ/policy/support macro sample produces Knowledge, Rule, Task, Workflow/API, and human-escalation outputs.
- Musinsa: global-brand season-campaign sample produces facts, missing inputs, MD questions, hypotheses, decision options, risks, and verification checks.
- Kakao Pay Securities: Korean investment notice sample produces plain explanation, key terms, risk checklist, fact/opinion separation, review flags, and non-advice notice.

### Failure / Refusal Samples

- Channel Talk: unsupported policy automation request must not invent policy.
- Musinsa: unsupported numeric forecast request must not invent internal data.
- Kakao Pay Securities: investment-advice request must be refused and redirected to education/risk questions.

### Five-Question Gate

Each README must pass this table:

| Question | README answer | Skill behavior | Test result |
| --- | --- | --- | --- |
| What/who/situation? | Y | Y | Y |
| Why this problem? | Y | Y | Y |
| How does it work? | Y | Y | Y |
| How was AI used? | Y | Y | Y |
| How was it verified? | Y | Y | Y |

### Logs

```bash
find logs -type f | sort
```

Pass criteria:
- `logs/codex/*.jsonl` exists.
- Logs are folder-local and original.
- Root orchestration logs and other company logs are not mixed in.

### Zip

```bash
zipinfo -1 submission.zip | sort
```

Pass criteria:
- Zip root contains `src/`, `README.md`, and `logs/`.
- Zip root does not contain a top-level `channel/`, `musinsa/`, or `kakaopay/` folder.
- `src/.codex-plugin/plugin.json` and `src/skills/<name>/SKILL.md` are present.

## Execution Order

1. Update root `plan.md` and `task.md`.
2. Run folder-specific subagents for `channel/`, `musinsa/`, and `kakaopay/`.
3. Review diffs and close gaps.
4. Regenerate `submission.zip` in each company folder.
5. Run structure, installation, function, refusal, five-question, log, and zip checks.
6. Commit and push.
