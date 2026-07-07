# Enterprise Problem Plugin Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or an equivalent subagent workflow to execute folder-specific tasks. The root chat is orchestration-only.

**Goal:** Build three independent Codex plugin submissions that solve public, verifiable problems for Channel Talk, Musinsa, and Kakao Pay Securities.

**Architecture:** The repository root coordinates planning, review, and Git only. Each company folder is an independent project root with its own research, plugin source, README, logs, verification, and `submission.zip`. Each plugin must solve one narrow core workflow rather than bundle broad features.

**Tech Stack:** Codex plugin, `src/.codex-plugin/plugin.json`, Codex skill in `src/skills/<name>/SKILL.md`, optional `src/.mcp.json`, Markdown docs, folder-local logs, zip packaging.

## Global Constraints

- Root workspace is orchestration-only.
- `channel/`, `musinsa/`, and `kakaopay/` are independent company-specific submissions.
- Each final `submission.zip` must contain `src/`, `README.md`, and `logs/` at the zip root.
- Each `src/` must contain `src/.codex-plugin/plugin.json` and at least one working plugin component.
- Prefer one narrow `src/skills/<name>/SKILL.md` as the initial plugin component.
- Do not combine multiple companies into one submission.
- Do not use private information, unverifiable anecdotes, uncited numbers, or AI summaries as standalone evidence.
- Preserve submitted logs without editing, excerpting, deleting, rewriting, or post-processing.
- For Kakao Pay Securities, do not design investment advice or buy/sell recommendation behavior.

---

## Assignment Interpretation

The three videos emphasize a shared AI-era talent theme: companies need people who solve real business problems, not people who merely list AI tools. The submission must translate that theme into company-specific, publicly verifiable problems and Codex plugins that address them.

Required five answers for every company:

1. What is the plugin, who uses it, and in what situation?
2. Why was this problem selected?
3. How does the plugin work?
4. How was AI used?
5. How was the plugin verified?

These answers must match the plugin behavior, README, logs, and evidence map.

## Research Method

Use a strict evidence ladder.

1. **Video analysis:** Treat the provided JoCoding videos as assignment-provided interview material and extract company context, AI strategy, and stated talent/problem framing.
2. **Trusted public search:** Use only trustworthy sources for problem evidence.
   - Preferred: company official pages, official blogs, technical blogs, product docs, press releases, job descriptions, IR/business reports.
   - Acceptable support: major media, industry reports, public institutions, associations, reputable interviews.
   - Not acceptable as core evidence: community posts, comments, personal blogs, unsourced summaries, AI-generated summaries.
3. **Evidence mapping:** For each core claim, record the source and how it connects to the plugin workflow.
4. **Technical literature:** Use arXiv papers and other academic papers for methods, not as standalone proof that the company has the problem.
5. **Implementation references:** Use GitHub, Codex official docs, installed marketplace plugins, and other open-source plugins for structure and validation patterns. Do not copy license-unclear code or prose.

Each company should have at minimum:

- 1 assignment video source.
- 1 official company source.
- 1 trustworthy supporting source.
- 1 technical reference, such as arXiv, GitHub, Codex docs, or a plugin example.

## Company Directions

### Channel Talk

Video source: <https://www.youtube.com/watch?v=5iRf37Z8Wd4>

Interpretation: Channel Talk values people who deeply reason about the real customer support problem instead of shallowly trying many AI tools.

Problem candidate: E-commerce support teams face repeated inquiries, context switching, inconsistent answers, and difficulty deciding which support workflows should be automated.

Plugin direction: A support operations analysis skill that reviews FAQ/policy/support-note inputs and produces inquiry taxonomy, automation candidates, answer-quality risks, and a next-action plan.

Primary user: E-commerce CX lead, support operations manager, Channel Talk implementation owner.

Research targets:

- Channel Talk official product/AI/customer support material.
- Public customer support automation or e-commerce CX operations sources.
- Technical references on RAG, support agents, conversation quality evaluation, and AI agent reliability.

### Musinsa

Video source: <https://www.youtube.com/watch?v=OLAWeIuiD5Y>

Interpretation: Musinsa emphasizes one-core multi-platform thinking, unifying fragmented data, and connecting deep reasoning to business impact.

Problem candidate: Fashion commerce teams manage fragmented brand, product, trend, and platform data, making it hard to turn broad market signals into clear merchandising or platform decisions.

Plugin direction: A fashion commerce decision-framing skill that structures brand/product/trend inputs into focused MD questions, evidence-backed hypotheses, and decision options.

Primary user: Fashion MD, brand operator, platform strategy/data operator.

Research targets:

- Musinsa official strategy, platform, brand, or tech materials.
- Public fashion commerce, recommendation, search, trend, or data integration sources.
- Technical references on fashion recommendation, multimodal product understanding, trend detection, and personalization.

### Kakao Pay Securities

Video source: <https://www.youtube.com/watch?v=aBuoojGjyf4>

Interpretation: Kakao Pay Securities emphasizes logical solvers who can use AI to make problems explainable and user-persuasive, especially for beginner investors and AI-assisted customer support.

Problem candidate: Beginner investors struggle to understand investment information, risks, and product explanations; support/content teams need explainable, risk-aware drafts rather than black-box advice.

Plugin direction: A beginner-investor explanation support skill that turns public investment/product/research text into plain-language explanation, risk checklist, uncertainty notes, and support-answer draft.

Primary user: Investor education/content operator, customer support operator, research support worker.

Safety boundary:

- The plugin must not recommend buying, selling, holding, timing, target prices, or personalized allocation.
- Output must be educational and support-oriented.
- README must include a non-investment-advice notice.

Research targets:

- Kakao Pay Securities official service, investor education, product, or press materials.
- Public financial consumer protection or beginner-investor education sources.
- Technical references on financial document summarization, explainable AI, hallucination mitigation, and risk disclosure.

## Execution Strategy

Use a stage-by-company matrix rather than one large task per company.

Stages:

1. Verify logging and submission baseline.
2. Analyze provided video.
3. Search trusted public sources.
4. Classify source reliability.
5. Build evidence map.
6. Review arXiv/papers for method ideas.
7. Review GitHub/Codex/plugin examples for implementation patterns.
8. Define problem statement.
9. Define one core workflow plugin concept.
10. Design plugin source structure, README, logs, and verification.
11. Implement company plugin in its folder only.
12. Verify plugin behavior, evidence consistency, logs, and package layout.

Subagents should receive one company and one stage or a small group of adjacent stages. The root orchestrator reviews outputs and prevents cross-folder mixing.

## Verification Plan

Before project work:

- Confirm each folder's hook setup actually writes unedited logs to that folder's `logs/`.
- If existing hooks produce slimmed or filtered logs, treat that as a blocker and adjust the logging plan before substantive work.
- Confirm root has no shared `log-hooks` used for submissions.

For each company:

- Check every problem claim has an official or trustworthy source.
- Check arXiv/papers are used for method design, not company-problem proof.
- Check GitHub/plugin examples are used only as references with license awareness.
- Run plugin validation appropriate to the final implementation.
- Use sample inputs to verify the one core workflow produces expected outputs.
- Verify the five required answers match README, plugin behavior, logs, and evidence map.
- Inspect `submission.zip` so its root contains exactly the expected top-level submission materials: `src/`, `README.md`, `logs/`.

## Deliverables

Root deliverables:

- `plan.md`: this orchestration and implementation plan.
- `task.md`: stage-by-company task checklist.

Company deliverables:

- `channel/submission.zip`
- `musinsa/submission.zip`
- `kakaopay/submission.zip`

Each company folder must also retain its working materials needed to explain and verify the submission.
