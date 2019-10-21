"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, result = [root, ], []
        while stack:
            current = stack.pop()
            result.append(current.val)
            stack.extend(current.children[::-1])
        return result
