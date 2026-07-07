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
- Subagents must use only their assigned folder's `log-hooks/` setup for logging.

## Logging Hooks

- Each work folder owns its own `log-hooks/` directory:
  - `channel/log-hooks/`
  - `kakaopay/log-hooks/`
  - `musinsa/log-hooks/`
- When running work for a specific folder, use that folder's hook setup so logs are written separately for that work area.
- Logs from one folder must not be reused as logs for another folder.
- The repository root should not own a shared `log-hooks/` directory.
- Before substantial work starts in a folder, verify that the folder's hook setup writes logs to that folder's own `logs/` directory.
- If the hook setup does not write to the correct folder-level `logs/`, stop and fix the setup before doing project work.

## Log Integrity

- Preserve AI conversation logs exactly as required for submission.
- Do not edit, excerpt, delete, rewrite, or post-process submitted logs after the fact.
- Do not copy logs between work folders.
- Do not paste API keys, passwords, tokens, or other secrets into chats because logs are submitted as-is.

## Evidence Rules

- Use only public, AI-verifiable sources as evidence for the selected problem.
- Do not rely on private company information, unverifiable personal experience, or uncited numbers.
- Keep evidence notes close to the relevant folder's README or research materials.
- The README and the five required answers must cite or clearly point to the same public evidence used by the plugin.

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
