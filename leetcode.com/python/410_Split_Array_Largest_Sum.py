# https://tinyurl.com/vf43ly3
# Approach 1: Brute force using DFS. Time limit exceeded
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        self.gloalMiniMax = float('inf')
        self.dfs(nums, m, 0, 0, 0, 0)
        return self.gloalMiniMax

    def dfs(self, nums, m, currentIdx, subarrayCount, currentSum, currentMax):
        n = len(nums)
        ans = self.gloalMiniMax
        if currentIdx == n and subarrayCount == m:
            ans = min(ans, currentMax)
            self.gloalMiniMax = ans
            return
        if currentIdx == n:
            return
        if currentIdx > 0:
            self.dfs(nums, m, currentIdx + 1, subarrayCount, currentSum + nums[currentIdx],
                     max(currentMax, currentSum + nums[currentIdx]))
        if subarrayCount < m:
            self.dfs(nums, m, currentIdx + 1, subarrayCount + 1, nums[currentIdx], max(currentMax, nums[currentIdx]))




# Approach 2: Binary search. Accepted
class Solution:
    def splitArray(self, nums, m):
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = low + (high - low) // 2
            pieces = self.split(nums, mid)
            if pieces > m:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def split(self, nums, upperLimit):
        currentPrefixSum, currentPieces = 0, 1
        for num in nums:
            if currentPrefixSum + num > upperLimit:
                currentPrefixSum = num
                currentPieces += 1
            else:
                currentPrefixSum += num
        return currentPieces