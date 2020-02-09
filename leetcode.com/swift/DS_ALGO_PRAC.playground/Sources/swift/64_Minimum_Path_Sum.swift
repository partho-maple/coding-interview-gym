import Foundation

class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        let row = grid.count + 1
        let column = grid[0].count + 1
        var dp = Array(repeating: [Int](repeating: Int.max, count: column), count: row)
        for i in 1 ..< row {
            for j in 1 ..< column {
                var up = dp[i - 1][j]
                var left = dp[i][j - 1]
                var minNum = min(up, left)
                if up == Int.max && left == Int.max {
                    minNum = 0
                }
                var num = minNum + grid[i - 1][j - 1]
                dp[i][j] = num
            }
        }
        return dp[row - 1][column - 1]
    }
}
