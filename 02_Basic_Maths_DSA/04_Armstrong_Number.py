# Armstrong Number Check

print("\n--- Armstrong Number Check ---")

# An Armstrong number is a number that is equal to the sum of its own digits
# each raised to the power of the number of digits.
# Example: 153 → 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 → Armstrong

def is_armstrong(n):
    num = n
    total = 0
    nod = len(str(n))     # Count number of digits
    while num > 0:
        digit = num % 10
        total += digit ** nod
        num = num // 10
    return total == n

# Example check
print(f"Is 153 an Armstrong number? {is_armstrong(153)}")    # True
print(f"Is 154 an Armstrong number? {is_armstrong(154)}")    # False

# Time Complexity: O(log10(n))
# Space Complexity: O(1)

# Armstrong Number:
# - Raise each digit to the power of total number of digits and sum them.
# - Time: O(log10(n)), Space: O(1)

