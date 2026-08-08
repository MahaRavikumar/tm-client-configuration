# Task Mining Client Configuration — Functional Requirements

**Format:** each entry starts with a **user story** (the Admin's intention) followed by the **functional requirements** — the capabilities the screen must have to achieve that intention.
**Status:** v3, in progress. User Stories 1–15 defined (all six config areas + approval-gated rollout; US14 config-file export/import/SQL withdrawn); gap/contradiction review applied. **New in v3: US15 — Save and Apply are decoupled**, so saving a draft no longer affects users; applying is a separate, attested action, with approval itself handled outside the product (decision #45). FR1.3 and FR1.4 updated accordingly, and US14's encoded import/export is **parked pending Product confirmation**. **Deny no longer shows the field inventory or screenshot control** — one statement replaces ~1.7 screens of locked-off toggles (FR4.3, FR4.5; decision #46). v3 reconciles Capture Rules with the built prototype: Default-rule level now editable — guarantee restated as **coverage, not capture**, plus a non-blocking warning when it is not Full (FR2.5, FR2.5a; knock-on fix to FR1.5), rule-name validation specified in full including the empty-on-create behaviour (FR2.2), attribute is a drop-down (FR3.1), operator set expanded and attribute-aware (FR3.2), EventType and TargetElementName dropped as scope attributes (FR3.3), IN via multi-select value (FR3.8), negation removed (FR3.7). Every create/edit flow now uses one **modal dialog** pattern with validity-gated Submit and revert-on-Cancel, the capture rule included (FR1.6). Deleting now **confirms instead of offering Undo** (FR2.6), and the rule-list card is stripped back to name + level badge + delete (FR2.3). **FR3.10 (plain-language scope summary on the rule card) has been removed** — a nested scope does not summarise legibly in a card-width line; the ID is retired rather than reused, so FR3.x numbering skips it. Its intent returns as **FR3.12**, a read-only read-back inside the rule editor where nesting can be shown with explicit parentheses. FR3.1 no longer speaks of "progressively exposing an advanced builder" (there is only one builder, which grows), FR3.6 records the **2-level nesting cap**, and FR3.3/FR3.4 are flagged as **still to be validated with Product**. A new rule opens with **Custom pre-selected** rather than no level chosen (FR4.1), and FR3.9 and FR3.13 now specify the per-node action menus and the per-attribute value help that the prototype already implements. **Privacy is built:** Data redaction and Hashing as two sections of one page, patterns shaped as *what to look for → what to do about it* with four actions, drag-reorder, a pasted-sample tester (FR6.2, FR6.4, FR6.5, FR6.9), and redaction suppressing hashing where the two would collide (FR7.9a). The **Live Event Monitor is renamed "View captured events"** and three factual errors in FR10.4 corrected — it is reactive, project-wide, and only makes a control available. Rationale and supersession history for all of the above is logged as decisions #31–#58 in `TM_Client_IA_Decision_Record.md`.
**IDs:** FRs are numbered per story (FR1.x, FR2.x…) for unique reference.

---

## User Story 1

**As an Admin, I want to configure client settings for a new project.**

**Functional requirements:**

- **FR1.1** Present the **6 config areas** as tabs, ordered by importance / mental model (decision #12): **Capture Rules · Privacy · Integrations & Extensions · User Attributes · Client Behaviour · Data Connection.** The most-used areas lead; the low-touch, pre-filled ones (Client Behaviour, Data Connection) trail. **Privacy** and **Integrations & Extensions** are container areas whose sub-screens are presented as **sections** — Privacy: Redaction · Hashing · Consent; Integrations & Extensions: SAP · Extensions. *(Changed from v2's order — Data Connection and Client Behaviour were mid-list; moved to the end as least-touched.)*
- **FR1.2** No landing page — the Admin lands directly on the **Capture Rules** area.
- **FR1.3** Persistent page header carrying **two distinct global actions** — **Save draft** and **Apply** — plus a **rollout state indicator** beside the page title. Both actions are **global** across all six areas. **Saving does not affect users**; only Apply does (see **US15**). There is **no autosave** — changes persist only on explicit Save. *(Open: confirm autosave feasibility with Engineering; going without it for now.)* Each area provides **inline validation** for fields that require it, **blocking Save while any required field is invalid** — a saved draft is therefore never invalid. *(Changed from v2, where a single **Save** both persisted and applied the configuration; superseded by decision #45.)*
- **FR1.4** A **More actions** menu in the header holds secondary actions: **Download configuration file** (FR15.5) and **Upload configuration file** (FR15.11) — the two human-readable file actions that drive the approval round-trip. There is **no** encoded export/import or SQL-generation action (US14 withdrawn; decision #62), and no separate Configuration File tab.
- **FR1.5** Display the **Default rule** with a subtext that plainly states **what its currently selected capture level captures** — and that it applies to any activity no other rule matches. Since it ships as Full, that subtext describes what Full captures out of the box, but it must **track the selected level** rather than assume Full (see FR2.5). *(Changed from v2, which hardcoded "what Full captures" when the Default's level was locked.)*
- **FR1.6** **Modal (dialog) behaviour — the single pattern for every create/edit flow.** All **collection items** are created and edited in a dialog: **capture rule** (US2–US5), **redaction pattern** (US6), **user attribute** (US11), **web-page extraction rule** (US12). They use **Submit** and **Cancel** — the primary button is labelled **Submit**, not "OK".
  - **Submit** **stages** the change into the working (unsaved) state and closes the dialog; it is only persisted by the global **Save** (FR1.3). **Submit is disabled until the item passes inline validation** (for a capture rule that means a valid name *and* at least one complete scope condition — FR2.2, FR3.11).
  - **Cancel discards.** A **newly created** item is **removed outright** — it never appears in the list. An **existing** item is **reverted to a snapshot** taken when the dialog opened, so Cancel undoes every edit made in that dialog. This makes "Cancel" truthful rather than decorative.
  - Because Submit is validity-gated, **an invalid item can never reach a list** — which is what removes the need for discard prompts, undo toasts, or delete-as-an-escape-hatch.
  - **Escape cancels. Clicking the overlay does not** — on a large form a stray backdrop click would discard part-built work.
  - **Dialogs are sized to their content.** A capture rule is **near-fullscreen** with a sticky header and footer and a scrolling body (it holds the scope builder plus ~29 field toggles); a redaction pattern or user attribute is a conventional centred dialog.
  - **Not modal:** the **singleton settings screens** — Privacy › Hashing and Consent, Data Connection (US9), Client Behaviour (US10), SAP Integration (US13) — are always-present, pre-filled inline forms edited directly on their screen and committed by the global Save. There is nothing to "create", so no dialog.
  - *(Changed from v2: v2 applied this only to small sub-items and left the capture rule as a full-page editor. The rule editor is now a dialog too — see decision #40, which supersedes decision #14's page flow — and Cancel's revert-from-snapshot behaviour is newly specified.)*

---

## User Story 2

**As an Admin, I want to create a new rule to define the scope and what data to be captured.**

**Functional requirements:**

- **FR2.1** A clear action button to **create a new rule**.
- **FR2.2** The Admin enters a **rule name** when creating a rule. The name is **required** and **not case-sensitive**; **duplicate names are not allowed** (case-insensitive check, compared on the trimmed value and applied against *all* rules including the Default). Show the error **inline**, and **block Save** while any rule name is invalid (per FR1.3).
  - **A new rule starts with an empty name**, not a placeholder value like "New rule", and **focus lands in the name field** on create. A prefilled name would defeat the required-field flow entirely (the field is never blank, so the error never fires) and would let two quick creations collide as duplicates. A rule left unnamed is shown in the rule list as *"Unnamed rule"* in an error style so it stays findable while Save is blocked.
  - **When each message appears:** the **required** error appears once the field has been **left (blurred)** — a freshly opened, untouched field is not pre-flagged. A **duplicate** name is flagged **live as it is typed**, since it only triggers on a full match and keeps the disabled Save self-explanatory.
- **FR2.3** Display the list of created rules. Each card is deliberately **minimal**: the **rule name**, its **capture level as a prominent badge directly beneath the name**, a **delete icon**, and a chevron into the editor. **No numbered list.** The card does **not** repeat the rule's scope expression or the capture level's description — both are one click away in the editor, and at list level they crowded out the two things the Admin actually scans for (which rule, and how much it captures). The **Default rule** card carries **no "Default" badge** — its position under a *Fallback* heading already says that — and shows its explanatory subtext **inline next to the name**, with its level badge beneath. *(Changed from v2, which put the scope expression and the level description in the card subtext; see decision #42.)*
- **FR2.4** The Admin can rearrange rules by **drag and drop**. Order **= precedence** (first-match, top rule wins); make this **explicit** in the UI.
- **FR2.5** **Separate the Default rule** from the created rules. The Default rule **cannot be moved or deleted**, always sorts **last**, and has **no scope** — only a capture level. Two distinct properties, deliberately not conflated:
  - **Coverage is guaranteed (structural).** Because the Default rule always exists and always matches, **every activity is evaluated by exactly one rule** — nothing ever falls through the rule set unhandled. This holds *regardless* of the Default's capture level, and is what FR2.7 protects.
  - **Capture is a policy choice (the Admin's).** The Default's **capture level is editable** and **defaults to Full**, so out of the box everything unmatched by a more specific rule is captured in full. An Admin may instead set it to **Deny** — a deliberate *capture-nothing-unless-explicitly-scoped* posture — or to **Custom**.
  - **FR2.5a — Warn on a non-Full Default.** Because this one level decides the fate of all unmatched activity, show a **non-blocking warning** wherever the Default's level is set to anything other than Full, stating plainly that activity matching no other rule will not be captured (or will be captured only partially). It **must not block Save** — a restrictive Default is a legitimate configuration, just one that should be chosen knowingly rather than by accident.
  - *(Changed from v2, where the Default level was fixed and locked to Full. Note the guarantee has been restated: v2 claimed the Default "guarantees nothing is silently dropped", which is only true while it is set to Full. With an editable level, the guarantee is **coverage**, not **capture** — and FR2.5a is what keeps a restrictive Default deliberate rather than silent.)*
- **FR2.6** The Admin can **delete** a rule from the rule list, via a **delete icon on the rule card** (placed before the chevron). Deleting asks first: show a **confirmation dialog** naming the rule, stating that its scope and captured-data settings go with it, and that the change **takes effect on Save** (FR1.3). Buttons are **Cancel** and a destructive **Delete rule**; **Escape** cancels. There is **no undo toast** — the question is asked before the act, not after it. The **Default rule has no delete affordance at all** (FR2.5 / FR2.7).
  - **This is the delete pattern for every collection item**, not just rules — redaction patterns (FR6.7), user attributes (FR11.7) and extraction rules (FR12.5) all confirm before deleting. One predictable pattern beats a per-object mix, and it pairs with the single create/edit dialog pattern of FR1.6.
  - *(Changed from v2, which specified a toast with Undo and explicitly **no** confirmation dialog. Reversed because a rule is a large composite object — scope tree, capture level, per-field selections — so a few seconds of Undo is a poor safety net for something that costly to rebuild, and an Undo that expires silently leaves no recovery path at all. Asking first is also cheap here: deletion is rare, unlike the bulk toggling elsewhere in the app. See decision #41.)*
- **FR2.7** Capture Rules always has **at least one rule** — guaranteed because the **Default rule cannot be deleted**.

---

## User Story 3

**As an Admin, I want to define a rule's scope so that the rule applies only to the applications, URLs, and contexts I target.**

**Functional requirements:**

- **FR3.1** **Simple-first.** Start with a simple picker to name the application(s) and/or URL(s) the rule targets. The **attribute is chosen from a drop-down select** (the curated list in FR3.3); the **value uses typeahead** (with suggestions + free typing). From there the Admin can **progressively add further conditions and groups** to build up an advanced scope definition — one condition is enough for the common case, and the compound structure is reached by adding to it rather than by switching into a separate mode. *(Changed from v2 twice: the attribute was previously specified as typeahead and is now a drop-down select, since the list is short and curated; and the "progressively expose the advanced condition builder" wording is dropped — there is no separate basic/advanced builder to reveal, only one builder that grows as conditions and groups are added.)*
- **FR3.2** A condition is expressed as **[attribute] [operator] [value(s)]**. Supported operators: **equals**, **does not equal**, **contains**, **does not contain**, **starts with**, and **Like** (wildcard / pattern match, e.g. `*.mybank.com`). The operator list is **attribute-aware** — only the operators that make sense for the selected attribute are shown (e.g. ProcessName offers equals / does not equal; URL and ApplicationTitle also offer contains, starts with, Like). The **value field is multi-select**, so one row can match several values — this subsumes the separate IN operator (see FR3.8). *(Reconciled with build: v2 listed only EQUALS / NOT EQUALS / LIKE; the shipped set adds contains, does not contain, and starts with, and is attribute-aware.)*
- **FR3.3** Curate the attribute list to the **High-criticality, scope-relevant attributes** from the Conditions inventory — the ones you'd actually target a rule by: **ProcessName, ApplicationName, ApplicationTitle, ActiveWindow, URL** (plus the conditional SAP attributes per FR3.4). Do not expose timestamps, IDs, or user-identity attributes here — they aren't scoping dimensions. **The exact attribute list is still to be validated with Product** — it was curated from the Conditions inventory by criticality, not confirmed against how Admins actually target rules in the field. *(Changed from v2, which also listed **EventType** and **TargetElementName**. Both are removed: a scope answers "**where** does this rule apply", and those two describe **what happened inside** a matched context — that belongs to the capture level (US4/US5), not to scoping. Keeping them invited rules that mixed the two axes.)*
- **FR3.4** **Conditional attributes.** **SAP and UIAA** attributes appear in the picker **only when their source is enabled** (both ship off by default); hide them otherwise so non-SAP / non-UIAA customers aren't shown irrelevant fields. **Browser-extension / Web-DOM attributes are not gated** — extensions ship on by default, so those fields are always shown (FR12.1). **Which attributes each source contributes, and whether hiding rather than disabling them is right, is still to be validated with Product** — hiding keeps the list clean but makes the capability undiscoverable to an Admin who doesn't already know the integration exists.
- **FR3.5** **Add comparison** — add a single condition row.
- **FR3.6** **Add group** — group conditions with an **AND / OR** combinator. Groups are **nestable, but capped at 2 levels below the root** — so the deepest expressible structure is `A OR (B AND (C OR D))`. "Add group" is offered only while that depth allows it, and "Wrap in group" only when the result would stay within the cap. *(Changed from v2's unqualified "nestable": unlimited nesting produces trees that are hard to read and hard to trust for a non-engineer Admin, while 2 levels covers the realistic targeting cases. Supersedes the earlier one-level cap of decision #26; see decision #33.)*
- **FR3.7** *(Removed — negation is not supported.)* Earlier versions specified an **Add negation (NOT)** action to wrap a condition or group and invert it. This has been **removed from the design**. Inversion is expressed directly through the **negative operators** (does not equal, does not contain) combined with the **multi-select value** (FR3.2), which covers the practical cases without a NOT wrapper. *(Change from v2: the "Add negation (NOT)" action, and the per-group NOT toggle, are gone. Trade-off: group-level negation such as `NOT (A AND B)` must now be hand-expanded to `(NOT A) OR (NOT B)`.)*
- **FR3.8** **Match a list of values (IN).** An attribute can be matched against **any value in a list**. This is realised through the **multi-select value field** (FR3.2), not a distinct IN operator/button: equals + multiple values = match any (OR-ed EQUALS); does not equal + multiple values = exclude all. *(Reconciled with build: IN is expressed via the multi-select value, not a separate operator.)*
- **FR3.9** **Per-node actions — the contents of the "more actions" (`⋮`) menu vary by node type and nesting depth.** Every condition and every non-root group carries its own `⋮` menu; what it offers is **not** the same everywhere, and developers should treat the matrix below as the specification rather than assuming one shared menu:

  | Node           | Where it sits                             | `⋮` menu offers                                   |
  | -------------- | ----------------------------------------- | ------------------------------------------------- |
  | **Condition**  | at root level (depth 0)                   | **Wrap in group** · **Delete condition**          |
  | **Condition**  | inside a group (depth 1)                  | **Wrap in group** · **Delete condition**          |
  | **Condition**  | inside a nested group (depth 2 — the cap) | **Delete condition** only                         |
  | **Group**      | depth 1                                   | **Delete group** only                             |
  | **Group**      | depth 2 (the cap)                         | **Delete group** only                             |
  | **Root group** | —                                         | *no menu* — the root cannot be deleted or wrapped |

  Rules that produce the matrix, so the behaviour is derivable rather than memorised:
  - **Wrap in group** is offered only when **both** hold: (a) wrapping the node would keep the tree **within the 2-level cap** (FR3.6) — which is why it disappears at depth 2; and (b) **at least one condition in the scope is complete**, since wrapping an empty condition is meaningless (progressive disclosure).
  - **Delete is always offered** on any deletable node — regardless of depth, and regardless of whether the node is complete. A half-filled condition and a deepest-level node must both remain removable; the `⋮` button is therefore **always present and always enabled**, never gated behind the completeness lock that hides Wrap.
  - **Groups never offer Wrap** — a group is already a group, so wrapping it would only add depth for no expressive gain.
  - **Deleting a group deletes its contents** with it. Deleting the **last remaining condition** in the root leaves a single empty condition row rather than an empty scope, since a rule requires at least one condition (FR3.11).
  - Negation is absent from every menu — inversion lives in the operators (FR3.7).
  *Implementation note (2026-07-29):* the prototype currently gives **conditions** a `⋮` menu as specified, but gives **groups a direct delete button with no menu**. The two need aligning — either add the single-item `⋮` menu to groups for affordance consistency, or keep the direct button on groups and accept two affordances. Trade-off: a `⋮` revealing exactly one item costs an extra click and hides a one-item list, which is why decision #28 originally kept delete as a direct control; decision #34 moved *condition* delete into the menu only because that row had four competing trailing controls, which a group header does not.
- **FR3.11** **Validation.** Flag incomplete conditions (missing attribute, operator, or value) inline. A created rule **requires at least one condition** — an empty scope is not allowed, because the catch-all case is already served by the Default rule.
- **FR3.12 - (Good to have)** **Plain-language read-back of the scope, inside the rule editor.** Show a **read-only** restatement of the scope expression beneath the condition builder, using the **same attribute labels as the dropdowns** and **explicit parentheses** for grouping — e.g. *"Process name = saplogon.exe OR (URL contains payroll AND (Application title = Chrome OR Application title = Edge))"*. It updates live as the scope is edited.
  - **Only shown once there is more than one condition.** A lone condition has no precedence to disambiguate, so a summary would merely restate the row above it.
  - **Read-only, deliberately.** An editable expression field would require a parser, syntax-error states and two-way sync with the tree — effectively teaching Admins a query language. The builder stays the single way to author a scope.
  - Incomplete conditions degrade to `… = …` rather than being hidden, so the read-back always reflects the tree as it actually stands.
  - *(Replaces the intent of the removed FR3.10, but relocated: a summary is unusable in a card-width line yet valuable in the editor, where its usefulness grows with nesting depth — precisely the case the stacked builder can only imply. The current Advanced editor already offers a text view of conditions, so this also preserves continuity for existing Admins. See decision #43.)*
- **FR3.13** **Per-attribute "how to find this value" help — required.** Each condition row carries a small **info affordance next to the value field** giving guidance specific to the **selected attribute**: where to obtain that value on the user's machine, plus a concrete example. This is **required, not optional** — an Admin writing a scope frequently does not know that *Process name* means the executable name, or where to read it, and the failure is **silent**: a wrong process name produces a rule that simply never matches, with no error to diagnose. Suggestions/typeahead (FR3.1) cover the common values; this covers the case where the value the Admin needs is **not** in the suggestion list.
  - **Trigger.** Opens on **hover** and on **keyboard focus** — the icon is focusable, so the guidance is reachable without a mouse. Dismisses on mouse-out, blur, or scroll.
  - **Content follows the attribute** and updates when the attribute changes. Before an attribute is chosen, show a generic fallback rather than nothing.
  - **Where the attribute supports wildcards**, the help says so — keeping the `*` hint next to the field where it is used rather than only in the operator list (FR3.2).
  - **Copy as built** (the source of truth for implementation):

    | Attribute            | Help text                                                                                                     |
    | -------------------- | ------------------------------------------------------------------------------------------------------------- |
    | Process name         | The app's executable name. Find it in Windows Task Manager → Details tab (e.g. `saplogon.exe`, `chrome.exe`). |
    | Application name     | The friendly app name from the title bar or Task Manager → Processes (e.g. Google Chrome).                    |
    | Application title    | Text shown in the window's title bar (e.g. "Payroll"). Use `*` as a wildcard.                                 |
    | Active window        | The full active-window title — copy it from the window's title bar. Use `*` as a wildcard.                    |
    | URL                  | The web address — copy it from the browser address bar. Use `*` as a wildcard (e.g. `*.mybank.com`).          |
    | SAP transaction code | The SAP transaction code from the SAP command field (e.g. `VA01`, `ME21N`).                                   |
    | SAP program          | The SAP program/report name (e.g. `SAPMV45A`).                                                                |
    | *(none selected)*    | Enter the value to match. Pick from the suggestions, or type your own.                                        |

  - *(Already built in the prototype; recorded here because it was implemented under decision #27 but never written into the user story. Any new scope attribute added under FR3.3 must ship with its own help text — the generic fallback is for the no-attribute-selected state, not a substitute.)*

---

## User Story 4

**As an Admin, I want to choose what a rule captures and see plainly what that means, so I'm confident the rule collects the right data.**

**Functional requirements:**

- **FR4.1** For each rule, the Admin selects one **capture level: Full, Custom, or Deny.** A **new rule opens with Custom pre-selected** — never with nothing selected. Custom is the privacy-safe middle option (FR4.4: interaction events on, content and screenshots off), so a pre-selection the Admin doesn't engage with can only ever *under*-capture, never quietly widen capture. It also keeps the "what this captures" preview (FR4.3) populated from the moment the dialog opens, rather than showing an empty panel until a level is picked. The Admin can switch to Full or Deny at any point. *(Changed from v2, which was silent on this, and from decision #17's "no tier preselected"; superseded by decision #44.)*
- **FR4.2** **Full** and **Deny** are **locked presets** (not editable); **Custom** is the only editable level.
- **FR4.3** Show a persistent **"what this captures" preview** for the selected level — **for Full and Custom** (Deny is the exception; see FR4.5). Events and logs are **combined inside the capture level** (per decision record #8/#15): the preview has **two sections**, listing **actual fields organised into groups** (not a flat dump), using the inventory groupings:
  - **Events** (which interactions are recorded): Navigation & window · Interaction · Content & clipboard · Scroll · Session & lifecycle.
  - **Data fields** (attributes logged per event): Identity · Timestamps & IDs · App & window context · Element / interaction · Content / input · Web / DOM · Screenshot dimensions · Coordinates & geometry · Versioning & meta · SAP family · UIAA family · Custom.
  *(The grouped, two-section preview directly addresses the Full/Usage-only confusion both VEs hit in testing — the Admin can see which events and which data fields each level actually collects.)*
- **FR4.4** **Custom** defaults to **interactions on, content/screenshots off** (safe-by-default) — the Admin turns content capture on deliberately.
- **FR4.5** **Deny** captures **nothing** for the rule's scope — a functional level used to exclude an app/URL from an otherwise-broad rule.
  - **Deny shows no field inventory and no screenshot control.** Both would render locked to "off"/"none", so the preview of FR4.3 does not apply here: instead of the event and data-field families, show a **single statement** confirming that no events are recorded, no data fields are logged and no screenshots are taken for anything this rule matches — plus a pointer to Full or Custom for anyone who landed on Deny by mistake.
  - **A statement, not blank space.** An empty region inside the dialog reads as broken or half-loaded; the statement carries the same reassurance the locked list used to, in one sentence.
  - *Why this doesn't contradict FR4.3:* the preview exists to resolve the **Full vs Custom** comprehension failure both VEs hit in testing (decision #23). Deny has no such gap — the answer is trivially "nothing" — so ~1.7 screens of disabled controls restated one word and invited futile clicking. *(Changed from v2, which applied the preview to all three levels; see decision #46.)*
- **FR4.6** Situational groups (**SAP, UIAA**) appear in the preview **only when their source is enabled**; noise groups are not surfaced by default. The **Web / DOM** group is always shown, not gated, since extensions are on by default (FR12.1).

---

## User Story 5

**As an Admin, I want to edit exactly which fields a Custom rule captures, so I can tune data collection and keep privacy-sensitive fields off unless I need them.**

**Functional requirements:**

- **FR5.1** The Custom editor is **only reachable when the level is Custom** (Full/Deny are locked, per FR4.2). It edits **both sections** of the capture level — **Events** (which interactions to record) and **Data fields** (attributes logged per event) — mirroring the two-section preview (FR4.3).
- **FR5.2** Present both sections in the **same groups as the preview**. In **Events**, each event group (Navigation & window, Interaction, Content & clipboard, Scroll, Session & lifecycle) is **toggleable on/off**. In **Data fields**, each family (Identity, App & window context, Element/interaction, Content/input, Web/DOM, etc.) and each field within it is **individually toggleable**.
- **FR5.3** Provide a **whole-family / whole-section toggle** (turn an entire event group or data-field family on/off in one action) in addition to per-field toggles.
- **FR5.4** **Default state = interaction events on, content fields + screenshots off** (FR4.4). Content/input fields (EnteredText, ClipboardText, SelectedText, etc.) are **flagged as privacy-sensitive** in the UI.
- **FR5.5** **Conditional & rarely-used groups.** **SAP and UIAA** families appear **only when their source is enabled** (both off by default). The **Web / DOM** family is always shown, since extensions ship on (FR12.1). Noise groups (Scroll, Coordinates & geometry, Screenshot dimensions) are **hidden behind a "show rarely-used fields" disclosure** — not surfaced by default.
- **FR5.6** **Screenshot mode** is part of the Custom editor: the Admin selects **none / active window / full desktop / all**. (This is a rule-level setting, not just a field toggle.) Where a mode other than "none" is chosen, captured screenshots are uploaded to the **Image Service Bucket** configured in Data Connection (FR9.2) — surface a hint/dependency so the Admin knows a destination bucket must be set for screenshots to be stored.

---

## User Story 6

**As an Admin, I want to redact sensitive content from captured data, so that PII and regulated data never leave the client.**

**Functional requirements:**

- **FR6.1** Ship **pre-set patterns**. **Enabled out of the box:** email addresses, social security numbers, credit card numbers. **Shipped but OFF by default:** Redact Windows username, Redact machine name — because **identity fields are pseudonymised by Hashing instead** (see US7 and FR7.9). This avoids identity being redacted to `*`** and thereby making its hash meaningless; an Admin who prefers full anonymisation over joinable pseudonyms can turn these two presets on.
- **FR6.2** The Admin can **create a new pattern** and **edit any pattern — including the pre-sets**: name, description, expression, action and scope are all editable. Every pattern has the same shape; a pre-set is only a pattern that ships with the product.
  - Pre-sets **cannot be deleted** (their protection is the point), but everything about how they match and what they do is the Admin's.
  - *(A build in 2026-08-05 briefly made pre-set expressions read-only, on the reasoning that a customer editing the credit-card regex could silently break it. Reverted the same day: customers do want their own expressions, and a locked matcher forces them to duplicate a rule to change one character. FR6.2 as originally written was right.)*
- **FR6.3** Pattern editor fields: **Pattern name** (required), **Description** (optional), **Regular expression** (required, editable; supports tokens like `{{username}}` and raw regex).
- **FR6.4** **Action** per pattern — what happens to a match. Four options, each stating its consequence:
  - **Mask completely** — every character replaced.
  - **Mask all but the last 4** — keeps the final four characters. The reason card numbers default to this: the last four are often needed to reconcile a record, and are not identifying on their own.
  - **Remove the value** — deleted, nothing left behind.
  - **Replace with a label** — fixed text such as `[redacted]`. The label is **required** when this action is chosen.
  - *(Expanded from v2's two options — asterisk mask or a tag. Partial masking and outright removal both exist in Sentry, Datadog and Google Cloud DLP, and partial masking is the one the card pattern actually needs.)*
- **FR6.5** **Where a pattern looks.** Each pattern carries a per-attribute scope, shown as an **always-open accordion** — the same family/parent-toggle pattern as the capture-rules field families and the hashing picker. There is **no All/Selected mode switch**.
  - **Everything is on by default.** A new pattern looks in every maskable attribute; the Admin narrows it by turning attributes off, group by group or individually.
  - **Grouped, each group with a parent toggle** (all-on / mixed / off): **Captured text** · **SAP** · **UI Automation**. The maskable set is **engine-defined, not Admin-defined**: Comment · Entered text · Clipboard text · Selected text · Active window · URL · Target element name · Target element value · Target link URL · Web page extractions · Element name (SAP) · Element text (SAP) · Window name (SAP) · User (SAP) · Control name (UIAA) · Control value (UIAA) · Help text (UIAA).
  - **The SAP and UI Automation groups are shown even when their source is off** — a deliberate departure from the producer→consumer rule used elsewhere. Redaction is a fail-safe: an Admin must be able to configure "mask these SAP fields" *before* SAP is enabled, so that turning SAP on later does not expose those fields unredacted until every pattern is revisited. See decision #60.
  - **Attributes the capture rules match on are not in the set** — `ProcessName` and similar — because redacting them would stop the Admin's own scope conditions matching. The engine excludes them and the UI cannot offer them.
  - **A pattern with every attribute off is invalid** and blocks Save; it would match nowhere and fail silently. *(Reworked from v2 and from an interim All/Selected two-mode design — see decision #58.)*
- **FR6.6** Patterns apply **top-to-bottom in list order**; the Admin can **reorder** (move up/down). Order matters — patterns apply sequentially.
- **FR6.7** The Admin can **delete** a pattern (confirmation dialog, per FR2.6).
- **FR6.8** Data Redaction is a **project-level (global) area**, applied across all rules; redaction runs **on the client before upload**.
- **FR6.9** **Try it — test against a pasted sample.** The pattern editor carries a sample box and a live result, so an Admin can see what a pattern does before saving it.
  - **Scoped to pasted text, deliberately.** It does not preview real captured data — that needs no data access, no infrastructure, and no waiting for a capture to happen. It de-risks the one thing that genuinely breaks: a wrong expression.
  - **Only the pattern being edited is applied**, and the UI says so — otherwise an Admin sees an email survive their email rule and assumes it is broken, when another pattern handles it.
  - **It scrolls with the form and is marked off by a divider** — not a pinned panel. It is a scratchpad, and the UI states that nothing in it is saved.
  - Patterns whose expression is a `**{{token}}**` resolved on the user's machine cannot be tried here; the box is replaced by an explanation.
  - *(No longer an enhancement — built 2026-08-05. Worth noting none of Sentry, Datadog or Google Cloud DLP offers a preview, so this is a differentiator rather than table stakes.)*

---

## User Story 7

**As an Admin, I want to hash sensitive attributes across all captured data, so identifying values are pseudonymized everywhere while staying joinable for analysis.**

**Functional requirements:**

- **FR7.1** A global **"Hash selected attributes"** master toggle (on/off for the whole project).
- **FR7.2** Display **only content/privacy-relevant attributes** — do **not** list non-sensitive fields (timestamps, IDs, ProcessName, geometry/coordinates, versioning, Custom). The curated set below is the **design's working list and must be validated with Engineering and Product before implementation** — which attributes the engine can actually hash, and which are privacy-relevant enough to warrant it, is their call to confirm:
  - **Identity:** SystemUser, UserId, MachineName.
  - **Content / input:** EnteredText, ClipboardText, ClipboardContentType, SelectedText, TargetElementValue, Comment, KeyboardCommand.
  - **Potentially-identifying context:** ApplicationTitle, ActiveWindow, ActiveElementName, TargetElementName, URL, WepPageExtractions, DomPath.
- **FR7.3** **Only the Identity group is on by default** — System user, User ID, Machine name. The other groups (Content / input, Potentially identifying context) ship **off**, behind a **"Show other attributes"** disclosure, and are toggled on only if the Admin needs them. Each group has a **parent toggle** (all on / mixed / off), mirroring the capture-rules field families; there are no separate select-all / select-none buttons.
  - **The attributes-to-hash section is hidden entirely while the master toggle is off** — there is nothing to configure until hashing is on.
  - *(Changed from v2's "all displayed fields checked by default". Ankit, Lead VE, 2026-07-13: hashing is used "for system users and machine ids… nothing else." Defaulting all 17 on contradicted the one piece of field evidence we have, and over-broad hashing was itself a named pain point — a user found the feature useless because it swallowed whole subject lines. See decision #59.)*
- **FR7.7** Applies **globally across all rules** (project-level), consistent with Redaction being global — regardless of a rule's capture level.
- **FR7.8** Include the **SAP and UI Automation privacy-relevant fields** (e.g. ElementTextSAP, ElementLabelSAP, Value_UIAA, Name_UIAA; not the source's structural / geometry fields), and **show them even when that source is disabled** — the same fail-safe inversion of the producer→consumer rule used in redaction scope (decision #60). An Admin must be able to say "hash these SAP fields" *before* SAP is enabled, so that turning it on later does not send those values unhashed until every setting is revisited. *(Changed from v2, which showed a source's fields only once it was enabled.)*
*(FR7.4 select-all/none and FR7.6 analysis-scope warning removed 2026-08-05; FR7.5 removed as it restated FR7.9's deterministic-hashing point. IDs retired, not reused.)*
- **FR7.9** (to confirm) **Order of operations with Redaction:** redaction is applied **first** (mask/remove PII), then hashing — so redacted values are never hashed raw. By default the two features **do not overlap on identity**: identity fields (SystemUser, MachineName, UserId) are **hashed, not redacted** (the identity redaction presets ship off — FR6.1), so identity produces a stable joinable hash rather than `*`**. If an Admin turns an identity redaction preset back on, redaction wins for that field and its hash is voided — surface this trade-off where the presets are toggled.
  - **FR7.9a — (to be validated with Eng) the UI must remove the contradiction, not explain it.** Where an **enabled redaction pattern already covers an attribute**, that attribute is shown as **unavailable for hashing**, with the reason stated inline and naming the pattern responsible — e.g. *"Already redacted by **Windows username** — hashing would have nothing left to hash."* The Admin is never asked to choose between two settings that cannot both apply. This is preferable to teaching the precedence rule: a rule the Admin has to remember is a rule they can get wrong, whereas an option that isn't offered cannot be.

---

## User Story 8

**As an Admin, I want to author the consent notice employees see, so data capture is transparent and lawfully based.**

**Functional requirements:**

- **FR8.1** User Consent is a **global (project-level) area**.
- **FR8.2** **Consent Text** editor, pre-filled with an **editable example template** covering the six standard sections — purpose of processing, legal basis, categories of personal data, recipients, retention, and contact — clearly marked as an example to be adapted by the project lead.
- **FR8.3** **Link to Additional Information** (optional) — a URL field (e.g. the company privacy policy).
- **FR8.4** **Label of Consent Checkbox** — editable text, defaulting to "I have read and agree to the above".
- **FR8.5** The consent is shown to employees **on first launch (welcome page)** and remains accessible in the client's **Privacy Settings**.

---

## User Story 9

**As an Admin, I want to review and adjust where captured data is sent and how it's cached, so the client connects to the right project without me setting it up from scratch.**

*(Low-touch screen — most Admins rarely change it. All values are pre-filled; the Admin edits only if needed.)*

**Functional requirements:**

- **FR9.1** One screen, **two sections**: Platform Upload and Caching. **All fields pre-filled**; every field is editable.
  - **Out of scope:** the product also carries a **Compatibility** section here (*Use Old Data Push API*, *Use Old Image Upload API*). These are legacy-API fallbacks for older platform versions, not configuration decisions an Admin makes about capture, and they are **deliberately excluded** from this redesign. Confirmed out of scope 2026-08-04. The same applies to Client Behaviour's *Use Legacy Screenshot Capturing* (FR10.1).
  - *Open:* the product's Caching section also has **Maximum Cached File Size (optional, GB)**, which FR9.3 does not list. Not built pending confirmation.
- **FR9.2** **Platform Upload** — Send Data to Celonis Platform (master toggle), Data Pool ID, Celonis Platform Team Subdomain, Server ID, Target Table Name, Image Service Bucket ID, Update Cloud Period (minutes).
- **FR9.3** **Caching** — Encrypt Local Data, Path for Transfer File Cache (**no Browse button — see note**), Number of Entries Limit, Timer Limit (minutes), Timeout (seconds), Auto Upload Old Cached Files, Maximum Cached File Age (optional, days).
  - **No Browse button, despite the desktop app having one.** In the desktop client, Browse picks a folder on the machine that is about to record. Here the Admin is in a **browser**, setting a path that applies to **other people's machines** — a picker would open on the Admin's own computer and let them choose a folder that may not exist on any end user's device. The help text explains that Windows variables such as `%USERPROFILE%` are resolved on the user's machine instead. *(FR9.3 inherited "with Browse" from the desktop UI without accounting for the change of surface.)*
- **FR9.4** Follows the global Save and inline-validation behaviour (US1, FR1.3).

---

## User Story 10

**As an Admin, I want to control how and when the client records, so capture fits our environment and can be validated during setup.**

*(Simple screen. All values pre-filled; the Admin edits only if needed.)*

**Functional requirements:**

- **FR10.1** One screen, **three sections**: Recording Behaviour, View Captured Events, Startup Mode.
  - **Out of scope:** the product's Logging screen also carries a **Compatibility** section (*Use Legacy Screenshot Capturing*), excluded on the same grounds as FR9.1's — a legacy fallback, not a capture decision. Confirmed out of scope 2026-08-04.
- **FR10.2** **Recording Behaviour** — general capture settings: Snippet Split Time (secs), Idle Waiting Time (mins), Alive Interval (mins), Use Native URL Retrieval, and the **UIAA** control.
- **FR10.3** **Prominently present the UIAA (UI Automation Accessibility) toggle** with a **callout/description of its benefit** — some users didn't know what it was for. Enabling it **reveals the UIAA attribute family inside Capture Rules** (same producer→consumer conditional display as SAP). Include the companion **"Applications to exclude from UIAA"** field.
- **FR10.4** **View captured events** — a toggle ("Show captured events in client") with **descriptive text**. It lets a user **see what has already been recorded on their own machine**.
  - **Renamed from "Live Event Monitor"** (2026-08-05). Every word of the old name misled, and each one produced a documented error: **"Live"** implied real-time streaming and produced the pre-rollout-validation claim; **"Monitor"** implied one party watching another and produced the Admin-only claim; **"Event"** is internal vocabulary an end user would not recognise. The new name states what the feature does and for whom.
  - **Enabling it only makes the control available — it does not open or display anything.** The client gains a control the user can choose to open. An Admin reading "Show…" could reasonably expect a panel to appear on the user's screen; it does not.
  - **It is reactive, not proactive.** It reports activity that has been captured and sent, so it confirms *what was collected*. It does **not** test a rule before rollout and cannot tell an Admin in advance whether a scope will match. The copy must not promise pre-rollout validation. *(v2 described it as "used to validate that rules capture the right data before rollout" — wrong, and it reached the prototype before being caught.)*
  - **It is project-wide, not per-person.** Turning it on shows the monitor to **every user in the project**; it **cannot** be limited to Admins or to a subset of people. The copy must say so, because the opposite is the natural assumption for a diagnostic-looking feature. *(v2 required the text to state the monitor "applies to Admin users only", and described permissions as being enforced on the Users & Invite page. Both were wrong — there is no per-user distinction to enforce.)*
  - **Customers have asked for per-person visibility, and it is currently not deliverable.** Limiting the monitor to named individuals would require the platform to tell each client which user it belongs to — **cloud → client** communication, which does not exist today (data flows client → cloud only) and which some customers block inbound at the network boundary. Raised by PM 2026-08-04, unresolved. Treat per-person visibility as **out of scope** until Engineering confirms a mechanism; the project-wide toggle itself is deliverable and unaffected.
  - Both corrections were made 2026-08-05; see decision #55.
- **FR10.5** **Startup Mode** — choose **Auto-start when computer starts** or **Manual-start by users**, each with explanatory subtext; plus a **"Minimize window when it starts"** option.
- **FR10.6** Follows the global Save and inline-validation behaviour (US1, FR1.3).

---

## User Story 11

**As an Admin, I want to define custom attributes end users pick when they start recording, so every capture is tagged with context like which team ran it.**

*Purpose: when an end user starts recording, the client prompts them to select from these custom attributes — e.g. Label "Team", value "HR-Payroll" — and all captures in that session are attributed accordingly (e.g. executed by someone from Payroll).*

**Functional requirements:**

- **FR11.1** The area opens with a designed **empty state** when no attributes are defined yet — not a blank panel. It carries four things: an **icon**, a **title** naming what is absent ("No user attributes yet"), a **line explaining the consequence** (users go straight into recording without being asked anything, so nothing tags the session), and **no call to action of its own** — the create button already sits in the section header (FR11.2), and duplicating it would give one action two homes. The same empty-state pattern is used wherever a collection can be empty (FR12.2). *(Changed from v2, which only required that the section be "empty" — an empty region reads as broken or half-loaded, and it leaves the Admin with nothing to act on.)*
- **FR11.2** A clear **Create custom attribute** button.
- **FR11.3** Creating an attribute: enter a **Label** (required, e.g. "Team") and **add multiple Values** (at least one required, e.g. Payroll, Talent Acquisition, Finance).
- **FR11.4** Option to **make the field mandatory** for end users ("Make this field mandatory for users").
- **FR11.5** **Maximum of 5 custom attributes.** Once 5 exist, disable the Create action and clearly state the limit.
- **FR11.6** **Inform the user about how these work and their limits** — descriptive text explaining the end-user prompt behaviour and the 5-attribute cap, so the purpose isn't guessed at.
- **FR11.7** The Admin can **edit** and **delete** existing attributes (delete via confirmation dialog, per FR2.6).
- **FR11.8** Follows the global Save and inline-validation behaviour (US1, FR1.3).

---

## User Story 12

**As an Admin, I want to enable browser extensions and define what data to pull from specific web pages, so browser-based work is captured with the right context.**

**Functional requirements:**

- **FR12.1** **General** — a **"Receive Data From All Extensions"** master toggle. The extension/DOM attributes (URL, WepPageExtractions, DomPath) live in the **always-shown Web / DOM field family** in capture rules — they are **not** source-gated behind this toggle, because extensions ship **on by default** (decision #16-era rollout assumption), so gating would hide fields that are almost always relevant. *(Changed from v2, which described the family as revealed by the toggle — same producer→consumer pattern as SAP/UIAA. That gating was dropped once extensions became on-by-default; SAP and UIAA remain gated because they are off by default. See decision #61.)*
- **FR12.2** **Web Page Data Extractions** (Google Chrome & Microsoft Edge) — a list of extraction rules with an **Add Rule** action. When the master toggle is **on but no rules exist**, show the same designed **empty state** as FR11.1: icon, title and consequence, with **no button of its own** (Add Rule stays in the section header). Here the consequence line must actively **correct a likely misreading** — that no extraction rules means no browser capture. It does not: browser activity is still captured, and an extraction rule is only needed to read a *specific* value off a page. Without that sentence an Admin may add rules they do not need, or assume the extensions are not working. This section is **shown only when "Receive Data From All Extensions" is on** — **hidden** otherwise (not greyed/disabled), consistent with how all source-gated sections behave (SAP retrieval settings, UIAA fields).
- **FR12.3** Each extraction rule is defined by: **Key** (required — the name the extracted value is stored under), **URL** (required — the page the rule applies to), and **Path** (required — the element path/selector to extract from). Provide **inline guidance for Path creation with a worked example** (e.g. a sample selector/XPath), since users won't know the expected format.
- **FR12.4** **Validation.** Reject an **invalid URL** — the Admin cannot save a rule with a malformed URL; show the error inline. Required fields (Key, URL, Path) must be filled before the rule can be saved.
- **FR12.5** The Admin can **edit** and **delete** extraction rules (delete via confirmation dialog, per FR2.6).
- **FR12.6** Follows the global Save and inline-validation behaviour (US1, FR1.3).

---

## User Story 13

**As an Admin, I want to enable SAP data capture and tune its retrieval, so SAP GUI work is captured reliably.**

*(Simple screen. All values pre-filled; the Admin edits only if needed.)*

**Functional requirements:**

- **FR13.1** A **"Retrieve SAP Data"** master toggle. Enabling it **reveals the SAP attribute family inside Capture Rules** (ElementTextSAP, TransactionSAP, ScreenNumberSAP, etc.) — same producer→consumer conditional display as UIAA and Extensions. Keep the SAP fields hidden for non-SAP customers until this is on.
- **FR13.2** Show the **retrieval settings only when "Retrieve SAP Data" is on** (hidden otherwise). Settings are **pre-filled and editable**: Number of Retry Attempts, Waiting Time for Retry (ms), SAP Process Monitor Interval (ms).
- **FR13.3** **Dynamically Enable Native Windows Dialogs for SAP GUI Scripting** (toggle, off by default; shown with the other SAP settings when the master toggle is on).
- **FR13.4** Follows the global Save and inline-validation behaviour (US1, FR1.3).

---

## User Story 14 — *withdrawn*

~~As an Admin, I want to export, import, and generate the table DDL for a configuration.~~

**Withdrawn 2026-08-07 (decision #62).** The encoded (base64) export/import and the *Generate SQL CREATE TABLE* action are **not part of this product**. The only file exchange is the **human-readable** Download / Upload configuration file used for the approval round-trip (FR15.5 / FR15.11) — which serves the "reuse across projects" need without a second, machine-only format. The Compatibility legacy-API settings on Data Connection and Client Behaviour are likewise out of scope (see FR9.1 / FR10.1). *(FR14.1–FR14.5 retired; IDs not reused.)*

## User Story 15

**As an Admin at a regulated customer, I want configuration changes to be reviewed and approved before they take effect for users, so that capture settings cannot be changed unilaterally.**

*Context: customers with change-control obligations (e.g. investment banks) require sign-off before capture settings apply to their workforce. **The approval itself happens outside this application** — the Admin downloads the configuration, circulates it (email, Slack, an internal change-management ticket), and the approvers respond there. The app therefore cannot verify that approval occurred; its job is to make applying a **separate, deliberate, attested** act rather than a side effect of saving.*

**Functional requirements:**

- **FR15.1** **Save and Apply are separate actions.** **Save draft** persists the configuration without affecting any user; **Apply** is what pushes it to the client population. A configuration therefore has three states: **working** (unsaved edits) · **saved draft** · **applied (live)**. Clients keep running the **applied** configuration for as long as a draft sits unapplied.
- **FR15.2** **Rollout state is always visible**, beside the page title (not among the actions — it describes the configuration, not an action). The indicator answers **one** question: *does what I am looking at match what the machines are running?*
  - **Not applied** — nothing has ever been applied; no capture is running for this project. Neutral tone, no date.
  - **Live** — the screen matches the deployed configuration. Green, **no note** — the page subtitle already states when it went out.
  - **Draft** — a configuration is deployed, and the screen differs from it. **Neutral tone, not amber** — a draft is the normal condition while configuring, so amber would read as *something is wrong* for most of the Admin's working time. Note reads **"changes not yet applied"**.
  - **The comparison is screen-versus-deployment**, not saved-versus-deployment. An unsaved edit and an unapplied saved draft are indistinguishable from the machines' point of view, so both read **Draft**.
  - **The saved/unsaved distinction is the Save button's job** — it reads *"Save draft"* when there are unsaved edits and *"Draft saved"* when there are none. The status must **not** repeat it; doing so duplicates information rather than adding any.
  - **The note appears only in the Draft state**, where it names the outstanding action — *"changes not yet applied"*. 
  - **The page subtitle carries the rollout fact**, and it is **the same on every tab** — *"Last applied on 4 Aug 2026, 19:45"*, or *"Nothing has been applied yet — no activity is being captured."* before a first apply. It must **not** be area-specific: the subtitle sits under a page-level title, so text that changes as the Admin moves between tabs reads as though the page changed when only the tab did. 
- **FR15.3** **Apply always acts on the saved draft, and is unavailable while unsaved edits exist** (the button explains why: *"Save your draft first"*). This is deliberate: the artefact sent for approval is the saved draft, so the Admin cannot get sign-off, tweak something, and apply the tweaked version. It removes the need to fingerprint or diff the approved file.
- **FR15.4** **Apply asks for confirmation.** A dialog states plainly that the settings **take effect for every user in this project straight away, replacing whatever is running now**, with **Cancel** and a primary **Apply**; Escape cancels. **No inputs are captured** — no approver name, ticket reference or evidence.
  - **The copy must stay generic — it must not name review or approval.** 
  - The dialog is still what makes applying deliberate rather than a side effect of saving. The app cannot verify approval and must not imply that it does.
- **FR15.5** (should be validated with Eng & product) **Download configuration file** — available from **More actions** (FR1.4), this produces the artefact the Admin circulates for approval. It downloads the **saved draft** (the thing that will be applied), as **human-readable** content, with a timestamped filename in the client's existing format: `generated_from_basic_settings_YYYY-MM-DD HH_MM_SS.recconf`. **Readability is the requirement, not a preference** — an approver who has never used this product must be able to read what they are approving, which the base64-encoded export of FR14.2 cannot satisfy. The two are separate artefacts with separate purposes: this one for human review, FR14.2's for machine round-tripping.
- **FR15.6** **Apply is immediate.** Once confirmed, the configuration becomes the live one for all users; the confirmation copy says so plainly rather than implying a delayed rollout.
- **FR15.7** **Approval covers the whole configuration**, not individual areas. There is one Save, one Apply, and one live configuration spanning all six areas — a change to a redaction pattern and a change to a screenshot setting go through the same gate.
- **FR15.8** **Admins can apply.** No separate approver or publisher role exists in the product, because the approval step is external. Anyone who can edit the configuration can apply it.
- **FR15.9** **No configuration version history.** Only two stored snapshots are required — the current **draft** and the current **live** configuration. Client settings are configured a handful of times during initial setup and rarely revisited, so a version list, rollback and change history are **out of scope**.
- **FR15.10** Validity gates **both** actions. Because Save is blocked while the configuration is invalid (FR1.3), a draft is always coherent, and so is the file sent for approval; Apply inherits the same guarantee.
- **FR15.11** **Upload configuration file** — the counterpart to FR15.5, also in **More actions**. After sending a file for approval the Admin may carry on editing, so the saved draft can drift from what was actually signed off. Uploading the approved file **restores it exactly**, making the approved artefact and the applied artefact the same object again. 
  - **Lands in the working state**, not live. The Admin still has to **Save** the draft and then **Apply** — upload changes nothing for users on its own.
  - **Replaces the whole configuration**, so **warn before overwriting**, and say explicitly when **unsaved changes will be lost**.
  - (To confirm with Eng) **Validate and reject outright — never partially apply.** Unreadable JSON, a file that isn't a configuration, missing sections, no capture rules, or no Default rule are each reported by name, and the current configuration is left untouched.

---

*15 stories drafted. Validation is captured inline per area (FR1.3, FR3.11, FR12.4) rather than as a dedicated story. Open item: C1 — identity-field default (hash vs redact) — see note below. Parked: US14 import/export (FR14.2–FR14.4) pending Product confirmation of the use case.*