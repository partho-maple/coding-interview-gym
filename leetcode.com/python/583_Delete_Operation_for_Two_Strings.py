class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1Len, word2Len = len(word1), len(word2)
        dp = [[0 for _ in range(word1Len + 1)] for _ in range(word2Len + 1)]
        maxSusequenceLen = 0
        for i in range(1, word2Len + 1):
            for j in range(1, word1Len + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i -1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i -1][j])
                maxSusequenceLen = max(maxSusequenceLen, dp[i][j])
        return (word1Len - maxSusequenceLen) + (word2Len - maxSusequenceLen)