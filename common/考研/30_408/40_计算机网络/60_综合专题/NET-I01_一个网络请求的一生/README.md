# NET-I01｜一个网络请求的一生：从域名到网页返回

状态：目录已建立；已有综合工作稿可作为 Source，正文待按新 Ownership 复核。

## Canonical Problem
浏览器拥有一个 URL 后，从名字解析到请求/响应返回，网络各 Topic 怎样协作？

## Composition
`URL -> DNS -> Destination IP -> Route/Next Hop -> ARP/MAC -> One-Hop Frames -> Routers/Forwarding -> TCP Endpoint -> HTTP Request/Response`

## Tracks
- Name / Address；
- Scope；
- Encapsulation；
- Distributed State；
- Feedback / Cost。

## Uses
NET01–NET08、NET-B01–NET-B04。

## Owns
完整网络请求轨迹，不重新拥有 DNS、ARP、routing、TCP、HTTP 等局部机制。
