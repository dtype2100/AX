# Agent Operating Rules

## Root Workspace

- Use the repository root only for orchestration, coordination, review, and Git operations.
- Do not perform product-specific implementation work directly in the repository root.
- Keep root-level changes limited to shared coordination files unless the user explicitly requests otherwise.

## Work Folders

- Treat `channel/`, `kakaopay/`, and `musinsa/` as separate work areas.
- Run each folder's work independently from the others.
- Do not mix files, logs, or implementation details between these folders unless the user explicitly requests cross-folder coordination.
- Treat each work folder as a separate company-specific plugin submission.
- Do not combine multiple companies, industries, or customer problems into one submission.

## Assignment Contract

- Each folder must solve one public, verifiable problem for one selected company, its industry, or its customers.
- Each folder must produce its own `submission.zip`.
- The final zip must contain `src/`, `README.md`, and `logs/` at the zip root.
- The final zip must exclude orchestration-only or build-only files such as `.codex/`, `log-hooks/`, `brief.md`, `research.md`, `checklist.md`, `AGENTS.md`, and `submission.zip` itself unless the assignment explicitly allows them.
- The folder name itself, such as `channel/`, `kakaopay/`, or `musinsa/`, must not appear as the top-level directory inside `submission.zip`.
- Keep each folder's plugin, README, logs, research notes, and answer materials consistent with each other.

## Required Submission Layout

Each work folder must be prepared so its `submission.zip` has this structure:

```text
submission.zip
├── src/
│   ├── .codex-plugin/plugin.json
│   ├── skills/<name>/SKILL.md
│   ├── .mcp.json
│   └── other runtime code and configuration files
├── README.md
└── logs/
```

- `src/.codex-plugin/plugin.json` is required.
- At least one working plugin component is required in addition to `plugin.json`.
- Prefer `src/skills/<name>/SKILL.md` as the default working plugin component.
- Use `src/.mcp.json` only when the plugin needs an MCP server.
- Put executable code and supporting configuration under `src/`.
- Put the final user-facing explanation at the folder-level `README.md`.
- Put AI conversation logs under the folder-level `logs/`.

## Subagent Execution

- This root chat acts only as the orchestrator.
- Assign actual development work inside `channel/`, `kakaopay/`, and `musinsa/` to separate subagents.
- Each subagent should treat its assigned folder as an independent project root.
- Subagents must stay within their assigned folder unless the orchestrator explicitly coordinates a cross-folder change.
- Subagents must use only their assigned folder's `.codex/hooks.json` and `log-hooks/` setup for logging.
- The orchestrator must pass root-level decisions into each company subagent's first message instead of copying root logs into company logs.
- Use `subagent-prompts.md` as the canonical first-message template for company subagents.
- A subagent session counts as company submission work only after it proves it is operating from the assigned company folder and can write logs there.
- If the subagent tool cannot prove the assigned folder is the active working root, use a separate Codex session/thread/window started from that company folder before doing company-specific work.

## Subagent Launch Template

Each company subagent must receive a first message with these facts:

- Assigned company and folder.
- Absolute working root path.
- Folder-only edit boundary.
- The matching `brief.md` file to read first.
- The requirement to verify `.codex/hooks.json`, `log-hooks/tools/save_log.py`, and `logs/codex/` before research or implementation.
- Failure policy: stop if logs are missing, filtered, mixed, copied, or written outside the assigned folder.
- Reporting format: changed files, evidence used, verification performed, and unresolved risks.

## Logging Hooks

- Each work folder owns its own `log-hooks/` directory:
  - `channel/log-hooks/`
  - `kakaopay/log-hooks/`
  - `musinsa/log-hooks/`
- Each work folder must also own the active Codex hook file:
  - `channel/.codex/hooks.json`
  - `kakaopay/.codex/hooks.json`
  - `musinsa/.codex/hooks.json`
- When running work for a specific folder, use that folder's hook setup so logs are written separately for that work area.
- Logs from one folder must not be reused as logs for another folder.
- The repository root should not own a shared `log-hooks/` directory.
- Before substantial work starts in a folder, verify that the folder's hook setup writes logs to that folder's own `logs/` directory.
- If the hook setup does not write to the correct folder-level `logs/`, stop and fix the setup before doing project work.

## Log Integrity

- Preserve AI conversation logs exactly as required for submission.
- Do not edit, excerpt, delete, rewrite, or post-process submitted logs after the fact.
- Do not copy logs between work folders.
- Do not copy root orchestration logs into company submission logs.
- Do not use a failed, unlogged, mixed, or wrong-folder session as a submitted company log.
- Do not paste API keys, passwords, tokens, or other secrets into chats because logs are submitted as-is.

## Failure Policy

- If logs are not created, stop the company work immediately and restart from a correctly configured folder session.
- If logs are written to the wrong folder, do not submit those logs and restart from the correct folder.
- If one session mixes multiple companies, exclude that session from company submission logs and redo the affected work in separate folder sessions.
- If a secret, token, password, or private company information enters a log, treat the session as unsafe for submission and redo the work without editing the log.
- If public evidence cannot be found for a problem claim, do not finalize that problem definition.
- If a plugin does not run as a Codex plugin, do not create `submission.zip`; reduce to the simplest working skill-based plugin first.

## Evidence Rules

- Use only public, AI-verifiable sources as evidence for the selected problem.
- Do not rely on private company information, unverifiable personal experience, or uncited numbers.
- Treat the provided YouTube videos as project context until a transcript, official page, or otherwise verifiable public text is captured.
- Do not make a final problem claim from a YouTube summary alone; confirm it with official company sources, trusted public sources, academic references, or relevant open-source examples.
- Keep evidence notes close to the relevant folder's README or research materials.
- The README and the five required answers must cite or clearly point to the same public evidence used by the plugin.

## Financial Safety

- In `kakaopay/`, keep the plugin educational and support-oriented.
- Do not produce buy, sell, hold, subscribe, redeem, avoid, target-price, market-timing, guaranteed-return, tax, legal, account-specific, or personalized-allocation advice.
- If a user asks for investment advice, refuse that part and offer plain-language explanation, risk checklist, uncertainty notes, or questions to ask a licensed professional.

## Required Five Answers

Each folder must be able to answer these questions from its own materials:

- What is the plugin, who uses it, and in what situation?
- Why was this problem selected?
- How does the plugin work?
- How was AI used?
- How was the plugin verified?

## Verification Gate

Before a work folder is considered ready for submission, verify:

- `src/.codex-plugin/plugin.json` exists.
- `src/skills/<name>/SKILL.md` or another working plugin component exists.
- The plugin can run as a Codex plugin.
- `README.md` explains the problem, target user, operation, evidence, and verification.
- `logs/` exists and contains the relevant original AI conversation logs for that folder.
- The five required answers are consistent with the plugin, README, logs, and public evidence.
- `submission.zip` contains `src/`, `README.md`, and `logs/` at the zip root.
