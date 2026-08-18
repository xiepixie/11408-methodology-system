# Homework Diagnostic Execution State Machine

## Purpose

Keep coverage mandatory while making expensive diagnosis/persistence conditional. Clean work must not be forced through empty MCP/local-write states.

## Execution graph

```text
INPUT
→ A Coverage + Fidelity
→ B Depth Classification
   ├─ clean → C1 Lightweight Feedback → J Closure
   ├─ local-fix → C2 Local Repair → J Closure
   └─ deep-diagnosis
        → D Learner-Route Diagnosis
        → E Mental-Model / Local-Owner Gate
        → F Improvement
        → G Retention Value Gate
        → H MCP Resolution
        → I Local Cognitive Resolution + Validation
        → J Closure
```

Maintain an internal ledger only for states that actually apply.

| State | Required evidence before advancing |
|---|---|
| A Coverage + Fidelity | every legible problem accounted for; prompt/options reconstructed enough to grade |
| B Depth | each problem = clean / local-fix / deep-diagnosis |
| C1 Clean | concise verdict; no invented diagnosis |
| C2 Local repair | exact bad step + correction + optional check |
| D Diagnosis | First Divergence + hypothesis + competitor + retest |
| E Model/local gate | Owner/provisional-model/audit outcome when triggered |
| F Improvement | process repair + at most one better user-facing route + verification |
| G Retention value | no archive value / archive candidate / possible exact stored review-update |
| H MCP | final archive/reuse/review/update/create outcome when MCP resolution applies |
| I Local | local state + completed writes/validation when applicable |
| J Closure | only completed actions reported |

Do not enter H or I merely to produce `No action` for a clean/local-fix problem.

## A — Coverage + Fidelity gate

Pass only when:
- all uploaded images have been inspected;
- all legible problem numbers/subproblems have been identified;
- continuations and crossed-out work are resolved as far as the image allows;
- uncertain handwriting is explicitly marked uncertain;
- the exact prompt is reliable enough to grade.

For multiple-choice / proposition questions, require an internal option ledger:

```text
A: exact proposition + load-bearing conditions
B: exact proposition + load-bearing conditions
C: exact proposition + load-bearing conditions
D: exact proposition + load-bearing conditions
```

Inspect domain/existence, quantifiers, strictness, implication direction, necessary/sufficient status, boundary cases, and hidden assumptions. If an unreadable symbol can change the answer, mark that judgment blocked instead of guessing.

## B — Depth gate

### clean
Use when the answer and route are sound enough and no material scoring/control/model signal appears.

### local-fix
Use when the main issue is an isolated execution/notation/copy slip or small inefficiency and immediate correction is enough.

### deep-diagnosis
Use when any of these appears:
- wrong recognition or path;
- missing/incorrect model or theorem condition;
- repeated execution/check pattern;
- fragile or accidental success;
- important boundary/counterexample;
- explicit request to inspect reasoning/model;
- possible local Handbook/Rule defect;
- a genuinely reusable new paradigm worth testing against stored representatives.

Classify before producing long explanations.

## C1 — Clean fast path

Give a short verdict and at most one material note. Default persistence: not needed.

## C2 — Local-fix fast path

Give:
1. exact bad step;
2. immediate correction;
3. one concrete check when useful.

Do not escalate a one-off slip into a broad cognitive diagnosis or database action.

## D — Diagnosis gate

A deep diagnosis is incomplete until all four exist:

1. Observable fact from the learner's work.
2. First Divergence.
3. Main hypothesis + at least one competing explanation.
4. Minimal retest that distinguishes them.

Do not substitute the standard solution for learner-route reconstruction.

## E — Mental-model / local-owner gate

Trigger when:
- user asks for mental-model review/optimization;
- diagnosis may be `model`;
- local Handbook/Rules may be implicated.

When a local Owner exists, read it before teaching the mechanism. Prefer the repository's own `cognitive_system.py start wrong` Context Pack router; do not maintain a duplicate subject-routing truth in this skill.

If no local Owner exists, use a provisional subject-appropriate model and label it non-Canonical.

Invoke `build-mental-models` when model diagnosis is plausible, the user requests model optimization, a Handbook Challenge exists, or the Owner appears causally/boundary incomplete. Audit the smallest affected branch, then return here.

## F — Improvement gate

For deep problems:
- repair the learner's route first;
- in the user-facing response, give at most one materially better route unless method comparison is itself the learning goal;
- state the route-selection signal;
- include a verification point.

MCP persistence is a separate output surface. If the MCP's current rich-content specification asks for fuller stored pedagogy or multiple approaches, follow that specification for persisted fields without bloating the user-facing grading response.

## G — Retention value gate

This gate judges **intrinsic future value before deduplication**.

Ask:
1. Would redoing this exact problem test a meaningful ability?
2. Does it reveal a reusable diagnostic signal, boundary, paradigm, or transfer check?
3. Is the prompt/source reliable enough to preserve?

Outcomes:
- `No archive value`;
- `Archive candidate`;
- `Possible exact stored review/update`.

Do **not** claim `non-redundant` here. Redundancy is resolved only after MCP search in H.

## H — MCP resolution gate

Enter only for `Archive candidate` or `Possible exact stored review/update`.

### Search / dedup

1. `search_questions` with distinctive prompt fragments;
2. search concept/template terms when functional redundancy is plausible;
3. `get_question(view="full")` only for plausible matches.

`search_questions` is a lightweight candidate search: it does not return answers/explanations and one query does not prove semantic uniqueness.

Final outcomes:
- `No archive — redundant/low value`;
- `Reuse existing representative — no review event`;
- `Review exact existing question`;
- `Update exact existing question`;
- `Create high-value new probe`.

### Create

Required sequence:
`search_questions -> get_content_format_spec -> taxonomy if needed -> upload/crop image if needed -> validate_question({draft: ...}) -> create_questions`

### Update

Required sequence:
`search_questions -> get_question(full/latest) -> get_content_format_spec -> update_question(expected_updated_at=<latest updated_at>)`

Validate reconstructed rich content before create. Follow any current MCP validation requirements for update.

### Review

Use `submit_review` only for the exact same stored question actually redone by the learner. Similar transfer evidence is not a review event.

## I — Local cognitive resolution + validation gate

For every deep problem inside local scope, choose one:
- No Update;
- Inbox / unresolved evidence;
- Candidate Rule;
- Handbook Challenge;
- Canonical defect correction;
- Exam Control.

Use the current repository contract to resolve the actual destination. Do not hardcode `80_evidence/inbox/`; current project workflows may use subject `inbox.md`, Subject Rules `## 待验证`, review logs, or another owned location.

### Stable correction vs promotion

- independently verified Canonical factual/mechanistic/applicability defect → Stable Write correction now when tools/contracts allow;
- new Rule/model adoption or maturity promotion → keep as evidence/candidate until the repository's promotion contract and any required human decision are satisfied.

If stable files changed, run the validation required by `AGENTS.md`. At minimum run repository `check`; run `progress --write`, `audit`, tests, or publish only when the changed asset/contract requires them.

## J — Closure gate

Report only applicable completed states:

```text
Coverage: total / clean / local-fix / deep-diagnosis
Deep: Q... First Divergence / diagnosis / minimal retest
MCP: Not needed | No write | Reused <id> | Created <id> | Updated <id> | Reviewed <id>
Local: Out of scope | No Update | Inbox | Candidate Rule | Handbook Challenge | Canonical defect correction | Exam Control
Validation: passed | not applicable | blocked by ...
```

Never report a write or validation as completed when it failed or was never executed.