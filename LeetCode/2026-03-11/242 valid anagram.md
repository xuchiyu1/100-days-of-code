# LeetCode 242 - Valid Anagram  
# 有效的字母异位词

---

## 🧠 Problem Description | 题目描述

**English:**  
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, otherwise return `False`.

An anagram means:
- Same characters
- Same frequency
- Order does NOT matter

**中文：**  
给定两个字符串 `s` 和 `t`，判断 `t` 是否是 `s` 的字母异位词。

字母异位词的定义：
- 字母相同
- 每个字母出现次数相同
- 顺序可以不同

---

# 🚀 Final Code | 最终代码

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 1️⃣ 长度不同直接返回 False
        if len(s) != len(t):
            return False
        
        # 2️⃣ 创建长度为 26 的计数数组
        arr = [0] * 26
        
        # 3️⃣ 同时统计 s 和 t
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
        
        # 4️⃣ 检查是否全部为 0
        for check in arr:
            if check != 0:
                return False
        
        return True
```

---

# 🔍 Line-by-Line Explanation | 逐行解析

---

## ① Length Check | 长度检查

```python
if len(s) != len(t):
    return False
```

**English:**  
If lengths differ, they cannot be anagrams.

**中文：**  
如果长度不同，不可能是异位词。

---

## ② Create Frequency Array | 创建频率数组

```python
arr = [0] * 26
```

**English:**  
Create an array of size 26 to store frequency of letters a–z.

**中文：**  
创建长度为 26 的数组，统计 a–z 的出现次数。

Mapping:

| Letter | Index |
|--------|--------|
| a | 0 |
| b | 1 |
| c | 2 |
| ... | ... |
| z | 25 |

---

## ③ Character → Index Mapping | 字符转索引

```python
ord(char) - ord('a')
```

**English Explanation:**  
`ord()` converts a character to ASCII number.

Example:
```
ord('a') = 97
ord('b') = 98
```

So:
```
ord('b') - ord('a') = 1
```

**中文解释：**  
`ord()` 把字符转换为 ASCII 数值。

例如：
```
ord('a') = 97
ord('b') = 98
```

因此：
```
ord('b') - ord('a') = 1
```

这样就能把：
```
'a' → 0
'b' → 1
...
```

---

## ④ Core Counting Logic | 核心统计逻辑

```python
for i in range(len(s)):
    arr[ord(s[i]) - ord('a')] += 1
    arr[ord(t[i]) - ord('a')] -= 1
```

**English:**  
- Add frequency for `s`
- Subtract frequency for `t`

If they are anagrams:
All increments cancel out decrements.

**中文：**  
- 对 `s` 出现的字母 +1
- 对 `t` 出现的字母 -1

如果是异位词：
所有加法都会被减法抵消。

---

## ⑤ Final Verification | 最终验证

```python
for check in arr:
    if check != 0:
        return False
```

**English:**  
Check every element in the array.  
If any value is not zero → mismatch.

Important:
This does NOT check `sum(arr) == 0`.

It checks:
```
All positions must equal 0
```

**中文：**  
逐个检查数组元素。  
只要有一个不为 0 → 直接 False。

重要：
它不是检查总和是否为 0。

而是检查：
```
每一个位置都必须是 0
```

数学表达：
```
∀ i ∈ [0,25], arr[i] == 0
```

---

# ❓ Your Questions Explained | 你问过的问题整理

---

## Q1: 会不会乱序导致出错？  
### Will order affect result?

**English:**  
No. Because each character maps to a fixed index.

Even if order changes:
Same letters → Same index → Correct cancellation.

**中文：**  
不会。

因为每个字母都有固定索引。

顺序改变不会影响统计结果。

---

## Q2: 如果总和为 0 但某些位置不为 0 怎么办？  
### What if sum(arr) == 0 but elements differ?

Example:
```
[1, -1, 0, 0, ...]
```

Sum = 0  
But algorithm checks each element.

So:
```
1 != 0 → return False
```

**中文：**  
算法不是检查总和。

而是逐个检查。

只要有一个位置不为 0 就直接 False。

---

## Q3: `for check in arr` 没有公式是什么意思？

**English:**  
`check` is just a variable name.

Equivalent to:
```
for value in arr:
```

It simply retrieves each element one by one.

**中文：**  
`check` 只是变量名。

等价于：
```
for value in arr:
```

它只是把数组里的元素一个个取出来。

---

# ⏱ Complexity | 时间复杂度

Time Complexity:
```
O(n)
```

Space Complexity:
```
O(1)
```

Because array size is fixed (26).

---

# 🧩 Pattern Summary | 模式总结

This is a:

## Frequency Array Pattern  
## 固定范围频率数组模式

Use when:
- Only lowercase letters
- Fixed character range
- Need O(1) space

模板：

```python
arr = [0] * K

for char in string:
    arr[mapping(char)] += 1
```

---

# 🏁 Core Insight | 核心思想

Valid Anagram is:

```
Frequency counting + cancellation + all-zero verification
```

中文：

```
字符频率统计 + 抵消思想 + 全零验证
```

---

# 🔥 Final Mental Model | 最终心智模型

This problem is NOT about string order.

It is about:

Transforming characters into indexed buckets  
and comparing frequency balance.

中文：

这题不是比较字符串顺序。

而是：

把字符映射到固定桶中  
然后比较频率是否完全抵消。
