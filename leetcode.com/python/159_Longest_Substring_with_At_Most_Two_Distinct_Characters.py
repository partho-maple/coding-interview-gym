from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) <= 0:
            return 0
        charCountDict = defaultdict(int)
        k, startIdx = 2, 0
        longestSubStrLen = 0
        for endIdx, currentChar in enumerate(s):
            if len(charCountDict) < k:
                charCountDict[currentChar] += 1
            elif len(charCountDict) == k:
                if currentChar in charCountDict:
                    charCountDict[currentChar] += 1
                else:
                    while len(charCountDict) == k:
                        charToRemove = s[startIdx]
                        charCountDict[charToRemove] -= 1
                        if charCountDict[charToRemove] == 0:
                            del charCountDict[charToRemove]
                        startIdx += 1
                    charCountDict[currentChar] = 1
            longestSubStrLen = max(longestSubStrLen, endIdx - startIdx + 1)
        return longestSubStrLen

