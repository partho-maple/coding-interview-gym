class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        low, high = min(sweetness), sum(sweetness)
        while low <= high:
            mid = low + (high - low) // 2
            cuts = self.split(sweetness, mid)
            if cuts > K:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def split(self, nums, upperLimit):
        currentPrefixSum, currentCuts = 0, 0
        for num in nums:
            if (currentPrefixSum + num) >= upperLimit:
                currentPrefixSum = 0
                currentCuts += 1
            else:
                currentPrefixSum += num
        return currentCuts