import Foundation

class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        guard nums.count > 0 else {
            return 0
        }
        var prefixSumCounter = [Int:Int]()
        prefixSumCounter[0] = 1
        var (subarrayCount, currentSum) = (0, 0)
        for num in nums {
            currentSum += num
            var prefixSum = currentSum - k
            if let count = prefixSumCounter[prefixSum] {
                subarrayCount += count
            }
            prefixSumCounter[currentSum, default: 0] += 1
        }
        return subarrayCount
    }
}
