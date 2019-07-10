
# Generalized anser. Memory limit exceded
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        edits = [[x for x in range(len(s) + 1)] for y in range(len(t) + 1)]
        for i in range(1, len(t) + 1):
            edits[i][0] = edits[i - 1][0] + 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    edits[i][j] = edits[i - 1][j - 1]
                else:
                    edits[i][j] = 1 + min(edits[i][j - 1], edits[i - 1][j - 1], edits[i - 1][j])
        return True if edits[-1][-1] == 1 else False


# Accepeted answer
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        if len(t) - len(s) > 1 or s == t:
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]
        return True
