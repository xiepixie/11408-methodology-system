# Smart Error Archive Boundary

## Purpose

Smart Error Archive is a **selective diagnostic-question persistence and true review-history layer**. It owns stored question records. It does not own local Handbook truth, Rules adoption, evidence promotion, or exam-control policy.

The current archive contains many legacy questions whose `diagnosis` / `fault_profile` fields are empty. Do not assume the existing archive is already cognitively structured just because the current schema supports diagnostic fields.

## 1. Actual read semantics

### `search_questions`

Use for deterministic candidate discovery and deduplication.

Current result shape is intentionally lightweight. It may include:

- `id`;
- `title`;
- `prompt_summary`;
- `subject`;
- `tags`;
- `difficulty`;
- `mastery_level`;
- diagnosis summary when present;
- `updated_at`.

It **does not return answers or explanations**. Therefore:

- one literal query does not prove semantic uniqueness;
- search distinctive prompt fragments for likely exact matches;
- also search concept/template terms when functional redundancy is plausible;
- inspect plausible matches with `get_question(view="full")` before update/review or before declaring a strong semantic duplicate.

### `get_question(view="full")`

Use only for plausible matches or exact records that may be reviewed/updated. Full view can include content, correct/wrong answer, explanation, diagnosis detail, review state, and current `updated_at`.

### `get_taxonomy`

Use when subject/tag naming is uncertain. Current canonical subjects include real archive categories such as 高等数学、线性代数、概率论与数理统计、数据结构、计算机组成原理、操作系统、计算机网络、英语. Do not invent a new spelling when a canonical subject already exists.

### `get_content_format_spec`

Read before creating or updating rich question content. It is the current server-side formatting contract and may evolve independently of this skill.

## 2. Retention + MCP state machine

```text
Intrinsic Retention Value
→ No archive value? ── yes → MCP not needed
→ Archive candidate / possible exact stored record
     ↓
search literal candidate(s)
     ↓
search functional/template candidate(s) when needed
     ↓
get_question(full) for plausible matches
     ↓
Final decision
   ├─ No archive — redundant/low value
   ├─ Reuse representative — no review event
   ├─ Review exact existing question
   ├─ Update exact existing question
   └─ Create high-value new probe
```

This ordering is deliberate: intrinsic value is judged before search, but non-redundancy is decided only after search.

## 3. Create contract

Create only when the exact problem is a high-value future probe and no adequate representative already covers the same learning function/boundary.

Required path:

1. `search_questions` for exact/literal candidates;
2. functional/template search when needed;
3. `get_content_format_spec`;
4. `get_taxonomy` only when naming is uncertain;
5. `upload_image` / `crop_image` when a retained prompt/diagram requires an image;
6. call `validate_question` using its actual wrapper: `{"draft": <validator-supported rich fields>}`;
7. require `valid=true` and an empty/acceptable `issues` list;
8. call `create_questions` with the full create item.

Use `mode="atomic"` when creating a tightly coupled batch whose partial creation would be harmful; otherwise respect the API's default/best-effort semantics.

Do not create merely because:

- the learner was wrong;
- the diagnosis was interesting;
- a one-off arithmetic/sign/copy slip occurred;
- the problem is another surface variant of an existing template.

## 4. Current rich-content contract

The server's current `rich-content-v1` specification is authoritative for persisted content. It currently requires a structured distinction between:

- `correct_answer`: concise formal exam/full-credit answer-sheet form;
- `explanation`: fuller pedagogical material with analysis/strategy, detailed solution, and summary/remediation sections;
- semantic HTML for tables;
- KaTeX-safe math formatting;
- persisted HTTP(S) image URLs for uploaded/cropped diagrams.

The current MCP spec may request **multiple approaches** for mathematics/physics. This is a storage-format requirement and does not override the grader's user-facing brevity rule of at most one materially better alternative route. Keep these output surfaces separate:

```text
User-facing homework feedback = selective, diagnostic, concise
Persisted archive explanation = current MCP rich-content contract
```

Always read the live content-format spec instead of copying an old template from this file.

### Validator shape is not the create-item shape

The current `validate_question` contract accepts either:

```text
{"question_id": "<uuid>"}
```

or:

```text
{"draft": { ...validator-supported rich fields... }}
```

Do **not** pass a create item as a flat top-level object. The current validator draft schema does not include every create-only field (for example `wrong_answer`), so validate the supported rich-content portion, then pass the full allowed item to `create_questions` after validation succeeds.

Current successful validation returns fields such as:

```text
valid: true
validator_version: question-validator-v1
issues: []
```

## 5. Supported diagnostic projections

Current question schema supports:

### `fault_profile`

Only the MCP enum:

- `recognition`;
- `path`;
- `execution`;
- `check`.

`primary` is required when the object is present; `related` is a short list of additional supported stages.

Do not distort local diagnoses to fill this enum:

- local `model` → preserve locally / in explanation; map only if a distinct supported question-stage failure is also evidenced;
- pure expression-only defect → do not force-map unless it is genuinely execution/check;
- `exam-decision` → keep local Exam Control; do not force-map.

### `root_cause`

Store the narrowest evidence-supported question-level cause, not labels like “粗心” or “基础差”.

### `trigger_rule`

Allowed as a question-level retrieval projection:

```text
signal = visible cue
→ action = first concrete retrieval action
```

It is not proof that the local Rules system has adopted that rule.

### `checklist`

Store only observable anti-error checks useful for redoing this exact problem/intended paradigm. Cross-problem rule adoption remains local.

## 6. Update contract

Use `update_question` when an exact existing record needs a materially better transcription, answer, explanation, learner wrong answer, or better-supported diagnostic projection.

Required discipline:

1. fetch `get_question(view="full")` immediately before update;
2. read the current `get_content_format_spec` before rewriting rich fields;
3. calculate the smallest allowlisted patch;
4. pass the fetched record's latest `updated_at` as `expected_updated_at`;
5. do not overwrite a stronger existing explanation/diagnosis with a weaker inference from one attempt.

If the rich content is substantially reconstructed, validate it when supported/appropriate before applying the update.

## 7. Review integrity

`submit_review(question_id=...)` means the learner actually redid **that exact stored question**.

Allowed:
- homework attempt is the exact archived problem and represents a genuine redo;
- learner intentionally retrieved the stored problem and answered it again.

Not allowed:
- a new problem is merely analogous;
- the same technique was demonstrated elsewhere;
- a representative problem reminded the agent of another archived card.

Current ratings are:

- `again`;
- `hard`;
- `good`;
- `easy`.

The server owns the scheduling calculation; do not write scheduler fields yourself.

## 8. Image boundary

Use MCP storage for question/diagram assets necessary to reconstruct a retained problem.

Workflow:

```text
local/session image
→ upload_image
→ optional crop_image
→ persist returned HTTP(S) URL
```

Do not persist raw base64 data URLs or internal `asset_id` in question image fields. Do not store the learner's entire handwritten page by default when a faithful prompt/diagram asset is sufficient.

## 9. Local/MCP ownership boundary

MCP:
- exact stored question;
- future retrieval/review;
- question-level diagnostic projections;
- mastery/review history.

Local repository:
- Canonical mental models;
- Subject Rules adoption;
- unresolved evidence lifecycle;
- Handbook Challenges/corrections;
- Exam Control.

A populated MCP `trigger_rule` or `checklist` never proves Canonical local adoption.

## 10. Closure report

Report only actions actually performed:

```text
MCP
- Not needed | No write | Reused <id> | Created <id> | Updated <id> | Reviewed <id>
- retention reason: why this exact problem is or is not worth future retrieval
- projections written: fault_profile / root_cause / trigger_rule / checklist, when applicable
```
