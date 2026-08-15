# OS-B03｜Process × File Reference

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS01 Process/Control ↔ OS05 File System。

## Mother Interface
`Task -> fd table entry -> OFD/open-file state -> inode/file object -> lifetime/reference changes`

## Owns
fork、dup、close、unlink 等操作怎样在 task、fd table、OFD、inode 不同层级改变引用关系。

## Boundary
process 本体由 OS01 Own；pathname/inode/OFD/file lifetime 语义由 File Topic Own；本 Bridge 只拥有引用交接与“哪个操作改变哪一层”。

## Manual
- [Canonical 正文](OS-B03_Process与FileReference_桥梁手册.tex)
- [Published PDF](../../../../90_publish/OS-B03_Process与FileReference_桥梁手册.pdf)

## Review v1
已核对 fd table、OFD、inode 三层对象及 fork/dup/close/unlink 的引用变化；下一轮用共享 offset 与 unlink-after-open 题验证。
