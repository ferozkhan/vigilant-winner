from typing import List


def check_position(arr: List[int]) -> int:
    """ function check and return positions not in ordered
    or items required move to bring sequence in order.
    algorithm runs in O(nlogn) and O(n) space.
    """
    not_in_place = 0
    if not arr:
        return not_in_place

    ordered_arr = arr.copy()
    ordered_arr.sort()
    for i in range(0, len(arr)):
        if ordered_arr[i] != arr[i]:
            not_in_place += 1
    return not_in_place



assert check_position([1,1,4,2,1,3]) == 3