# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
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
            for i in range(levelLength):
                node = queue.pop(0)
                levels[currentLevel].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            currentLevel += 1

        return levels[::-1]  # Simply reverse the list. [start:stop:step] so step is -1
