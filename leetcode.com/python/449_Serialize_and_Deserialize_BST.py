# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
# Approach 1: No space optimisation done. Using preorder DFS
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'X' + ','
        leftSubTree = self.serialize(root.left)
        rightSubTree = self.serialize(root.right)
        return str(root.val) + "," + leftSubTree + rightSubTree

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = deque(data.split(","))
        return self.deserializeHelper(queue)

    def deserializeHelper(self, stream):
        if not stream or stream[0] == "X":
            return None
        node = TreeNode(stream.popleft())
        node.left = self.deserializeHelper(stream)
        stream.popleft()
        node.right = self.deserializeHelper(stream)
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))