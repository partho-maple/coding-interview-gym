"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result, queue = [], [root] if root else []
        while queue:
            levelNode = []
            for node in queue:  # add value of every node in queue
                levelNode.append(node.val)
            result.append(levelNode)
            children = []
            for node in queue:  # for every node in queue add its children
                for child in node.children:
                    children.append(child)
            queue = children  # replaces the queue.

        return result
