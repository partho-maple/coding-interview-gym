# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Solusion
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        rightInverted = self.invertTree(root.right)
        leftInverted = self.invertTree(root.left)
        root.left = rightInverted
        root.right = leftInverted
        return root


# Iterative Solusion
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = [root, ]
        while queue:
            current = queue.pop(0)
            if current:
                current.left, current.right = current.right, current.left # Swaps the node
                queue.append(current.left)
                queue.append(current.right)
        return root
