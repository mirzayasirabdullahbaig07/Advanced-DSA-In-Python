"""
 LeetCode #2149 — Rearrange Array Elements by Sign
============================================================
 Problem Statement:
------------------------------------------------------------
You are given a 0-indexed integer array `nums` of even length consisting of an equal number 
of positive and negative integers.

Your task is to rearrange the elements of `nums` so that:
1 Every consecutive pair of integers has opposite signs.
2 For all integers with the same sign, the order from the original array is preserved.
3 The rearranged array starts with a positive integer.

Return the modified array that satisfies all these conditions.

------------------------------------------------------------
 Example 1:
------------------------------------------------------------
Input:
    nums = [3, 1, -2, -5, 2, -4]

Output:
    [3, -2, 1, -5, 2, -4]

Explanation:
    Positives = [3, 1, 2]
    Negatives = [-2, -5, -4]
    The only valid alternating arrangement (starting with positive) is:
    [3, -2, 1, -5, 2, -4]

------------------------------------------------------------
 Example 2:
------------------------------------------------------------
Input:
    nums = [-1, 1]

Output:
    [1, -1]

Explanation:
    Positive = [1], Negative = [-1]
    After rearranging alternately starting with positive → [1, -1]

------------------------------------------------------------
 Objective:
------------------------------------------------------------
Rearrange the array such that:
    - Elements alternate in sign (+, -, +, -, ...)
    - Relative order among same-sign elements is maintained
    - The first element is positive

------------------------------------------------------------
 Constraints:
------------------------------------------------------------
2 <= nums.length <= 2 * 10⁵
nums.length is even
Each |nums[i]| ≤ 10⁵
Equal number of positive and negative integers

============================================================
 Approach 1: Brute Force Method
============================================================

 Intuition:
-------------
We can start by dividing all numbers into two separate lists:
    → One for positive numbers
    → One for negative numbers
Then, we can merge them back alternately into the original array:
    Positive → Negative → Positive → Negative → ...

This ensures alternate signs and maintains original order.

------------------------------------------------------------
 Code Implementation:
------------------------------------------------------------
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        n = len(nums)

        # Step 1: Separate positive and negative numbers
        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        # Step 2: Rearrange alternately
        for i in range(len(pos)):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]

        return nums
"""
------------------------------------------------------------
 Dry Run:
------------------------------------------------------------
Input:
    nums = [3, 1, -2, -5, 2, -4]

Step 1 → Separate:
    pos = [3, 1, 2]
    neg = [-2, -5, -4]

Step 2 → Merge alternately:
    nums[0] = 3 (pos[0])
    nums[1] = -2 (neg[0])
    nums[2] = 1 (pos[1])
    nums[3] = -5 (neg[1])
    nums[4] = 2 (pos[2])
    nums[5] = -4 (neg[2])

Final Output:
    [3, -2, 1, -5, 2, -4]

------------------------------------------------------------
 Time Complexity:
O(N) for separating + O(N) for merging → O(2N) ≈ O(N)

 Space Complexity:
O(N) — for storing positives and negatives separately

------------------------------------------------------------
 Advantages:
 Very easy to understand and implement  
 Preserves order perfectly

 Disadvantages:
 Uses extra space for two temporary arrays

============================================================
 Approach 2: Optimal Solution (Using Two Pointers)
============================================================

 Intuition:
-------------
We can improve space usage slightly by using two pointers:
- One pointer (`posIndex`) for placing positives (even indices: 0, 2, 4, …)
- Another pointer (`negIndex`) for placing negatives (odd indices: 1, 3, 5, …)

As we traverse the array:
- If we encounter a positive number → place it at ans[posIndex], move posIndex += 2
- If we encounter a negative number → place it at ans[negIndex], move negIndex += 2

This way, we build the final result in a single pass.

------------------------------------------------------------
 Code Implementation:
------------------------------------------------------------
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        posIndex, negIndex = 0, 1

        for i in range(n):
            if nums[i] < 0:
                ans[negIndex] = nums[i]
                negIndex += 2
            else:
                ans[posIndex] = nums[i]
                posIndex += 2

        return ans
"""
------------------------------------------------------------
 Dry Run:
------------------------------------------------------------
Input:
    nums = [3, 1, -2, -5, 2, -4]
Initial:
    ans = [0, 0, 0, 0, 0, 0]
    posIndex = 0, negIndex = 1

→ nums[0] = 3 → positive → ans[0] = 3 → posIndex = 2  
→ nums[1] = 1 → positive → ans[2] = 1 → posIndex = 4  
→ nums[2] = -2 → negative → ans[1] = -2 → negIndex = 3  
→ nums[3] = -5 → negative → ans[3] = -5 → negIndex = 5  
→ nums[4] = 2 → positive → ans[4] = 2 → posIndex = 6  
→ nums[5] = -4 → negative → ans[5] = -4 → negIndex = 7  

Final Output:
    ans = [3, -2, 1, -5, 2, -4]

------------------------------------------------------------
 Time Complexity:
O(N) — one traversal only

 Space Complexity:
O(N) — new array created to store the answer

------------------------------------------------------------
 Advantages:
 Single-pass efficient approach  
 Easy to read and code  
 No need for two separate lists

 Disadvantages:
 Still uses O(N) extra space (cannot be done truly in-place easily)

============================================================
 Final Comparison Table:
============================================================

| Approach              | Time Complexity | Space Complexity | Order Preserved | Description                            |
|-----------------------|-----------------|------------------|-----------------|----------------------------------------|
| Brute Force           | O(N)            | O(N)             |  Yes          | Separate + Merge                       |
| Optimal (Two Pointers)| O(N)            | O(N)             |  Yes          | Fill using two indices directly        |

============================================================
 Final Summary:
------------------------------------------------------------
 Both approaches work perfectly and preserve order.
 Optimal solution is cleaner, more efficient, and widely used in interviews.
 Key takeaway:
   Use two pointers for problems involving alternating placement 
   of elements based on a condition (positive/negative, even/odd, etc.).

------------------------------------------------------------
 Example Recap:

Input:
    nums = [3, 1, -2, -5, 2, -4]
Output:
    [3, -2, 1, -5, 2, -4]

Input:
    nums = [-1, 1]
Output:
    [1, -1]

Both solutions achieve the same correct result.
"""
