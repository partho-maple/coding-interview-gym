# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        return self.postorderTraversalHelper(root, result)

    def postorderTraversalHelper(self, root, result):
        if root:
            self.postorderTraversalHelper(root.left, result)
            self.postorderTraversalHelper(root.right, result)
            result.append(root.val)
        return result