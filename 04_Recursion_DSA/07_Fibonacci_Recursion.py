# What is Fibonacci Number and how to solve using recursion?

# Recursive Function
def func(num):
    if num == 0 or num == 1:
        return num
    return func(num - 1) + func(num - 2)

# Main Caller Function (like in a class-based structure)
def fib(n: int) -> int:
    answer = func(n)
    return answer


# Example usage
num = int(input("Enter the number: "))
print("Fibonacci number is:", fib(num))

# Time Complexity: O(2^n) – exponential due to repeated calls
# Space Complexity: O(n) – due to recursion stack
