# Kakao Pay Securities Research Phase

## Problem Hypothesis

Beginner or low-experience investors using Kakao Pay Securities can access investments easily, but still need plain-language help understanding public investment text, product risks, uncertainty, and what questions to ask before acting. A narrow Codex skill should help support, education, or content operators convert public investment/product/research text into an educational explanation, risk checklist, uncertainty notes, and a support-answer draft.

This workflow must not produce buy, sell, hold, target price, market timing, or personalized allocation recommendations.

## Target User

Primary user: Kakao Pay Securities investor education, customer support, content, or research-support operator.

Situation: the operator has public source text, such as a product notice, research excerpt, FAQ, risk disclosure, or investor education page, and needs a consistent support-oriented explanation for beginner investors.

## Evidence Map

| Claim | Source | Reliability | Plugin implication |
| --- | --- | --- | --- |
| Kakao Pay Securities positions itself around easier investing for users with smaller assets or less experience. | Kakao Pay Securities official site, main page: https://www.kakaopaysec.com/ | Tier 1: company official | Focus the plugin on beginner-friendly explanation and support workflows. |
| Kakao Pay Securities highlights small-amount access, MTS usability, understandable investment news, recurring stock purchase, stock gifting, fractional overseas stocks, and fund products. | Kakao Pay Securities official site, business/service sections: https://www.kakaopaysec.com/ | Tier 1: company official | Inputs may span investment news, stocks, overseas fractional shares, funds, and product notices; output should normalize jargon without recommending action. |
| Kakao Pay Securities states investors have the right to sufficient explanation, should read product documents/terms before investing, and may lose principal on financial investment products. | Kakao Pay Securities official site disclosure text: https://www.kakaopaysec.com/ | Tier 1: company official | Every output should include source-grounded risk notes, document-reading prompts, and non-advice language. |
| Investment risk includes uncertainty and possible financial loss; different products have different risk/return and liquidity characteristics. | SEC Investor.gov, "What is Risk?": https://www.investor.gov/introduction-investing/investing-basics/what-risk | Tier 1: public regulator investor education | Build a risk checklist that calls out volatility, business, interest-rate, liquidity, inflation, and principal-loss risks when relevant. |
| Securities and investment products are not the same as insured deposits; value can rise or fall. | SEC Investor.gov, "What is Risk?": https://www.investor.gov/introduction-investing/investing-basics/what-risk | Tier 1: public regulator investor education | Avoid language implying guarantees; force explicit "not deposit-like / principal may be lost" checks where relevant. |
| Grounded generation with retrieval/provenance is a useful pattern for knowledge-intensive explanations because model-only factual recall is limited. | Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", arXiv: https://arxiv.org/abs/2005.11401 | Tier 2: peer-reviewed method paper | Require the skill to ground answers in user-provided public text and cite/quote only short source snippets. |
| Finance-domain AI support needs explicit routing/safety layers and human QA in high-stakes settings. | Park et al., "AI PB: A Grounded Generative Agent for Personalized Investment Insights", arXiv: https://arxiv.org/abs/2510.20099 | Tier 2: academic/preprint method reference | Keep the first plugin as a non-personalized support draft tool with hard finance-safety boundaries and operator review. |
| Agent Skills are packaged as a folder with required `SKILL.md`, metadata, instructions, and optional scripts/references/assets. | Agent Skills specification: https://agentskills.io/specification and GitHub repo: https://github.com/agentskills/agentskills | Tier 2: public technical specification/GitHub reference | Implement as one minimal skill under `src/skills/<name>/SKILL.md`; add scripts only if needed later. |

## Method References

- Retrieval-augmented generation: use the RAG pattern only as a design principle: ground outputs in explicit source text, surface provenance, and avoid unsupported claims. Source: https://arxiv.org/abs/2005.11401
- Grounded finance AI safety: use layered safety as a design principle, but do not build a personalized investment agent. Source: https://arxiv.org/abs/2510.20099

## Implementation Structure References

- Required local assignment structure: `src/.codex-plugin/plugin.json`, `src/skills/<name>/SKILL.md`, folder-level `README.md`, and folder-level `logs/`.
- Public skill structure reference: Agent Skills spec says a skill directory minimally contains `SKILL.md` with `name` and `description`, plus Markdown instructions; scripts, references, and assets are optional. Source: https://agentskills.io/specification
- GitHub reference repo for the same spec: https://github.com/agentskills/agentskills

## Finance Safety Risks

- The plugin could accidentally turn explanation into advice. Guardrail: prohibit buy/sell/hold, target prices, market timing, and personalized allocation.
- The plugin could overstate certainty from public research text. Guardrail: require uncertainty notes and "what is unknown from this source" sections.
- The plugin could omit principal-loss or non-deposit warnings. Guardrail: require a risk checklist and non-investment-advice notice in every output.
- The plugin could personalize outputs from user demographics or account data. Guardrail: use only public text supplied by the operator and refuse personalized recommendations.
- The plugin could hallucinate regulatory or product facts. Guardrail: require source-bound phrasing and ask for missing product documents rather than filling gaps.

## Open Risks

- The brief's YouTube URL, https://www.youtube.com/watch?v=aBuoojGjyf4, was not publicly fetchable through the available browser/search path in this phase, so it remains unanalyzed.
- The exact Kakao Pay Securities official page URLs for some customer-center subsections may require JavaScript navigation; the main official site was usable and enough for the first hypothesis.
- Future README wording should be reviewed against Korean financial advertising and investor-protection constraints before packaging.
- The plugin should be verified on examples covering stock news, fund/product notices, and research excerpts before `submission.zip`.

## Recommended Next Workflow

1. Define the minimal skill name and output contract: plain-language summary, key terms, risk checklist, uncertainty notes, source-grounded support draft, and refusal rules.
2. Create `src/.codex-plugin/plugin.json` and one skill at `src/skills/<name>/SKILL.md`.
3. Draft `README.md` from this evidence map and the five required answers.
4. Verify the skill with public sample inputs and confirm it refuses investment advice.
5. Package only after logs, README, source, and behavior are consistent.
