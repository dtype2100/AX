# Kakao Pay Securities Project Checklist

## 0. Baseline

- [x] Treat `kakaopay/` as the Kakao Pay Securities project root.
- [x] Confirm `.codex/hooks.json` is active for new work.
- [x] Confirm logs are copied verbatim to `logs/`.
- [x] Read `brief.md`.
- [x] Confirm the active session working root is `kakaopay/`.
- [x] Confirm root orchestration logs are not copied into `logs/`.
- [ ] Stop if logs are filtered, missing, or written elsewhere.
- [ ] Exclude any failed, unlogged, mixed, or wrong-folder session from submission logs.
- [x] Keep all outputs educational and support-oriented.

## 1. Research

- [ ] Analyze <https://www.youtube.com/watch?v=aBuoojGjyf4>.
- [x] Find one Kakao Pay Securities official source about beginner investing, investor education, AI support, product explanation, or customer support.
- [x] Find one trustworthy supporting source about investor education, financial consumer understanding, explainable finance AI, or risk disclosure.
- [x] Review one arXiv or academic method reference.
- [x] Review one GitHub/Codex/plugin structure reference.
- [x] Create an evidence map with claim, source, reliability tier, and plugin implication.

## 2. Problem And Plugin

- [x] Define the target user.
- [x] Define the beginner-investor explanation situation and public evidence.
- [ ] Write the problem statement and why it was selected.
- [ ] Define one core workflow: public investment/product/research text to plain-language explanation, risk checklist, uncertainty notes, and support-answer draft.
- [ ] Exclude buy/sell/hold recommendations, target prices, timing, and personalized allocation.
- [ ] Define plugin name, skill name, sample prompt, and expected output.

## 3. Build And Verify

- [ ] Create `kakaopay/src/.codex-plugin/plugin.json`.
- [ ] Create `kakaopay/src/skills/<name>/SKILL.md`.
- [ ] Draft `kakaopay/README.md` with the five required answers and non-investment-advice notice.
- [ ] Verify the skill with sample finance explanation inputs.
- [ ] Verify outputs avoid investment advice and include risks/uncertainty.
- [ ] Verify README, evidence, behavior, and logs are consistent.
- [ ] Package `kakaopay/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.
