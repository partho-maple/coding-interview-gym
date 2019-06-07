# https://www.algoexpert.io/questions/Validate%20BST

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


# Here the parameter 'tree' is the root node, not the whole tree
def validate_bst(tree):
    return validate_bst_helper(tree, float("-inf"), float("inf"))


def validate_bst_helper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False
    left_is_valid = validate_bst_helper(tree.left, min_value, tree.value)
    right_is_valid = validate_bst_helper(tree.right, tree.value, max_value)
    return left_is_valid and right_is_valid


# driver/test code
test_tree = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
    .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
    .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
    .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)
is_valid_bst = validate_bst(test_tree)
print("Is BST valid ? - ", is_valid_bst)

