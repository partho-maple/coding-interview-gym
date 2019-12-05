from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Counter = Counter(s1)
        s2Counter = Counter(s2[:len(s1) - 1])
        for right in range(len(s1) - 1, len(s2)):
            s2Counter[s2[right]] += 1
            if s1Counter == s2Counter:
                return True
            s2Counter[s2[right - len(s1) + 1]] -= 1
            if s2Counter[s2[right - len(s1) + 1]] == 0:
                del s2Counter[s2[right - len(s1) + 1]]
        return False

