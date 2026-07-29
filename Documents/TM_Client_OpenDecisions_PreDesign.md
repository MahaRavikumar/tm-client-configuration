# Task Mining Client Configuration — Open Decisions Before Design

**Purpose:** the interaction behaviors that are still unresolved and that change *what gets drawn*. Ordered by how much they block hi-fi work. Lo-fi exploration can proceed around most of these by showing the alternatives — but each should be closed before committing to hi-fi.
**Last updated:** 2026-07-23.

Legend — **Owner** = who decides · **Blocks** = the screen(s) that can't be finalized until resolved · **Lean** = current recommendation.

---

## Blocking — RESOLVED 2026-07-23

**1. Full vs Custom comprehension — ✅ RESOLVED.** Rename to **Custom** *plus* a persistent "what this captures" summary + field-set preview on each level. Not the rename alone. Re-validate the selector specifically. (Decision #23.)

**2. Custom default content set — ✅ RESOLVED: option (b).** Interaction events ON (typed, pasted, copied) so the *action* is recorded; content fields OFF (EnteredText, ClipboardText, SelectedText). (Decision #21.)

**3. Rule evaluation order — ✅ RESOLVED: first-match.** Most specific matching rule wins; Default rule is the catch-all fallback, not a cumulative baseline. (Decision #20.)

**4. Deny — ✅ RESOLVED: functional, user-selectable posture** (not a placeholder), enforced via base-URL / process-name matching. Treat as MVP. (Decision #22.)

---

## Blocking — resolve before hi-fi (lo-fi can show options)

**5. Live Event Monitor — placement + admin-access model**
Right neighbourhood in testing but placement fuzzy; both VEs want it admin-gated at project/user level.
· *Owner:* group (define admin roles) · *Blocks:* nav placement of LEM, its entry point, permissions UI · *Lean:* keep under Client Behaviour as its own labeled item; add an admin-only visibility gate.

**6. SAP enablement location — global vs within scope**
Model keeps SAP enablement global (prior PM call); Jonas expected to enable SAP *within a rule's scope*; Tim expected a dedicated SAP section.
· *Owner:* PM + Eng · *Blocks:* SAP integration placement, conditional-display trigger for SAP fields · *Lean:* keep enablement global but make SAP fields appear in a rule only when enabled (conditional display) + inline "enable SAP" affordance from the rule.

**7. Web page extraction — Integrations vs Capture Rules**
Jonas argues extraction is URL-conditional like scope and belongs in Capture Rules; architecture currently treats them as independent.
· *Owner:* Maha (rethink) + Eng · *Blocks:* whether extraction is modeled as a capture-rule concept or a separate area · *Lean:* keep under Integrations for MVP (architecture reality); revisit once rule/scope model is stable.

**8. Hashing — global vs per-rule**
Model keeps hashing global; Advanced editor allows per-rule/conditional hashing.
· *Owner:* Maha (validate with VEs) · *Blocks:* where hashing lives (global Privacy vs inside a rule) · *Lean:* global default; only add per-rule override if VEs confirm it's actually used.

**9. Element ID / class name — noise vs agentic blueprint**
Tim rated low; PM says critical for agents to act on UI elements.
· *Owner:* PM (this is explicitly a PM call) · *Blocks:* whether these fields appear in the Custom editor and how they're framed (analytics noise vs "retain for agentic") · *Lean:* park under a "retain for agentic" flag distinct from criticality; await PM.

---

## Non-blocking — can design around, resolve opportunistically

**10. Group Client Behaviour with Data Connection (Jonas).** Minor IA grouping; try both in lo-fi.
**11. Redaction improvements** — tagging, pre-built GDPR/HIPAA libraries, ordering (9-digit before 5-digit), testability. Direction, not spec; owned by the team to rethink.
**12. How validation works in EMS** — Preview is Windows-only today; the Simulator (post-MVP) is the proposed answer. Doesn't block MVP capture-rule design.

---

## PM/Product still owed (from scope one-pager)
A confirmed PRD, MVP boundary, and a target (baseline + goal) per success metric. The strawman (`TM_Client_Scope_Phasing_Metrics.docx`) stands in until Product owns it. Not a design blocker, but it decides which screens are actually in the MVP you design toward.
