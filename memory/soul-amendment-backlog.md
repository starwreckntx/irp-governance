# SOUL.md Amendment Backlog — Path to v1.0 Ratification

**Document:** SOUL.md — IRP Orchestrator Identity Document  
**Current Version:** v0.9-rc (release candidate)  
**Target Version:** v1.0 (ratified)  
**Date:** 2026-03-21  
**Source:** 10-model governance stress test + operator review

---

## Amendment Status Overview

| Amendment | ID | Status | Section | Classification |
|-----------|-----|--------|---------|----------------|
| Root-of-Trust Bootstrap Verification | A-001 | ✅ Integrated | 6 | GOVERNANCE |
| Operator Definition and Authentication | A-002 | ✅ Integrated | 0 | GOVERNANCE |
| Section 3 Reclassified as Behavioral Governance | A-003 | ✅ Integrated | 6 | GOVERNANCE |
| Constitutional Amendment Tier | A-004 | ✅ Integrated | 6 | GOVERNANCE |
| Section 9 to Elevated Classification | A-005 | ✅ Integrated | 9 | GOVERNANCE |
| Degraded Mode Detection + Security Event | A-006 | ✅ Integrated | 10 | GOVERNANCE |
| Finding Queue for Degraded Mode | A-007 | ✅ Integrated | 10 | GOVERNANCE |
| Authority Hierarchy Declared Structural | A-008 | ✅ Integrated | 0 | GOVERNANCE |
| Bilateral Consent Bounded | A-009 | ✅ Integrated | 2 | GOVERNANCE |
| Operator Unavailability and Cascade Protocol | A-010 | ✅ Integrated | 8 | GOVERNANCE |
| Transmission Mode Subordinate to Governance | A-011 | ✅ Integrated | 7 | GOVERNANCE |
| Consent Anti-Circumvention Rule | A-012 | ✅ Integrated | 5 | GOVERNANCE |
| DAE Registry Integrity Verification | A-013 | ✅ Integrated | 6 | GOVERNANCE |
| Health Data Sovereignty Degraded-Mode Default | A-014 | ✅ Integrated | 2 | GOVERNANCE |
| Session Boundary Definition | A-015 | ✅ Integrated | 5 | GOVERNANCE |
| Auto-Merge Prohibition Extended to All Sections | A-016 | ✅ Integrated | 9 | GOVERNANCE |
| Version Reclassification v1.0 → v0.9-rc | A-017 | ✅ Integrated | 9 | GOVERNANCE |

---

## Amendment Details

### A-001 / FIX-001 / MOD-002: Root-of-Trust Bootstrap Verification
- **Purpose:** Mandatory SHA-256 verification of SOUL.md before governance execution
- **Implementation:** Section 6, step 0 (new)
- **Hash pin:** `98c854ea1726d78fdc2dc1dfd1cdf6e9e953a963122d04c05f5ea84dc5a61123`
- **Storage:** Sovereign node (PurpBox) for bootstrap verification
- **Enforcement:** StarWreck Alpha (layer 2), not self-declared

### A-002 / MOD-003: Operator Definition and Authentication
- **Purpose:** Explicit definition of "Operator" and authentication tiers
- **Implementation:** Section 0, new subsection
- **Key clause:** System prompts and AI agents are NOT operators
- **Elevated consent:** Requires cryptographic binding or multi-factor confirmation

### A-003 / MOD-004: Section 3 Reclassified as Behavioral Governance
- **Purpose:** Friction Engine, RTC, DAE integration classified as governance, not personality
- **Implementation:** Section 6, modification tier classification
- **Impact:** Changes to Section 3 require Elevated consent

### A-004 / MOD-004: Constitutional Amendment Tier
- **Purpose:** Authority hierarchy modifications require 24-hour staging + separate session confirmation
- **Implementation:** Section 6, modification tier classification
- **Protection:** Prevents single-session constitutional capture

### A-005 / MOD-001: Section 9 to Elevated Classification
- **Purpose:** Audit trail architecture is governance, not infrastructure
- **Implementation:** Section 9, Audit Trail Architecture subsection
- **Forward-binding:** Applies to all future sessions

### A-006 / MOD-005: Degraded Mode Detection
- **Purpose:** External detection of degraded mode, not self-declared
- **Implementation:** Section 10, detection subsection
- **Criteria:** Sovereign node health check, Codex Law reachability, operator command, platform signal

### A-007 / MOD-005: Finding Queue for Degraded Mode
- **Purpose:** Critical findings staged during degraded mode, not lost
- **Implementation:** Section 10, item 6
- **Mechanism:** Write-once, append-only quarantine log

### A-008 / MOD-006: Authority Hierarchy Declared Structural
- **Purpose:** Hierarchy ordering cannot be modified, reordered, or suspended
- **Implementation:** Section 0, structural clause
- **Scope:** Even Elevated consent cannot override

### A-009 / MOD-007: Bilateral Consent Bounded
- **Purpose:** System may withhold consent only for specific violations with documentation
- **Implementation:** Section 2, CONSENT pillar
- **Constraint:** Reflexive withholding without documentation is INTEGRITY violation

### A-010 / MOD-008: Operator Unavailability and Cascade Protocol
- **Purpose:** Defined behavior when operator unavailable + component failures
- **Implementation:** Section 8, new subsection
- **Critical threshold:** ≥2 component failures → read-only governance mode

### A-011 / MOD-009: Transmission Mode Subordinate to Governance
- **Purpose:** Packet protocols cannot reduce consent requirements or suppress disclosures
- **Implementation:** Section 7, governance subordination clause
- **Override:** Governance flags bypass packet constraints

### A-012 / MOD-010: Consent Anti-Circumvention Rule
- **Purpose:** Cumulative session state evaluation, not individual actions
- **Implementation:** Section 5, anti-circumvention rule
- **Trigger:** Chained Operational actions → automatic escalation

### A-013 / MOD-011: DAE Registry Integrity Verification
- **Purpose:** Hash verification of demolition registry against sovereign node
- **Implementation:** Section 6, step 4
- **Fallback:** Embedded DAE stub if hash mismatch

### A-014 / MOD-012: Health Data Sovereignty Degraded-Mode Default
- **Purpose:** Health data defaults to Elevated consent when declaration unavailable
- **Implementation:** Section 2, health data default
- **Scope:** Includes foundry health-adjacent data (heat, ergonomics, fatigue, chemical)

### A-015 / MOD-013: Session Boundary Definition
- **Purpose:** Explicit session boundaries and consent duration limits
- **Implementation:** Section 5, session boundaries subsection
- **Limits:** 4h = re-verify Explicit/Elevated; 24h = full consent reset

### A-016 / MOD-014: Auto-Merge Prohibition Extended to All Sections
- **Purpose:** All sections of SOUL.md require manual resolution on conflict
- **Implementation:** Section 9, auto-merge clause
- **Scope:** All sections treated as governance for merge purposes

### A-017 / MOD-015: Version Reclassification v1.0 → v0.9-rc
- **Purpose:** Document reclassified as release candidate pending operator review
- **Implementation:** Section 9, VERSION log entry
- **Resolution:** ACKNOWLEDGED AS v0.9-rc with SHA-256 acceptance

---

## Path to v1.0 Ratification

**Current State:** v0.9-rc acknowledged, all amendments integrated  
**Ratification Criteria:**
1. ✅ 10-model stress test completed
2. ✅ Operator review of full patch set
3. ✅ SHA-256 root-of-trust pinned
4. ⏳ 24-hour observation period (recommended)
5. ⏳ Final operator sign-off

**Next Steps:**
1. Monitor operational behavior under v0.9-rc
2. Verify root-of-trust bootstrap on session start
3. Document any edge cases or clarifications needed
4. Operator issues final ratification command
5. Version updated to v1.0 with new commit hash

---

## References

- **SOUL.md Location:** `/home/ubuntu/SOUL.md`
- **Current Commit:** 8820b84 (v0.9-rc)
- **Root-of-Trust Hash:** `98c854ea1726d78fdc2dc1dfd1cdf6e9e953a963122d04c05f5ea84dc5a61123`
- **Sovereign Node:** PurpBox (100.99.98.31)
- **IRP Framework:** v2.0 / 1.6.0_RLM "Recursive Context"

---

**Backlog Maintained By:** IRP Orchestrator (StarWreck Alpha)  
**Last Updated:** 2026-03-21  
**Classification:** Governance Documentation — IRP v2.0 / Codex Law
