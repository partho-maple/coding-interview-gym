class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carrry = 0
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            if i == len(digits) - 1:
                num += 1

            if num + carrry > 9:
                if i == 0:
                    result.append((num + carrry) % 10)
                    result.append((num + carrry) // 10)
                else:
                    result.append(0)
                    carrry = 1
            else:
                result.append(num + carrry)
                carrry = 0
        return reversed(result)
