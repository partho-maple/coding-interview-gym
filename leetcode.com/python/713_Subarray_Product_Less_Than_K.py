class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= 0 or k <= 1:
            return 0
        cumulativeProduct = 1
        left, subarrayCount = 0, 0
        for right, num in enumerate(nums):
            cumulativeProduct *= num
            while cumulativeProduct >= k:
                cumulativeProduct /= nums[left]
                left += 1
            subarrayCount += (right - left + 1)
        return subarrayCount