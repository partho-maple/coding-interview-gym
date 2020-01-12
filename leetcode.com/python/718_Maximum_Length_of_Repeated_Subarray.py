class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lenA, lenB = len(A), len(B)
        dp = [[0 for _ in range(lenA + 1)] for _ in range(lenB + 1)]
        maxLength = 0
        for i in range(1, lenB + 1):
            for j in range(1, lenA + 1):
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    maxLength = max(maxLength, dp[i][j])
        return maxLength
