import Foundation

// BruteForce. Time: O(arrayLen*3^steps). TLE. 12 / 31 test cases passed.
class Solution {
    func numWays(_ steps: Int, _ arrLen: Int) -> Int {
        var totalWays = 0
        numWaysDFSHelper(steps, arrLen, 0, 1, &totalWays)
        return totalWays
    }
    
    private func numWaysDFSHelper(_ steps: Int, _ arrLen: Int, _ currentIndex: Int, _ currentSteps: Int, _ totalWays: inout Int) {
        if currentSteps > steps {
            if currentIndex == 0 {
                totalWays += 1
                totalWays = totalWays % (Int(pow(Double(10), Double(9))) + 7)
            }
            return
        }
        
        for i in [0, -1, 1] {
            let newIndex = currentIndex + i
            if newIndex >= 0 && newIndex < arrLen {
                numWaysDFSHelper(steps, arrLen, newIndex, currentSteps + 1, &totalWays)
            }
        }
    }
}

//Source: https://tinyurl.com/yynv9xe2
// DFS with memo. Accepted
class Solution {
    func numWays(_ steps: Int, _ arrLen: Int) -> Int {
        if steps < 0 || arrLen <= 0 {
            return 0
        }
        var memo = [String:Int]()
        return numWaysDFSHelper(steps, arrLen, 0, &memo)
    }
    
    private func numWaysDFSHelper(_ remainingSteps: Int, _ arrLen: Int, _ currentIndex: Int, _ memo: inout [String:Int]) -> Int {
        if let totalwaysFromMemo = memo["\(currentIndex)-\(remainingSteps)"] {
            return totalwaysFromMemo
        }
        if currentIndex < 0 || currentIndex > arrLen - 1 {
            memo["\(currentIndex)-\(remainingSteps)"] = 0
            return 0
        }
        if remainingSteps == 0 {
            if currentIndex == 0 {
                return 1
            } else {
                return 0
            }
        }
        
        var currentWays = 0
        for i in [0, -1, 1] {
            let newIndex = currentIndex + i
            if newIndex >= 0 && newIndex < arrLen {
                currentWays += numWaysDFSHelper(remainingSteps - 1, arrLen, newIndex, &memo)
            }
        }
        memo["\(currentIndex)-\(remainingSteps)"] = currentWays % (Int(pow(Double(10), Double(9))) + 7)
        return memo["\(currentIndex)-\(remainingSteps)"]!
    }
}


//Source: https://tinyurl.com/yynv9xe2
// DP
import Foundation
class Solution {
    func numWays(_ steps: Int, _ arrLen: Int) -> Int {
        if steps < 0 || arrLen <= 0 {
            return 0
        }
        var dp = Array(repeating: Array(repeating: 0, count: arrLen), count: (steps + 1))
        dp[0][0] = 1
        for i in 1...steps {
            for j in 0..<arrLen {
                dp[i][j] += dp[i - 1][j]
                if j > 0 {
                    dp[i][j] += dp[i - 1][j - 1]
                }
                if j < arrLen - 1 {
                    dp[i][j] += dp[i - 1][j + 1]
                }
            }
        }
        return dp[steps][0] % (Int(pow(Double(10), Double(9))) + 7)
    }
}
