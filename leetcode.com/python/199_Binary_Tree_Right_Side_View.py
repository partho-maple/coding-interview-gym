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

