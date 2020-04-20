


def remove_element(arr, val):
    """
    Remove all element from arr for arr[i] == val.
    below algorithm runs in O(n) runtime complexity and constant space.
    """
    x = 0
    for i in range(0, len(arr)):
        if arr[i] != val:
            arr[x] = arr[i]
            x += 1
    return x


arr = [0,1,2,2,3,0,4,2]
length = remove_element(arr, 2)
assert len(arr[:length]) == length
