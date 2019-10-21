class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        return self.climbStairsHelper(n, memo)

    def climbStairsHelper(self, n, memo):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            memo[n] = 0
            return 0
        elif n == 1:
            memo[n] = 1
            return 1
        elif n == 2:
            memo[n] = 2
            return 2
        if n - 1 in memo:
            oneStepCounter = memo[n - 1]
        else:
            oneStepCounter = self.climbStairsHelper(n - 1, memo)
            memo[n - 1] = oneStepCounter
        if n - 2 in memo:
            twoStepCounter = memo[n - 2]
        else:
            twoStepCounter = self.climbStairsHelper(n - 2, memo)
            memo[n - 2] = twoStepCounter
        return oneStepCounter + twoStepCounter



sol = Solution()
result = sol.climbStairs(28)
print("Numbers: ", result)