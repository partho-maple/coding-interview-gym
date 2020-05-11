# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = predecessor = None # predecessor of the current node https://tinyurl.com/ycrzmfzg

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if predecessor and root.val < predecessor.val:
                y = root
                if not x:
                    x = predecessor
                else:
                    break
            predecessor = root
            root = root.right

        x.val. y.val = y.val, x.val
