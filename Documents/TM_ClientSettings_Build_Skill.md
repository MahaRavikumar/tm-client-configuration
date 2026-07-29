---
name: build-tm-client-settings
description: Build a clickable prototype of the redesigned Task Mining Client Settings page using the Celonis design system. Use when an agent (Cursor or Figma Make) is asked to build or extend this page.
version: 1.0
updated: 2026-07-23
---

# Build Skill — Task Mining Client Settings (redesign prototype)

## How to use this file
- **Cursor:** place at the repo root (rename to `.cursorrules`, or add as a `.mdc` rule with `alwaysApply: true`). Then prompt: *"Build the Task Mining Client Settings prototype described in this rule."*
- **Figma Make:** paste this whole file as the context/brief, then prompt: *"Build this prototype."*
- Either way: **read the whole file before writing code.** The workflow context (user stories + functional requirements) defines *what to build*; the component section defines *how to build it correctly*.

---

## 1. What you're building
A single, clickable **web prototype** of the redesigned **Client Settings** page for Celonis Task Mining, inside the EMS. It replaces today's fragmented setup (a Basic web page + a Windows-only Advanced desktop editor) with one unified, guided configuration surface. There is **no Basic/Advanced mode toggle** — the user configures directly.

Persona: **Admin / Value Engineer (VE)** who sets up what Task Mining records for a project. Not a developer; wants a clear, safe, fast path to a working configuration.

Scope of this prototype: the **overall page layout (IA in the app shell)** *and* the **capture-rule flow** within it. Use mock/sample data throughout; no backend.

---

## 2. User stories (workflow context)
> Synthesized from the product proposal, IA decisions, and research — the shared PRD did not include explicit stories, so treat these as the working set.

**Unified configuration**
- As an Admin, I want to configure everything Task Mining captures from one web page, so I don't need a separate Windows tool.
- As a Mac-based VE, I want to complete setup without a Windows VM.

**Capture Rules**
- As an Admin, I want to see a list of capture rules — a Default rule plus any specific rules — so I know what's captured where.
- As an Admin, I want to create a rule by defining its **scope** (applications / URLs) and choosing a **capture level**.
- As an Admin, I want the **most specific matching rule to win** (first-match), so behaviour is predictable; anything unmatched falls through to the Default rule.

**Capture levels (the primary control)**
- As an Admin, I want to pick **one named level** (Full / Custom / Deny) per scope instead of toggling dozens of settings.
- As an Admin, I want to **see what each level captures** (a plain-language summary + a preview of the actual field set) before I commit.
- As an Admin, I want **Custom** to start from a safe default and let me edit up (add content, screenshots) or down.
- As an Admin, I want **Full and Deny to be locked** (no attribute control) so the simple choice stays simple.

**Captured data**
- As an Admin, I want **events and data fields together** in one "Captured data" view, not separate Event/Logging tabs.
- As an Admin, I want to see **only relevant fields** — noise removed, and situational families (SAP, UIAA) hidden until their source is enabled.

**Privacy & validation**
- As an Admin, I want **redaction, hashing, and consent in one place**, and redaction that uses meaningful labels (e.g. "Group Chat") rather than blanket asterisks.
- As an Admin, I want to validate what's captured (today this is reactive — checking the data table); the Live Event Monitor is **admin-gated**.

---

## 3. Functional requirements
Build to these. Where a requirement is a locked decision it's tagged `[LOCKED]`; where it's still open, build the stated default but keep it easy to swap `[OPEN]`.

**Layout & IA**
1. Render inside a **Celonis app shell**: left navigation + a page header ("Client Settings") with a primary **Save** action. Breadcrumb: Projects › [Project] › Client Settings.
2. The page's config areas (left sub-nav or tabs — pick what the design system supports best): **Capture Rules · Privacy & Consent · Client Behaviour · Data Connection · User Attributes · Integrations & Extensions · Configuration File.** Capture Rules is the primary/first area. `[OPEN: sub-nav vs tabs]`
3. Moving between areas keeps the shell; only the content pane changes.

**Capture Rules**
4. Capture Rules area shows a **rule list**: the **Default rule** (capture level only, *no* scope), any specific rules, and a **Create new rule** action. Convey precedence (specific rules over Default). `[LOCKED: first-match]`
5. Opening/creating a rule shows the **rule editor** in this order: **Scope → Capture level → Captured data → Screenshots**. Screenshots is a **peer** step, not nested under the level. `[LOCKED]`
6. Scope = the applications and URLs the rule applies to (mock an app/URL picker).

**Capture level**
7. Level choices: **Full / Custom / Deny.** A new rule has **no level preselected**; the Default rule is **Full** out of the box. `[LOCKED]`
8. **Full and Deny are locked** — selecting them shows what they do but exposes **no attribute editing**. **Custom is the only editable tier.** `[LOCKED]`
9. Each level shows a persistent **"what this captures" summary + a preview of the field set.** Switching level **updates the preview live.** This is the most important interaction in the prototype. `[LOCKED]`

**Captured data (Custom)**
10. Custom's editable view has **two sections: Events** (which interactions to record) and **Data fields** (attributes logged per event). `[LOCKED]`
11. Custom **default state**: interaction **events ON** (e.g. typed, pasted, copied) but **content fields OFF** (EnteredText, ClipboardText, SelectedText); **screenshots OFF**. Editable up/down. `[LOCKED]`
12. **Noise fields are not shown** at all. **SAP and UIAA field families appear only when their source is enabled** (conditional display). `[LOCKED for noise; OPEN for exact SAP trigger]`

**Deny**
13. Deny is a **functional, selectable posture** that excludes capture for its scope (nothing to preview/redact). `[LOCKED]`

**Privacy & Consent**
14. Group **Data Redaction, Hashing (global), and User Consent** here. Redaction supports labelled replacement and (as direction) testing against sample data. `[OPEN: hashing global vs per-rule — default global]`

**Client Behaviour**
15. Includes **Startup mode** and the **Live Event Monitor**; LEM is **admin-gated** (show an admin-only affordance). `[OPEN: exact placement + access model]`

**General**
16. Each area has its own Save; unsaved changes are indicated.
17. Use realistic **sample data** (e.g. rules for Salesforce, a payroll URL, an Excel app).

---

## 4. Using the Celonis component library (do this correctly)
The real design system is available to you (installed package / Storybook / MCP / `llms.txt`). **Use it — do not hand-roll UI or invent component names and props.**

- **Discover first:** list the available components and read their real prop APIs from Storybook / the package types / the MCP before using them. If a component or prop is uncertain, verify against the source — never guess an API.
- **Map these UI needs to the library's actual components:** app shell / side navigation, page header, breadcrumb, cards/panels, tabs, radio group, checkbox, switch/toggle, select/dropdown, text input, list/table, buttons (primary / secondary / tertiary-text), badges/status pills, banner/alert, tooltip (for the "why" guidance), and modal/drawer (for the rule editor if needed).
- **Follow the library's tokens** for spacing, colour, and type — don't override with custom CSS unless a gap genuinely requires it, and say so.
- If the library is somehow **not** resolvable at build time, stop and report that rather than approximating — approximated components are the main failure mode here.

---

## 5. Build constraints & output
- **Framework:** React (the design system is React/Emotion-based). Single prototype app; **in-memory state only**, no backend, no persistence.
- **Clickable paths that must work end to end:**
  1. Land on Client Settings → move between config areas.
  2. Capture Rules → open the Default rule → see it's Full.
  3. Create a new rule → set scope → switch level Full ↔ Custom ↔ Deny and watch the **captured-data preview update live**.
  4. In Custom → toggle a content field / screenshots and see the preview reflect it.
- Keep it a **prototype**: sample data, no real capture, no auth. Note anything mocked.

---

## 6. Acceptance criteria
1. The redesigned IA is laid out in the app shell using **real design-system components**, and you can navigate between all config areas.
2. A viewer can create a rule, set scope, and choose a level with **no level preselected** on a new rule and **Full on the Default rule**.
3. **Full and Deny expose no attribute editing; Custom does**, starting from the safe default (events on, content off, screenshots off).
4. Switching level **updates the "what this captures" preview live** — the single most important behaviour.
5. Noise fields are absent; SAP/UIAA fields appear only when their source is enabled.
6. No invented components or props — everything traces to the actual library.

---

## 7. Source docs (if available alongside this file)
`TM_Client_IA_Decision_Record.md` (decisions #1–#23) · `TM_Client_NavTree.mermaid` (IA) · `TM_Client_CaptureFlow.svg` (capture model) · `TM_Client_NavTest_Synthesis.md` (what tested well / where users got confused) · `TM_Client_OpenDecisions_PreDesign.md` (resolved vs open). Read these for the "why" behind any requirement.
