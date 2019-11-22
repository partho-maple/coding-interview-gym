# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            isBad = isBadVersion(mid)
            if isBad:
                right = mid
            else:
                left = mid + 1
        return left
