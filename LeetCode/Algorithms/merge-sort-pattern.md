# Merge Sort Pattern

## 中文：归并排序模板  
## English: Merge Sort Pattern

---

## 1. 模式本质 / Pattern Essence

中文  

```text
分治 + 双指针
```

English  

```text
Divide & Conquer + Two pointers
```

---

## 2. 适用场景 / When to Use

- 排序
- 合并两个有序数组
- 分治问题

---

## 3. 核心模板 / Core Template

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)
```

---

## 4. merge 模板 / Merge Template

```python
def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i == len(left):
            res.append(right[j])
            j += 1
        elif j == len(right):
            res.append(left[i])
            i += 1
        elif left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res
```

---

## 5. merge 核心逻辑 / Merge Logic

中文  

```text
1. 比较当前元素
2. 小的放入结果
3. 对应指针移动
4. 一边用完 -> 直接复制另一边
```

English  

```text
1. Compare current elements
2. Append smaller one
3. Move pointer
4. If one side is done, copy the rest
```

---

## 6. 关键理解 / Key Understanding

### p1 / p2

```text
指针，不是比较次数
Pointers, not counters
```

---

### OR vs AND

```text
OR: 保证所有元素都处理
AND: 会丢元素
```

---

## 7. 复杂度 / Complexity

```text
Time: O(n log n)
Space: O(n)
```

---

## 8. 常见错误 / Common Mistakes

### ❌ 用 AND

会丢数据

### ❌ 忘记复制剩余部分

导致排序不完整

### ❌ 不用 temp

会覆盖数据

---

## 9. 和其他模式对比 / Compare

| Pattern | Core |
|--------|------|
| Two Pointers | 区间 |
| Sliding Window | 子数组 |
| Monotonic Stack | 最近更大 |
| Merge Sort | 分治 + merge |

---

## 10. 一句话总结 / One-line Summary

中文  

```text
归并排序就是不断拆分数组，然后用双指针把有序数组合并回去
```

English  

```text
Merge sort splits arrays and merges them back using two pointers
```
