# Two Pointer – Opposite Ends Template  
# 双指针对撞模板（中英文对照）

---

## 🧠 Pattern Overview  
## 模式概述

This pattern is used when:

- The array is sorted (or can be sorted)
- We need to find pairs or combinations
- We move pointers inward from both ends

适用场景：

- 数组已排序（或可以排序）
- 查找两数之和 / 三数之和
- 区间缩小问题

---

## 🎯 Core Idea  
## 核心思想

We use two pointers:

- `left` starting from the beginning
- `right` starting from the end

Based on the sum comparison, we move one pointer.

使用两个指针：

- left 从左开始
- right 从右开始

根据大小关系移动指针。

---

## 📌 Basic Template  
## 基础模板

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

---

## 🔍 Why Sorting Is Required  
## 为什么必须排序

Sorting ensures:

- Left pointer moving right increases value
- Right pointer moving left decreases value

排序保证：

- left++ → 数值变大
- right-- → 数值变小

Without sorting, pointer movement logic breaks.

---

## 🧠 Example: 3Sum  
## 示例：三数之和

3Sum structure:

```python
nums.sort()

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            result.append([nums[i], nums[left], nums[right]])

            left += 1
            right -= 1

            # skip duplicates
            while left < right and nums[left] == nums[left-1]:
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1
```

---

## ⏱ Time Complexity  
## 时间复杂度

Outer loop: O(n)  
Inner two-pointer scan: O(n)

Total: O(n²)

原因：

两个指针只会单向移动，不会回退。

---

## 🚀 When To Use  
## 使用时机

Use this pattern when:

- You see sum problems
- Array can be sorted
- Need to reduce dimension

当看到：

- 求和类问题
- 可排序数组
- 降维问题

优先考虑此模式。

---

# End
