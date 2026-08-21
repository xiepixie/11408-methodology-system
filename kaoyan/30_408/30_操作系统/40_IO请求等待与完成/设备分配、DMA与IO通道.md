# 设备分配、DMA 与 I/O 通道

> 训练定位：解决“给逻辑设备名、SDT/DCT/COCT/CHCT、DMA、I/O Channel、SPOOLing，要求判断资源分配链、谁搬数据、谁控制序列、谁可能阻塞”的题目族。  
> 模型归属：[OS-05｜I/O 系统](OS-05_IO系统_方法论手册.tex)。设备独立性、经典设备分配表、DMA、I/O Channel 与 SPOOLing 的机制由 Canonical 正文拥有；本文件只训练资源链和责任边界。

## 母题表示：I/O 题先分四个问题

```text
Naming       我申请的是哪个逻辑/物理设备？
Allocation   哪些资源必须占有才能服务请求？
Movement     数据由 CPU/PIO 还是 DMA 搬运？
Control      谁组织一串 I/O 操作、谁报告完成？
```

这四个问题经常同时出现，但不是一回事。

## 问题一：设备独立性先从逻辑名开始

应用最好使用逻辑设备名；系统通过 LUT/映射把它解析到可用物理设备及驱动入口。

这层间接性允许：

- 同类设备替换；
- I/O 重定向；
- 应用不直接绑定具体硬件编号。

### 局部规则

**触发信号**：题面出现 logical device、LUT、设备独立性。

**第一动作**：先写“逻辑名 → 物理资源/驱动”的解析，再进入分配；不要把 LUT 和 DCT 当成同一张状态表。

**检查与退出**：如果答案已经开始讨论某个具体控制器是否忙，却还没说明逻辑设备名映射到了哪个设备类/实例，先退回 LUT/映射层；设备独立性解决“上层怎样不绑定具体硬件”，不等于设备已经成功分配。

## 问题二：经典设备分配链是多层资源检查

408 经典表：

- **SDT**：System Device Table，系统设备总表/入口；
- **DCT**：Device Control Table，具体设备状态、等待队列、驱动入口；
- **COCT**：Controller Control Table，控制器状态与连接关系；
- **CHCT**：Channel Control Table，I/O 通道资源状态。

可压成：

$$
\boxed{Process\ Request\to SDT\to DCT\to COCT\to CHCT}
$$

### 局部规则：申请“设备”可能隐含申请多层资源

**触发信号**：题目给设备空闲但控制器/通道忙。

**第一动作**：继续向上检查所需控制器和 Channel；设备本体空闲不等于整个 I/O 路径可立即建立。

**检查与退出**：只有设备、控制器、通道等本次请求必需层级都可建立绑定时，才可判断“可立即分配”；若某一层失败，必须把等待对象定位到该层，不能笼统写成“等待设备”。

## 问题三：动态分配逐层失败时，等待对象也不同

典型过程：

```text
locate device
-> check DCT
-> check COCT
-> check CHCT
-> all available: mark allocation and start
```

某层不可用时，进程等待的是**那一层资源可用**，不是笼统“等 I/O”。

回收也要恢复对应资源状态，并唤醒相应等待者。

### 死锁接口

若多个进程以不同顺序占有/申请：

```text
device -> controller -> channel
```

就可能形成资源等待环。此时交给并发/死锁模型分析，不要把所有设备等待都称为死锁。

## 问题四：DMA 主要卸载“逐字搬运”

经典 DMA：

```text
CPU/driver setup descriptor/address/count
-> DMA engine transfers device <-> memory
-> transfer completes
-> interrupt/completion notification
-> kernel completion path
```

CPU 仍负责：

- 提交请求；
- 设置方向、地址、长度；
- 管理映射/缓冲状态；
- 处理完成通知。

所以：

$$
\boxed{DMA\neq no\ CPU\ involvement}
$$

它只是把大块数据逐字节/逐字的搬运从 CPU 指令路径卸载。

## 问题五：DMA 的总线使用方式看“连续占多久”

经典教材常见：

- Cycle Stealing：每次拿少量总线周期，与 CPU 交替；
- Burst/Block：连续占用一段时间批量搬；
- Transparent：尽量在 CPU 不使用总线的空隙搬运。

### 检查

三者改变的是 CPU 与 DMA 对互连/存储器访问的竞争方式，不改变“DMA 负责设备与内存间数据搬运”这一核心责任。

## 问题六：I/O Channel 不是“可编程 DMA”的同义词

上传速记稿把 Channel 近似写成“可编程 DMA”。这可以作为很粗的升级直觉，但不应作为正式定义。

更稳定的层级区别：

### DMA

重点：

$$
\boxed{Offload\ Data\ Movement}
$$

CPU 配置一块传输，DMA 负责设备↔内存搬运。

### I/O Channel

经典大型机/教材模型：

$$
\boxed{CPU\ submits\ higher-level\ I/O\ job
\to Channel\ executes\ channel\ program}
$$

Channel 不仅搬数据，还能组织更完整的一串设备控制与 I/O 操作。

因此：

> **DMA 主要卸载搬运；Channel 进一步卸载控制与 I/O 序列组织。**

## 问题七：三类 Channel 按“共享方式”理解

- 字节多路通道：多个低速设备按小粒度交叉共享；
- 数组选择通道：一次选择一个高速设备，连续完成一批传输；
- 数组多路通道：在多个高速设备的块操作间复用。

做对比题固定问：

```text
一次服务谁？
占用多久？
每次传多少？
多个设备能否交叉推进？
```

不孤立背中文名称。

## 问题八：Interrupt 与 DMA 继续分线

- DMA：数据路径，谁搬数据；
- Interrupt：控制/通知路径，CPU 如何知道事件完成。

典型组合完全可以是：

```text
blocking read
+ DMA movement
+ interrupt completion
+ process Blocked -> Ready
```

I/O 完成后进程一般先变 Ready，是否立即 Running 仍由调度器决定。

## 问题九：SPOOLing 是虚拟设备/任务排队，不是“大 Buffer”

经典 SPOOLing：

```text
user task
-> disk input/output well + request queue
-> background service
-> exclusive physical device
```

核心效果：用户进程不再直接长期占有物理打印机等独占设备，而是提交逻辑任务，由后台进程排队服务。

### 边界

- 不会让打印机物理速度自动变快；
- submit completed ≠ physical output completed；
- 内存 buffer 与磁盘 spool well 是不同层次；
- Canonical 经典模型可依赖通道或等价卸载机制实现并发外围传输，但不能把“任何没有 Channel 的系统都绝不可能实现类似 spooling”当跨时代绝对命题。

## 代表母题：设备空闲但通道忙

进程 P 请求某设备：

```text
DCT: device free
COCT: controller free
CHCT: required channel busy
```

结论：当前完整资源链不可分配，P 需要按题设策略等待对应 Channel/资源释放；不能因为 DCT free 就开始传输。

## 代表母题：DMA 完成后进程是否立即运行

```text
P 发起阻塞 read
-> P Blocked
-> DMA 搬数据
-> completion interrupt
-> ISR/completion path marks P Ready
```

此时只能稳定推出：

$$P:Blocked\to Ready.$$

若 CPU 正在运行更高优先级进程，P 未必立即 Running。

## 陌生设备题固定落笔协议

```text
1. 先写 logical name 是否需要 LUT 解析。
2. 设备分配画 SDT -> DCT -> COCT -> CHCT 资源链。
3. 每层分别标 free/busy、owner、wait queue。
4. DMA 只回答数据搬运责任，不等于完成通知。
5. Interrupt 只回答完成通知/控制转移，不等于搬运。
6. Channel 写“执行通道程序、进一步卸载控制”，不要等同 DMA。
7. SPOOLing 写中转存储 + 请求队列 + 后台服务 + 独占设备虚拟化。
8. 最后检查：I/O complete 是否被错误写成原进程立即 Running？
```

## 最短压缩

> **设备题分资源链与责任链：SDT→DCT→COCT→CHCT 决定能不能分配；DMA 卸载搬运，Channel 进一步卸载控制序列，Interrupt 负责完成通知，SPOOLing 负责把独占设备任务化排队。**
