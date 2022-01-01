import Foundation

// My first attempt
class Solution {
    func nextPermutation(_ nums: inout [Int]) {
        guard nums.count >= 2 else {
            return
        }
        
        for leftIdx in stride(from:(nums.count - 2), through:0, by:-1) {
            let leftNum = nums[leftIdx], rightNum = nums[leftIdx + 1]
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


// My second attempt
class Solution {
    func nextPermutation(_ nums: inout [Int]) {
        guard nums.count > 1 else {
            return
        }
        for rightIdx in stride(from: nums.count - 1, through: 1, by: -1) {
            let rightNum = nums[rightIdx], leftNum = nums[rightIdx - 1]
            if rightNum > leftNum {
                var swapIdx = rightIdx, nextGraterNum = rightNum
                for j in swapIdx..<nums.count {
                    if leftNum < nums[j] && nums[j] < nextGraterNum  {
                        swapIdx = j
                        nextGraterNum = nums[j]
                    }
                }
                nums.swapAt(rightIdx - 1, swapIdx)
                nums[rightIdx..<nums.count].sort()
                return
            }
        }
        nums.sort()
    }
}
