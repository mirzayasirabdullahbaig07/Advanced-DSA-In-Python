"""
-------------------------------------------------------------
DSA Problem: Maximum Subarray (LeetCode #53)
-------------------------------------------------------------
 Problem Statement:
Given an integer array 'nums', find the contiguous subarray 
with the largest sum and return its sum.

Example:
---------
Input  : nums = [-2,1,-3,4,-1,2,1,-5,4]
Output : 6
Explanation: Subarray [4,-1,2,1] has the largest sum 6.

Constraints:
------------
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# ==============================================================
# BRUTE FORCE — TRIPLE LOOP
# ==============================================================
"""
 Technique Used:
-------------------
Exhaustive search:
- Check every possible subarray and compute its sum.
- Keep track of the maximum sum found.

 Behind the Scenes:
---------------------
- Nested loops:
    * Outer loop → start index i
    * Middle loop → end index j
    * Inner loop → sum elements from i to j
- Impractical for large arrays (O(n³)), but good for understanding.
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = float("-inf")        # global maximum sum
        n = len(nums)
        for i in range(n):          # start index
            for j in range(i, n):   # end index
                cur_sum = 0
                for k in range(i, j+1):  # sum subarray i..j
                    cur_sum += nums[k]
                maxi = max(maxi, cur_sum)
        return maxi

# Complexity:
# Time: O(n³) → three nested loops
# Space: O(1) → only scalars used

# ==============================================================
# BETTER BRUTE FORCE — DOUBLE LOOP
# ==============================================================
"""
 Technique Used:
-------------------
Cumulative sum reuse:
- Keep a running sum while expanding the end index j.
- Avoid recomputing sum from scratch each time.

 Behind the Scenes:
---------------------
- Outer loop → start index i
- Inner loop → extend to end index j
- Add nums[j] to running sum s
- Update maximum sum
- Still O(n²), but faster than triple loop
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = float("-inf")
        n = len(nums)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]           # extend current subarray
                maxi = max(maxi, s)    # update maximum
        return maxi

# Complexity:
# Time: O(n²) → two nested loops
# Space: O(1)

# ==============================================================
# OPTIMAL — KADANE'S ALGORITHM
# ==============================================================
"""
 Technique Used:
-------------------
Dynamic programming / prefix sum:
- Maintain the maximum subarray sum ending at current index.
- If current running sum < 0, reset it (drop negative prefix).

 Behind the Scenes:
---------------------
- curSum → maximum sum of subarray ending at current index
- maxi → global maximum
- Traverse array once:
    * curSum += num
    * maxi = max(maxi, curSum)
    * if curSum < 0 → reset curSum = 0
- Optimal single-pass solution
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = float("-inf")  # global max
        curSum = 0            # current subarray sum

        for num in nums:
            curSum += num         # extend current subarray
            maxi = max(maxi, curSum)

            if curSum < 0:        # negative drag – drop prefix
                curSum = 0

        return maxi

# Complexity:
# Time: O(n) → single pass
# Space: O(1) → only two scalar variables used

# ==============================================================
# Summary of Techniques
# ==============================================================
"""
| Approach          | Time   | Space | When to Use                           |
|------------------|--------|-------|--------------------------------------|
| Triple Loop       | O(n³)  | O(1)  | Teaching brute force                  |
| Double Loop       | O(n²)  | O(1)  | Small n (≤ 1000)                     |
| Kadane's Algorithm| O(n)   | O(1)  | Real input, interviews, optimal       |
"""

