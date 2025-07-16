# What is Palindrome Recursion?
# Nitin is palindrome
# maham is palindrome
# madam is palindrome
# abcddcba is palindrome


# now do it first using loop

def palindrome(s, left, right):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

s = input("Enter a string: ").lower()  # for case-insensitive check
if palindrome(s, 0, len(s) - 1):
    print("It is palindrome (loop)")
else:
    print("It is not palindrome (loop)")



# now do it using recursion

def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False

    return func(s, left + 1, right - 1)

s = input("Enter a string: ").lower()
if func(s, 0, len(s) - 1):
    print("It is palindrome (recursion)")
else:
    print("It is not palindrome (recursion)")
