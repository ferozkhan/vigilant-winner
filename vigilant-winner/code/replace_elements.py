from typing import List


def replace_elements(arr: List[int]) -> List[int]:
    """
    [17,18,5,4,6,1]
    max(arr[i], arr[i-1])
    """
    length = len(arr)
    i = length - 1
    while i > 0:
        if i == length - 1:
            arr[i] = max(arr[i], -1)
        else:
            arr[i] = max(arr[i+1], arr[i])
        i -=1
    arr.append(-1)
    return arr[1:]


print(replace_elements([17,18,5,4,6,1]))