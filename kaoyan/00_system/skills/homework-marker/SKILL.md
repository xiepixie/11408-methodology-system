---
name: homework-marker
description: "Grade and diagnose learner attempts in handwritten, photographed, scanned, or typed homework, worksheets, quizzes, exams, and practice in any subject. Use when the user provides learner work/answers/reasoning or explicitly asks to 批改作业、判对错、估分、找薄弱点、定位 First Divergence、优化过程/思路、检查心智模型、筛选高价值错题、生成复测、或把诊断结果反哺错题库/知识系统. Do not trigger for ordinary solve-only questions with no learner attempt unless the user explicitly asks for grading/diagnosis. Treat attachments and provided rubrics as primary truth."
---

# HomeworkMarker

## Mission

Turn learner work into **accurate grading + high-value cognitive feedback** without forcing every problem into a heavyweight diagnosis or database workflow.

This skill is domain-general. It may be used for schoolwork, tutoring, self-study, competition practice, certification/exam preparation, or post-exam review. A particular repository, course, or exam system is only an optional knowledge provider, never the identity of this skill.

Keep five decisions separate:

1. **Fidelity** — what exactly was asked and what did the learner actually write?
2. **Correctness** — what is right, wrong, incomplete, or unreadable?
3. **Depth** — clean, local-fix, or deep-diagnosis?
4. **Diagnosis** — where is the First Divergence and what competing explanation remains?
5. **Persistence** — should anything be retained in an error archive, rule system, or knowledge model?

## Execution graph

```text
INPUT
→ A Coverage + Fidelity
→ B Correctness / Scoring
→ C Depth Classification
   ├─ clean → D1 Lightweight Feedback → I Closure
   ├─ local-fix → D2 Local Repair → I Closure
   └─ deep-diagnosis
        → E Learner-Route Diagnosis
        → F Mental-Model / Knowledge-Source Gate
        → G Improvement + Minimal Retest
        → H Persistence Resolution
        → I Closure
```

Every legible problem must pass A–C. Only `deep-diagnosis` problems enter E–H.

Read [references/execution-state-machine.md](references/execution-state-machine.md) for exact gates.

## A — Coverage + Fidelity

Attachments are primary truth. Read **all uploaded pages/images/files before answering**.

Reconstruct:

- problem/subproblem order;
- printed prompt, options, diagrams, tables, constants, rubric or answer key;
- learner derivation/argument and final answer;
- crossed-out versus retained work;
- continuations across pages;
- unreadable symbols that could alter correctness.

Never invent missing handwriting or hidden rubric requirements.

Source priority:

1. user's uploaded prompt/work/rubric/answer key;
2. a verified canonical source explicitly connected to this task;
3. independently reconstructed source only when needed.

For multiple-choice / true-false / proposition tasks, inspect each option's load-bearing conditions: domain, existence, quantifiers, strictness, implication direction, necessary/sufficient status, endpoints, and hidden assumptions.

Read [references/grading-protocol.md](references/grading-protocol.md).

## B — Correctness / Scoring

Separate answer correctness from process quality.

For each problem, determine:

- correct / basically correct / partially correct / incorrect / unreadable;
- exact first material error or omission;
- scoring impact when a rubric exists.

Use an exact numerical score only when the task provides a reliable scoring scheme. Otherwise label totals as estimates and avoid invented point allocations.

## C — Depth classification

Classify every legible problem as exactly one:

- `clean` — correct/stable; no meaningful model, route, control, or scoring signal;
- `local-fix` — isolated slip or small inefficiency; immediate correction is enough;
- `deep-diagnosis` — meaningful recognition/path/model/control issue, repeated pattern, fragile success, valuable boundary, or explicit request to inspect reasoning/model.

Do not fully analyze every problem. Read [references/diagnosis-and-retention.md](references/diagnosis-and-retention.md).

## D1 — Clean

Keep feedback short: verdict plus at most one material note. No persistence work by default.

## D2 — Local repair

Show only:

- exact bad step;
- immediate correction;
- one concrete preventive check when useful.

Do not turn a one-off arithmetic/sign/copy/notation slip into a broad learner diagnosis.

## E — Learner-route diagnosis

For every `deep-diagnosis` problem:

1. reconstruct the learner's actual route before replacing it with an ideal solution;
2. locate the **First Divergence** — earliest consequential deviation whose repair prevents the downstream failure;
3. separate:
   - observable fact;
   - main hypothesis;
   - at least one competing explanation;
   - smallest retest that distinguishes them.

Use diagnosis classes descriptively:

- `model` — concept/mechanism/condition/boundary is wrong, missing, or unavailable;
- `recognition` — relevant knowledge may exist but the triggering structure was not recognized;
- `path` — structure was recognized but the chosen start/route was invalid, fragile, or needlessly expensive;
- `execution-check-expression` — route was sound but calculation, state tracking, verification, notation, or scoring expression failed;
- `task-decision` — time/risk/attention/skip-return policy dominated the loss.

Do not infer a stable weakness from one unexplained event.

## F — Mental-model / knowledge-source gate

Trigger when:

- the user asks to review/deepen/optimize a mental model;
- `model` is a plausible diagnosis;
- an external/local knowledge owner may be implicated.

Use the most relevant **knowledge provider**, not a hardcoded repository:

- attached textbook/notes/rubric;
- a connected course or project repository;
- a local mental-model handbook;
- no external owner → use a provisional model and label it as such.

Read [references/knowledge-source-routing.md](references/knowledge-source-routing.md) and [references/handoff-contracts.md](references/handoff-contracts.md).

Invoke `build-mental-models` when the user explicitly asks for mental-model work, when a causal chain/boundary must be audited, or when the current owner may itself be defective. **A proposed Canonical model correction must pass this model-audit handoff (or an equivalent provider-owned audit) before stable write.** Audit the smallest affected branch, then return to this workflow.

## G — Improvement + Minimal Retest

For deep problems:

1. **repair the learner's route first**;
2. give at most one materially better user-facing route when it reduces risk, work, ambiguity, or verification cost;
3. state the selection signal for that route;
4. include a verification point;
5. give the smallest retest that can distinguish the main diagnosis from its competitor.

Do not drown the learner in alternative methods unless method comparison is itself the goal.

## H — Persistence resolution

Persistence is optional and provider-specific. A diagnosis can be valuable without writing anything anywhere.

### H1 — Retention value

Before searching any archive, ask whether this **exact problem** is a good future probe:

- would redoing it test a meaningful ability?
- does it expose a reusable boundary, paradigm, or diagnostic signal?
- is the prompt/source reliable enough to preserve?

Outcomes:

- `No archive value`;
- `Archive candidate`;
- `Possible exact stored review/update`.

### H2 — Error/archive provider

If Smart Error Archive or another archive is available and retention warrants it, resolve literal/functional redundancy before creating anything. For Smart Error Archive, follow the real MCP contract in [references/persistence-adapters.md](references/persistence-adapters.md).

Every persisted question must satisfy the **Standalone Question Invariant**: it must remain fully understandable and solvable when retrieved alone. If the source is one item inside a worksheet/exam set and depends on another item's setup, diagram, notation, definition, intermediate result, or shared background, copy the minimum necessary dependency into this question and rewrite it as local givens. Do not persist references such as “use the result of the previous question”, “as shown in Question 3”, or “continue from above”; the archived question must not mention other questions merely to recover missing context.

A similar transfer problem is not automatically a review of an existing stored question. Archive statistics, due-review selection, and exam-set evaluation are **longitudinal planning functions**, not automatic steps of ordinary single-attempt grading.

### H3 — Knowledge/rule provider

If a local/connected cognitive system is in scope, choose one of:

- `No Update`;
- `Unresolved evidence / Inbox`;
- `Candidate Rule`;
- `Model Challenge`;
- `Canonical defect correction`;
- `Task/Exam Control`.

Never hardcode a repository-specific path or vocabulary into the universal workflow. Follow that provider's current ownership, terminology, and promotion contracts; project generic HomeworkMarker terms into provider-native terms only at the adapter boundary.

Distinguish:

- independently verified defect in an existing canonical model → correction may proceed when authority/tools permit;
- new rule/model adoption from one homework event → evidence/candidate first, not automatic promotion.

## I — Closure

Report actions actually completed, not hypothetical writes.

For a normal batch:

```text
Coverage
- total / clean / local-fix / deep-diagnosis

Grading
- Q... verdict / scoring note

Deep findings
- Q... First Divergence / diagnosis / minimal retest

Persistence
- Archive: Not needed | No write | Reused <id> | Created <id> | Updated <id> | Reviewed <id>
- Knowledge system: Out of scope | No Update | Evidence | Candidate Rule | Model Challenge | Canonical correction | Task Control

Validation
- passed | not applicable | blocked by <exact blocker>
```

Do not claim a write succeeded when validation or persistence failed.