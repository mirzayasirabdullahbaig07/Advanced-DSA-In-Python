# What is Insertion Sort in Python?
# ----------------------------------
# Insertion Sort is a simple sorting algorithm that builds the final sorted list one item at a time.
# It's much like sorting playing cards in your hands.
# At each step, it picks the next element and inserts it into the correct position among the previously sorted elements.

# Where do we use it?
# --------------------
#  When the list is **small**
#  When the list is **already mostly sorted**
#  When we want a **simple, in-place sorting** with minimal memory usage

# Example list to sort
nums = [3, 5, 6, 4, 8, 9, 10, 7, 1]

# Length of the list
n = len(nums)

# Insertion Sort Algorithm
for i in range(1, n):
    key = nums[i]  # Current element to insert
    j = i - 1

    # Move elements of nums[0..i-1], that are greater than key, to one position ahead
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    # Insert the key into the correct location
    nums[j + 1] = key

# Final sorted list
print("Sorted list using Insertion Sort:", nums)

# Time Complexity:
# ----------------
# Best Case: O(n)         --> when the array is already sorted
# Average Case: O(n^2)
# Worst Case: O(n^2)      --> when the array is sorted in reverse

# Space Complexity:
# -----------------
# O(1) --> In-place sorting algorithm, does not require extra space
