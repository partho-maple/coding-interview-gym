class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        allCombinations = []
        self.backtrack("", 0, 0, n, allCombinations)
        return allCombinations


    def backtrack(self, currentCombination, openCount, closeCount, n, allCombinations):
        if len(currentCombination) == n*2:
            allCombinations.append(currentCombination)
            return
        if openCount < n:
            self.backtrack(currentCombination + "(", openCount + 1, closeCount, n, allCombinations)
        if closeCount < openCount:
            self.backtrack(currentCombination + ")", openCount, closeCount + 1, n, allCombinations)


sol = Solution()
input = 3
output = sol.generateParenthesis(input)
print('Res: ', output)