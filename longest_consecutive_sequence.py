"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


def find_longest_consecutive_element(arr):
    max_con_length = 0
    hash_map = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[j])
            if diff not in hash_map:
                hash_map[diff] = []
            if arr[i] not in hash_map[diff]:
                for x in hash_map[diff]:
                    if abs(x - arr[i]) == diff:
                        hash_map[diff].append(arr[i])
            if arr[j] not in hash_map[diff]:
                for x in hash_map[diff]:
                    if abs(x - arr[j]) == diff:
                        hash_map[diff].append(arr[j])
            max_con_length = max(max_con_length, len(hash_map[diff]))
    return max_con_length


# assert find_longest_consecutive_element([100, 4, 200, 1, 3, 2]) == 4
print(find_longest_consecutive_element([1, 2, 3, 5, 6]))# == 5
print(find_longest_consecutive_element([100, 4, 200, 1, 3, 2]))

