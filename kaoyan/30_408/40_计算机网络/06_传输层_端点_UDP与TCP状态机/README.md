# 传输层：从 host 交付到 process 会话

状态：已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证。

## Hook

IP 只能把 packet 送到 host；port 与 endpoint state 才能把数据交给正确 process。TCP 进一步用双向 byte sequence、ACK、窗口和连接状态构造有序 byte stream。

## Scope / Stop Boundary

本册 Owns port/socket endpoint、mux/demux、UDP/TCP 首部与 pseudo-header、TCP connection identity、SEQ/ACK、三次握手、数据传输、`rwnd`、zero-window probe、half-close、TIME-WAIT 与 RST。

通用可靠正确性由 NET03 Owns；`cwnd` 的反馈算法由 NET07 Owns；process block/wakeup 只通过 X-B04 Candidate 接口引用，不进入本册协议正文。

## Read Next

- [NET03 可靠传输](../03_可靠传输_序号_ACK_定时器与滑动窗口/README.md)
- [NET07 拥塞控制](../07_拥塞_共享资源与反馈控制/README.md)
- [NET-B03 Reliable Transfer × TCP](../50_科内桥梁/NET-B03_ReliableTransfer与TCP/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-06_传输层与TCP_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-06_传输层与TCP_方法论手册.pdf)

## Source Diff

旧 README 已完整迁入 `.tex`；本轮补齐 UDP 固定首部/长度、TCP Data Offset/flags/window/checksum/options，以及 pseudo-header 与线上首部的严格边界。8 页 Published View 已同步，TCP 未被简化成 GBN 或 SR。
