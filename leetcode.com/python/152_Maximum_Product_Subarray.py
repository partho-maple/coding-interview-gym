class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minProd, maxProd, bestSoFar = 1, 1, nums[0]
        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum < 0:
                minProd, maxProd = maxProd, minProd
            maxProd = max(maxProd*currentNum, currentNum)
            minProd = min(minProd*currentNum, currentNum)
            bestSoFar = max(bestSoFar, maxProd)
        return bestSoFar
