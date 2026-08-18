---
name: homework-marker-legacy-kaoyan
description: "Deprecated compatibility alias for the former kaoyan-specific homework grader. Do not use for normal homework grading or cognitive diagnosis; use the general `homework-marker` skill instead. Keep only so old references to the previous skill name remain understandable during migration."
---

# Legacy alias: kaoyan-homework-grader

This directory is retained only for migration compatibility.

The active, domain-general skill is:

`../homework-marker/SKILL.md`

Do not maintain grading logic, MCP contracts, repository routing, or diagnosis rules in this legacy entrypoint. All future improvements belong to `homework-marker`.

The former kaoyan repository behavior is now an optional adapter documented by HomeworkMarker under:

`../homework-marker/references/knowledge-source-routing.md`
