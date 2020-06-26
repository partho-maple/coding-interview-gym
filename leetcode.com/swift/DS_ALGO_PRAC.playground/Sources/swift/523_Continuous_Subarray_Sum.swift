/*
// Initial solution. Time complexity: O(n^2)
import Foundation
class Solution {
    func checkSubarraySum(_ nums: [Int], _ k: Int) -> Bool {
        guard nums.count > 1 else {return false}
        
        for i in (0..<(nums.count) - 1) {
            var currentSum = nums[i]
            for j in ((i + 1)..<nums.count) {
                currentSum += nums[j]
                if k == 0 {
                    if currentSum == 0 {
                        print("1")
                        return true
                    } else {
                        continue
                    }
                } else if currentSum % abs(k) == 0 {
                    print("3")
                    return true
                }
            }
        }
        return false
    }
}
 */
