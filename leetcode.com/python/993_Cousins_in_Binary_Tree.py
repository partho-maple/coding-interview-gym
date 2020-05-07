# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        xLevel, xParent = self.isCousinsHelperDFS(root, None, 0, x)
        yLevel, yParent = self.isCousinsHelperDFS(root, None, 0, y)

        if xParent and yParent and (xParent != yParent) and (xLevel == yLevel):
            return True
        else:
            return False

    def isCousinsHelperDFS(self, node, parent, currentLevel, x):
        if not node:
            return (0, None)
        if node.val == x:
            return (currentLevel, parent)

        leftLevel, leftParent = self.isCousinsHelperDFS(node.left, node, currentLevel + 1, x)
        rightLevel, rightParent = self.isCousinsHelperDFS(node.right, node, currentLevel + 1, x)
        if leftParent:
            return (leftLevel, leftParent)
        else:
            return (rightLevel, rightParent)


