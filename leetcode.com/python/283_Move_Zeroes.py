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



# My solution duriing mock
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        read, write = 0, 0
        while read < len(nums):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                read += 1
                write += 1
            else:
                read += 1


"""
[0,1,0,3,12]
 r
 w
"""