# NET-I01｜一个网络请求的一生：从域名到网页返回

状态：已采用候选；Canonical Integration 正文已建立并发布，组合边界已复核。

## Hook

浏览器只有 URL 时，配置、名字解析、逐跳转发、端点连接和 HTTP 语义必须按依赖组合；缓存与已有状态又会改变实际事件轨迹。本册追踪这条组合链，不重新解释任何局部协议。

## Canonical Problem

`URL -> DHCP（若无配置） -> DNS -> Destination IP -> FIB/Next Hop -> ARP/ND -> Frame/Switch -> Router/LPM -> TCP Endpoint -> HTTP Request/Response`

## Owns / Uses

- Owns 模块识别、组合次序、四条并行轨迹、失败分支与独立验证；
- Uses NET01--NET08 与 NET-B01--NET-B04；
- DNS、ARP、routing、TCP、拥塞和 HTTP 的机制仍由各 Topic Owner 修改。

## Stop Boundary

到第一份 HTTP response 被应用解释为止。NIC/driver/kernel stack、TLS/QUIC 内部、CDN 调度与浏览器渲染是 Extension；网络接收唤醒进程仍受 X-B04 Promotion Gate 约束。

## Canonical Manual

- [Canonical LaTeX 正文](NET-I01_一个网络请求的一生_综合手册.tex)
- [Published PDF](../../../../90_publish/408/NET-I01_一个网络请求的一生_综合手册.pdf)
