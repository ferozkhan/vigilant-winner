from typing import List


def remove_duplicates(arr: List[int]) -> int:
    """
    remove duplicates from given array.
    complexity: runtime O(n) | space O(1)
    """
    last_val = None
    j = 0
    for i in range(len(arr)):
        if arr[i] != last_val:
            last_val = arr[i]
            arr[j] = arr[i]
            j += 1
    return len(arr[:j])


assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]
assert remove_duplicates([1, 1, 2]) == [1, 2]