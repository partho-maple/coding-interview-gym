class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfitWithKTransaction(prices, k)


    # # This solution is getting "Memory Limit Exceeded"
    # def maxProfitWithKTransaction(self, prices, k):
    #     if not prices:
    #         return 0
    #     profits = [[0 for d in prices] for t in range(k + 1)]
    #     for t in range(1, k + 1):
    #         maxThusFar = float('-inf')
    #         for d in range(1, len(prices)):
    #             maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
    #             profits[t][d] = max(profits[t][d - 1], maxThusFar + prices[d])
    #     return profits[-1][-1]
    #
    #
    # Updated implementation to avoid "Memory Limit Exceeded". But yet "Memory Limit Exceeded"
    def maxProfitWithKTransaction(self, prices, k):
        if not prices or k <= 0:
            return 0
        evenProfits = [0 for d in prices]
        oddProfits = [0 for d in prices]
        for t in range(1, k + 1):
            maxThusFar = float('-inf')
            if t % 2 == 1:
                currentProfits = oddProfits
                previousProfits = evenProfits
            else:
                currentProfits = evenProfits
                previousProfits = oddProfits
            for d in range(1, len(prices)):
                maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
                currentProfits[d] = max(currentProfits[d - 1], maxThusFar + prices[d])
        return evenProfits[-1] if t % 2 == 0 else oddProfits[-1]




sol = Solution()
# input = [3,2,6,5,0,3]
input = [5,11,3,50,60,90]
k = 2
output = sol.maxProfit(k, input)
print('Res: ', output)