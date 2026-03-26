# Heap / Priority Queue / Top K Notes

## 中文标题：堆 / 优先队列 / Top K 模式笔记
## English Title: Heap / Priority Queue / Top K Pattern Notes

---

## 1. Heap 是什么 / What Is a Heap

Heap（堆）是一种特殊的数据结构，最常见的是：

- 最小堆（min heap）
- 最大堆（max heap）

在 Python 里，`heapq` 默认实现的是最小堆。

A heap is a special data structure. The most common types are:

- min heap
- max heap

In Python, `heapq` implements a min heap by default.

---

## 2. Heap 的作用 / What Heap Is Used For

Heap 适合用来做：

- 快速拿到最小值 / 最大值
- 动态维护 Top K
- 合并多个有序结构
- 数据流中的第 K 大 / 第 K 小

Heaps are useful for:

- quickly accessing min/max
- dynamically maintaining Top K
- merging multiple sorted structures
- finding the Kth largest/smallest in a stream

---

## 3. Python Heap 基础 / Python Heap Basics

```python
import heapq
```

常用操作：

```python
heapq.heappush(heap, x)   # 入堆
heapq.heappop(heap)       # 出堆
heap[0]                   # 堆顶
```

Important operations:

```python
heapq.heappush(heap, x)   # push
heapq.heappop(heap)       # pop
heap[0]                   # top element
```

---

## 4. Heap 的核心性质 / Core Property of Heap

最小堆：

- 堆顶永远是最小值

最大堆：

- 堆顶永远是最大值

Min heap:

- the root is always the smallest element

Max heap:

- the root is always the largest element

---

## 5. Top K 模式 / Top K Pattern

Top K 问题的核心想法：

- 只保留最重要的 `k` 个元素
- 当堆大小超过 `k` 时，删除不重要的那个
- 最后堆里剩下的就是答案候选

Core idea of Top K problems:

- keep only the `k` most important elements
- remove the least important one when heap size exceeds `k`
- the remaining elements are the answer candidates

---

## 6. 通用模板 / General Template

### 6.1 第 K 大 / 第 K 小

```python
import heapq

def kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
```

适用场景：

- 215. Kth Largest Element in an Array
- 数据流中动态找第 K 大

Use cases:

- 215. Kth Largest Element in an Array
- Kth largest in a stream

---

### 6.2 前 K 个高频元素

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])

    return res[::-1]
```

适用场景：

- 347. Top K Frequent Elements
- 692. Top K Frequent Words

Use cases:

- 347. Top K Frequent Elements
- 692. Top K Frequent Words

---

## 7. 为什么堆大小是 k / Why Heap Size Is k

中文  
Top K 问题只关心前 k 个，所以堆里只保留 k 个候选。

English  
Top K problems only care about the top k candidates, so the heap keeps only k elements.

---

## 8. 为什么返回 heap[0] / Why Return heap[0]

中文  
如果我们用最小堆维护最大的 k 个元素，那么堆顶就是这 k 个元素中最小的那个，也就是第 k 大。

English  
If we use a min heap to maintain the largest k elements, the heap top is the smallest among them, which is the kth largest.

---

## 9. 经典题型 / Classic Problems

### Top K 类
- 215. Kth Largest Element in an Array
- 347. Top K Frequent Elements
- 703. Kth Largest Element in a Stream
- 692. Top K Frequent Words

### 合并 / 选择类
- 23. Merge k Sorted Lists
- 373. Find K Pairs with Smallest Sums
- 378. Kth Smallest Element in a Sorted Matrix
- 313. Super Ugly Number

---

## 10. 复杂度 / Complexity

如果维护大小为 k 的堆：

- 入堆：`O(log k)`
- 出堆：`O(log k)`
- 总体：`O(n log k)` 或 `O(m log k)`

If maintaining a heap of size `k`:

- push: `O(log k)`
- pop: `O(log k)`
- total: `O(n log k)` or `O(m log k)`

---

## 11. 常见错误 / Common Mistakes

### 错误 1：把最大堆和最小堆搞混

Top K 问题通常使用最小堆来保留最大 `k` 个元素。

### 错误 2：忘记限制堆大小

如果不控制大小为 `k`，就不是 Top K 了。

### 错误 3：比较对象搞错

347 比较的是“频率”，不是数字大小。

215 比较的是“数值大小”。

---

## 12. 学习顺序 / Learning Order

推荐顺序：

1. 先理解 heap 是什么
2. 学会 `heapq.heappush` / `heapq.heappop`
3. 做 215
4. 做 347
5. 做 703

Recommended order:

1. Understand what a heap is
2. Learn `heappush` / `heappop`
3. Solve 215
4. Solve 347
5. Solve 703

---

## 13. 一句话总结 / One-line Summary

中文  
Heap 是动态维护最值和 Top K 的利器。

English  
Heap is a powerful tool for maintaining extremes and Top K elements dynamically.
