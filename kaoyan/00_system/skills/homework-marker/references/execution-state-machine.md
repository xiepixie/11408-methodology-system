# HomeworkMarker Execution State Machine

## Purpose

Keep **coverage mandatory** while making expensive diagnosis, archive search, and system writeback conditional.

## State ledger

| State | Required evidence before advancing |
|---|---|
| A Coverage + Fidelity | every legible problem accounted for; source reliable enough to grade |
| B Correctness / Scoring | verdict + material scoring effect when supported |
| C Depth | clean / local-fix / deep-diagnosis |
| D1 Clean | concise verdict; no invented diagnosis |
| D2 Local repair | exact bad step + correction + optional check |
| E Diagnosis | observable fact + First Divergence + hypothesis + competitor + retest |
| F Knowledge/model gate | owner/provisional model/audit outcome when triggered |
| G Improvement | repaired route + optional better route + verification + retest |
| H Persistence | only applicable archive/knowledge actions resolved |
| I Closure | only completed actions reported |

Do not enter H merely to record `No action` for every clean problem.

## A — Coverage + Fidelity

Pass only when:

- every uploaded page/image/file has been inspected;
- all legible problem numbers/subproblems are identified;
- continuations and crossed-out work are resolved as far as evidence allows;
- uncertain handwriting is explicitly marked uncertain;
- prompt/options/rubric are reliable enough to grade.

If an unreadable symbol can change the answer, block that judgment instead of guessing.

## B — Correctness / Scoring

For each problem identify:

- answer status;
- first material error/omission if any;
- downstream consequences;
- rubric effect when a reliable rubric exists.

Do not infer exact points from exam conventions when the rubric is absent.

## C — Depth gate

### clean
Correct/stable enough; no meaningful cognitive/control signal.

### local-fix
The main issue is an isolated arithmetic, sign, copy, notation, routine justification, or small efficiency defect.

### deep-diagnosis
Use when one or more apply:

- wrong recognition or route;
- missing/incorrect theorem condition, concept, mechanism, or boundary;
- repeated execution/check pattern;
- fragile or accidental success;
- important counterexample/boundary;
- explicit request to inspect reasoning/model;
- possible defect in a connected/local knowledge owner;
- a genuinely reusable paradigm worth future testing.

## D1 — Clean fast path

Give a short verdict and at most one material note. Stop unless the user explicitly requests deeper analysis.

## D2 — Local-fix fast path

Give:

1. exact bad step;
2. immediate correction;
3. one concrete check when useful.

Do not escalate a one-off slip into a stable weakness or archive action.

## E — Diagnosis gate

A deep diagnosis is incomplete until all four exist:

1. **Observable fact** from the learner's actual work.
2. **First Divergence** — earliest consequential deviation.
3. **Main hypothesis + at least one competing explanation**.
4. **Minimal retest** capable of distinguishing them.

Do not substitute the standard solution for learner-route reconstruction.

## F — Knowledge/model gate

Trigger only when the task implicates a mental model or a knowledge owner.

Provider priority:

1. user attachments / supplied rubric / supplied notes;
2. task-specific connected source explicitly relevant to the work;
3. local project/course knowledge system when one exists;
4. provisional domain model if no owner exists.

If an owner exists, read it before teaching the disputed mechanism. If the owner itself may be wrong, audit rather than silently aligning the learner to it. Before any Canonical model correction, complete the explicit model-audit handoff in `handoff-contracts.md` or the provider's equivalent gate.

## G — Improvement gate

For deep problems:

- minimally repair the learner's own route first;
- give at most one materially better user-facing route unless comparison is the goal;
- state the trigger/selection signal;
- include a verification point;
- include the minimal retest.

## H — Persistence gate

Persistence is **not** part of correctness.

### Archive branch

Enter only when the exact problem has intrinsic future retrieval value or may correspond to an exact stored record.

Then resolve redundancy/review/update/create against the active archive provider. Do not automatically expand ordinary grading into longitudinal learning statistics, due-review planning, or exam-set evaluation.

### Knowledge/rule branch

Enter only when the diagnosis creates meaningful evidence for a rule/model/control system.

Possible outcomes:

- No Update;
- Unresolved evidence;
- Candidate Rule;
- Model Challenge;
- Canonical defect correction;
- Task/Exam Control.

A proven defect in an existing canonical owner is different from promoting a new model/rule. The former may be corrected; the latter normally needs evidence/promotion authority.

## I — Closure gate

Report only applicable completed states:

```text
Coverage: total / clean / local-fix / deep-diagnosis
Grading: per-problem verdicts
Deep: Q... First Divergence / diagnosis / minimal retest
Archive: Not needed | No write | Reused | Created | Updated | Reviewed
Knowledge: Out of scope | No Update | Evidence | Candidate Rule | Model Challenge | Canonical correction | Task Control
Validation: passed | not applicable | blocked by ...
```

Never report a write or validation as completed when it failed or was not executed.