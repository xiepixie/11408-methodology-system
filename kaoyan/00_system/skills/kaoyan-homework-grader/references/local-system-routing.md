# DevSpace + Local Cognitive System Routing

## Purpose

Use the `kaoyan` repository as a cognitive Owner only when the repository actually owns the problem's subject/model. Prefer the repository's executable routing contract over duplicating a static subject map inside this skill.

## 1. DevSpace boot

For an in-scope deep diagnosis:

1. open the repository root:
   `/Users/xpx/Library/Mobile Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/工作领域/资源/kaoyan`
2. reuse that workspace for the grading session;
3. read `AGENTS.md`;
4. read `CURRENT.md`;
5. read the context-routing protocol.

### Context routing protocol
The repository standard context routing protocol is:
`00_system/agent_context_protocol.md`

Resolve this safely:

- try the path named by current `AGENTS.md` first;
- if it is missing, discover the uniquely matching context-routing protocol under `00_system/`;
- read the current file and report the documentation drift if it matters to the task;
- do not stop the homework diagnosis merely because the legacy filename is stale.

Do not scan the whole repository for context.

## 2. Prefer the repository router

After identifying a likely subject/topic from the homework, run:

```bash
python3 00_system/cognitive_system.py start wrong --subject <subject> --topic <topic>
```

The router is the current executable source for:

- accepted subject aliases;
- Course / Subject Context Pack paths;
- Subject Rules locations;
- candidate Topic / Bridge / Integration Landing Pages;
- Canonical `.tex` discovery when present.

Examples known to work in the current repository include:

```bash
python3 00_system/cognitive_system.py start wrong --subject calculus --topic 极限
python3 00_system/cognitive_system.py start wrong --subject os --topic 虚拟内存
```

Read only the returned Context Pack plus the exact candidate Landing / Canonical body needed for the problem.

If `start wrong` rejects the subject or cannot route the topic, fall back to the Atlas/Rules rules in the context-routing protocol. Do not invent a new local subject tree.

## 3. Owner model

Current repository ownership is:

```text
Course / Subject Atlas README
  = Canonical map, mother questions, routing, Foundation

Topic / Bridge / Integration README
  = Landing Page, scope, links, status

Topic / Bridge / Integration Canonical .tex
  = deep mechanism body when one exists

Subject Rules Markdown
  = question signals, first actions, checks, stop boundaries

Evidence / inbox / review logs / candidate sections
  = unverified learning evidence

90_publish/*.pdf
  = derived publication view, never writable knowledge Owner
```

For Atlas, the README itself is Canonical. For Topic/Bridge/Integration, read the Landing first and follow it to the Canonical `.tex` when one exists. If no mature `.tex` exists, say so and treat any additional model as provisional.

## 4. Mental-model hard gate

Before explaining the mechanism when the user requests mental-model review or diagnosis may be `model`:

```text
Homework evidence
→ repository start wrong routing
→ Atlas / Rules / exact Owner read
→ First Divergence + competing explanation
→ build-mental-models audit when triggered
→ local model decision
→ return to homework closure
```

Never teach from generic memory first and align to the repository afterward when a local Owner exists.

## 5. Local evidence/write routing

Use the repository's current `wrong` logic:

`Observable Facts → First Divergence → Related Mental Model → Missing / Misused / Unavailable? → Competing Explanation → Minimal Retest`

Then choose one outcome.

### No Update

Use for one-off, insufficiently explained, or action-neutral events.

### Inbox / unresolved evidence

Use when evidence is valuable but uncertain: repeated-looking errors with competing explanations, possible model challenge, fragile success, or a candidate action not operational enough for Rules.

**Do not hardcode `80_evidence/inbox/`.** The current collaboration contract may route evidence to a subject `inbox.md`, global/408 inbox, review log, or another owned evidence location.

### Candidate Rule

Route to the relevant Subject Rules `## 待验证` only when the candidate has:

- trigger signal;
- concrete action;
- success/check condition;
- stop/failure boundary.

Do not promote slogans such as “细心”“多检查”.

### Handbook Challenge

Use when evidence suggests the Canonical mechanism/boundary may be wrong but the defect is not independently established.

### Canonical defect correction

Use when definition, proof, counterexample, authoritative source, or reproducible logic independently establishes that the existing Canonical Owner contains a factual/mechanistic/applicability error.

Before a stable correction, follow current `AGENTS.md` and load only the triggered contracts, typically:

- `00_system/collaboration_workflow.md`;
- `00_system/ownership_matrix.md` when Owner/dependency matters;
- `00_system/handbook_contract.md` when structure/Rule boundary matters;
- `00_system/evidence_promotion.md` when the issue is evidence/Rule promotion rather than a factual correction.

Then find the unique Owner, search duplicate definitions/downstream Uses, edit only owned truth, propagate necessary references, and validate.

### Exam Control

Use when time allocation, exit/return, risk, or attention policy dominates the failure.

## 6. Correction is not promotion

The repository's actual workflow distinguishes two authority levels:

- **repairing a proven error in an existing Canonical Owner** can proceed through Stable Write when independently verified;
- **adopting a new Rule, model, Bridge, maturity state, or other new stable claim** requires the repository's evidence/promotion process and any required human decision.

One homework event is normally evidence, not automatic adoption.

## 7. Validation

After local stable edits:

1. call `devspace.show_changes` once after the final related edit;
2. run the validation required by current `AGENTS.md`;
3. at minimum for normal stable content changes run:

```bash
python3 00_system/cognitive_system.py check
```

Use `progress --write`, `audit`, tests, or publish only when the changed asset or project contract requires them. Do not claim a Canonical correction completed until required validation succeeds.

## 8. End-of-session report

```text
Local
- State: Out of scope | No Update | Inbox | Candidate Rule | Handbook Challenge | Canonical defect correction | Exam Control
- Router: subject/topic used, when applicable
- Read: exact Atlas / Rules / Owner paths
- Changed: exact files or none
- Owner: canonical owner or none
- Validation: passed / not applicable / blocked
- Unresolved human decision: only when repository policy genuinely requires one
```
