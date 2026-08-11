# AGENTS
> Scope: `common/考研/` and descendants. Upper-level instructions still apply.

## Boot
Read only: `AGENTS.md` → `CURRENT.md` → `00_system/agent_context_protocol.md`.
Do not scan the whole repository “for safety”.
```bash
python3 00_system/cognitive_system.py start <scenario> --subject <subject> --topic <topic>
```
Scenarios: `explore / model-diff / solve / wrong / adversary / practice / import / review / publish`.

## Source of Truth
```text
Atlas README.md                   = Canonical Atlas Source + navigation hub
Atlas assets/<Atlas>_Poster.tex   = optional derived visual poster; never a second knowledge Owner
Topic/Bridge/Integration README   = Landing Page only
Topic/Bridge/Integration <name>.tex = Canonical deep body
90_publish/*.pdf                  = compiled reading / visual view
Subject Rules                     = Markdown Control rules
Inbox                             = unverified learning input
System contracts                  = Markdown project rules
```
Atlas is the deliberate format exception: its body is the map itself, so Markdown is Canonical. A missing Atlas `.tex` is normal. Topic / Bridge / Integration still require a Canonical `.tex` before they count as mature bodies. Old README/PDF content outside these roles is Source.
Stable Handbook types remain `Atlas / Topic / Bridge / Integration`. Foundation belongs to Atlas; Extension / Anti-Bridge are relationship roles.

## Load Contracts Only When Triggered
| Task | Read |
| ------------------------ | ------------------------------------ |
| stable write/import/topology/status | `00_system/collaboration_workflow.md` |
| create/restructure Handbook or Rules | `00_system/handbook_contract.md` |
| large Handbook body rewrite | `00_system/handbook_writing_spec.md` |
| Owner/duplication/dependency | `00_system/ownership_matrix.md` |
| evidence/Rule promotion | `00_system/evidence_promotion.md` |
| architecture change | `00_system/architecture.md` |
| terminology conflict | `00_system/terminology.md` |
| check/audit behavior | `00_system/repository_integrity.md` |
| shared solving control | `01_control/problem_solving_kernel.md` |
Do not redefine another contract here; link its Owner.

## Stable-Write Procedure
Before changing a Handbook, formal Rule, Ownership entry, status, or topology:
1. decide `Knowledge` vs `Control`;
2. find the unique Owner;
3. search existing definitions and downstream Uses / Bridges / Integrations;
4. edit the Owner; replace duplicates with minimal references;
5. change status only when the physical asset changed;
6. update `CURRENT.md` only when the current direction changed;
7. validate the repository.
If Owner is unclear, keep the idea in Inbox or mark the conflict. Never create a second stable truth.

## Handbook / Rule Boundary
Atlas package: `README.md` + optional `assets/<Atlas>_Poster.tex`. The README owns Mother Question, scope, Topic/Bridge/Integration map, routing, Foundation and cross-module relationships. The poster may visualize the same map but cannot introduce a new semantic claim.
Topic / Bridge / Integration package: `README.md` + `<Handbook>.tex` + optional `assets/`. Their README is only the entry; `.tex` owns definitions, mechanisms, derivations, boundaries, worked examples and compression.
Bridge owns a reusable interface; Integration owns one multi-module process. A connection with no independent interface stays `Use / Bridge Note / Candidate / Extension`.
Mechanism and invocation are different Owners: Handbook explains why it works; Rules explain what signal triggers what action, how to verify it, and when to stop.
For wrong answers, preserve the user's original process, locate First Divergence, then decide `No Update / Inbox / Candidate Rule / Handbook Challenge`.

## Publication
For Topic / Bridge / Integration deep bodies:
```bash
python3 00_system/cognitive_system.py publish "<target.tex>"
```
This is the only recommended deep-Handbook publish entry. Atlas does not require publication to be complete; optional Atlas posters are derived visuals under `assets/` and use `python3 00_system/cognitive_system.py publish-view "<Atlas>/assets/<Atlas>_Poster.tex"`. Never edit PDF by hand.

## Validation
After stable changes:
```bash
python3 -m py_compile 00_system/cognitive_system.py   # if script changed
python3 -m unittest discover -s 00_system/tests -p 'test_*.py'  # if script changed
python3 00_system/cognitive_system.py progress --write
python3 00_system/cognitive_system.py check
python3 00_system/cognitive_system.py audit
```
`check` blocks machine-provable errors. `audit` reports allowed maintenance debt; `audit --all` expands the full missing-`.tex` backlog. Exact rules: `00_system/repository_integrity.md`.
Do not bypass tool write restrictions with shell redirection or generated scripts.

## Delivery
For complex repository work, report: context used; facts vs hypotheses; `No Update / Candidate / Canonical Update`; files changed and Owner roles; unresolved human decisions; next smallest validation step.

## Commit Attribution
If an AI creates a commit, include a `Co-Authored-By` trailer using that agent's own identity.
