from typing import List


def move_zeroes_f1(arr: List[int]) -> None:
    """ this runs in quadratic time and constant space.
    And very inefficient.
    """
    i = j = 0
    length = len(arr)
    while i < length:
        if arr[i] == 0:
            while arr[j] == 0 and j < length - 1:
                j += 1
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j = i


def move_zeroes_f2(arr: List[int]) -> None:
    """this algorithm runs in linear time and constant space.
    better algorithm than f1.
    """
    j = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1


nums = [0,1,0,3,12]
move_zeroes_f1(nums)
assert nums == [1, 3, 12, 0, 0]

nums = [0,1,0,3,12]
move_zeroes_f2(nums)
assert nums == [1, 3, 12, 0, 0]