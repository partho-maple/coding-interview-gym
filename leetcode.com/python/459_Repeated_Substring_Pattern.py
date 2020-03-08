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
