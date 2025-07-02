# ---------------------- 👨‍💻 Time Complexity & Space Complexity in Python DSA ----------------------

# ❌ WRONG DEFINITION (Common Misunderstanding):
# Time complexity is NOT the number of seconds a code takes to run.
# Example:
# - On a Mac, code takes 5 seconds.
# - On Windows 7, it takes 15 seconds.
# This isn't time complexity — it’s hardware performance!

# ✅ REAL DEFINITION:
# Time Complexity = Rate of increase in operations with respect to input size (n).
# We use Big-O notation (e.g., O(n), O(n²), O(log n)) to describe it.
# It shows the approximate growth pattern, not the exact execution time.

# Example:
for i in range(1, 6):
    print("yasir")
# The loop runs 5 times, each with 3 operations: check, print, increment.
# Total operations = 3 * 5 = 15 → Time complexity = O(n), not O(15)

# ---------------------- 🧠 Rules to Calculate Time Complexity ----------------------

# Rule 1: Always calculate time complexity in worst case (Big-O).
# Rule 2: Ignore constant values.
# Rule 3: Ignore lower-order terms.

# ---------------------- 🔥 Best, Average, and Worst Case ----------------------

# Example:
age = 100
if age >= 80:
    print("most senior citizen")
elif age >= 60 and age <= 80:
    print("senior")
elif age >= 24 and age < 60:
    print("working")
elif age >= 16 and age < 24:
    print("teenager")
else:
    print("babies")

# Best Case: age = 100 → 1 operation
# Average Case: age = 50 → 3 operations
# Worst Case: age = 10 → All conditions checked → 5 operations

# ❓ Why Worst Case?
# In real-world systems (e.g., websites with millions of users), we must ensure performance holds up under maximum load.

# ---------------------- 🚫 Avoid Constant Values ----------------------

# Example:
# O(8n⁶ + 3n² + 15)
# If n is very large (e.g., 10⁵), constants and lower terms are negligible.
# Final TC = O(n⁶)

# ---------------------- 🚫 Avoid Lower Bound ----------------------

# Example:
# Adding 100,000 to 1,000,000,000,000 has little effect → So, ignore small terms.

# ---------------------- 📊 Types of Time Complexity ----------------------

# Big-O     → Worst case (upper bound)
# Theta (θ) → Average case (tight bound)
# Omega (Ω) → Best case (lower bound)

# Interviewers usually expect Big-O (worst case) unless specified.

# ---------------------- 📌 Example: Nested Loop O(n²) ----------------------

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # some code
        pass

# i = 1 → j runs 1 to n
# i = 2 → j runs 1 to n
# Total operations = n * n = O(n²)

# ---------------------- 📌 Example: Triangular Loop ----------------------

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # some code
        pass

# j runs 1, 2, 3, ..., n → total = n(n+1)/2 = O(n²)

# ---------------------- 🧮 Space Complexity ----------------------

# Space Complexity = Total memory used
# Includes:
# - Input space (original inputs)
# - Auxiliary space (temporary variables/data structures)

# Example:
a = 2
b = 4
sum_ab = a + b
print(sum_ab)
# Input space: a, b
# Auxiliary space: sum_ab

# Example 2 (Bad Practice):
x = 2
y = 2
x = x + y  # modifying input space (not recommended)
print(x)
# ❌ Don't modify input space unless explicitly allowed

# ---------------------- 🚨 TLE — Time Limit Exceeded ----------------------

# Time limit on many platforms = 1 second = 10⁸ operations
# If your algorithm takes 10¹⁰ operations, it will take 100 seconds → TLE

# Example:
lst = [5, 8, 7, 6, 5, 1, 3]
# If you use bubble sort (O(n²)) and N = 10⁵:
# 10⁵ * 10⁵ = 10¹⁰ → Too slow!

# ---------------------- 🧠 Time Complexity of Python List Operations ----------------------

# Operation                 | Average      | Worst
# -------------------------|--------------|--------------
# Copy                     | O(n)         | O(n)
# Append                   | O(1)         | O(1)
# Pop (last)               | O(1)         | O(1)
# Pop (middle)             | O(n)         | O(n)
# Insert                   | O(n)         | O(n)
# Get item (lst[i])        | O(1)         | O(1)
# Set item (lst[i] = x)    | O(1)         | O(1)
# Delete item              | O(n)         | O(n)
# Iterate                  | O(n)         | O(n)
# Slice                    | O(k)         | O(k)
# Extend                   | O(k)         | O(k)
# Sort                     | O(n log n)   | O(n log n)
# Multiply lst*k           | O(nk)        | O(nk)
# x in lst                 | O(n)         | O(n)

# ---------------------- 🧠 Time Complexity of Set Operations ----------------------

# Operation                       | Average     | Worst
# -------------------------------|-------------|-------------
# x in s                         | O(1)        | O(n)
# s | t (Union)                  | O(len(s)+len(t))
# s & t (Intersection)           | O(min(s,t)) | O(len(s)*len(t))
# s - t (Difference)             | O(len(s))   | O(len(s))
# s ^ t (Symmetric Difference)   | O(len(s))   | O(len(s)*len(t))

# Example:
my_set = {5, 3, 2, 1, 10, 11, 15}
print(15 in my_set)  # O(1) average case

# ---------------------- 🧠 Time Complexity of Dictionary Operations ----------------------

# Operation               | Average      | Worst
# ------------------------|--------------|--------------
# k in d                  | O(1)         | O(n)
# Get item                | O(1)         | O(n)
# Set item                | O(1)         | O(n)
# Delete item             | O(1)         | O(n)
# Copy                    | O(n)         | O(n)
# Iterate                 | O(n)         | O(n)

# Example:
my_dict = {'a': 7, 'c': 10, 15: 20}
print('a' in my_dict)  # O(1)

# ---------------------- 🔚 Final Notes ----------------------

# ✅ Always assume Big-O (worst case) in interviews unless stated.
# ✅ Ignore constants and lower-order terms.
# ✅ Don't mutate input space unless asked.
# ✅ Know the complexity of built-in operations in Python.
# ✅ Time complexity is critical in competitive programming and real-world systems.
# ✅ Space complexity is also important in memory-limited environments.

# Let me know if you want this saved as a .py file or converted to GitHub-friendly markdown!
