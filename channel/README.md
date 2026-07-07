# Channel ALF Planner

## What is the plugin, who uses it, and in what situation?

Channel ALF Planner is a skill-only Codex plugin for e-commerce CX leads, support operations managers, and Channel Talk implementation owners preparing an ALF setup. The user pastes FAQ, policy, product, support-note, and optional anonymized inquiry text; the skill returns inquiry taxonomy, FAQ gaps, ALF Rule candidates, ALF Task candidates, answer-quality risks, escalation triggers, and next setup actions.

## Why was this problem selected?

Channel Talk's public AI documentation centers on reducing repetitive inquiries so teams can focus on important work. Its FAQ guide says ALF can answer from registered FAQ content and recommends FAQ topics from open chats. Its Rule, Knowledge, Task, and Analytics guides show the setup work spans structured knowledge, rules, automated tasks, tags, routing, and continuous measurement.

That makes pre-automation planning the narrow public problem: support teams need to decide what to add to FAQ/Knowledge, what to automate with ALF Rules or Tasks, and what should remain human-reviewed. The research notes cite the Channel Talk AI, FAQ, Rule, Knowledge, Task, Analytics, homepage, and verified AX video context, plus supporting CX and human-AI support references.

## How does the plugin work?

The plugin contributes one skill: `channel-alf-planner`. When invoked, Codex asks for pasted source text if needed, rejects private customer data, normalizes messy inquiries into canonical customer questions, groups them into a taxonomy, and outputs the required planning tables:

- Inquiry taxonomy
- FAQ gaps
- ALF Rule candidates
- ALF Task candidates
- Answer-quality risks
- Escalation triggers
- Next Channel Talk setup actions

It does not call Channel Talk APIs, create workflows directly, or require an MCP server.

## How was AI used?

AI is used as a planning assistant over user-provided support material. It reads unstructured text, reformulates customer messages into concise questions, groups repeated themes, and drafts setup recommendations while preserving uncertainty and escalation notes. The skill instructs Codex to say "not enough evidence" instead of inventing missing policy or integration details.

## How was the plugin verified?

This logged pass verified the Channel-only working root, hook configuration, existing `logs/codex/` files, plugin manifest JSON, skill frontmatter, requested source layout, and consistency between `research.md`, the README, and the skill output contract. The skill is intentionally text-only, so the synthetic-input check focused on whether the instructions cover shipping, cancellation, exchange/refund, stock, payment, damaged-item, and escalation cases with the required output sections. `submission.zip` was recreated with only `src/`, `README.md`, and `logs/` at the zip root.

## Evidence

- Channel Talk AI category: https://docs.channel.io/help/en/categories/AI-d5340000
- Channel Talk FAQ guide: https://docs.channel.io/help/en/articles/FAQ--db21218c
- Channel Talk Rule guide: https://docs.channel.io/help/en/articles/Rule-b43e19a1
- Channel Talk Knowledge guide: https://docs.channel.io/help/en/articles/Knowledge--803f6ac9
- Channel Talk Task guide: https://docs.channel.io/help/en/articles/Task--2a16be8b
- Channel Talk Chats analytics guide: https://docs.channel.io/help/en/articles/analytics-chats-10d6b120
- Channel Talk homepage: https://channel.io/us
- Channel Talk AX video context: https://www.youtube.com/watch?v=5iRf37Z8Wd4
- Vogue Business CX automation context: https://www.voguebusiness.com/technology/cx-customer-service-ai-zendesk-kustomer-powerfront
- Human-AI customer support method reference: https://arxiv.org/abs/2301.12158
- E-commerce message-to-question method reference: https://arxiv.org/abs/2401.09785
