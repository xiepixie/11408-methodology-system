# H-B02｜局部模型与区间定理：中值点、余项与误差控制

状态：待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅。

## Position

高数 Topic03 ↔ Topic04 的内部 Bridge。

## Mother Interface

研究局部 Taylor/插值模型怎样借助 Rolle 链、中值点构造和区间正则性，获得对整个区间有效的余项、误差和导数估计。

## Owns

只拥有“局部模型 → 区间存在性定理 → 误差控制”的接口；Taylor 本体归 Topic03，中值定理归 Topic04。

## Uses

Topic03、Topic04。

## Boundary

中值点通常只保证存在，不可随意固定；不同余项形式的正则性和区间条件必须分别核对。

## Source Pack

旧 `I-07.1_多中值点与参数`、`I-07.2_插值余项与导数估计` 为核心来源。

## 训练导航

- [局部模型到区间结论](局部模型到区间结论.md) —— 从局部 Taylor/导数信息制造零点结构，并经 Rolle 链升级为余项、误差界与区间结论。

## Manual

- Canonical Source：[局部模型与区间定理_中值点余项与误差控制.tex](局部模型与区间定理_中值点余项与误差控制.tex)
- Published View：[局部模型与区间定理_中值点余项与误差控制.pdf](../../../../90_publish/math1/局部模型与区间定理_中值点余项与误差控制.pdf)

## Review v2
I-07.1/I-07.2 已完成逐段 Source Diff。本轮把 Bridge 从“余项摘要”补成完整接口：多中值点由插点与区间分割保证彼此不同；中值点参数在二阶非退化时趋于 $1/2$、一般首个非零高阶为 $m$ 时趋于 $m^{-1/(m-1)}$；Lagrange/Hermite 余项统一为“零点/重零点 → Rolle 链 → 高阶导数见证”；点态余项进一步运输到积分误差、导数估计和滑动区间 Taylor。完整 Landau--Kolmogorov 理论仍作 Extension。状态仍待人工确认。
