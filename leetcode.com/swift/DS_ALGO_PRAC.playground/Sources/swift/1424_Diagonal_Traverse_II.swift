import Foundation
class Solution {
    func findDiagonalOrder(_ nums: [[Int]]) -> [Int] {
        var result = [Int]()
        var nodeQueue = [(nums[0][0], 0, 0)]
        var visitedCellSet = Set<String>()
        visitedCellSet.insert("\(0)-\(0)")
        while !nodeQueue.isEmpty {
            var currentLevelLength = nodeQueue.count
            while currentLevelLength > 0 {
                currentLevelLength -= 1
                var (value, row, col) = nodeQueue.removeFirst()
                result.append(value)
                for neighbour in [(1,0),(0,1)] {
                    var (newRow, newCol) = (row + neighbour.0, col + neighbour.1)
                    if newRow < nums.count && newCol < nums[newRow].count && !visitedCellSet.contains("\(newRow)-\(newCol)") {
                        nodeQueue.append((nums[newRow][newCol], newRow, newCol))
                        visitedCellSet.insert("\(newRow)-\(newCol)")
                    }
                }
            }
        }
        return result
    }
}
