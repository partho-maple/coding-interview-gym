class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slowPtr = 0  # points the last index of consequtive non-zero elements keeping the original order from left
        for fastPtr in range(len(nums)):
            if nums[fastPtr] != 0:
                nums[fastPtr], nums[slowPtr] = nums[slowPtr], nums[fastPtr]
                slowPtr += 1
