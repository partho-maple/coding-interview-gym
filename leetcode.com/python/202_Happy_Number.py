class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slowRuner, fastRunner = n, self.getNextNumer(n)
        while fastRunner != 1 and fastRunner != slowRuner:
            fastRunner = self.getNextNumer(self.getNextNumer(fastRunner))
            slowRuner = self.getNextNumer(slowRuner)
        return fastRunner == 1

    def getNextNumer(self, num):
        totalSum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            totalSum += (digit ** 2)
        return totalSum
