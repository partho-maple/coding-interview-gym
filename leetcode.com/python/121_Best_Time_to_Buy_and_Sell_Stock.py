class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float("inf")
        maximumProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maximumProfit:
                maximumProfit = price - minPrice
        return maximumProfit
