# Logarithmic Time Complexity (O(log n))
# -------------------------------------------------------------
# In logarithmic time, the number of operations reduces significantly
# at each step, typically by half. This commonly occurs in binary search, 
# divide-and-conquer techniques, etc.

# -----------------------------
# Part 1: Using Loops (10 Programs)
# -----------------------------

# Program 1: Binary Search (Loop)
def binary_search_loop(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
# Time: O(log n), Space: O(1)

# Program 2: Divide Counter Loop
def divide_loop(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    print("Divisions:", count)
# Time: O(log n), Space: O(1)

# Program 3: Logarithmic Print
import math
def log_loop(n):
    i = 1
    while i < n:
        print("i:", i)
        i *= 2
# Time: O(log n), Space: O(1)

# Program 4: Remove Halves

def halve_list_loop(arr):
    while len(arr) > 1:
        arr = arr[:len(arr)//2]
        print(arr)
# Time: O(log n), Space: O(n) due to list slicing

# Program 5: Base-2 Logarithm Counter

def log_counter(n):
    print("Log base 2 of n is:", math.floor(math.log2(n)))
# Time: O(1), Space: O(1) but uses log internally

# Program 6: Bit Shift Counter

def bit_shift_loop(n):
    count = 0
    while n:
        n >>= 1
        count += 1
    print("Shifts:", count)
# Time: O(log n), Space: O(1)

# Program 7: Binary Length Counter

def binary_length(n):
    print("Binary length:", len(bin(n)) - 2)
# Time: O(log n), Space: O(1)

# Program 8: Count Halves until 1

def count_halves(n):
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    print("Steps to reach 1:", steps)
# Time: O(log n), Space: O(1)

# Program 9: Log Loop with Condition

def log_loop_cond(n):
    i = n
    while i >= 1:
        print(i)
        i //= 2
# Time: O(log n), Space: O(1)

# Program 10: Search in Power of Two

def power_two_search(n):
    i = 1
    while i <= n:
        if i == n:
            print("Found")
            return
        i *= 2
    print("Not Found")
# Time: O(log n), Space: O(1)


# -----------------------------
# Part 2: Using Recursion (10 Programs)
# -----------------------------

# Program 11: Binary Search (Recursive)
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)
# Time: O(log n), Space: O(log n) due to recursion stack

# Program 12: Recursive Halving

def halve_recursively(n):
    if n <= 1:
        return
    print(n)
    halve_recursively(n // 2)
# Time: O(log n), Space: O(log n)

# Program 13: Logarithmic Print Recursive

def print_log_recursive(i, n):
    if i >= n:
        return
    print(i)
    print_log_recursive(i * 2, n)
# Time: O(log n), Space: O(log n)

# Program 14: Count Halves Recursively

def count_halves_recursive(n):
    if n <= 1:
        return 0
    return 1 + count_halves_recursive(n // 2)
# Time: O(log n), Space: O(log n)

# Program 15: Bit Count Recursively

def count_bits_recursive(n):
    if n == 0:
        return 0
    return 1 + count_bits_recursive(n >> 1)
# Time: O(log n), Space: O(log n)

# Program 16: Log2 Calculation Recursively

def log2_recursive(n):
    if n <= 1:
        return 0
    return 1 + log2_recursive(n // 2)
# Time: O(log n), Space: O(log n)

# Program 17: Power of Two Check

def is_power_of_two(n):
    if n == 1:
        return True
    if n == 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)
# Time: O(log n), Space: O(log n)

# Program 18: Recursive Shift Count

def shift_count_recursive(n):
    if n == 0:
        return 0
    return 1 + shift_count_recursive(n >> 1)
# Time: O(log n), Space: O(log n)

# Program 19: Divide Until Base Case

def divide_until_one(n):
    if n <= 1:
        return
    print(n)
    divide_until_one(n // 2)
# Time: O(log n), Space: O(log n)

# Program 20: Recursive Power Search

def power_two_search_recursive(i, n):
    if i > n:
        print("Not Found")
        return
    if i == n:
        print("Found")
        return
    power_two_search_recursive(i * 2, n)
# Time: O(log n), Space: O(log n)

# -----------------------------
# End of Logarithmic Time Complexity Programs
# -----------------------------
