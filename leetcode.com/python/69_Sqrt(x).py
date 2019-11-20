class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left, right = 0, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
        return right




sol = Solution()
x = 6
out = sol.mySqrt(x)
print("Res: ", out)