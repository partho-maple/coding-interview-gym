
import Foundation

class Solution {
    func nextPermutation(_ nums: inout [Int]) {
        guard nums.count >= 2 else {
            return
        }
        
        for leftIdx in stride(from:(nums.count - 2), through:0, by:-1) {
            var leftNum = nums[leftIdx]
            var rightNum = nums[leftIdx + 1]
            if leftNum < rightNum {
                var swapIdx = leftIdx + 1
                for i in (swapIdx..<nums.count) {
                    if leftNum < nums[i] && rightNum > nums[i] {
                        swapIdx = i
                    }
                }
                nums.swapAt(leftIdx, swapIdx)
                nums[(leftIdx + 1)..<nums.count].sort(by: {$0 < $1})
                return
            }
        }
        nums.reverse()
    }
}
