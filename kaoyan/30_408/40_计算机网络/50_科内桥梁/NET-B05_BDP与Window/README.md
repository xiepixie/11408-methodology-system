# BDP × Window：用在途预算填满反馈管道

状态：已采用；Canonical Bridge 正文已建立并发布，待题目验证。

## Hook

链路速率只说明“能多快发送”，窗口才决定反馈回来前允许保留多少未确认数据。本桥把物理 BDP 转换为可靠传输窗口与利用率条件。

## Scope / Stop Boundary

NET01 Owns rate、propagation、RTT 与 BDP；NET03 Owns window/ACK 机制。本桥只拥有两者间的量纲接口、利用率边界和题目口径辨识，不拥有流控或拥塞算法。

## Canonical Manual

- [Canonical LaTeX 正文](NET-B05_BDP与Window_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/NET-B05_BDP与Window_桥梁手册.pdf)
