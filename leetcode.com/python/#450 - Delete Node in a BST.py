# https://leetcode.com/problems/delete-node-in-a-bst/solution/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.right is not None:
                succrssor = self.successor(root)
                root.val = succrssor
                root.right = self.deleteNode(root.right, succrssor)
            elif root.left is not None:
                predecessor = self.predecessor(root)
                root.val = predecessor
                root.left = self.deleteNode(root.left, predecessor)
        return root


