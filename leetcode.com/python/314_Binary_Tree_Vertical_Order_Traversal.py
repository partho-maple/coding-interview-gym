# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import defaultdict


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque([(root, 0)])
        verticalNodeMap = defaultdict(list)
        while queue:
            node, horrizotalDistace = queue.popleft()
            if node:
                verticalNodeMap[horrizotalDistace].append(node.val)
                queue.append((node.left, horrizotalDistace - 1))
                queue.append((node.right, horrizotalDistace + 1))

        minHorrizotalDistace, maxHorrizotalDistace = min(verticalNodeMap.keys()), max(verticalNodeMap.keys())

        result = []
        for key in range(minHorrizotalDistace, maxHorrizotalDistace + 1):
            result.append(verticalNodeMap[key])
        return result


# My solution during mock, getting TLE, don't know why
from collections import defaultdict
from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        orderMap = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            currentNode, vLine = queue.popleft()
            if currentNode:
                orderMap[vLine].append(root.val)
                queue.append((root.left, vLine - 1))
                queue.append((root.right, vLine + 1))

        result = []
        for i in range(min(orderMap.keys()), max(orderMap.keys()) + 1):
            result.append(orderMap[i])
        return result