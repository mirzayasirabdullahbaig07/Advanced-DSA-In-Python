# ---------------------------------------------
# Recursion using parameters - Examples
# ---------------------------------------------

# Example 1: Print x, n times using recursion
def print_x_n_times(x, n):
    if n == 0:
        return
    print(x)
    print_x_n_times(x, n - 1)

print("Example 1: Print x, n times")
print_x_n_times(15, 4)

print("--------------")

# Example 2: Print 1 to n using head recursion
# Head Recursion: Do the job before recursive call
def print_1_to_n_head(i, n):
    if i > n:
        return
    print(i)
    print_1_to_n_head(i + 1, n)

print("Example 2: Print 1 to n (head recursion)")
print_1_to_n_head(1, 4)

print("--------------")

# Example 3: Print 1 to n using tail recursion (backtracking)
# Tail Recursion: Do the recursive call first, then the job
def print_1_to_n_tail(i, n):
    if i > n:
        return
    print_1_to_n_tail(i + 1, n)
    print(i)

print("Example 3: Print 1 to n (tail recursion - backtracking)")
print_1_to_n_tail(1, 4)

print("--------------")

# Example 4: Print n to 1 using tail recursion (backtracking)
def print_n_to_1_tail(i, n):
    if i > n:
        return
    print_n_to_1_tail(i + 1, n)
    print(i)

print("Example 4: Print n to 1 (tail recursion - backtracking)")
print_n_to_1_tail(1, 4)

print("--------------")

# Example 5: Print n to 1 using head recursion
def print_n_to_1_head(n):
    if n == 0:
        return
    print(n)
    print_n_to_1_head(n - 1)

print("Example 5: Print n to 1 (head recursion)")
print_n_to_1_head(4)
