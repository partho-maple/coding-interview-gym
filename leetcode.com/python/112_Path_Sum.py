# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive Approach - Accepted
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        resultCache = []
        self.hasPathSumHelper(root, sum, 0, resultCache)
        return any(resultCache)

    def hasPathSumHelper(self, root, sum, currentSum, resultCache):
        if root:
            currentSum += root.val
            if root.left:
                self.hasPathSumHelper(root.left, sum, currentSum, resultCache)
            if root.right:
                self.hasPathSumHelper(root.right, sum, currentSum, resultCache)
            if not root.left and not root.right:
                if currentSum == sum:
                    resultCache.append(True)
                else:
                    resultCache.append(False)



# Iterative Approach - Accepted
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val), ]
        while stack:
            currentNode, currentSum = stack.pop()
            if currentNode:
                if currentNode.right:
                    stack.append((currentNode.right, currentSum + currentNode.right.val))
                if currentNode.left:
                    stack.append((currentNode.left, currentSum + currentNode.left.val))
                if not currentNode.left and not currentNode.right:
                    if currentSum == sum:
                        return True
        return False




