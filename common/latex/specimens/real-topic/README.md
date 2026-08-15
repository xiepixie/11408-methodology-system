# Real Topic Visual / Layout Gate

> **Canonical Source is not copied here.** The regression wrappers use `docmute` to read the current Canonical body directly while muting its preamble.
>
> **Target**：`common/考研/10_数学一/10_高等数学/04_局部到整体_中值定理与函数形状/局部到整体_中值定理与函数形状.tex`

## Files

```text
topic04-adapter.tex
    = compatibility glue only: map transitional `corebox` to `mentalmodel`

topic04-standard.tex
    = profile=standard wrapper

topic04-margin.tex
    = profile=margin + twoside wrapper
```

The adapter must never contain duplicated Handbook knowledge text.

## Baseline problem discovered

Before layout migration, Topic04 contained four width defects caused by old fixed-width table arithmetic:

```text
18.0pt overfull  — cross-page 3-column table
8.04pt overfull  — cross-page 5-column boundary table
18.0pt overfull  — cross-page Source-routing table
18.0pt overfull  — appendix fixed-width tabular
```

The repeated pattern came from treating fixed `p/L` content widths as if their sum could equal `\linewidth`, while inter-column `\tabcolsep` still consumed additional width.

The unadapted margin wrapper also exposed a separate structural defect: a six-stage process was encoded as one unbreakable boxed math line. That was a source-layout assumption, not proof that the margin profile itself was unusable.

## Layout-only migration performed — 2026-08-11

No knowledge claim, theorem, example, ownership boundary or problem-solving rule was changed.

The Canonical Topic now uses the forward Family API for the objects whose geometry genuinely requires it:

```text
3 cross-page fixed-width longtables
    -> handbooklongtable + flexible Y explanation columns

appendix fixed-width tabular
    -> handbooktable + flexible Y explanation column

2 six-stage one-line boxed chains
    -> processchain
       stages stay atomic
       line breaks allowed only at arrow boundaries

long English slash compounds
    -> explicit \allowbreak at semantic-safe slash boundaries
```

The Topic preamble was also opportunistically migrated from copied local typography/table/color definitions to the transitional `ipara-handbook.sty`. This is allowed by the global migration contract because the file already required a real layout repair; it was not a style-only rewrite.

To keep the transitional Canonical source and the experimental KOMA Family source-compatible, `common/考研/ipara-handbook.sty` now exposes thin compatibility shims for:

```text
handbooklongtable
processchain
```

The long-term implementations remain owned by `common/latex/ipara-handbook.cls`; the old package is not promoted back into a global architecture Owner.

## Final regression result

After the migration, all three execution paths compile successfully under TeX Live 2026 + XeLaTeX:

```text
A. Canonical Topic + transitional ipara-handbook.sty
B. ipara-handbook.cls profile=standard
C. ipara-handbook.cls profile=margin, twoside=true
```

Final diagnostics for all three:

```text
0 Warning
0 Overfull
0 Underfull
0 undefined / Undefined
0 Error
```

Therefore:

```text
Standard Real Topic Layout Gate = PASS
Margin Real Topic Layout Gate   = PASS
```

This is stronger than the earlier relative-regression result: the old four table-width diagnostics are no longer being carried forward.

## What this Gate proves

The evidence supports the following Design System decisions:

1. `handbooklongtable` is justified by real Canonical content, not only a synthetic demo.
2. `processchain` is justified as a structural display primitive: it solves a real profile-width failure without shrinking text or duplicating content.
3. A 116mm main reading column can contain this real mathematics Topic **when wide structures are expressed through the correct structural API**.
4. Fixed-width arithmetic such as `L{a} + L{b} + L{\linewidth-a-b}` should not be the forward authoring pattern.
5. Margin failure must first be diagnosed as a content-geometry contract problem before changing global page geometry.

## What this Gate does **not** prove

It does **not** prove that `profile=margin` should become the default Handbook profile.

The current Topic body contains almost no genuine semantic-margin content. The next gate is therefore informational rather than mechanical:

```text
add only a small number of truly supplementary margin objects
-> verify MainText remains complete when margin is hidden
-> inspect odd/even placement and density
-> compare retrieval/navigation value against profile=standard
```

Empty margin space is not information architecture. `116mm + 5mm + 39mm` remains a candidate geometry until that semantic-margin evaluation is complete.
