import Foundation
//class Solution {
//    func minimumEffortPath(_ heights: [[Int]]) -> Int {
//        guard !heights.isEmpty, !heights[0].isEmpty else {
//            return 0
//        }
//
//        var visited = Set<String>()
//        visited.insert("0-0")
//        var (path, minPath) = ([heights[0][0]], heights[0][0])
//
//        minimumEffortPathDFSHelper(heights, path, &minPath, 0, 0, &visited)
//        return minPath
//    }
//
//    func minimumEffortPathDFSHelper(_ heights: [[Int]], _ path: [Int], _ minPath: inout Int, _ currentX: Int, _ currentY: Int, _ visited: inout Set<String>) {
//        print("currentX: \(currentX), currentY: \(currentY)")
//        if currentX == heights.count - 1 && currentY == heights[0].count - 1 {
//            minPath = min(minPath, path.max()!)
//            print("path: \(path)")
//            return
//        }
//        print("------")
//        for neighbor in [(-1,0),(0,1),(1,0),(0,-1)] {
//            var (newX, newY) = (currentX + neighbor.0, currentY + neighbor.1)
//            if newX >= 0 && newX < heights.count && newY >= 0 && newY < heights[newX].count && !visited.contains("\(newX)-\(newY)") {
//                var currVal = heights[newX][newY]
//                var prevVal = heights[currentX][currentY]
//
//                visited.insert("\(newX)-\(newY)")
//                minimumEffortPathDFSHelper(heights, path + [abs(prevVal - currVal)], &minPath, newX, newY, &visited)
//                visited.remove("\(newX)-\(newY)")
//            }
//        }
//    }
//}

/*
 [
 [1,2,1,1,1],
 [1,2,1,2,1],
 [1,2,1,2,1],
 [1,2,1,2,1],
 [1,1,1,2,1]]
 */



class Solution {
    func numSubmat(_ mat: [[Int]]) -> Int {
        guard !mat.isEmpty && !mat.first?.isEmpty else {
            return 0
        }
        var dp = Array(repeating: Array(repeating: 0, count: mat.first?.count + 1), count: mat.count + 1)
        var numSubmat = 0
        for i in 1...mat.count {
            for j in 1...mat.first?.count {
                if mat[i - 1][j - 1] == 1 {
                    var currentCount = 0
                    if dp[i - 1][j] == 1 {
                        currentCount += dp[i - 1][j]
                        currentCount += 1
                    }
                    if dp[i - 1][j - 1] == 1 {
                        currentCount += dp[i - 1][j - 1]
                        currentCount += 1
                    }
                    if dp[i][j - 1] == 1 {
                        currentCount += dp[i][j - 1]
                        currentCount += 1
                    }
                    
                    dp[i][j] = currentCount
                    numSubmat = max(numSubmat, dp[i][j])
                }
            }
        }
        return currentCount
    }
}
