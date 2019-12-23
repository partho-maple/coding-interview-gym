class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        allCombinations, currentCombinations = [], []
        self.generateCombinations(n, k, 1, currentCombinations, allCombinations)
        return allCombinations

    def generateCombinations(self, n, k, startingNum, currentCombinations, allCombinations):
        if len(currentCombinations) == k:
            allCombinations.append(list(currentCombinations))
            return
        for i in range(startingNum, n + 1):
            currentCombinations.append(i)
            self.generateCombinations(n, k, i + 1, currentCombinations, allCombinations)
            currentCombinations.pop()  # Backtrack




sol = Solution()
n = 2
k = 1
out = sol.combine(n, k)
print("Res: ", out)