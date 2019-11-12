class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        days = len(prices)
        totalProfit = 0
        minimumPrice = prices[0]
        for today in range(1, days):
            if prices[today] < minimumPrice:
                minimumPrice = prices[today]
            elif minimumPrice < (prices[today] - fee):
                totalProfit += (prices[today] - minimumPrice - fee)
                minimumPrice = prices[today] - fee   #  https://tinyurl.com/unnnjwx  and  https://tinyurl.com/umjax4y
        return totalProfit


sol = Solution()
prices = [1,3,7,5,10,3]
fee = 3
output = sol.maxProfit(prices, fee)
print('Res: ', output)