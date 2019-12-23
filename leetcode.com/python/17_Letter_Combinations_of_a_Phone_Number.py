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
        allCombination = []
        if digits:
            self.backtrack("", digits, phone, allCombination)
        return allCombination

    def backtrack(self, currentCombination, leftoverDigits, alphaDigitalMap, allCombination):
        if len(leftoverDigits) == 0:
            allCombination.append(currentCombination)
        else:
            for letter in alphaDigitalMap[leftoverDigits[0]]:

                # # Use this one line. Or the following 3 line code
                # self.backtrack(currentCombination + letter, leftoverDigits[1:], alphaDigitalMap, allCombination)

                currentCombination += letter
                self.backtrack(currentCombination, leftoverDigits[1:], alphaDigitalMap, allCombination)
                currentCombination = currentCombination[:-1]  # Backtrack, remove last character from currentCombination




sol = Solution()
input = "23"
output = sol.letterCombinations(input)
print('Res: ', output)