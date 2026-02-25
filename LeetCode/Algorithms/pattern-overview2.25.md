# Algorithm Templates Collection

This document summarizes core algorithm templates learned so far.

The goal is not to memorize problems, but to recognize reusable patterns.

---

# 1️⃣ Stable Two-Pointer (Compression Pattern)

## When to Use
- Remove elements
- Remove duplicates
- Move zeroes
- Partition by condition
- In-place modification with order preserved

## Template

```python
slow = 0

for fast in range(len(nums)):
    if CONDITION(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1

# Optional cleanup step
for i in range(slow, len(nums)):
    nums[i] = FILL_VALUE
```

## Key Idea
- `slow` marks the boundary of valid elements.
- `fast` scans through the array.
- Preserves relative order (stable partition).

Time Complexity: O(n)  
Space Complexity: O(1)

---

# 2️⃣ Two-Pointer (Opposite Ends)

## When to Use
- Sorted arrays
- Two Sum II
- 3Sum
- Pair-based problems

## Template

```python
nums.sort()
left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        # process result
        left += 1
        right -= 1
    elif total < target:
        left += 1
    else:
        right -= 1
```

## Key Idea
- Requires sorted array.
- Moves inward based on comparison.
- Efficient for sum problems.

Time Complexity: O(n) per layer

---

# 3️⃣ Sliding Window (Fixed Size)

## When to Use
- Substring matching
- Anagram detection
- Fixed-length window problems

## Template

```python
# initialize window
for i in range(k):
    update_window()

# check initial window
check_condition()

# slide window
for i in range(k, len(arr)):
    remove_left()
    add_right()
    check_condition()
```

## Key Idea
- Window size is constant.
- Update incrementally instead of recomputing.
- Often used with frequency arrays.

Time Complexity: O(n)

---

# 4️⃣ Sliding Window (Variable Size)

## When to Use
- Longest substring problems
- Minimum window substring
- Dynamic interval problems

## Template

```python
left = 0

for right in range(len(s)):
    expand_window()

    while condition_invalid:
        shrink_window()
        left += 1

    update_answer()
```

## Key Idea
- Window grows and shrinks dynamically.
- Maintains a valid condition.

Time Complexity: O(n)

---

# 5️⃣ Double Hash Map (Bijection Pattern)

## When to Use
- Isomorphic strings
- Word pattern
- One-to-one mapping problems

## Template

```python
map1 = {}
map2 = {}

for a, b in zip(s, t):
    if a in map1 and map1[a] != b:
        return False
    if b in map2 and map2[b] != a:
        return False

    map1[a] = b
    map2[b] = a
```

## Key Idea
- Enforces bidirectional uniqueness.
- Prevents many-to-one mappings.

Time Complexity: O(n)

---

# 6️⃣ Frequency Counting Pattern

## When to Use
- Majority element
- Top K frequent
- Character counting
- Duplicate detection

## Template

```python
count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1
```

## Key Idea
- Use dictionary for counting.
- Efficient O(n) frequency tracking.

---

# 7️⃣ Bucket Sort Pattern

## When to Use
- Top K frequent elements
- Frequency-based grouping

## Template

```python
buckets = [[] for _ in range(n + 1)]

for num, freq in count.items():
    buckets[freq].append(num)

res = []
for i in range(n, 0, -1):
    for num in buckets[i]:
        res.append(num)
```

## Key Idea
- Frequency acts as index.
- Avoids full sorting.
- Space-for-time optimization.

Time Complexity: O(n)

---

# 8️⃣ Greedy Pattern

## When to Use
- Best Time to Buy and Sell Stock
- Interval scheduling
- Local optimal → global optimal problems

## Template

```python
min_value = float('inf')
best = 0

for x in nums:
    min_value = min(min_value, x)
    best = max(best, x - min_value)
```

## Key Idea
- Maintain best local state.
- Update answer incrementally.

Time Complexity: O(n)

---

# 9️⃣ Binary Search

## When to Use
- Sorted arrays
- Searching boundaries
- Logarithmic search problems

## Template

```python
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

Time Complexity: O(log n)

---

# 🔟 Backtracking

## When to Use
- Permutations
- Combinations
- Subsets
- Search all possible solutions

## Template

```python
def backtrack(path, choices):
    if base_condition:
        result.append(path[:])
        return

    for choice in choices:
        path.append(choice)
        backtrack(path, updated_choices)
        path.pop()
```

Time Complexity: Exponential

---

# 1️⃣1️⃣ Monotonic Stack

## When to Use
- Next greater element
- Daily temperatures
- Stock span
- Range maximum problems

## Template

```python
stack = []

for i in range(len(nums)):
    while stack and CONDITION:
        index = stack.pop()
        # update result

    stack.append(i)
```

Time Complexity: O(n)

---

# Final Notes

Mastering patterns is more powerful than memorizing individual problems.

Recognize the structure → Apply the template → Adjust conditions.

Algorithm learning is about pattern abstraction.
# 算法模板总览（Algorithm Templates Overview）

本文件整理当前阶段常见的算法模式与通用模板。

目标不是记住题目，而是掌握可复用的结构。

---

# 1️⃣ 稳定双指针（压缩模式）

## 适用场景
- 删除元素
- 数组去重
- 移动 0
- 条件分区（偶数在前、负数在前等）
- 原地修改且保持顺序

## 模板

```python
slow = 0

for fast in range(len(nums)):
    if 条件成立(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1

# 如果需要清理剩余部分（如补 0）
for i in range(slow, len(nums)):
    nums[i] = 填充值
```

## 核心理解

- `slow` 表示有效区边界
- `fast` 负责扫描数组
- 保持相对顺序（稳定分区）

时间复杂度：O(n)  
空间复杂度：O(1)

---

# 2️⃣ 对撞双指针

## 适用场景
- 有序数组
- 两数之和（排序版本）
- 三数之和（3Sum）
- 区间缩小问题

## 模板

```python
nums.sort()
left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        # 处理结果
        left += 1
        right -= 1
    elif total < target:
        left += 1
    else:
        right -= 1
```

## 核心理解

- 通常需要先排序
- 根据比较结果向中间移动
- 常用于求和类问题

时间复杂度：每层 O(n)

---

# 3️⃣ 固定长度滑动窗口

## 适用场景
- 子串匹配
- 异位词查找
- 固定长度窗口问题

## 模板

```python
# 初始化窗口
for i in range(k):
    更新窗口状态

# 检查初始窗口
检查条件

# 滑动窗口
for i in range(k, len(arr)):
    移除左侧元素
    加入右侧元素
    检查条件
```

## 核心理解

- 窗口长度固定
- 增量更新状态
- 常配合频率数组

时间复杂度：O(n)

---

# 4️⃣ 可变长度滑动窗口

## 适用场景
- 最长子串
- 最小覆盖子串
- 动态区间问题

## 模板

```python
left = 0

for right in range(len(s)):
    扩展窗口

    while 条件不满足:
        收缩窗口
        left += 1

    更新答案
```

## 核心理解

- 窗口动态扩展与收缩
- 维护合法区间

时间复杂度：O(n)

---

# 5️⃣ 双哈希映射（双向映射）

## 适用场景
- 同构字符串
- 单词模式匹配
- 一一映射问题

## 模板

```python
map1 = {}
map2 = {}

for a, b in zip(s, t):
    if a in map1 and map1[a] != b:
        return False
    if b in map2 and map2[b] != a:
        return False

    map1[a] = b
    map2[b] = a
```

## 核心理解

- 建立双向映射
- 防止多对一关系

时间复杂度：O(n)

---

# 6️⃣ 频率统计模式

## 适用场景
- 多数元素
- 高频元素
- 字符计数
- 去重判断

## 模板

```python
count = {}

for x in nums:
    count[x] = count.get(x, 0) + 1
```

## 核心理解

- 字典统计频率
- O(n) 统计效率

---

# 7️⃣ 桶排序模式

## 适用场景
- Top K 高频元素
- 频率分组问题

## 模板

```python
buckets = [[] for _ in range(n + 1)]

for num, freq in count.items():
    buckets[freq].append(num)

res = []
for i in range(n, 0, -1):
    for num in buckets[i]:
        res.append(num)
```

## 核心理解

- 频率作为索引
- 用空间换时间
- 避免排序

时间复杂度：O(n)

---

# 8️⃣ 贪心算法

## 适用场景
- 股票最大利润
- 区间调度
- 局部最优推出全局最优

## 模板

```python
min_value = float('inf')
best = 0

for x in nums:
    min_value = min(min_value, x)
    best = max(best, x - min_value)
```

## 核心理解

- 实时维护局部最优
- 每步更新全局答案

时间复杂度：O(n)

---

# 9️⃣ 二分查找

## 适用场景
- 有序数组查找
- 查找边界
- 对数时间搜索问题

## 模板

```python
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

时间复杂度：O(log n)

---

# 🔟 回溯

## 适用场景
- 全排列
- 子集
- 组合
- 枚举所有可能

## 模板

```python
def backtrack(path, choices):
    if 终止条件:
        result.append(path[:])
        return

    for choice in choices:
        path.append(choice)
        backtrack(path, 更新后的选择)
        path.pop()
```

时间复杂度：指数级

---

# 1️⃣1️⃣ 单调栈

## 适用场景
- 下一个更大元素
- 每日温度
- 股票跨度
- 区间最大值问题

## 模板

```python
stack = []

for i in range(len(nums)):
    while stack and 条件成立:
        index = stack.pop()
        # 更新答案

    stack.append(i)
```

时间复杂度：O(n)

---

# 总结

当前阶段已经掌握：

- 稳定双指针
- 滑动窗口
- 双向映射
- 频率统计
- 桶排序
- 贪心

下一阶段可以重点学习：

- 对撞双指针进阶（3Sum）
- 单调栈
- 二分查找
- 回溯算法

算法学习的核心是：

识别模式 → 套用模板 → 调整条件。
