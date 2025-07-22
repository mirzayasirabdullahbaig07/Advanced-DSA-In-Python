# What is Quick Sort?
# Quick Sort is a divide-and-conquer sorting algorithm. 
# It works by selecting a 'pivot' element and partitioning the array 
# into two sub-arrays: elements less than the pivot and elements greater than the pivot.
# It then recursively applies the same logic to the sub-arrays.

# Why do we use it?
# Quick Sort is efficient for large datasets and has good average-case performance.

# Where is it used?
# It's used in various places like:
# - Library implementations (e.g., Python's `sorted()` internally uses Timsort, a hybrid of Merge and Quick Sort)
# - When memory usage is a concern (Quick Sort uses O(1) extra space)

# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n^2) (when the pivot is the smallest or largest element repeatedly)

# Space Complexity: O(log n) due to recursive stack (not O(1), unless tail-recursion optimized)

nums = [4, 1, 7, 6, 3, 2, 8]

# Partition function to rearrange elements around the pivot
def partition(nums, low, high):
    pivot = nums[low]  # Pivot can also be last/middle/random
    i = low + 1
    j = high

    while i <= j:
        while i <= high and nums[i] <= pivot:
            i += 1
        while j >= low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j  # New pivot position

# Quick Sort function
def quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)

# Run the sort
quick_sort(nums, 0, len(nums) - 1)
print("Sorted array:", nums)
