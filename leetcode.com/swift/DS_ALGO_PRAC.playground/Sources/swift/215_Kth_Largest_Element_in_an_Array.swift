import Foundation

class Solution {
    func findKthLargest(_ nums: [Int], _ k: Int) -> Int {
        guard nums.count > 1 else {
            return nums.first!
        }
        var start = 0, end = nums.count - 1, nums = nums
        return quickSelectKthLargest(&nums, nums.count - k, &start, &end)
    }
    
    func quickSelectKthLargest(_ nums: inout [Int], _ position: Int, _ start: inout Int, _ end: inout Int) -> Int {
        while start < end {
            var pivotIndex = start, leftIndex = start + 1, rightIndex = end
            while leftIndex <= rightIndex {
                if nums[leftIndex] > nums[pivotIndex] && nums[rightIndex] < nums[pivotIndex] {
                    nums.swapAt(leftIndex, rightIndex)
                }
                if nums[leftIndex] <= nums[pivotIndex] {
                    leftIndex += 1
                }
                if nums[rightIndex] >= nums[pivotIndex] {
                    rightIndex -= 1
                }
            }
            nums.swapAt(pivotIndex, rightIndex)
            if rightIndex == position {
                return nums[rightIndex]
            } else if position < rightIndex {
                end = rightIndex - 1
            } else {
                start = rightIndex + 1
            }
        }
        return nums[start]
    }
}
