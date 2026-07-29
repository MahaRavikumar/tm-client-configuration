# Events & Logs Grouping — Facilitation Script (~15 min)

Run this **after** the tree test, in the same moderated session. Screen-share the audit workbook → **"Events (grouping)"** and **"Logging (grouping)"** sheets and fill the yellow columns live.

**Goal:** validate/refine how events and logging attributes cluster into value tiers — *Always capture · Situational · Noise* — and hear the *why*. This is directional (small n); the reasoning matters more than the vote.

---

## Before you start
- Have both grouping sheets open; you'll fill **VE tier** and **Notes / why** as they talk.
- You're validating groups (~17 cards), not 122 items. Don't read every attribute aloud.

## 1. Frame it (say this, ~30 sec)
"We capture a lot of data fields. I've clustered them into groups. I'd love your help sorting each group into three buckets — **Always capture, Situational, or Noise** — and hearing why. There are no wrong answers; I'm testing the grouping, not you."

## 2. Warm-up (1 question)
"When you set up capture, how do you personally decide what's worth capturing versus what's noise?"
→ Listen for their mental model; it frames everything after.

## 3. Sort the groups (events first, then logging)
For each group: state your starting point, then ask them to place it.
- "This group is **[name]** — things like [1–2 examples]. Always, Situational, or Noise?"
- "**Why?** When would you need it / not need it?"
- Record their tier + reason in the yellow columns.

Go in this order (fastest signal first):
- **Events:** Navigation & window → Interaction → Content & clipboard → Scroll → Session & lifecycle
- **Logging:** Content/input → Element/interaction → App/window → Identity → Coordinates & geometry → Screenshot dimensions → SAP family → UIAA family → the rest

## 4. Probe the contested ones (spend most time here)
These are where the value is — don't rush them:
- **Content / input & Content events** — high value but privacy-heavy. "Do you actually use typed text / clipboard, or is redaction enough?"
- **SAP family** — "Only for SAP customers? Which SAP fields actually matter — transaction, screen number?"
- **UIAA family** — "Ankit mentioned UIAA sometimes captures values found nowhere else — true for you?"
- **Coordinates / geometry / screenshot dimensions** — "Do these ever get used, or always noise?"
- **Session & lifecycle** — "Idle useful for segmenting time? Session/alive — noise?"

## 5. Catch exceptions
When they say "mostly noise except X," note the exception at the item level in Notes — that's the gold for right-sizing default capture.

---

## Prompts to keep handy
- "Always, Situational, or Noise?"
- "When would you actually use this?"
- "If this were off by default, would you miss it?"
- "Which one field in this group is the one you can't live without?"

## Don'ts
- Don't lead ("this is noise, right?") — ask open, then react.
- Don't try to cover all 122 — groups + exceptions is enough.
- Don't debate; capture their view and move on.

## After the session
- Map their **Always / Situational / Noise** back to capture level: Always → Usage-only & Full · Situational → Full-only or per-integration · Noise → candidate to drop from default.
- Compare the two VEs' calls; flag agreements (act on) vs splits (needs more input).
- Feed refinements into the **Events** and **Logging** sheets' Criticality / Capture-level columns.
