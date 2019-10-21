# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        currentLevel = 0
        queue = [root, ]
        while queue:
            levels.append([])
            levelLength = len(queue)
            start = end = 0
            isEvenLevel = True if currentLevel % 2 == 0 else False
            for i in range(levelLength):
                node = queue.pop(0)
                levels[currentLevel].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if isEvenLevel is False:
                levels[currentLevel] = levels[currentLevel][::-1]
            currentLevel += 1
        return levels
