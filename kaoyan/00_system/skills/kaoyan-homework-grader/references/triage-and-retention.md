# Homework Triage and Retention Gate

## Purpose

Keep four decisions separate:

1. Was the answer correct?
2. How deeply should this problem be diagnosed now?
3. Does the exact problem have intrinsic future retrieval value?
4. After archive search, is it non-redundant or an exact stored review/update?

A wrong answer does not imply deep diagnosis or archival. A correct answer may still justify deep diagnosis when the route is fragile, accidental, or exposes a valuable boundary.

## 1. Coverage pass: inspect everything, expand selectively

Every legible problem gets a verdict, but only high-signal problems receive the full diagnosis/persistence path.

### `clean`

Use when answer and route are sound enough and no material model/path/control/scoring issue appears.

Action:
- short verdict;
- at most one material note;
- no persistence work by default.

### `local-fix`

Use when the route is essentially sound and the issue is local: arithmetic/sign/copy error, notation defect, one omitted routine justification, or an obvious inefficiency.

Action:
- exact line;
- immediate correction;
- one specific preventive check when useful;
- no broad diagnosis or archive by default.

### `deep-diagnosis`

Use when at least one is true:
- recognition/path/model boundary is exposed;
- route is correct only by luck or unstable heuristic;
- competing explanations remain;
- mistake recurs or has high downstream impact;
- problem is a compact representative probe of a reusable paradigm;
- important boundary/counterexample appears;
- user explicitly asks to inspect reasoning/model.

Only these problems receive the full First-Divergence workflow by default.

## 2. Slip vs stable signal

### One-off computation/transcription slip

Default:
- `local-fix`;
- immediate redo;
- no new MCP card;
- no claim such as “粗心” or “计算能力差”.

Escalate only when evidence supports a stable control problem, for example:
- same branch/sign/state-bookkeeping failure recurs across unlike problems;
- risky intermediate states are repeatedly omitted;
- the same independent check is repeatedly skipped.

Even then, the best persistence action may be local Rule evidence rather than another archived question.

### Routine template repetition

Another standard numeric variant does not deserve a new card merely because it is wrong.

When archive search later shows an existing representative tests the same:

`trigger → first action → key invariant/check → boundary`

prefer reuse/no new card.

A similar problem is transfer evidence, not a `submit_review` event for that representative.

### Cognitive breakpoint

Missed trigger, wrong theorem condition, wrong representation, path selection error, missing case split, false invariant, or owner/state confusion deserves deep diagnosis. It still must pass the retention gates below.

### New classic paradigm / mother problem

A correct problem can be retention-worthy when it is a compact, reusable probe not already represented. The model definition still belongs to the local cognitive system when a local Owner exists; the archive stores the probe.

## 3. Retention Gate A — intrinsic future value

Run this **before** archive search.

Ask:

1. If this exact problem reappears later, what meaningful ability would redoing it test?
2. Does it expose a diagnostic signal, important boundary, reusable paradigm, or transfer check?
3. Is the prompt/diagram/correct resolution reliable enough to preserve?
4. Is this a good probe rather than merely an interesting diagnosis?

Outcomes:

- `No archive value`;
- `Archive candidate`;
- `Possible exact stored review/update`.

If the only future value is “看看还会不会算错这个数”, choose `No archive value`.

## 4. Retention Gate B — archive resolution / non-redundancy

Only archive candidates or possible exact stored records enter this gate.

Use Smart Error Archive:

1. search distinctive prompt fragments for literal/exact candidates;
2. search concept/template terms when functional redundancy is plausible;
3. inspect plausible matches with `get_question(view="full")`.

Then choose one final outcome:

- `No archive — redundant/low value`;
- `Reuse existing representative — no review event`;
- `Review exact existing question`;
- `Update exact existing question`;
- `Archive this question — high-value new probe`.

Do not claim non-redundancy before this search stage.

## 5. What counts as functional redundancy?

Treat two problems as functionally redundant when the future retrieval test is materially the same despite surface differences.

Compare:

- trigger/signal;
- first action;
- core representation or invariant;
- key risk/check;
- important boundary/case split.

Surface number changes usually do not create a new learning function.

Create a second representative only when it tests a materially different boundary, representation, competing path, failure mode, or transfer demand.

## 6. Review-state integrity

`submit_review(question_id=...)` means the learner actually reviewed/redid **that stored question**.

Allowed:
- the homework task is the exact archived question and this attempt is genuinely a redo;
- the learner intentionally retrieved that exact card and answered it again.

Not allowed:
- merely similar template;
- same technique used elsewhere;
- a new homework problem reminds the agent of the archived representative.

For analogous new problems, use the evidence to judge transfer locally; do not mutate another card's review history.

## 7. Correct answers can still matter

Do not archive correct work just because it is interesting. Deepen or retain only when it reveals:

- fragile success;
- unexplained guess with future risk;
- valuable new paradigm/representative probe;
- important boundary handling that tests real transfer.

Routine clean success remains lightweight.

## 8. Local persistence is independent

Question retention and local cognitive writeback are separate.

Examples:

- a repeated control failure may deserve `Candidate Rule` evidence but no new question card;
- a high-value mother problem may deserve a new MCP card but no local model change;
- a proven Handbook defect may require Canonical correction even if the exact problem is a poor future retrieval probe.

Do not use one persistence decision as evidence for another.
