#!/usr/bin/env python3
"""Stop-hook helper: saves the AI chat transcript into the submission's logs/ folder.

Invoked automatically by the Claude Code / Codex Stop hook after each turn.
Output: logs/<tool>/<session_id>.jsonl  (tool = claude-code | codex).
You do not need to run or edit this file.
"""
import argparse
import json
import os
import shutil
import sys


def main() -> int:
    # Never write to stdout — Codex parses Stop-hook stdout as a decision.
    # Always exit 0 so a logging failure never blocks the participant's session.
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", required=True, choices=["claude-code", "codex"])
    args = parser.parse_args()

    try:
        payload = json.load(sys.stdin)
    except Exception as exc:  # noqa: BLE001 - non-fatal
        print(f"save_log: failed to parse stdin JSON: {exc}", file=sys.stderr)
        return 0

    transcript_path = payload.get("transcript_path")
    cwd = payload.get("cwd") or os.getcwd()
    session_id = payload.get("session_id") or "session"

    if not transcript_path or not os.path.isfile(transcript_path):
        print(
            f"save_log: transcript_path missing or not a file: {transcript_path!r}",
            file=sys.stderr,
        )
        return 0

    safe_session = os.path.basename(str(session_id))
    if safe_session in ("", ".", ".."):
        safe_session = "session"
    dest_dir = os.path.join(cwd, "logs", args.tool)
    dest = os.path.join(dest_dir, f"{safe_session}.jsonl")

    # Submission logs must remain original and unedited. Copy the transcript verbatim.
    try:
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copyfile(transcript_path, dest)
    except Exception as exc:  # noqa: BLE001 - non-fatal
        print(f"save_log: copy failed: {exc}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
