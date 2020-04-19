

# complexity: run -> O(N) | space O(1)
def valid_mountain_array(A):
    array_length = len(A)
    step = 0
    # walk up the mountain
    while step < array_length - 1 and A[step] < A[step + 1]:
        step += 1

    # check peak
    # beginning and ending, cant be a peak
    if step == 0 or step == array_length - 1:
        return False

    # walk down the mountain
    while step < array_length - 1 and A[step] > A[step + 1]:
        step += 1

    return step == array_length - 1


assert valid_mountain_array([0, 1]) == False
assert valid_mountain_array([0, 1, 0]) == True
assert valid_mountain_array([0, 1, 1, 0]) == False