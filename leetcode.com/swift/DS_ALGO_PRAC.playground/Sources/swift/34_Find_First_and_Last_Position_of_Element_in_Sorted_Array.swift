import Foundation

class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        var result = [-1, -1]
        var (left, right) = (0, nums.count - 1)
        while left <= right {
            let mid = left + (right - left)/2
            if nums[mid] == target {
                result = [mid, mid]
                var (leftRight, rightLeft) = (mid, mid)
                
                while left < leftRight {
                    let midL = left + (leftRight - left)/2
                    if nums[midL] == target {
                        leftRight = midL
                    } else {
                        left = midL + 1
                    }
                }
                while rightLeft + 1 <= right {
                    let midR = (right + rightLeft + 1) / 2
                    if nums[midR] > target {
                        right = midR - 1
                    } else {
                        rightLeft = midR
                    }
                }
                result = [leftRight, rightLeft]
                return result
            } else if nums[mid] < target {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return result
    }
}
