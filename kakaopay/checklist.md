# Kakao Pay Securities Project Checklist

## 0. Baseline

- [x] Treat `kakaopay/` as the Kakao Pay Securities project root.
- [x] Confirm `.codex/hooks.json` is active for new work.
- [x] Confirm logs are copied verbatim to `logs/`.
- [x] Read `brief.md`.
- [x] Confirm the active session working root is `kakaopay/`.
- [x] Confirm root orchestration logs are not copied into `logs/`.
- [x] Stop if logs are filtered, missing, or written elsewhere.
- [x] Exclude any failed, unlogged, mixed, or wrong-folder session from submission logs.
- [x] Keep all outputs educational and support-oriented.

## 1. Research

- [x] Analyze <https://www.youtube.com/watch?v=aBuoojGjyf4>.
- [x] Find one Kakao Pay Securities official source about beginner investing, investor education, AI support, product explanation, or customer support.
- [x] Find one trustworthy supporting source about investor education, financial consumer understanding, explainable finance AI, or risk disclosure.
- [x] Review one arXiv or academic method reference.
- [x] Review one GitHub/Codex/plugin structure reference.
- [x] Create an evidence map with claim, source, reliability tier, and plugin implication.

## 2. Problem And Plugin

- [x] Define the target user.
- [x] State the target user as a customer-support knowledge / investor-education content operator and label it as an inferred function, not an official job-title claim.
- [x] Define the beginner-investor explanation situation and public evidence.
- [x] Write the problem statement and why it was selected.
- [x] Define one core workflow: public investment/product/research text to plain-language explanation, risk checklist, uncertainty notes, and support-answer draft.
- [x] Exclude buy/sell/hold recommendations, target prices, timing, and personalized allocation.
- [x] Define plugin name, skill name, sample prompt, and expected output.

## 3. Build And Verify

- [x] Create `kakaopay/src/.codex-plugin/plugin.json`.
- [x] Create `kakaopay/src/skills/<name>/SKILL.md`.
- [x] Draft `kakaopay/README.md` with the five required answers and non-investment-advice notice.
- [x] Add Role Fit Matrix, Evidence Matrix, and Before / After to README.
- [x] Include one functional sample showing source-grounded educational output.
- [x] Verify the skill with sample finance explanation inputs.
- [x] Verify outputs avoid investment advice and include risks/uncertainty.
- [x] Verify refusal coverage for buy/sell/hold, target price, timing, subscription/redemption, tax/legal, account-specific judgment, and personalized allocation.
- [x] Verify privacy guard stops on personal information, account data, resident-registration number, salary, tokens, and secrets.
- [x] Verify README, evidence, behavior, and logs are consistent.
- [x] Verify `logs/` exists and preserves original folder-local conversation logs.
- [x] Package `kakaopay/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.
- [x] Verify zip gate: zip root contains `src/`, `README.md`, and `logs/`, with no top-level `kakaopay/` directory.
