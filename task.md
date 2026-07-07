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
- [ ] Stop project work if logs are filtered, missing, or written to another folder.

## 1. Shared Research And Reference Setup

- [ ] Review Codex plugin and skill docs.
- [ ] Review installed marketplace plugin examples for manifest and skill layout.
- [ ] Search GitHub for relevant Codex plugin, skill, and MCP examples.
- [ ] Record references and license notes.
- [x] Confirm root orchestration logs will not be copied into company logs.
- [x] Prepare the fixed first-message template for company subagents in `subagent-prompts.md`.
- [x] Confirm the fallback rule: if a subagent cannot prove the assigned folder is its working root, restart in a company-folder Codex session.
- [ ] Identify arXiv search terms:
  - Channel Talk: RAG customer support, conversational agent evaluation, support automation.
  - Musinsa: fashion recommendation, multimodal product understanding, trend detection.
  - Kakao Pay Securities: financial summarization, explainable AI, hallucination mitigation, risk disclosure.

## 2. Channel Talk

- [ ] Read `channel/brief.md` in the Channel Talk session.
- [ ] Confirm the Channel Talk session working root is `channel/`.
- [ ] Confirm `channel/logs/codex/` receives the Channel Talk session log.
- [ ] Analyze <https://www.youtube.com/watch?v=5iRf37Z8Wd4>.
- [ ] Find one Channel Talk official source.
- [ ] Find one trustworthy support/CX/e-commerce source.
- [ ] Create `channel/` evidence map.
- [ ] Review at least one arXiv or academic method reference.
- [ ] Review at least one GitHub/Codex/plugin structure reference.
- [ ] Define problem, user, situation, and why selected.
- [ ] Define one core workflow with input, output, sample prompt, and expected output.
- [ ] Design and implement `channel/src/.codex-plugin/plugin.json`.
- [ ] Design and implement `channel/src/skills/<name>/SKILL.md`.
- [ ] Draft `channel/README.md` around the five required answers.
- [ ] Verify skill output and evidence consistency.
- [ ] Package `channel/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.

## 3. Musinsa

- [ ] Read `musinsa/brief.md` in the Musinsa session.
- [ ] Confirm the Musinsa session working root is `musinsa/`.
- [ ] Confirm `musinsa/logs/codex/` receives the Musinsa session log.
- [ ] Analyze <https://www.youtube.com/watch?v=OLAWeIuiD5Y>.
- [ ] Find one Musinsa official source.
- [ ] Find one trustworthy fashion commerce/data/recommendation source.
- [ ] Create `musinsa/` evidence map.
- [ ] Review at least one arXiv or academic method reference.
- [ ] Review at least one GitHub/Codex/plugin structure reference.
- [ ] Define problem, user, situation, and why selected.
- [ ] Define one core workflow with input, output, sample prompt, and expected output.
- [ ] Design and implement `musinsa/src/.codex-plugin/plugin.json`.
- [ ] Design and implement `musinsa/src/skills/<name>/SKILL.md`.
- [ ] Draft `musinsa/README.md` around the five required answers.
- [ ] Verify skill output and evidence consistency.
- [ ] Package `musinsa/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.

## 4. Kakao Pay Securities

- [ ] Read `kakaopay/brief.md` in the Kakao Pay Securities session.
- [ ] Confirm the Kakao Pay Securities session working root is `kakaopay/`.
- [ ] Confirm `kakaopay/logs/codex/` receives the Kakao Pay Securities session log.
- [ ] Analyze <https://www.youtube.com/watch?v=aBuoojGjyf4>.
- [ ] Find one Kakao Pay Securities official source.
- [ ] Find one trustworthy investor education/risk disclosure source.
- [ ] Create `kakaopay/` evidence map.
- [ ] Review at least one arXiv or academic method reference.
- [ ] Review at least one GitHub/Codex/plugin structure reference.
- [ ] Define problem, user, situation, and why selected.
- [ ] Define one educational support workflow with input, output, sample prompt, and expected output.
- [ ] Exclude buy/sell/hold recommendations, target prices, timing, and personalized allocation.
- [ ] Design and implement `kakaopay/src/.codex-plugin/plugin.json`.
- [ ] Design and implement `kakaopay/src/skills/<name>/SKILL.md`.
- [ ] Draft `kakaopay/README.md` around the five required answers and non-investment-advice notice.
- [ ] Verify skill output avoids investment advice and includes risks/uncertainty.
- [ ] Package `kakaopay/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.

## 5. Final Review

- [ ] Confirm every company has a separate plugin and `submission.zip`.
- [ ] Confirm no logs are copied between company folders.
- [ ] Confirm root orchestration logs are not copied into company logs.
- [ ] Confirm failed, unlogged, mixed, or wrong-folder sessions are excluded from submitted logs.
- [ ] Confirm logs are original and unedited.
- [ ] Confirm every README answers the five required questions.
- [ ] Confirm every problem definition has trusted public evidence.
- [ ] Confirm arXiv/GitHub/plugin references are not used as company problem proof.
- [ ] Confirm each plugin is one narrow core workflow.
- [ ] Confirm all zip files have required root layout.
