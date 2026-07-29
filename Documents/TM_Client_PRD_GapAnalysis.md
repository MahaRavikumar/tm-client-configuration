# PRD Gap Analysis — Unified Task Mining Configuration Experience

**Reviewed:** `PRD_ Unified Task Mining Configuration Experience.docx` (PM: Ravi Teja Avvari)
**Against:** Data Capture Proposal, Scope/Phasing/Metrics one-pager, IA Decision Record, and research (interviews + navigation tests).
**Date:** 2026-07-23. **Prepared by:** Product Design.

The PRD and our design work agree on the destination — one unified, web-based, non-Windows configuration experience — and the PRD adds things we owed (a concrete usability target, a delivery date, an owner for validation feasibility). The gaps below are places where the PRD is silent on our central design decisions, adds new scope, or takes a position that our research pushes back on. None are fatal; most are reconciliations to close together before design commits.

---

## A. Missing from the PRD (our work it doesn't yet reflect)

**1. The capture-level model (Full / Custom / Deny) — our central concept — is absent.**
This is the biggest gap. The whole proposal and decision record are built on capture levels: one named choice per scope that replaces dozens of low-level toggles (decisions #6, #17). The PRD never mentions it — it describes "Information Buckets" and template-driven "recommended capture rules" instead. Those are complementary, not the same mechanism. The PRD should name capture levels as the primary control, or we need to reconcile which model is the spine.

**2. The object-based IA isn't reflected.**
Our validated structure — Capture Rules at the centre; Privacy & Consent, Client Behaviour, Data Connection, User Attributes, Integrations around it — appears in the PRD only as generic "logical categories / Information Buckets." Tree tests validated this specific structure; the PRD should point to it rather than a generic grouping.

**3. "New projects only — no migration" (decision #18) is not stated — and the PRD implies the opposite.**
The PRD's framing ("migrate all desktop-only advanced features," the "one-way street" pain point) reads as promising continuity/migration for existing configurations. We explicitly scoped this to **new projects only, reuse via duplicating rule sets, no migration mapper**. This is a scope conflict to settle explicitly — it changes what Engineering builds.

**4. Rule model / engine behavior absent.**
First-match evaluation (#20), the default rule as catch-all, scope → level → captured data → screenshots — none of it is in the PRD. Templates presume rules exist but the rule model itself isn't described.

**5. "Granularity is a competitive strength" is missing — risking a "capture less" reading.**
Our strongest research steer (Ankit) is that the fix is guidance/bucketing, **not** reducing capture depth. The PRD's "Information Overload & Overengineering" section leans toward trimming fields; without the counter-principle it could be read as "capture less," which contradicts the research. Add the nuance: keep depth, add comprehension.

**6. Duplicate rule sets (our MVP) and the Rule Capture Simulator (our Post-MVP) aren't mentioned.**
Our one-pager MVP included duplicating rule sets for reuse; Post-MVP included the Simulator (privacy-safe preview on mock data) and redaction suggestions. The PRD's phasing is different (see §B) and omits both.

**7. LEM admin-access model is missing.**
Both VEs and our decision log say the Live Event Monitor must be **admin-gated** (privilege handling at project/user level). The PRD wants LEM "prominent… as a standard step in the configuration wizard" for everyone — see conflict §C.2.

**8. Redaction specifics are thinner than research demands.**
The PRD's "Contextual Redaction" (meaningful labels instead of asterisks) is a good pickup of Ankit's tagging point. But it drops the rest of that finding: **pre-built GDPR/HIPAA libraries, match ordering (9-digit before 5-digit), and the ability to test a rule against sample data.**

**9. Two success metrics we proposed are dropped.**
The PRD keeps usability, first-time accuracy, and self-service — but drops **data quality / signal-to-noise (VE feedback)** and **redaction misses / privacy incidents.** Losing the privacy-incident metric is notable given how central privacy is to the pitch.

---

## B. New in the PRD (we need to absorb — net-new scope)

**1. Configuration Templates (Phase 2).** Pre-built templates for common apps (Excel, Outlook, Salesforce) that auto-apply recommended capture rules. This is net-new — it doesn't appear in any of our docs. It's related to but distinct from "duplicate rule sets." Design implication: a template picker and a template→rule application flow. Worth deciding how templates relate to capture levels (does a template just preset a rule's scope + level?).

**2. Concrete success target.** Usability rating **2.5/5 → 4.0/5**. This is the baseline+goal our one-pager said Product still owed. Good to have it.

**3. Committed delivery — December 2026.** Our one-pager left timelines to Engineering. With a date now fixed, the MVP/Post-MVP line matters more: confirm the Simulator and templates are genuinely Phase 2 and not expected by December.

**4. "TBD based on Danish Aziz" on the validation suite.** Explicit dependency/owner for validation feasibility — aligns with our Simulator-feasibility → Danish note.

---

## C. Direct conflicts to reconcile

**1. Validation philosophy.** PRD makes Preview + LEM a **prominent, standard wizard step** and tracks "Validation Usage (Preview frequency)" as a core metric. Our research found validation is mostly **reactive** — VEs check the captured-data table; Preview/LEM are largely undiscovered/unused, with pre-upload Preview a minority enterprise need. Elevating Preview as central may optimise for a behaviour most users don't have. Reconcile: is the goal to *increase* Preview use (a behaviour-change bet) or to *support the reactive pattern* (better data-table validation, plus the Simulator)? The PRD hedges with "TBD based on Danish," so this is open — flag it.

**2. LEM for everyone vs admin-gated.** PRD: LEM as a standard step for all users. Research + decision: LEM shows real-time captured data and must be **restricted to admins** for privilege/privacy reasons. Reconcile the access model before it's designed as an open wizard step.

**3. Migration.** PRD implies migrating existing setups; our decision is new-projects-only. (Same as A.3 — listed here because it's a true either/or.)

**4. Mental model: templates + buckets vs capture levels + objects.** The PRD's spine is "unify + templates + information buckets"; ours is "object IA + capture levels." These can fit together (templates preset a rule's scope+level within the object IA), but the PRD doesn't say that. Agree on one integrated model so design isn't caught between two.

---

## D. Recommended reconciliations (for the PM conversation)

1. Add **capture levels (Full/Custom/Deny)** to the PRD as the primary capture control, and reference the **object-based IA** and rule model explicitly (link the proposal + nav tree).
2. State the **new-projects-only / no-migration** scope in the PRD, and soften the "migrate everything" language accordingly.
3. Resolve the **validation stance** with Danish: reactive-support + Simulator vs. prominent Preview — and set the LEM **admin-gating** model.
4. Confirm **phasing**: templates and Simulator as Phase 2; duplicate rule sets in MVP; verify all against the December 2026 date.
5. Restore the **data-quality and privacy-incident metrics**, or consciously agree to drop them.
6. Fold the **full redaction ask** (libraries, ordering, test-against-sample) into the Contextual Redaction feature.
7. Add the **"granularity is a strength"** principle so "reduce noise" isn't misread as "capture less."
8. Clarify how **Configuration Templates** relate to capture levels and duplicate rule sets so the three don't overlap confusingly.
