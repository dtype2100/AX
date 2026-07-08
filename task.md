# Final Submission Alignment Task Checklist

> Root rule: coordinate only. Company-specific edits belong in `channel/`, `musinsa/`, and `kakaopay/`.

## 0. Root Coordination

- [x] Move work onto a non-master implementation branch.
- [x] Replace root `plan.md` with the final integrated improvement plan.
- [x] Keep this checklist updated as implementation proceeds.
- [x] Review final diffs from all company folders.
- [x] Commit and push after all verification gates pass.

## 1. Channel Talk

- [x] Update `channel/README.md` target user to Channel Talk AX Consultant.
- [x] Keep customer-side CX operations manager as stakeholder, not primary plugin user.
- [x] Add Role Fit Matrix, Evidence Matrix, and Before / After sections.
- [x] Reflect video context: AX, AI agent, essential problem solving, talent density.
- [x] Update `channel/src/skills/channel-alf-planner/SKILL.md` output contract.
- [x] Include Implementation Context, Knowledge Readiness, Response Scenario Candidates, Workflow/API Handoff Candidates, Operator Handoff Notes, and Post-Launch Review.
- [x] Add unsupported-policy failure test summary.
- [x] Update `channel/research.md` with hiring-site role-fit rationale.
- [x] Update `channel/checklist.md` with five-question and verification gates.
- [x] Regenerate `channel/submission.zip`.

## 2. Musinsa

- [x] Update `musinsa/README.md` target user to global-fashion category growth MD.
- [x] Add Role Fit Matrix, Evidence Matrix, and Before / After sections.
- [x] Reflect video context: data fragmentation, one-core multi-platform, business impact.
- [x] Update `musinsa/src/skills/musinsa-md-brief/SKILL.md` input expectations and output contract.
- [x] Include category, brand, season, SKU depth, sales/transaction, profit or margin, inventory, price/promotion, customer segment, and exposure plan.
- [x] Include Business Impact, Portfolio/SKU Considerations, and Pricing And Promotion Risks.
- [x] Add unsupported numeric forecast failure test summary.
- [x] Update `musinsa/research.md` with hiring-site role-fit rationale.
- [x] Update `musinsa/checklist.md` with five-question and verification gates.
- [x] Regenerate `musinsa/submission.zip`.

## 3. Kakao Pay Securities

- [x] Update `kakaopay/README.md` target user to customer-support knowledge / investor-education content operator.
- [x] State that the target user is an inferred function, not a claimed official job title.
- [x] Add Role Fit Matrix, Evidence Matrix, and Before / After sections.
- [x] Reflect video context: Solver, logical explanation, user understanding.
- [x] Update `kakaopay/src/skills/kakaopay-investor-explainer/SKILL.md` privacy guard and output contract.
- [x] Include Fact vs Opinion, Risk Checklist, Uncertainty Notes, Human Review Required, Compliance Review Needed, and Notice.
- [x] Add investment-advice refusal test summary.
- [x] Update `kakaopay/research.md` with hiring-site/culture role-fit rationale.
- [x] Update `kakaopay/checklist.md` with five-question and verification gates.
- [x] Regenerate `kakaopay/submission.zip`.

## 4. Verification Gates

- [x] Run structure checks in all folders.
- [x] Run plugin installation checks in all folders.
- [x] Run functional sample checks in all folders.
- [x] Run failure/refusal checks in all folders.
- [x] Confirm five-question gate is all `Y`.
- [x] Confirm logs are folder-local, original, and not mixed.
- [x] Confirm each `submission.zip` has `src/`, `README.md`, and `logs/` at the zip root.
