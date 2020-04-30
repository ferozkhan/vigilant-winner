
import unittest


"""
complexity: 
    run-time => O(n)
    space => O(1) 
"""
def reverse(list_of_chars):

    if len(list_of_chars) < 2:
        return list_of_chars

    i = 0
    j = len(list_of_chars) - 1

    while i < j:
        list_of_chars[i], list_of_chars[j] = list_of_chars[j], list_of_chars[i]
        i += 1
        j -= 1

    return list_of_chars


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)
