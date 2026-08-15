# LaTeX Design System Regression Specimens

> **Role**: implementation regression assets for `common/latex/`; not Handbook knowledge sources and not publication artifacts.
>
> **Canonical architecture**: [`../README.md`](../README.md)

## Active public-API specimens

```text
handbook-body.tex
    = shared semantic body; contains no documentclass/profile-specific visual code

handbook.tex
    = profile=standard wrapper

handbook-margin.tex
    = profile=margin + twoside wrapper
```

The most important regression invariant is:

> `handbook.tex` and `handbook-margin.tex` must consume the **same** `handbook-body.tex`.

This tests the Design System rule:

```text
Content declares meaning;
Profile decides appearance.
```

`semanticmargin` must therefore remain meaningful in both profiles:

- `standard`: render supplementary content inline;
- `margin`: render it in the outer semantic margin.

Likewise `widecontent` must accept the same body:

- `standard`: safely degrade to ordinary body width;
- `margin`: temporarily consume the outer-margin envelope.

## Focused / diagnostic specimens

```text
handbook-margin-gate.tex
    = small positive smoke test for profile=margin, odd/even mirroring and widecontent

handbook-engine-standard.tex
    = raw KOMA + CTeX engine experiment used before ipara-core/class extraction

handbook-engine-margin.tex
    = raw margin-engine experiment; verifies KOMA addmargin*, marginnote and candidate geometry
```

The two `handbook-engine-*` files are diagnostic evidence, not public template examples. New content must not copy their raw preambles.

## Current candidate geometry

As of 2026-08-11:

```text
standard main column = 170 mm

margin main column   = 116 mm
semantic margin      = 39 mm
margin gap            = 5 mm
```

The synthetic same-source regression is clean for both profiles. `standard=170mm` is backed by the real Topic04 gate: the previous KOMA `DIV=11` width (~152.7mm) introduced a new long-formula overflow, while 170mm removed that engine-level defect.

Topic04 has now also completed a layout-only migration to `handbooklongtable`, `handbooktable`, `processchain` and semantic-safe line-break points. After that migration, the transitional Canonical path, `profile=standard`, and `profile=margin` all compile with zero matching diagnostics. These geometry values remain **experimental**, not frozen Design Tokens, because margin information value still needs a semantic-margin gate.

## Local regression command

From the repository root:

```bash
TEXINPUTS="common/latex:common/latex/specimens:" \
  xelatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/ipara-standard \
  common/latex/specimens/handbook.tex

TEXINPUTS="common/latex:common/latex/specimens:" \
  xelatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/ipara-margin \
  common/latex/specimens/handbook-margin.tex
```

Run each wrapper at least twice when checking TOC / marks / references.

Final logs must not contain unexplained:

```text
Warning
Overfull
Underfull
undefined / Undefined
Error
```

## Current evidence

On 2026-08-11, TeX Live 2026 + XeLaTeX compiled both shared-body profiles twice with no matching diagnostics. The shared body now also covers `handbooklongtable` (`xltabular` + `Y` columns) in both profiles.

A real regression is kept under `real-topic/` and reads the current Canonical Topic04 body directly through `docmute`; it does not duplicate the knowledge text.

Current Real Topic result after layout-only migration:

```text
Canonical Topic + transitional ipara-handbook.sty
  = 0 matching diagnostics

profile=standard, 170mm
  = 0 matching diagnostics

profile=margin, 116mm + 5mm + 39mm
  = 0 matching diagnostics
```

Therefore both **Standard Real Topic Layout Gate** and **Margin Real Topic Layout Gate** pass. The next unresolved question is informational rather than mechanical: whether a small number of genuine semantic-margin objects improves navigation/retrieval enough to justify the narrower main column.
