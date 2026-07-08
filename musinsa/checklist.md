# Musinsa Project Checklist

## 0. Baseline

- [x] Treat `musinsa/` as the Musinsa project root.
- [x] Confirm `.codex/hooks.json` is active for new work.
- [x] Confirm logs are copied verbatim to `logs/`.
- [x] Read `brief.md`.
- [x] Confirm the active session working root is `musinsa/`.
- [x] Confirm root orchestration logs are not copied into `logs/`.
- [x] Stop if logs are filtered, missing, or written elsewhere.
- [x] Exclude any failed, unlogged, mixed, or wrong-folder session from submission logs.

## 1. Research

- [x] Analyze <https://www.youtube.com/watch?v=OLAWeIuiD5Y>.
- [x] Find one Musinsa official source about platform strategy, brands, data, AI, search, or recommendation.
- [x] Find one trustworthy supporting source about fashion commerce, trend detection, recommendation, or data integration.
- [x] Review one arXiv or academic method reference.
- [x] Review one GitHub/Codex/plugin structure reference.
- [x] Create an evidence map with claim, source, reliability tier, and plugin implication.

## 2. Problem And Plugin

- [x] Define the target user.
- [x] Refine target user to Musinsa global-fashion category growth MD.
- [x] Confirm role-fit rationale: global-fashion MD is stronger than PB/women or vertical sports unless narrower workflows are added.
- [x] Define the merchandising/data situation and public evidence.
- [x] Write the problem statement and why it was selected.
- [x] Define one core workflow: brand/product/trend inputs to MD questions, hypotheses, decision options, and risk notes.
- [x] Confirm input expectations include category, brand, season, SKU depth, sales/transaction, profit or margin, inventory, price/promotion, customer segment, and exposure plan.
- [x] Confirm output includes Business Impact, Portfolio/SKU Considerations, and Pricing And Promotion Risks.
- [x] Confirm missing revenue, profit, inventory, pricing, promotion, SKU, and partnership constraints are visible.
- [x] Confirm the plugin does not claim to be a recommendation engine, pricing optimizer, inventory optimizer, or internal-data tool.
- [x] Define plugin name, skill name, sample prompt, and expected output.

## 3. Build And Verify

- [x] Create `musinsa/src/.codex-plugin/plugin.json`.
- [x] Create `musinsa/src/skills/<name>/SKILL.md`.
- [x] Draft `musinsa/README.md` with the five required answers.
- [x] Confirm README explicitly answers: what/who/situation, why selected, how it works, how AI was used, and how verified.
- [x] Confirm README covers Role Fit Matrix, Evidence Matrix, and Before / After.
- [x] Verify the skill with sample fashion commerce inputs.
- [x] Verify functional sample includes business impact, SKU/portfolio, pricing/promotion, brand/customer risk, and verification checks.
- [x] Add failure/refusal test: if asked for a numeric sales forecast without internal or cited data, do not invent numbers; turn it into missing inputs and verification checks.
- [x] Verify README, evidence, behavior, and logs are consistent.
- [x] Verify `logs/` exists and contains original folder-local AI conversation logs.
- [x] Package `musinsa/submission.zip` with `src/`, `README.md`, and `logs/` at zip root.

## 4. Final Gates

- [x] Run `python3 -m json.tool src/.codex-plugin/plugin.json`.
- [x] Run `test -f README.md`.
- [x] Run `test -d logs`.
- [x] Run `find src -maxdepth 4 -type f | sort`.
- [ ] Confirm final zip root contains `src/`, `README.md`, and `logs/`.
