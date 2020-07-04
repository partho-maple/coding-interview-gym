import Foundation
class Solution {
    func isMonotonic(_ A: [Int]) -> Bool {
        guard A.count > 2 else {
            return true
        }
        var (isIncreasing, isDecreasing) = (true, true)
        
        for i in 2..<A.count {
            if (A[i - 2] <= A[i - 1] && A[i - 1] <= A[i]) {
                continue
            } else {
                isIncreasing = false
                break
            }
        }
        
        for i in 2..<A.count {
            if (A[i - 2] >= A[i - 1] && A[i - 1] >= A[i]) {
                continue
            } else {
                isDecreasing = false
                break
            }
        }
        
        return (isIncreasing || isDecreasing)
    }
}
