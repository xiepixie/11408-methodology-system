# 操作系统全域结构与 Bridge / Integration 复核 v1

日期：2026-08-15  
场景：review  
范围：`30_408/30_操作系统/` 全目录

## 1. 复核目标

在外部 OS 笔记 76 篇全量 Source Diff 已完成后，不再继续按来源篇数扩写 Topic，而是反向检查当前 OS 稳定资产是否满足项目契约：

1. Subject Atlas 是否仍只有一个 Canonical Owner；
2. 六册 Foundation/Topic 是否保持唯一机制 Owner 与清晰 Stop Boundary；
3. Internal Bridge 是否真正只 Own handoff，而没有把 Linux/某教材实现当 OS 定义；
4. Integration 是否已经从 README 壳升级为可维护 `.tex`，并只 Own composition；
5. Rules 是否覆盖进程/调度/IPC 与新 Integration 暴露出的题面第一动作；
6. Source Diff / README 状态是否与真实文件事实一致。

## 2. 结论

### 2.1 Topic 层

OS-00、OS-01/02、OS-03、OS-04、OS-05、OS-06/07 的 Mother Model、Owner、Stop Boundary 与 CodeBrick 76 篇回写已经形成稳定闭环。本轮没有发现需要重写六册 Topic 的结构性缺口，结论为 `No topology change / No bulk rewrite`。

当前主要风险已从“知识缺失”转为“接口层旧口径残留”：Bridge 仍存在旧 Topic 编号和 Linux-specific representation 被写成定义的情况；两个 Integration 只有 README，没有 Canonical deep body。

### 2.2 Atlas / Landing

- `30_操作系统/README.md` 保持唯一 Canonical Subject Atlas。
- `00_学科总图/README.md` 从可能形成第二 Owner 的 `Owns` 改为 `Mirrors / Expands`，明确只派生根 Atlas 的深层地图。
- OS-B01--B04 README 的旧编号全部统一到当前拓扑：OS-01/02、OS-03、OS-04、OS-05、OS-06/07。
- CodeBrick OS Source Diff 顶部状态与 review index 由“仍在进行”修正为“76 篇逐篇语义核销与双向完成审计已完成”。

## 3. Bridge 第二轮语义收敛

### OS-B01 Wait / Block / Wakeup

旧问题：把 Wait Queue 固定定义为 Linux `task_struct` 双向链表、把 `TASK_*` 当跨系统状态定义、把 wake 写成“直接移入 run queue 并变 RUNNING”、把 `while` 推广成所有等待原语的绝对规则。

收敛后接口：

```text
Condition Unsatisfied
-> Register Wait + Block Safely
-> Event / State Change
-> Wake Eligible Waiter
-> Ready/Runnable
-> Scheduler/Dispatch
-> Reacquire Protection + Recheck if the interface requires it
```

稳定不变量是“检查条件失败到等待者已可被未来事件定位并安全让出 CPU 之间不能存在 lost-wakeup 窗口”；Linux wait queue 只保留为 implementation example。

### OS-B02 Process × Virtual Memory

旧问题：`task_struct/mm_struct/VMA/CR3` 被混进定义；默认任何 execution switch 都换页表；COW 被写成“所有可写 VMA + 固定 COW bit + 4KB copy”。

收敛后接口：

```text
Process Identity
-> Address-Space Association
-> fork Parent/Child Mapping Relation
-> private write
-> Protection Fault / COW Decision
-> Mapping Divergence if needed
-> Retry
```

关键边界：Execution Switch 不推出 Address-Space Switch；COW 只服务 private divergence semantics，显式共享 mapping 不机械套 COW；页大小、标志位、引用计数位置属于 VM 实现。

### OS-B03 Process × File Reference

旧问题：Bridge 自己 Own 最终文件销毁/块回收；把单个 `f_count` 当“所有打开引用”的总条件；Linux fd array / struct file / inode 字段被写成通用定义。

收敛后三层：

```text
Task descriptor binding
-> Open Instance / OFD
-> File Object
-> FS persistent mapping
```

Bridge 只 Own binding/reference handoff 与 shared-OFD current-offset 推论。文件对象最终删除、日志和空间回收继续由 OS-06/07 Own。

### OS-B04 VM × File × I/O

旧问题：把 `(inode, offset)`、Page Cache frame、VA 称为“三个完全等价身份”；固定 PTE.valid、TASK_UNINTERRUPTIBLE、DMA、interrupt、4KB，以及 `read=2 copies / mmap=1 copy` 等实现/性能结论。

收敛后接口：

```text
File Object + File Range
<-> Cached/Resident Page State
<-> Process VA Mapping
<-> I/O Request / Completion
<-> Persistent Storage State
```

明确 Content Identity、Residency State、VA Mapping 是不同关系；completion 先更新软件状态再 wake；dirty 与 durable 分开；buffered I/O 与 mmap 的性能只做 workload-dependent 比较。

## 4. Integration 建设

### OS-I01 Blocking `read()`

新建 Canonical `.tex`，Own：

```text
Running task
-> syscall
-> fd/OFD/file range
-> cached/resident?
-> I/O request if needed
-> wait/block
-> completion
-> Ready
-> scheduler/dispatch
-> resume syscall
-> return bytes/EOF/error
```

同时追踪 Control、File Reference、Data/Residency、Device/Completion 四条线。重点阻断：`read != disk I/O`、`submit I/O != block`、`completion != running`、成功 read 不保证返回请求长度 `n`。

### OS-I02 `fork()` + COW + Resource Reference

新建 Canonical `.tex`，把“fork 复制什么”改写为逐对象关系向量：

```text
New Identity
+ Execution Context semantics
+ Private/Shared VM mapping relation
+ fd binding copy
+ OFD reference sharing
+ File Object reference
-> later write/close/read/lseek/exec selectively changes one relation
```

重点阻断：fork 全量复制、父子共享整个地址空间、相同 fd 数字推出共享 offset、exec 创建新进程。

两册 Integration 均只组合既有 Topic/Bridge，不重新定义 COW、OFD、I/O 或 scheduler。

### 4.1 Derived Learning View 对齐

`80_实战课程/` 保持 Prototype / Derived Learning View，不晋升 Knowledge Owner。本轮只修与 Canonical 冲突/陈旧的路由与导航：Lesson 01/02 的 OS Anchor 统一为 OS-01/02；Source Manifest 的 Trap 路由改为 OS-00 + OS-01/02 + X-B01，并仅在设备完成分支调用 X-B03；Lesson 04 到 Lesson 05 的“待制作”陈旧标记移除；课程首页把“fork 复制整块内存”的误导式压缩改成“逻辑独立、物理暂时共享并按写分化”。

HTML 内的 xv6 结构体、PTE 位和 4 KiB page 继续保留，因为这些页面已经通过 QUALITY Gate 明确标注为 RISC-V / xv6 implementation，而不是 OS 定义。

## 5. Rules 增量

`90_做题规则/README.md` 新增待验证控制器：

- 状态题把 state label 落到 Queue / Wait Relation；
- 调度计算先定 Candidate / Key / Decision / Tie / Preemption；
- context-switch 计数先区分 event / save-restore / mode switch / address-space switch；
- IPC 先定 object / capacity / blocking semantics；
- fork 综合题逐对象标 Copy / Share / Reference / Rebuild；
- blocking read 同时画 Control / File / Data / Completion 四条线。

这些规则仍是 Candidate，未因静态正文完整而自动升级为“已采用”。

## 6. Legacy Source 路由

`60_科内桥梁/OS_科内桥梁与跨科接口_方法论手册.tex` 明确降为 Legacy Source，并在文件顶部加入禁止作为当前 Owner 的警告：

- Priority Inversion / inheritance / ceiling -> OS-03；
- MMIO / Port I/O -> CO-08 + X-B01/X-B03，OS-05 Use；
- Process × File -> OS-B03；
- VM × File/Page Cache -> OS-B04。

由于当前 Source 保留策略不删除历史知识文件，root legacy `.tex` 仍会触发 `A-ATLAS-DUPLICATE-TEX` audit；这是已知维护债务，不代表知识 Ownership 未决。

## 7. 验证

- OS-B01、B02、B03、B04 均经 `cognitive_system.py publish` 成功重新发布；页数分别 3 / 3 / 4 / 3。
- OS-I01、OS-I02 均经正式 publish 入口成功发布；均为 5 页。
- `80_实战课程/html` 当前 7 个 HTML（index + Lesson 01--06）经 HTML parser 检查无解析错误、无缺失本地 href；6 段 inline JavaScript 经 `node --check` 均通过。未建设的 Lesson 07--15 已从假链接改为 Planned 卡片，避免导航把“路线规划”伪装成已存在页面。
- 新 Integration 的下一验证门槛不是继续扩写，而是使用陌生题观察：能否无提示完成 `Owner Recognition -> Composition -> State Transition -> Independent Verification`。

## 8. 当前最小下一步

优先选择两类此前未用于写作的综合题：

1. 一个普通文件 blocking read，混入 cache hit/miss、I/O completion 和 scheduler 条件；
2. 一个 fork 后同时出现 COW write、共享 OFD offset 与 close/exec 的题。

记录第一处分歧（First Divergence）。只有重复出现相同错误入口时，才继续更新 Rules 或 Bridge；不要因为还能添加更多工程细节继续膨胀 Topic。
