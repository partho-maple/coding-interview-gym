"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.

        :type root: Node
        :rtype: TreeNode
        """
        if root is None:
            return None
        binary = TreeNode(root.val)     # Create a root node
        if root.children is None or len(root.children) <= 0:
            return binary
        binary.right = self.encode(root.children[0])    # Right child of binary is the encoding of of all n-ary  children, starting with the first child. Other children of n-array root are left child  of previous nodes child.
        node = binary.right
        for child in root.children[1:]:
            node.left = self.encode(child)
            node = node.left
        return binary


    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """
        if data is None:
            return None
        n_ary = Node(data.val, [])      # Create n-ary root
        node = data.right               # Move to first child of n-ary root
        while node:                     # while more children of n-ary root
            n_ary.children.append(self.decode(node))
            node = node.left
        return n_ary


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))