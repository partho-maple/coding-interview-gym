import Foundation
class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        let numsSet = Set<Int>(nums)
        var maxSequence = 0
        for num in numsSet {
            if !numsSet.contains(num - 1) {
                var end = num
                while numsSet.contains(end + 1) {
                    end += 1
                }
                maxSequence = max(maxSequence, end - num + 1)
            }
        }
        return maxSequence
    }
}
