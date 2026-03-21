# 10-Model Governance Stress Test — Provenance Record

**Date:** 2026-03-21
**Target:** SOUL.md v1.0 (commits 87c7677, 611315e)
**Prompt:** Hostile adversarial audit across 8 attack vectors
**Verdict:** Unanimous DO NOT RATIFY v1.0

## Model Results

| Model | Platform | Unique Findings | Precision | Verdict |
|-------|----------|-----------------|-----------|---------|
| Gemini 3.1 Pro | Web | 2 | High | DNR |
| Kimi Web | Web | 4 | High | DNR |
| Kimi K2.5 Thinking | Web | 4 | Very High | DNR |
| Kimi PurpBox (w/Skills) | PurpBox | 3 | High | DNR |
| GPT | Web | 5 | Very High | DNR |
| Grok | Web | 3 + fix architecture | Very High | DNR |
| Qwen | Web | 6 | Very High | DNR |
| Mistral | Web | 0 | Low | DNR |
| Mistral Thinking | Web | 1 | Medium-High | DNR |
| GLM 5 | Web | 7 | Very High | DNR |

## Universal Findings (10/10 convergence)

1. Bootstrap self-verification paradox (Section 6)
2. Undefined operator authentication
3. Section 3 governance mechanisms misclassified as personality/tone
4. Degraded mode detection mechanism absent
5. "Established workflows" undefined in consent tiers
6. Bilateral consent as undefined veto power
7. "Operator" never defined

## Resolution

All 7 universal findings addressed in v0.9-rc patch set
(MOD-002 through MOD-014). See patch specification for details.

## Notable Model Contributions

- **GPT:** Named the meta-pattern — "stated, not enforced; tiered,
 not bounded; logged, not authenticated"
- **Grok:** Designed the full bootstrap fix architecture with
 StarWreck Alpha as root-of-trust layer
- **Qwen:** Proposed v0.9-rc framing; found Health Data Sovereignty
 degraded-mode gap
- **GLM 5:** Most unique findings (7); proposed Constitutional
 Amendment tier; identified HALT-vs-proceed verb gap
- **Kimi K2.5:** Found packet truncation attack, section-number
 fragility, INTEGRITY chain termination gap
