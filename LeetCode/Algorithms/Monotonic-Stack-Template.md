# Monotonic Stack Template  
# 单调栈算法模板

---

## 🧠 What is a Monotonic Stack?  
## 什么是单调栈？

A stack that maintains elements in either increasing or decreasing order.

一种保持递增或递减顺序的栈结构。

---

## 🎯 When to Use  
## 使用场景

- Next Greater Element
- Next Smaller Element
- Daily Temperatures
- Largest Rectangle in Histogram

- 下一个更大元素
- 下一个更小元素
- 每日温度
- 柱状图最大矩形

---

## 📌 Decreasing Stack Template (Next Greater Element)  
## 单调递减栈（找更大元素）

```python
stack = []
for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        # process idx
    stack.append(i)
```

---

## 📌 Increasing Stack Template (Next Smaller Element)  
## 单调递增栈（找更小元素）

```python
stack = []
for i in range(len(nums)):
    while stack and nums[i] < nums[stack[-1]]:
        idx = stack.pop()
        # process idx
    stack.append(i)
```

---

## 🔥 Key Properties  
## 关键性质

- Each index enters stack once
- Each index leaves stack once
- Total operations ≤ 2n
- Time complexity O(n)

- 每个元素最多入栈一次
- 最多出栈一次
- 总操作不超过 2n
- 时间复杂度 O(n)

---

## 🧠 Why O(n)?  
## 为什么是 O(n)？

Although it looks like nested loops,  
each element is popped only once.

虽然看似嵌套循环，但每个元素只会被弹出一次。

---

## 🚀 Mental Model  
## 心智模型

The stack stores "unresolved indices".

栈存的是“尚未找到答案的索引”。

When a larger element appears,  
we resolve previous smaller elements.

遇到更大的值时，解决之前较小的元素。

---

# End
