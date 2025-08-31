# Exponential Time Complexity
# Definition:
# The runtime of the algorithm grows exponentially with the input size. Common form is O(2^n).

# ----------------------------------------------------------
# 10 Programs using Recursion (O(2^n))
# ----------------------------------------------------------

# Program 1: Fibonacci (Recursive)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# Time: O(2^n), Space: O(n)

# Program 2: Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)
# Time: O(2^n), Space: O(n)

# Program 3: All Binary Strings of Length n
def generate_binary(n, s=""):
    if n == 0:
        print(s)
        return
    generate_binary(n-1, s + "0")
    generate_binary(n-1, s + "1")
# Time: O(2^n), Space: O(n)

# Program 4: Subset Generation
def generate_subsets(arr, i=0, subset=[]):
    if i == len(arr):
        print(subset)
        return
    generate_subsets(arr, i+1, subset)
    generate_subsets(arr, i+1, subset + [arr[i]])
# Time: O(2^n), Space: O(n)

# Program 5: Permutations (Factorial but often exponential in nature)
def permutations(s, l=0):
    if l == len(s):
        print(''.join(s))
    else:
        for i in range(l, len(s)):
            s[l], s[i] = s[i], s[l]
            permutations(s, l + 1)
            s[l], s[i] = s[i], s[l]
# Time: O(n!), Space: O(n)

# Program 6: Count Ways to Climb Stairs (1, 2 steps)
def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n-1) + count_ways(n-2)
# Time: O(2^n), Space: O(n)

# Program 7: Boolean Parenthesization Problem
def count_parenthesis_ways(expr, i, j, isTrue):
    if i > j:
        return 0
    if i == j:
        if isTrue:
            return 1 if expr[i] == 'T' else 0
        else:
            return 1 if expr[i] == 'F' else 0
    ways = 0
    for k in range(i+1, j, 2):
        leftT = count_parenthesis_ways(expr, i, k-1, True)
        leftF = count_parenthesis_ways(expr, i, k-1, False)
        rightT = count_parenthesis_ways(expr, k+1, j, True)
        rightF = count_parenthesis_ways(expr, k+1, j, False)
        op = expr[k]
        if isTrue:
            if op == '&':
                ways += leftT * rightT
            elif op == '|':
                ways += leftT * rightT + leftT * rightF + leftF * rightT
            elif op == '^':
                ways += leftT * rightF + leftF * rightT
        else:
            if op == '&':
                ways += leftF * rightF + leftF * rightT + leftT * rightF
            elif op == '|':
                ways += leftF * rightF
            elif op == '^':
                ways += leftT * rightT + leftF * rightF
    return ways
# Time: O(2^n), Space: O(n)

# Program 8: K-th Symbol in Grammar
def kth_symbol(n, k):
    if n == 1:
        return 0
    mid = 2**(n-1) // 2
    if k <= mid:
        return kth_symbol(n-1, k)
    return 1 - kth_symbol(n-1, k-mid)
# Time: O(n), Space: O(n)

# Program 9: All Combinations of Balanced Parentheses
def generate_parenthesis(n, s='', open=0, close=0):
    if len(s) == 2 * n:
        print(s)
        return
    if open < n:
        generate_parenthesis(n, s + '(', open + 1, close)
    if close < open:
        generate_parenthesis(n, s + ')', open, close + 1)
# Time: O(2^n), Space: O(n)

# Program 10: Exponentiation by Doubling (not exponential, but classic power)
def exponential_brute(a, b):
    if b == 0:
        return 1
    return a * exponential_brute(a, b-1)

# Time: O(b), Space: O(b) (if b = n, linear. if optimized, O(log n))
