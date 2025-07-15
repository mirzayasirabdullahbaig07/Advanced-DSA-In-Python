# ================================================================
# Recursion: Factorial of a Number
# ================================================================

# ------------------------------------------------
# What is Factorial?
# ------------------------------------------------
# - The factorial of a number `n` (denoted as n!) is the product of
#   all positive integers less than or equal to `n`.
# - Example:
#     5! = 5 × 4 × 3 × 2 × 1 = 120

# ------------------------------------------------
# Recursive Flow for Factorial
# ------------------------------------------------
# - f(n) = n × f(n - 1)   ← Recursive relation
# - Base Cases:
#     f(0) = 1
#     f(1) = 1

# Recursive Implementation of Factorial

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n - 1)
    return n * factorial(n - 1)

# Example
print("Factorial of 5:", factorial(5))  # Output: 120

# ------------------------------------------------
# Time and Space Complexity
# ------------------------------------------------
# - Time Complexity:  O(n)      → n recursive calls
# - Space Complexity: O(n)      → due to call stack
