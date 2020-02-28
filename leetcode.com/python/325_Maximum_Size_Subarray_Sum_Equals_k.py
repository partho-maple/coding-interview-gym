from collections import Counter

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sliding Window -- No, because the array contains negative number
        # Dictionary + prefixSum technique
        maxSubarrayLen, currentSum, prefixSum = 0, 0, 0
        prefixSumIndexCounter = Counter()       # Stores the indexes of the elements not the occurrences
        prefixSumIndexCounter[0] = -1
        for idx in range(len(nums)):
            currentSum += nums[idx] #  increment current sum
            prefixSum = currentSum - k
            if currentSum == k:
                maxSubarrayLen = idx + 1
            elif prefixSum in prefixSumIndexCounter: # check if there is a prefix subarray we can take out to reach k
                currentSubarrayLen = idx - prefixSumIndexCounter[prefixSum]
                maxSubarrayLen = max(maxSubarrayLen, currentSubarrayLen)
            if currentSum not in prefixSumIndexCounter:
                prefixSumIndexCounter[currentSum] = idx
        return maxSubarrayLen



class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sliding Window -- No, because the array contains negative number
        # Dictionary + prefixSum technique
        maxSubarrayLen, currentSum, prefixSum = 0, 0, 0
        prefixSumIndexCounter = Counter()
        prefixSumIndexCounter[0] = -1
        for idx in range(len(nums)):
            currentSum += nums[idx] #  increment current sum
            prefixSum = currentSum - k
            if currentSum == k:
                maxSubarrayLen = idx + 1
            elif prefixSum in prefixSumIndexCounter: # check if there is a prefix subarray we can take out to reach k
                currentSubarrayLen = idx - prefixSumIndexCounter[prefixSum]
                maxSubarrayLen = max(maxSubarrayLen, currentSubarrayLen)
            if currentSum not in prefixSumIndexCounter:
                prefixSumIndexCounter[currentSum] = idx
        return maxSubarrayLen


sol = Solution()
# nums = [1, -1, 5, -2, 3]
# k = 3
# nums = [-2,-1,2,1]
# k = 1
nums = [1,0,-1]
k = -1
out = sol.maxSubArrayLen(nums, k)
print("Res: ", out)