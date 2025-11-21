'''
Problem
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

from typing import List

def sum_to_k(arr: list[int], k: int) -> bool:
    # Holds already seen values
    seen_vals = set()

    # Check list in O(N) time and space complexity.
    for num in arr:
        if k-num in seen_vals:
            return True
        seen_vals.add(num)
    return False

# List of test cases: (nums, k, expected_result, description)
test_cases = [
    # 1. Standard Cases
    ([10, 15, 3, 7], 17, True,  "Standard Example (10 + 7)"),
    ([10, 15, 3, 7], 20, False, "No valid pair exists"),

    # 2. Edge Cases
    ([], 5,             False, "Empty list"),
    ([5], 5,            False, "Single element (needs two numbers)"),
    ([1, 2, 3], 100,    False, "Target much larger than any sum"),
    
    # 3. Duplicates & Self-Usage
    ([5, 2, 1], 10,     False, "Cannot use the same element twice (5+5)"),
    ([5, 5, 1], 10,     True,  "Can use duplicates if they exist (5+5)"),
    
    # 4. Negative Numbers & Zeros
    ([-5, 10, 3], 5,    True,  "Negative numbers (-5 + 10)"),
    ([0, 5, 3], 5,      True,  "Zero handling (0 + 5)"),
    ([0, 0], 0,         True,  "Double zeros"),
    ([-10, -20], -30,   True,  "Two negative numbers"),
]

print(f"{'Status':<10} | {'Expected':<10} | {'Result':<10} | {'Description'}")
print("-" * 80)

for nums, k, expected, desc in test_cases:
    result = sum_to_k(nums, k)
    status = "PASSED" if result == expected else "FAILED"
    print(f"{status:<10} | {str(expected):<10} | {str(result):<10} | {desc}")