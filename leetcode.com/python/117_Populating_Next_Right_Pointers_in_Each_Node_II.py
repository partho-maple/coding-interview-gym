"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
 
                 1 -> nullptr
               /  \
 parent       2 -> 3 -> nullptr
             / \    \
            4 ->5 -> 7
    childHead   
                   child

"""

# From Here:  https://tinyurl.com/rfjhzj3
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        parentNode, childHeadNode, childNode = root, None, None
        while parentNode: # top-to-bottom iteration. Traversing each level by level
            while parentNode: # left-to-right iteration. Traversing each node of a certain level
                if parentNode.left:
                    if childHeadNode:
                        childNode.next = parentNode.left
                        childNode = parentNode.left
                    else:
                        childHeadNode = parentNode.left
                        childNode = parentNode.left
                if parentNode.right:
                    if childHeadNode:
                        childNode.next = parentNode.right
                        childNode = parentNode.right
                    else:
                        childHeadNode = parentNode.right
                        childNode = parentNode.right
                parentNode = parentNode.next #  move parent node to right in the same level
            parentNode = childHeadNode # go to next level by moving parentNode one step down
            childHeadNode = None
            childNode = None
        return root





