# from collections import defaultdict
# class Solution(object):
#     def lengthOfLongestSubstringKDistinct(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         if not s or len(s) <= 0 or not k or k == 0:
#             return 0
#         charCountDict = defaultdict(int)
#         startIdx = 0
#         longestSubStrLen = 0
#         for endIdx, currentChar in enumerate(s):
#             if len(charCountDict) < k:
#                 charCountDict[currentChar] += 1
#             elif len(charCountDict) == k:
#                 if currentChar in charCountDict:
#                     charCountDict[currentChar] += 1
#                 else:
#                     while len(charCountDict) == k:
#                         charToRemove = s[startIdx]
#                         charCountDict[charToRemove] -= 1
#                         if charCountDict[charToRemove] == 0:
#                             del charCountDict[charToRemove]
#                         startIdx += 1
#                     charCountDict[currentChar] = 1
#             longestSubStrLen = max(longestSubStrLen, endIdx - startIdx + 1)
#         return longestSubStrLen


# My solution during Mock
from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) <= 0 or k == 0:
            return 0
        left, right, maxLen = 0, 0, float("-inf")
        frequencies = defaultdict(int)
        while right < len(s):
            frequencies[s[right]] += 1
            while len(frequencies) > k:
                frequencies[s[left]] -= 1
                if frequencies[s[left]] == 0:
                    del frequencies[s[left]]
                left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen


"""
length of the longest substring contains at most k distinct characters >> longest substring 

"eceba"

e:1
b:1
"""