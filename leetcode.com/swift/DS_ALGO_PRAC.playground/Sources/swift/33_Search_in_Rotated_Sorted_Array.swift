import Foundation
class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        guard nums.count > 0 else {
            return -1
        }
        var (leftIdx, rightIdx) = (0, nums.count - 1)
        while leftIdx <= rightIdx {
            var midIdx = leftIdx + (rightIdx - leftIdx) / 2
            if nums[midIdx] == target {
                return midIdx
            }
            if nums[leftIdx] <= nums[midIdx] {
                // Left side is sorted
                if nums[leftIdx] < target && target < nums[midIdx]  {
                    rightIdx = midIdx - 1
                } else {
                    leftIdx = midIdx + 1
                }
            } else if nums[rightIdx] > nums[midIdx] {
                // Right side is sorted
                if nums[rightIdx] > target && target < nums[midIdx]  {
                    leftIdx = midIdx + 1
                } else {
                    rightIdx = midIdx + 1
                }
            }
        }
        return -1
    }
}
