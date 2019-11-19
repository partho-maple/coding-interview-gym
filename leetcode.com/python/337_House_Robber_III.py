# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Post-order DFS traversal
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.robHelper(root))

    def robHelper(self, root):
        if not root:
            return (0, 0)
        leftHouseRobbery = self.robHelper(root.left)
        rightHouseRobbery = self.robHelper(root.right)
        robCurrentHouseNow = root.val + leftHouseRobbery[1] + rightHouseRobbery[1]
        robCurrentLaterLater = max(leftHouseRobbery) + max(rightHouseRobbery)
        return (robCurrentHouseNow, robCurrentLaterLater)
