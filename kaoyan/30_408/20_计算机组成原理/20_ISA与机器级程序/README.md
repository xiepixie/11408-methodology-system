# ISA 与机器级程序：软件意图怎样成为可执行契约

状态：LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布。

## Hook

同一段 C 代码可以被不同微架构执行，但软件必须观察到一致的架构语义。本册追踪“程序意图 → 架构状态 → 编码/地址语义 → 下一架构状态”，把指令格式、寻址、机器级程序和 ABI 放回同一条生成链。

## Scope / Stop Boundary

本册 Owns ISA contract、架构状态、指令格式与编码预算、有效地址、访存宽度、字节序/对齐、C 到机器级语义和 ABI 调用边界。

不展开 CO-03 的数据通路与控制、CO-04 的流水线重叠、CO-06/07 的 Cache/TLB 实现，也不拥有 OS 的 fault、调度和上下文软件动作。

## Owns / Uses

- Uses CO-01 的位串解释与有限宽度运算；
- Outputs Read Set、Derived Values、Write Set、Next PC 和 EA 给 CO-03；
- 通过 CO-B01 与数据通路交接；
- ISA/特权与 OS 的接口上移到跨科 Bridge，ABI 不等于 ISA 自动行为。

## 训练导航

- [标志比较与条件转移](标志比较与条件转移.md)：训练有限位宽减法 → 算术标志（CF/OF/ZF/SF）→ signed/unsigned compare → 条件转移控制流；以 2023 Q16 为核心母题。
- [字节序、对齐与有效地址](字节序对齐与有效地址.md)：训练寻址方式与 EA 生成、大端/小端物理字节排布、边界对齐、结构体对齐三规则与多字节访存；以 2019 Q15 为核心母题，覆盖 2023 Q44、2018 Q15、2016 Q14/Q18、2017 Q13 与 2020 Q14。
- [指令格式、扩展操作码与相对寻址](指令格式、扩展操作码与相对寻址.md)：把指令格式压成 bit budget/escape 编码树，并用 `PC_base + sext(disp) × unit` 训练相对寻址与机器字长/指令字长边界。
- [函数调用、ABI 与编译器边界](函数调用、ABI与编译器边界.md)：训练把函数调用中的语言语义、ISA 原语、ABI 保存/传参与编译器具体选择分层，避免把某套栈帧或寄存器习惯升级成跨架构规律。

## Read Next

- [CO-03 CPU 数据通路与控制](../30_CPU数据通路与控制/README.md)
- [CO-B01 ISA Semantic × Datapath](../85_科内桥梁/CO-B01_ISA语义与数据通路/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-02_ISA与机器级程序_方法论手册.tex)
- [Published PDF](../../../90_publish/408/CO-02_ISA与机器级程序_方法论手册.pdf)

## 当前状态

本册已完成 CO-程序机器级表示与指令系统设计、CO-函数调用栈帧、CO-寄存器按可访问性分类及相关归档 Source 的第一轮 Owner Diff。正文仍是待人工确认候选；扩展操作码、EA、字节序/对齐、C/ABI 边界和 `x=a[i]+1` 母例已进入 Canonical，固定 MIPS/ABI/节拍被限制为例子或边界。Published PDF 为 9 页。
