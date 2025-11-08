"""
-------------------------------------------------------------
DSA Problem: Maximum Consecutive Ones (LeetCode #485)
-------------------------------------------------------------
 Problem Statement:
Given a binary array 'nums' (containing only 0s and 1s),
return the maximum number of consecutive 1's in the array.

Example:
---------
Input  : nums = [1, 1, 0, 1, 1, 1]
Output : 3

Explanation:
------------
There are two streaks of consecutive 1s:
- First streak = [1, 1] → length 2
- Second streak = [1, 1, 1] → length 3
Maximum consecutive 1s = 3
"""

# ==============================================================
# OPTIMAL SOLUTION — SINGLE PASS COUNTING
# ==============================================================
"""
 Technique Used:
-------------------
Single Pass Iteration with a Running Counter

 Idea:
- Traverse the array once, maintaining two variables:
    1. cnt  → Current streak of consecutive 1s
    2. maxi → Maximum streak found so far
- If current element is 1 → increment cnt
- If current element is 0 → reset cnt and update maxi
- At the end, compare cnt with maxi in case the array ends with 1s

 Behind the Scenes:
---------------------
This is a simple linear scan:
- No nested loops → O(n) time
- No extra data structures → O(1) space
- The technique leverages a running counter to capture consecutive sequences efficiently
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cnt = 0   # Counter for current consecutive 1s
        maxi = 0  # Maximum consecutive 1s found so far

        # Step 1: Traverse the array
        for num in nums:
            if num == 1:
                # Increment counter when 1 is found
                cnt += 1
            else:
                # Update maximum and reset counter on 0
                maxi = max(maxi, cnt)
                cnt = 0

        # Step 2: Final comparison (in case array ends with 1s)
        return max(maxi, cnt)


"""
 Step-by-Step Explanation:
-----------------------------
1. Initialize cnt = 0, maxi = 0
2. Loop through each element in nums:
   - If nums[i] == 1 → cnt += 1
   - Else (nums[i] == 0):
       → maxi = max(maxi, cnt)
       → cnt = 0
3. After loop, return max(maxi, cnt)
   - This ensures the last streak of 1s is considered

Dry Run Example:
----------------
nums = [1, 1, 0, 1, 1, 1]

Iteration:
i=0 → 1 → cnt=1 → maxi=0
i=1 → 1 → cnt=2 → maxi=0
i=2 → 0 → maxi=max(0,2)=2 → cnt=0
i=3 → 1 → cnt=1 → maxi=2
i=4 → 1 → cnt=2 → maxi=2
i=5 → 1 → cnt=3 → maxi=2
End → return max(maxi,cnt)=max(2,3)=3
"""

# ==============================================================
# Potential Edge Cases
# ==============================================================
"""
1. All Elements are 1:
   nums = [1,1,1,1,1] → Output = 5

2. No 1s in the array:
   nums = [0,0,0] → Output = 0

3. Single Element:
   nums = [1] → Output = 1
   nums = [0] → Output = 0

4. Alternating 1s and 0s:
   nums = [1,0,1,0,1] → Output = 1

5. Streak at the End:
   nums = [0,1,1,1,0,1,1] → Output = 3
"""

# ==============================================================
# Time and Space Complexity
# ==============================================================
"""
 Time Complexity: O(n)
- Single pass through the array
- Constant-time operations inside the loop

 Space Complexity: O(1)
- Only two variables (cnt and maxi) are used
- No extra space that scales with input size
"""

