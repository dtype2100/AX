# Musinsa MD Brief

## What is the plugin, who uses it, and in what situation?

`musinsa-md-brief` is a skill-only Codex plugin for a Musinsa fashion MD, brand operator, or platform strategy/data operator. It is used when the user has partial brand, product, trend, customer, season, campaign, search, or transaction snippets and needs a concise merchandising decision brief.

## Why was this problem selected?

Public Musinsa materials emphasize partner-brand growth, customer style discovery, AI-assisted trend curation, and conversational product discovery. The problem selected from `research.md` is the planning gap before recommendation or promotion work: messy commerce signals need to become clear facts, missing inputs, MD questions, hypotheses, decision options, and risks.

Evidence used:

- Musinsa corporate site: partner-brand growth and customer style discovery, https://corp.musinsa.com/ko/
- Musinsa Newsroom, AI Trend Curation, 2026-06-03, https://newsroom.musinsa.com/newsroom-menu/2026-0603
- Musinsa Newsroom, ChatGPT Musinsa app, 2026-06-09, https://newsroom.musinsa.com/newsroom-menu/2026-0609-01
- Musinsa Newsroom trend/metric examples, vacation accessories and 29CM satin skirt demand, 2026-07-06 and 2026-07-02, https://newsroom.musinsa.com/newsroom-menu/2026-0706 and https://newsroom.musinsa.com/newsroom-menu/2026-0702
- Banerjee et al., "Recommendation of Compatible Outfits Conditioned on Style", arXiv, 2022, https://arxiv.org/abs/2203.16161

## How does the plugin work?

The plugin exposes one skill at `src/skills/musinsa-md-brief/SKILL.md`. When invoked with brand/product/trend/metric snippets, it returns:

- facts
- missing inputs
- MD questions
- hypotheses
- decision options
- brand and customer risks
- verification checks

It does not use an MCP server or live APIs. It works from user-supplied snippets and cited public evidence only.

## How was AI used?

AI was used to read the Musinsa brief, checklist, and research notes, then encode the researched workflow into a reusable Codex skill. The skill uses AI to structure ambiguous merchandising inputs, separate facts from hypotheses, and surface practical checks before a human MD or strategy operator acts.

## How was the plugin verified?

Verification for this stage:

- confirmed the active working root is `/Users/jinlee/ax_herkerton/musinsa`
- confirmed `.codex/hooks.json`, `log-hooks/tools/save_log.py`, and `logs/codex/` exist
- checked local Codex plugin manifest guidance from `plugin-creator`
- kept the plugin skill-only with `src/.codex-plugin/plugin.json` and `src/skills/musinsa-md-brief/SKILL.md`
- aligned the README, plugin behavior, and evidence claims with `research.md`
- dry-checked the skill against the public Musinsa vacation accessories and satin skirt trend examples from `research.md`

`submission.zip` has not been created yet.
