# Linear Time Complexity
# Definition: 
# The execution time grows linearly with the input size n. Each element is visited once.

# Program 1: Print All Elements (Easy)
def print_all(arr):
    for x in arr:
        print(x)
# What it does: Prints all elements in the list.
# Time Complexity: O(n) – Traverses each element once.
# Space Complexity: O(1)

# Program 2: Find Maximum in List (Easy)
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    print("Max:", max_val)
# What it does: Finds the maximum number in list.
# Time Complexity: O(n) – One scan of array.
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



# Constant Time Complexity with Recursion-like Behavior (O(1))
# Definition:
# The execution time does not depend on input size. Only one recursive call or fixed operations performed.


# Program 1: Recursive Hello Message (Easy)
def recursive_hello():
    print("Hello from recursion!")
# What it does: Just prints a message once.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 2: Recursive Sum with Base Value (Easy)
def base_case_sum():
    return 5 + 7
# What it does: Adds two constants.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 3: Fixed Recursive Call (Medium)
def call_once():
    def inner():
        print("Called inner once")
    inner()
# What it does: Calls an inner function once.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 4: Single-Level Recursive Return (Medium)
def single_return():
    def base():
        return 42
    print(base())
# What it does: Calls a base function once.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 5: Return Fixed Value Recursively (Easy)
def return_constant():
    def inner():
        return "AI"
    return inner()
# What it does: Returns fixed value through one call.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 6: Print Default Message via Nested Function (Medium)
def nested_print():
    def default():
        print("Default Message")
    default()
# What it does: Calls function with no loop/recursion.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 7: Conditional Exit (Hard to confuse but still O(1))
def condition_based():
    x = 10
    if x > 5:
        print("Greater than 5")
# What it does: Condition check and print.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 8: Recursive Call Prevention (Interesting)
def block_recursive():
    def check(flag):
        if flag:
            return "Skip recursion"
    print(check(True))
# What it does: Prevents further recursion using condition.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 9: Tuple Destructuring in Function (Medium)
def tuple_unpack():
    def unpack():
        a, b = (1, 2)
        print(a + b)
    unpack()
# What it does: Just unpacks and prints sum.
# Time Complexity: O(1)
# Space Complexity: O(1)


# Program 10: Fixed Recursive-style Evaluation (Medium)
def fixed_eval():
    def inner():
        return len("ML")
    print(inner())
# What it does: Evaluates length of fixed string.
# Time Complexity: O(1)
# Space Complexity: O(1)
