# Time O(n) |  Space O(logn)
def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum


def findMaxSum(tree):
    if tree is None:
        return (0, 0)
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBrach = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNoode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBrach)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNoode)

    return (maxSumAsBrach, maxPathSum)
