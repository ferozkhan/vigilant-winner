"""
find hourglas max sum from given 2D array.
a b c
  d
e f g
"""

def get_houglas_sum_helper(arr, x, y):
    return arr[x][y] + arr[x - 1][y - 1] + arr[x - 1][y] + \
           arr[x - 1][y + 1] + arr[x + 1][y - 1] + \
           arr[x + 1][y] + arr[x + 1][y + 1]


def hourglass_sum(arr):
    rows = len(arr)
    cols = len(arr[0])

    max_sum = float('-inf')
    i = 1
    while 0 < i < rows - 1:
        j = 1
        while 0 < j < cols - 1:
            max_sum = max(max_sum, get_houglas_sum_helper(arr, i, j))
            j += 1
        i += 1
    return max_sum


input_arr1 = [[-1, -1, 0, -9, -2, -2],
              [-2, -1, -6, -8, -2, -5],
              [-1, -1, -1, -2, -3, -4],
              [-1, -9, -2, -4, -4, -5],
              [-7, -3, -3, -2, -9, -9],
              [-1, -3, -1, -2, -4, -5]]

input_arr2 = [[1, 1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0],
              [0, 0, 2, 4, 4, 0],
              [0, 0, 0, 2, 0, 0],
              [0, 0, 1, 2, 4, 0]]


assert hourglass_sum(input_arr1) == -6
assert hourglass_sum(input_arr2) == 19
