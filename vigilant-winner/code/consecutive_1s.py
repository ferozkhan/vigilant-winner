"""
function to check maximum consecutive 1s in a binary number.
"""


def get_max_consecutive_1s(n: int):
    """
        function runs in logarithmic time and constant space.
    """
    max_sum = current_sum = 0
    while n > 0:
        binary_bit, n = n % 2, n // 2
        if binary_bit == 0:
            max_sum = max(current_sum, max_sum)
            current_sum = 0
        current_sum += binary_bit
    return max(max_sum, current_sum)


assert get_max_consecutive_1s(5) == 1
assert get_max_consecutive_1s(6) == 2
assert get_max_consecutive_1s(65535) == 16
assert get_max_consecutive_1s(1000000000) == 3
