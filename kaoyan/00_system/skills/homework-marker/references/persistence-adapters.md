# Persistence Adapters

## Purpose

Persistence is optional. HomeworkMarker grades and diagnoses correctly even when no archive or knowledge system is connected.

This file defines provider boundaries, with Smart Error Archive as the currently verified question-archive adapter.

## 1. Universal archive boundary

An archive owns stored problem records and review history. It does **not** automatically own:

- canonical subject knowledge;
- stable rules;
- learner-wide weakness claims;
- course/exam control policy.

Before creating anything, the exact problem must pass intrinsic retention value and archive redundancy resolution.

## 2. Smart Error Archive — verified read semantics

These tools span two different responsibilities:

- **single-question persistence** — search/get/validate/create/update/review;
- **longitudinal planning facts** — learning stats, due-review candidates, exam-set metrics.

HomeworkMarker uses the first group during ordinary grading only when retention warrants it. Use the second group only for an explicit cross-attempt review/practice/planning request.

### `search_questions`

Use for deterministic lightweight candidate discovery.

It can return fields such as:

- `id`;
- `title`;
- `prompt_summary`;
- `subject`;
- `tags`;
- `difficulty`;
- `mastery_level`;
- diagnosis summary when present;
- `updated_at`.

It does **not** return full answers/explanations. Therefore:

- one literal query does not prove semantic uniqueness;
- search distinctive prompt fragments for likely exact matches;
- search concept/template terms when functional redundancy is plausible;
- inspect plausible candidates with `get_question(view="full")`.

### `get_question(view="full")`

Use for plausible duplicates, exact records being updated, or genuine review resolution. Full view can include content, answers, explanation, diagnostic fields, review state, and current `updated_at`.

### `get_taxonomy`

Use only when subject/tag naming is uncertain. Do not force a new taxonomy spelling when a canonical one already exists.

### `get_content_format_spec`

Read before creating or rewriting rich content. The live server contract is authoritative and may evolve independently of this skill.

### `get_learning_stats` / `get_review_candidates` / `evaluate_exam`

Treat these as objective longitudinal/planning inputs, not grading verdicts.

- `get_learning_stats` returns factual review/mastery/lapse/due/fault metrics; it does not prove a stable cognitive weakness by itself.
- `get_review_candidates` returns deterministic due-order candidates and reasons; it does not decide the learner's broader practice strategy.
- `evaluate_exam` computes objective metrics for a supplied question set; it does not choose the set or produce a quality judgment.

Do not call these automatically while grading one attempt. Use them only when the user explicitly asks for progress review, due practice, practice planning, or exam assembly.

## 3. Standalone Question Invariant

Every persisted question must be a **self-contained retrieval unit**. A future learner should be able to open that one record, understand the task, and solve it without seeing the original worksheet, exam page, neighboring subproblem, or conversation.

Before create or update, inspect whether the candidate depends on anything outside itself:

- definitions, notation, variables, constants, assumptions, or shared setup introduced earlier;
- a diagram/table/data block printed with another item or at the top of a question group;
- a result proved/calculated in a previous subproblem;
- instructions such as “continue from above”, “use the preceding result”, “same conditions as before”, or “according to Question 3”.

If such a dependency is **load-bearing**, copy the minimum necessary information into the archived prompt and express it as a local given. Preserve the mathematical/logical dependency, but remove the cross-question reference.

Example transformation:

```text
Bad archive prompt:
“Using the result of Question (1), find the maximum value of f(x).”

Good archive prompt:
“Given that f'(x)=... and the critical points are ..., find the maximum value of f(x) on ... .”
```

The archived record should not mention another question merely because that is how the source set was organized. Question numbers may be retained only as source metadata when useful, never as a prerequisite for understanding the task.

If the dependency cannot be reconstructed faithfully from the supplied material, do **not** invent it. Keep the question unarchived or mark persistence blocked by missing context.

This invariant applies independently to `content`, options, diagrams, answer, and explanation: none should rely on hidden neighboring-question context.

## 4. Smart Error Archive — create path

Use:

```text
search literal candidates
→ search functional/template candidates when needed
→ inspect plausible full records
→ make candidate self-contained (Standalone Question Invariant)
→ get_content_format_spec
→ get_taxonomy if naming is uncertain
→ upload image if retained prompt/diagram requires it
→ validate_question({"draft": {...}})
→ require valid=true
→ create_questions
```

The validator's draft shape is **not identical** to the create-item shape. Do not pass a create item as a flat top-level validator request. Current validator drafts may omit create-only fields such as `wrong_answer`.

A successful validation currently returns fields such as:

```text
valid: true
validator_version: question-validator-v1
issues: []
```

## 5. Smart Error Archive — update path

For an exact existing record:

1. fetch `get_question(view="full")` immediately before update;
2. read the live content format when rich fields will change;
3. calculate the smallest allowlisted patch;
4. pass the latest `updated_at` as `expected_updated_at`;
5. do not overwrite stronger existing content with a weaker inference from one learner attempt.

## 6. Review integrity

Use `submit_review` only when the learner actually redid **that exact stored question**.

Do not submit a review because:

- a similar transfer problem was attempted;
- the same technique appeared elsewhere;
- a new problem reminded the agent of a representative card.

## 7. Diagnostic projections

Smart Error Archive currently supports question-level diagnostic fields such as:

- `fault_profile` with stages `recognition`, `path`, `execution`, `check`;
- `root_cause`;
- `trigger_rule`;
- `checklist`.

Do not distort the richer HomeworkMarker diagnosis merely to fill these enums:

- pure `model` issue → preserve in explanation/local knowledge system unless a supported stage is separately evidenced;
- pure task/exam-decision issue → keep in task/exam control rather than force-map;
- one-off slip → usually no diagnostic projection.

A populated archive `trigger_rule` is a retrieval aid for that problem; it does not prove a local rule system has adopted the rule.

## 8. Rich-content boundary

User-facing feedback and archive content are different surfaces.

```text
User-facing feedback
= selective, concise, diagnosis-first

Persisted archive explanation
= obey live archive rich-content contract
```

If the archive requires fuller pedagogy, structured sections, or multiple solution approaches, satisfy that in persisted fields without bloating the learner-facing response.

## 9. Images

For retained prompt/diagram assets:

```text
session/local image
→ upload_image
→ persist returned HTTP(S) URL
```

Do not persist raw base64 or internal asset identifiers in question image fields. Do not store an entire learner handwriting page by default when a faithful prompt/diagram crop is sufficient.

## 10. Existing data is heterogeneous

Do not assume legacy archive records already contain `fault_profile`, `root_cause`, `trigger_rule`, or `checklist`. Treat absent fields as absent data, not as evidence that no diagnosis exists.

Do not bulk-backfill legacy records from guesswork. Improve an existing record only when the exact question is retrieved and the new information is supported strongly enough to justify an update.

## 11. Learner-profile boundary

Archive records are question-centered. Even when multiple records share a fault stage, do not convert counts directly into claims such as “the learner has a recognition weakness.” A longitudinal learner claim requires cross-attempt evidence, competing explanations, and appropriate scope.

HomeworkMarker may report archive facts separately from its current-attempt diagnosis; it must not let historical metrics override the visible evidence in the submitted work.

## 12. Closure

Report only operations actually completed:

```text
Archive
- Not needed | No write | Reused <id> | Created <id> | Updated <id> | Reviewed <id>
- retention reason
- fields changed, when applicable
- validation result
```
