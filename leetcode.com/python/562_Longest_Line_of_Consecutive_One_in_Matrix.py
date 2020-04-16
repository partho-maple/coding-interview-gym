# Approach 1: Brute force. Time limit exceeded. 57 / 57 test cases passed, but took too long.
# # https://tinyurl.com/vqppbae
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rowCount, colCount = len(M), len(M[0]) if M else 0
        if rowCount <= 0 or colCount <= 0:
            return 0
        maxOnes = 0

        # Checks horizontal lines for max ones
        for rowIdx in range(rowCount):
            currentOnes = 0
            for colIdx in range(colCount):
                if M[rowIdx][colIdx] == 1:
                    currentOnes += 1
                    maxOnes = max(maxOnes, currentOnes)
                else:
                    currentOnes = 0

        # Checks vertical lines for max ones
        for colIdx in range(colCount):
            currentOnes = 0
            for rowIdx in range(rowCount):
                if M[rowIdx][colIdx] == 1:
                    currentOnes += 1
                    maxOnes = max(maxOnes, currentOnes)
                else:
                    currentOnes = 0

        # Checks upper diagonal lines for max ones
        for diagonalCol in range(max(rowCount, colCount)):
            currentOnes = 0
            for rowIdx, colIdx in zip(range(rowCount), range(diagonalCol, colCount)):
                if M[rowIdx][colIdx] == 1:
                    currentOnes += 1
                    maxOnes = max(maxOnes, currentOnes)
                else:
                    currentOnes = 0

        # Checks lower diagonal lines for max ones
        for diagonalCol in range(max(rowCount, colCount)):
            currentOnes = 0
            for rowIdx, colIdx in zip(range(diagonalCol, rowCount), range(colCount)):
                if M[rowIdx][colIdx] == 1:
                    currentOnes += 1
                    maxOnes = max(maxOnes, currentOnes)
                else:
                    currentOnes = 0

        # Checks upper anti-diagonal lines for max ones
        for diagonalCol in range(max(rowCount, colCount)):
            currentOnes = 0
            for rowIdx, colIdx in zip(range(rowCount), range(colCount - 1 - diagonalCol, -1, -1)):
                if M[rowIdx][colIdx] == 1:
                    currentOnes += 1
                    maxOnes = max(maxOnes, currentOnes)
                else:
                    currentOnes = 0

        # Checks lower anti-diagonal lines for max ones
        for diagonalCol in range(max(rowCount, colCount)):
            currentOnes = 0
            for rowIdx, colIdx in zip(range(diagonalCol, rowCount), range(colCount - 1, -1, -1)):
                if M[rowIdx][colIdx] == 1:
                    currentOnes += 1
                    maxOnes = max(maxOnes, currentOnes)
                else:
                    currentOnes = 0

        return maxOnes




# Approach 2: Better Brute force. Accepted
# https://tinyurl.com/t3xtfq8
from collections import defaultdict

class Solution(object):
    def longestLine(self, M):
        rowCount, colCount = len(M), len(M[0]) if M else 0
        if rowCount <= 0 or colCount <= 0:
            return 0

        maxOnes = 0
        linesDict = defaultdict(list)
        for rowIdx in range(rowCount):
            for colIdx in range(colCount):
                val = M[rowIdx][colIdx]
                linesDict[0, rowIdx].extend([val])
                linesDict[1, colIdx].extend([val])
                linesDict[2, rowIdx + colIdx].extend([val])
                linesDict[3, rowIdx - colIdx].extend([val])

        for line in linesDict.values():
            currentMaxOnes = self.onesCount(line)
            maxOnes = max(maxOnes, currentMaxOnes)
        return maxOnes

    def onesCount(self, line):
        ans, count = 0, 0
        for num in line:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        return ans


# Approach 3: 3-D Dynamic Programming
# https://tinyurl.com/vqppbae
from collections import defaultdict

class Solution(object):
    def longestLine(self, M):
        rowCount, colCount = len(M), len(M[0]) if M else 0
        if rowCount <= 0 or colCount <= 0:
            return 0

        maxOnes = 0
        dp = [[[0 for _ in range(4)] for _ in range(colCount)] for _ in range(rowCount)]
        for rowIdx in range(rowCount):
            for colIdx in range(colCount):
                val = M[rowIdx][colIdx]
                if val:
                    # 0 = Horizontal, 1 = Vertical, 2 = Diagonal and 3 = Anti-diagonal
                    dp[rowIdx][colIdx][0] = (dp[rowIdx][colIdx - 1][0] + 1) if colIdx > 0 else 1
                    dp[rowIdx][colIdx][1] = (dp[rowIdx - 1][colIdx][1] + 1) if rowIdx > 0 else 1
                    dp[rowIdx][colIdx][2] = (dp[rowIdx - 1][colIdx - 1][2] + 1) if (colIdx > 0 and rowIdx > 0) else 1
                    dp[rowIdx][colIdx][3] = (dp[rowIdx - 1][colIdx + 1][3] + 1) if (colIdx < colCount - 1 and rowIdx > 0) else 1
                    maxOnes = max([maxOnes, dp[rowIdx][colIdx][0], dp[rowIdx][colIdx][1], dp[rowIdx][colIdx][2], dp[rowIdx][colIdx][3]])

        return maxOnes


# My solutions during Leetcode Mock Interview
class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0

        dp = [[[0, 0, 0, 0] for _ in range(len(M[0]) + 2)] for _ in range(len(M) + 1)]
        maxLen = 0
        for i in range(1, len(M) + 1):
            for j in range(1, len(M[0]) + 1):
                if M[i - 1][j - 1] == 1:
                    ho = dp[i][j - 1][0] + 1
                    vt = dp[i - 1][j][1] + 1
                    di = dp[i - 1][j - 1][2] + 1
                    ad = dp[i - 1][j + 1][3] + 1
                    lineLengths = [ho, vt, di, ad]
                    dp[i][j] = lineLengths
                    currentMaxLen = max(lineLengths)
                    maxLen = max(maxLen, currentMaxLen)
        # print("DP: ", dp)
        return maxLen