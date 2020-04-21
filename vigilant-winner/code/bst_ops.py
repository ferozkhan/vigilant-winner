# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        parent = None
        while node:
            parent = node
            if value >= self.value:
                node = node.right
            else:
                node = node.left
        if parent:
            if value >= parent.value:
                parent.right = BST(value)
            else:
                parent.left = BST(value)

        return self

    def search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value > node.value:
            return self.search(node.right, value)
        if value < node.value:
            return self.search(node.left, value)


def contains(self, value):
    return self.search(self, value)


def get_min_value(self):
    current = self
    while current:
        current = current.right
    return current.value


def remove(self, value, parent=None):
    current = self
    while current is not None:
        if value < current.value:
            parent = current
            current = current.left
        elif value > current.value:
            parent = current
            current = current.right
        else:
            if current.left and current.right:
                current.value = current.right.get_min_value()
                current.right.remove(current.value, current)
            elif parent is None:
                if current.left:
                    current.value = current.left.value
                    current.right = current.left.right
                    current.left = current.left.left
                elif current.right:
                    current.value = current.right.value
                    current.right = current.right.right
                    current.left = current.right.left
            elif parent.left == current:
                parent.left = current.left if current.left else current.right
            elif parent.right == current:
                parent.right = current.right if current.right else current.left

    return self



""""""""


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = self
        parent = None
        while node:
            parent = node
            if value >= self.value:
                node = node.right
            else:
                node = node.left
        if parent:
            if value >= parent.value:
                parent.right = BST(value)
            else:
                parent.left = BST(value)

        return self

    def search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value > node.value:
            return self.search(node.right, value)
        if value < node.value:
            return self.search(node.left, value)


def contains(self, value):
    return self.search(self, value)


def get_min_value(self):
    current = self
    while current.left is not None:
        current = current.left
    return current.value


def remove(self, value, parent=None):
    current = self
    while current is not None:
        if value < current.value:
            parent = current
            current = current.left
        elif value > current.value:
            parent = current
            current = current.right
        else:
            if current.left and current.right:
                current.value = current.right.get_min_value()
                current.right.remove(current.value, current)
            elif parent is None:
                if current.left:
                    current.value = current.left.value
                    current.right = current.left.right
                    current.left = current.left.left
                elif current.right:
                    current.value = current.right.value
                    current.left = current.right.left
                    current.right = current.right.right
            elif parent.left == current:
                parent.left = current.left if current.left else current.right
            elif parent.right == current:
                parent.right = current.left if current.left else current.right
            break


    return self
