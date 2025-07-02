# Extraction of Digits using Loop (One of the Best Core Concepts in Python DSA)

# Problem:
# Given a number `n`, extract and print each digit from last to first (i.e., reverse order).

# Example:
# Input: n = 5873
# Output: 3 7 8 5

# Key Concept:
# - The **last digit** of a number can be obtained using **modulus (%)** with 10
# - The **remaining digits** can be obtained using **floor division (//)** with 10

# Breakdown:
# Step 1: 5873 % 10 = 3  → last digit
# Step 2: 5873 // 10 = 587
# Step 3: 587 % 10 = 7   → next digit
# Step 4: 587 // 10 = 58
# Step 5: 58 % 10 = 8    → next digit
# Step 6: 58 // 10 = 5
# Step 7: 5 % 10 = 5     → last digit
# Step 8: 5 // 10 = 0    → loop ends

# Python Code
n = 5873                        # Input number
num = n                         # Store original number (optional, for backup/reference)

while num > 0:                  # Continue loop until number becomes 0
    last_digit = num % 10       # Extract the last digit using modulus
    print(last_digit, end=" ")  # Print the digit (in reverse order)
    num = num // 10             # Remove the last digit using floor division

# Output: 3 7 8 5
