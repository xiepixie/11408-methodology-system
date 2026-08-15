# 操作系统实战课程 · HTML 教学视图

> 状态：Prototype / Derived Learning View（非 Canonical Knowledge Owner）
>
> 目标：把 MIT 6.1810 / xv6 的公开课程、实验与源码，重新组织成服务 408 的中文交互式 HTML 教学页。

## 1. 边界

本目录不是第六个 OS Topic，也不替代现有 Handbook。

- **408 稳定知识 Owner**：仍由 `../README.md`、五个 Core Topic 的 Canonical `.tex`、Bridge / Integration 与 `../90_做题规则/README.md` 持有。
- **MIT / xv6**：作为真实系统 Source 与实验载体，用来让抽象机制“跑起来”。
- **HTML**：Derived Learning View。负责教学顺序、动画、源码路径、实验提示、408 Bridge 与 retrieval check；若 HTML 与 Canonical Handbook 冲突，以 Canonical Owner 为准，并回到 Owner 做 Source Diff。
- **不镜像课程网页**：正文重新讲解，只保留必要的来源链接、源码定位和实验任务摘要。

## 2. 文件结构

```text
80_实战课程/
├── README.md
├── SOURCES.md
└── html/
    ├── index.html
    └── 01-os-interface.html
```

后续 HTML 一页一个教学单元，保持可直接在浏览器打开，不依赖构建系统。

## 3. 课程主线

```text
程序看到的 OS 接口
-> user/kernel 与 system call
-> trap / interrupt / exception
-> page table / address space
-> page fault / COW
-> process / scheduling / context switch
-> lock / sleep / wakeup / coordination
-> deadlock（408 定制实验）
-> device / interrupt / DMA / I/O
-> file / inode / block / logging
-> mmap 与 VM × File
-> Blocking read / fork+COW 综合追踪
```

MIT 6.1810 提供真实机制与 xv6 实验；408 缺而 MIT 不以考试形式覆盖的部分（调度算法、Banker、典型页面置换等）由我们补成短实验。

## 4. 页面统一结构

每页尽量固定为：

1. **Mother Question**：这一页真正解决什么问题；
2. **Minimum Model**：最小对象 / 关系 / 队列；
3. **Mechanism Trace**：一次真实事件怎样推进状态；
4. **xv6 Code Path**：代码入口、关键 struct / function；
5. **Interactive Lab**：可观察、可修改、可验证；
6. **408 Bridge**：教材抽象 ↔ xv6 对象 ↔ 考题语言；
7. **Boundary / Anti-Pattern**：最容易混淆的边界；
8. **Retrieval Check**：关闭页面后必须能复原的起手与主链。

## 5. 当前进度

- [x] 建立 MIT 6.1810 / xv6 Source Manifest；
- [x] 建立 HTML 课程总览页；
- [x] 第一页：操作系统接口——从用户程序到内核；
- [ ] 第二页：System Call——一次受控的控制权转移；
- [ ] 第三页：Trap——异常、中断与系统调用为何能共用入口；
- [ ] 后续按 `SOURCES.md` 的 408 路线逐页推进。
