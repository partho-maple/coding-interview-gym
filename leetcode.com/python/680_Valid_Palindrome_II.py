# Dynamic Programming approach.  TLE
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
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

        if (stringLenght <= dp[0][-1] + 1):
            return True
        else:
            return False




# Two Pointer approach.  Accepted
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True
