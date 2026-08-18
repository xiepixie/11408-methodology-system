# HomeworkMarker Handoff Contracts

## Purpose

Prevent responsibility drift between HomeworkMarker, mental-model auditing, question archives, and local knowledge systems.

HomeworkMarker owns **single-attempt evidence interpretation and orchestration**. It may call other providers, but it must not silently absorb their ownership.

## 1. HomeworkMarker → Build Mental Models

Trigger this handoff when:

- `model` is a plausible diagnosis and the disputed mechanism/boundary matters;
- the user explicitly asks to review or optimize a mental model;
- a Canonical owner may be defective;
- a proposed stable model correction would otherwise be written.

Pass the smallest supported packet:

```text
Task context
- exact problem / relevant rubric or source

Learner evidence
- exact learner step(s) that matter
- what is observed vs unreadable/unknown

Diagnosis state
- First Divergence
- main hypothesis
- competing explanation
- minimal retest already proposed

Knowledge target
- suspected concept/mechanism/boundary
- suspected Owner/provider, if any

Requested operation
- diagnose | review affected branch

Scope
- smallest causal branch needed to resolve the diagnosis
```

Do **not** pass a learner-specific hypothesis as if it were a verified subject fact.

Expected return to HomeworkMarker:

```text
Owner status
- trustworthy | critical gap | canonical defect

Model finding
- verified mechanism/boundary or unresolved gap

Affected branch
- exact concept/mechanism/interface touched

Learner implication
- what this result supports or rules out in the current diagnosis

System action
- none | evidence | model challenge | canonical correction candidate

Retest consequence
- whether/how the minimal retest should change
```

HomeworkMarker then resumes the learner-facing workflow. Build Mental Models does not own the grading verdict, question retention decision, or archive review state.

## 2. HomeworkMarker → Question Archive

The archive receives only **question-level** information justified by the exact retained problem.

Appropriate payloads include:

- exact prompt/content/options;
- all load-bearing givens needed to solve the archived question independently;
- correct answer/explanation;
- retained learner wrong answer when appropriate;
- question-level diagnostic projection;
- trigger/checklist for future retrieval;
- subject/tags/difficulty;
- exact-question review result.

Before handoff, enforce the **Standalone Question Invariant**: if the retained item originally depended on another question, earlier subproblem, shared diagram, prior result, or group-level setup, inline the minimum necessary dependency as local context. Preserve the dependency itself but remove references to neighboring questions. The archive payload must not require phrases such as “由上一题可知”, “根据第 3 题”, “沿用前问条件”, or “continue from above” to be intelligible. If the missing dependency cannot be reconstructed faithfully, block persistence rather than fabricate it.

Do not persist as question facts:

- global learner traits;
- unsupported stable weaknesses;
- local Handbook truth;
- unadopted Candidate Rules;
- generic task/exam policy that is not specific to the question.

Archive output may inform HomeworkMarker about exact duplicates, review history, due status, or objective metrics. It does not override the evidence visible in the current learner attempt.

## 3. Longitudinal archive analytics boundary

Functions such as learning statistics, due-review selection, and exam-set evaluation belong to a **longitudinal learning-planning layer**.

HomeworkMarker may use them only when the user explicitly asks for cross-attempt review, practice selection, progress analysis, or an exam/practice set.

Do not automatically call them during normal one-batch grading merely because the archive exposes them.

If a future dedicated review/practice-planning skill exists, that skill should own this layer.

## 4. HomeworkMarker → Local Knowledge Provider

Send an **evidence packet**, not a stable conclusion, unless the provider's correction gate has already been satisfied.

Recommended packet:

```text
Source
- current problem / learner evidence

Observed signal
- First Divergence + exact evidence

Diagnosis
- hypothesis + competitor + retest status

Knowledge/control implication
- possible model defect | possible rule/control signal | no stable implication

Proposed destination
- No Update | Inbox/evidence | Candidate Rule | Model Challenge | Canonical correction candidate | Task Control
```

The provider owns:

- its native terminology;
- unique Owner selection;
- evidence-promotion policy;
- stable-write authority;
- validation.

HomeworkMarker must not create a second stable truth.

## 5. Provider vocabulary projection

Generic HomeworkMarker terms are transport terms. Convert them only at the adapter boundary.

Example for the current `kaoyan` provider:

```text
HomeworkMarker generic        kaoyan native term
model                         模型问题
recognition                   识别问题
path                          路径问题
execution-check-expression    执行/检查/表达问题
task-decision                 考试决策问题
Model Challenge               Handbook Challenge
Task Control                  Exam Control
```

Do not rename the provider's Canonical terminology just to match the universal skill.

## 6. Stable correction gate

A Canonical model correction requires all applicable conditions:

1. the disputed source/prompt has adequate fidelity;
2. the current canonical Owner has been identified;
3. the defect is independently verified or reproducibly derived;
4. a model audit (`build-mental-models` or provider-equivalent) confirms the affected branch;
5. the provider's stable-write authority permits the change;
6. provider validation passes after the edit.

A single learner error is never sufficient evidence by itself for a Canonical correction.

## 7. Ownership summary

```text
HomeworkMarker
= learner attempt → grading / First Divergence / hypothesis / retest / orchestration

Build Mental Models
= subject/model causal truth → mechanisms / boundaries / owner audit

Question Archive
= retained problem records → exact review history / mastery / retrieval metadata

Local Knowledge Provider
= stable Handbooks / Rules / evidence promotion / project-native ownership

Longitudinal Planner (optional/future)
= cross-attempt stats → review selection / practice plan / exam assembly
```

When uncertain, prefer an explicit handoff over duplicating another component's role.