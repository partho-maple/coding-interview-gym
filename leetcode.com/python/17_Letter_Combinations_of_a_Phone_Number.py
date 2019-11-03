class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        result = []
        if digits:
            self.backtrack("", digits, phone, result)
        return result

    def backtrack(self, combination, nextDigits, alphaDigitalMap, cache):
        if len(nextDigits) == 0:
            cache.append(combination)
        else:
            for letter in alphaDigitalMap[nextDigits[0]]:
                self.backtrack(combination + letter, nextDigits[1:], alphaDigitalMap, cache)




sol = Solution()
input = "23"
output = sol.letterCombinations(input)
print('Res: ', output)