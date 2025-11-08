"""
-------------------------------------------------------------
DSA Problem: Sort Colors (LeetCode #75)
-------------------------------------------------------------
 Problem Statement:
Given an array 'nums' containing n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order: red (0), white (1), blue (2).

Example:
---------
Input  : nums = [2,0,2,1,1,0]
Output : [0,0,1,1,2,2]

Constraints:
------------
- You must solve it in-place.
- You cannot use library sort functions.
"""

# ==============================================================
# OPTIMAL SOLUTION — DUTCH NATIONAL FLAG / ONE-PASS
# ==============================================================
"""
 Technique Used:
-------------------
Dutch National Flag Algorithm (Three-Pointer Partitioning)

 Idea:
- Maintain three regions using pointers:
  1. 0 ... low-1     → all 0s (red)
  2. low ... mid-1   → all 1s (white)
  3. mid ... high    → unknown/unprocessed
  4. high+1 ... end  → all 2s (blue)

- Iterate using 'mid':
    * If nums[mid] == 0 → swap with nums[low], increment low & mid
    * If nums[mid] == 1 → mid++, it's already in correct region
    * If nums[mid] == 2 → swap with nums[high], decrement high (mid stays)

🛠 Behind the Scenes:
---------------------
- Dynamically partitions the array so that every element goes to its
  correct region in a single pass.
- Only one traversal; each element is handled at most once.
- No extra space needed; in-place swaps.
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0                # boundary for 0s (red)
        mid = 0                # current element to check
        high = len(nums) - 1   # boundary for 2s (blue)

        while mid <= high:
            if nums[mid] == 0:
                # swap current 0 into red region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in correct region (white)
                mid += 1
            else:
                # swap current 2 into blue region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

"""
 Step-by-Step Explanation:
-----------------------------
nums = [2,0,2,1,1,0]

1. Initial pointers: low=0, mid=0, high=5
2. nums[mid]=2 → swap nums[mid] & nums[high] → high=4 → nums=[0,0,2,1,1,2]
3. nums[mid]=0 → swap nums[mid] & nums[low] → low=1, mid=1 → nums=[0,0,2,1,1,2]
4. nums[mid]=2 → swap nums[mid] & nums[high] → high=3 → nums=[0,0,1,1,2,2]
5. nums[mid]=1 → mid++ → mid=3
6. nums[mid]=1 → mid++ → mid=4 → mid > high → end

Result: [0,0,1,1,2,2]
"""

# ==============================================================
# Time and Space Complexity
# ==============================================================
"""
 Time Complexity: O(n)
- Single pass through the array
- Each element is examined and swapped at most once

 Space Complexity: O(1)
- Only three pointers (low, mid, high) are used
- In-place, no extra data structures needed
"""

# ==============================================================
# Comparison to Other Approaches
# ==============================================================
"""
1. Brute Force / Built-in Sort:
   - nums.sort() → O(n log n), conceptually easy but not linear
2. Counting Sort:
   - Count 0s, 1s, 2s → overwrite array → O(n) time, O(1) space
   - Two passes instead of one
3. Dutch National Flag (Optimal):
   - One-pass, constant space
   - Elegant pointer-based partitioning
   - Interview-ready solution
"""
