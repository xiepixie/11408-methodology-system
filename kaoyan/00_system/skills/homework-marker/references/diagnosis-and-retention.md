# Diagnosis and Retention

## Purpose

Keep **grading depth**, **cognitive diagnosis**, and **future retention** independent.

A wrong answer does not automatically deserve deep diagnosis or archival. A correct answer may deserve deep diagnosis when the route is fragile, accidental, or exposes a valuable boundary.

## 1. Depth triage

### clean

Use when answer and route are sound enough and no material model/path/control/scoring issue appears.

Action: short verdict; no persistence by default.

### local-fix

Use when the issue is local: arithmetic/sign/copy/notation error, one routine omission, or obvious inefficiency.

Action: exact line → correction → optional check.

### deep-diagnosis

Use when at least one is true:

- recognition/path/model boundary is exposed;
- route succeeds only by luck or unstable heuristic;
- competing explanations remain;
- mistake recurs or has high downstream impact;
- important counterexample/boundary appears;
- user explicitly asks to inspect reasoning/model;
- the problem is a compact representative probe of a reusable paradigm.

## 2. Diagnosis classes

### model
Concept, theorem condition, causal mechanism, object model, or applicability boundary is wrong/missing/unavailable.

### recognition
Relevant knowledge may exist, but the learner did not recognize the structure/signal/object that should activate it.

### path
The structure was recognized, but the chosen first action or route was invalid, fragile, or needlessly expensive.

### execution-check-expression
The route was sound, but calculation, state bookkeeping, notation, verification, or scoring/communication failed.

### task-decision
Time allocation, entry/exit/return behavior, risk, or attention policy dominated the loss.

These labels are descriptive hypotheses, not personality traits.

## 3. Retention Gate A — intrinsic value

Run before any archive search.

Ask:

1. If this exact problem reappears later, what meaningful ability would it test?
2. Does it expose a reusable diagnostic signal, boundary, paradigm, or transfer check?
3. Is the prompt/diagram/correct resolution reliable enough to preserve?
4. Can the retained item be made fully self-contained, with every load-bearing dependency available inside that one record?
5. Is this a good probe rather than merely an interesting diagnosis?

If the item depends on another problem/subproblem, shared setup, diagram, notation, or prior result, retention is allowed only after the minimum necessary dependency can be faithfully inlined. If that context cannot be reconstructed without guessing, do not archive the item yet.

Outcomes:

- `No archive value`;
- `Archive candidate`;
- `Possible exact stored review/update`.

If the only future value is “看看还会不会算错这个数”, choose `No archive value`.

## 4. Retention Gate B — archive resolution

Only archive candidates or possible exact stored records enter this gate.

Against the active archive provider:

1. search distinctive prompt fragments for literal/exact candidates;
2. search concept/template terms when functional redundancy is plausible;
3. inspect plausible full records.

Then choose:

- `No archive — redundant/low value`;
- `Reuse existing representative — no review event`;
- `Review exact existing question`;
- `Update exact existing question`;
- `Archive this question — high-value new probe`.

Do not claim non-redundancy before search.

## 5. Functional redundancy

Two problems are functionally redundant when their future retrieval test is materially the same despite surface differences.

Compare:

- trigger/signal;
- first action;
- core representation or invariant;
- key risk/check;
- important boundary/case split.

A second representative is justified only when it tests a materially different boundary, representation, competing path, failure mode, or transfer demand.

## 6. Review integrity

A review event means the learner actually redid **that exact stored problem**.

A merely analogous problem is transfer evidence, not a review of the representative card.

## 7. Local knowledge persistence is independent

Examples:

- repeated control failure may deserve Candidate Rule evidence but no new archive card;
- a high-value mother problem may deserve an archive card but no model change;
- a proven canonical model defect may require correction even if the exact problem is a poor future retrieval probe.

Never use one persistence decision as proof for another.