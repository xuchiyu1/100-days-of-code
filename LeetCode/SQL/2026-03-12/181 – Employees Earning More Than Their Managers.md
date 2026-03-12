# LeetCode 181 – Employees Earning More Than Their Managers
## 员工工资高于经理（Self Join 自连接）

---

# 🧩 Problem Description | 题目描述

## English

Write a SQL query to find employees who earn more than their managers.

Return the employee's name.

---

## 中文

写一条 SQL 查询语句，找出工资高于其经理的员工。

返回员工的名字。

---

# 📊 Table Structure | 表结构

```
Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
```

说明：

- 每个员工都有一个 id
- managerId 指向其经理的 id
- 经理也在同一张表中

---

# 🧠 核心思路 | Core Idea

这是一个典型的：

```
Self Join（自连接）
```

问题。

原因：

- 员工在 Employee 表
- 经理也在 Employee 表
- 需要同一张表内部比较

---

# 🔁 什么是 Self Join？

Self Join 是：

> 同一张表 JOIN 自己

我们给表两个别名：

- e1 = 员工
- e2 = 经理

---

# 💻 正确 SQL 语句

```sql
SELECT e1.name AS Employee
FROM Employee e1
INNER JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
```

---

# 🔎 逐句解释 | Line-by-line Explanation

---

## ① FROM Employee e1

表示：

- 第一份 Employee 表
- 别名为 e1
- 代表员工

---

## ② INNER JOIN Employee e2

表示：

- 再复制一份 Employee 表
- 别名为 e2
- 代表经理

---

## ③ ON e1.managerId = e2.id

连接条件：

```
员工的 managerId = 经理的 id
```

也就是：

```
员工.managerId → 指向经理.id
```

这一步把员工和对应的经理匹配起来。

---

## ④ WHERE e1.salary > e2.salary

筛选条件：

```
员工工资 > 经理工资
```

只保留符合条件的员工。

---

# 📈 执行逻辑模拟 | Execution Simulation

假设表数据：

| id | name | salary | managerId |
|----|------|--------|----------|
| 1  | A    | 5000   | NULL     |
| 2  | B    | 6000   | 1        |
| 3  | C    | 4000   | 1        |

---

JOIN 后形成：

| e1.name | e1.salary | e2.name | e2.salary |
|----------|-----------|----------|-----------|
| B        | 6000      | A        | 5000      |
| C        | 4000      | A        | 5000      |

---

WHERE 过滤：

- B → 6000 > 5000 ✅
- C → 4000 > 5000 ❌

最终结果：

```
B
```

---

# ❗ 为什么用 INNER JOIN？

因为：

- 只保留有经理的员工
- managerId 为 NULL 的不会出现

INNER JOIN 规则：

```
只有 ON 条件为 TRUE 的行才会保留
```

NULL 比较永远不是 TRUE。

---

# 🧠 面试重点 | Interview Points

1. 这是 Self Join
2. 需要给表取别名
3. ON 条件负责匹配
4. WHERE 条件负责筛选
5. INNER JOIN 不会保留未匹配行

---

# 🔄 扩展问题 | Extensions

## 如果想保留没有经理的员工？

使用：

```
LEFT JOIN
```

---

## 如果想找工资低于经理的员工？

改为：

```
WHERE e1.salary < e2.salary
```

---

## 如果想返回经理名字？

```sql
SELECT e1.name AS Employee,
       e2.name AS Manager
FROM Employee e1
INNER JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
```

---

# ⏱ 复杂度 | Complexity

时间复杂度：

```
O(n)
```

数据库通过索引优化 JOIN。

空间复杂度：

```
由数据库执行计划决定
```

---

# 📌 关键记忆句

```
Self Join = 同一张表复制两份比较
INNER JOIN = 只保留匹配成功的行
ON = 连接条件
WHERE = 过滤条件
```

---

# 🎯 本题训练点

- Self Join 理解
- 表别名使用
- INNER JOIN 逻辑
- ON 与 WHERE 区别
- NULL 不参与匹配

---
