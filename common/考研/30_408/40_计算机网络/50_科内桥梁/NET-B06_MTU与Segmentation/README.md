# MTU × Segmentation：四层尺寸责任

状态：已采用；Canonical Bridge 正文已建立并发布，待题目验证。

## Hook

应用消息、TCP segment、IP packet 与链路 frame 各有自己的边界。路径 MTU 约束 IP 尺寸，MSS 才约束 TCP 数据段；本桥负责把两者接起来。

## Scope / Stop Boundary

NET04 Owns MTU、IP packet 与 fragmentation/PMTU；NET06 Owns TCP segmentation、MSS 与 byte stream。本桥只拥有尺寸预算、Owner 分工与跨层失败分支，不重讲 IP/TCP 首部字段。

## Canonical Manual

- [Canonical LaTeX 正文](NET-B06_MTU与Segmentation_桥梁手册.tex)
- [Published PDF](../../../../90_publish/NET-B06_MTU与Segmentation_桥梁手册.pdf)
