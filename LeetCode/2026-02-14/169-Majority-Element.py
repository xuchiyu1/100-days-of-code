# =========================================================
# LeetCode 169 - Majority Element
# Date: 2026-02-14
# Difficulty: Easy
# Type: HashMap / Frequency Counting
#
# Concepts:
# - Dictionary
# - for loop
# - len()
# - integer division //
#
# Logic:
# 1. Count frequency of each number.
# 2. Return number with count > n//2.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# =========================================================

class Solution:
    def majorityElement(self, nums):
        
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        threshold = len(nums) // 2

        for key in count:
            if count[key] > threshold:
                return key
