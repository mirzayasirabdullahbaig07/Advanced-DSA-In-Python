# ================================================================
# Recursion: Reverse an Array
# ================================================================

# Problem:
# Reverse an array using recursion (no loops)

# Example:
# Input : [5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5]

# ------------------------------------------------
#  Recursive Approach
# ------------------------------------------------
# - Use two pointers: left (start) and right (end)
# - Swap elements at left and right
# - Move the pointers inward: left + 1, right - 1
# - Stop when left >= right (base case)

def reverse_array_recursive(nums, left, right):
    # Base condition
    if left >= right:
        return
    
    # Swap elements
    nums[left], nums[right] = nums[right], nums[left]
    
    # Recursive call
    reverse_array_recursive(nums, left + 1, right - 1)

# Wrapper function (optional)
def reverse_array(nums):
    reverse_array_recursive(nums, 0, len(nums) - 1)

# Example usage
nums = [5, 4, 3, 5, 4, 3, 2, 2, 4, 2]
reverse_array(nums)
print("Reversed Array:", nums)  # Output: [2, 4, 2, 2, 3, 4, 5, 3, 4, 5]

# ------------------------------------------------
# Time and Space Complexity
# ------------------------------------------------
# - Time Complexity:  O(n)     → where n = len(nums)
# - Space Complexity: O(n)     → due to recursion stack (n/2 calls)
