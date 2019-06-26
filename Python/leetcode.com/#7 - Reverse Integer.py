class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0
        reverseStr = ''
        isPositive = True
        if x < 0:
            x = x * (-1)
            isPositive = False
        elif x == 0:
            return 0
        while x / 10 >= 1:
            mod = x % 10
            x = x // 10
            if mod == 0 and reverseStr is '':
                continue
            reverseStr = str(reverseStr) + str(mod)
        if x > 0:
            reverseStr = str(reverseStr) + str(x)
        if isPositive:
            reverseInt = int(reverseStr)
        else:
            reverseInt = int(reverseStr) * (-1)
        if reverseInt >= 2 ** 31 - 1 or reverseInt <= -2 ** 31:
            return 0
        else:
            return reverseInt


sol = Solution()
inputInt = 1534236469
reverseInt = sol.reverse(inputInt)
print("Reverse Int: ", reverseInt)