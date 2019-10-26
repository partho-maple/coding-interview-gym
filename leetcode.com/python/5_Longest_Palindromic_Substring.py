class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        currentLongest = [0, 1]
        for i in range(1, len(s)):
            odd = self.getLongestPalindromeFrom(s, i - 1, i + 1)
            even = self.getLongestPalindromeFrom(s, i - 1, i)
            longest = max(odd, even, key = lambda x: x[1] - x[0])
            currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
        return s[currentLongest[0]:currentLongest[1]]


    def getLongestPalindromeFrom(self, string, leftIdx, rightIdx):
        while leftIdx >= 0 and rightIdx < len(string):
            if string[leftIdx] != string[rightIdx]:
                break
            else:
                leftIdx -= 1
                rightIdx += 1
        return [leftIdx + 1, rightIdx]