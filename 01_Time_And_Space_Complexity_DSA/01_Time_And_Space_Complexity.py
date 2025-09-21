# Time Complexity and Space Complexity
# ----------------------------------
# Both measure an algorithm’s efficiency.
# - Time complexity shows how the running time increases with input size.
# - Space complexity tracks memory usage.
#
# Both are essential for optimizing algorithms, especially when dealing with large datasets or limited resources.
#
# In this article, we will explore these two concepts of algorithm analysis,
# along with their examples, cases, best practices, and more.

# -----------------------------------------------------
# What is Time Complexity?
# -----------------------------------------------------
# When solving a problem, there may be multiple approaches (codes) to achieve the desired result.
# The concept of time complexity helps us evaluate & compare these approaches.
#
# It allows us to determine which one is more efficient. It’s a crucial metric that often becomes
# a key focus during technical interviews because it demonstrates the effectiveness of a solution.
#
# Time complexity measures how the time required to execute a code changes as the size of the input grows.
# It is independent of the machine used to execute the code & focuses solely on the algorithm’s behavior.

# -----------------------------------------------------
# Example 1: Simple While Loop
# -----------------------------------------------------
i = 1
while i <= 5:
    print("Code and Debug")
    i += 1

# Step Analysis:
# Initialization → Comparison → Execution → Increment → Repeat.
# The loop runs 5 times.
# For each iteration → 3 steps.
# Total steps = 5 × 3 = 15 → O(N) after ignoring constants.

# -----------------------------------------------------
# Why Not Use Machine Time?
# -----------------------------------------------------
# - Different machines have different execution speeds.
# - Evaluating code only by machine execution time is unreliable.

# -----------------------------------------------------
# Rules for Calculating Time Complexity
# -----------------------------------------------------
# 1. Always analyze the worst-case scenario.
# 2. Ignore constant factors.
# 3. Focus on growth rate.

# -----------------------------------------------------
# Example 2: Grading System
# -----------------------------------------------------
marks = int(input("Enter your marks = "))

if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
elif marks >= 50 and marks < 60:
    print("E")
else:
    print("Fail")

# Best Case: 3 steps (input, condition, print)
# Worst Case: 7 steps (input + 5 conditions + else)
# Average Case: depends on distribution of marks
# Worst-case Time Complexity = O(k), where k = number of conditions.

# -----------------------------------------------------
# Ignoring Constants Example
# -----------------------------------------------------
# T(N) = 5N^10 + 8N^3 + 2
# For very large N → Dominant term = N^10 → Time Complexity = O(N^10)

# -----------------------------------------------------
# What is Space Complexity?
# -----------------------------------------------------
# Space complexity refers to the amount of memory required by a program during execution.
#
# Components:
# - Input Space → memory for input data.
# - Auxiliary Space → temporary memory for variables, data structures, stacks.

# Example:
a = int(input())  # Input Space
b = int(input())  # Input Space
c = a + b         # Auxiliary Space
print(c)
# Total variables used = 3 → Space Complexity = O(1)

# If using an array of size N → Space Complexity = O(N).

# -----------------------------------------------------
# Good Coding Practice:
# -----------------------------------------------------
# - Do not modify inputs directly just to reduce space.
# - Always prioritize clarity & integrity of code.

# -----------------------------------------------------
# Competitive Programming Guidelines
# -----------------------------------------------------
# - Online servers handle about 10^8 operations per second.
# - For 2s time limit → ≤ 2 × 10^8 operations.
# - Always aim for O(10^8) operations or lower.

# -----------------------------------------------------
# Conclusion
# -----------------------------------------------------
# By understanding and optimizing both time complexity and space complexity:
# - You write efficient, scalable code.
# - Maintain input integrity unless explicitly allowed.
# - Be mindful of execution constraints in coding platforms.
# - These skills improve coding interviews and real-world problem solving.
