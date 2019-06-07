# https://www.algoexpert.io/questions/BST%20Traversal

class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

 # Average: O(log(n)) time | O(1) space
 # Worst: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self


# O(n) time | O(n) space
def in_order_traverse(tree, array):
    if tree is not None:
        in_order_traverse(tree.left, array)
        array.append(tree.value)
        in_order_traverse(tree.right, array)
    return array


# O(n) time | O(n) space
def pre_order_traverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        in_order_traverse(tree.left, array)
        in_order_traverse(tree.right, array)
    return array


# O(n) time | O(n) space
def post_order_traverse(tree, array):
    if tree is not None:
        in_order_traverse(tree.left, array)
        in_order_traverse(tree.right, array)
        array.append(tree.value)
    return array


# driver/test code
test_tree = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
    .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
    .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
    .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)
