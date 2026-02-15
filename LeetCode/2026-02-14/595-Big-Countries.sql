/* =========================================================
   LeetCode 595 - Big Countries
   Date: 2026-02-14
   Difficulty: Easy
   Type: SQL Filtering

   Concepts:
   - SELECT
   - WHERE
   - OR
   - >=

   Logic:
   1. Select required columns.
   2. Filter rows where area >= 3000000
      OR population >= 25000000.
   ========================================================= */

SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
