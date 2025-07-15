# ================================================================
# Recursion: Parameterized vs Functional
# ================================================================

# ------------------------------------------------
# What is Parameterized Recursion?
# ------------------------------------------------
# - In parameterized recursion, we pass extra parameters to carry
#   state or computation (like running sum, product, etc.) through
#   the recursive calls.
# - The final result is usually printed or used inside the function
#   and is NOT returned.

# Example: Sum of 1 to n using Parameterized Recursion

def func_param(sum, i, n):
    # Base condition: when i exceeds n, print the sum
    if i > n:
        print("Parameterized Sum:", sum)
        return
    # Recursive call: add current i to sum and increase i
    func_param(sum + i, i + 1, n)

func_param(0, 1, 4)  # Output: Parameterized Sum: 10


# ------------------------------------------------
# What is Functional Recursion?
# ------------------------------------------------
# - In functional recursion, each function call returns a value.
# - The return values are used to compute the final result during
#   the **return phase** of recursion.
# - There’s always a base condition and a flow that returns data.

# Example: Sum of 1 to n using Functional Recursion

def func_return(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: return current n + result of func(n-1)
    return n + func_return(n - 1)

print("Functional Sum:", func_return(4))  # Output: Functional Sum: 10


# ------------------------------------------------
# Key Differences Between Both Types
# ------------------------------------------------
# | Feature              | Parameterized Recursion    | Functional Recursion        |
# |----------------------|--------------------------- |-----------------------------|
# | Result returned?     | No (printed inside)        | Yes (returned by function)  |
# | Parameters used      | Extra parameters (like sum)| Only necessary input        |
# | Logic flow           | During recursive calls     | During return phase         |
# | Typical use case     | Accumulating values        | Returning computed result   |

# ------------------------------------------------
# Time and Space Complexity
# ------------------------------------------------
# - Time Complexity: O(n)
# - Space Complexity: O(n)  (due to recursion stack)

# ------------------------------------------------
# Tip:
# Use parameterized recursion when you want to build up state
# as you go down the recursion stack.
# Use functional recursion when you want to return a final result
# and compose it on the way back up.
