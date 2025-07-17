# What is Selection Sort in Python?
# Selection Sort is a simple comparison-based sorting algorithm.
# It repeatedly finds the minimum element from the unsorted part and puts it at the beginning.
# You can use it to sort in both ascending and descending order.

# Example list
nums = [5, 7, 8, 4, 1, 6, 9, 2]

# Function to perform selection sort (ascending order)
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the current element with the smallest found
        nums[i], nums[min_index] = nums[min_index], nums[i]

# Call the function to sort the list
selection_sort(nums)

# Output the sorted list
print("Sorted in Ascending Order:", nums)

# Time Complexity:
# Worst Case:    O(n^2)
# Average Case:  O(n^2)
# Best Case:     O(n^2)
# Because it always performs n(n-1)/2 comparisons regardless of input order.

# Space Complexity:
# O(1) — Constant space, in-place sorting.

# To sort in descending order:
# Change the comparison from < to >
# Example: if nums[j] > nums[max_index]:
