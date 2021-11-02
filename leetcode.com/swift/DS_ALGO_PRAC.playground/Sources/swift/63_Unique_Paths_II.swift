class Solution {
    func uniquePathsWithObstacles(_ obstacleGrid: [[Int]]) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: obstacleGrid[0].count + 1), count: obstacleGrid.count + 1)
        for i in 0..<obstacleGrid.count {
            for j in 0..<obstacleGrid[0].count {
                if obstacleGrid[i][j] == 0 {
                    if i == 0 && j == 0 {
                        dp[i + 1][j + 1] = 1
                    } else {
                        dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
                    }
                }
            }
        }
        return dp.last!.last!
    }
}
