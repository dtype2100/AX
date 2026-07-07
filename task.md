# Enterprise Problem Plugin Task Checklist

> Root rule: this file coordinates work only. Actual company work belongs inside `channel/`, `musinsa/`, or `kakaopay/`.

## 0. Common Baseline

- [ ] Confirm current Git state before dispatching subagents.
- [ ] Confirm `channel/`, `musinsa/`, and `kakaopay/` are treated as independent project roots.
- [ ] Inspect each folder's `log-hooks` setup.
- [ ] Verify logs from `channel/` work are written to `channel/logs/`.
- [ ] Verify logs from `musinsa/` work are written to `musinsa/logs/`.
- [ ] Verify logs from `kakaopay/` work are written to `kakaopay/logs/`.
- [ ] Confirm submitted logs are full original logs, not slimmed or post-processed logs.
- [ ] If the hook writes filtered logs, stop company work and fix the logging plan first.
- [ ] Confirm each company will produce a separate `submission.zip`.
- [ ] Confirm `submission.zip` root layout: `src/`, `README.md`, `logs/`.

## 1. Shared Reference Research

- [ ] Review Codex official plugin structure requirements.
- [ ] Review Codex official skill authoring requirements.
- [ ] Review installed plugin examples for manifest and skill layout.
- [ ] Review GitHub examples of Codex plugins, skills, or MCP servers.
- [ ] Record reference links used for implementation patterns.
- [ ] Check licenses before copying any code or substantial prose.
- [ ] Prefer original implementation over code copying.
- [ ] Identify arXiv search terms for each company:
  - Channel Talk: RAG customer support, conversational agent evaluation, support automation.
  - Musinsa: fashion recommendation, multimodal product understanding, trend detection, personalization.
  - Kakao Pay Securities: financial document summarization, explainable AI finance, hallucination mitigation, risk disclosure.

## 2. Channel Talk Tasks

### 2.1 Video Analysis

- [ ] Watch or transcribe <https://www.youtube.com/watch?v=5iRf37Z8Wd4>.
- [ ] Extract claims about AI agents, e-commerce support, problem-solving depth, and talent density.
- [ ] Separate direct video claims from inferred project ideas.
- [ ] Save analysis notes inside `channel/`.

### 2.2 Trusted Public Search

- [ ] Find at least one Channel Talk official source about customer support, AI, CX, or e-commerce.
- [ ] Find at least one trustworthy supporting source about e-commerce support automation or CX operations.
- [ ] Reject sources that are comments, unsourced blogs, or unverifiable summaries.
- [ ] Save source list inside `channel/`.

### 2.3 Evidence Map

- [ ] Create a claim-to-source map inside `channel/`.
- [ ] Include columns: claim, source type, source link, reliability tier, plugin implication.
- [ ] Confirm every core problem claim has an official or trustworthy supporting source.

### 2.4 Technical References

- [ ] Find at least one arXiv or academic reference on RAG, AI agents, support automation, or answer quality evaluation.
- [ ] Find at least one GitHub/Codex/plugin reference for skill structure or evaluation pattern.
- [ ] Mark these as method references, not company problem proof.

### 2.5 Problem Definition

- [ ] Define the user: e-commerce CX lead, support operations manager, or Channel Talk implementation owner.
- [ ] Define the situation: repeated support inquiries, policy/FAQ updates, automation planning, answer quality review.
- [ ] Define the problem in one paragraph with evidence links.
- [ ] Draft the answer to: "Why was this problem selected?"

### 2.6 Plugin Concept

- [ ] Limit the plugin to one core workflow.
- [ ] Define input: FAQ, policy text, sample inquiry list, or support notes.
- [ ] Define output: inquiry taxonomy, automation candidates, answer-quality risks, next-action plan.
- [ ] Define the skill name and plugin name.
- [ ] Define a sample prompt and expected output.

### 2.7 Design, Implementation, Verification

- [ ] Design `channel/src/.codex-plugin/plugin.json`.
- [ ] Design `channel/src/skills/<name>/SKILL.md`.
- [ ] Draft `channel/README.md` around the five required answers.
- [ ] Implement the minimal plugin.
- [ ] Verify the skill with sample support inputs.
- [ ] Verify evidence, README, plugin behavior, and logs are consistent.
- [ ] Package `channel/submission.zip` with `src/`, `README.md`, `logs/` at the zip root.

## 3. Musinsa Tasks

### 3.1 Video Analysis

- [ ] Watch or transcribe <https://www.youtube.com/watch?v=OLAWeIuiD5Y>.
- [ ] Extract claims about one-core multi-platform, fragmented data, fashion domain complexity, and business impact.
- [ ] Separate direct video claims from inferred project ideas.
- [ ] Save analysis notes inside `musinsa/`.

### 3.2 Trusted Public Search

- [ ] Find at least one Musinsa official source about platform strategy, brands, data, AI, search, recommendation, or commerce operations.
- [ ] Find at least one trustworthy supporting source about fashion commerce, trend detection, search, recommendation, or data integration.
- [ ] Reject sources that are comments, unsourced blogs, or unverifiable summaries.
- [ ] Save source list inside `musinsa/`.

### 3.3 Evidence Map

- [ ] Create a claim-to-source map inside `musinsa/`.
- [ ] Include columns: claim, source type, source link, reliability tier, plugin implication.
- [ ] Confirm every core problem claim has an official or trustworthy supporting source.

### 3.4 Technical References

- [ ] Find at least one arXiv or academic reference on fashion recommendation, multimodal product understanding, trend detection, or personalization.
- [ ] Find at least one GitHub/Codex/plugin reference for skill structure or decision-support output.
- [ ] Mark these as method references, not company problem proof.

### 3.5 Problem Definition

- [ ] Define the user: fashion MD, brand operator, platform strategy operator, or data operator.
- [ ] Define the situation: fragmented brand/product/trend inputs and unclear merchandising decisions.
- [ ] Define the problem in one paragraph with evidence links.
- [ ] Draft the answer to: "Why was this problem selected?"

### 3.6 Plugin Concept

- [ ] Limit the plugin to one core workflow.
- [ ] Define input: brand notes, product data excerpts, trend notes, platform goals.
- [ ] Define output: structured MD questions, evidence-backed hypotheses, decision options, risk notes.
- [ ] Define the skill name and plugin name.
- [ ] Define a sample prompt and expected output.

### 3.7 Design, Implementation, Verification

- [ ] Design `musinsa/src/.codex-plugin/plugin.json`.
- [ ] Design `musinsa/src/skills/<name>/SKILL.md`.
- [ ] Draft `musinsa/README.md` around the five required answers.
- [ ] Implement the minimal plugin.
- [ ] Verify the skill with sample fashion commerce inputs.
- [ ] Verify evidence, README, plugin behavior, and logs are consistent.
- [ ] Package `musinsa/submission.zip` with `src/`, `README.md`, `logs/` at the zip root.

## 4. Kakao Pay Securities Tasks

### 4.1 Video Analysis

- [ ] Watch or transcribe <https://www.youtube.com/watch?v=aBuoojGjyf4>.
- [ ] Extract claims about beginner investors, AI consultation, decision support, logical problem solving, and solver talent.
- [ ] Separate direct video claims from inferred project ideas.
- [ ] Save analysis notes inside `kakaopay/`.

### 4.2 Trusted Public Search

- [ ] Find at least one Kakao Pay Securities official source about beginner investing, investor education, AI support, product explanation, or customer support.
- [ ] Find at least one trustworthy supporting source about financial consumer understanding, investor education, explainable finance AI, or risk disclosure.
- [ ] Reject sources that are comments, unsourced blogs, or unverifiable summaries.
- [ ] Save source list inside `kakaopay/`.

### 4.3 Evidence Map

- [ ] Create a claim-to-source map inside `kakaopay/`.
- [ ] Include columns: claim, source type, source link, reliability tier, plugin implication.
- [ ] Confirm every core problem claim has an official or trustworthy supporting source.

### 4.4 Technical References

- [ ] Find at least one arXiv or academic reference on financial document summarization, explainable AI, hallucination mitigation, or risk disclosure.
- [ ] Find at least one GitHub/Codex/plugin reference for safe explanation or checklist-style skill output.
- [ ] Mark these as method references, not company problem proof.

### 4.5 Problem Definition

- [ ] Define the user: investor education operator, customer support operator, content operator, or research support worker.
- [ ] Define the situation: explaining investment/product information and risk to beginner investors.
- [ ] Define the problem in one paragraph with evidence links.
- [ ] Draft the answer to: "Why was this problem selected?"

### 4.6 Plugin Concept

- [ ] Limit the plugin to one core workflow.
- [ ] Define input: public investment/product/research text.
- [ ] Define output: plain-language explanation, risk checklist, uncertainty notes, support-answer draft.
- [ ] Explicitly exclude buy/sell/hold recommendations, target prices, timing, and personalized allocation.
- [ ] Define the skill name and plugin name.
- [ ] Define a sample prompt and expected output.

### 4.7 Design, Implementation, Verification

- [ ] Design `kakaopay/src/.codex-plugin/plugin.json`.
- [ ] Design `kakaopay/src/skills/<name>/SKILL.md`.
- [ ] Draft `kakaopay/README.md` around the five required answers.
- [ ] Include non-investment-advice language in `kakaopay/README.md` and skill behavior.
- [ ] Implement the minimal plugin.
- [ ] Verify the skill with sample finance explanation inputs.
- [ ] Verify outputs avoid investment advice and include risk/uncertainty notes.
- [ ] Verify evidence, README, plugin behavior, and logs are consistent.
- [ ] Package `kakaopay/submission.zip` with `src/`, `README.md`, `logs/` at the zip root.

## 5. Final Cross-Project Review

- [ ] Confirm each company has a separate plugin and `submission.zip`.
- [ ] Confirm no company folder uses another folder's logs.
- [ ] Confirm logs are original and unedited.
- [ ] Confirm every README answers all five required questions.
- [ ] Confirm every problem definition has trusted public evidence.
- [ ] Confirm arXiv/GitHub/plugin references are not misused as company problem proof.
- [ ] Confirm each plugin is one narrow core workflow.
- [ ] Confirm `kakaopay/` does not provide investment advice.
- [ ] Confirm all zip files have the required root layout.
- [ ] Confirm final Git status and commit only intentional files.
