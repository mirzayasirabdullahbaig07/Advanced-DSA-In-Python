"""
---------------------------------------------
DSA Problem: Missing Number (LeetCode #268)
---------------------------------------------
 Problem Statement:
Given an array 'nums' containing 'n' distinct numbers 
in the range [0, n], return the only number in the range 
that is missing from the array.

Example:
---------
Input  : nums = [3, 0, 1]
Output : 2

Explanation:
------------
The range is [0, 3], and '2' is missing from the list.
"""

# ==============================================================
# APPROACH 1 — BRUTE FORCE
# ==============================================================
"""
 Technique Used:
-------------------
Linear Search with Membership Checking.

 Idea:
We know that the missing number must be between 0 and n.
For each number i in [0, n]:
    - Check if i is present in the array.
    - If not, that’s our missing number.

 Behind the Scenes:
---------------------
The 'in' operator in Python performs a linear scan (O(n)).
Since we use it for each number (O(n) times),
this results in an overall O(n²) complexity.

 Time Complexity:  O(n²)
 Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Step 1: Iterate through all numbers from 0 to n
        for i in range(len(nums) + 1):
            # Step 2: Check if i is not present in nums
            if i not in nums:
                # Step 3: Return the missing number
                return i


"""
 Example Dry Run:
-------------------
nums = [3, 0, 1]
n = 3

Check sequence:
i = 0 → found
i = 1 → found
i = 2 → NOT found → return 2
"""


# ==============================================================
# APPROACH 2 — BETTER SOLUTION (HASH MAP)
# ==============================================================
"""
 Technique Used:
-------------------
Hashing (Dictionary / Frequency Map)

 Idea:
We can use a dictionary to track whether each number 
from 0 to n exists in nums.
If any number’s frequency remains 0 → that’s the missing number.

 Behind the Scenes:
---------------------
We initialize all keys 0 to n in a hash map with value 0.
We iterate once to mark existing numbers.
We iterate again to find the one with frequency 0.

This avoids the O(n²) scan, giving us linear time.

 Time Complexity:  O(n)
 Space Complexity: O(n)
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # Step 1: Initialize frequency dictionary
        freq = {i: 0 for i in range(n + 1)}

        # Step 2: Mark presence of each number
        for num in nums:
            freq[num] += 1

        # Step 3: Find the number that has count 0
        for key, value in freq.items():
            if value == 0:
                return key


"""
 Example Dry Run:
-------------------
nums = [3, 0, 1]
n = 3

Initial freq = {0:0, 1:0, 2:0, 3:0}
After marking:
    freq[3] = 1
    freq[0] = 1
    freq[1] = 1
Now freq = {0:1, 1:1, 2:0, 3:1}
Missing number = 2
"""


# ==============================================================
# APPROACH 3 — OPTIMAL SOLUTION (MATHEMATICAL FORMULA)
# ==============================================================
"""
 Technique Used:
-------------------
Mathematical Formula (Sum of Natural Numbers)

 Idea:
The sum of all numbers from 0 to n is given by:
    total_sum = n * (n + 1) / 2

If we subtract the actual sum of elements in nums 
from the expected total sum,
the difference gives the missing number.

 Behind the Scenes:
---------------------
Instead of looping or using data structures,
we rely purely on arithmetic operations.

This approach is the most efficient:
• No nested loops (only one pass)
• No extra space used
• Uses the concept of Arithmetic Progression (AP)

 Time Complexity:  O(n)
 Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Step 1: Get number of elements
        n = len(nums)

        # Step 2: Expected sum of 0..n using AP formula
        expected_sum = (n * (n + 1)) // 2

        # Step 3: Actual sum of given numbers
        actual_sum = sum(nums)

        # Step 4: Missing number = expected_sum - actual_sum
        return expected_sum - actual_sum


"""
 Example Dry Run:
-------------------
nums = [3, 0, 1]
n = 3
expected_sum = (3 * (3 + 1)) // 2 = 6
actual_sum   = 3 + 0 + 1 = 4
missing_num  = 6 - 4 = 2
Output → 2
"""

# ==============================================================
# COMPARISON SUMMARY
# ==============================================================

"""
---------------------------------------------------------------
| Approach  | Technique Used        | Time Complexity | Space  |
|------------|-----------------------|-----------------|---------|
| Brute Force| Linear Search         | O(n²)           | O(1)   |
| Better     | Hashing (Dictionary)  | O(n)            | O(n)   |
| Optimal    | Math Formula (AP Sum) | O(n)            | O(1)   |
---------------------------------------------------------------

 Key Learning:
1. Start with a simple (but slow) brute-force idea.
2. Optimize it using data structures (hash maps).
3. Finally, simplify with mathematical reasoning.
This process shows the evolution of problem-solving in DSA.
"""
