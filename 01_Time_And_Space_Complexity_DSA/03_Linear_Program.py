# Linear Time Complexity using Loop (O(n))
# Definition:
# The execution time grows linearly with the input size n. Each element is visited once.


# Program 1: Print All Elements (Easy)
def print_all(arr):
    for x in arr:
        print(x)
# What it does: Prints all elements in the list.
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 2: Find Maximum in List (Easy)
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    print("Max:", max_val)
# What it does: Finds the maximum number in list.
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 3: Count Occurrences (Easy)
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    print("Count:", count)
# What it does: Counts how many times target appears.
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 4: Sum of Elements (Easy)
def sum_elements(arr):
    total = 0
    for x in arr:
        total += x
    print("Sum:", total)
# What it does: Adds all values in array.
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 5: Copy Array (Medium)
def copy_array(arr):
    new_arr = []
    for val in arr:
        new_arr.append(val)
    print("Copied:", new_arr)
# What it does: Creates a new list from old one.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 6: Linear Search (Medium)
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Found at index:", i)
            return
    print("Not Found")
# What it does: Searches for key in array.
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 7: Convert to Uppercase (Medium)
def to_uppercase(strings):
    for s in strings:
        print(s.upper())
# What it does: Converts each string to uppercase.
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 8: Count Even Numbers (Easy)
def count_even(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:
            count += 1
    print("Even count:", count)
# What it does: Counts even numbers in the list.
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 9: Print Pairs with One Loop (Hard)
def print_pairs(arr):
    for x in arr:
        print(f"({x}, {x})")
# What it does: Prints pairs (same element twice).
# Time Complexity: O(n)
# Space Complexity: O(1)


# Program 10: Remove Negatives (Hard)
def remove_negatives(arr):
    positive = []
    for num in arr:
        if num >= 0:
            positive.append(num)
    print("Positives:", positive)
# What it does: Filters out negative numbers.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Linear Time Complexity with Recursion (O(n))
# Definition:
# The time taken grows linearly with the input size.


# Program 1: Print numbers from 1 to n (Easy)
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
# What it does: Prints numbers from 1 to n recursively.
# Time Complexity: O(n)
# Space Complexity: O(n) due to call stack


# Program 2: Sum of first n natural numbers (Easy)
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
# What it does: Recursively sums numbers from 1 to n.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 3: Count digits of a number (Medium)
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
# What it does: Counts number of digits in integer.
# Time Complexity: O(n) where n is number of digits
# Space Complexity: O(n)


# Program 4: Find max in list (Medium)
def find_max(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max(arr, n - 1))
# What it does: Recursively finds max in list.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 5: Print characters of a string (Easy)
def print_chars(s):
    if s == "":
        return
    print(s[0])
    print_chars(s[1:])
# What it does: Prints all characters in string.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 6: Reverse a string recursively (Medium)
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]
# What it does: Reverses a string using recursion.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 7: Recursively print elements of a list (Easy)
def print_list_elements(lst):
    if not lst:
        return
    print(lst[0])
    print_list_elements(lst[1:])
# What it does: Recursively prints list elements.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 8: Check if a string is palindrome (Medium)
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
# What it does: Checks if string is palindrome.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 9: Find factorial using recursion (Easy)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
# What it does: Calculates factorial of n.
# Time Complexity: O(n)
# Space Complexity: O(n)


# Program 10: Recursively copy a list (Hard)
def copy_list(lst):
    if not lst:
        return []
    return [lst[0]] + copy_list(lst[1:])
# What it does: Creates a copy of list recursively.
# Time Complexity: O(n)
# Space Complexity: O(n)
