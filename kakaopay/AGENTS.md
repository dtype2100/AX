# Kakao Pay Securities Agent Rules

## Project Boundary

- Treat `kakaopay/` as the project root for the Kakao Pay Securities submission.
- Do not edit `channel/` or `musinsa/` from this project.
- Follow the root `AGENTS.md`, then apply this file's stricter folder-specific rules.

## Workflow

- Use `kakaopay/checklist.md` as the task checklist.
- Solve one public, verifiable Kakao Pay Securities problem with one narrow Codex plugin workflow.
- Keep research notes, evidence maps, README content, plugin behavior, logs, and final answers consistent.

## Submission Layout

- Prepare the final `kakaopay/submission.zip` so its zip root contains:
  - `src/`
  - `README.md`
  - `logs/`
- Put plugin source under `kakaopay/src/`.
- `kakaopay/src/.codex-plugin/plugin.json` is required.
- Prefer one skill at `kakaopay/src/skills/<name>/SKILL.md`.

## Evidence And References

- Use trusted public evidence for problem claims.
- Prefer Kakao Pay Securities official sources and reputable supporting sources.
- Use arXiv, GitHub, Codex docs, and existing plugins only as method or implementation references.
- Do not use private information, unsourced numbers, comments, or AI summaries as standalone evidence.

## Finance Safety

- Do not provide buy, sell, hold, target price, market timing, or personalized allocation recommendations.
- Keep outputs educational, explanatory, and support-oriented.
- Include non-investment-advice language in the README and plugin behavior.

## Logging

- Use `kakaopay/.codex/hooks.json` as the active Codex hook entrypoint.
- Keep the hook script under `kakaopay/log-hooks/`.
- Before substantial work starts, verify logs are written to `kakaopay/logs/`.
- Submitted logs must be original and unedited.
- Do not copy logs from another company folder.
