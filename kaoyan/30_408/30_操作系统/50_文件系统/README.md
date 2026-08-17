# 文件系统

状态：待人工确认；已发布。历史文件系统笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管。

> 持久化字节怎样获得名称、对象身份、索引、打开实例和崩溃一致性？

## Scope

本册沿 `Name -> Object -> Open State -> Data Mapping -> Persistent Protocol` 追踪文件从路径解析到打开、读写、块映射和崩溃恢复的一生。

## Owns / Uses / Stop Boundary

- **Owns**：pathname/directory entry/dentry/inode、VFS、fd/OFD/offset、文件生命周期、byte-to-block、free space、crash consistency 与 journaling。
- **Uses**：VM/I-O Bridge 的 Page Cache；I/O Topic 的 request/driver/completion；进程 Topic 的 fd 引用交接。
- **Stop Boundary**：`read/write` 形成 I/O request 后停止，不重讲 DMA、interrupt、block/wakeup 或 page-replacement policy。

## Read Next

进程与打开文件引用见 [Process × File Reference](../60_科内桥梁/OS-B03_Process与FileReference/README.md)，完整读路径见 [OS-I01](../70_综合专题/OS-I01_BlockingRead/README.md)。

## Manual

- [Canonical LaTeX](OS-06_OS-07_文件系统与持久化_方法论手册.tex)
- [Published PDF](../../../90_publish/408/OS-06_OS-07_文件系统与持久化_方法论手册.pdf)
