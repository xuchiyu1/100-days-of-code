# 两数组并集（保留最小次数）扩展解析

---

## 🧩 题目

给两个数组：

```
nums1 = [1,2,2]
nums2 = [2,2,3]
```

输出：

```
[2,2]
```

规则：

> 每个元素保留两个数组中的最小出现次数

---

# 🎯 核心思路

1. 分别统计两个数组的频率
2. 遍历所有 key
3. 取 min(count1, count2)

---

# 🧠 手推过程

nums1 统计：

```
{1:1, 2:2}
```

nums2 统计：

```
{2:2, 3:1}
```

遍历所有 key：

```
{1,2,3}
```

计算：

- 1 → min(1,0) = 0
- 2 → min(2,2) = 2
- 3 → min(0,1) = 0

结果：

```
[2,2]
```

---

# 💻 代码实现（dict 版本）

```python
def intersect_min(nums1, nums2):

    mp1 = {}
    for num in nums1:
        mp1[num] = mp1.get(num, 0) + 1

    mp2 = {}
    for num in nums2:
        mp2[num] = mp2.get(num, 0) + 1

    result = []

    for key in set(mp1.keys()) | set(mp2.keys()):
        times = min(mp1.get(key, 0), mp2.get(key, 0))
        result.extend([key] * times)

    return result
```

---

# 🚀 进阶写法（Counter）

```python
from collections import Counter

def intersect_min(nums1, nums2):

    c1 = Counter(nums1)
    c2 = Counter(nums2)

    result_counter = c1 & c2   # 自动取 min

    return list(result_counter.elements())
```

---

# 🧠 扩展问题

## 1️⃣ 如果取最大次数怎么办？

改为：

```
max(mp1.get(k,0), mp2.get(k,0))
```

## 2️⃣ 如果只判断是否存在？

直接用：

```
set(nums1) & set(nums2)
```

## 3️⃣ 如果一个数组极大怎么办？

统计较小数组：

```
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
```

---

# ⏱ 复杂度

时间复杂度：

```
O(n + m)
```

空间复杂度：

```
O(unique_elements)
```

---

# 🎯 本题训练点

- dict 计数
- set 合并 key
- min / max 次数控制
- 两数组优化策略

---

# 最终模式总结

```
两数组问题
→ 是否需要次数？
    是 → dict
    否 → set
```

```
