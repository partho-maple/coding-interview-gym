# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        currentNode = root
        while True:
            if val < currentNode.val:
                if currentNode.left is None:
                    return None
                else:
                    currentNode = currentNode.left
            elif val > currentNode.val:
                if currentNode.right is None:
                    return None
                else:
                    currentNode = currentNode.right
            else:
                return currentNode
