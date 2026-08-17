# OS-B03｜Process × File Reference

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS-01/02 Process/Control ↔ OS-06/07 File System。

## Mother Interface
`Task descriptor binding -> Open Instance/OFD -> File Object -> reference/lifetime handoff`

## Owns
fork、dup、close 等操作怎样在进程 descriptor binding、OFD/open instance、file object 不同层级改变引用关系；unlink 的命名变化由 OS-06/07 Own，本 Bridge 只追踪它与既有打开引用的交接。

## Boundary
process 本体由 OS-01/02 Own；pathname/inode/OFD/file lifetime 语义由 OS-06/07 Own；本 Bridge 只拥有引用关系在两侧 Owner 之间怎样交接，以及“哪个操作改变哪一层”。

## Manual
- [Canonical 正文](OS-B03_Process与FileReference_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/OS-B03_Process与FileReference_桥梁手册.pdf)

## Review v2
已把具体 fd array / `struct file` / 单一 `f_count` 从通用定义中移除；Bridge 只 Own binding/reference handoff 与“同一 OFD ⇒ 共享 current offset”等推论，最终文件对象删除/块回收回到 OS-06/07。下一轮用共享 offset 与 unlink-after-open 陌生题验证。
