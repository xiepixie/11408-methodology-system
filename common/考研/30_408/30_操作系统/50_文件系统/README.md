# 文件系统

状态：目录已建立，已有发布物待纳管。

母问题：持久化字节怎样获得名称、对象身份、索引、打开实例和崩溃一致性？Owns pathname/dentry/inode、VFS、fd/OFD/offset、byte-to-block 与 journaling；`read()` 在形成 I/O request 后停止。

