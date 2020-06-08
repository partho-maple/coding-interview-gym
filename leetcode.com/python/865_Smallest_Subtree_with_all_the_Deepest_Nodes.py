# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The Lowest Common Ancestor/Manager for all the nodes(deepest nodes) of the last level(deepest level) of the tree
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        lca, depth = self.subtreeWithAllDeepestHelper(root)
        return lca

    def subtreeWithAllDeepestHelper(self, root):
        if not root:
            return None, 0
        left, lDepth = self.subtreeWithAllDeepestHelper(root.left)
        right, rDepth = self.subtreeWithAllDeepestHelper(root.right)

        if lDepth > rDepth:
            return left, lDepth + 1
        elif lDepth < rDepth:
            return right, rDepth + 1
        else:
            return root, lDepth + 1  # lDepth == rDepth
