
# Count Digits - Loop Method

print("\n\n--- Counting Digits (Loop Method) ---")

n = 8239
num = n
count = 0

while num > 0:
    count += 1
    num = num // 10

print(f"Total digits in {n} = {count}")

# Time Complexity: O(log10(n))
# Space Complexity: O(1)


# ----------------------------------------------------------------------------------
# Count Digits - Logarithmic Method
# ----------------------------------------------------------------------------------

print("\n--- Counting Digits (Logarithmic Method) ---")

from math import log10

def count_digits(num):
    if num == 0:
        return 1  # log10(0) is undefined, but 0 has 1 digit
    return int(log10(num)) + 1

# Examples:
print(f"Digits in 8409: {count_digits(8409)}")      # 4
print(f"Digits in 844449: {count_digits(844449)}")  # 6
print(f"Digits in 409: {count_digits(409)}")        # 3

# Time Complexity: O(1)
# Space Complexity: O(1)

# Digit Extraction:
# - Use while loop with %10 and //10 to print digits in reverse order.
# - Time: O(log10(n)), Space: O(1)

# Digit Counting:
# - Loop Method: O(log10(n)), Space: O(1)
# - Log Method:  O(1),         Space: O(1)

# Logarithmic method is faster and cleaner but requires import.

# These are foundational DSA building blocks used in number theory, digit manipulation,
# and base conversions.
