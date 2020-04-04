class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        ss = s + s
        ss = ss[1:-1]
        return ss.find(s) != -1



# My solution duting Mock contest
from collections import Counter
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 0:
            return False
        L = len(s)
        for i in range(L // 2):
            if L % (i + 1) == 0:
                pieces = []
                for j in range(0, L, i + 1):
                    pieces.append(s[j:j + i + 1])
                counter = Counter(pieces)
                if len(counter) == 1:
                    return True
        return False