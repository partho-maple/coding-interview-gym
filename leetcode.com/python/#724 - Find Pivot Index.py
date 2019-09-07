class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == (S - nums[i] - leftSum):
                return i
            leftSum += nums[i]
        return -1
