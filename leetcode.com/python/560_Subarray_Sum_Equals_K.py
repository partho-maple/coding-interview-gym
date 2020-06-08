# from collections import Counter

# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """

#         # Edge case
#         if not nums:
#             return 0

#         # Sliding Window -- No, because the array contains negative number
#         # Dictionary + prefixSum technique
#         subArrayCount, currentSum = 0, 0
#         prefixSumCounter = Counter()
#         prefixSumCounter[0] = 1
#         for num in nums:
#             currentSum += num
#             prefixSum = currentSum - k
#             if prefixSum in prefixSumCounter:
#                 subArrayCount += prefixSumCounter[prefixSum]
#             prefixSumCounter[currentSum] += 1
#         return subArrayCount


# # My solution duriing mock
# # The following solution is basically a slidinng window type solutio which won't work for egative numbers
# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if len(nums) <= 0:
#             return 0
#         prefixSum = [0] + nums
#         for i in range(1, len(prefixSum)):
#             prefixSum[i] = prefixSum[i - 1] + prefixSum[i]

#         left, right, subArrayCount = 0, 1, 0
#         while right < len(prefixSum) and left < right:
#             currentSum = prefixSum[right] - prefixSum[left]
#             if currentSum == k:
#                 subArrayCount += 1
#                 right += 1
#             elif currentSum < k:
#                 right += 1
#             else:
#                 left += 1
#         return subArrayCount


from collections import Counter


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= 0:
            return 0

        prefixSum, currentSum, subArrayCount = 0, 0, 0
        prefixSumCounter = Counter()
        prefixSumCounter[0] = 1

        for num in nums:
            currentSum += num
            requiredPrefixSum = currentSum - k
            if requiredPrefixSum in prefixSumCounter:
                subArrayCount += prefixSumCounter[requiredPrefixSum]
            prefixSumCounter[currentSum] += 1

        return subArrayCount