# 🔥 Hash / Frequency Counting Pattern 总框架
# 哈希 / 频率统计 模式体系总结

---

# 🧠 1️⃣ 核心思想 Core Idea

所有这类题的本质都是：

```
统计 → 比较
Count → Compare
```

把字符串问题转化成：

```
资源统计模型
Resource Accounting Model
```

---

# 🏗 2️⃣ 抽象模型 Abstract Model

设：

```
Supply  = 资源供给
Demand  = 资源需求
Bucket  = 频率桶 (数组 or 字典)
```

核心公式：

```
Supply - Demand
```

然后根据题目要求判断：

```
== 0
>= 0
排序后相同
频率作为 key
```

---

# 🧩 3️⃣ 四种常见类型

---

## ① 完全平衡型（Exact Match）
### 例题：242 Valid Anagram

判断：

```
∀ i, bucket[i] == 0
```

数学表达：

```
Supply - Demand = 0
```

代码核心：

```python
for i in range(len(s)):
    bucket[s[i]] += 1
    bucket[t[i]] -= 1

for value in bucket:
    if value != 0:
        return False
```

中文理解：

必须完全抵消。

---

## ② 资源校验型（Resource Validation）
### 例题：383 Ransom Note

判断：

```
Supply - Demand >= 0
```

一旦出现：

```
bucket[i] < 0
```

立即返回 False。

代码核心：

```python
for char in magazine:
    bucket[char] += 1

for char in ransomNote:
    bucket[char] -= 1
    if bucket[char] < 0:
        return False
```

中文理解：

库存不能为负。

---

## ③ 分组型（Frequency as Key）
### 例题：49 Group Anagrams

核心思想：

```
把频率数组当作 key
```

示例：

```python
count = [0] * 26
for c in word:
    count[ord(c)-ord('a')] += 1

key = tuple(count)
```

中文理解：

同频率的字符串放到同一组。

---

## ④ Top K / 高频统计型
### 例题：347 Top K Frequent Elements

核心思想：

```
统计频率 → 根据频率排序或桶排序
```

模型：

```
Value → Frequency
Frequency → Bucket
```

---

# 📊 4️⃣ Array vs HashMap

---

## Array 版本（固定字符范围）

优点：
```
O(1) 空间
更快
```

适用：
```
只包含 a-z
只包含 ASCII
固定字符集
```

模板：

```python
bucket = [0] * 26
bucket[ord(char) - ord('a')] += 1
```

---

## HashMap 版本（通用字符）

优点：
```
适用 Unicode
适用任意字符
```

模板：

```python
from collections import defaultdict

bucket = defaultdict(int)

for char in string:
    bucket[char] += 1
```

---

# 🧠 5️⃣ 心智模型升级 Mental Model Upgrade

不要再把它看成“字符串题”。

把它看成：

```
桶管理问题
Inventory Management Problem
```

流程统一：

```
1. 建桶
2. 加库存
3. 减库存
4. 校验库存状态
```

---

# 🧮 6️⃣ 数学表达总结

| 类型 | 数学表达 |
|------|----------|
| 完全匹配 | Supply - Demand = 0 |
| 资源校验 | Supply - Demand >= 0 |
| 分组 | Frequency Vector 相同 |
| Top K | 排序(Frequency) |

---

# 🔥 7️⃣ 高频面试题归类

属于这个 Pattern 的题：

```
242 Valid Anagram
383 Ransom Note
49 Group Anagrams
438 Find All Anagrams
347 Top K Frequent Elements
451 Sort Characters by Frequency
```

---

# 🎯 8️⃣ 终极总结

所有频率题都可以抽象成：

```
频率桶 + 资源模型 + 状态判断
```

英文总结：

```
Frequency Bucket + Resource Model + State Validation
```

---

# 🧩 一句话记忆

```
Count first.
Compare later.
```

中文：

```
先统计。
再判断。
```

---

# 🏁 你当前阶段定位

你已经从：

```
语法理解阶段
```

进入：

```
算法模式抽象阶段
```

下一步建议：

专门建立：

```
Algorithms/
    ├── Hash/
    ├── SlidingWindow/
    ├── TwoPointers/
    ├── Greedy/
```

开始系统化模式归纳。

这才是真正的算法进阶路线。
