import Foundation
class Solution {
    func longestOnes(_ A: [Int], _ K: Int) -> Int {
        var (left, right, currentK, maxLength) = (0, 0, K, 0)
        while left <= right, right < A.count {
            if A[right] == 1 {
                right += 1
            } else {
                if currentK > 0 {
                    right += 1
                    currentK -= 1
                } else {
                    // Window shrinking
                    if A[left] == 0 {
                        if currentK < K {
                            currentK += 1
                        } else {
                            right += 1
                        }
                    }
                    left += 1
                }
            }
            maxLength = max(maxLength, (right - left))
        }
        return maxLength
    }
}
