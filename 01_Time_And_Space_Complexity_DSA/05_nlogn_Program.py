# N log N Time Complexity Programs (Loop and Recursion)
# -----------------------------------------------------
# These programs demonstrate O(n log n) time complexity through both loops and recursion.
# Common in divide-and-conquer algorithms like Merge Sort and Quick Sort.


# ------------------ LOOP BASED (O(n log n)) ------------------

# Program 1: Nested loop with log steps
import math

def loop_nlogn_1(n):
    for i in range(n):
        j = 1
        while j < n:
            print(i, j)
            j *= 2
# Time: O(n log n), Space: O(1)


# Program 2: Log loop inside outer loop

def loop_nlogn_2(n):
    for i in range(n):
        k = n
        while k > 1:
            print(i, k)
            k = k // 2
# Time: O(n log n), Space: O(1)


# Program 3: Multiplying inner loop

def loop_nlogn_3(n):
    for i in range(n):
        x = 1
        while x < n:
            print(i, x)
            x *= 3
# Time: O(n log n), Space: O(1)


# Program 4: Log reduction inside loop

def loop_nlogn_4(n):
    for i in range(n):
        val = n
        while val > 1:
            print(val)
            val //= 2
# Time: O(n log n), Space: O(1)


# Program 5: Outer loop + log inner loop base 10

def loop_nlogn_5(n):
    for i in range(n):
        count = 1
        while count <= n:
            print(i, count)
            count *= 10
# Time: O(n log n), Space: O(1)


# Program 6: Classic pattern

def loop_nlogn_6(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            print(i, j)
# Time: O(n log n), Space: O(1)


# Program 7: Bit shift based log loop

def loop_nlogn_7(n):
    for i in range(n):
        b = 1
        while b < n:
            print(i, b)
            b <<= 1
# Time: O(n log n), Space: O(1)


# Program 8: Increasing power

def loop_nlogn_8(n):
    for i in range(n):
        j = 1
        while j <= n:
            print(j)
            j = j * 2
# Time: O(n log n), Space: O(1)


# Program 9: Double while loop

def loop_nlogn_9(n):
    for i in range(n):
        y = n
        while y > 1:
            print(i, y)
            y //= 2
# Time: O(n log n), Space: O(1)


# Program 10: Combined decrement and multiplication

def loop_nlogn_10(n):
    for i in range(n):
        j = 1
        while j <= n:
            print(i + j)
            j *= 2
# Time: O(n log n), Space: O(1)



# ------------------ RECURSION BASED (O(n log n)) ------------------

# Program 1: Merge Sort Style

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
# Time: O(n log n), Space: O(n)


# Program 2: Quick Sort Partition

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
# Time: O(n log n), Space: O(n)


# Program 3: Balanced Recursion Tree

def balanced_recurse(n):
    if n <= 1:
        return
    balanced_recurse(n // 2)
    balanced_recurse(n // 2)
# Time: O(n log n), Space: O(log n)


# Program 4: Divide List and Process

def divide_and_log(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    divide_and_log(arr[:mid])
    divide_and_log(arr[mid:])
# Time: O(n log n), Space: O(log n)


# Program 5: Recursive Halving with Work

def halve_and_work(n):
    if n <= 1:
        return
    for i in range(n):
        print(i)
    halve_and_work(n // 2)
# Time: O(n log n), Space: O(log n)


# Program 6: String Merge Recursion

def merge_string(s):
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    left = merge_string(s[:mid])
    right = merge_string(s[mid:])
    return left + right
# Time: O(n log n), Space: O(log n)


# Program 7: Modified Merge with Side Print

def merge_side_work(arr):
    if len(arr) <= 1:
        return arr
    print("Splitting:", arr)
    mid = len(arr) // 2
    left = merge_side_work(arr[:mid])
    right = merge_side_work(arr[mid:])
    return left + right
# Time: O(n log n), Space: O(log n)


# Program 8: Recursively Divide with Print

def log_work(n):
    if n <= 1:
        return
    print("Working at", n)
    log_work(n // 2)
    log_work(n // 2)
# Time: O(n log n), Space: O(log n)


# Program 9: Hybrid Recursive Logging

def recurse_log(n):
    if n <= 1:
        return
    for i in range(n):
        print(i)
    recurse_log(n // 2)
# Time: O(n log n), Space: O(log n)


# Program 10: Divide with Counting

def divide_count(n):
    if n <= 1:
        return
    divide_count(n // 2)
    divide_count(n // 2)
    print(n)
# Time: O(n log n), Space: O(log n)
