"""
 Problem #169 — Majority Element (LeetCode)

 Problem Statement:
Given an integer array nums of size n, return the majority element — the element that appears more than ⌊ n / 2 ⌋ times.
You may assume the majority element always exists.

Example:
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
Explanation: The number 2 appears 4 times which is greater than 7/2 = 3.

-------------------------------------------------------------------
 INTUITION:
We need to find the number that appears more than half of the array’s length. 
It’s guaranteed that one such number always exists.

-------------------------------------------------------------------
 Solution 1: Brute Force (Double Loop)
-------------------------------------------------------------------
 Intuition:
Compare each element with every other element and count how many times it appears.
If its count > n // 2, that’s the majority element.

 Approach:
1. Loop through every element i.
2. For each i, count how many times nums[i] appears in the array.
3. If count > n // 2 → return that element.

 Code:
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            if count > n // 2:
                return nums[i]
"""
 Example:
nums = [3, 3, 4]
i = 0 → count(3) = 2 → 2 > 3//2 (1) → return 3

 Time Complexity: O(n²)
 Space Complexity: O(1)

 Conclusion:
Simple to understand but inefficient for large inputs.

-------------------------------------------------------------------
 Solution 2: Better (Using Hash Map)
-------------------------------------------------------------------
 Intuition:
Instead of counting manually, use a dictionary (hash map) to store how many times each number appears.

 Approach:
1. Create an empty dictionary.
2. For each num in nums, increase its count in the dictionary.
3. After counting, check which number’s count > n // 2.

 Code:
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for k, v in freq.items():
            if v > n // 2:
                return k
"""
 Example:
nums = [2, 2, 1]
Step 1 → freq = {2: 2, 1: 1}
Check → 2 appears 2 times > 3//2 → return 2

 Time Complexity: O(n)
 Space Complexity: O(k), where k = number of unique elements

 Conclusion:
Much faster than brute force, but uses extra space for counting.

-------------------------------------------------------------------
 Solution 3: Optimal (Boyer-Moore Voting Algorithm)
-------------------------------------------------------------------
 Intuition:
Think of every different element as “canceling” one vote of the majority element.
Since the majority element has more than half of total votes, it will survive at the end.

 Approach:
1. Start with `count = 0` and `candidate = None`.
2. Traverse the array:
   - If count == 0 → pick current num as candidate.
   - If num == candidate → increase count.
   - Else → decrease count.
3. After the loop ends, candidate will be the majority.

 Code:
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
"""
 Example:
nums = [2, 2, 1, 1, 1, 2, 2]
Step-by-step:
Index | Num | Candidate | Count
0     | 2   | 2         | 1
1     | 2   | 2         | 2
2     | 1   | 2         | 1
3     | 1   | 2         | 0 (reset)
4     | 1   | 1         | 1
5     | 2   | 1         | 0 (reset)
6     | 2   | 2         | 1
 Final Candidate = 2 → Majority Element

 Time Complexity: O(n)
 Space Complexity: O(1)

 Why It Works:
Every time we meet a number different from the candidate, it “cancels” one vote.
Since the majority element has more votes than all others combined, it can never be fully canceled.

-------------------------------------------------------------------
 Final Comparison:

| Approach     | Time | Space | Notes |
|---------------|------|--------|--------|
| Brute Force   | O(n²) | O(1)  | Simple but slow |
| Hash Map      | O(n)  | O(k)  | Fast but uses memory |
| Boyer-Moore   | O(n)  | O(1)  | Fastest & cleanest |

-------------------------------------------------------------------
 Conclusion:
The Boyer-Moore Voting Algorithm is the best solution for this problem.
It’s elegant, uses constant space, and runs in linear time.
This is the standard approach interviewers expect for “Majority Element” questions.
"""
