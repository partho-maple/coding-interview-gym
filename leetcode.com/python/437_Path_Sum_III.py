# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BruteForce, Getting TLE and MLE.
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        resultCache, currentPath = [], []
        self.pathSumHelper(root, sum, currentPath, resultCache)
        return len(resultCache)

    def pathSumHelper(self, root, sum, currentPath, resultCache):
        if root:
            currentPath.append(root.val)
            currentSum = 0
            for idx, num in reversed(list(enumerate(currentPath))):
                currentSum += num
                if currentSum == sum:
                    resultCache.append(list(currentPath[idx:]))
            if root.left:
                self.pathSumHelper(root.left, sum, currentPath, resultCache)
            if root.right:
                self.pathSumHelper(root.right, sum, currentPath, resultCache)
            currentPath.pop()  # Backtrack the result path





# # BruteForce - Accepted
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        resultCache, currentPath = [], []
        return self.pathSumHelper(root, sum, currentPath, resultCache)


    def pathSumHelper(self, root, sum, currentPath, resultCache):
        pathCount, prefixSum = 0, 0
        if root:
            currentPath.append(root.val)
            for idx, num in reversed(list(enumerate(currentPath))):
                prefixSum += num
                if prefixSum == sum:
                    pathCount += 1
            if root.left:
                pathCount += self.pathSumHelper(root.left, sum, currentPath, resultCache)
            if root.right:
                pathCount += self.pathSumHelper(root.right, sum, currentPath, resultCache)
            currentPath.pop()  # Backtrack the result path
        return pathCount






from collections import Counter

# PrefixSum/PathSum approach - Accepted. Source: https://tinyurl.com/wkxjmqv
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        prefixSumCounter, currentPathSum, self.totalNumerOfPaths = Counter(), 0, 0
        prefixSumCounter[0] = 1
        self.pathSumHelper(root, sum, currentPathSum, prefixSumCounter)
        return self.totalNumerOfPaths



    def pathSumHelper(self, root, targetSum, currentPathSum, prefixSumCounter):
        if root is None:
            return
        currentPathSum += root.val
        oldPathSum = currentPathSum - targetSum
        if oldPathSum in prefixSumCounter:
            self.totalNumerOfPaths += prefixSumCounter[oldPathSum]
        prefixSumCounter[currentPathSum] += 1
        self.pathSumHelper(root.left, targetSum, currentPathSum, prefixSumCounter)
        self.pathSumHelper(root.right, targetSum, currentPathSum, prefixSumCounter)
        prefixSumCounter[currentPathSum] -= 1

