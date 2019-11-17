# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return ""
        paths = []
        self.binaryTreePathsHelper(root, paths, [])
        return paths

    def binaryTreePathsHelper(self, root, paths, currentRoute):
        if root:
            currentRoute.append(str(root.val))
            if not root.left and not root.right:  # If the node is a leaf
                paths.append("->".join(currentRoute))
            else:
                if root.left:
                    self.binaryTreePathsHelper(root.left, paths, currentRoute)
                if root.right:
                    self.binaryTreePathsHelper(root.right, paths, currentRoute)
            currentRoute.pop()
