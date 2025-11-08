"""
==========================================
 Right Rotate an Array by K Places
==========================================

 Problem Statement:
Given an array 'nums' and an integer 'k', rotate the array to the right by k steps, 
where k is non-negative.

Each rotation shifts elements to the right, 
and the last k elements move to the front of the array.

We will explore three approaches:
1. Brute Force (Using pop and insert)
2. Better Solution (Using slicing)
3. Optimal Solution (Using reversing)
"""

# =========================================================
#  1. BRUTE FORCE SOLUTION (Using pop and insert)
# =========================================================

"""
 Technique Used:
- Basic Python list operations (`pop()` and `insert()`).
- For every rotation, remove the last element and insert it at the front.
- We repeat this process 'k' times.

 Intuition:
If k = n (array length), the array remains unchanged.
So, we first do: k = k % n
Then, perform k right rotations using pop and insert.

 Time Complexity: O(k × n)
Because insert(0, x) takes O(n) time, repeated k times.
 Space Complexity: O(1)
We modify the array in-place without using extra space.
"""

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return

        k %= n  # Handle cases where k > n

        for _ in range(k):
            last = nums.pop()     # Removes last element
            nums.insert(0, last)  # Inserts it at the start

# Example Dry Run
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print("Brute Force Output:", nums)
"""
Step-by-step:
Initial: [1,2,3,4,5,6,7]
After 1st rotation: [7,1,2,3,4,5,6]
After 2nd rotation: [6,7,1,2,3,4,5]
After 3rd rotation: [5,6,7,1,2,3,4]
"""


# =========================================================
#  2. BETTER SOLUTION (Using Python Slicing)
# =========================================================

"""
 Technique Used:
- Python's powerful list slicing to rearrange elements efficiently.
- Use k = k % n to normalize rotations.
- Slice and concatenate:
  nums[:] = nums[n-k:] + nums[:n-k]

 Intuition:
The last k elements move to the front, 
and the first (n-k) elements shift to the right.

 Time Complexity: O(n)
Each slice copies elements once.
 Space Complexity: O(n)
Temporary slices are created during concatenation.
"""

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return

        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]

# Example Dry Run
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print("Slicing Output:", nums)
"""
Step-by-step:
nums[n-k:] = [5,6,7]
nums[:n-k] = [1,2,3,4]
New array = [5,6,7,1,2,3,4]
"""


# =========================================================
#  3. OPTIMAL SOLUTION (Using Reverse Algorithm)
# =========================================================

"""
 Technique Used:
- Reversal Algorithm for Array Rotation
- Instead of shifting one by one, reverse parts of the array to achieve rotation efficiently.

 Intuition:
For Right Rotate by k:
1. Reverse last k elements
2. Reverse first n-k elements
3. Reverse the entire array

Example:
nums = [1,2,3,4,5,6,7], k = 3

Step 1: Reverse last k → [1,2,3,4,5,6,7] → [1,2,3,4,5,7,6]
Step 2: Reverse first n-k → [4,3,2,1,5,7,6]
Step 3: Reverse entire array → [5,6,7,1,2,3,4]

 Time Complexity: O(n)
Each reversal traverses part of the array once.
 Space Complexity: O(1)
No extra array used — in-place swapping.
"""

class Solution:
    def reverse(self, nums, l, r):
        """Helper function to reverse array between indices l and r"""
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums, k):
        n = len(nums)
        if n == 0:
            return

        k %= n

        # Step 1: Reverse last k elements
        self.reverse(nums, n - k, n - 1)

        # Step 2: Reverse first n - k elements
        self.reverse(nums, 0, n - k - 1)

        # Step 3: Reverse the entire array
        self.reverse(nums, 0, n - 1)

# Example Dry Run
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print("Optimal (Reversal) Output:", nums)
"""
Step 1: Reverse last 3 → [1,2,3,4,7,6,5]
Step 2: Reverse first 4 → [4,3,2,1,7,6,5]
Step 3: Reverse all → [5,6,7,1,2,3,4]
"""


# =========================================================
#  Summary of All Approaches
# =========================================================

"""
| Approach      | Technique Used          | Time Complexity | Space Complexity | Remarks |
|----------------|-------------------------|----------------|------------------|----------|
| Brute Force    | pop() + insert() loop   | O(k × n)        | O(1)             | Simple but slow for large k |
| Better         | List Slicing            | O(n)            | O(n)             | Elegant and Pythonic |
| Optimal        | Reverse Algorithm       | O(n)            | O(1)             | Best for large arrays |
"""
