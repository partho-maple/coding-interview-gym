# Approach 1: Brute Force using simple recursion. TLE
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.minPathSumHelper(grid, 0, 0)

    def minPathSumHelper(self, grid, currentRow, currentCol):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid) - 1
        col = len(grid[0]) - 1
        if (currentRow == row) and (currentCol == col):
            return grid[currentRow][currentCol]
        if currentRow > row or currentCol > col:
            return float('inf')
        bottomPathSum = self.minPathSumHelper(grid, currentRow + 1, currentCol)
        rightPathSum = self.minPathSumHelper(grid, currentRow, currentCol + 1)
        minPath = min(bottomPathSum, rightPathSum)
        return grid[currentRow][currentCol] + minPath



# Approach 2: Top-Down DP recursion and memoization.  Accepted
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cache = {}
        return self.minPathSumHelper(grid, 0, 0, cache)

    def minPathSumHelper(self, grid, currentRow, currentCol, cache):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        key = str(currentRow) + " - " + str(currentCol)
        if key in cache:
            return cache[key]
        row = len(grid) - 1
        col = len(grid[0]) - 1
        if (currentRow == row) and (currentCol == col):
            return grid[currentRow][currentCol]
        if currentRow > row or currentCol > col:
            return float('inf')
        bottomPathSum = self.minPathSumHelper(grid, currentRow + 1, currentCol, cache)
        rightPathSum = self.minPathSumHelper(grid, currentRow, currentCol + 1, cache)
        minPath = min(bottomPathSum, rightPathSum)
        path = grid[currentRow][currentCol] + minPath
        cache[key] = path
        return cache[key]





# Approach 3: Bottom-Up tabulation DP.  Accepted
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[float('inf') for _ in range(len(grid[0]) + 1)] for _ in range(len(grid) + 1)]
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                up = dp[i - 1][j]
                left = dp[i][j - 1]
                minNum = min(up, left)
                if (up == float('inf') and left == float('inf')):
                    minNum = 0
                num = minNum + grid[i - 1][j - 1]
                dp[i][j] = num
        return dp[-1][-1]

