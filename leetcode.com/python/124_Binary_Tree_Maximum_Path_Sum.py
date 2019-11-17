# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, maxSum = self.maxPathSumHelper(root)
        return maxSum

    def maxPathSumHelper(self, root):
        if not root:
            return (float('-inf'), float('-inf'))
        leftMaxSumAsBranch, leftMaxPathSum = self.maxPathSumHelper(root.left)
        rightMaxSumAsBranch, rightMaxPathSum = self.maxPathSumHelper(root.right)
        maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
        value = root.val
        maxSumAsBranch = max(maxChildSumAsBranch + value, value)
        maxSumAsRootNodeOrTriangle = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
        maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNodeOrTriangle)
        return (maxSumAsBranch, maxPathSum)



sol = Solution()
root = TreeNode(-3)
out = sol.maxPathSum(root)
print("Res", out)