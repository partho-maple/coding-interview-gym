import Foundation

// Straight forward DFS. Time limit exceeded
// Time: O(2^(m*n))
class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        return uniquePathHelper((m, n), (0,0))
    }
    
    func uniquePathHelper(_ destinationCoord: (Int, Int), _ currentCoord: (Int, Int)) -> Int {
        if currentCoord == (destinationCoord.0 - 1, destinationCoord.1 - 1) {
            return 1
        }
        if currentCoord.0 >= destinationCoord.0 || currentCoord.1 >= destinationCoord.1 {
            return 0
        }
        
        let right = uniquePathHelper(destinationCoord, (currentCoord.0 + 1, currentCoord.1))
        let down = uniquePathHelper(destinationCoord, (currentCoord.0, currentCoord.1 + 1))
        return right + down
    }
}


// Top-Down with memoizations. Accepted
// Time: O(2^(m*n))
class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        var memo = [String:Int]()
        return uniquePathHelper((m, n), (0,0), &memo)
    }
    
    func uniquePathHelper(_ destinationCoord: (Int, Int), _ currentCoord: (Int, Int), _ memo: inout [String:Int]) -> Int {
        if let value = memo["\(currentCoord.0)-\(currentCoord.1)"] {
            return value
        }
        if currentCoord == (destinationCoord.0 - 1, destinationCoord.1 - 1) {
            return 1
        }
        if currentCoord.0 >= destinationCoord.0 || currentCoord.1 >= destinationCoord.1 {
            return 0
        }
        
        let right = uniquePathHelper(destinationCoord, (currentCoord.0 + 1, currentCoord.1), &memo)
        let down = uniquePathHelper(destinationCoord, (currentCoord.0, currentCoord.1 + 1), &memo)
        memo["\(currentCoord.0)-\(currentCoord.1)"] = right + down
        return right + down
    }
}


// Bottom-Up dp. Accepted
// Time: O(m*n)
class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        var dpTable = Array(repeating: Array(repeating: 1, count: m), count: n)
        for i in 1..<n {
            for j in 1..<m {
                dpTable[i][j] = dpTable[i - 1][j] + dpTable[i][j - 1]
            }
        }
        return dpTable[n - 1][m - 1]
    }
}
