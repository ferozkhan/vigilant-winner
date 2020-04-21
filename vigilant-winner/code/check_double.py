from collections import Counter
from typing import List


def check_if_double_exist(arr: List[int]) -> bool:
    memo = set()
    for num in arr:
        if num in memo or num *4 in memo:
            return True
        else:
            memo.add(num *2)
    return False


def checkIfExist(arr: List[int]) -> bool:
    k = Counter(arr)
    print(k, k[0])
    if k[0] > 1: return 1
    for i in arr:
        if k[2 * i] and i != 0:
            return 1
    else:
        return 0

assert check_if_double_exist([10,2,5,3]) == True
assert check_if_double_exist([3, 7, 1, 11]) == False
checkIfExist([10,2,5,3])
checkIfExist([3, 7, 1, 11, 0])

