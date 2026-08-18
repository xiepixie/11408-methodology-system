# Homework Grading Protocol

## 1. Evidence first

Treat the homework page as evidence of the learner's actual process.

Before judging any answer, reconstruct across **all uploaded images**:

- problem/subproblem number;
- printed prompt, conditions, options, diagrams, tables, constants;
- learner's line-by-line work;
- crossed-out work versus intended final work;
- final answer/conclusion;
- page continuations;
- unreadable symbols that could change correctness.

If a later page repairs an earlier line, grade the repaired route. If a material symbol is unreadable, mark that judgment uncertain instead of guessing.

## 2. Coverage is mandatory; depth is selective

Every legible problem gets a coverage verdict. Only high-signal problems get deep analysis.

### `clean`

Correct and stable; no meaningful model, path, control, scoring, or boundary signal.

Output: short verdict + one material note at most.

### `local-fix`

An isolated execution/notation/copy slip or small inefficiency whose correction does not require a broader cognitive hypothesis.

Output: exact bad step → immediate correction → one concrete check if useful.

### `deep-diagnosis`

Use when the problem exposes or may expose:

- recognition failure;
- path failure;
- theorem/model/boundary misunderstanding;
- repeated execution/check pattern;
- fragile or accidental success;
- important counterexample/boundary;
- new reusable paradigm;
- possible defect in a local mental model;
- explicit user request to inspect the reasoning/model.

For every `deep-diagnosis`, the First-Divergence and closure workflow is mandatory.

## 3. Fidelity before reasoning

Do not grade a proposition you have not reconstructed accurately.

### Multiple-choice / true-false / proposition questions

Before deciding correctness, write an internal option ledger:

```text
A: exact proposition + load-bearing conditions
B: exact proposition + load-bearing conditions
C: exact proposition + load-bearing conditions
D: exact proposition + load-bearing conditions
```

For each option explicitly inspect:

1. existence assumptions;
2. domain/support;
3. quantifiers (`任意 / 存在 / 至少 / 唯一`);
4. strict vs non-strict inequalities;
5. implication direction and converse;
6. necessary vs sufficient conditions;
7. endpoint/boundary cases;
8. hidden regularity/independence/nonzero assumptions.

Do **not** judge an option just because it looks like a familiar theorem.

Typical mathematical check:

```text
f > g eventually
≠ automatically
lim f > lim g
```

First ask whether both limits exist and what order relation the theorem actually preserves.

The same principle applies outside mathematics: reconstruct the exact claim before pattern-matching it to a rule.

## 4. Reconstruct the learner's route before solving

Use the universal control frame:

`Target → Objects → Constraints → Structure → Output Shape → Candidate Paths → Risk Point → Verification → Expression`

Then adapt to the discipline rather than forcing one ontology onto every subject.

### Mathematics

Emphasize:
- representation;
- transformation legality;
- invariants/equivalence;
- theorem conditions;
- domain/boundary/case split;
- proof or independent check.

### Computer science / systems

Emphasize:
- object identity;
- state;
- event/transition;
- ownership/layer boundary;
- invariant;
- resource/time/cost;
- precise output/commit condition.

### Physics / engineering

Emphasize:
- system boundary;
- variables/state;
- assumptions/idealization;
- conservation/law/constraint;
- units/dimensions;
- sign convention/reference frame;
- limiting case / order-of-magnitude check.

### Language / humanities

Emphasize:
- task/claim;
- evidence;
- syntax/structure/discourse function when relevant;
- criterion/constraint;
- competing interpretation;
- whether the answer actually addresses the prompt.

### Other subjects

Build the minimum provisional reasoning frame needed by the task. Do not invent a fake kaoyan-specific doctrine.

The goal is to understand what the learner actually did, not to replace the page with an ideal solution.

## 5. First Divergence

For every `deep-diagnosis`, identify the earliest consequential point whose repair would prevent downstream failure.

A complete diagnosis contains four pieces:

1. **Observable fact** — exact visible step/omission/claim.
2. **First Divergence** — earliest consequential deviation.
3. **Main hypothesis + competing explanation** — do not collapse uncertainty too early.
4. **Minimal retest** — the smallest new task that distinguishes the explanations.

The final wrong line is not automatically the First Divergence.

Do not manufacture a First Divergence for a clean problem.

## 6. Diagnosis categories

Use these categories descriptively across subjects; use local Owners only when the repository actually supports that subject.

### `model`

The learner's concept, causal mechanism, object model, theorem condition, or applicability boundary is wrong/missing/unavailable.

### `recognition`

The required knowledge may exist, but the learner did not recognize the structure/signal/object that should activate it.

### `path`

The structure was recognized, but the chosen first action or route was invalid, fragile, or needlessly expensive.

### `execution-check-expression`

The route was sound, but calculation, state bookkeeping, notation, verification, or scoring/communication chain failed.

A one-off arithmetic/sign/copy slip is weak evidence; keep it at `local-fix` unless recurrence or structure supports a control hypothesis.

### `exam-decision`

The main loss came from time allocation, entry/exit/return behavior, risk, or attention policy rather than the question mechanism.

## 7. Mental-model review is a hard precondition when triggered

If either is true:

- the user asks to review/optimize the mental model; or
- the diagnosis may be `model` / Handbook Challenge,

then **read the relevant Canonical Owner before teaching the mechanism** when a local Owner exists.

Do not:

```text
explain from generic memory
→ then open the repository afterward
```

Use:

```text
route with repository `start wrong` when available
→ read returned Atlas / Rules / exact Owner
→ compare learner route
→ audit model if needed
→ explain
```

Do not maintain a second static subject-routing truth in this protocol when the repository router can resolve the current paths.

If no local Owner exists, give a provisional/non-Canonical model.

When `build-mental-models` is triggered, audit the smallest affected causal branch and return to the homework workflow afterward.

## 8. Grade correctness and process quality separately

### Correctness / scoring

For each material scoring element, mark:

- hit;
- partial hit;
- miss;
- invalidated by an earlier step;
- impossible to judge from the image.

Use an exact numerical score only when an authoritative rubric exists. Otherwise label any total as `估分`.

For ordinary homework without an exam rubric, discuss correctness/completeness rather than inventing exam points.

### Process repair

Repair the learner's own route with the smallest useful change.

Look for:
- unnecessary work;
- transformations before structural simplification;
- hidden assumptions;
- fragile notation;
- missing intermediate assertions;
- recomputation instead of maintaining state/invariants;
- absent checkpoint after a high-risk step.

### Strategy improvement

For deep problems, provide at most **one** materially better route when it improves:

- risk;
- length;
- theorem-condition clarity;
- number of cases;
- invariant strength;
- independent verification;
- working-memory/time cost.

State the **selection signal** for choosing that route next time.

Do not list several methods merely for completeness in the **user-facing grading response**. If a problem is persisted to Smart Error Archive, the archive's live `rich-content-v1` specification is a separate output contract and may require fuller explanation or multiple approaches in stored fields.

## 9. Slip vs stable control weakness

A single sign/copy/arithmetic error defaults to immediate correction, not long-term diagnosis.

Upgrade it to a control hypothesis only when evidence shows recurrence or structure, e.g.:

- same sign/branch bookkeeping failure across unrelated problems;
- repeatedly skipping a risky intermediate state;
- repeatedly failing the same independent check;
- systematic transcription breakdown in long expressions;
- a reliable trigger predicts the failure.

Then formulate a specific action and minimal retest. Do not archive every instance.

## 10. Retention is separate from diagnosis

After diagnosis, first judge the **intrinsic future value** of the exact question. Only an archive candidate then enters Smart Error Archive search for literal/functional deduplication and exact-record resolution.

Do not equate:

- wrong → archive;
- deep diagnosis → archive;
- cognitive issue → archive;
- routine template variant → new card;
- similar transfer problem → review of an existing representative.

Do not claim `non-redundant` before MCP search. The retained problem should be a high-information future probe that remains valuable after archive resolution.

## 11. Output by depth

### Clean

`Qn：正确 / 基本正确 — <one material note if any>`

### Local fix

- **问题位置**: exact line/step;
- **当场订正**: what to redo;
- **防错检查**: one concrete check if useful;
- **留存**: default `No archive`.

### Deep diagnosis

1. **判定与采分点 / 完成度**
2. **First Divergence**
3. **薄弱点诊断** — evidence + main hypothesis + competing explanation
4. **过程优化**
5. **思路优化**
6. **心智模型复习 / 临时推理模型** — only when the mental-model gate actually triggers
7. **最小复测**
8. **留存判定** — intrinsic value first, then archive resolution when needed
9. **系统反哺** — report MCP / Local / Validation only when applicable and actually resolved

## 12. Evidence discipline

- Tie every criticism to visible work or a verified source.
- Do not infer broad weakness from one unexplained slip.
- Correct answers may still expose unstable routes or control risks.
- Wrong answers may still contain valid intermediate reasoning.
- Separate `false`, `valid but inefficient`, and `incomplete expression`.
- Missing information stays missing.
- A teaching-friendly story is not evidence of the learner's actual misconception.
- Deep analysis must be justified by information value, not verbosity.
