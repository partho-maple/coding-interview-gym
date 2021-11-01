// Brute force
class Solution {
    func maxPoints(_ points: [[Int]]) -> Int {
        guard points.count > 1 else {
            return points[0].max()!
        }
        var (prevRowDP, currentRowDP) = (points[0], Array(repeating: Int.min, count: points[0].count))
        for row in 1..<points.count {
            for col in 0..<points[0].count {
                for prevCol in 0..<prevRowDP.count {
                    currentRowDP[col] = [currentRowDP[col], points[row][col] + prevRowDP[prevCol] - abs(col - prevCol)].max()!
                }
            }
            prevRowDP = currentRowDP
        }
        return currentRowDP.max()!
    }
}

// DP. Main algorithm from here, https://tinyurl.com/yg6hs4md
class Solution {
    func maxPoints(_ points: [[Int]]) -> Int {
        if points.count == 1 {
            return points[0].max()!
        }
        if points[0].count == 1 {
            return points.compactMap { $0.reduce(0, +) }.reduce(0, +)
        }
        
        var prevRowDP = points[0]
        for row in 0..<points.count - 1 {
            var currentRowDP = Array(repeating: 0, count: points[0].count)

            // Build left
            var left = [prevRowDP[0]] + Array(repeating: 0, count: prevRowDP.count - 1)
            for index in 1..<left.count {
                left[index] = [prevRowDP[index], left[index - 1] - 1].max()!
            }
            
            // Build right
            var right = Array(repeating: 0, count: prevRowDP.count - 1) + [prevRowDP.last!]
            for index in stride(from: right.count - 2, through: 0, by: -1) {
                right[index] = [prevRowDP[index], right[index + 1] - 1].max()!
            }
            
            
            for col in 0..<prevRowDP.count {
                currentRowDP[col] = [left[col], right[col]].max()! + points[row + 1][col]
            }
            prevRowDP = currentRowDP
        }
        return prevRowDP.max()!
    }
}
