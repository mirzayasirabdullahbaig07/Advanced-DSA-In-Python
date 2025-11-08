"""
==========================================
 Move Zeroes | LeetCode 283 | Explained
==========================================

 Problem Statement:
---------------------
Given an integer array nums, move all 0’s to the end of it 
while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example:
---------
Input:  nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

# =========================================================
#  BRUTE FORCE SOLUTION (Using Temporary List)
# =========================================================

"""
 Technique Used:
------------------
- Array Traversal + Temporary Storage
- Extract all non-zero elements into a temporary list `temp`
- Copy them back to the original array
- Fill the remaining positions with zeros

 DSA Concept Behind:
----------------------
- Traversing arrays to filter data (non-zero extraction)
- Maintaining order by appending in sequence
- Rewriting in-place for final arrangement

 Time Complexity: O(n)
   - One traversal to collect non-zeros
   - One traversal to copy them back
   - One traversal to fill zeros
 Space Complexity: O(n)
   - Uses an extra list `temp` to hold non-zero elements
"""

class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        temp = []  # To store all non-zero elements

        # Step 1: Collect all non-zero elements
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])

        # Step 2: Copy non-zero elements back
        nz = len(temp)
        for i in range(nz):
            nums[i] = temp[i]

        # Step 3: Fill remaining positions with zeros
        for i in range(nz, n):
            nums[i] = 0


#  Example Dry Run
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print("Brute Force Output:", nums)

"""
Dry Run:
---------
Input  : [0, 1, 0, 3, 12]
Step 1 : temp = [1, 3, 12]
Step 2 : nums = [1, 3, 12, _, _]
Step 3 : nums = [1, 3, 12, 0, 0]
Output : [1, 3, 12, 0, 0]
"""


# =========================================================
#  OPTIMAL SOLUTION (Using Two-Pointer Technique)
# =========================================================

"""
 Technique Used:
------------------
- Two Pointer Approach (in-place)
- One pointer (`i`) tracks the position of the first zero.
- Second pointer (`j`) scans for non-zero elements.
- Whenever a non-zero element is found, swap it with the zero at position `i`.
- Increment `i` to move the zero boundary forward.

 DSA Concept Behind:
----------------------
- **Two-Pointer Technique**: Widely used in array manipulation problems
  to minimize extra space and reduce passes.
- **In-place Swapping**: Moves elements efficiently while maintaining order.

 Intuition:
-------------
Imagine pushing all non-zero elements forward (left side), 
while zeros get naturally pushed toward the end.

 Time Complexity: O(n)
   - Each element is visited at most once.
 Space Complexity: O(1)
   - Only uses pointers; no extra storage required.
"""

class Solution:
    def moveZeroes(self, nums):
        if len(nums) <= 1:
            return  # No need to process single-element array

        # Step 1: Find first zero's position
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        else:
            return  # No zeros found

        # Step 2: Use second pointer j to find next non-zero
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]  # Swap
                i += 1
            j += 1


#  Example Dry Run
nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print("Optimal (Two Pointer) Output:", nums)

"""
Dry Run:
---------
Initial: [0, 1, 0, 3, 12]
i = 0 (points to first zero)
j = 1 (finds non-zero 1)

Swap → [1, 0, 0, 3, 12]
i moves to index 1
j moves ahead

Next swap (nums[j]=3, j=3) → [1, 3, 0, 0, 12]
Next swap (nums[j]=12, j=4) → [1, 3, 12, 0, 0]

Output : [1, 3, 12, 0, 0]
"""

# =========================================================
#  Summary of Both Approaches
# =========================================================

"""
| Approach      | Technique Used          | Time Complexity | Space Complexity | Remarks |
|----------------|-------------------------|----------------|------------------|----------|
| Brute Force    | Temporary List (extra space) | O(n)        | O(n)             | Maintains order but not space efficient |
| Optimal        | Two-Pointer (in-place)      | O(n)        | O(1)             | Best approach, efficient and clean |
"""

# =========================================================
#  Behind the Scenes (Core DSA Concepts)
# =========================================================

"""
 1. Two Pointer Technique:
   - Common in array rearrangement problems.
   - One pointer tracks the target position, 
     and the other scans for valid elements to swap.

 2. In-place Operations:
   - Avoids creating new arrays, reducing space usage.
   - Used in optimized algorithms to achieve O(1) space.

 3. Stability (Relative Order Preservation):
   - We ensure non-zero elements maintain their order.
   - Important detail in DSA array transformation problems.

 4. Real-world Analogy:
   - Think of moving all zero-weight boxes to the back of a truck
     without changing the order of heavy ones.
"""

