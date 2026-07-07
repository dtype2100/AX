# Agent Operating Rules

## Root Workspace

- Use the repository root only for orchestration, coordination, review, and Git operations.
- Do not perform product-specific implementation work directly in the repository root.
- Keep root-level changes limited to shared coordination files unless the user explicitly requests otherwise.

## Work Folders

- Treat `channel/`, `kakaopay/`, and `musinsa/` as separate work areas.
- Run each folder's work independently from the others.
- Do not mix files, logs, or implementation details between these folders unless the user explicitly requests cross-folder coordination.

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
