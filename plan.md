# Enterprise Problem Plugin Implementation Plan

> **For agentic workers:** Use folder-specific subagents. The repository root is orchestration-only.

**Goal:** Build three independent Codex plugin submissions for Channel Talk, Musinsa, and Kakao Pay Securities.

**Architecture:** Each company folder is an independent project root with its own active hook config, original logs, research, plugin source, README, verification, and `submission.zip`.

**Tech Stack:** Codex plugin, `src/.codex-plugin/plugin.json`, one core skill in `src/skills/<name>/SKILL.md`, optional `src/.mcp.json`, Markdown docs, folder-local logs, zip packaging.

## Non-Negotiable Setup

- Active hooks live at:
  - `channel/.codex/hooks.json`
  - `musinsa/.codex/hooks.json`
  - `kakaopay/.codex/hooks.json`
- Hook scripts live under each folder's `log-hooks/tools/save_log.py`.
- Submitted logs must be copied verbatim from the Codex transcript.
- Automatic capture happens when Codex runs in the company folder, loads that folder's `.codex/hooks.json`, and the hook is trusted/approved.
- Do not start substantive company research or implementation until each folder proves logs are written to its own `logs/` directory.
- Root `AGENTS.md` and folder `AGENTS.md` files define durable operating rules. Planning/checklist docs may be regenerated after hook setup.

## Assignment Requirements

Each company submission must produce a `submission.zip` with this root layout:

```text
submission.zip
├── src/
│   ├── .codex-plugin/plugin.json
│   ├── skills/<name>/SKILL.md
│   ├── .mcp.json
│   └── other runtime code and configuration files
├── README.md
└── logs/
```

Each README must answer:

1. What is the plugin, who uses it, and in what situation?
2. Why was this problem selected?
3. How does the plugin work?
4. How was AI used?
5. How was the plugin verified?

## Research Rules

- Use the provided video as assignment interview context, not as the only proof.
- Use trusted public evidence for problem claims:
  - official company sources first
  - reputable media, industry reports, public institutions, associations, IR/business reports as support
- Do not use private information, unverifiable anecdotes, comments, unsourced numbers, or AI summaries as standalone evidence.
- Use arXiv and academic papers only for technical method references.
- Use GitHub, Codex docs, and existing plugins only for implementation structure references.
- Check licenses before copying any code or substantial prose; prefer original implementation.

## Company Directions

### Channel Talk

- Video: <https://www.youtube.com/watch?v=5iRf37Z8Wd4>
- Problem candidate: e-commerce support teams face repeated inquiries, context switching, inconsistent answers, and uncertainty about what to automate.
- Core workflow: analyze FAQ/policy/support notes and produce inquiry taxonomy, automation candidates, answer-quality risks, and next-action plan.
- User: e-commerce CX lead, support operations manager, Channel Talk implementation owner.
- Technical references: RAG, conversational agents, support automation, answer quality evaluation.

### Musinsa

- Video: <https://www.youtube.com/watch?v=OLAWeIuiD5Y>
- Problem candidate: fashion commerce teams manage fragmented brand, product, trend, and platform data, making merchandising decisions hard to frame.
- Core workflow: structure brand/product/trend inputs into MD questions, evidence-backed hypotheses, decision options, and risk notes.
- User: fashion MD, brand operator, platform strategy/data operator.
- Technical references: fashion recommendation, multimodal product understanding, trend detection, personalization.

### Kakao Pay Securities

- Video: <https://www.youtube.com/watch?v=aBuoojGjyf4>
- Problem candidate: beginner investors struggle to understand investment information, product risks, and support explanations.
- Core workflow: turn public investment/product/research text into plain-language explanation, risk checklist, uncertainty notes, and support-answer draft.
- User: investor education operator, customer support operator, content operator, research support worker.
- Safety boundary: no buy/sell/hold, target price, market timing, or personalized allocation recommendations.
- Technical references: financial document summarization, explainable AI, hallucination mitigation, risk disclosure.

## Execution Strategy

Use a stage-by-company matrix:

1. Verify hooks and original log capture.
2. Analyze the video.
3. Search trusted public sources.
4. Classify reliability and build evidence map.
5. Review arXiv/papers for methods.
6. Review GitHub/Codex/plugin examples for structure.
7. Define problem statement.
8. Define one core workflow.
9. Design plugin, README, verification, and package layout.
10. Implement in the company folder only.
11. Verify behavior, evidence consistency, logs, and `submission.zip`.

## Verification Gates

- Hook gate: `logs/codex/<session_id>.jsonl` appears in the correct company folder and matches the source transcript verbatim.
- Evidence gate: every core problem claim has official or trustworthy support.
- Safety gate: `kakaopay/` never gives investment advice.
- Plugin gate: `plugin.json`, one working skill, README, logs, and sample verification all exist.
- Packaging gate: zip root contains `src/`, `README.md`, and `logs/`, not the company folder itself.
