# Prototype Build Brief — Task Mining Client Configuration (lo-fi, interactive)

Hand this to Claude Code (open it in the `TM_ClientConfiguration` folder). It captures the validated IA, the resolved decisions, and the exact scope so the prototype starts on solid ground.

## Goal
An interactive **lo-fi wireframe** (HTML) that replaces the current **Client Settings** page. Two things matter equally: (1) the **overall layout** — how the new object-based IA is arranged on the page, and (2) the **capture-rule flow** within it, especially the highest-risk surface: the **capture-level selector** and the **Custom editor**. Purpose is to test layout and the level-switching behavior. **Keep it a neutral wireframe** — greyscale, boxes and labels, no brand styling, colors, or polish. We're evaluating structure, not visual design; don't bias the review with a finished look.

## Read first (in this folder)
- `TM_Client_IA_Decision_Record.md` — decisions #1–#23 (the "why").
- `TM_Client_NavTest_Synthesis.md` — what the two VEs validated / where they got confused.
- `TM_Client_OpenDecisions_PreDesign.md` — what's resolved vs still open.
- `TM_Client_NavTree.mermaid` and `TM_Client_CaptureFlow.svg` — IA + capture model.
- `Tree Testing_mocks/` — existing lo-fi frames to stay visually consistent with.
- `Screenshots/Referrences/Celonis/Task mining_client settings.png` — **the exact page being replaced**. Study it for *what it does* (the jobs to re-home), not for how it looks — do not copy its visual style.

## What this replaces (current Client Settings page)
Today's page (`Task mining_client settings.png`) is one long scroll that fuses three concerns the new model separates:
- **Setup-mode radios** — "Use basic settings / Use advanced settings" → **dissolved** (no more Basic/Advanced).
- **Captured Applications** — three radios: *Capture all applications and URLs* / *Capture selected applications or URLs* / *Capture all but exclude some* → becomes **Scope + the Default rule** (all = Default at Full; selected = specific rules; exclude = Deny rules).
- **Captured Details** — a toggle list (Basic data, Name of active window/tab, Context of app/webpage, Input values…) → becomes **Captured data governed by the capture level** (these toggles are what Full locks on / Custom lets you edit).
Reproducing this mapping — so a viewer can see the old page's jobs re-homed into the new structure — is part of the point.

## Scope to build
**A. Overall layout (the shell + IA)**
1. **Celonis project shell** — left icon rail + project nav (Home, **Client Settings** [active], Users & Invite, Project Connection, then a "Data Configuration" group), breadcrumb (Projects › [Project] › Client Settings), page header with a primary **Save** action top-right.
2. **The new Client Settings IA as the content area** — the top-level areas from the nav tree: **Capture Rules, Privacy, Data Connection, Client Behaviour, User Attributes, Integrations, Configuration File**. Show how a user moves between them (left sub-nav or tabs — try what fits the shell).

**B. Capture-rule flow (the deep path)**
3. **Capture Rules list** — Default rule (catch-all, level only, no scope) + existing rules + "Create new rule".
4. **Rule editor** — Scope → Capture level → Captured data → Screenshots (screenshots is a peer, not nested under level).
5. **Capture-level selector** — Full / Custom / Deny.
6. **Custom editor** — the editable Captured-data view (two sections: Events + Data fields).

## Behavior locked by decisions (build to these)
- **First-match evaluation (#20):** the most specific matching rule wins; Default is the fallback. Show precedence in the list; a new rule starts with **no level preselected**; Default = **Full** out of the box.
- **Full & Deny are LOCKED (#17):** no attribute control. **Custom is the only editable tier.**
- **Custom default = option (b) (#21):** interaction events ON (typed, pasted, copied) but content fields OFF (EnteredText, ClipboardText, SelectedText). Screenshots off by default in Custom; can be added.
- **Deny is functional & selectable (#22):** a real posture that excludes capture — not a placeholder.
- **Level clarity (#23):** each level shows a persistent **"what this captures" summary + a preview of the actual field set**. This is the core thing the prototype must nail — it's the fix for the Full/Usage-only confusion both VEs hit.
- **Clean by default:** noise fields removed from the UI; **situational families (SAP, UIAA) hidden until their source is enabled** (conditional display).

## Still open — design around, don't hard-code
LEM placement + admin-access gate; SAP enablement location (global vs in scope); web-extraction placement (Integrations vs Capture Rules); hashing scope (global vs per-rule); element ID/class as "retain for agentic" (PM call). Where these appear, make them easy to swap.

## Wireframe styling (intentionally minimal)
- Greyscale only — white/grey fills, thin grey borders, one default system font. No brand colors, gradients, shadows, or icons beyond simple placeholders.
- Boxes, labels, and standard form controls (radios, checkboxes, toggles-as-plain-controls, dropdowns) are enough. Represent structure and state, not visual design.
- Use plain affordances to show hierarchy (indentation, borders, spacing) rather than styled components.

## Build constraints
- **Single self-contained `.html` file** (inline CSS + JS).
- **No localStorage/sessionStorage** — keep all state in memory (JS variables / in-page state).
- Prioritize two moments: navigating the **overall layout** between config areas, and the **level switch → captured-data preview updating live** inside a rule.
- Suggested filename: `TM_Client_Config_Wireframe.html`.

## Success check
1. Is the new IA laid out clearly on the page, with a way to move between config areas?
2. Can a viewer see how the old page's three jobs (setup mode, captured applications, captured details) are re-homed into the new structure?
3. Can a viewer, without explanation, tell what Full vs Custom vs Deny will capture — and see the field set change when they switch levels or edit Custom?
