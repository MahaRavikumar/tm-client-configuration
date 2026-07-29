# Task Mining Client Configuration — Functional Requirements

**Format:** each entry starts with a **user story** (the Admin's intention) followed by the **functional requirements** — the capabilities the screen must have to achieve that intention.
**Status:** v3, in progress. User Stories 1–14 defined (all six config areas + config-file actions); gap/contradiction review applied. v3 reconciles Capture Rules with the built prototype: Default-rule level now editable — guarantee restated as **coverage, not capture**, plus a non-blocking warning when it is not Full (FR2.5, FR2.5a; knock-on fix to FR1.5), rule-name validation specified in full including the empty-on-create behaviour (FR2.2), attribute is a drop-down (FR3.1), operator set expanded and attribute-aware (FR3.2), EventType and TargetElementName dropped as scope attributes (FR3.3), IN via multi-select value (FR3.8), negation removed (FR3.7). Every create/edit flow now uses one **modal dialog** pattern with validity-gated Submit and revert-on-Cancel, the capture rule included (FR1.6). Deleting now **confirms instead of offering Undo** (FR2.6), and the rule-list card is stripped back to name + level badge + delete (FR2.3). Rationale and supersession history for all of the above is logged as decisions #31–#42 in `TM_Client_IA_Decision_Record.md`.
**IDs:** FRs are numbered per story (FR1.x, FR2.x…) for unique reference.

---

## User Story 1
**As an Admin, I want to configure client settings for a new project.**

**Functional requirements:**
- **FR1.1** Present the **6 config areas** and let the Admin move between them via a **left sub-nav**: Capture Rules, Privacy, Data Connection, Client Behaviour, User Attributes, Integrations. **Privacy** and **Integrations** are container areas whose sub-screens are presented as **tabs** — Privacy: Redaction · Hashing · Consent; Integrations: SAP · Extensions.
- **FR1.2** No landing page — the Admin lands directly on the **Capture Rules** area.
- **FR1.3** Persistent page header with a primary **Save** action (Save is **global**, across all areas) and an unsaved-changes state. There is **no autosave** — changes persist only on explicit Save. *(Open: confirm autosave feasibility with Engineering; going without it for now.)* Each area provides **inline validation** for fields that require it, blocking Save while a required field is invalid.
- **FR1.4** A **More actions** menu next to Save holds additional actions, including **import / export**. (No separate Configuration File tab.)
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
- **FR3.1** **Simple-first.** Start with a simple picker to name the application(s) and/or URL(s) the rule targets. The **attribute is chosen from a drop-down select** (the curated list in FR3.3); the **value uses typeahead** (with suggestions + free typing). Progressively expose the advanced condition builder only when the Admin needs more than a plain match. *(Changed from v2: the attribute was previously specified as typeahead; it is now a drop-down select, since the attribute list is short and curated.)*
- **FR3.2** A condition is expressed as **[attribute] [operator] [value(s)]**. Supported operators: **equals**, **does not equal**, **contains**, **does not contain**, **starts with**, and **Like** (wildcard / pattern match, e.g. `*.mybank.com`). The operator list is **attribute-aware** — only the operators that make sense for the selected attribute are shown (e.g. ProcessName offers equals / does not equal; URL and ApplicationTitle also offer contains, starts with, Like). The **value field is multi-select**, so one row can match several values — this subsumes the separate IN operator (see FR3.8). *(Reconciled with build: v2 listed only EQUALS / NOT EQUALS / LIKE; the shipped set adds contains, does not contain, and starts with, and is attribute-aware.)*
- **FR3.3** Curate the attribute list to the **High-criticality, scope-relevant attributes** from the Conditions inventory — the ones you'd actually target a rule by: **ProcessName, ApplicationName, ApplicationTitle, ActiveWindow, URL** (plus the conditional SAP attributes per FR3.4). Do not expose timestamps, IDs, or user-identity attributes here — they aren't scoping dimensions. *(Changed from v2, which also listed **EventType** and **TargetElementName**. Both are removed: a scope answers "**where** does this rule apply", and those two describe **what happened inside** a matched context — that belongs to the capture level (US4/US5), not to scoping. Keeping them invited rules that mixed the two axes.)*
- **FR3.4** **Conditional attributes.** SAP, UIAA, and browser-extension attributes appear in the picker **only when their source is enabled**; hide them otherwise so non-SAP / non-extension customers aren't shown irrelevant fields.
- **FR3.5** **Add comparison** — add a single condition row.
- **FR3.6** **Add group** — group conditions with an **AND / OR** combinator; groups are **nestable** to build compound expressions.
- **FR3.7** *(Removed — negation is not supported.)* Earlier versions specified an **Add negation (NOT)** action to wrap a condition or group and invert it. This has been **removed from the design**. Inversion is expressed directly through the **negative operators** (does not equal, does not contain) combined with the **multi-select value** (FR3.2), which covers the practical cases without a NOT wrapper. *(Change from v2: the "Add negation (NOT)" action, and the per-group NOT toggle, are gone. Trade-off: group-level negation such as `NOT (A AND B)` must now be hand-expanded to `(NOT A) OR (NOT B)`.)*
- **FR3.8** **Match a list of values (IN).** An attribute can be matched against **any value in a list**. This is realised through the **multi-select value field** (FR3.2), not a distinct IN operator/button: equals + multiple values = match any (OR-ed EQUALS); does not equal + multiple values = exclude all. *(Reconciled with build: IN is expressed via the multi-select value, not a separate operator.)*
- **FR3.9** Each node (condition or group) can be **deleted** individually and **wrapped into a group** in place.
- **FR3.10** Show a **plain-language summary** of the scope expression (e.g. "ProcessName = Chrome AND URL LIKE *.gmail.com") so the Admin can read back what the rule targets without parsing the tree.
- **FR3.11** **Validation.** Flag incomplete conditions (missing attribute, operator, or value) inline. A created rule **requires at least one condition** — an empty scope is not allowed, because the catch-all case is already served by the Default rule.

---

## User Story 4
**As an Admin, I want to choose what a rule captures and see plainly what that means, so I'm confident the rule collects the right data.**

**Functional requirements:**
- **FR4.1** For each rule, the Admin selects one **capture level: Full, Custom, or Deny.**
- **FR4.2** **Full** and **Deny** are **locked presets** (not editable); **Custom** is the only editable level.
- **FR4.3** Show a persistent **"what this captures" preview** for the selected level. Events and logs are **combined inside the capture level** (per decision record #8/#15): the preview has **two sections**, listing **actual fields organised into groups** (not a flat dump), using the inventory groupings:
  - **Events** (which interactions are recorded): Navigation & window · Interaction · Content & clipboard · Scroll · Session & lifecycle.
  - **Data fields** (attributes logged per event): Identity · Timestamps & IDs · App & window context · Element / interaction · Content / input · Web / DOM · Screenshot dimensions · Coordinates & geometry · Versioning & meta · SAP family · UIAA family · Custom.
  
  *(The grouped, two-section preview directly addresses the Full/Usage-only confusion both VEs hit in testing — the Admin can see which events and which data fields each level actually collects.)*
- **FR4.4** **Custom** defaults to **interactions on, content/screenshots off** (safe-by-default) — the Admin turns content capture on deliberately.
- **FR4.5** **Deny** captures **nothing** for the rule's scope — a functional level used to exclude an app/URL from an otherwise-broad rule.
- **FR4.6** Situational groups (SAP, UIAA, extension) appear in the preview **only when their source is enabled**; noise groups are not surfaced by default.

---

## User Story 5
**As an Admin, I want to edit exactly which fields a Custom rule captures, so I can tune data collection and keep privacy-sensitive fields off unless I need them.**

**Functional requirements:**
- **FR5.1** The Custom editor is **only reachable when the level is Custom** (Full/Deny are locked, per FR4.2). It edits **both sections** of the capture level — **Events** (which interactions to record) and **Data fields** (attributes logged per event) — mirroring the two-section preview (FR4.3).
- **FR5.2** Present both sections in the **same groups as the preview**. In **Events**, each event group (Navigation & window, Interaction, Content & clipboard, Scroll, Session & lifecycle) is **toggleable on/off**. In **Data fields**, each family (Identity, App & window context, Element/interaction, Content/input, Web/DOM, etc.) and each field within it is **individually toggleable**.
- **FR5.3** Provide a **whole-family / whole-section toggle** (turn an entire event group or data-field family on/off in one action) in addition to per-field toggles.
- **FR5.4** **Default state = interaction events on, content fields + screenshots off** (FR4.4). Content/input fields (EnteredText, ClipboardText, SelectedText, etc.) are **flagged as privacy-sensitive** in the UI.
- **FR5.5** **Conditional & rarely-used groups.** SAP, UIAA, and extension families appear **only when their source is enabled**. Noise groups (Scroll, Coordinates & geometry, Screenshot dimensions) are **hidden behind a "show rarely-used fields" disclosure** — not surfaced by default.
- **FR5.6** **Screenshot mode** is part of the Custom editor: the Admin selects **none / active window / full desktop / all**. (This is a rule-level setting, not just a field toggle.) Where a mode other than "none" is chosen, captured screenshots are uploaded to the **Image Service Bucket** configured in Data Connection (FR9.2) — surface a hint/dependency so the Admin knows a destination bucket must be set for screenshots to be stored.
- **FR5.7** Keep the **"what this captures" summary live** as the Admin toggles, so edits are legible immediately.

---

## User Story 6
**As an Admin, I want to redact sensitive content from captured data, so that PII and regulated data never leave the client.**

**Functional requirements:**
- **FR6.1** Ship **pre-set patterns**. **Enabled out of the box:** email addresses, social security numbers, credit card numbers. **Shipped but OFF by default:** Redact Windows username, Redact machine name — because **identity fields are pseudonymised by Hashing instead** (see US7 and FR7.9). This avoids identity being redacted to `***` and thereby making its hash meaningless; an Admin who prefers full anonymisation over joinable pseudonyms can turn these two presets on.
- **FR6.2** The Admin can **create a new pattern** and **edit any pattern — including the pre-sets** (name, description, and regex are all editable).
- **FR6.3** Pattern editor fields: **Pattern name** (required), **Description** (optional), **Regular expression** (required, editable; supports tokens like `{{username}}` and raw regex).
- **FR6.4** **Replacement method** per pattern: **asterisk mask** (`***`) or a **tag/label**.
- **FR6.5** Each pattern applies to a set of **captured content fields, pre-selected per pattern by default**; the Admin can **toggle off** fields they don't want that pattern to redact.
- **FR6.6** Patterns apply **top-to-bottom in list order**; the Admin can **reorder** (move up/down). Order matters — patterns apply sequentially.
- **FR6.7** The Admin can **delete** a pattern (confirmation dialog, per FR2.6).
- **FR6.8** Data Redaction is a **project-level (global) area**, applied across all rules; redaction runs **on the client before upload**.
- **FR6.9** *(Enhancement — not in current product)* **Test against a sample**: paste sample text and preview the redaction result before saving, to de-risk regex mistakes.

---

## User Story 7
**As an Admin, I want to hash sensitive attributes across all captured data, so identifying values are pseudonymized everywhere while staying joinable for analysis.**

**Functional requirements:**
- **FR7.1** A global **"Hash selected attributes"** master toggle (on/off for the whole project).
- **FR7.2** Display **only content/privacy-relevant attributes** — do **not** list non-sensitive fields (timestamps, IDs, ProcessName, geometry/coordinates, versioning, Custom). The curated set:
  - **Identity:** SystemUser, UserId, MachineName.
  - **Content / input:** EnteredText, ClipboardText, ClipboardContentType, SelectedText, TargetElementValue, Comment, KeyboardCommand.
  - **Potentially-identifying context:** ApplicationTitle, ActiveWindow, ActiveElementName, TargetElementName, URL, WepPageExtractions, DomPath.
- **FR7.3** All displayed (privacy-relevant) fields are **checked by default**.
- **FR7.4** **Select-all / select-none** bulk actions.
- **FR7.5** Hashing is **deterministic** (same input → same hash), so data stays **joinable** across events but de-identified.
- **FR7.6** Show the warning that **hashing limits analysis scope**, so the trade-off is explicit.
- **FR7.7** Applies **globally across all rules** (project-level), consistent with Redaction being global — regardless of a rule's capture level.
- **FR7.8** Where a source is enabled, include its **privacy-relevant fields only** (e.g. ElementTextSAP, ElementLabelSAP, Value_UIAA, Name_UIAA); hide the source's structural/geometry fields.
- **FR7.9** **Order of operations with Redaction:** redaction is applied **first** (mask/remove PII), then hashing — so redacted values are never hashed raw. By default the two features **do not overlap on identity**: identity fields (SystemUser, MachineName, UserId) are **hashed, not redacted** (the identity redaction presets ship off — FR6.1), so identity produces a stable joinable hash rather than `***`. If an Admin turns an identity redaction preset back on, redaction wins for that field and its hash is voided — surface this trade-off where the presets are toggled.

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
- **FR9.2** **Platform Upload** — Send Data to Celonis Platform (master toggle), Data Pool ID, Celonis Platform Team Subdomain, Server ID, Target Table Name, Image Service Bucket ID, Update Cloud Period (minutes). *(SQL generation lives only in More actions → Generate SQL 'CREATE TABLE' query, FR14.5 — not on this screen.)*
- **FR9.3** **Caching** — Encrypt Local Data, Path for Transfer File Cache (with Browse), Number of Entries Limit, Timer Limit (minutes), Timeout (seconds), Auto Upload Old Cached Files, Maximum Cached File Age (optional, days).
- **FR9.4** Follows the global Save and inline-validation behaviour (US1, FR1.3).

---

## User Story 10
**As an Admin, I want to control how and when the client records, so capture fits our environment and can be validated during setup.**

*(Simple screen. All values pre-filled; the Admin edits only if needed.)*

**Functional requirements:**
- **FR10.1** One screen, **three sections**: Recording Behaviour, Live Event Monitor, Startup Mode.
- **FR10.2** **Recording Behaviour** — general capture settings: Snippet Split Time (secs), Idle Waiting Time (mins), Alive Interval (mins), Use Native URL Retrieval, and the **UIAA** control.
- **FR10.3** **Prominently present the UIAA (UI Automation Accessibility) toggle** with a **callout/description of its benefit** — some users didn't know what it was for. Enabling it **reveals the UIAA attribute family inside Capture Rules** (same producer→consumer conditional display as SAP). Include the companion **"Applications to exclude from UIAA"** field.
- **FR10.4** **Live Event Monitor** — a toggle ("Show Live Event Monitor in Client") with **descriptive text**: it's a real-time view of the events the client is capturing, used to **validate that rules capture the right data** before rollout. The text must state the monitor **applies to Admin users only**. There is **no permission control on this screen** — who counts as an Admin is enforced elsewhere (the **Users & Invite** page); this toggle only decides whether the monitor is available in the client for those users.
- **FR10.5** **Startup Mode** — choose **Auto-start when computer starts** or **Manual-start by users**, each with explanatory subtext; plus a **"Minimize window when it starts"** option.
- **FR10.6** Follows the global Save and inline-validation behaviour (US1, FR1.3).

---

## User Story 11
**As an Admin, I want to define custom attributes end users pick when they start recording, so every capture is tagged with context like which team ran it.**

*Purpose: when an end user starts recording, the client prompts them to select from these custom attributes — e.g. Label "Team", value "HR-Payroll" — and all captures in that session are attributed accordingly (e.g. executed by someone from Payroll).*

**Functional requirements:**
- **FR11.1** The area opens with an **empty custom-attributes section** when none are defined yet.
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
- **FR12.1** **General** — a **"Receive Data From All Extensions"** master toggle. Enabling it **reveals the extension/DOM attribute family inside Capture Rules** (URL, WepPageExtractions, DomPath, ExtensionName) — same producer→consumer conditional display as UIAA and SAP.
- **FR12.2** **Web Page Data Extractions** (Google Chrome & Microsoft Edge) — a list of extraction rules with an **Add Rule** action; opens with an **empty state** when none are defined. This section is **shown only when "Receive Data From All Extensions" is on** — **hidden** otherwise (not greyed/disabled), consistent with how all source-gated sections behave (SAP retrieval settings, UIAA fields).
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

## User Story 14
**As an Admin, I want to export, import, and generate the table DDL for a configuration, so I can reuse configs across projects and set up the destination data model.**

**Functional requirements:**
- **FR14.1** These actions live behind the **More actions** menu next to Save (per FR1.4) — **not** a separate Configuration File tab.
- **FR14.2** **Export configuration as JSON** (base64-encoded) — produces a portable file representing the full configuration.
- **FR14.3** **Import configuration from JSON** (base64-encoded) — loads a configuration into the editor as the working (unsaved) state; it does not take effect until the Admin Saves.
- **FR14.4** **Import validation** — reject malformed or invalid JSON with a clear error and **do not partially apply**. Because import **replaces the current configuration**, warn the Admin before overwriting (especially with unsaved changes).
- **FR14.5** **Generate SQL 'CREATE TABLE' query** — produces the DDL for the target table (aligned to the Target Table Name in Data Connection, FR9.2), so the Admin can create the destination table in the data pool. Offer copy-to-clipboard.

---

*All 14 stories drafted. Validation is captured inline per area (FR1.3, FR3.11, FR12.4) rather than as a dedicated story. Open item: C1 — identity-field default (hash vs redact) — see note below.*
