# -------------------------
# Approach 1: Brute-Force
# -------------------------
# Check all numbers from 1 to 'number' to find factors

number = 10
result = []

for i in range(1, number + 1):
    if number % i == 0:
        result.append(i)

print("Factors (Brute-force):", result)

# Time Complexity: O(n)
# Space Complexity: O(k)  where k = number of factors



# -------------------------
# Approach 2: Better Approach
# -------------------------
# Factors of a number cannot be more than n//2 (except the number itself)
# So, we loop only from 1 to n//2 and then add the number itself at the end

number = 20
result = []

for i in range(1, number // 2 + 1):
    if number % i == 0:
        result.append(i)

result.append(number)  # the number itself is always a factor

print("Factors (Better):", result)

# Time Complexity: O(n/2) ≈ O(n)
# Space Complexity: O(k)



# -------------------------
# Approach 3: Optimal Approach using sqrt(n)
# -------------------------
# Factors always appear in pairs (i, number // i)
# So we only loop till sqrt(number) to find all factor pairs

from math import sqrt

number = 36
result = []

for i in range(1, int(sqrt(number)) + 1):
    if number % i == 0:
        result.append(i)
        if number // i != i:  # Avoid adding square root twice
            result.append(number // i)

result.sort()  # Optional: to return factors in sorted order

print("Factors (Optimal):", result)

# Time Complexity: O(√n)
# Space Complexity: O(k)
