# ISA 与机器级程序：软件意图怎样成为可执行契约

状态：Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建。

> **迁移提示**：以下长篇内容是此前误写在 README 中的 working source。它可用于后续 Source Diff，但不再视为 Handbook 正文。正式手册必须迁入同目录 `.tex`；迁移完成后本 README 将压缩为引子、范围、边界和阅读链接。

## 1. 母问题

高级语言中的值、控制流与存储访问，怎样被翻译为处理器必须实现的软件可见行为？

ISA 是软件和处理器之间的契约，不是某张具体数据通路图：

```text
program intent
-> machine state representation
-> instruction semantic steps
-> next architectural state
```

## 2. ISA 承诺什么，不承诺什么

ISA 通常规定：

- 寄存器及其位宽、可见状态；
- 指令编码与操作语义；
- 地址形成、访存宽度、对齐和字节序规则；
- 控制转移、异常与特权接口；
- 某些内存顺序约束。

ISA 通常不规定：流水级数、Cache 容量、是否乱序、内部总线数、控制器由硬布线还是微程序实现。相同 ISA 可以有多种微架构。

## 3. 指令格式是有限编码预算

固定长度指令中的位要在 opcode、register、immediate 和 function 字段之间分配。

```text
more registers -> more register-index bits
larger immediate -> more immediate bits
more operations -> more opcode/function space
```

三者竞争同一编码预算，因此指令格式题的本质是约束分配，而非认图。

定长编码利于并行取指和规则译码；变长编码可提高代码密度，但增加边界识别和译码复杂度。RISC/CISC 是一组权衡，不是“简单一定快、复杂一定慢”的标签。

## 4. 寻址：先形成地址，再访问对象

寻址方式回答有效地址怎样形成：

$$
EA=f(\text{instruction fields},\text{register state},PC,\text{memory})
$$

| 方式 | 地址/操作数来源 | 额外代价 | 易混点 |
|---|---|---|---|
| 立即 | 指令字段就是值 | 受字段位数限制 | 没有数据访存 |
| 寄存器 | 寄存器中就是值 | 寄存器端口 | 不形成内存地址 |
| 基址+偏移 | $EA=R[base]+sext(imm)$ | 一次加法 | 数组、栈帧常用 |
| PC 相对 | $target=PC+offset$ | 加法与范围限制 | PC 基准以 ISA 为准 |
| 间接 | 内存内容再次作为地址 | 额外访存 | “取地址”和“取数据”分层 |

地址形成只产生 VA/逻辑地址；若系统启用地址翻译，后面还要经过 MMU。

## 5. 字节序、对齐与访问宽度

- **Endian** 决定多字节对象的各字节映射到递增地址的顺序，不改变寄存器内该值的数学意义；
- **Alignment** 约束对象起始地址是否为其粒度的倍数；未对齐访问是否允许、拆成几次事务或触发异常由 ISA/实现规定；
- **Load width** 决定读多少字节，signed/unsigned load 决定扩展方式；store 只写规定宽度的低位。

做题时必须画“低地址在左还是右”的地址表，不能只看十六进制字符串视觉顺序。

## 6. C 到机器状态的映射

### 6.1 表达式与数组

`a[i]` 的机器级核心不是方括号，而是地址算术：

$$
\operatorname{addr}(a[i])=base(a)+i\times sizeof(T)
$$

二维行优先数组：

$$
\operatorname{addr}(a[i][j])=base+(iN+j)\times sizeof(T)
$$

这条式子同时连接 ISA 寻址、Cache 空间局部性和虚拟页访问序列。

### 6.2 条件与循环

高级语言控制结构通常降为：比较产生条件、条件分支选择下一 PC、无条件跳转形成回边。分支目标是否采用 PC 相对、比较与分支是否合并，取决于 ISA。

### 6.3 函数调用

函数调用至少涉及四类约定：参数/返回值位置、返回地址、调用者/被调用者保存寄存器、栈帧布局。这些通常由 ABI 约定，不应全部误写为 ISA 硬件规则。

```text
caller prepares arguments
-> call changes control flow and return-address state
-> callee establishes frame / saves required state
-> return restores agreed state and PC
```

## 7. 四条母指令

| 指令族 | 读取 | 计算 | 可能访问内存 | 提交 |
|---|---|---|---|---|
| ADD | 两个源寄存器 | 算术结果 | 否 | 目标寄存器 |
| LOAD | base 寄存器 | 有效地址 | 读 | 目标寄存器 |
| STORE | base + data | 有效地址 | 写 | 内存状态 |
| BRANCH | 源寄存器 + PC | 条件与目标 | 仅取指路径 | PC |

这个表是后续数据通路和流水线分析的语义锚点。

## 8. 不变量与边界

| 维度 | 不变量 | 常见越界 |
|---|---|---|
| 编码 | 同一编码在当前 ISA 上语义确定 | 把教材数据通路当作 ISA 唯一实现 |
| 状态 | 指令结果按契约更新可见状态 | 把中间寄存器当架构寄存器 |
| 地址 | 地址形成与对象宽度明确 | 把指针位宽等同物理地址线数 |
| 调用 | ABI 双方对保存责任一致 | 把 ABI 当硬件自动保存 |
| 异常 | faulting 指令的可见效果符合精确性规则 | 一律假设“执行完才异常” |

机器字长、指针宽度、PC 宽度、物理地址宽度和指令长度相关但不必相等；题目未给架构时不能强行推出等式。

## 9. 母例：$x=a[i]+1$

一种 load/store ISA 的表示链：

1. 取得 `a` 的基址和 `i`；
2. 计算 $i\times\operatorname{sizeof}(element)$；
3. 与基址相加形成元素地址；
4. load 元素到寄存器，并按类型扩展；
5. add immediate 1；
6. store 回目标位置或保存在寄存器，取决于 `x` 的分配。

这里没有唯一指令序列：优化器、寄存器分配和 ISA 都会改变表示，但 C 层可观察语义必须一致。

## 10. 做题调用协议

1. 列出指令前后的架构状态差；
2. 解码字段预算，明确每个字段的解释；
3. 区分 value、address、address of address；
4. 先算 EA，再处理 endian/alignment/translation；
5. 函数题分开 ISA 事实、ABI 约定和编译器选择；
6. 最后把语义交给数据通路，不反向用某张图篡改 ISA。

## 11. 最小反例

- 32 位指令不推出 PC 是 32 位；指令宽度与地址宽度是不同预算。
- “大端机器寄存器里高字节在低位”错误；字节序描述内存地址顺序。
- `LOAD` 的最终对象在内存，不代表有效地址必须再访问内存才能形成。

## 12. 压缩信号

> ISA 先说“必须发生什么”，微架构再决定“怎样和何时发生”。

## 13. 校验依据

- [RISC-V RV32I 官方规范](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)用于校验定长格式、load/store、branch 与 sign extension 的契约式表达。
- 归档《指令格式、寻址方式、指令类型》用于覆盖 408 题型；其中 OS 上下文切换内容不纳入本 Topic。
