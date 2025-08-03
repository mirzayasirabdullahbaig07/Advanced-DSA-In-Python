# Quadratic Time Complexity Programs (O(n^2)) Using Loop and Recursion
# Definition:
# The execution time increases proportionally to the square of the input size.
# Commonly seen in nested loops or recursive calls with nested behavior.


# -----------------------------
# Programs Using Loops (O(n^2))
# -----------------------------

# Program 1: Nested Loop Print (Easy)
def nested_loop_print(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
# Explanation: Prints all pairs (i, j)
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Program 2: Multiplication Table (Easy)
def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i}*{j}={i*j}")
# Explanation: Prints n x n multiplication table
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Program 3: Count Pairs (Medium)
def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print("Total pairs:", count)
# Explanation: Increments count for every (i,j)
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Program 4: Diagonal Elements of Matrix (Medium)
def diagonal_matrix(n):
    matrix = [[i * j for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                print(matrix[i][j])
# Explanation: Creates matrix, prints diagonal
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 5: Triangle Pattern (Medium)
def triangle_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
# Explanation: Nested loop for pattern
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Program 6: Matrix Addition (Medium)
def add_matrices(n):
    A = [[i for _ in range(n)] for i in range(n)]
    B = [[j for j in range(n)] for _ in range(n)]
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    print(result)
# Explanation: Adds two n x n matrices
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 7: Boolean Grid Fill (Hard)
def fill_grid(n):
    grid = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = True
    return grid
# Explanation: Fills grid with True
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 8: Print All Index Pairs (Medium)
def print_pairs(n):
    for i in range(n):
        for j in range(i, n):
            print(f"({i},{j})")
# Explanation: Prints upper triangular pairs
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Program 9: Nested Factor Multiplication (Hard)
def multiply_pairs(n):
    product = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            product *= (i + j)
    print(product)
# Explanation: Multiplies all pair sums
# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Program 10: Character Grid Creation (Medium)
def char_grid(n):
    grid = [['X' for _ in range(n)] for _ in range(n)]
    for row in grid:
        print(' '.join(row))
# Explanation: Prints n x n character grid
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# ---------------------------------
# Programs Using Recursion (O(n^2))
# ---------------------------------

# Program 11: Recursive Nested Calls (Easy)
def recursive_nested(i, j):
    if i == 0 or j == 0:
        return
    print(i, j)
    recursive_nested(i-1, j)
    recursive_nested(i, j-1)
# Explanation: Two recursive calls reducing i and j
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 12: Print Triangular Pattern Recursively (Medium)
def recursive_triangle(n, row=0):
    if row == n:
        return
    print('* ' * (row + 1))
    recursive_triangle(n, row + 1)
# Explanation: Prints triangle using recursion
# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Program 13: Count Recursive Pairs (Hard)
def count_recursive_pairs(n):
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        return 1 + helper(i-1, j) + helper(i, j-1)
    print(helper(n, n))
# Explanation: Recursive pair counting
# Time Complexity: O(2^n) but can be bounded for small grids to O(n^2)
# Space Complexity: O(n^2)


# Program 14: Sum of Matrix Recursively (Medium)
def sum_matrix(matrix, i=0, j=0):
    n = len(matrix)
    if i >= n:
        return 0
    if j >= n:
        return sum_matrix(matrix, i+1, 0)
    return matrix[i][j] + sum_matrix(matrix, i, j+1)
# Explanation: Sums matrix recursively
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 15: Recursive Grid Print (Medium)
def recursive_grid(n, i=0, j=0):
    if i >= n:
        return
    if j >= n:
        print()
        recursive_grid(n, i+1, 0)
        return
    print('*', end=' ')
    recursive_grid(n, i, j+1)
# Explanation: Prints grid using recursion
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 16: Recursive Upper Triangle (Medium)
def upper_triangle(i, j, n):
    if i >= n:
        return
    if j >= n:
        print()
        upper_triangle(i + 1, i + 1, n)
        return
    print(f"({i},{j})", end=' ')
    upper_triangle(i, j + 1, n)
# Explanation: Recursively prints upper triangle
# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Program 17: Recursively Fill 2D Array (Hard)
def fill_recursive(matrix, i=0, j=0):
    n = len(matrix)
    if i >= n:
        return
    if j >= n:
        fill_recursive(matrix, i+1, 0)
        return
    matrix[i][j] = i + j
    fill_recursive(matrix, i, j+1)
# Explanation: Recursively fills 2D grid
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 18: Recursive Combinations (Hard)
def combinations(n):
    def helper(i, j):
        if i == n or j == n:
            return 1
        return helper(i + 1, j) + helper(i, j + 1)
    print(helper(0, 0))
# Explanation: Computes grid combinations
# Time Complexity: O(2^n) → Approx O(n^2) for small values with DP
# Space Complexity: O(n^2)


# Program 19: Spiral Fill Recursively (Hard)
# Note: Demonstrative logic, not actual spiral

def dummy_spiral(matrix, i=0, j=0):
    n = len(matrix)
    if i >= n or j >= n:
        return
    matrix[i][j] = i * j
    dummy_spiral(matrix, i + 1, j)
    dummy_spiral(matrix, i, j + 1)
# Explanation: Dummy spiral fill
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)


# Program 20: Nested Recursion with Base Limit (Hard)
def nested(n):
    def inner(i, j):
        if i == 0 or j == 0:
            return 1
        return inner(i-1, j) + inner(i, j-1)
    print(inner(n, n))
# Explanation: Nested structure like Pascal’s triangle
# Time Complexity: O(n^2) approx with memoization
# Space Complexity: O(n^2)
