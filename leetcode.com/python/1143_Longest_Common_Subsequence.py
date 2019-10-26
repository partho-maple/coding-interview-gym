
#   Solution 1
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) < len(text2):
            small = text1
            big = text2
        else:
            small = text2
            big = text1
        subsequences = [[0 for _ in range(len(small) + 1)] for _ in range(len(big) +  1)]
        for i in range(len(big)):
            currentChar = big[i]
            for j in range(len(small)):
                otherChar = small[j]
                if currentChar == otherChar:
                    subsequences[i + 1][j + 1] = subsequences[i][j] + 1
                else:
                    subsequences[i + 1][j + 1] = max(subsequences[i][j + 1], subsequences[i + 1][j])
        return subsequences[-1][-1]



#   Solution 2
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        small, big = sorted((text1, text2), key=len)
        oddRow = [0 for _ in range(len(small) + 1)]
        evenRow = [0 for _ in range(len(small) + 1)]
        for i in range(1, len(big) + 1):
            if i % 2 == 1:
                currentRow = oddRow
                prevRow = evenRow
            else:
                currentRow = evenRow
                prevRow = oddRow
            currentChar = big[i - 1]
            for j in range(1, len(small) + 1):
                otherChar = small[j - 1]
                if currentChar == otherChar:
                    currentRow[j] = prevRow[j - 1] + 1
                else:
                    currentRow[j] = max(currentRow[j - 1], prevRow[j])
        return oddRow[-1] if len(big) % 2 == 1 else evenRow[-1]





sol = Solution()
text1 = "abcde"
text2 = "ace"
output = sol.longestCommonSubsequence(text1, text2)
print('Res: ', output)

