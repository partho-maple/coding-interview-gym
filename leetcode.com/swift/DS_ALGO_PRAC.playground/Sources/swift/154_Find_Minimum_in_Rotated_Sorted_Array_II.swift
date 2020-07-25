import Foundation
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var (leftIdx, rightIdx) = (0, nums.count - 1)
        while leftIdx < rightIdx {
            let midIdx = leftIdx + (rightIdx - leftIdx) / 2
            if nums[midIdx] < nums[rightIdx] {
                rightIdx = midIdx
            } else if nums[midIdx] > nums[rightIdx] {
                leftIdx = midIdx + 1
            } else {
                rightIdx -= 1
            }
        }
        return nums[leftIdx]
    }
}

