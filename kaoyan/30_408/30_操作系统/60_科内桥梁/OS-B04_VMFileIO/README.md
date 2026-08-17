# OS-B04｜VM × File × I/O

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS-04 Virtual Memory ↔ OS-06/07 File System ↔ OS-05 I/O。

## Mother Interface
`File Object + File Range <-> Cached/Resident Page State <-> Process VA Mapping <-> I/O Request/Completion <-> Persistent State`

## Owns
file-backed 内容身份、cached/resident state、VA mapping 与 I/O request/completion 在 File/VM/I-O 之间怎样分责与交接。

## Responsibility Split
- File：内容身份、文件偏移与持久对象；
- VM：虚拟映射、页驻留与 fault-side mapping；
- I/O：缺页/回写引出的设备请求、完成与等待。

## Anti-Bridge
`Hardware Cache != OS Page Cache`。

## Manual
- [Canonical 正文](OS-B04_VMFileIO_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/OS-B04_VMFileIO_桥梁手册.pdf)

## Review v2
已阻断“file range / page-cache frame / VA 是三个完全等价身份”的旧压缩，并移除固定 PTE 位、`TASK_UNINTERRUPTIBLE`、DMA/interrupt、4KB 与 `read=2 copies / mmap=1 copy` 等实现级绝对化。下一轮用 mmap fault、dirty writeback、durability 与共享映射陌生题验证。
