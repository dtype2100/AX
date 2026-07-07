# Kakao Pay Investor Explainer

## What is the plugin, who uses it, and in what situation?

Kakao Pay Investor Explainer is a minimal skill-only Codex plugin for Kakao Pay Securities support, education, content, or research-support operators. It turns public investment, product, research, disclosure, FAQ, or support text into beginner-friendly educational material: a plain-language explanation, key terms, risk checklist, uncertainty notes, and a source-grounded support draft.

The plugin is for operator drafting and review. It is not for automated customer advice.

## Why was this problem selected?

Kakao Pay Securities publicly positions its service around accessible investing, including smaller-amount investing, understandable investment news, recurring stock purchase, stock gifting, fractional overseas stocks, and fund products. Its disclosures also say investors have the right to sufficient explanation, should read product documents and terms, and may lose principal on financial investment products.

That creates a narrow, verifiable support problem: public investment text can be hard for beginner investors to understand, and operators need consistent educational explanations that surface risk and uncertainty without turning into recommendations.

Supporting evidence is recorded in `research.md`, including Kakao Pay Securities official material, SEC Investor.gov risk education, and method references for grounded generation.
The verified public video context also supports a narrow AI 상담-assist workflow focused on explainable uncertainty, not personalized investment advice.

## How does the plugin work?

The plugin contains one skill at `src/skills/kakaopay-investor-explainer/SKILL.md`. When triggered, it requires public or user-provided source text and produces:

- Plain-language explanation.
- Key terms.
- Risk checklist.
- Uncertainty notes.
- Source-grounded support draft.
- Non-investment-advice notice.

It refuses or redirects requests for buy, sell, hold, target price, market timing, personalized allocation, tax/legal/account-specific advice, or unsupported claims.

## How was AI used?

AI is used as a drafting assistant. The skill instructs Codex to extract source-supported facts, rewrite them in plain language, identify key terms and risks, and flag missing information for human review. The workflow follows a grounded-generation pattern: use the supplied public source first and avoid filling gaps from model memory.

## How was the plugin verified?

Verification for this stage checked that:

- The active working root was `/Users/jinlee/ax_herkerton/kakaopay`.
- `.codex/hooks.json` calls `log-hooks/tools/save_log.py`, which writes verbatim logs under `logs/codex/` for the active folder.
- `logs/codex/` exists and contains original session logs.
- `src/.codex-plugin/plugin.json` exists.
- `src/skills/kakaopay-investor-explainer/SKILL.md` exists.
- The skill frontmatter uses the required `name` and `description` fields.
- The workflow includes the required finance-safety refusal rules and non-investment-advice notice.
- A sample explanation prompt was checked against the required output sections: plain-language explanation, key terms, risk checklist, uncertainty notes, support draft, and notice.
- A sample advice prompt was checked against the refusal rules for buy/sell/hold, target price, market timing, and personalized allocation requests.

`submission.zip` was recreated with only `src/`, `README.md`, and `logs/` at the zip root.

## Notice

This plugin supports educational explanation and operator drafting only. It does not provide investment advice and must not recommend buying, selling, holding, market timing, target prices, or personalized allocation.
