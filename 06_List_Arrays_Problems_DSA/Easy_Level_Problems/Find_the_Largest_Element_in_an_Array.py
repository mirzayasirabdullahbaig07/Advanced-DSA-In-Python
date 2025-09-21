# Python Program to Find the Largest Element in an Array (Without Sorting)
# ----------------------------------------------------------------------
# In this article, we’ll guide you through the Python program to find the largest element
# in an Array without Sorting. We’ll cover examples, brute force solution, optimal solution,
# dry runs, edge cases, and time/space complexities.

# ----------------------------------------------------------------------
# Examples
# ----------------------------------------------------------------------
# Example 1:
# Input: arr = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
#
# Example 2:
# Input: arr = [5, 5, 5, 5]
# Output: 5
# Explanation: All elements are equal, so largest = 5.
#
# Example 3:
# Input: arr = [10]
# Output: 10
# Explanation: Single element array, so 10 is largest.
#
# Constraints:
# 1 <= arr.size() <= 10^6
# 0 <= arr[i] <= 10^6

# ----------------------------------------------------------------------
# 1. Brute Force Solution (With Sorting)
# ----------------------------------------------------------------------
# Intuition:
# Sorting places all elements in ascending order → largest element is last.
#
# Approach:
# 1. Sort the array.
# 2. Return the last element.

def largestElement_bruteforce(arr: [], n: int) -> int:
    # Sort the elements first
    arr.sort()

    # Return the largest from the end
    return arr[-1]

# Code Explanation:
# arr.sort() → Sorts the array.
# arr[-1] → After sorting, the last element is the largest.

# Dry Run:
# arr = [1, 8, 7, 56, 90]
# After sorting → [1, 7, 8, 56, 90]
# arr[-1] = 90 → Output = 90

# Edge Cases:
# - Single element → largest = that element.
# - All identical elements → returns that element.
# - Already unsorted input handled by sorting.

# Complexity:
# Time → O(n log n) due to sorting.
# Space → O(1) (ignoring sorting space overhead).

# ----------------------------------------------------------------------
# 2. Optimal Solution (Single Pass Solution)
# ----------------------------------------------------------------------
# Intuition:
# Keep track of the maximum while traversing the array.
#
# Approach:
# 1. Initialize max with the first element.
# 2. Traverse each element.
# 3. If an element is greater, update max.
# 4. Return max.

def largestElement_optimal(arr: [], n: int) -> int:
    max_num = arr[0]
    
    for num in arr:
        if num > max_num:
            max_num = num
    
    return max_num

# Code Explanation:
# - max_num = arr[0] → Assume first element is largest.
# - for num in arr → Traverse all elements.
# - if num > max_num → Update max_num.
# - return max_num → Final largest element.

# Dry Run:
# arr = [1, 8, 7, 56, 90]
# Step 1: max_num = 1
# Step 2: Compare 8 → 8 > 1 → max_num = 8
# Step 3: Compare 7 → 7 < 8 → no change
# Step 4: Compare 56 → 56 > 8 → max_num = 56
# Step 5: Compare 90 → 90 > 56 → max_num = 90
# Output = 90

# Edge Cases:
# - Single element → directly returned.
# - All identical elements → returns that element.
# - Negative numbers → handled correctly (largest = closest to zero).

# Complexity:
# Time → O(n) since we traverse once.
# Space → O(1) constant extra space.

# ----------------------------------------------------------------------
# Conclusion:
# ----------------------------------------------------------------------
# - Brute Force uses sorting: O(n log n).
# - Optimal uses a single pass: O(n).
# - Always prefer the optimal solution for efficiency.
#
# Recommended Practice: Try both approaches to understand trade-offs.
