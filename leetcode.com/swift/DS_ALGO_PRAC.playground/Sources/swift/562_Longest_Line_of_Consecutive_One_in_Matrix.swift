class Solution {
    func longestLine(_ M: [[Int]]) -> Int {
        guard M.count > 0 else {
            return 0
        }
        var dp = Array(repeating: Array(repeating: [0,0,0,0], count: (M[0].count + 1)), count: (M.count + 1))
        var maxLen = 0
        for i in 0..<M.count {
            for j in 0..<M[i].count {
                let currentNum = M[i][j]
                if currentNum == 1 {
                    var partialResult = [1,1,1,1]
                    
                    partialResult[0] += dp[i + 1][j][0]
                    partialResult[1] += dp[i][j][1]
                    partialResult[2] += dp[i][j + 1][2]
                    if j < M[i].count - 1 {
                        partialResult[3] += dp[i][j + 2][3]
                    }
                    
                    dp[i + 1][j + 1] = partialResult
                    maxLen = max(maxLen, partialResult.max()!)
                }
            }
        }
        return maxLen
    }
}
