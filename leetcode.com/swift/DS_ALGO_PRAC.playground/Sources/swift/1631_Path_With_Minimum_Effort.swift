import Foundation

// Simple DFS. TLE
class Solution {
    func minimumEffortPath(_ heights: [[Int]]) -> Int {
        guard !heights.isEmpty, !heights[0].isEmpty else {
            return 0
        }
        
        var visited = Set<String>()
        visited.insert("0-0")
        var (path, minPath) = ([0], Int.max)
        
        minimumEffortPathDFSHelper(heights, path, &minPath, 0, 0, &visited)
        return minPath
    }
    
    func minimumEffortPathDFSHelper(_ heights: [[Int]], _ path: [Int], _ minPath: inout Int, _ currentX: Int, _ currentY: Int, _ visited: inout Set<String>) {
        if currentX == heights.count - 1 && currentY == heights[0].count - 1 {
            minPath = min(minPath, path.max()!)
            return
        }
        for neighbor in [(-1,0),(0,1),(1,0),(0,-1)] {
            var (newX, newY) = (currentX + neighbor.0, currentY + neighbor.1)
            if newX >= 0 && newX < heights.count && newY >= 0 && newY < heights[newX].count && !visited.contains("\(newX)-\(newY)") {
                var currVal = heights[newX][newY]
                var prevVal = heights[currentX][currentY]
                let diff = abs(prevVal - currVal)
                if diff < minPath {
                    visited.insert("\(newX)-\(newY)")
                    minimumEffortPathDFSHelper(heights, path + [diff], &minPath, newX, newY, &visited)
                    visited.remove("\(newX)-\(newY)")
                }
            }
        }
    }
}
