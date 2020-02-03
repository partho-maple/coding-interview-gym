# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        return self.preOrderDFS(root)

    def preOrderDFS(self, root):
        if not root:
            return None
        left = self.preOrderDFS(root.left)
        right = self.preOrderDFS(root.right)
        root.left = None
        if left:
            root.right = left
            tailOfLeft = self.getRightTailNode(left)
            tailOfLeft.right = right
        return root

    def getRightTailNode(self, root):
        if not root or not root.right:
            return root
        return self.getRightTailNode(root.right)

