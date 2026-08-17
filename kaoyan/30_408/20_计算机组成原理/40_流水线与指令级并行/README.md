# 流水线与指令级并行：重叠执行怎样保持顺序语义

状态：LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布。

## Hook

流水线提升稳态吞吐，不自动缩短单条指令延迟。本册把多条指令放到同一时间轴上，追踪依赖、资源、need/ready、forward/stall/flush 与精确提交。

## Scope / Stop Boundary

本册 Owns stage timing、latency/throughput、结构/数据/控制 hazard、旁路、停顿、冲刷、CPI、精确异常和 408 范围内 ILP。

不重讲 CO-03 的单指令微操作，不拥有 Cache/TLB 状态机；完整乱序、多核一致性和编译器后端只保留 Extension。

## Owns / Uses

- Uses CO-02 的 ISA 顺序语义和 CO-03 的单指令依赖/提交；
- Uses CO-06/07 的 miss/fault 延迟接口；
- 输出多指令的 need/ready、资源和提交约束给 CO-I01；
- 固定停顿数必须绑定题设 stage、旁路和存储延迟。

## Read Next

- [CO-03 CPU 数据通路与控制](../30_CPU数据通路与控制/README.md)
- [CO-B01 ISA Semantic × Datapath](../85_科内桥梁/CO-B01_ISA语义与数据通路/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-04_流水线与指令级并行_方法论手册.tex)
- [Published PDF](../../../90_publish/408/CO-04_流水线与指令级并行_方法论手册.pdf)

## 当前状态

正文已吸收归档《指令流水线》的可迁移主干：吞吐/延迟、stage、三类 hazard、need/ready、forwarding、stall、flush、分支与 CPI。固定五级停顿数、现代处理器具体参数和 RISC/CISC 绝对化结论仍需题设或真题证据。
