"""
-------------------------------------------------------------
DSA Problem: Two Sum (LeetCode #1)
-------------------------------------------------------------
 Problem Statement:
Given an array of integers 'nums' and an integer 'target',
return the indices of the two numbers such that they add up
to 'target'. Each input has exactly one solution and each
element can be used only once.

Example:
---------
Input  : nums = [2,7,11,15], target = 9
Output : [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""

# ==============================================================
# OPTIMAL SOLUTION — USING HASH MAP (DICTIONARY)
# ==============================================================
"""
 Technique Used:
-------------------
Hash Map (Dictionary) for Constant-Time Lookup

 Idea:
- While iterating through the array, calculate the complement
  needed to reach the target:
    remaining = target - nums[i]
- If the complement is already in the hash map, we found the pair.
- Otherwise, store the current number and its index in the hash map
  for future reference.
- This allows finding the pair in a single pass O(n) without nested loops.

 Behind the Scenes:
---------------------
1. Use a dictionary to store numbers as keys and their indices as values.
2. For each number, check if the complement exists in the dictionary:
   - If yes → return [index of complement, current index]
   - If no  → store current number in dictionary
3. This ensures only one pass through the array is needed.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}  # Stores number → index

        # Step 1: Iterate through the array
        for i, num in enumerate(nums):
            remaining = target - num  # Compute complement

            # Step 2: Check if complement exists in hash_map
            if remaining in hash_map:
                # Pair found → return indices
                return [hash_map[remaining], i]

            # Step 3: Store current number and index for future checks
            hash_map[num] = i


"""
 Step-by-Step Explanation:
-----------------------------
nums = [3,2,4], target = 6

Iteration:
i=0 → num=3 → remaining=3 → not in hash_map → store 3:0 → hash_map={3:0}
i=1 → num=2 → remaining=4 → not in hash_map → store 2:1 → hash_map={3:0,2:1}
i=2 → num=4 → remaining=2 → 2 is in hash_map → return [1,2]

Result = [1,2]
"""

# ==============================================================
# Edge Cases
# ==============================================================
"""
1. Negative Numbers:
   nums = [-1, -2, -3, -4, -5], target = -8 → Output = [2,4]

2. Pair at the Start:
   nums = [1,5,3], target = 6 → Output = [0,1]

3. Pair at the End:
   nums = [1,2,4,5], target = 9 → Output = [2,3]

4. Duplicates:
   nums = [3,3], target = 6 → Output = [0,1]

Note: Problem guarantees exactly one solution.
"""

# ==============================================================
# Time and Space Complexity
# ==============================================================
"""
 Time Complexity: O(n)
- Single pass through the array
- Each dictionary lookup and insertion is O(1) on average

 Space Complexity: O(n)
- In the worst case, all numbers are stored in the hash map
- Hash map size scales linearly with input size
"""
