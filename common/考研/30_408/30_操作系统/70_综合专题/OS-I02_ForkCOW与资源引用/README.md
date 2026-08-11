# OS-I02｜`fork()` + COW + Resource Reference

状态：目录已建立，正文未建。

## Canonical Problem
`fork()` 之后，新旧进程哪些状态复制、哪些资源共享、什么时候发生 COW 或引用关系分化？

## Composition
`Parent Task -> fork -> Child Task -> address-space relation + file-reference relation -> later write/close -> independent state changes`

## Uses
OS01、OS03、OS05、OS-B02、OS-B03。

## Owns
跨 Process/VM/File 的 fork 协作轨迹与分化时点，不重新拥有 COW、fd/OFD 或调度机制。

## Verification
逐对象检查 task identity、address space、PTE/page relation、fd table、OFD、inode 是否“复制 / 共享 / 引用计数变化”。
