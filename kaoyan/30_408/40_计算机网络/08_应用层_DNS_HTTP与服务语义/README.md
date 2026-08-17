# 应用层：把通信能力组织成可发现、可解释的服务

状态：已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证。

## Hook

Transport 只移动 datagram 或 byte stream，不知道域名、资源、邮件和文件意味着什么。本册解释应用怎样定义对象、名字、操作、消息、响应与长期状态。

## Scope / Stop Boundary

本册 Owns C/S 与 P2P、WWW browser/server/document/link/URL 组成、DNS hierarchy/delegation/cache、HTTP resource/representation/method/status、FTP control/data，以及 SMTP submission/relay、POP3/IMAP access 与 MIME 分工。

DHCP 的配置生命周期由 NET04 Owns；TCP/UDP 的连接与可靠性由 NET06 Owns；NET-I01 只组合调用本册输出。

## Read Next

- [NET06 传输层与 TCP](../06_传输层_端点_UDP与TCP状态机/README.md)
- [NET-I01 一个网络请求的一生](../60_综合专题/NET-I01_一个网络请求的一生/README.md)
- [网络做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-08_应用层服务语义_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-08_应用层服务语义_方法论手册.pdf)

## Source Diff

旧 README 已完整迁入 `.tex`；新增 WWW 组成与对象依赖、DNS query/referral/cache、HTTP request/response 与连接依赖、FTP active/passive、SMTP relay 和 mailbox access 的协议流程。7 页 Published View 已同步；DNS/HTTP 的 transport mapping 保持为版本/题设边界。
