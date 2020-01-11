class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringLen = len(s)

        # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
        dp = [[False for _ in range(stringLen)] for _ in range(stringLen)]
        subStringCount = 0

        # every string with one character is a palindrome
        for i in range(stringLen):
            dp[i][i] = 1
            subStringCount += 1

        for startIdx in range(stringLen - 1, -1, -1):
            for endIdx in range(startIdx + 1, stringLen):
                if s[startIdx] == s[endIdx]:
                    # if it's a two character string or if the remaining string is a palindrome too
                    if endIdx - startIdx == 1 or dp[startIdx +  1][endIdx - 1]:
                        dp[startIdx][endIdx] = True
                        subStringCount += 1

        return subStringCount




