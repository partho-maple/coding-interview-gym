import Foundation
class Solution {
    func countSquares(_ matrix: [[Int]]) -> Int {
        let (rows, cols) = (matrix.count, matrix[0].count)
        guard rows > 0, cols > 0 else {
            return 0
        }
        var dp = matrix
        var result = 0
        for i in 0..<rows {
            for j in 0..<cols {
                if matrix[i][j] == 1 {
                    if i == 0 || j == 0 {
                        result += 1
                    } else {
                        var cellValue = 1
                        if let minNeighbour = [ dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j] ].min() {
                            cellValue += minNeighbour
                        }
                        result += cellValue
                        dp[i][j] = cellValue
                    }
                }
            }
        }
        return result
    }
}
