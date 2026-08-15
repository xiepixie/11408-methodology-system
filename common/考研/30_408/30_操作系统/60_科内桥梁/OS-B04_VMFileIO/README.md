# OS-B04｜VM × File × I/O

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS03 Virtual Memory ↔ OS05 File System ↔ OS04 I/O。

## Mother Interface
`File-backed content -> page identity/mapping -> resident state -> miss/writeback I/O -> mapping remains valid`

## Owns
file-backed page、Page Cache、mmap 相关内容在 File/VM/I-O 之间怎样分责与交接。

## Responsibility Split
- File：内容身份、文件偏移与持久对象；
- VM：虚拟映射、页驻留与 fault-side mapping；
- I/O：缺页/回写引出的设备请求、完成与等待。

## Anti-Bridge
`Hardware Cache != OS Page Cache`。

## Manual
- [Canonical 正文](OS-B04_VMFileIO_桥梁手册.tex)
- [Published PDF](../../../../90_publish/OS-B04_VMFileIO_桥梁手册.pdf)

## Review v1
已核对 file identity、page identity、mapping、residency、I/O request 的分层；下一轮用 mmap 缺页、脏页回写和共享映射题验证。
