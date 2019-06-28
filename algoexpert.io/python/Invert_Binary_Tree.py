# https://www.algoexpert.io/questions/Invert%20Binary%20Tree

import unittest

class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i = 0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current  = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


# Using iteration
# O(n) time | O(n) space
def invert_binary_tree(tree):
    # Here the parameter 'tree' is not likely the whole tree.
    # It's the root node of the whole tree
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swap_left_and_right(current)
        queue.append(current.left)
        queue.append(current.right)

# Using recursion
# O(n) time | O(d) space , here d = depth of the tree
def invert_binary_tree(tree):
    if tree is None:
        return
    swap_left_and_right(tree)
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)

def swap_left_and_right(tree):
    tree.left, tree.right = tree.right, tree.left


test6 = BinaryTree(1).insert([2, 3, 4, 5, 6])
# invertedTest6 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6])
invertedTest6 = invert_binary_tree(test6)

test7 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
# invertedTest7 = BinaryTree(1).invertedInsert([2, 3, 4, 5, 6, 7])
invertedTest7 = invert_binary_tree(test7)


print(test6)
print(invertedTest6)


class TestProgram(unittest.TestCase):

    def test_case_6(self):
        self.assertTrue(test6.__eq__(invertedTest6))


if __name__ == "__main__":
    unittest.main()



