# Channel Talk Project Checklist

## 0. Baseline

- [x] Treat `channel/` as the Channel Talk project root.
- [x] Confirm `.codex/hooks.json` is active for new work.
- [x] Confirm logs are copied verbatim to `logs/`.
- [x] Read `brief.md`.
- [x] Confirm the active session working root is `channel/`.
- [x] Confirm root orchestration logs are not copied into `logs/`.
- [x] Stop if logs are filtered, missing, or written elsewhere.
- [x] Exclude any failed, unlogged, mixed, or wrong-folder session from submission logs.

## 1. Research

- [ ] Analyze <https://www.youtube.com/watch?v=5iRf37Z8Wd4>.
- [x] Find one Channel Talk official source about support, AI, CX, or e-commerce.
- [x] Find one trustworthy supporting source about support automation or CX operations.
- [x] Review one arXiv or academic method reference.
- [x] Review one GitHub/Codex/plugin structure reference.
- [x] Create an evidence map with claim, source, reliability tier, and plugin implication.

## 2. Problem And Plugin

- [x] Define the target user.
- [x] Define the support situation and public evidence.
- [x] Write the problem statement and why it was selected.
- [x] Define one core workflow: FAQ/policy/support notes to taxonomy, automation candidates, quality risks, and next actions.
- [x] Define plugin name, skill name, sample prompt, and expected output.

## 3. Build And Verify

- [x] Create `channel/src/.codex-plugin/plugin.json`.
- [x] Create `channel/src/skills/<name>/SKILL.md`.
- [x] Draft `channel/README.md` with the five required answers.
- [x] Verify the skill with sample support inputs.
- [x] Verify README, evidence, behavior, and logs are consistent.
- [x] Package `channel/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.
