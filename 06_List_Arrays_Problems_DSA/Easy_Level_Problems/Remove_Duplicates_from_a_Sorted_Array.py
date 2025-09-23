"""
===========================================================
 Problem: Remove Duplicates from Sorted Array (LeetCode #26)
===========================================================

-----------------------------------------------------------
 Understand the Problem
-----------------------------------------------------------
- Input: A sorted array (non-decreasing order).
- Task: Remove duplicates in-place so that each unique
  element appears only once, preserving order.
- Output:
  - Modify nums in-place.
  - Return the number of unique elements.
- Extra constraint: Do NOT use extra space (in-place).

Example:
nums = [0,0,1,1,1,2,2,3,3,4]
Output → nums = [0,1,2,3,4,_,_,_,_,_]
Return 5 (since there are 5 unique numbers).

Key Constraints:
- nums is sorted.
- Must be in-place (no new array).
- Return length of unique elements.
"""

# =========================================================
# 1. Brute Force Solution (Dictionary)
# =========================================================
"""
Intuition & Approach:
- Use a dictionary to track unique numbers (keys auto-remove duplicates).
- Copy unique keys back to nums.
- Return the number of unique elements.

Time Complexity: O(n + n) → O(n)
Space Complexity: O(k) where k = number of unique elements (worst O(n)).
"""

from typing import List

class SolutionBruteForce:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = dict()
        # Pass 1: collect unique elements
        for i in nums:
            my_dict[i] = 0

        # Pass 2: write back unique keys
        j = 0
        for n in my_dict:
            nums[j] = n
            j += 1
        return j


"""
Dry Run (nums = [0,0,1,1,1,2,2,3,3,4]):
Step 1: my_dict = {0:0, 1:0, 2:0, 3:0, 4:0}
Step 2: Write back:
    nums = [0,1,2,3,4,_,_,_,_,_]
Return 5.

Edge Cases:
- [] → return 0
- [1,2,3] (no duplicates) → return 3
- [1,1,1] (all same) → return 1
"""

# =========================================================
# 2. Optimal Solution (Two Pointers)
# =========================================================
"""
Intuition & Approach:
- Use two pointers (i and j).
- i = index of last unique element.
- j = scanning pointer.
- If nums[j] != nums[i], then nums[j] is a new unique number.
    → Move i forward, place nums[j] at nums[i].
- At the end, unique elements are in nums[:i+1].
- Return i+1 as count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class SolutionOptimal:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


"""
Dry Run (nums = [0,0,1,1,1,2,2,3,3,4]):

i=0, j=1 → nums[1]==nums[0] → skip
i=0, j=2 → nums[2]!=nums[0] → i=1, nums[1]=1
i=1, j=3 → nums[3]==nums[1] → skip
i=1, j=5 → nums[5]!=nums[1] → i=2, nums[2]=2
i=2, j=7 → nums[7]!=nums[2] → i=3, nums[3]=3
i=3, j=9 → nums[9]!=nums[3] → i=4, nums[4]=4

Final: nums = [0,1,2,3,4,_,_,_,_,_], return 5.

Edge Cases:
- [] → return 0
- [1,1,1] → return 1
- [1,2,3] → return 3
"""

# =========================================================
# Demo Run
# =========================================================
if __name__ == "__main__":
    nums1 = [0,0,1,1,1,2,2,3,3,4]
    solver1 = SolutionBruteForce()
    k1 = solver1.removeDuplicates(nums1)
    print("Brute Force:", nums1, "Unique count:", k1)

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    solver2 = SolutionOptimal()
    k2 = solver2.removeDuplicates(nums2)
    print("Optimal:", nums2, "Unique count:", k2)
