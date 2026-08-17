# 通信基础与网络性能：把信息送过有限信道

状态：已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证。

## Hook

提高链路速率只能缩短序列化时间，不能消除传播距离。本册从信息的物理表示出发，把 bit/symbol/signal、容量上限、四类时延、store-and-forward、流水线、throughput 与 BDP 组织成一张时间和容量地图。

## Scope / Stop Boundary

本册 Owns source/transmitter/channel/receiver/destination 的物理链，传输介质与接口特性，repeater/hub，编码/调制/复用的选择边界，Nyquist/Shannon 的 408 模型，电路/报文/分组交换及数据报/虚电路，四类 delay、流水线、throughput 与 BDP。

不拥有共享介质争用、可靠窗口或拥塞反馈；它只输出链路速率、传播时间和在途规模给 NET02、NET03、NET07。

## Read Next

- [NET02 单跳交付](../02_单跳交付_帧_MAC_局域网与交换机/README.md)
- [NET03 可靠传输](../03_可靠传输_序号_ACK_定时器与滑动窗口/README.md)
- [网络做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-01_通信基础与网络性能_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-01_通信基础与网络性能_方法论手册.pdf)

## Source Diff

旧 README 的全部机制、公式、母例、边界与来源说明已迁入唯一 `.tex`；本轮按 2026 考纲覆盖审计补入通信物理链、传输介质、物理接口、repeater/hub、报文交换、数据报/虚电路及其状态位置模型。8 页 Published View 已同步，正文保留候选标记以等待题目验证。
