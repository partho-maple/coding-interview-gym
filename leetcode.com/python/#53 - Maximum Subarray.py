class Solution(object):
    def maxSubArray(self, nums):
        max_ending_here = nums[0]
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

