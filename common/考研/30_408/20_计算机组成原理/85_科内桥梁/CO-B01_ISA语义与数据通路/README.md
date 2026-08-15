# CO-B01｜ISA Semantic × Datapath

状态：LaTeX 工作稿待人工确认；Canonical Bridge 正文已建立并发布。

## Hook

ISA 给出软件承诺，数据通路需要值、依赖、允许写入和异常边界。若没有稳定 handoff，设计者只能从助记符猜通路，或从教材图反推 ISA。

## Mother Interface

```text
Instruction Semantic
-> Architectural Delta Packet
-> Value Dependency Contract
-> Datapath / Control Input
```

## Owners / Boundary

- Left Owner：[CO-02 ISA 与机器级程序](../../20_ISA与机器级程序/README.md)；
- Right Owner：[CO-03 CPU 数据通路与控制](../../30_CPU数据通路与控制/README.md)；
- 本 Bridge 只 Own 六字段语义包、翻译顺序和双向校验；
- C/ABI、编码与 EA 本体留在 CO-02，部件/MUX/排拍/控制字留在 CO-03，多指令 hazard 留在 CO-04。

## Read Next

- 新增指令或判断通路支持性：先读本 Bridge；
- 已进入资源冲突、微操作排拍或关键路径：转入 CO-03；
- 已进入多指令 need/ready、forwarding、stall：转入 CO-04。

## Canonical Manual

- [Canonical LaTeX 正文](CO-B01_ISA语义与数据通路_桥梁手册.tex)
- [Published PDF](../../../../90_publish/CO-B01_ISA语义与数据通路_桥梁手册.pdf)

## 当前状态

CO-02/03 两侧 Owner 已存在，接口通过 Bridge Validity 与 Standalone Promotion 两道 Gate。正文仍待人工确认，不代表规则已通过真题验证。

## Review v1
已核对六字段架构状态差包、值依赖契约、ADD/LOAD 最小例和双向校验；保持 C/ABI、部件、hazard 的停止边界。下一轮用 store、分支和异常指令验证语义包完整性。
