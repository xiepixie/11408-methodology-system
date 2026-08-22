# AI / ML Inbox

这里保存尚未通过 Area Boundary / Topic Ownership 判断的真实学习观察、算法疑问、Source Diff 与候选连接。

整理时先问：

1. 它属于哪个已锁定 Area 的既有解释责任？
2. 是 Leaf Topic 内的新 section，还是两个 Owner 之间的 Bridge？
3. 是多个模块共同完成一次任务的 Integration，还是纵向 Research Direction？
4. 是否真的出现了现有八个 Area 无法解释的新 Mother Question？

默认先路由，不因为看到新模型名、论文名或产品名就新增一级目录。

## 待整理

### GPU 并行计算 / Triton 算子实现的长期 Owner

本轮 FlashAttention 学习暴露出一个真实但尚未需要升级架构的边界：CUDA execution model、GPU memory hierarchy、Triton blocked-program abstraction、kernel autotuning / software pipelining 等知识会被多个深度学习算子复用，但当前八 Area / Leaf Boundary 中没有专门的 ML Systems / GPU Kernel Owner。

当前处理：

- Attention Topic 只 Own **理解 FlashAttention 所必需的最小 GPU/Triton 实现层**；
- generic AutoDiff 继续由 Area 50 / Leaf 07 Own；
- 不把通用 CUDA/Triton 编程大全塞进 Attention，也不立即新增 Core Leaf；
- 若后续在 GEMM、LayerNorm、MoE、quantization/custom ops 等至少两个独立机制中重复调用同一套 GPU kernel 心智模型，再做 Owner Diff，判断应进入 Research Direction、Atlas Supplement、Extension 或新的稳定 Leaf。

需要验证的判据：删掉 FlashAttention 以后，是否仍有一条可复用、能产生新判断的“tensor program → parallel decomposition → memory movement → scheduling → performance”母模型；若有，再决定是否晋升。

