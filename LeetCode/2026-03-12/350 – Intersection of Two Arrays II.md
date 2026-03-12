# LeetCode 350 – Intersection of Two Arrays II
## 两数组交集（允许重复）

---

## 📌 题目描述

给定两个整数数组 `nums1` 和 `nums2`，返回它们的交集。

要求：

- 每个元素在结果中出现的次数
- 等于它在两个数组中出现次数的最小值
- 结果顺序不限

---

## 🧠 本题核心本质

这是一个：

> 两数组 + 需要统计次数 + 取最小值

的问题。

因此必须使用：

```
哈希表（dict）
```

不能使用 set。

原因：

- set 只能判断“是否存在”
- dict 才能记录“出现次数”

---

# 🎯 解题思路（逐步推导）

## 第一步：统计 nums1 中每个元素出现次数

例如：

```
nums1 = [1,2,2,1]
```

统计结果：

```
{1:2, 2:2}
```

实现方式：

```python
mp = {}
for num in nums1:
    mp[num] = mp.get(num, 0) + 1
```

解释：

- `mp.get(num, 0)`：如果 num 不存在返回 0
- 每遇到一次就 +1
- 得到频率字典

---

## 第二步：遍历 nums2

例如：

```
nums2 = [2,2]
```

遍历过程：

- 遇到 2
- 检查是否在 mp 中
- 并且 mp[2] > 0
- 加入结果
- 次数减 1

---

## 为什么要减 1？

因为题目允许重复。

如果：

```
nums1 = [2,2]
nums2 = [2,2]
```

正确答案是：

```
[2,2]
```

如果你直接删除：

```
del mp[2]
```

那第二次就匹配不到了。

所以必须：

```
mp[2] -= 1
```

这叫：

> 消耗一次计数

---

# 💻 完整代码（推荐写法）

```python
class Solution:
    def intersect(self, nums1, nums2):

        # 优化：保证 nums1 是较小数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # 统计较小数组的频率
        mp = {}
        for num in nums1:
            mp[num] = mp.get(num, 0) + 1

        result = []

        # 遍历另一个数组
        for num in nums2:
            if num in mp and mp[num] > 0:
                result.append(num)
                mp[num] -= 1

        return result
```

---

# 🔎 逐行代码解析

```python
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
```

作用：

- 哈希表建立在小数组上
- 节省空间
- 降低时间常数

---

```python
mp = {}
```

创建空字典，用于存储频率。

---

```python
mp[num] = mp.get(num, 0) + 1
```

统计频率。

---

```python
if num in mp and mp[num] > 0:
```

判断两个条件：

1. num 存在
2. 还剩次数

---

```python
mp[num] -= 1
```

消耗次数。

---

# ⏱ 时间复杂度

```
O(n + m)
```

- n = len(nums1)
- m = len(nums2)

哈希查找平均 O(1)。

---

# 🗂 空间复杂度

```
O(unique elements in smaller array)
```

因为只统计小数组。

---

# 🚀 进阶写法（Counter 版本）

```python
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        inter = c1 & c2
        return list(inter.elements())
```

---

## Counter 原理

- `c1 & c2` 会自动取最小次数
- `elements()` 会按次数展开元素

例如：

```
Counter({2:2}) & Counter({2:3})
```

得到：

```
Counter({2:2})
```

---

# 🧠 模式总结

当遇到：

> 两数组问题

要问自己：

1. 是否需要去重？
   - 是 → set
2. 是否需要次数？
   - 是 → dict
3. 交集是最小次数？
   - min
4. 并集是最大次数？
   - max

---

# 🎯 本题训练点

- dict 频率统计
- 次数消耗模型
- 两数组哈希优化
- 小数组优先策略
- 时间复杂度思维

---

# 📌 关键记忆句

```
允许重复 → 必须计数 → dict
消耗次数 → 减 1
```

---

# 完整结论

这道题属于：

```
两数组 + 计数交集
```

核心结构是：

```
频率统计 + 次数控制
```

掌握它，你就掌握了：

- 350
- 多数组交集
- TopK 变体
- 频率排序基础
