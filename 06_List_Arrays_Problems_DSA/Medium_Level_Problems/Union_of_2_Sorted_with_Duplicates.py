# Union of Two Sorted Arrays | Optimal Solution using Two-Pointer Technique

def sortedArray(a: [int], b: [int]) -> [int]:
    """
     Problem Statement:
    Given two sorted arrays a[] and b[] (which may contain duplicates),
    return a sorted list containing all distinct elements present in either array.

    Example:
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 6, 7]
    Output → [1, 2, 3, 4, 5, 6, 7]
    """

    # Initialize two pointers for both arrays
    i = 0
    j = 0
    result = []

    """
     Technique Used: Two-Pointer Approach
    --------------------------------------------------------
    - Both arrays are already sorted.
    - Use two pointers `i` and `j` to traverse both arrays simultaneously.
    - At each step:
        - Compare a[i] and b[j].
        - Append the smaller value to the result if it's not a duplicate.
        - Move the pointer forward in the array from which the element was taken.
    - This method ensures sorted order and avoids duplicates efficiently.
    """

    # Traverse both arrays simultaneously
    while i < len(a) and j < len(b):

        # Case 1: When current element in a <= current element in b
        if a[i] <= b[j]:
            """
             Behind the Scenes:
            - If a[i] <= b[j], then a[i] should be considered first.
            - But before appending, check whether it's already added (avoid duplicates).
            """
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1  # move pointer in a forward

        # Case 2: When b[j] < a[i]
        else:
            """
             Behind the Scenes:
            - If b[j] is smaller, it comes earlier in sorted order.
            - Append b[j] if it's not a duplicate.
            """
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1  # move pointer in b forward

    # Process any remaining elements in a[]
    while i < len(a):
        """
         After main traversal:
        - If a[] still has remaining elements, add them (without duplicates).
        """
        if len(result) == 0 or result[-1] != a[i]:
            result.append(a[i])
        i += 1

    # Process any remaining elements in b[]
    while j < len(b):
        """
         Similarly, add remaining elements from b[].
        """
        if len(result) == 0 or result[-1] != b[j]:
            result.append(b[j])
        j += 1

    # Return the final sorted union array
    return result


# -------------------------- DRY RUN --------------------------
"""
Example:
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

Step-by-step:
i=0, j=0 → a[i]=1, b[j]=1 → add 1 → i=1
i=1, j=0 → a[i]=2, b[j]=1 → add 2 → j=1
i=1, j=1 → both 2 → add once → i=2, j=2
...
continue until both arrays are done.
Result = [1, 2, 3, 4, 5, 6, 7]
"""

# -------------------------- TEST CASES --------------------------
print(sortedArray([1, 2, 3, 4, 5], [1, 2, 3, 6, 7]))  # [1, 2, 3, 4, 5, 6, 7]
print(sortedArray([2, 2, 3, 4, 5], [1, 1, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sortedArray([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]))  # [1, 2]
print(sortedArray([], [1, 2, 3]))                     # [1, 2, 3]
print(sortedArray([1, 2, 3], []))                     # [1, 2, 3]


# -------------------------- COMPLEXITY ANALYSIS --------------------------
"""
 Time Complexity: O(n + m)
----------------------------------------
- Each element of array a and b is traversed at most once.
- Hence, total time = n + m operations.

Space Complexity: O(n + m)
----------------------------------------
- In the worst case (no duplicates), all elements from both arrays
  are stored in the result list.

 Summary:
----------------------------------------
Technique Used: Two-Pointer Merge Technique
Type: Optimal and In-Place Traversal
Efficient For: Sorted Arrays
Stable: Yes (maintains sorted order)
Avoids: Duplicates using last element check
"""
