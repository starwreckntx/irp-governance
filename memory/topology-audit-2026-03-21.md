# Network Topology Audit — 2026-03-21

## Classification: OpenClaw (Abacus.ai)

**Classification:** EXTERNAL CONSUMER (not mesh participant)
**Platform:** Abacus.ai Kubernetes container
**Tailscale status:** Not installed / not viable (container constraints)
**Mesh access:** Via authenticated HTTPS Funnel bridge to PurpBox
**Authentication:** API key header on FastAPI endpoint (port 8000)

**Known limitation:** Funnel bridge uses IPv4 pin (`--resolve`) which will fail on Tailscale A record rotation. DNS re-resolution daemon needed on PurpBox (see amendment backlog).

OpenClaw is architecturally external to the Tailscale mesh. It consumes mesh services (Mnemosyne, git, file operations) through the Funnel bridge endpoint. It does not route traffic, does not participate in mesh key exchange, and does not have a Tailscale IP. Access is application-layer authenticated, not network-layer authenticated.

**This is a design decision, not a limitation workaround.** Cloud-hosted inference nodes are external consumers by nature. Documenting them as mesh participants creates false topology assumptions that degrade security posture.

---

## Mesh Overview

### TAILSCALE MESH (100.x.x.x)

| Node | Tailscale IP | Role | Status |
|------|--------------|------|--------|
| PurpBox/Kali | 100.99.98.31 | Primary sovereign node — Mnemosyne, Gemini Bridge, Funnel bridge | ✅ Online |
| Windows Box | 100.79.242.30 | Persistent ledger / SSH bridging | ✅ Online |
| Kali Live USB | — | Ephemeral security/recon | — |
| PTM Bridge Server | — | [To be documented] | — |

### EXTERNAL CONSUMERS (authenticated, not meshed)

| Node | Access Method | Auth | Status |
|------|---------------|------|--------|
| OpenClaw (Abacus.ai) | Funnel bridge → PurpBox | API key header | ✅ Operational |
| [future external nodes] | — | — | — |

## Service Matrix

| Service | Host | Port | Tailscale Access | External Access |
|---------|------|------|------------------|-----------------|
| Mnemosyne (via Gemini Bridge) | PurpBox | 8001 | ✅ 100.99.98.31:8001 | ✅ Via Funnel bridge |
| Hub API | PurpBox | 3000 | ✅ 100.99.98.31:3000 | ❌ |
| Collab Server | PurpBox | 8000 | ✅ 100.99.98.31:8000 | ❌ |
| IRP General Assembly | PurpBox | 8004 | ⚠️ Missing per audit | — |
| Integrity Daemon | PurpBox | 6666 | ✅ | ❌ |
| OpenClaw Gateway | Abacusclaw | 18789 | ❌ | ✅ Funnel (HTTPS) |

## Communication Paths

### ✅ Working Paths
```
Operator (Windows) → Tailscale → PurpBox:8001 (Mnemosyne)
Operator (Windows) → Tailscale → PurpBox:3000 (Hub API)
Internet → Funnel → Abacusclaw:18789 (OpenClaw)
OpenClaw → Funnel Bridge → PurpBox:8000 → Mnemosyne:8001
```

### ❌ Blocked Paths (by design)
```
Abacusclaw → PurpBox:8001 (no Tailscale route — external consumer)
```

## Audit Findings

1. **Mnemosyne is healthy** — Running on PurpBox:8001, reachable via Tailscale and Funnel bridge
2. **OpenClaw correctly classified** — External consumer, not mesh participant (design decision)
3. **IRP General Assembly missing** — Port 8004 not responding on PurpBox
4. **Integrity Daemon running** — Port 6666 active
5. **Funnel bridge operational** — Enables external consumer access
6. **Security posture maintained** — Network-layer isolation preserved

## Known Issues

| Issue | Impact | Mitigation |
|-------|--------|------------|
| Funnel bridge IPv4 pin | DNS rotation breaks connectivity | DNS re-resolution daemon on PurpBox (backlog) |
| IRP General Assembly (8004) | Service unavailable | Investigate and restart |

## Recommendations

1. **Immediate:** Investigate IRP General Assembly on port 8004
2. **Short-term:** Implement DNS re-resolution daemon for Funnel bridge stability
3. **Long-term:** Maintain clear boundary between mesh nodes and external consumers

---
**Audit Date:** 2026-03-21  
**Auditor:** IRP Orchestrator (StarWreck Alpha)  
**Classification:** Topology Documentation — IRP v2.0 / Codex Law
