"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [root, ]
        result = []
        while stack:
            current = stack.pop()
            if current and current.children:
                stack.extend(current.children)
            if current:
                result.append(current.val)
        return result[::-1]

