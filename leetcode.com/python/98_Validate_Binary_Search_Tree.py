# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class BST:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

 # Average: O(log(n)) time | O(1) space
 # Worst: O(n) time | O(1) space
    def insert(self, val):
        currentNode = self
        while True:
            if val < currentNode.val:
                if currentNode.left is None:
                    currentNode.left = BST(val)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(val)
                    break
                else:
                    currentNode = currentNode.right
        return self



import sys

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        MAX = sys.maxint
        MIN = -sys.maxint - 1
        return self.isValidBSTHelper(root, MIN, MAX)


    def isValidBSTHelper(self, root, minValue, maxValue):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return minValue < root.val < maxValue
        if root.val <= minValue or root.val >= maxValue:
            return False
        leftSubtreeIsValid = self.isValidBSTHelper(root.left, minValue, root.val)
        rightSubtreeIsValid = self.isValidBSTHelper(root.right, root.val, maxValue)
        return leftSubtreeIsValid and rightSubtreeIsValid


# driver/test code
# test_tree = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
#     .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
#     .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
#     .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)
test_tree = BST(2).insert(1).insert(4).insert(None).insert(None).insert(3).insert(6)
sol = Solution()
is_valid_bst = sol.isValidBST(test_tree)
print("Is BST valid ? - ", is_valid_bst)