# ----------------------------------------------
# HASHING IN PYTHON – FULL EXPLANATION & EXAMPLES
# ----------------------------------------------

# What is Hashing?
# Hashing is a method of mapping data to fixed-size values (hash values).
# It's used for fast data access, lookups, counting frequency, etc.

# Why Use Hashing?
# - To reduce time complexity to O(1) for lookups
# - To avoid nested loops (O(n × m))
# - To count frequencies of elements efficiently
# - To implement data structures like sets and dictionaries

# -----------------------------------------------
# Example 1: Integer Frequency Hashing
# -----------------------------------------------

# Problem:
# Count how many times each number in list `m` appears in list `n`.

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 1, 5, 67, 2]

# Brute Force Solution (Time Limit Exceeded for large input)
# Time Complexity: O(n * m), Space: O(1)
for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(count)

# Optimal Solution Using List Hashing (when values are in known small range)
# Time: O(n + m), Space: O(1) for fixed size list
hash_list = [0] * 11  # Assuming numbers are in range 1 to 10

for num in n:
    hash_list[num] += 1

for num in m:
    if 1 <= num <= 10:
        print(hash_list[num])
    else:
        print(0)

# Optimal Solution Using Dictionary (general purpose for large or unknown values)
# Time: O(n + m), Space: O(k) where k is number of unique elements in n
freq_map = {}

for num in n:
    freq_map[num] = freq_map.get(num, 0) + 1

for num in m:
    print(freq_map.get(num, 0))

# -----------------------------------------------
# Example 2: Character Frequency Hashing
# -----------------------------------------------

# Problem:
# Count frequency of characters from a string using hashing

s = "azyxyyzaaaaa"
q = ["a", "a", "y", "x"]

# Optimal Using List (only for lowercase a-z)
# Time: O(s + q), Space: O(1) since list is fixed at size 26
hash_list = [0] * 26  # One slot for each letter a-z

for ch in s:
    index = ord(ch) - ord('a')  # convert 'a' to 0, 'b' to 1, ...
    hash_list[index] += 1

for ch in q:
    index = ord(ch) - ord('a')
    print(hash_list[index])

#  Optimal Using Dictionary (works for any characters including digits, symbols)
freq_map = {}

for ch in s:
    freq_map[ch] = freq_map.get(ch, 0) + 1

for ch in q:
    print(freq_map.get(ch, 0))

# -----------------------------------------------
# Summary Table

# | Approach          | Time Complexity | Space Complexity | Flexibility          |
# |-------------------|-----------------|------------------|----------------------|
# | Brute Force       | O(n × m)        | O(1)             | Low                  |
# | List Hashing      | O(n + m)        | O(k) fixed       | Limited to ranges    |
# | Dictionary Hashing| O(n + m)        | O(k) dynamic     | High (generic usage) |

# Use List Hashing when range of values is small and known.
# Use Dictionary Hashing when values are large, unknown, or characters.
