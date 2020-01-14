class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1Len, str2Len = len(str1), len(str2)
        dp = [["" for _ in range(str1Len + 1)] for _ in range(str2Len + 1)]

        # if one of the strings is of zero length, SCS would be equal to the length of the other string
        for i in range(1, str1Len + 1):
            dp[0][i] = str1[i - 1]
        for i in range(1, str2Len + 1):
            dp[i][0] = str2[i - 1]

        for i in range(1, str2Len + 1):
            for j in range(1, str1Len + 1):
                if str1[j - 1] == str2[i - 1]:
                    dp[i][j] = str2[i - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = str2[i - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]



