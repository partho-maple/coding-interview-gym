from collections import defaultdict
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        subStringCount = 0
        couter = {c: 0 for c in 'abc'}
        while right < len(s):
            couter[s[right]] += 1
            while all(couter.values()):
                couter[s[left]] -= 1
                left += 1
            subStringCount += left
            right += 1
        return subStringCount