# LeetCode 383 — Ransom Note  
# 勒索信（Ransom Note）

---

## 🧠 Problem Description | 题目描述

**English:**  
Given two strings `ransomNote` and `magazine`, return `True` if `ransomNote` can be constructed using the letters from `magazine`. Each letter in `magazine` can only be used once.

**中文：**  
给定两个字符串 `ransomNote` 和 `magazine`，判断是否可以用 `magazine` 里的字母拼出 `ransomNote`。`magazine` 中的每个字母只能使用一次。

---

## ✅ Core Idea | 核心思路

把 `magazine` 看成“库存（Supply）”，把 `ransomNote` 看成“需求（Demand）”。先统计库存，再逐个消耗需求；若任一字母被消耗到负数，说明库存不足，直接返回 `False`。

---

## 🚀 Final Code (Array) | 最终代码（数组版，适用于 a–z）

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 26 长度数组表示 a-z 的库存
        arr = [0] * 26

        # 统计 magazine（补货）
        for ch in magazine:
            arr[ord(ch) - ord('a')] += 1

        # 消耗 ransomNote（需求）
        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            arr[idx] -= 1
            # 一旦为负，库存不足
            if arr[idx] < 0:
                return False

        return True
```

---

## 🔁 Alternative (HashMap) | 备选（哈希表，支持任意字符集）

```python
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        bucket = defaultdict(int)
        for ch in magazine:
            bucket[ch] += 1
        for ch in ransomNote:
            bucket[ch] -= 1
            if bucket[ch] < 0:
                return False
        return True
```

---

## 🔍 Line-by-Line Explanation | 逐行解析

1. `arr = [0] * 26`  
   **EN:** Create buckets for letters a–z.  
   **中:** 用长度 26 的数组表示 a–z 的库存。

2. `for ch in magazine: arr[...] += 1`  
   **EN:** Count each char in `magazine` (supply increase).  
   **中:** 统计 `magazine`，增加库存。

3. `for ch in ransomNote: arr[...] -= 1`  
   **EN:** Consume for each char in `ransomNote` (demand).  
   **中:** 消耗 `ransomNote` 的字母需求。

4. `if arr[idx] < 0: return False`  
   **EN:** If any bucket goes negative → not enough supply → fail.  
   **中:** 若任一字母库存变为负数，说明不足，直接返回 `False`。

5. `return True`  
   **EN:** All demands satisfied.  
   **中:** 所需字母均可满足，返回 `True`。

---

## 🧠 Key Insight | 关键要点

- 不是检查顺序，而是检查**供需数量**。  
- 负数意味着**需要 > 库存**，与字母出现顺序无关。  
- 这是一个“库存管理”模型（Supply / Demand）。

---

## ⏱ Complexity | 复杂度

- 时间复杂度：`O(n + m)`，`n = len(ransomNote)`，`m = len(magazine)`。  
- 空间复杂度：数组版 `O(1)`（固定 26），哈希表版 `O(k)`（字符种类 k）。

---

## 🔁 Compare with 242 Valid Anagram | 与 242（异位词）对比

- **242 (Valid Anagram)：** 同时对两个字符串做 +1 / -1，最后检查每个桶是否都为 0（完全平衡）。  
- **383 (Ransom Note)：** 先统计 `magazine`（全部 +1），再逐个对 `ransomNote` -1，过程中不能出现负数（供给足够）。  
- 本质差别：242 要**完全相等**（Supply - Demand == 0）；383 要**充足**（Supply - Demand >= 0）。

---

## ✏️ Edge Cases | 边界情况

- `ransomNote` 为空 → 返回 `True`（不需要任何字母）。  
- `magazine` 为空且 `ransomNote` 非空 → 返回 `False`。  
- 非小写字母输入 → 使用哈希表版本以支持任意字符集。

---

## 🧩 Pattern Template | 模式模板（可复用）

**Array（固定字符集）**

```python
bucket = [0] * K   # K = 字符范围大小
for ch in supply_string:
    bucket[mapping(ch)] += 1
for ch in demand_string:
    bucket[mapping(ch)] -= 1
    if bucket[mapping(ch)] < 0:
        return False
return True
```

**HashMap（通用）**

```python
from collections import defaultdict
bucket = defaultdict(int)
for ch in supply:
    bucket[ch] += 1
for ch in demand:
    bucket[ch] -= 1
    if bucket[ch] < 0:
        return False
return True
```

---

## ✅ Final Summary | 最终总结

- 383 是典型的频率统计（频率桶 + 资源模型）。  
- 先补货（统计 magazine），再消耗（ransomNote），出现负数则失败。  
- 若字符范围固定优先用数组实现（更快更省空间）；若字符集任意则用哈希表。
