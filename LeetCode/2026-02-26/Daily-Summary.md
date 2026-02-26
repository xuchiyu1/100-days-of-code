# 2026-02-26 Daily Summary  
# 2026-02-26 学习总结

---

## 1️⃣ LeetCode 15 – 3Sum  
## 三数之和

### Core Idea（核心思路）

- Sort the array  
- Fix one number using a loop  
- Use two pointers to find two-sum  
- Skip duplicates carefully  

- 先排序  
- 外层固定一个数  
- 内层用对撞双指针找 two-sum  
- 必须处理去重逻辑  

---

### Key Insight（关键理解）

3Sum reduces to 2Sum after fixing one number.

三数之和本质是：

固定一个数 → 剩下变成两数之和问题。

---

### Time Complexity（时间复杂度）

O(n²)

Reason:

Outer loop runs n times  
Inner two-pointer scan runs at most n times  

外层 n 次  
内层线性扫描 n 次  

---

## 2️⃣ LeetCode 177 – Nth Highest Salary  
## 第 N 高工资

### Core Idea（核心思路）

- Use DISTINCT to remove duplicate salaries  
- Order by Salary DESC  
- Use OFFSET N-1  

- 必须使用 DISTINCT 去重  
- 按工资降序排列  
- 用 OFFSET N-1  

---

### Why DISTINCT?（为什么必须 DISTINCT）

We must rank distinct salary values, not rows.

必须按不同工资排名，而不是按行号。

---

### Correct SQL Structure（标准写法）

```sql
SET N = N - 1;

SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET N;
```

---

## 3️⃣ LeetCode 178 – Rank Scores  
## 分数排名

### Core Idea（核心思路）

Use window function:

使用窗口函数：

```sql
DENSE_RANK() OVER (ORDER BY score DESC)
```

---

### Ranking Function Comparison  
### 排名函数对比

| Function | Behavior | 中文说明 |
|----------|----------|----------|
| ROW_NUMBER() | Always increases | 每行递增 |
| RANK() | Skips numbers after ties | 会跳号 |
| DENSE_RANK() | No gaps | 不跳号 |

178 requires DENSE_RANK.

178 题必须使用 DENSE_RANK。

---

### Two ORDER BY Explanation  
### 两个 ORDER BY 的区别

```sql
DENSE_RANK() OVER (ORDER BY score DESC)
...
ORDER BY score DESC;
```

- ORDER BY inside OVER → defines ranking logic  
- Final ORDER BY → defines output display order  

- OVER 内 ORDER BY 决定排名规则  
- 最后 ORDER BY 决定显示顺序  

---

## 4️⃣ Binary Search Complexity  
## 二分查找复杂度理解

### Why O(log n)?  
### 为什么是 O(log n)？

Each step halves the search space:

每一步都砍掉一半区间：

n → n/2 → n/4 → n/8 → ...

If n = 1024:

1024 = 2¹⁰  
So maximum 10 comparisons.

如果 n = 1024：

最多比较 10 次。

---

## Patterns Reinforced Today  
## 今天强化的算法模式

- Two Pointer (Opposite Ends)  
- 双指针对撞  
- Deduplication Logic  
- 去重逻辑  
- SQL Ranking Functions  
- SQL 排名函数  
- DISTINCT vs Row Counting  
- DISTINCT 与行数区别  
- Logarithmic Complexity  
- 对数复杂度理解  

---

## Reflection  
## 反思

Today focused on understanding structure and complexity,  
not just writing working code.

今天重点是理解算法结构和复杂度来源，  
而不是单纯写出能运行的代码。

Key improvement:

- Understanding why 3Sum is O(n²)  
- Understanding why Binary Search is O(log n)  
- Mastering SQL ranking logic  

重要提升：

- 理解 3Sum 的 O(n²) 来源  
- 理解 二分查找的 O(log n) 本质  
- 掌握 SQL 排名函数逻辑  

---

# End  
# 结束
