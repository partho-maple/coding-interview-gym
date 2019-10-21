class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverseStringHelper(0, len(s) - 1, s)

    def reverseStringHelper(self, start, end, newS):
        if start >= end:
            return
        newS[start], newS[end] = newS[end], newS[start]
        self.reverseStringHelper(start + 1, end - 1, newS)

