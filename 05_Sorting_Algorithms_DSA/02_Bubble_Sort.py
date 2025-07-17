# -----------------------------------------------------------------------------------
# What is Bubble Sort in Python?
# Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
# compares adjacent elements and swaps them if they are in the wrong order.
# The pass through the list is repeated until the list is sorted.

# Example list
nums = [5, 1, 6, 8, 2, 4, 9]

# Function to perform bubble sort (ascending order)
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                # Swap if the element is greater than the next
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

# Call the function to sort the list
bubble_sort(nums)

# Output the sorted list
print("Sorted in Ascending Order (Bubble Sort):", nums)

# Time Complexity:
# Worst Case:    O(n^2) — when the list is in reverse order
# Average Case:  O(n^2)
# Best Case:     O(n) — when the list is already sorted (with optimization)

# Space Complexity:
# O(1) — Constant space, in-place sorting

# Source: https://codeanddebug.in/blog/bubble-sort-algorithm-in-python/
