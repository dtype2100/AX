# Channel Talk Project Checklist

## 0. Baseline

- [x] Treat `channel/` as the Channel Talk project root.
- [x] Confirm `channel/.codex/hooks.json` is active for new work.
- [x] Confirm logs are copied verbatim to `channel/logs/`.
- [ ] Stop if logs are filtered, missing, or written elsewhere.

## 1. Research

- [ ] Analyze <https://www.youtube.com/watch?v=5iRf37Z8Wd4>.
- [ ] Find one Channel Talk official source about support, AI, CX, or e-commerce.
- [ ] Find one trustworthy supporting source about support automation or CX operations.
- [ ] Review one arXiv or academic method reference.
- [ ] Review one GitHub/Codex/plugin structure reference.
- [ ] Create an evidence map with claim, source, reliability tier, and plugin implication.

## 2. Problem And Plugin

- [ ] Define the target user.
- [ ] Define the support situation and public evidence.
- [ ] Write the problem statement and why it was selected.
- [ ] Define one core workflow: FAQ/policy/support notes to taxonomy, automation candidates, quality risks, and next actions.
- [ ] Define plugin name, skill name, sample prompt, and expected output.

## 3. Build And Verify

- [ ] Create `channel/src/.codex-plugin/plugin.json`.
- [ ] Create `channel/src/skills/<name>/SKILL.md`.
- [ ] Draft `channel/README.md` with the five required answers.
- [ ] Verify the skill with sample support inputs.
- [ ] Verify README, evidence, behavior, and logs are consistent.
- [ ] Package `channel/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.
