# Channel Talk Agent Rules

All relative paths in this file are relative to `channel/`.

## Project Boundary

- Treat `channel/` as the project root for the Channel Talk submission.
- Do not edit `musinsa/` or `kakaopay/` from this project.
- Follow the root `AGENTS.md`, then apply this file's stricter folder-specific rules.

## Workflow

- Use `checklist.md` as the task checklist.
- Read `brief.md` before research, design, or implementation.
- Solve one public, verifiable Channel Talk problem with one narrow Codex plugin workflow.
- Keep research notes, evidence maps, README content, plugin behavior, logs, and final answers consistent.

## Submission Layout

- Prepare the final `submission.zip` so its zip root contains:
  - `src/`
  - `README.md`
  - `logs/`
- Put plugin source under `src/`.
- `src/.codex-plugin/plugin.json` is required.
- Prefer one skill at `src/skills/<name>/SKILL.md`.

## Evidence And References

- Use trusted public evidence for problem claims.
- Prefer Channel Talk official sources and reputable supporting sources.
- Use arXiv, GitHub, Codex docs, and existing plugins only as method or implementation references.
- Do not use private information, unsourced numbers, comments, or AI summaries as standalone evidence.

## Logging

- Use `.codex/hooks.json` as the active Codex hook entrypoint.
- Keep the hook script under `log-hooks/`.
- Prove the active working root is `channel/` before company work starts.
- Before substantial work starts, verify logs are written to `logs/`.
- Submitted logs must be original and unedited.
- Do not copy logs from another company folder.
- Do not copy root orchestration logs into `logs/`.
- Stop and restart from a clean Channel Talk session if logs are missing, mixed, copied, filtered, or written outside `channel/`.
