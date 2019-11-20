"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):

    # # Iterative level order traversal
    # def connect(self, root):
    #     """
    #     :type root: Node
    #     :rtype: Node
    #     """
    #     level_starting_Node = root
    #     while level_starting_Node:
    #         current_node = level_starting_Node  # first node of the level
    #         while current_node: # keep going to the right of that level
    #             if current_node.left:
    #                 current_node.left.next = current_node.right
    #             if current_node.right and current_node.next:
    #                 current_node.right.next = current_node.next.left
    #             current_node = current_node.next
    #         level_starting_Node = level_starting_Node.left
    #     return root

    # Recursive level order traversal, top-down, pre-order DFS
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

