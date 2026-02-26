# SQL Ranking & Nth Highest Salary Guide  
# SQL 排名函数与第 N 高工资复习总结（双语版）

---

# Part 1️⃣ – 177. Nth Highest Salary  
# 第一部分：第 N 高工资

---

## 🧩 Problem Description (English)

Given an Employee table, return the Nth highest salary.  
If it does not exist, return NULL.

---

## 🧩 题目描述（中文）

给定 Employee 表，返回第 N 高工资。  
如果不存在，返回 NULL。

---

## 🎯 Key Concept  
## 核心概念

We must count **distinct salaries**, not rows.  
必须按“不同的工资”计算排名，而不是按行号。

---

## ❗ Why DISTINCT Is Required  
## 为什么必须使用 DISTINCT

Example:

| Salary |
|--------|
| 100    |
| 100    |
| 90     |

Second highest salary should be 90.  
Without DISTINCT, OFFSET would skip rows incorrectly.

如果不加 DISTINCT，重复工资会影响 OFFSET 计算。

---

## ✅ Recommended Solution (MySQL – LeetCode Safe Version)

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;

  RETURN (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET N
  );
END
```

---

## 🧠 Why `SET N = N - 1`?

MySQL does not always allow arithmetic inside LIMIT.

```sql
LIMIT N - 1, 1   ❌ sometimes fails in functions
```

So we compute first:

```sql
SET N = N - 1;
```

Then use:

```sql
LIMIT 1 OFFSET N
```

---

## 📌 Edge Case

If N is greater than the number of distinct salaries:

The subquery returns empty → function returns NULL.

如果 N 超过不同工资数量，自动返回 NULL。

---

# Part 2️⃣ – 178. Rank Scores  
# 第二部分：排名函数

---

## 🧩 Problem Description (English)

Rank scores in descending order.  
Equal scores share the same rank.  
Ranking should not skip numbers.

---

## 🧩 题目描述（中文）

对分数降序排名。  
相同分数排名相同。  
排名不跳号。

---

## ✅ Correct Solution

```sql
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;
```

---

# 🧠 Three Ranking Functions Explained  
# 三种排名函数对比

Example data:

| Score |
|-------|
| 100   |
| 100   |
| 90    |

---

## 1️⃣ ROW_NUMBER()

```sql
ROW_NUMBER() OVER (ORDER BY score DESC)
```

Result:

| Score | Row_Number |
|-------|------------|
| 100   | 1 |
| 100   | 2 |
| 90    | 3 |

❌ Different ranks for equal values.

---

## 2️⃣ RANK()

```sql
RANK() OVER (ORDER BY score DESC)
```

Result:

| Score | Rank |
|-------|------|
| 100   | 1 |
| 100   | 1 |
| 90    | 3 |

⚠ Skips rank 2.

---

## 3️⃣ DENSE_RANK()

```sql
DENSE_RANK() OVER (ORDER BY score DESC)
```

Result:

| Score | Rank |
|-------|------|
| 100   | 1 |
| 100   | 1 |
| 90    | 2 |

✅ No skipped numbers.  
This is what problem 178 requires.

---

# 🔎 Why Two ORDER BY Clauses?  
# 为什么有两个 ORDER BY？

```sql
DENSE_RANK() OVER (ORDER BY score DESC)
...
ORDER BY score DESC;
```

| Position | Purpose |
|----------|----------|
| Inside OVER | Determines ranking logic |
| Final ORDER BY | Controls output display order |

内部 ORDER BY 决定排名规则  
外部 ORDER BY 决定显示顺序

If you remove the final ORDER BY:
Ranking stays correct, but output order may change.

去掉最后的 ORDER BY，排名不变，但显示顺序可能不同。

---

# 🔥 Alternative Solution (Without Window Function)

Older MySQL method:

```sql
SELECT 
  s1.Score,
  (
    SELECT COUNT(DISTINCT s2.Score)
    FROM Scores s2
    WHERE s2.Score > s1.Score
  ) + 1 AS rank
FROM Scores s1
ORDER BY s1.Score DESC;
```

Logic:
Count how many distinct scores are greater, then +1.

逻辑：统计有多少个不同分数比当前大，然后加 1。

---

# 📊 Summary Table  
# 总结对比表

| Problem | Core Concept |
|----------|--------------|
| 177 | DISTINCT + ORDER BY + OFFSET |
| 178 | DENSE_RANK() |
| Ranking difference | ROW_NUMBER vs RANK vs DENSE_RANK |

---

# 🧠 Key Takeaways  
# 核心总结

1. Use DISTINCT when ranking unique salary levels.  
   计算工资排名必须去重。

2. DENSE_RANK does not skip numbers.  
   DENSE_RANK 不跳号。

3. RANK skips numbers when ties exist.  
   RANK 会跳号。

4. ROW_NUMBER always increments.  
   ROW_NUMBER 永远递增。

5. ORDER BY inside OVER defines ranking logic.  
   OVER 内的 ORDER BY 决定排名规则。

6. Final ORDER BY controls output display.  
   最后的 ORDER BY 控制显示顺序。

---

# 🎯 Interview Insight  
# 面试核心知识点

If interviewer asks:

“What is the difference between RANK and DENSE_RANK?”

Answer:

RANK skips numbers after ties,  
DENSE_RANK does not.

如果面试问区别：

RANK 会跳号  
DENSE_RANK 不跳号

---

# End
