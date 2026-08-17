# 计算机组成原理 CO02 ISA Source Diff

> 日期：2026-08-11
>
> 性质：Evidence 层 Handbook Diff，不是新的知识 Owner。

## 1. 产品与 Owner

- 产品：Topic CO-02《ISA 与机器级程序》。
- Canonical Owner：`30_408/20_计算机组成原理/20_ISA与机器级程序/CO-02_ISA与机器级程序_方法论手册.tex`。
- Knowledge 进入 Canonical `.tex`；题面动作进入计组 Rules；系统调用、上下文切换、OS handler 与存储硬件机制继续由相邻 Owner 负责。

## 2. Source Pack 核销

| Source | 结论 | 去向 |
|---|---|---|
| `CO-程序机器级表示与指令系统设计.md` | Canonical Update + Reject mix | 编码预算、扩展操作码、EA、机器级程序进入 CO02；固定 MIPS 格式、固定 PC 步长与 RISC/CISC 绝对化被降为例子或拒绝 |
| `CO-函数调用栈帧.md` | Canonical Update + Extension mix | 参数/返回值、返回地址、保存责任和栈帧进入 ABI 边界；具体 cdecl/stdcall、C++ inline 和堆管理不扩成 CO02 主干 |
| `CO-寄存器按可访问性分类.md` | Challenge + Explicit Reject | 保留“当前 ISA 是否提供合法操作”的判据；拒绝跨架构固定四级清单、OS 管理边界等于 ISA 边界、Cache/MMU 对所有特权软件绝对不可见 |
| `指令格式,寻址方式,指令类型.md` | Canonical Update + Split | ISA/格式/寻址进入 CO02；系统调用生命周期进入 X-B01/OS，进程切换与页表/TLB 进入 OS/CO07，blocking read 不进入本册 |
| `指令周期与时序.md` | Empty Source | 0 行，不产生更新 |
| `指令执行过程.md` | Empty Source | 0 行，不产生更新 |

## 3. Canonical Update

母模型固定为：

```text
Program Intent
-> Architectural State
-> Encoding / Address Semantics
-> Next Architectural State
```

正文补齐了模型含义、生成方向、对象/状态、编码预算、EA 生命周期、字节序/对齐、C 与函数调用、ISA/ABI 边界、代价权衡、五列概念边界、做题协议、考纲映射和 `x=a[i]+1` 贯穿母例。

## 4. Candidate Rules

新增或强化：指令题先写架构状态差、逐层扣除扩展前缀、EA 前区分 value/address/address-of-address、字节序先画地址表、函数调用分 ISA/ABI/编译器选择、各类宽度分开预算。

这些规则尚无真题表现证据，不进入“已采用”。

## 5. Explicit Rejects

- 32 位指令必然对应 32 位 PC、指针或物理地址；
- RISC 必然硬布线、CISC 必然微程序；
- CALL/RET、保存寄存器和栈清理在所有 ISA/ABI 上采用同一动作；
- 基址寻址天然等于某种 OS 物理重定位实现；
- PC、PSW、Cache、MMU 存在跨架构固定可见性等级；
- 未对齐访问必然采用同一种异常或事务拆分方式。

## 6. 结果与下一步

本轮结果是 **Canonical Candidate + Candidate Rules + Explicit Rejects**。CO02 已发布 9 页阅读视图；下一步以 CO02 输出的语义包和 CO03 输入的状态差/值依赖建立 CO-B01，不能让 Bridge 重讲 C、编码或数据通路本体。
