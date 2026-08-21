# BDP × Window：用在途预算填满反馈管道

状态：已采用；Canonical Bridge 正文已建立并发布。305 题中已有直接性能题完成首轮验证，剩余只需补复杂口径变式。

## Hook

链路速率只说明“能多快发送”，窗口才决定反馈回来前允许保留多少未确认数据。本桥把物理 BDP 转换为可靠传输窗口与利用率条件。

## Scope / Stop Boundary

NET01 Owns rate、propagation、RTT 与 BDP；NET03 Owns window/ACK 机制。本桥只拥有两者间的量纲接口、利用率边界和题目口径辨识，不拥有流控或拥塞算法。

## Canonical Manual

- [Canonical LaTeX 正文](NET-B05_BDP与Window_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/NET-B05_BDP与Window_桥梁手册.pdf)

## Question Evidence

734 用 `symbol rate × propagation time` 验证“速率×时间=在途量”，761、762、772 则把完整反馈周期转换为滑动窗口/序号需求，949、953 从 TCP 侧验证窗口不足会限制发送。**Bridge 的核心量纲接口已验证**。后续只需补“异速率链路 + 非零 ACK 发送 + window/rwnd/cwnd 同时限制”的复杂变式。
