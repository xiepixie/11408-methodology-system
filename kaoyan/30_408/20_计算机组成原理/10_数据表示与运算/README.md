# 数据表示与运算

> 类型：Topic
> 状态：LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布。

## 引子

同一串比特怎样在给定位宽、解释和运算规则后得到确定结果？

```text
Bit Pattern
-> Interpretation
-> Exact Value
-> Operation
-> Finite-width Result
-> Lost Information / Flags
```

## Scope

本 Topic 拥有位权、位宽、unsigned/signed、原码与补码、扩展/截断/移位、ALU 标志、定点乘除基本算法、溢出、除零检测、IEEE 754 编码、运算链与舍入。

它给 CO-02/03 提供“操作数和结果在有限格式中意味着什么”，但不拥有 ISA 对异常、饱和、舍入模式和标志寄存器的具体软件契约，也不展开完整 CPU 数据通路。

## Stop Boundary

- 本册解释电路能检测什么；检测后是异常、规定值还是软件可见标志归 ISA。
- 本册解释乘除的寄存器布局与循环不变量；具体教材变体必须由题设确认。
- C/C++ 的整数提升和未定义行为不是本册 Owner，只在机器级映射处作为接口。

## 阅读

- [Canonical 深度正文](CO-01_数据表示与运算_方法论手册.tex)
- [发布 PDF](../../../90_publish/408/CO-01_数据表示与运算_方法论手册.pdf)
- [计组 Subject Atlas](../README.md)
- [计组做题规则](../90_做题规则/README.md)
- [ISA 与机器级程序](../20_ISA与机器级程序/README.md)

## 来源状态

旧定点、浮点、乘法、除法和运算电路笔记只作为 Source；Source Diff 见 `80_evidence/review_log/`。本 README 只负责入口、边界与导航。
