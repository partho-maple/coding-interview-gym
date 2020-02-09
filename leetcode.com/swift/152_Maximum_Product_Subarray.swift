import Foundation

class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        var maxProd = 1
        var minProd = 1
        var best = nums[0]
        for i in 0 ..< nums.count {
            var currentNum = nums[i]
            if currentNum < 0 {
                swap(&maxProd, &minProd)
            }
            maxProd = max(maxProd * currentNum, currentNum)
            minProd = min(minProd * currentNum, currentNum)
            best = max(best, maxProd)
        }
        return best
    }
}