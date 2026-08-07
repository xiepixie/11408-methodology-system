# 计算机组成原理学科总图

状态：目录已建立，正文未建。

规划标题：《ISA 语义如何成为硬件时序》。

## Position

本 Atlas 建立整机视角和八个 Topic 的位置，不展开具体电路、地址题或流水线计算。

## Mother Model

$$
\text{Program Meaning}
\xrightarrow{ISA}
\text{Data Movement + Control + Timing}
\to \text{Committed State}
$$

## Owns

- ISA 与微架构的边界；
- State / Location / Path / Resource / Timing / Commit 统一语言；
- 指令主线、存储主线和 I/O 主线的连接地图；
- 正确性优先于性能优化的总约束。

## 三条主线

```text
Instruction: C -> ISA -> Datapath -> Pipeline
Storage: Address -> Main Memory -> Cache -> Translation
External: CPU -> Bus/Controller -> Device -> Interrupt/DMA
```

## Stop Boundary

不在 Atlas 中完整讲补码、控制信号、hazard、Cache 映射、页表位数或 DMA 时序。它们必须由各 Topic 独立拥有。

## 计划压缩页

一张 LOAD 全景图，但只标出每一步的 Owner，不展开慢路径。
