import Foundation
class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        var steps = k % nums.count
        if steps == 0 {
            return
        }
        nums.reverse()
        
        // Swap first portion
        var (left, right) = (0, steps - 1)
        while left < right {
            nums.swapAt(left, right)
            left += 1
            right -= 1
        }
        
        // Swap last portion
        (left, right) = (steps, nums.count - 1)
        while left < right {
            nums.swapAt(left, right)
            left += 1
            right -= 1
        }
    }
}

/*
 Input: nums = [1,2,3,4,5,6,7], k = 3
 Output: [5,6,7,1,2,3,4]
 
 
  1,2,3,4, 5,6,7
 
  1,2,3,4, 7,6,5
 
  7,6,5, 4,3,2,1
 
 
 
 >5,6,7, 1,2,3,4
 
 >5,6,7,1,2,3,4
*/
