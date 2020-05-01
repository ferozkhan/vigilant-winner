import unittest


def merge_sorted_array(arr1, arr2):
    """
    Complexity:
        runtime: O(n)
        space: O(n)
    """
    def helper(l1, l2, merged_arr):
        if not l1 or not l2:
            """ if one or both lists empty, return """
            return merged_arr + (l1 or l2)

        """ smallest item is always the first element, 
        pick the smallest from 0th index of both lists """
        if l1[0] < l2[0]:
            merged_arr.append(l1[0])
            """ list-1 element is added to the merged_arr and remove, since its smallest """
            return helper(l1[1:], l2, merged_arr)
        else:
            merged_arr.append(l2[0])
            """ list-2 element is added to the merged_arr and remove, since its smallest """
            return helper(l1, l2[1:], merged_arr)

    return helper(arr1, arr2, [])


class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_sorted_array([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_sorted_array([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_sorted_array([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_sorted_array([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_sorted_array([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)