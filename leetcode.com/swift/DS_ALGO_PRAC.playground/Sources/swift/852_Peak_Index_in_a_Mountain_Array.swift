import Foundation

class Solution {
    func peakIndexInMountainArray(_ A: [Int]) -> Int {
        var leftIdx = 0, rightIdx = A.count - 1
        while leftIdx < rightIdx {
            var midIdx = leftIdx + Int((rightIdx - leftIdx) / 2)
            if A[midIdx] < A[midIdx + 1] {
                leftIdx = midIdx + 1
            } else {
                rightIdx = midIdx
            }
        }
        return leftIdx
    }
}
