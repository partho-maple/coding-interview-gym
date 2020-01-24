# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Top-Down approach - Accepted
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        longestSeque = 0
        longestSeque = self.longestConsecutiveHelper(root, None, 0, longestSeque)
        return longestSeque

    def longestConsecutiveHelper(self, root, parent, currentLongestSeque, longestSeque):
        if not root:
            return max(currentLongestSeque, longestSeque)
        if parent and root.val == parent.val + 1:
            currentLongestSeque += 1
        else:
            currentLongestSeque = 1
        longestSeque = max(currentLongestSeque, longestSeque)
        leftLength = self.longestConsecutiveHelper(root.left, root, currentLongestSeque, longestSeque)
        rightLength = self.longestConsecutiveHelper(root.right, root, currentLongestSeque, longestSeque)
        maxLength = max(leftLength, rightLength, longestSeque)
        return maxLength




# Bottom-Up approach - Accepted
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dummyNode = TreeNode(float("inf"))
        dummyNode.left = root
        longestSeque, val = self.longestConsecutiveHelper(dummyNode)
        return longestSeque

    def longestConsecutiveHelper(self, root):
        if not root:
            return (0, float("-inf"))
        leftLength, leftVal = self.longestConsecutiveHelper(root.left)
        rightLength, rightVal = self.longestConsecutiveHelper(root.right)

        if leftVal != float("-inf") and root.val == leftVal - 1:
            leftLength += 1
        elif rightVal != float("-inf") and root.val == rightVal - 1:
            rightLength += 1
        longestSeque = max(leftLength, rightLength, 1)

        return (longestSeque, root.val)
