# Naive solution using simple backtracking. Time Limit Exceeded
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sumOfItems = sum(nums)
        if sumOfItems % k != 0:              # if 's' is a an odd number, we can't have two subsets with equal sum
            return False
        if k == 1:
            return True
        return self.canPartitionHelper(nums, sumOfItems/k, 0)


    def canPartitionHelper(self, nums, sumOfItems, currentIndex):
        if sumOfItems == 0:            # base check
            return True
        numsLen = len(nums)
        if numsLen == 0 or currentIndex >= numsLen:
            return False

        # recursive call after choosing the number at the `currentIndex`
        # if the number at `currentIndex` exceeds the sum, we shouldn't process this
        if nums[currentIndex] <= sumOfItems:
            if self.canPartitionHelper(nums, sumOfItems - nums[currentIndex], currentIndex + 1):
                return True # Backtrack

        # recursive call after excluding the number at the 'currentIndex'
        return self.canPartitionHelper(nums, sumOfItems, currentIndex + 1)




#
#
#
# # Solution using simple backtracking and memoization. Dynamic Programming on Top-Down approach. Accepted
# class Solution(object):
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         s = sum(nums)
#         if s % k != 0:              # if 's' is a an odd number, we can't have two subsets with equal sum
#             return False
#         dp = [[-1 for _ in range(int(s/k) + 1)] for _ in nums]
#         return True if self.canPartitionHelper(nums, s/k, 0, dp) == 1 else False
#
#
#     def canPartitionHelper(self, nums, sum, currentIndex, dp):
#         if sum == 0:            # base check
#             return 1
#         numsLen = len(nums)
#         if numsLen == 0 or currentIndex >= numsLen:
#             return 0
#
#         # if we have not already processed a similar problem
#         if dp[currentIndex][sum] == -1:
#             # recursive call after choosing the number at the `currentIndex`
#             # if the number at `currentIndex` exceeds the sum, we shouldn't process this
#             if nums[currentIndex] <= sum:
#                 if self.canPartitionHelper(nums, sum - nums[currentIndex], currentIndex + 1, dp):
#                     dp[currentIndex][sum] = 1
#                     return 1 # Backtrack
#
#             # recursive call after excluding the number at the 'currentIndex'
#             dp[currentIndex][sum] = self.canPartitionHelper(nums, sum, currentIndex + 1, dp)
#         return dp[currentIndex][sum]
#
#
#
#
#
# # Solution using Dynamic Programming on Bottom-up approach. Accepted
# class Solution(object):
#     def canPartitionKSubsets(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         if k == 1: return True
#         s = sum(nums)
#         if s % k != 0:  # if 's' is a an odd number, we can't have two subsets with equal sum
#             return False
#
#         # we are trying to find a subset of given numbers that has a total sum of 's/2'.
#         s = int(s / k)
#
#         numsLen = len(nums)
#         dp = [[False for _ in range(int(s) + 1)] for _ in range(numsLen)]
#
#
#         # populate the s=0 columns, as we can always for '0' sum with an empty set
#         for i in range(numsLen):
#             dp[i][0] = True
#
#         # with only one number, we can form a subset only when the required sum is
#         # equal to its value
#         for j in range(1, s + 1):
#             dp[0][j] = nums[0] == j
#
#         # process all subsets for all sums
#         for i in range(1, numsLen):
#             for j in range(1, s + 1):
#                 if dp[i - 1][j]:  # if we can get the sum 'j' without the number at index 'i'
#                     dp[i][j] = dp[i - 1][j]
#                 elif j >= nums[i]:  # else if we can find a subset to get the remaining sum
#                     dp[i][j] = dp[i - 1][j - nums[i]]
#
#         return dp[numsLen - 1][s]
#



sol = Solution()
nums = [2,2,2,2,3,4,5]
k = 4
out = sol.canPartitionKSubsets(nums, k)
print("Result: ", out)