# 计算机网络统一总图

状态：目录已建立，正文未建。

规划标题：《计算机网络统一总图：分布式状态、作用域与报文的一生》。

建议发布篇幅：12 到 16 页。篇幅只是约束 Atlas 不膨胀，不是完成标准。

## Position

本 Atlas 解释为什么出现网络机制，以及八个 Topic 各自解决什么问题。五层模型只作为作用域与覆盖地图，不直接变成五本专题。

## Mother Problem

独立机器之间的进程怎样在 Distance、Finite Capacity、Unreliability、Sharing、Heterogeneity 和 No Global State 的约束下通信？

这些矛盾分别生成 delay/pipelining、queue/congestion、ACK/retransmission、MAC/multiplexing、layering/IP 和 distributed routing 等机制。

## Owns

- 六个根本矛盾；
- Scope 模型；
- encapsulation 的职责边界；
- Name -> Address -> Route -> Next Hop -> MAC 交付链；
- Data Plane / Control Plane；
- Endpoint State / Network State；
- Reliability / Flow / Congestion 三分；
- 八个 Topic 的 Ownership 地图；
- 网络八问。

## Uses

八个 Topic 建成后，本 Atlas 只保留一段最小机制摘要和链接。

## Stop Boundary

不推导 Nyquist/Shannon，不模拟 GBN/SR，不计算子网，不运行 Dijkstra，不完整画 TCP 状态机，也不解释 HTTP 字段细节。

## 导航母题

“一个 packet 的一生”只作为地图：标出每一步所在作用域、状态持有者和 Owner，不在 Atlas 中打穿全过程。
