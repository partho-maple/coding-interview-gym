import itertools
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        possibilities = sorted(list(itertools.permutations(sorted(A))), reverse=True)
        for i in possibilities:
            a, b, c, d = i
            hours = (a * 10 + b)
            minuites = (c * 10 + d)
            if hours < 24 and minuites < 60:
                return "{}{}:{}{}".format(a, b, c, d)
        return ""
