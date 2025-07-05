# frequency_map_example.py

# ✅ Goal:
# Count the frequency of each number in the list using two methods

nums = [1, 2, 4, 5, 6, 4, 3, 3, 2, 8, 7, 111]

# -----------------------------
# 🟩 Method 1: Manual Dictionary Update (if-else)
# -----------------------------
x = 1  # number to check frequency of
frequency_map = dict()

for i in range(0, len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]] += 1
    else:
        frequency_map[nums[i]] = 1

print("Method 1 - Manual if-else")
print(f"Frequency of {x}:", frequency_map[x])

# Time complexity: O(n)
# Space complexity: O(n)

# -----------------------------
# 🟩 Method 2: Using dict.get()
# -----------------------------
hash_map = {}
n = len(nums)

for i in range(0, n):
    # dict.get(key, default) returns value if key exists, else default
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print("\nMethod 2 - Using dict.get()")
print(f"Frequency of {x}:", hash_map[x])

# Time complexity: O(n)
# Dictionary operations: add, delete, update, access => O(1) average case
