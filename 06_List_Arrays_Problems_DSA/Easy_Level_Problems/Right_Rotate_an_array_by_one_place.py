# Right Rotate an Array by One Place

# Example array
nums = [3, 4, 4, 45, 3, 0, 10, 6, 7]
n = len(nums)

"""
 Problem Statement:
Rotate the array elements to the right by one position.
This means the last element moves to the front,
and all other elements shift one place to the right.

Example:
Before rotation: [3, 4, 4, 45, 3, 0, 10, 6, 7]
After rotation:  [7, 3, 4, 4, 45, 3, 0, 10, 6]
"""

# ---------------- METHOD 1: Using Slicing ----------------
"""
Technique: Python List Slicing
nums[-1:] gives the last element as a list → [7]
nums[:-1] gives all elements except the last one → [3, 4, 4, 45, 3, 0, 10, 6]
By concatenating: nums[-1:] + nums[:-1] → [7] + [3, 4, 4, 45, 3, 0, 10, 6]
Finally, assign back to nums[:] to modify the list in place.
"""

nums[:] = nums[-1:] + nums[:-1]
print("After rotation using slicing:", nums)

"""
 Behind the scenes:
- nums[-1:] extracts the last element (7)
- nums[:-1] extracts all except last
- + combines both lists
- nums[:] updates original array without creating a new reference

 Time Complexity: O(n)
 Space Complexity: O(n)  (because a new list is created internally)
"""

# ---------------- METHOD 2: Using a Loop ----------------
nums = [3, 4, 4, 45, 3, 0, 10, 6, 7]
n = len(nums)

"""
Technique: In-place rotation using a temporary variable
- Store the last element in a temp variable.
- Shift all elements from right to left by one index.
- Place the temp element at the first position.
"""

temp = nums[n - 1]       # store the last element
for i in range(n - 2, -1, -1):  # start from second last to 0
    nums[i + 1] = nums[i]      # shift elements right
nums[0] = temp                 # put the last element at first index

print("After rotation using loop:", nums)

""""
 Behind the scenes:
Suppose nums = [3, 4, 4, 45, 3, 0, 10, 6, 7]
- temp = 7
- shifting starts from i = 7 down to i = 0
  so nums[8] = nums[7], nums[7] = nums[6], ... until nums[1] = nums[0]
- finally nums[0] = temp (7)
Result → [7, 3, 4, 4, 45, 3, 0, 10, 6]

 Time Complexity: O(n)
 Space Complexity: O(1)  (in-place rotation using only one variable)
"""
