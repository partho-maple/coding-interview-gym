# Brute-force solution. TLE
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.minCutHelper(s, 0, len(s) - 1)


    def minCutHelper(self, string, startIdx, endIdx):
        # we don't need to cut the string if it is a palindrome
        if startIdx >= endIdx or self.isPalindrome(string, startIdx, endIdx):
            return 0

        # at max, we need to cut the string into its 'length-1' pieces
        minimumCuts = endIdx - startIdx
        for idx in range(startIdx, endIdx + 1):
            if self.isPalindrome(string, startIdx, idx):
                # we can cut here as we have a palindrome from 'startIndex' to 'i'
                nextCut = self.minCutHelper(string, idx + 1, endIdx)
                minimumCuts = min(minimumCuts, 1 + nextCut)
        return minimumCuts


    def isPalindrome(self, string, startIdx, endIdx):
        while startIdx <= endIdx:
            if string[startIdx] != string[endIdx]:
                return False
            startIdx += 1
            endIdx -= 1
        return True





# Dynamic Programming using memoization solution. Accepted
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        strLen = len(s)
        dpMinCuts = [[-1 for _ in range(strLen)] for _ in range(strLen)]
        dpIsPalingrome = [[-1 for _ in range(strLen)] for _ in range(strLen)]
        return self.minCutHelper(s, 0, strLen - 1, dpMinCuts, dpIsPalingrome)


    def minCutHelper(self, string, startIdx, endIdx, dpMinCuts, dpIsPalingrome):
        # we don't need to cut the string if it is a palindrome
        if startIdx >= endIdx or self.isPalindrome(string, startIdx, endIdx, dpIsPalingrome):
            return 0

        if dpMinCuts[startIdx][endIdx] == -1:
            # at max, we need to cut the string into its 'length-1' pieces
            minimumCuts = endIdx - startIdx
            for idx in range(startIdx, endIdx + 1):
                if self.isPalindrome(string, startIdx, idx, dpIsPalingrome):
                    # we can cut here as we have a palindrome from 'startIndex' to 'i'
                    nextCut = self.minCutHelper(string, idx + 1, endIdx, dpMinCuts, dpIsPalingrome)
                    minimumCuts = min(minimumCuts, 1 + nextCut)
            dpMinCuts[startIdx][endIdx] = minimumCuts

        return dpMinCuts[startIdx][endIdx]


    def isPalindrome(self, st, x, y, dpIsPalindrome):
        if dpIsPalindrome[x][y] == -1:
            dpIsPalindrome[x][y] = 1
            i, j = x, y
            while i < j:
                if st[i] != st[j]:
                    dpIsPalindrome[x][y] = 0
                    break
                i += 1
                j -= 1
                # use memoization to find if the remaining string is a palindrome
                if i < j and dpIsPalindrome[i][j] != -1:
                    dpIsPalindrome[x][y] = dpIsPalindrome[i][j]
                    break

        return True if dpIsPalindrome[x][y] == 1 else False




# Dynamic Programming using Bottom-Up solution. Accepted
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        strLen = len(s)

        # isPalindrome[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
        dpIsPalingrome = [[False for _ in range(strLen)] for _ in range(strLen)]

        # every string with one character is a palindrome
        for i in range(strLen):
            dpIsPalingrome[i][i] = True

        # populate isPalindrome table
        for strIdx in range(strLen - 1, -1, -1):
            for endIdx in range(strIdx + 1, strLen):
                if s[strIdx] == s[endIdx]:
                    # if it's a two character string or if the remaining string is a palindrome too
                    if endIdx - strIdx == 1 or dpIsPalingrome[strIdx + 1][endIdx - 1]:
                        dpIsPalingrome[strIdx][endIdx] = True

        # now lets populate the second table, every index in 'dpMinCuts' stores the minimum cuts needed
        # for the substring from that index till the end
        dpMinCuts = [0 for _ in range(strLen)]
        for strIdx in range(strLen - 1, -1, -1):
            minCuts = strLen  # maximum cuts
            for endIdx in range(strLen - 1, strIdx - 1, -1):
                if dpIsPalingrome[strIdx][endIdx]:
                    # we can cut here as we got a palindrome
                    # also we don't need any cut if the whole substring is a palindrome
                    minCuts = 0 if endIdx == strLen - 1 else min(minCuts, 1 + dpMinCuts[endIdx + 1])
            dpMinCuts[strIdx] = minCuts
        return dpMinCuts[0]






