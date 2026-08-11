# NET-B01｜IP Forwarding × Single-Hop Delivery

状态：目录已建立，正文未建。

## Owners
NET04 IP 地址与分组转发 ↔ NET02 单跳交付。

## Mother Interface
`Destination IP -> Next-hop IP -> Next-hop MAC -> Frame -> One-Hop Delivery`

## Owns
IP 层决定 next hop 后，怎样把网络层交付目标翻译成链路层一跳交付对象；每一跳为什么需要重新封装 MAC。

## Boundary
ARP 的 `NextHopIP -> MAC` 语义由 NET04 Own；frame/MAC/switch 交付由 NET02 Own。
