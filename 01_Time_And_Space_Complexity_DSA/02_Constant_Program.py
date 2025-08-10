# Constant Time Complexity (O(1))
# Definition:
# The execution time does not depend on the size of input.
# Even if the input grows, the number of operations remains constant.

# Program 1: Access first element
def access_first(arr):
    print(arr[0])
# What it does: Prints the first element of the list.
# Why O(1): Accessing a specific index in a list takes constant time, no matter the list size.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 2: Check if number is even
def is_even(num):
    print(num % 2 == 0)
# What it does: Checks if a given number is divisible by 2.
# Why O(1): A single modulus operation takes constant time, regardless of the number’s size.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 3: Swap two numbers
def swap_numbers(a, b):
    a, b = b, a
    print(a, b)
# What it does: Exchanges the values of two variables.
# Why O(1): Only a fixed number of assignments happen, independent of input size.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 4: Return sum of first and last element
def sum_first_last(arr):
    print(arr[0] + arr[-1])
# What it does: Adds the first and last elements of a list and prints the result.
# Why O(1): Accessing elements by index and adding them both take constant time.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 5: Fixed multiplication
def multiply_fixed():
    print(25 * 4)
# What it does: Multiplies two fixed numbers.
# Why O(1): The same number of operations are performed every time, regardless of any input.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 6: Compare two values
def compare_values(a, b):
    print(a > b)
# What it does: Checks if one value is greater than another.
# Why O(1): Comparison between two numbers is always constant time.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 7: Print a constant string
def constant_message():
    print("Hello World!")
# What it does: Prints the same message every time.
# Why O(1): Printing a fixed message requires the same operations each time.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 8: Access middle element
def middle_element(arr):
    print(arr[len(arr)//2])
# What it does: Finds and prints the middle element of a list.
# Why O(1): List indexing and integer division both happen in constant time.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 9: Calculate square of a number
def square_number(num):
    print(num * num)
# What it does: Calculates and prints the square of a given number.
# Why O(1): Multiplication takes constant time regardless of the number’s size.
# Time Complexity: O(1)
# Space Complexity: O(1)

# Program 10: Get dictionary value by key
def get_value(dictionary, key):
    print(dictionary[key])
# What it does: Retrieves and prints a value from a dictionary using its key.
# Why O(1): Dictionary lookups are constant time on average due to hashing.
# Time Complexity: O(1)
# Space Complexity: O(1)


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
