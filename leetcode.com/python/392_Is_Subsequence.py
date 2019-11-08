from collections import defaultdict
from bisect import bisect_left

# Using Binary search
class Solution(object):
    def createMap(self, s):
        # create a map. key is char. value is index of apperance in acending order.
        posMap = defaultdict(list)
        for i, char in enumerate(s):
            posMap[char].append(i)
        return posMap

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        posMap = self.createMap(t)
        # lowBound is the minimum index the current char has to be at.
        lowBound = 0
        for char in s:
            if char not in posMap: return False
            charIndexList = posMap[char]
            # try to find an index that is larger than or equal to lowBound
            i = bisect_left(charIndexList, lowBound)
            if i == len(charIndexList): return False
            lowBound = charIndexList[i] + 1
        return True


# Using  Two Pointer
# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s) == 0:
#             return True
#         if len(t) == 0:
#             return False
#         i, j = 0, 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return True if i == len(s) else False




sol = Solution()
s = "abc"
t = "ahbgdca"
out = sol.isSubsequence(s, t)
print('Res: ', out)