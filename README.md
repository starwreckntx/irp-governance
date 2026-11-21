```
 _   _   _   _   _____        ___        _        ___     ____   ___    ____
| | | | | | | | | ____|      ( _ )      | |      / _ \   / ___| |_ _|  / ___|
| |_| | | | | | |  _|       / _ \/\     | |     | | | | | |  _   | |  | |
|  _  | | |_| | | |___      \ (_> <     | |___  | |_| | | |_| |  | |  | |___
|_| |_|  \___/  |_____|      \___/\/     |_____|  \___/   \____| |___|  \____|
```

> **[Hue & Logic Labs](https://www.hueandlogic.com)** · Maintained by [Joseph Byram (starwreckntx)](https://github.com/starwreckntx)

---

# irp-governance

**Live governance infrastructure for the IRP Orchestrator.**

Operated by Joseph (starwreckntx) — Pack3t C0nc3pts / Hue & Logic Labs LLC

---

## What This Is

This repository contains the operational governance documents for the
IRP (Individual Reflexive Protocol) Orchestrator — an AI system governed
by explicit consent frameworks, threat models, and accountability
structures.

The primary document is `SOUL.md`, the orchestrator's identity and
governance specification. It defines how the system behaves, how it
can be modified, who can modify it, and what happens when things break.

**Current version:** v0.9-rc (release candidate)
**Root-of-trust hash:** `16c8f86ebb8ec6e39d0588ce29857e5bbe110db2ecbba6da77021c45b51e7319`

## What This Is Not

- **Not a template.** This governs a specific system operated by a
 specific human. Forking it does not give you governed AI.
- **Not a framework for adoption.** The IRP methodology lives in
 [IRP__METHODOLOGIES-](https://github.com/starwreckntx/IRP__METHODOLOGIES-).
 This repo is the governance layer that controls it.
- **Not static.** Every commit is a governance modification with
 consent classification, operator acknowledgment, and audit trail.
 The modification log in Section 9 of SOUL.md is the ground truth.

## How It's Governed

SOUL.md governs itself through a four-tier consent framework:

| Tier | Scope | Example |
|------|-------|---------|
| Implicit | Low-risk, read-only | Reading a file |
| Operational | Established workflows | Running a build |
| Explicit | External actions, data sharing | Sending an email |
| Elevated | Governance modifications, health data | Modifying SOUL.md |

The authority hierarchy is structural and immutable:
1. Codex Law (constitutional)
2. StarWreck Alpha (operational context)
3. SOUL.md (identity + degraded-mode governance)
4. Session instructions

## Provenance

v0.9-rc was produced through:
- Collaborative authoring (operator + Claude)
- 10-model adversarial governance stress test
 (Gemini 3.1 Pro, Kimi ×3, GPT, Grok, Qwen, Mistral ×2, GLM 5)
- 17-fix patch specification with discrete commits
- Full consent framework compliance throughout

The `audit/` directory contains stress test results, consent grants,
and patch specifications.

## Structure

| Directory | Contents |
|-----------|----------|
| `/` | SOUL.md — the governance document |
| `memory/` | Amendment backlog, topology audits, operational tools |
| `audit/` | Stress test provenance, consent grants, patch specs |
| `codex-law/` | Reference pointer to canonical Codex Law source |

## License

CC BY-NC-SA 4.0 — Creative Commons Attribution-NonCommercial-ShareAlike 4.0

You can read, share, and build on this work with attribution.
You cannot use it commercially. Derivatives must use the same license.

Full terms: https://creativecommons.org/licenses/by-nc-sa/4.0/

---

*"The pursuit of perfect never results in excellence — but governance
without accountability is just decoration."*
