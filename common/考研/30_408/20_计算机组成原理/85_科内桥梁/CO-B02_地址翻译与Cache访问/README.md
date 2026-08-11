# CO-B02｜Address Translation × Cache Access

状态：目录已建立，正文未建。

## Owners
CO07 地址翻译硬件 ↔ CO06 Cache 与存储层次。

## Mother Interface
`VA -> Translation State -> PA -> Cache Address Fields -> Hit/Miss Path`

## Owns
TLB/page-table translation 的输出怎样成为 Cache/Memory 访问输入，以及地址位在组合访问路径中的责任边界。

## Boundary
Page Fault 的 OS 修复不属于本 Bridge；进入 X-B02。Hardware Cache ≠ OS Page Cache。
