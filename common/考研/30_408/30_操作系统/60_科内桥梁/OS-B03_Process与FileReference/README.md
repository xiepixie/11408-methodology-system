# OS-B03｜Process × File Reference

状态：目录已建立，正文未建。

## Owners
OS01 Process/Control ↔ OS05 File System。

## Mother Interface
`Task -> fd table entry -> OFD/open-file state -> inode/file object -> lifetime/reference changes`

## Owns
fork、dup、close、unlink 等操作怎样在 task、fd table、OFD、inode 不同层级改变引用关系。

## Boundary
process 本体由 OS01 Own；pathname/inode/OFD/file lifetime 语义由 File Topic Own；本 Bridge 只拥有引用交接与“哪个操作改变哪一层”。
