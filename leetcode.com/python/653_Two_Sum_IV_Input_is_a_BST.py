# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        diffSet = set()
        return self.findTargetHelper(root, k, diffSet)

    def findTargetHelper(self, root, k, diffSet):
        if not root:
            return False
        if root.val in diffSet:
            return True
        else:
            diffSet.add((k - root.val))
            left = self.findTargetHelper(root.left, k, diffSet)
            right = self.findTargetHelper(root.right, k, diffSet)
            return left or right
