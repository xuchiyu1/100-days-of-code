# Algorithm Complexity Notes  
# 算法复杂度笔记（中英文对照）

---

## 1️⃣ O(n) – Linear Time  
## 线性复杂度

Definition:

Algorithm scans each element once.

定义：

每个元素最多访问一次。

Example:

- Two Pointer
- Sliding Window

Why?

Pointers move only forward, never backward.

因为：

指针单向移动，总移动次数 ≤ n。

---

## 2️⃣ O(n²) – Quadratic Time  
## 二次复杂度

Definition:

Nested loops or double scanning.

定义：

双层循环或两层线性扫描。

Example:

- 3Sum
- Bubble sort

3Sum explanation:

Outer loop O(n)  
Inner two-pointer scan O(n)

Total: O(n²)

---

## 3️⃣ O(log n) – Logarithmic Time  
## 对数复杂度

Definition:

Each step halves the search space.

定义：

每次把搜索区间减半。

Example:

Binary Search

n → n/2 → n/4 → n/8 ...

If n = 1024:

1024 = 2¹⁰

So maximum 10 steps.

---

## 4️⃣ O(n log n)

Definition:

Combination of sorting + linear scan.

定义：

排序 + 线性扫描。

Example:

- Merge Sort
- 3Sum (sorting + n² part)

---

## 🧠 Key Comparison  
## 复杂度对比

| Complexity | Behavior |
|------------|----------|
| O(n) | Linear growth |
| O(n²) | Quadratic growth |
| O(log n) | Halving search space |
| O(n log n) | Sorting related |

---

## 🎯 Important Insight  
## 关键理解

- Sliding window is O(n) because pointers move only forward.
- Binary search is O(log n) because search space halves.
- 3Sum is O(n²), not O(n³), because inner loop is linear.

---

## 🚀 Mental Model  
## 思维模型

O(n):

“Check one by one”

O(log n):

“Cut the space in half”

O(n²):

“Nested scanning”

---

# End
