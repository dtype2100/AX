# Musinsa Research

Date: 2026-07-08

## Problem Hypothesis

Musinsa's fashion commerce teams need to turn fast-moving brand, product, and trend signals into clear merchandising decisions. Public Musinsa materials show a platform built around partner-brand growth, style discovery, trend-aware curation, and AI-assisted search. The narrow plugin opportunity is not to build another recommender system, but to help an MD or strategy operator frame messy inputs into evidence-backed questions, hypotheses, options, and risks before deciding what to promote, curate, or investigate.

## Target User

Primary user: Musinsa fashion MD, brand operator, or platform strategy/data operator.

Situation: the user has partial inputs such as a category trend, search spike, brand list, season context, product notes, campaign idea, or customer segment, and needs a structured decision brief.

## Evidence Map

| Claim | Source | Reliability | Plugin implication |
| --- | --- | --- | --- |
| Musinsa's stated mission includes helping partner brands grow and offering diverse ways for customers to discover personal style. | Musinsa corporate site, mission lines on partner success and style discovery: https://corp.musinsa.com/ko/ | Tier 1: official company source | The workflow should connect customer discovery and partner-brand implications, not optimize only for short-term sales. |
| Musinsa is actively using AI to analyze external real-time fashion and beauty trends and connect them to products through proactive curation. | Musinsa Newsroom, "AI Trend Curation", 2026-06-03: https://newsroom.musinsa.com/newsroom-menu/2026-0603 | Tier 1: official company source | The plugin should ask for trend source, category, timing, product attributes, and confidence, then convert them into MD actions. |
| Musinsa describes a move from search-centered commerce toward conversational fashion/beauty discovery using ChatGPT and a Musinsa MCP. | Musinsa Newsroom, ChatGPT Musinsa app, 2026-06-09: https://newsroom.musinsa.com/newsroom-menu/2026-0609-01 | Tier 1: official company source | A Codex skill can mirror this direction as an internal planning assistant: context-rich prompts, recommendation rationale, and risk notes. |
| Musinsa publishes search and transaction signal examples, such as vacation item search increases and 29CM satin skirt demand growth. | Musinsa Newsroom, vacation accessories, 2026-07-06: https://newsroom.musinsa.com/newsroom-menu/2026-0706; 29CM satin skirt trend, 2026-07-02: https://newsroom.musinsa.com/newsroom-menu/2026-0702 | Tier 1: official company source | The plugin should accept simple metrics, such as search lift, transaction lift, season/event context, and category keywords, then separate observed facts from hypotheses. |
| Musinsa's PB and partner-brand ecosystem has measurable interaction; public reporting cites consumer-level research that PB purchases can lead to future purchases from partner brands. | Musinsa Newsroom, Dongguk University PB synergy report, 2026-06-19: https://newsroom.musinsa.com/newsroom-menu/2026-0619 | Tier 1: official company source reporting independent academic work | The workflow should include cannibalization/complementarity questions and brand ecosystem risks when recommending curation options. |
| Fashion retail decisions in Seoul are fast-moving, local, and trend-sensitive; Vogue reports that Musinsa operates across online, offline, emerging brands, resale, and community. | Vogue Business, "The world's most innovative retailers, according to Vogue editors", 2024-04-15: https://www.voguebusiness.com/story/consumers/the-worlds-most-innovative-retailers-according-to-vogue-editors; Vogue, "Setting Up Shop in Seoul", 2026-02: https://www.vogue.com/article/setting-up-shop-in-seoul | Tier 2: reputable fashion/business press | The plugin should produce concise, time-sensitive briefs rather than long reports, and should make localization/customer-context assumptions explicit. |

## Method References

- Fashion recommendation research supports using compatibility, style/theme, product category, image, and text attributes as decision features. Reference: Banerjee et al., "Recommendation of Compatible Outfits Conditioned on Style", arXiv, 2022, https://arxiv.org/abs/2203.16161.
- Outfit compatibility research also supports grouping items and evaluating fit across a set, not just single-item relevance. Reference: Moosaei et al., "Fashion Recommendation and Compatibility Prediction Using Relational Network", arXiv, 2020, https://arxiv.org/abs/2005.06584.

## Implementation Structure References

- Agent Skills define a lightweight folder with a required `SKILL.md`, metadata, instructions, and optional scripts/references/assets. Reference: Agent Skills Overview, https://agentskills.io/.
- For this submission, the simplest structure should be one Codex plugin with `src/.codex-plugin/plugin.json` and one skill at `src/skills/musinsa-md-brief/SKILL.md`. No MCP server is needed unless a later phase requires live APIs.

## Video Context

- Title: "무신사의 AI 시대 전략과 인재상 | AX 인재전쟁 3화 무신사"; verified from YouTube oEmbed by the root orchestrator on 2026-07-08.
- URL: https://www.youtube.com/watch?v=OLAWeIuiD5Y
- Source type: public YouTube video from 조코딩 JoCoding; provider YouTube.
- Transcript availability: Korean auto-generated transcript fetched from public YouTube via `youtube_transcript_api` by the root orchestrator on 2026-07-08. Do not save or quote the full transcript.
- Summary aligned to plugin problem: the video frames Musinsa as a fashion/beauty commerce platform connecting brands and customers, discusses one-core multi-platform strategy and consolidation of fragmented member, product, and data systems, and emphasizes turning broad, complex problems into clear decisions that help Musinsa discover brands customers will like.

## Open Risks

- Official Musinsa newsroom claims are strong for company direction, but some are press-release claims. The README should distinguish observed public facts from plugin hypotheses.
- No private Musinsa data is available. The plugin must work from user-supplied inputs and public evidence, not pretend to access internal metrics.
- Avoid overbuilding: a skill-only workflow is enough for the submission unless later verification proves a script is necessary.

## Recommended Next Workflow

1. Define the plugin as `musinsa-md-brief`: a skill that turns brand, product, trend, and metric snippets into an MD decision brief.
2. Draft the skill with a fixed output shape: facts, missing inputs, MD questions, hypotheses, decision options, brand/customer risks, and verification checks.
3. Build only the required plugin files under `src/`.
4. Verify with two small sample prompts based on public Musinsa newsroom examples: vacation accessories and satin skirt demand.
5. Write `README.md` from this research, keeping the five required answers aligned with the skill behavior.
