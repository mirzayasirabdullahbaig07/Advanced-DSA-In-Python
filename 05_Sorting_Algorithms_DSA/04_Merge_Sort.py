# ----------------------------------------------------
# What is Merge Sort?
# ----------------------------------------------------
# Merge Sort is a Divide and Conquer algorithm.
# It divides the input array into two halves, calls itself for the two halves,
# and then merges the two sorted halves.

# ----------------------------------------------------
# Why and Where We Use Merge Sort?
# ----------------------------------------------------
# - Merge Sort is very efficient for large datasets.
# - It has guaranteed O(n log n) time complexity in all cases (best, average, worst).
# - It is a stable sorting algorithm.
# - Used in applications where consistent time is required (e.g., external sorting, databases, etc.)

# ----------------------------------------------------
# How Does Division Work?
# ----------------------------------------------------
# - If the array length is even: split evenly, e.g., [1, 2, 3, 4] → [1, 2] and [3, 4]
# - If the array length is odd: one subarray will be 1 element larger, e.g., [1, 2, 3] → [1] and [2, 3]

# ----------------------------------------------------
# Merge Sort Implementation in Python
# ----------------------------------------------------

def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] <= right[j]:  # FIX: corrected index from right[i] to right[j]
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])  # FIX: was wrongly using `n` instead of `m`
        j += 1

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Recursive calls
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_array(left, right)

# ----------------------------------------------------
# Example Use Case
# ----------------------------------------------------
nums = [3, 1, 3, 4, 1, 5, 2, 6, 4]
sorted_nums = merge_sort(nums)
print("Sorted Array:", sorted_nums)

# ----------------------------------------------------
# Time Complexity:
# Best / Average / Worst: O(n log n)
# Space Complexity: O(n) due to extra space used for merging
# ----------------------------------------------------
