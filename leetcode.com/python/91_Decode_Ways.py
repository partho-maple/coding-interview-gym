# Approach 1: SSSimple recursive solution. Time Limit Exceeded
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.numDecodingsHelper(s, 0)

    def numDecodingsHelper(self, s, currentIdx):
        if currentIdx >= len(s):
            return 1
        if int(s[currentIdx:currentIdx + 1]) <= 0:
            return 0
        currentWays = 0
        oneNumWays = self.numDecodingsHelper(s, currentIdx + 1)
        currentWays += oneNumWays
        diff = abs(len(s) - currentIdx)
        if diff >= 2 and int(s[currentIdx:currentIdx + 2]) < 27:
            twoNumWays = self.numDecodingsHelper(s, currentIdx + 2)
            currentWays += twoNumWays
        return currentWays





# Approach 2: Simple recursive solution with memoization. Accepted
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        return self.numDecodingsHelper(s, 0, cache)

    def numDecodingsHelper(self, s, currentIdx, cache):
        if s[currentIdx:] in cache:
            return cache[s[currentIdx:]]
        if currentIdx >= len(s):
            return 1
        if int(s[currentIdx:currentIdx + 1]) <= 0:
            return 0
        currentWays = 0
        oneNumWays = self.numDecodingsHelper(s, currentIdx + 1, cache)
        currentWays += oneNumWays
        diff = abs(len(s) - currentIdx)
        if diff >= 2 and int(s[currentIdx:currentIdx + 2]) < 27:
            twoNumWays = self.numDecodingsHelper(s, currentIdx + 2, cache)
            currentWays += twoNumWays
        cache[s[currentIdx:]] = currentWays
        return cache[s[currentIdx:]]





# Approach 3: Bottom-Up taulation DP. Accepted
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        if sLen <= 0:
            return 0
        dp = [0] * (sLen + 1)
        dp[0] = 1
        for i in range(1, sLen + 1):
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            if i != 1 and s[i - 2:i] < "27" and s[i - 2:i] > "09":
                dp[i] += dp[i - 2]
        return dp[-1]


