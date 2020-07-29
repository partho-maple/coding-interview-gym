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

// BruteForce with memoization. Time: O(arrayLen*3^steps).
class Solution {
    func numWays(_ steps: Int, _ arrLen: Int) -> Int {
        var memo = [String:Int]()
        numWaysDFSHelper(steps, arrLen, 0, 1, &memo)
        print(memo)
        return memo["0-0"] ?? 0
    }
    
    private func numWaysDFSHelper(_ steps: Int, _ arrLen: Int, _ currentIndex: Int, _ currentSteps: Int, _ memo: inout [String:Int]) {
        if let totalwaysFromMemo = memo["\(currentIndex)-\(steps - currentSteps)"] {
            memo["\(currentIndex)-\(steps - currentSteps)"] = totalwaysFromMemo + 1
            return
        }
        if currentSteps > steps {
            if currentIndex == 0 {
                if let totalwaysFromMemo = memo["0-0"] {
                    memo["0-0"] = (totalwaysFromMemo + 1) % (Int(pow(Double(10), Double(9))) + 7)
                } else {
                    memo["0-0"] = 1
                }
            }
            return
        }
        
        for i in [0, -1, 1] {
            let newIndex = currentIndex + i
            if newIndex >= 0 && newIndex < arrLen && newIndex <= steps {
                if let totalwaysFromMemo = memo["\(newIndex)-\(steps - currentSteps - 1)"] {
                    memo["\(newIndex)-\(steps - currentSteps - 1)"] = totalwaysFromMemo + 1
                } else {
                    numWaysDFSHelper(steps, arrLen, newIndex, currentSteps + 1, &memo)
                    memo["\(newIndex)-\(steps - currentSteps - 1)"] = totalwaysFromMemo + 1
                }
            }
        }
    }
}
