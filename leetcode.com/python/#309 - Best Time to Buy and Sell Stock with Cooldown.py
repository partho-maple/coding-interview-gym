# Unfinished

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        cooldown = False
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i] and cooldown is False:
                profit = (prices[i + 1] - prices[i]) + profit
                cooldown = True
            elif prices[i + 1] > prices[i] and cooldown is True:
                profit = (prices[i + 1] - prices[i]) + profit
                cooldown = True
            else:
                cooldown = False
        return profit


sol = Solution()
prices = [1,2,4]
profit = sol.maxProfit(prices)
print("Profit: ", profit)


