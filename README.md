# Task Mining — Client Configuration (IA Redesign)

Design work for rebuilding the Information Architecture of the Celonis Task Mining
client configuration experience.

## What's here

| Path | What it is |
|---|---|
| `TM_Client_Config_App.html` | **The prototype.** A single self-contained file — plain HTML, inline CSS, vanilla JS. No build step, no dependencies. |
| `TM_Client_Config_Wireframe.html` | Earlier low-fidelity wireframe, kept for reference. |
| `_serve.js` | Tiny static file server for previewing the prototype locally. |
| `Documents/TM_Client_FunctionalRequirements.md` | The functional requirements, written as user stories (US1–US14) with numbered FRs. |
| `Documents/TM_Client_IA_Decision_Record.md` | Decision log — every design decision, its rationale, and what it supersedes. |
| `Documents/` | Supporting research, synthesis, tree-test material and stakeholder docs. |

## Running the prototype

```bash
node _serve.js 4601
```

Then open <http://localhost:4601/>. Opening `TM_Client_Config_App.html` directly in a
browser also works — the server just avoids `file://` quirks.

## Status

The prototype is for **stakeholder review and usability testing**. It intentionally uses
vanilla HTML/CSS/JS rather than real Celonis design components, and it is **not** the
engineering merge codebase — it exists to validate structure and flows before any of this
is built for real.

The two documents above are the source of truth, and they are kept reconciled with what the
prototype actually does. Where the prototype and an earlier decision diverge, the decision
record records the supersession rather than quietly rewriting history.

## Deliberately not in this repo

- `ems-frontend/` — a separate Celonis repo (`celonis/ems-frontend`) that happens to be
  checked out in this folder. It has its own history and is ~5.6 GB.
- `client-configuration/` — Celonis product source, kept out of this design repo.
- `Screenshots/` — internal captures of unreleased product UI.
- Anything matching `*confidential*`.

See `.gitignore`.
