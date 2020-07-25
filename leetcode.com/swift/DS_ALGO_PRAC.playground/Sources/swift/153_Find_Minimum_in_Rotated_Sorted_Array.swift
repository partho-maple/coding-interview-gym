import Foundation
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var (leftIdx, rightIdx) = (0, nums.count - 1)
        var currentMin = Int.max
        while leftIdx <= rightIdx {
            let midIdx = leftIdx + (rightIdx - leftIdx) / 2
            if nums[leftIdx] <= nums[midIdx] {
                // Left side is sorted
                currentMin = min(currentMin, nums[leftIdx])
                leftIdx = midIdx + 1
            } else {
                if nums[rightIdx] >= nums[midIdx] {
                    // Right side is sorted
                    currentMin = min(currentMin, nums[midIdx])
                    rightIdx = midIdx - 1
                } else {
                    currentMin = min(currentMin, nums[midIdx])
                }
            }
        }
        return currentMin
    }
}
