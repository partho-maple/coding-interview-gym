class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combinations = []
        self.backtrack("", 0, 0, n, combinations)
        return combinations

    def backtrack(self, string, openCount, closeCount, maxcount, combinations):
        if len(string) == maxcount*2:
            combinations.append(string)
            return
        if openCount < maxcount:
            self.backtrack(string + "(", openCount + 1, closeCount, maxcount, combinations)
        if closeCount < openCount:
            self.backtrack(string + ")", openCount, closeCount + 1, maxcount, combinations)


sol = Solution()
input = 3
output = sol.generateParenthesis(input)
print('Res: ', output)