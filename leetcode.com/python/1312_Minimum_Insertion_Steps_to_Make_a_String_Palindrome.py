class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringLenght = len(s)

        # dp[i][j] stores the length of LPS from index 'i' to index 'j'
        dp = [[0 for _ in range(stringLenght)] for _ in range(stringLenght)]

        # every sequence with one element is a palindrome of length 1
        for i in range(stringLenght):
            dp[i][i] = 1

        for startIdx in range(stringLenght - 1, -1, -1):
            for endIdx in range(startIdx + 1, stringLenght):
                if s[startIdx] == s[endIdx]:
                    dp[startIdx][endIdx] = dp[startIdx + 1][endIdx - 1] + 2
                else:
                    dp[startIdx][endIdx] = max(dp[startIdx + 1][endIdx], dp[startIdx][endIdx -1])

        numberOfInsersion = stringLenght - dp[0][-1]
        return numberOfInsersion
