# Approach 1: Sliding window. O(n)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, length = 0, 0, float("inf")
        sLen = len(nums)
        currentSum = 0
        while right < sLen:
            currentSum += nums[right]
            right += 1
            while currentSum >= s:
                length = min(length, right - left)
                currentSum -= nums[left]
                left += 1
        return length if length != float("inf") else 0

