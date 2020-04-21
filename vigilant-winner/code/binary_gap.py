
def get_binary(N):
    output = ''
    count_ones = 0
    while N > 0:
        binary_bit, N = N % 2, N // 2
        output += str(binary_bit)
        if binary_bit == 1:
            count_ones += 1
    return output, count_ones > 1


def solution(N):
    binary, has_gap = get_binary(N)
    if not has_gap:
        return 0
    count_gap = False
    max_gap = current_gap = 0
    for i in range(len(binary)):
        if binary[i] == '1' and not count_gap:
            count_gap = True

        if binary[i] == '0' and count_gap:
            current_gap += 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0
    return max_gap


print(solution(32))
print(solution(592))
print(solution(51712))

