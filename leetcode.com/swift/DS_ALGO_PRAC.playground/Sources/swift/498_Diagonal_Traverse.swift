import Foundation

class Solution {
    func findDiagonalOrder(_ matrix: [[Int]]) -> [Int] {
        var result = [Int]()
        var (rowCount, colCount) = (matrix.count, 0)
        guard rowCount > 0 else {
            return result
        }
        colCount = matrix[0].count
        var (direction, currentRow, currentCol) = (0, 0, 0) // 0 means up and 1 means down
        for _ in 1...(rowCount * colCount) {
            result.append(matrix[currentRow][currentCol])
            if direction == 0 {
                // going up
                for (index, item) in [(-1, 1),(0, 1),(1, 0)].enumerated() {
                    let (newRow, newCol) = (item.0 + currentRow, item.1 + currentCol)
                    if newRow >= 0, newRow < rowCount,  newCol >= 0, newCol < colCount {
                        (currentRow, currentCol) = (newRow, newCol)
                        if index == 1 || index == 2 {
                            direction = 1
                        }
                        break
                    }
                }
            } else {
                // doing down
                for (index, item) in [(1, -1),(1, 0),(0, 1)].enumerated() {
                    let (newRow, newCol) = (item.0 + currentRow, item.1 + currentCol)
                    if newRow >= 0, newRow < rowCount,  newCol >= 0, newCol < colCount {
                        (currentRow, currentCol) = (newRow, newCol)
                        if index == 1 || index == 2 {
                            direction = 0
                        }
                        break
                    }
                }
            }
        }
        return result
    }
}
