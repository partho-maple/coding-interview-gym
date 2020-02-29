import math

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) / 2
            isPossible = self.isPossible(piles, H, mid)
            if isPossible:
                high = mid
            else:
                low = mid + 1
        return low

    def isPossible(self, piles, H, k):
        totalHours = 0
        for bananas in piles:
            totalHours += bananas / k
            if bananas % k != 0:
                totalHours += 1
        return totalHours <= H


