# 计算机网络做题规则

状态：工作稿，待验证规则已建立，尚无已采用规则。

## 已采用

暂无。以下规则先进入待验证区。

## 待验证

### 第一问先定 Scope

做网络题前先写当前讨论一跳、端到端、一个 AS 还是跨 AS。字段和状态必须放回其有效范围。

### 名字必须写类型

出现“地址”“目的地”“端点”时，明确它是 domain、IP、next-hop IP、MAC、port 还是 socket endpoint。

### 表的生成与使用分开

转发表题先判断当前是在运行 forwarding lookup，还是在模拟 routing protocol 更新表项。

### 可靠、流控、拥塞先写受保护对象

先判断问题保护的是 data delivery、receiver buffer 还是 network capacity，再选择 sequence/ACK、`rwnd` 或 `cwnd` 模型。

### 性能题先画时间线

先分开 transmission、propagation、processing、queueing 和等待 ACK 的区段，再使用 RTT、BDP、window utilization 等公式。

## 已否定

暂无。
