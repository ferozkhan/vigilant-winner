import unittest


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


"""
Complexity: 
    runtime: O(n), since visiting each node
    space: O(n), since storing each node in array
"""
def is_binary_search_tree(root):

    # empty tree is a valid binary search tree
    if root is None:
        return True

    # queue is used to traverse the tree
    # initialize with root
    stack = [(root, float('inf'), float('-inf'))]

    # traverse until stack is not empty
    while stack:
        node, upper_bound, lower_bound = stack.pop()
        # check if node is a valid binary search node
        if (lower_bound >= node.value) or (node.value >= upper_bound):
            return False
        if node.left:
            # insert left node, with ancestor as upper_bound
            stack.append((node.left, node.value, lower_bound))
        if node.right:
            # insert right node, with ancestor as lower_bound
            stack.append((node.right, upper_bound, node.value))

    # Tree is valid binary tree if all node are traversed
    # and all nodes are valid.
    return True


class Test(unittest.TestCase):

    def xtest_valid_full_tree(self):
        tree = BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)