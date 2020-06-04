# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rightView = []
        queue = [root, ]
        currentLevelLength = 0
        while queue:
            currentLevelLength = len(queue)
            for idx in range(currentLevelLength):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if idx == (currentLevelLength - 1):
                    rightView.append(node.val)
        return rightView



#  My solution during mock contest
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = deque([root])
        rightView = []
        while queue:
            currentLevelLen = len(queue)
            for i in range(currentLevelLen):
                currentNode = queue.popleft()
                if currentNode:
                    if i == currentLevelLen - 1:
                        rightView.append(currentNode.val)
                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)
        return rightView