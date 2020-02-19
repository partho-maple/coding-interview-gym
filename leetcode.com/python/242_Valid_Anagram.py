from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sCounter = Counter(s)
        tCounter = Counter(t)
        return sCounter == tCounter

