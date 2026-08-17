# 计算机组成原理 v3 统一总图 Model Diff 与 Canonical 增补

日期：2026-08-11

## Source

`30_408/00_统一总图/408统一总图_心智模型手册_v3.tex` 的计组章节（约第 451–588 行）及跨科接口段（约第 1003–1078 行）。该 `.tex` 按当前仓库契约属于 Atlas Deep Map / Source，不替代 `30_408/20_计算机组成原理/README.md` 的 Canonical Subject Atlas。

## 发现的缺口

1. 旧总图的计组母模型是 `ISA State -> Data Location -> Datapath/Control -> Timing -> Commit -> Cost`；当前 Atlas 原先只显式到 Commit，Cost 被零散放在 Rules，缺少统一入口。
2. 旧总图包含四个学习轴、LOAD 贯穿表、专题映射、六组边界和六步做题入口；这些内容没有完整出现在当前 Subject Atlas。
3. CO01–08 的局部正文已有不少机制，但读者缺少“本册坐标、输入/输出状态包、相邻 Owner 与局部成本”的显式导航。
4. 旧总图的编号把性能列为 CO-08、把总线/I/O 列为 CO-07；当前 Canonical Atlas 已把主存、数据通路、流水线、地址翻译、总线/I/O 分成 CO05–08，并规定性能是跨 Topic Cost 坐标，不是第九个硬件 Topic。

## Canonical Update

- 扩充 Subject Atlas：六格坐标、四个学习轴、LOAD 导航表、核心概念边界与六步做题入口；Cost 明确归 `90_做题规则` 与各 Topic 的局部参数。
- 扩充 Rules：完整 CPU time、CPI/总时间、throughput/latency、带宽瓶颈与协议效率。
- 在 CO01–08 各 Canonical `.tex` 增加“全科坐标与跨册交接”段，分别落实 `ISA State`、`Data Location`、`Datapath/Control`、`Timing`、`Resource/Cost`、翻译与 I/O 接口。
- 保留 CO-B01/B02 与 CO-I01 的现有 Bridge/Integration Owner，不复制旧总图的局部机制。

## 不采取的迁移

- 不把旧总图直接复制进每一册；总图负责 Map，Topic 负责 Depth。
- 不按旧编号新建一个“性能 Topic”；性能仍是跨册成本坐标。
- 不把旧总图中的 `TLB/Page Fault/Cache`、`Interrupt/DMA` 关系改写为单一机制；它们继续由 CO07/CO06/CO08 与 X-B02/X-B03 分责。

## 待验证

本轮解决的是地图覆盖和导航缺口，不等于知识已通过真题验证。后续用 LOAD/STORE/BRANCH、TLB+Cache、流水线性能和 DMA/中断综合题检查新增入口是否能改变首步推理，并据证据晋升 Rules。
