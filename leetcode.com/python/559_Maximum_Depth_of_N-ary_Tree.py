"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

#   Bottom-Up approach
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        maxDepthOfChildren = 0
        for child in root.children:
            depth = self.maxDepth(child)
            maxDepthOfChildren = max(maxDepthOfChildren, depth)
        return maxDepthOfChildren + 1




#   Top-Down approach
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        return self.maxDepthHelper(root, 1, 1)

    def maxDepthHelper(self, root, depth, maxDepth):
        if root is None:
            return maxDepth
        maxDepth = max(depth, maxDepth)
        for child in root.children:
            maxDepth = self.maxDepthHelper(child, depth + 1, maxDepth)
        return maxDepth


