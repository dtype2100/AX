# Musinsa Project Checklist

## 0. Baseline

- [x] Treat `musinsa/` as the Musinsa project root.
- [x] Confirm `.codex/hooks.json` is active for new work.
- [x] Confirm logs are copied verbatim to `logs/`.
- [x] Read `brief.md`.
- [x] Confirm the active session working root is `musinsa/`.
- [x] Confirm root orchestration logs are not copied into `logs/`.
- [x] Stop if logs are filtered, missing, or written elsewhere.
- [x] Exclude any failed, unlogged, mixed, or wrong-folder session from submission logs.

## 1. Research

- [x] Analyze <https://www.youtube.com/watch?v=OLAWeIuiD5Y>.
- [x] Find one Musinsa official source about platform strategy, brands, data, AI, search, or recommendation.
- [x] Find one trustworthy supporting source about fashion commerce, trend detection, recommendation, or data integration.
- [x] Review one arXiv or academic method reference.
- [x] Review one GitHub/Codex/plugin structure reference.
- [x] Create an evidence map with claim, source, reliability tier, and plugin implication.

## 2. Problem And Plugin

- [x] Define the target user.
- [x] Define the merchandising/data situation and public evidence.
- [x] Write the problem statement and why it was selected.
- [x] Define one core workflow: brand/product/trend inputs to MD questions, hypotheses, decision options, and risk notes.
- [x] Define plugin name, skill name, sample prompt, and expected output.

## 3. Build And Verify

- [x] Create `musinsa/src/.codex-plugin/plugin.json`.
- [x] Create `musinsa/src/skills/<name>/SKILL.md`.
- [x] Draft `musinsa/README.md` with the five required answers.
- [x] Verify the skill with sample fashion commerce inputs.
- [x] Verify README, evidence, behavior, and logs are consistent.
- [x] Package `musinsa/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.
