class Solution(object):

    #   Solution 1
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if (n & (~n + 1)) == n:  # ~n + 1 = -n
            return True
        else:
            return False


