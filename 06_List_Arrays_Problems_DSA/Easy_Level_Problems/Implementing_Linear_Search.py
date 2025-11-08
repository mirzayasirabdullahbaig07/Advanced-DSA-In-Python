# Linear Search | Explained in Python

"""
 Problem Statement:
Given an array `arr` of n integers and an integer `x`,
find whether element `x` is present in the array.
If found, return the index of its first occurrence; otherwise, return -1.

Example:
arr = [10, 20, 30, 40, 50], x = 30
Output → 2  (since 30 is present at index 2)
"""

def linearSearch(n: int, num: int, arr: [int]) -> int:
    """
     Technique Used: Linear Search (Sequential Search)
    -----------------------------------------------------
    - This is one of the most basic searching algorithms in DSA.
    - It works by scanning the entire array sequentially from left to right.
    - Each element is compared with the target value `num`.
    - If a match is found, we return its index immediately.
    - If no match is found after traversing the entire array, return -1.
    """

    # Step 1: Traverse through the array
    for i in range(len(arr)):
        """
         Behind the Scenes:
        - We iterate over each index `i` starting from 0.
        - On every iteration, the element arr[i] is compared to the target num.
        - Comparison operation → arr[i] == num
        - This continues until we find the target or reach the end.
        """
        if arr[i] == num:
            """
             Element Found:
            - When arr[i] matches num, we have found the target.
            - Return the current index `i` immediately.
            - No need to continue the loop as we only want the first occurrence.
            """
            return i

    """
     Element Not Found:
    - If the loop completes and we didn’t find any match,
      that means num is not present in arr.
    - Return -1 to indicate that.
    """
    return -1


# -------------------------- DRY RUN --------------------------
"""
Example:
arr = [2, 4, 6, 8, 10], num = 8

Step 1: Compare arr[0] (2) with 8 → not equal
Step 2: Compare arr[1] (4) with 8 → not equal
Step 3: Compare arr[2] (6) with 8 → not equal
Step 4: Compare arr[3] (8) with 8 → match found → return 3
Output = 3
"""

# -------------------------- TEST CASES --------------------------
arr = [10, 20, 30, 40, 50]
print("Index of 30:", linearSearch(len(arr), 30, arr))  # Output: 2
print("Index of 60:", linearSearch(len(arr), 60, arr))  # Output: -1


# -------------------------- COMPLEXITY ANALYSIS --------------------------
"""
 Time Complexity:
----------------------------------
Best Case: O(1)  → Element found at the first position.
Worst Case: O(n) → Element not found or present at the last position.
Average Case: O(n) → On average, we may have to scan half of the array.

 Space Complexity:
----------------------------------
O(1) → Constant space.
Only a few variables (like i, num) are used, no extra data structures.

 Summary:
----------------------------------
Technique Used: Linear / Sequential Search
In-Place: Yes
Stable: Yes (does not disturb order)
Efficient For: Small / unsorted datasets
Not Efficient For: Large arrays (use Binary Search when sorted)
"""
