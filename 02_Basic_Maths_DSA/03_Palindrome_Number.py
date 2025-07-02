 # Palindrome Number Check


print("\n--- Palindrome Number Check ---")

# A number is a palindrome if it reads the same forward and backward.
# Example: 12321 → reversed = 12321 → palindrome 
#          1234  → reversed = 4321  → not palindrome 

def is_palindrome(n):
    num = n
    result = 0
    while num > 0:
        last_digit = num % 10
        result = (result * 10) + last_digit
        num = num // 10
    return n == result

# Example check
print(f"Is 1234 a palindrome? {is_palindrome(1234)}")    # False
print(f"Is 1221 a palindrome? {is_palindrome(1221)}")    # True

# Time Complexity: O(log10(n))
# Space Complexity: O(1)


# Palindrome Check:
# - Reverse number using digit extraction and compare.
# - Time: O(log10(n)), Space: O(1)
#
# These are foundational DSA building blocks used in number theory, digit manipulation,
# and base conversions.
