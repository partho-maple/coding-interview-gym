# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        resultCache, currentPath = [], []
        self.pathSumHelper(root, sum, currentPath, resultCache)
        return resultCache

    def pathSumHelper(self, root, sum, currentPath, resultCache):
        if root:
            currentPath.append(root.val)
            if not root.left and not root.right:
                if root.val == sum:
                    resultCache.append(list(currentPath))
            if root.left:
                self.pathSumHelper(root.left, sum - root.val, currentPath, resultCache)
            if root.right:
                self.pathSumHelper(root.right, sum - root.val, currentPath, resultCache)
            currentPath.pop()  # Backtrack the result path
