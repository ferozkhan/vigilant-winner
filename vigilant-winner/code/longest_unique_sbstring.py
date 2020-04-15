


"""
runtime complexity: O(nlog(n))
space complexity: O(m), m: average length substring
"""
def find_longest_substring_length(s: str) -> int:
    max_substring_length = 0
    seen = {}
    i = 0
    while i < len(s):
        if s[i] in seen:
            max_substring_length = max(max_substring_length, len(seen))
            i = seen[s[i]]
            seen = {}
        else:
            seen[s[i]] = i
        i += 1
    return max(max_substring_length, len(seen))


assert find_longest_substring_length(' ') == 1
assert find_longest_substring_length('abcabcabb') == 3
assert find_longest_substring_length('dvdf') == 3
