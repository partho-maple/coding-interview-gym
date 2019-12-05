from collections import Counter

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Edge case
        if not nums:
            return 0

        # Sliding Window -- No, because the array contains negative number
        # Dictionary + prefixSum technique
        subArrayCount, currentSum = 0, 0
        prefixSumCounter = Counter()
        prefixSumCounter[0] = 1
        for num in nums:
            currentSum += num #  increment current sum
            prefixSum = currentSum - k
            if prefixSum in prefixSumCounter: # check if there is a prefix subarray we can take out to reach k
                subArrayCount += prefixSumCounter[prefixSum]
            prefixSumCounter[currentSum] += 1  # add current sum to sum count
        return subArrayCount





sol = Solution()
nums = [1,1,1]
k = 2
out = sol.subarraySum(nums, k)
print("Res: ", out)