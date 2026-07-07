# Enterprise Problem Plugin Task Checklist

> Root rule: coordinate only. Company work belongs inside `channel/`, `musinsa/`, or `kakaopay/`.

## 0. Hook And Log Baseline

- [x] Confirm `channel/.codex/hooks.json` exists.
- [x] Confirm `musinsa/.codex/hooks.json` exists.
- [x] Confirm `kakaopay/.codex/hooks.json` exists.
- [x] Confirm each hook calls `log-hooks/tools/save_log.py`.
- [x] Confirm each `save_log.py` copies transcripts verbatim.
- [x] Verify `channel/` work writes to `channel/logs/`.
- [x] Verify `musinsa/` work writes to `musinsa/logs/`.
- [x] Verify `kakaopay/` work writes to `kakaopay/logs/`.
- [x] Stop project work if logs are filtered, missing, or written to another folder.

## 1. Shared Research And Reference Setup

- [x] Review Codex plugin and skill docs.
- [x] Review installed marketplace plugin examples for manifest and skill layout.
- [x] Search GitHub for relevant Codex plugin, skill, and MCP examples.
- [x] Record references and license notes.
- [x] Confirm root orchestration logs will not be copied into company logs.
- [x] Prepare the fixed first-message template for company subagents in `subagent-prompts.md`.
- [x] Confirm the fallback rule: if a subagent cannot prove the assigned folder is its working root, restart in a company-folder Codex session.
- [x] Identify arXiv search terms:
  - Channel Talk: RAG customer support, conversational agent evaluation, support automation.
  - Musinsa: fashion recommendation, multimodal product understanding, trend detection.
  - Kakao Pay Securities: financial summarization, explainable AI, hallucination mitigation, risk disclosure.

## 2. Channel Talk

- [x] Read `channel/brief.md` in the Channel Talk session.
- [x] Confirm the Channel Talk session working root is `channel/`.
- [x] Confirm `channel/logs/codex/` receives the Channel Talk session log.
- [ ] Analyze <https://www.youtube.com/watch?v=5iRf37Z8Wd4>.
- [x] Find one Channel Talk official source.
- [x] Find one trustworthy support/CX/e-commerce source.
- [x] Create `channel/` evidence map.
- [x] Review at least one arXiv or academic method reference.
- [x] Review at least one GitHub/Codex/plugin structure reference.
- [x] Define problem, user, situation, and why selected.
- [x] Define one core workflow with input, output, sample prompt, and expected output.
- [x] Design and implement `channel/src/.codex-plugin/plugin.json`.
- [x] Design and implement `channel/src/skills/<name>/SKILL.md`.
- [x] Draft `channel/README.md` around the five required answers.
- [x] Verify skill output and evidence consistency.
- [x] Package `channel/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.

## 3. Musinsa

- [x] Read `musinsa/brief.md` in the Musinsa session.
- [x] Confirm the Musinsa session working root is `musinsa/`.
- [x] Confirm `musinsa/logs/codex/` receives the Musinsa session log.
- [ ] Analyze <https://www.youtube.com/watch?v=OLAWeIuiD5Y>.
- [x] Find one Musinsa official source.
- [x] Find one trustworthy fashion commerce/data/recommendation source.
- [x] Create `musinsa/` evidence map.
- [x] Review at least one arXiv or academic method reference.
- [x] Review at least one GitHub/Codex/plugin structure reference.
- [x] Define problem, user, situation, and why selected.
- [x] Define one core workflow with input, output, sample prompt, and expected output.
- [x] Design and implement `musinsa/src/.codex-plugin/plugin.json`.
- [x] Design and implement `musinsa/src/skills/<name>/SKILL.md`.
- [x] Draft `musinsa/README.md` around the five required answers.
- [x] Verify skill output and evidence consistency.
- [x] Package `musinsa/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.

## 4. Kakao Pay Securities

- [x] Read `kakaopay/brief.md` in the Kakao Pay Securities session.
- [x] Confirm the Kakao Pay Securities session working root is `kakaopay/`.
- [x] Confirm `kakaopay/logs/codex/` receives the Kakao Pay Securities session log.
- [ ] Analyze <https://www.youtube.com/watch?v=aBuoojGjyf4>.
- [x] Find one Kakao Pay Securities official source.
- [x] Find one trustworthy investor education/risk disclosure source.
- [x] Create `kakaopay/` evidence map.
- [x] Review at least one arXiv or academic method reference.
- [x] Review at least one GitHub/Codex/plugin structure reference.
- [x] Define problem, user, situation, and why selected.
- [x] Define one educational support workflow with input, output, sample prompt, and expected output.
- [x] Exclude buy/sell/hold recommendations, target prices, timing, and personalized allocation.
- [x] Design and implement `kakaopay/src/.codex-plugin/plugin.json`.
- [x] Design and implement `kakaopay/src/skills/<name>/SKILL.md`.
- [x] Draft `kakaopay/README.md` around the five required answers and non-investment-advice notice.
- [x] Verify skill output avoids investment advice and includes risks/uncertainty.
- [x] Package `kakaopay/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.

## 5. Final Review

- [x] Confirm every company has a separate plugin and `submission.zip`.
- [x] Confirm no logs are copied between company folders.
- [x] Confirm root orchestration logs are not copied into company logs.
- [x] Confirm failed, unlogged, mixed, or wrong-folder sessions are excluded from submitted logs.
- [x] Confirm logs are original and unedited.
- [x] Confirm every README answers the five required questions.
- [x] Confirm every problem definition has trusted public evidence.
- [x] Confirm arXiv/GitHub/plugin references are not used as company problem proof.
- [x] Confirm each plugin is one narrow core workflow.
- [x] Confirm all zip files have required root layout.
