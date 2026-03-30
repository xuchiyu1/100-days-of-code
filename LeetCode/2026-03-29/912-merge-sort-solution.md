# 912. Sort an Array

## 中文：排序数组  
## English: Sort an Array

---

## 1. 题目 / Problem

中文  
给定一个整数数组 `nums`，请将其按升序排列。

English  
Given an integer array `nums`, sort the array in ascending order.

---

## 2. 核心思路 / Core Idea

中文  
使用归并排序（Merge Sort）：

1. 拆分数组
2. 分别排序左右两边
3. 合并两个有序数组

English  
Use Merge Sort:

1. Divide the array
2. Recursively sort left and right parts
3. Merge two sorted arrays

---

## 3. 分治思想 / Divide and Conquer

中文  
归并排序属于分治算法：

```text
分（Divide） -> 排（Conquer） -> 合（Merge）
```

English  
Merge sort is a divide-and-conquer algorithm:

```text
Divide -> Conquer -> Merge
```

---

## 4. 为什么 n <= 1 直接返回 / Base Case

中文  
长度为 0 或 1 的数组天然有序。

English  
An array of size 0 or 1 is already sorted.

---

## 5. merge 的本质 / Essence of Merge

中文  
merge 的核心是：

```text
把两个有序数组合并成一个有序数组
```

English  
Merge means:

```text
Combine two sorted arrays into one sorted array
```

---

## 6. merge 详细流程 / Merge Step-by-step

示例：

```text
左: [2,5]
右: [1,3]
```

Step 1  
比较 2 和 1 → 放 1  

```text
[1]
```

Step 2  
比较 2 和 3 → 放 2  

```text
[1,2]
```

Step 3  
比较 5 和 3 → 放 3  

```text
[1,2,3]
```

Step 4  
右边用完 → 放剩下的 5  

```text
[1,2,3,5]
```

---

## 7. 指针含义 / Pointer Meaning

中文  

```text
p1 = 左数组指针
p2 = 右数组指针
k  = 写入位置
```

English  

```text
p1 = pointer in left array
p2 = pointer in right array
k  = write index
```

---

## 8. 为什么用 OR / Why OR

中文  

```text
while p1 < n1 OR p2 < n2
```

因为：

```text
只要有一边没处理完，就必须继续
```

English  

We use OR because:

```text
we must process all elements from both arrays
```

---

## 9. 时间复杂度 / Time Complexity

```text
O(n log n)
```

中文  
log n 层，每层处理 n 个元素

English  
log n levels, each level processes n elements

---

## 10. 空间复杂度 / Space Complexity

```text
O(n)
```

因为需要辅助数组

---

## 11. 代码 / Code

```python
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort(nums, 0, len(nums) - 1)
        return nums

    def sort(self, nums, lo, hi):
        if lo >= hi:
            return

        mid = (lo + hi) // 2

        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)

        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        temp = nums[lo:hi+1]

        i = 0
        j = mid - lo + 1

        for k in range(lo, hi + 1):
            if i > mid - lo:
                nums[k] = temp[j]
                j += 1
            elif j > hi - lo:
                nums[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
```

---

## 12. 一句话总结 / One-line Summary

中文  
归并排序 = 分治 + 双指针 merge

English  
Merge Sort = Divide & Conquer + Two-pointer merge
