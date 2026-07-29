# Task Mining Client Configuration — Navigation Test Synthesis

**Sessions:** 2 moderated navigation/first-click tests, 2026-07-20.
**Participants:** Jonas Bernien (VE) · 11:00 CEST; Tim Gautreau (VE) · 14:59 CEST. Facilitator: Mahalakshmi Ravikumar; observer: Ravi Teja Avvari (PM).
**Method:** participants were asked where they'd go to perform tasks against the proposed object-based IA, then reviewed the grouped event/data lists.
**Status:** consolidates both sessions. A third session is still pending — treat these findings as directional but consistent (two senior VEs converged on most points).

---

## 1. Headline

The **object-based IA held up.** On every "where would you go to…" task, both participants landed in the intended area with little hesitation — privacy for redaction, Capture Rules → new rule → Scope for targeting an app, Client Behaviour for startup. The IA's top-level structure is validated enough to design against.

**The one consistent failure is the capture-level naming.** Both Jonas *and* Tim could not explain the difference between **Full** and **Usage-only**. This is the strongest signal in either session and is the direct basis for renaming Usage-only → **Custom** (already actioned). The design must still prove the rename plus a "what this captures" summary actually resolves the confusion — the label change alone is a hypothesis, not a validated fix.

---

## 2. What worked (findability confirmed)

| Task | Jonas | Tim | Verdict |
|---|---|---|---|
| Stop storing credit-card numbers | Privacy & Consent → Data reduction | "Data reduction" section | ✅ both correct |
| Capture all actions for a specific app | Capture Rules → target apps/URLs | Capture Rules → create new rule → Scope | ✅ both correct |
| Auto-start capture on login | Client Behaviour / Startup mode | Client Behaviour → Startup mode | ✅ both correct |
| Anonymize usernames | Privacy & Consent (hashing) | — | ✅ correct |
| Turn off screenshots | Capture Rules | — | ✅ correct |
| Real-time validation (Live Event Monitor) | guessed Client Behaviour | Recording Behaviour | ◑ right neighbourhood, placement fuzzy |
| Enable SAP capture | SAP as an app within Capture Rules | dedicated "SAP Integration" section | ⚠ **split** — see §3 |

---

## 3. IA change signals (from the sessions)

- **SAP display is conditional (aligned).** Jonas: don't show 10–15 SAP fields to non-SAP customers — only surface SAP attributes when SAP is enabled in scope. Confirms the conditional-display decision. *Tension:* Jonas mentally located SAP *enablement inside scope/Capture Rules*, while the current model keeps SAP enablement global (PM's prior call). The two participants also split on where SAP lives (Tim → dedicated section; Jonas → within a rule). **Flag for the open-decisions list.**
- **Web page extraction → into Capture Rules (Jonas).** Argued extraction is URL-conditional logic just like scope, so it belongs with rules, not as a separate Integrations item. Maha noted the architecture treats them as independent processes. Logged as Maha's follow-up ("rethink extraction logic").
- **Group Client Behaviour with Data Connection (Jonas).** Both concern how/where data is transmitted to the platform.
- **Live Event Monitor needs admin-gated access (both).** Showing real-time capture to all users is problematic; restrict via an admin toggle at project/user level. Group follow-up: define admin roles + permissions for LEM.
- **Remove "noise" fields from the UI entirely (Tim, aligned).** Don't just deprioritize — don't show them. Reduces junk data presented to the VE.

---

## 4. Event & data prioritization — where they converged

**High value (keep, prominent):** navigation & window events; interaction (click/keyboard) — Jonas notes these are strongest combined with UIAA; identity fields (with hashing); local timestamps (preferred over UTC); app/window context (name, title, active window); URL; content input (entered text) — *high value but privacy-sensitive, so Full/Custom-gated*.

**Situational (show only in context):** SAP family (24 fields) — only when SAP enabled; UIAA family — "Value" field notably important (Wells Fargo); clipboard *content* (sensitive) vs the clipboard *action* (useful) → priority depends on level; custom attributes (Goldman used them to tag projects — redundant if project name is captured natively).

**Noise (remove from UI):** scroll events (mouse wheel/up/down); screenshot dimensions, coordinates, geometry; process ID, application path (no activity-validation value — app path only argued for remote software removal); event type, session ID, snippet ID, screenshot ID.

**Streamline:** clipboard → capture **"Copy to clipboard" only**, drop "Clipboard changed"; collapse granular Ctrl-C/Ctrl-X into the single copy event.

**Platform defaults, not user-configurable:** session/lifecycle events (start/stop, idle, lock/unlock). *Minor divergence:* Tim + Ravi want these logged automatically and hidden from config; Jonas rated them medium–high for data transformation. Resolution: log by default, don't expose as a config choice.

**Include for ops:** client + extension versioning (useful for monitoring corporate rollouts / update compliance).

**Unresolved:** element **ID / class name** — Tim rated low/noise; Ravi (PM) says they're critical for **agentic blueprints** (agents need identifiers to act on UI elements). Kicked to the open-decisions list as a PM call.

---

## 5. What this means for design

The nav skeleton is safe to build on. Before hi-fi, the level selector and the Custom editor carry the most risk (the Full/Usage-only confusion lived there), so those deserve the most exploration and a follow-up validation. The event/data lists should ship with noise removed and situational families hidden until their source is enabled — the "clean by default" posture both VEs asked for.
