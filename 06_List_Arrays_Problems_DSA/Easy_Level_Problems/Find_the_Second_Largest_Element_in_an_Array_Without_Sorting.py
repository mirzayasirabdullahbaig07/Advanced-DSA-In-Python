"""
===================================================
 Problem: Second Largest and Second Smallest
===================================================

You are given an array a of length n.
Return a list [secondLargest, secondSmallest], where

    secondLargest  = the second-largest distinct value in a
    secondSmallest = the second-smallest distinct value in a

Constraints:
- All elements are distinct
- n ≥ 2

---------------------------------------------------
 Example
---------------------------------------------------
a             → Answer     Why
[5, 1, 3, 4, 2] → [4, 2]   Sorted → 1 < 2 < 3 < 4 < 5
                           2nd largest = 4, 2nd smallest = 2

[9, 7]         → [7, 9]   Only two elements.
                           Second-largest = smaller one (7)
                           Second-smallest = larger one (9)

---------------------------------------------------
 High-level Idea
---------------------------------------------------
We need:
- Top two largest numbers
- Bottom two smallest numbers

Sorting is unnecessary (O(n log n)).
Instead:
- Track just two best candidates on each side.
- Done in O(n) with O(1) space.

---------------------------------------------------
 Solution 1 – Better (Two-pass)
---------------------------------------------------
Intuition:
1st pass → find absolute min and max.
2nd pass → find the next best candidates:
           - greater than min (second-smallest)
           - smaller than max (second-largest)

Time: O(n) + O(n) = O(2n) → O(n)
Space: O(1)

"""

from typing import List

def getSecondOrderElements_two_pass(n: int, a: List[int]) -> List[int]:
    # Initialize sentinels
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    # -------- Pass 1: absolute min & max --------
    for x in a:
        small = min(small, x)
        large = max(large, x)

    # -------- Pass 2: second min & second max --------
    for x in a:
        if x < second_small and x != small:   # candidate above min
            second_small = x
        if x > second_large and x != large:   # candidate below max
            second_large = x

    return [second_large, second_small]


"""
---------------------------------------------------
 Dry Run (Two-pass)
---------------------------------------------------
Array = [5, 1, 3, 4, 2]

Pass 1 → small=1, large=5
Pass 2 → second_small=2, second_large=4

Return → [4, 2]
"""

"""
---------------------------------------------------
 Solution 2 – Optimal (One-pass)
---------------------------------------------------
Why faster?
We can update both smallest & largest pairs in
a single scan, with careful if–elif ordering.

Idea:
- If x is new min → push old min down to 2nd min.
- Else if x in-between → update 2nd min.
- If x is new max → push old max down to 2nd max.
- Else if x in-between → update 2nd max.

Time: O(n) (single scan)
Space: O(1)
"""

def getSecondOrderElements_one_pass(n: int, a: List[int]) -> List[int]:
    # Initialize sentinels
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    # -------- Single pass: update both ends --------
    for x in a:
        # ----- Smaller side -----
        if x < small:                        # found new min
            second_small = small             # push old min
            small = x
        elif small < x < second_small:       # between min and 2nd min
            second_small = x

        # ----- Larger side -----
        if x > large:                        # found new max
            second_large = large             # push old max
            large = x
        elif second_large < x < large:       # between 2nd max and max
            second_large = x

    return [second_large, second_small]


"""
---------------------------------------------------
 Dry Run (One-pass)
---------------------------------------------------
Array = [9, 7]

x = 9:
    small=9, second_small=inf
    large=9, second_large=-inf

x = 7:
    smaller side → 7 < small → second_small=9, small=7
    larger side → 7 > second_large and != large → second_large=7

Return → [7, 9]
"""

"""
---------------------------------------------------
 Which one to choose?
---------------------------------------------------
Criterion        Better (2-pass)           Optimal (1-pass)
-------------------------------------------------------------
Code clarity     Simpler to explain        Denser if-elif ladder
Reads array      2 × n                     1 × n
Speed            Linear both ways          Half the scans

Interview tip:
- Show two-pass first (clearer logic).
- Then refine to one-pass to show optimization skills.

---------------------------------------------------
 Key Takeaways
---------------------------------------------------
- Tracking only two smallest & two largest values
  is enough for all "second-order" problems.
- Clever if–elif ordering merges two passes into one.
- Always update second variables *before* overriding
  the first ones, or you lose information.

===================================================
"""

# ------------------- Demo -------------------
if __name__ == "__main__":
    arr1 = [5, 1, 3, 4, 2]
    arr2 = [9, 7]

    print("Two-pass:", getSecondOrderElements_two_pass(len(arr1), arr1))  # [4, 2]
    print("One-pass:", getSecondOrderElements_one_pass(len(arr2), arr2))  # [7, 9]
