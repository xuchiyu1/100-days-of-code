# 哈希表模式总结（Hash Map Pattern）

---

## 🎯 核心问题类型

当题目涉及：

- 两个数组
- 元素是否存在
- 统计出现次数
- 去重
- 交集 / 并集

第一反应：

> 用 set 还是 dict？

---

# 一、是否存在问题

### 关键词

- contains
- duplicate
- exist

### 用什么？

```
set
```

### 模板

```python
s = set(nums)
if target in s:
    ...
```

---

# 二、计数问题

### 关键词

- frequency
- 出现次数
- 统计

### 用什么？

```
dict
```

### 模板

```python
mp = {}
for num in nums:
    mp[num] = mp.get(num, 0) + 1
```

---

# 三、交集问题

## 349（去重）

- 用 set
- 匹配后删除避免重复

```python
mp = set(nums1)

for num in nums2:
    if num in mp:
        result.append(num)
        mp.remove(num)
```

---

## 350（允许重复）

- 用 dict 计数
- 匹配后减 1

```python
if num in mp and mp[num] > 0:
    result.append(num)
    mp[num] -= 1
```

---

# 四、并集问题

## 去重并集

```python
return list(set(nums1) | set(nums2))
```

## 保留最大次数

```python
max(mp1.get(k,0), mp2.get(k,0))
```

## 保留最小次数

```python
min(mp1.get(k,0), mp2.get(k,0))
```

---

# 五、复杂度思维

当看到：

> 两个数组 + 哈希表

要问：

1. 谁更小？
2. 哈希表建在哪个上？
3. 是否需要交换？

```python
if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
```

---

# 🧠 记忆结构

| 类型 | 数据结构 |
|------|----------|
| 是否存在 | set |
| 去重 | set |
| 计数 | dict |
| 可重复交集 | dict |
| 最大/最小次数 | dict |

---

# 总结公式

```
存在 → set
次数 → dict
重复控制 → 减 1
去重控制 → remove
```

```
