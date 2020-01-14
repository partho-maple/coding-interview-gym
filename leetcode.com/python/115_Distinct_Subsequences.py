# Simple recursive approach.    Time Limit Exceeded
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return self.numDistinctHelper(s, t, 0, 0)


    def numDistinctHelper(self, s, t, sIdx, tIdx):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # if we have reached the end of the pattern
        if tIdx == len(t):
            return 1

        # if we have reached the end of the string but pattern has still some characters left
        if sIdx == len(s):
            return 0

        c1 = 0
        if s[sIdx] == t[tIdx]:
            c1 = self.numDistinctHelper(s, t, sIdx + 1, tIdx + 1)

        c2 = self.numDistinctHelper(s, t, sIdx + 1, tIdx)

        return c1 + c2


# Top-down Dynamic Programming with Memoization -    Accepted
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[-1  for _ in range(len(s))] for _ in range(len(t))]
        return self.numDistinctHelper(s, t, 0, 0, dp)


    def numDistinctHelper(self, s, t, sIdx, tIdx, dp):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # if we have reached the end of the pattern
        if tIdx == len(t):
            return 1

        # if we have reached the end of the string but pattern has still some characters left
        if sIdx == len(s):
            return 0

        if dp[tIdx][sIdx] == -1:
            c1 = 0
            if s[sIdx] == t[tIdx]:
                c1 = self.numDistinctHelper(s, t, sIdx + 1, tIdx + 1, dp)

            c2 = self.numDistinctHelper(s, t, sIdx + 1, tIdx, dp)
            dp[tIdx][sIdx] = c1 + c2

        return dp[tIdx][sIdx]


# Bottom-up Dynamic Programming -    Accepted
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sLen, tLen = len(s), len(t)

        if tLen == 0:
            return 1

        if sLen == 0 or sLen < tLen:
            return 0

        # dp[sIndex][tIndex] will be storing the count of SPM up to str[0..sIndex-1][0..tIndex-1]
        dp = [[0 for _ in range(sLen + 1)] for _ in range(tLen + 1)]

        for i in range(sLen + 1):
            dp[0][i] = 1

        for tIdx in range(1, tLen + 1):
            for sIdx in range(1, sLen + 1):
                if s[sIdx - 1] == t[tIdx - 1]:
                    dp[tIdx][sIdx] = dp[tIdx - 1][sIdx - 1]
                dp[tIdx][sIdx] += dp[tIdx][sIdx - 1]

        return dp[-1][-1]