# Musinsa Agent Rules

## Project Boundary

- Treat `musinsa/` as the project root for the Musinsa submission.
- Do not edit `channel/` or `kakaopay/` from this project.
- Follow the root `AGENTS.md`, then apply this file's stricter folder-specific rules.

## Workflow

- Use `musinsa/checklist.md` as the task checklist.
- Read `musinsa/brief.md` before research, design, or implementation.
- Solve one public, verifiable Musinsa problem with one narrow Codex plugin workflow.
- Keep research notes, evidence maps, README content, plugin behavior, logs, and final answers consistent.

## Submission Layout

- Prepare the final `musinsa/submission.zip` so its zip root contains:
  - `src/`
  - `README.md`
  - `logs/`
- Put plugin source under `musinsa/src/`.
- `musinsa/src/.codex-plugin/plugin.json` is required.
- Prefer one skill at `musinsa/src/skills/<name>/SKILL.md`.

## Evidence And References

- Use trusted public evidence for problem claims.
- Prefer Musinsa official sources and reputable supporting sources.
- Use arXiv, GitHub, Codex docs, and existing plugins only as method or implementation references.
- Do not use private information, unsourced numbers, comments, or AI summaries as standalone evidence.

## Logging

- Use `musinsa/.codex/hooks.json` as the active Codex hook entrypoint.
- Keep the hook script under `musinsa/log-hooks/`.
- Prove the active working root is `musinsa/` before company work starts.
- Before substantial work starts, verify logs are written to `musinsa/logs/`.
- Submitted logs must be original and unedited.
- Do not copy logs from another company folder.
- Do not copy root orchestration logs into `musinsa/logs/`.
- Stop and restart from a clean Musinsa session if logs are missing, mixed, copied, filtered, or written outside `musinsa/`.
