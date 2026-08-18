# Knowledge Source Routing

## Purpose

HomeworkMarker is universal; knowledge systems are optional providers. Never make one repository, exam, curriculum, or note vault the identity of the skill.

## 1. Provider priority

When a problem needs external grounding, use the narrowest relevant source in this order:

1. **User-provided material** — prompt, rubric, answer key, textbook excerpt, teacher notes, course handout.
2. **Task-specific connected source** — a repository, course workspace, knowledge base, or canonical exam source explicitly relevant to the task.
3. **Local mental-model system** — when the user's project owns the concept/rule being diagnosed.
4. **Provisional model** — when no authoritative or user-owned source exists.

Attachments remain primary truth for what the learner was actually asked and wrote.

## 2. Read-before-teach rule

When `model` is plausible or the user explicitly asks for mental-model review:

```text
Homework evidence
→ identify relevant owner/provider
→ read smallest necessary owner/context
→ compare learner route with owner
→ audit owner if needed
→ explain/repair
```

Do not teach from generic memory first and then retrofit the local owner's terminology afterward.

## 3. Provider contract

For any repository/knowledge system:

- read its `AGENTS.md`, project instructions, ownership rules, terminology, or equivalent when available;
- prefer its executable router/index over maintaining a duplicate static routing table in HomeworkMarker;
- read only the context pack / landing page / canonical body needed for the current problem;
- respect its native vocabulary, stable-write, evidence-promotion, and validation rules;
- translate generic HomeworkMarker diagnosis/output terms into provider-native terms only at the adapter boundary;
- never write derived/publication views as if they were canonical owners.

If the provider is unavailable or out of scope, continue grading with a provisional model and state that no local owner was used.

## 4. `kaoyan` adapter

The current `kaoyan` repository is one supported provider, not a universal dependency. Its native diagnostic/control vocabulary is authoritative inside that repository; in particular generic `task-decision` projects to `考试决策问题`, generic `Model Challenge` to `Handbook Challenge`, and generic `Task Control` to `Exam Control`.

When the task belongs to that repository:

1. open the repository root in DevSpace;
2. read `AGENTS.md` and `CURRENT.md`;
3. follow its current context-routing protocol;
4. prefer its router:

```bash
python3 00_system/cognitive_system.py start wrong --subject <subject> --topic <topic>
```

5. read only the returned Context Pack plus the exact Topic/Bridge/Integration owner needed.

Standard repository protocol: read `00_system/agent_context_protocol.md` for context-routing protocol under `00_system/`.

Do not duplicate the repository's subject routing table in this skill.

## 5. Local write outcomes

When a provider supports cognitive writeback, choose the provider-appropriate equivalent of:

- `No Update`;
- `Unresolved evidence / Inbox`;
- `Candidate Rule`;
- `Model Challenge`;
- `Canonical defect correction`;
- `Task/Exam Control`.

Do not hardcode destinations such as `80_evidence/inbox/`. Follow the provider's current ownership contract.

## 6. Correction vs promotion

Keep authority levels separate:

- **Existing canonical factual/mechanistic/applicability defect independently verified** → before stable write, require the provider's model-audit equivalent (for this ecosystem, normally `build-mental-models`) on the smallest affected branch; then correction may proceed through the provider's stable-write path when tools/authority permit.
- **New rule/model/bridge/maturity claim inferred from learner evidence** → preserve as evidence/candidate until the provider's promotion process is satisfied.

One homework event is normally evidence, not automatic adoption.

## 7. Validation

After any provider write:

- run the provider's required validation/checks;
- report exact files/records changed;
- report blockers precisely;
- never claim a correction/update succeeded if validation failed.