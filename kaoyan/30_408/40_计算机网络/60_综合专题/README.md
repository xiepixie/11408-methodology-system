# 计算机网络 Integration Layer

状态：框架已采用；NET-I01 已完成组合边界复核并发布 Canonical LaTeX 阅读版。

当前只建立：

- [NET-I01｜一个网络请求的一生：从域名到网页返回](NET-I01_一个网络请求的一生/README.md)

它把完整请求拆成两个时间尺度：事务层根据 `Intent + Current State` 决定下一步需要什么状态或报文；每产生一条 IP 数据报，就反复调用 `destination IP -> FIB/LPM -> next hop -> current-link identity -> frame -> next node` 的逐跳交付子程序。它追踪 Name / Scope / Encapsulation / State Owner / Plane 的协作，不重新教授 DNS、ARP、IP、TCP、HTTP 等局部机制。
