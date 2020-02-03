# Approach 1: Recursion.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.uniquePathsHelper(m, 0, n, 0, 0)


    def uniquePathsHelper(self, m, currentM, n, currentN, paths):
        if (currentN, currentM) == (n - 1, m - 1):
            return paths + 1
        if currentM >= m or currentN >= n:
            return paths
        down = self.uniquePathsHelper(m, currentM, n, currentN + 1, paths)
        right = self.uniquePathsHelper(m, currentM + 1, n, currentN, paths)
        return down + right


# Approach 2: Recursion with memoization. Source: https://tinyurl.com/tvolzor
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = {}
        return self.uniquePathsHelper(m, n, memo)

    def uniquePathsHelper(self, m, n, memo):
        if (m, n) in memo:
            return memo[(m, n)]
        elif m == 1 or n == 1:
            return 1
        up = self.uniquePathsHelper(m, n - 1, memo)
        left = self.uniquePathsHelper(m - 1, n, memo)
        memo[(m, n)] = up + left
        return memo[(m, n)]




# Approach 3: DP. Source: https://tinyurl.com/tvolzor
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j - 1] +  dp[i - 1][j]
        return dp[-1][-1]