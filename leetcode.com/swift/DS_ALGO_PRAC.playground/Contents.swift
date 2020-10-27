import Foundation
class Solution {
    func minimumEffortPath(_ heights: [[Int]]) -> Int {
        guard !heights.isEmpty, !heights[0].isEmpty else {
            return 0
        }
        var heights = heights
        var minEffort = heights[0][0]
        var queue = Array([0,0])
        while !queue.isEmpty {
            var currentCell = queue.removeFirst()
            var (currentX, currentY) = (currentCell[0], currentCell[1])
            var currentMinEffort = heights[currentX][currentY]
            var currentLevelSize = queue.count
            
            for _ in 0..<currentLevelSize {
                
            }
            minEffort = max(minEffort, currentMinEffort)
        }
    }
}
