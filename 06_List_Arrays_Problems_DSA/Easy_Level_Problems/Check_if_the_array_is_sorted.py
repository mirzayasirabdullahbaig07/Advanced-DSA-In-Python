"""
===================================================
 Problem: Check if Array is Sorted (Non-decreasing)
===================================================

---------------------------------------------------
1. What does the problem ask?
---------------------------------------------------
Given an integer array arr, decide if it is sorted
in non-decreasing order (each element ≤ next one).
Return True if the whole array obeys this rule,
otherwise return False.

---------------------------------------------------
2. Quick Examples
---------------------------------------------------
arr         → Output   Why
[1, 2, 2, 5] → True    Every element ≤ next.
[3, 4, 1]    → False   4 > 1 breaks the rule.
[7]          → True    Single element → sorted.
[]           → True    Empty list → trivially sorted.

---------------------------------------------------
3. Intuition & Approach
---------------------------------------------------
Think sliding window of size 2:
- Compare each pair (arr[i], arr[i+1]).
- If all satisfy arr[i] ≤ arr[i+1] → sorted.
- The *first* violation proves unsorted → early exit.

Analogy:
Walking uphill. The moment you step *down* a hill,
you know the terrain is not fully uphill.

---------------------------------------------------
4. Code
---------------------------------------------------
"""

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        n = len(arr)
        # Compare neighbour pairs
        for i in range(n - 1):             # loop until 2nd-last element
            if arr[i] > arr[i + 1]:        # found a drop → unsorted
                return False
        return True                        # never dropped → sorted


"""
---------------------------------------------------
5. Step-by-step Explanation
---------------------------------------------------
- No special handling for size ≤ 1:
  loop auto-skips → return True.
- For each index i from 0 to n-2:
    Compare arr[i] vs arr[i+1].
    If arr[i] > arr[i+1], exit early → False.
- If loop ends without exit, all pairs valid → True.

---------------------------------------------------
6. Dry Run
---------------------------------------------------
Input: [3, 5, 5, 2, 6]

i   Compare    Result
0   3 ≤ 5      OK
1   5 ≤ 5      OK
2   5 ≤ 2      False → exit

Function returns False.

---------------------------------------------------
7. Complexity
---------------------------------------------------
Metric     Value     Reason
Time       O(n)      Single linear scan.
Space      O(1)      Only loop index; no extra DS.

---------------------------------------------------
8. Conclusion
---------------------------------------------------
- To check sorted order, just compare neighbours.
- Clean 5-line code, O(n) time, O(1) space.
- Early exit when unsorted detected.
- Already optimal — nothing fancier needed!

===================================================
"""

# ------------------- Demo -------------------
if __name__ == "__main__":
    s = Solution()
    print(s.arraySortedOrNot([1, 2, 2, 5]))  # True
    print(s.arraySortedOrNot([3, 4, 1]))     # False
    print(s.arraySortedOrNot([7]))           # True
    print(s.arraySortedOrNot([]))            # True