import unittest
from typing import List


def merge_sorted_array_recursively(arr1: List, arr2: List) -> List:
    """
    Complexity:
        runtime: O(n)
        space: O(n)
    """
    def helper(l1: List, l2: List, merged_arr: List) -> List:
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


def merge_sorted_array_iteratively(arr1: List, arr2: List) -> List:
    """
        Complexity:
            runtime: O(n)
            space: O(n)
    """
    merge_arr_length = len(arr1) + len(arr2)
    merged_arr = [None] * merge_arr_length

    arr1_current_index = arr2_current_index = merged_arr_current_index = 0
    while merged_arr_current_index < merge_arr_length:
        """ find the smallest item and add it to the merged_arr """

        is_arr1_exhausted = arr1_current_index >= len(arr1)
        is_arr2_exhausted = arr2_current_index >= len(arr2)

        if (not is_arr1_exhausted and
                (is_arr2_exhausted or
                 arr1[arr1_current_index] <= arr2[arr2_current_index])):
            merged_arr[merged_arr_current_index] = arr1[arr1_current_index]
            # increment the index of arr1, since current index value is added to the merged_arr
            arr1_current_index += 1
        else:
            merged_arr[merged_arr_current_index] = arr2[arr2_current_index]
            # increment the index of arr2, since current index value is added to the merged_arr
            arr2_current_index += 1

        # increment the index of merged_arr since item is assigned to current index
        merged_arr_current_index += 1

    return merged_arr


class XTest(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_sorted_array_recursively([], [])
        expected = []
        self.assertEqual(actual, expected)
        actual = merge_sorted_array_iteratively([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_sorted_array_recursively([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)
        actual = merge_sorted_array_iteratively([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_sorted_array_recursively([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)
        actual = merge_sorted_array_iteratively([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_sorted_array_recursively([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)
        actual = merge_sorted_array_iteratively([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_sorted_array_recursively([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)
        actual = merge_sorted_array_iteratively([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)