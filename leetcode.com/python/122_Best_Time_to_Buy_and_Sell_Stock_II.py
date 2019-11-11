class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += (prices[i + 1] - prices[i])
        return profit


sol = Solution()
prices = [1,2,3,4,5]
profit = sol.maxProfit(prices)
print("Profit: ", profit)

