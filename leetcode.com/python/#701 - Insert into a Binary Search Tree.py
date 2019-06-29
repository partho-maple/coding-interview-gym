# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        currentNode = root
        while True:
            if val < currentNode.val:
                if currentNode.left is not None:
                    currentNode = currentNode.left
                else:
                    currentNode.left = TreeNode(val)
                    break
            elif val > currentNode.val:
                if currentNode.right is not None:
                    currentNode = currentNode.right
                else:
                    currentNode.right = TreeNode(val)
                    break
        return root

