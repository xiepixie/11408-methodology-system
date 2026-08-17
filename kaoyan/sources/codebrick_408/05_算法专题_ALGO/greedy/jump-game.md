---
title: 跳跃游戏：贪心 vs 动态规划
source: https://www.codebrick.tech/algo-blog/posts/greedy/jump-game.html
---

# 跳跃游戏：贪心 vs 动态规划

### 跳跃游戏贪心流程

## LC 55. 跳跃游戏

数组中每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个位置。

### 贪心 O(n)

维护能到达的最远位置，如果最远位置 ≥ 末尾，就能到达。javascript

```
function canJump(nums) {
  let farthest = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > farthest) return false; // 到不了位置 i
    farthest = Math.max(farthest, i + nums[i]);
  }
  return true;
}
```

## LC 45. 跳跃游戏 II

保证能到达末尾，求最少跳跃次数。

### 贪心 O(n)

类似 BFS 的层级遍历：每一"层"是当前跳一次能到达的范围。javascript

```
function jump(nums) {
  let jumps = 0;
  let curEnd = 0;    // 当前跳跃能到达的边界
  let farthest = 0;  // 下一跳能到达的最远处

  for (let i = 0; i < nums.length - 1; i++) {
    farthest = Math.max(farthest, i + nums[i]);
    if (i === curEnd) {
      jumps++;
      curEnd = farthest;
    }
  }
  return jumps;
}
```

**理解**：

- `curEnd` 是当前这一跳的边界
- 到达边界时必须再跳一次，`jumps++`
- 在这一跳的范围内，记录能到达的最远位置作为下一跳的边界

### 为什么贪心可行？

每一步我们都选择能跳到最远的位置——这保证了用最少的跳跃次数覆盖最多的距离。可以证明贪心选择不会错过最优解。

## 复杂度

- 时间 O(n)，空间 O(1)

## LeetCode 练习

- LC 55. 跳跃游戏 ⭐
- LC 45. 跳跃游戏 II ⭐
- LC 1306. 跳跃游戏 III