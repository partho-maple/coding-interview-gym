# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bfsLevelOrder = [root]
        currentIdx = 0
        while bfsLevelOrder[currentIdx]:
            currentNode = bfsLevelOrder[currentIdx]
            bfsLevelOrder.append(currentNode.left)
            bfsLevelOrder.append(currentNode.right)
            currentIdx += 1
        return not any(bfsLevelOrder[currentIdx:])
