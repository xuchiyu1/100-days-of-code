/* =========================================================
   LeetCode 176 - Second Highest Salary
   Date: 2026-02-14
   Difficulty: Medium
   Type: Sorting + Subquery

   Concepts:
   - DISTINCT
   - ORDER BY DESC
   - LIMIT
   - OFFSET
   - Subquery

   Logic:
   1. Remove duplicate salaries.
   2. Sort descending.
   3. Skip highest (OFFSET 1).
   4. Return second highest.
   ========================================================= */

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
