# https://leetcode.com/problems/closest-binary-search-tree-value


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        return self


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.closestValueHelper(root, target, float("inf"))

    def closestValueHelper(self, root, targetVal, currentClosestNodeVal):
        currentNode = root
        while currentNode is not None:
            currentClosestDiff = abs(targetVal - currentClosestNodeVal)
            currentDiff = abs(currentNode.val - targetVal)
            if currentClosestDiff > currentDiff:
                currentClosestNodeVal = currentNode.val
            if targetVal < currentNode.val:
                currentNode = currentNode.left
            elif targetVal > currentNode.val:
                currentNode = currentNode.right
            else:
                break
        return currentClosestNodeVal


test_tree = TreeNode(4).insert(2).insert(5).insert(1).insert(3)
solution = Solution()

closest_val = solution.closestValue(test_tree, 3.714286)
print(str(closest_val) + " is the Closest Value")
