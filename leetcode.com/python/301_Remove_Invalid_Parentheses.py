import sys

# Approach 1: simple backtracking with DFS  - S0urce:   https://tinyurl.com/rbp6xa7
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        resultSet = set()
        minRemovalCount = sys.maxsize
        self.calculateRemovalDFS(s, 0, 0, [], 0, 0, minRemovalCount, resultSet)
        return list(resultSet)


    def calculateRemovalDFS(self, originalString, leftParenCout, rightPareCount, currentStringArr, currentRemovalCount, currentIndex, minRemovalCount, resultSet):
        if currentIndex == len(originalString):
            if currentRemovalCount == minRemovalCount and leftParenCout == rightPareCount:
                resultSet.add("".join(currentStringArr))
                return
            else:
                if currentRemovalCount < minRemovalCount and leftParenCout == rightPareCount:
                    minRemovalCount = currentRemovalCount
                    resultSet.clear()
                    resultSet.add("".join(currentStringArr))
                    return
            return
        if originalString[currentIndex] != '(' and originalString[currentIndex] != ')':
            self.calculateRemovalDFS(originalString, leftParenCout, rightPareCount, currentStringArr.append(originalString[currentIndex]), currentRemovalCount, currentIndex + 1, minRemovalCount, resultSet)
            currentStringArr.pop()
        else:
            self.calculateRemovalDFS(originalString, leftParenCout, rightPareCount, currentStringArr, currentRemovalCount + 1, currentIndex + 1, minRemovalCount, resultSet)
            currentStringArr.append(originalString[currentIndex])
            if originalString[currentIndex] == '(':
                self.calculateRemovalDFS(originalString, leftParenCout + 1, rightPareCount, currentStringArr, currentRemovalCount, currentIndex + 1, minRemovalCount, resultSet)
            elif originalString[currentIndex] == ')' and leftParenCout > rightPareCount:
                self.calculateRemovalDFS(originalString, leftParenCout, rightPareCount + 1, currentStringArr, currentRemovalCount, currentIndex + 1, minRemovalCount, resultSet)
            currentStringArr.pop()





sol = Solution()
input = "()())()"
out = sol.removeInvalidParentheses(input)
print("Res: ", out)







