# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)

    def sortedArrayToBSTHelper(self, nums, left, right):
        if left > right:
            return None
        rootIdx = (left + right) // 2
        root = TreeNode(nums[rootIdx])
        root.left = self.sortedArrayToBSTHelper(nums, left, rootIdx - 1)
        root.right = self.sortedArrayToBSTHelper(nums, rootIdx + 1, right)
        return root

