# OS-I02｜`fork()` + COW + Resource Reference

状态：LaTeX 工作稿待人工确认；Canonical Integration 正文已建立并发布。

## Canonical Problem
`fork()` 之后，新旧进程哪些状态复制、哪些资源共享、什么时候发生 COW 或引用关系分化？

## Composition
`Parent Task -> fork -> Child Task -> address-space relation + file-reference relation -> later write/close -> independent state changes`

## Uses
OS-01/02、OS-04、OS-06/07、OS-B02、OS-B03；只有题目继续进入共享内存同步或实际 I/O 时，再调用 OS-03 / OS-05。

## Owns
跨 Process/VM/File 的 fork 协作轨迹、逐对象 Copy/Share/Reference/Rebuild 判定与分化时点，不重新拥有 COW、fd/OFD 或调度机制。

## Verification
逐对象检查 task identity、execution context、private/shared mapping、fd binding、OFD/open instance、file object 是否“复制 / 共享 / 引用 / 后续分化”，不把具体内核引用计数字段当成跨系统定义。

## Manual
- [Canonical 正文](OS-I02_ForkCOW与资源引用_综合手册.tex)
- [Published PDF](../../../../90_publish/408/OS-I02_ForkCOW与资源引用_综合手册.pdf)
