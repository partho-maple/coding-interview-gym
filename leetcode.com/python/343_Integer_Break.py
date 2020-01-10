
# Sourcce:  https://tinyurl.com/smsj265
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        dp[0] = None
        for m in range(1, n + 1):
            startNum = 1
            endum = m - startNum
            maxProd = 0
            while startNum <= endum:
                maxProd = max(maxProd, max(startNum, dp[startNum]) * max(endum, dp[endum]))
                startNum += 1
                endum -= 1
            dp[m] = maxProd
        return dp[-1]

